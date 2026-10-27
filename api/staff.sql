-- Additive staff fields and functions for the existing inquiries table.
-- Do not replace submit_inquiry or mark_inquiry_email.
-- Apply this file once as the table owner. Do not run schema.sql against the live database.

alter table public.inquiries
  add column if not exists status text not null default 'new',
  add column if not exists staff_notes text,
  add column if not exists staff_updated_at timestamptz;

alter table public.inquiries
  drop constraint if exists inquiries_status,
  add constraint inquiries_status
    check (status in ('new', 'contacted', 'planning', 'booked', 'closed', 'spam'));

alter table public.inquiries
  drop constraint if exists inquiries_staff_notes,
  add constraint inquiries_staff_notes
    check (staff_notes is null
      or (staff_notes = btrim(staff_notes)
          and char_length(staff_notes) between 1 and 4000));

create index if not exists inquiries_status_submitted_idx
  on public.inquiries (status, submitted_at desc);

do $$
begin
  if not exists (select 1 from pg_roles where rolname = 'fmtstaff') then
    create role fmtstaff login;
  end if;
end $$;

create or replace function list_inquiries(p_status text, p_limit integer)
returns table (
  id uuid,
  submitted_at timestamptz,
  name text,
  email text,
  phone text,
  trip text,
  travel_when text,
  party text,
  notes text,
  visitor_email_status text,
  ryan_email_status text,
  status text,
  staff_notes text,
  staff_updated_at timestamptz
)
language plpgsql
security definer
set search_path = public
as $$
declare
  lim integer;
begin
  lim := least(coalesce(p_limit, 100), 100);
  if lim < 1 then
    lim := 1;
  end if;
  if p_status is not null and p_status not in (
    'new', 'contacted', 'planning', 'booked', 'closed', 'spam'
  ) then
    raise exception 'bad_status' using errcode = 'P0001';
  end if;
  return query
  select i.id, i.submitted_at, i.name, i.email, i.phone, i.trip,
         i.travel_when, i.party, i.notes, i.visitor_email_status,
         i.ryan_email_status, i.status, i.staff_notes, i.staff_updated_at
  from inquiries i
  where p_status is null or i.status = p_status
  order by i.submitted_at desc
  limit lim;
end;
$$;

create or replace function get_inquiry(p_id uuid)
returns table (
  id uuid,
  submitted_at timestamptz,
  name text,
  email text,
  phone text,
  trip text,
  travel_when text,
  party text,
  notes text,
  visitor_email_status text,
  ryan_email_status text,
  status text,
  staff_notes text,
  staff_updated_at timestamptz
)
language plpgsql
security definer
set search_path = public
as $$
begin
  return query
  select i.id, i.submitted_at, i.name, i.email, i.phone, i.trip,
         i.travel_when, i.party, i.notes, i.visitor_email_status,
         i.ryan_email_status, i.status, i.staff_notes, i.staff_updated_at
  from inquiries i
  where i.id = p_id;
end;
$$;

create or replace function update_inquiry_staff(
  p_id uuid,
  p_status text,
  p_staff_notes text
) returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  clean_notes text;
begin
  if p_status not in ('new', 'contacted', 'planning', 'booked', 'closed', 'spam') then
    raise exception 'bad_status' using errcode = 'P0001';
  end if;
  clean_notes := nullif(btrim(coalesce(p_staff_notes, '')), '');
  if clean_notes is not null and char_length(clean_notes) > 4000 then
    raise exception 'notes_too_long' using errcode = 'P0001';
  end if;
  update inquiries
  set status = p_status,
      staff_notes = clean_notes,
      staff_updated_at = clock_timestamp()
  where inquiries.id = p_id;
  if not found then
    raise exception 'not_found' using errcode = 'P0001';
  end if;
end;
$$;

revoke all on function list_inquiries(text, integer) from public;
revoke all on function get_inquiry(uuid) from public;
revoke all on function update_inquiry_staff(uuid, text, text) from public;

grant execute on function list_inquiries(text, integer) to fmtstaff;
grant execute on function get_inquiry(uuid) to fmtstaff;
grant execute on function update_inquiry_staff(uuid, text, text) to fmtstaff;
