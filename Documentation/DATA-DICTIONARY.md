# Data dictionary

This file describes the Forever Memories Travel inquiry database. It was compared with the running database and with [api/schema.sql](../api/schema.sql) on 2026-10-14.

[api/schema.sql](../api/schema.sql) is the script that creates this database. This file is the description of what that database means. They must agree. The rows themselves are not in this repository.

## Database changes

Any change to the database requires an update to this data dictionary in the same pull request. The pull request is incomplete without that update.

A database change is any of these:

- A new, dropped, or renamed table, column, function, trigger, or role
- A change to a type, nullability, default, check, unique key, or primary key
- A new, dropped, or changed index
- A change to a function or trigger that changes what is stored, when a row is created, or who can read or write it
- A change to a role or a grant
- A new allowed value for a stored field, including a new trip label

Update [api/schema.sql](../api/schema.sql) in that same pull request. Apply the script on the laptop as the `postgres` superuser. GitHub Pages does not apply database changes. Merging this repository does not change the laptop database.

Do not commit inquiry rows, passwords, tunnel credentials, or the Cloudflare Email Sending token.

## Where the database is

| Item | Value |
| --- | --- |
| Machine | `hp-linux-plex-server`, the home Linux laptop |
| Operating system time zone | `America/Denver` |
| Engine | PostgreSQL 16.15, package `16.15-0ubuntu0.24.04.1` |
| Database name | `forever_memories` |
| Schema | `public` |
| Listen address | `127.0.0.1` port `5432` only |
| Service | `postgresql` |
| API listen address | `127.0.0.1` port `8787` only |
| API service | `forever-memories-inquiries` |
| API user | `fmtinq` |
| API code on the laptop | `/opt/forever-memories-inquiries` |
| API environment file | `/etc/forever-memories-inquiries.env`, mode `640`, owner `root:fmtinq` |

Postgres is not open to the home network or the internet. The API is not open to them either. A connection from another computer to port 5432 on this laptop is refused. The public path is the Cloudflare Tunnel described in the repository [README](../README.md#cloudflare-tunnel).

The API connects through the local Postgres socket. The connection string is in [api/.env.example](../api/.env.example):

```text
dbname=forever_memories user=fmtinq host=/var/run/postgresql
```

There is no database password in the repository. `fmtinq` is a peer-authenticated login for the operating-system user `fmtinq`.

## What is stored

One table, `public.inquiries`, holds every accepted trip request. The honeypot field `company` is not a column. A non-empty honeypot is rejected and nothing is written.

The server sets `submitted_at`. The form cannot choose it. A `BEFORE INSERT` trigger, `inquiries_stamp_submitted_at`, sets `submitted_at` to `clock_timestamp()` on every insert. The column default is the same function, and the trigger replaces that value as well.

| Column | Type | Null | Default | Form JSON field | Meaning |
| --- | --- | --- | --- | --- | --- |
| `id` | `uuid` | no | `gen_random_uuid()` | returned as `id` | Primary key. The confirmation page shows this as the reference. |
| `submitted_at` | `timestamptz` | no | `clock_timestamp()` | none | Server receipt time. The trigger overwrites it on insert. Stored as an absolute time. The laptop zone is `America/Denver`. |
| `idempotency_key` | `uuid` | no | | `idempotency_key` | Identifies one browser attempt. Unique. |
| `payload_fingerprint` | `text` | no | | computed | 64-character lowercase hex SHA-256 of the normalized request. |
| `source_url` | `text` | no | | `source_url` | Site page that sent the request. Origin and path only. |
| `name` | `text` | no | | `name` | Visitor name, trimmed. |
| `email` | `text` | no | | `email` | Visitor email, trimmed and lowercased. |
| `phone` | `text` | yes | | `phone` | Phone. Empty input is stored as null. |
| `trip` | `text` | no | | `trip` | One of the five trip labels below. |
| `travel_when` | `text` | yes | | `when` | When the visitor wants to travel. Free text, not a date. Empty input is stored as null. |
| `party` | `text` | yes | | `who` | Who is going. Empty input is stored as null. |
| `notes` | `text` | yes | | `notes` | Free notes. Empty input is stored as null. |
| `client_ip` | `inet` | no | | none | Client address from `CF-Connecting-IP` when that header is present, otherwise the socket peer. |
| `visitor_email_status` | `text` | no | `pending` | none | Delivery state of the visitor's confirmation email. |
| `ryan_email_status` | `text` | no | `pending` | none | Delivery state of the agency notice. `sent` only when both `ryanhocking@gmail.com` and `jennifer@forevermemoriestravel.com` were accepted. `failed` when either send fails. |
| `status` | `text` | no | `new` | none | Staff progress. `new`, `contacted`, `planning`, `booked`, `closed`, or `spam`. Existing rows stay `new` when the column is added. |
| `staff_notes` | `text` | yes | | none | Copy of the newest `inquiry_staff_notes` row whose `deleted_at` is null. Null when that inquiry has no such row. Not published. |
| `staff_updated_at` | `timestamptz` | yes | | none | `created_at` of that same row. Null when `staff_notes` is null. A status-only save does not change it. |

`client_ip` is trusted from `CF-Connecting-IP` because the API port is localhost and `cloudflared` is the process that sets the header.

## Constraints

| Name | Rule |
| --- | --- |
| `inquiries_pkey` | `id` is the primary key. |
| `inquiries_idempotency_key_key` | `idempotency_key` is unique. |
| `inquiries_fingerprint_hex` | `payload_fingerprint` matches `^[0-9a-f]{64}$`. |
| `inquiries_name` | Trimmed, length 1 to 200. |
| `inquiries_email` | Lowercased and trimmed, length 3 to 254, and matches one `@` with a dot in the domain. |
| `inquiries_phone` | Null, or trimmed with length 1 to 40. |
| `inquiries_trip` | `Family vacation`, `Theme park`, `Cruise`, `International`, or `Not sure yet`. |
| `inquiries_travel_when` | Null, or trimmed with length 1 to 300. |
| `inquiries_party` | Null, or trimmed with length 1 to 400. |
| `inquiries_notes` | Null, or trimmed with length 1 to 4000. |
| `inquiries_source_url` | Length 1 to 500, and matches `https://forevermemoriestravel.com` or `https://www.forevermemoriestravel.com`, with an optional path. |
| `inquiries_visitor_email_status` | `pending`, `sent`, or `failed`. |
| `inquiries_ryan_email_status` | `pending`, `sent`, or `failed`. |
| `inquiries_status` | `new`, `contacted`, `planning`, `booked`, `closed`, or `spam`. |
| `inquiries_staff_notes` | Null, or trimmed with length 1 to 4000. |

## Indexes

| Name | Columns |
| --- | --- |
| `inquiries_pkey` | `id` |
| `inquiries_idempotency_key_key` | `idempotency_key` unique |
| `inquiries_submitted_at_idx` | `submitted_at` descending |
| `inquiries_fingerprint_submitted_idx` | `payload_fingerprint`, `submitted_at` descending |
| `inquiries_client_ip_submitted_idx` | `client_ip`, `submitted_at` descending |
| `inquiries_status_submitted_idx` | `status`, `submitted_at` descending |

## When a row is created

`submit_inquiry` is the only insert path used by the API. It is `SECURITY DEFINER`, owned by `postgres`, with `search_path` set to `public`.

The fingerprint is the hex SHA-256 of these values joined by ASCII unit separator `chr(31)`, in this order: trimmed name, lowercased email, phone or empty, trimmed trip, travel time or empty, party or empty, notes or empty, and trimmed source URL. `pgcrypto` provides `digest`. The extension installed in this database is `pgcrypto` 1.3.

The function then does this:

1. Rejects a null idempotency key or a null client address.
2. If that idempotency key already exists and the fingerprint matches, it returns the existing row and `created` is false.
3. If that idempotency key already exists and the fingerprint differs, it raises `idempotency_conflict`. The API returns HTTP 409. Nothing new is stored.
4. If a different key has the same fingerprint and `submitted_at` is within the last 2 minutes, it returns that existing row and `created` is false.
5. After 2 minutes, the same words are a new row.
6. If this client address already has 5 inserted rows in the last hour, it raises `rate_limited`. The API returns HTTP 429. A replay that returns an existing row does not count toward the 5.
7. Otherwise it inserts one row. `created` is true. Both email statuses start as `pending`.

The function returns `inquiry_id`, `inquiry_submitted_at`, `created`, `out_visitor_email`, and `out_ryan_email`. Those names are the function result. They are not columns.

The API sends the visitor email and the agency notice only when `created` is true. A replay does not send again. The row is kept when email fails. The messages are sent by Cloudflare Email Sending as Forever Memories Travel `<donotreply@forevermemoriestravel.com>`, with `reply_to` set to `ryanhocking@gmail.com`. `MAIL_DISABLED=1` turns sending off. The visitor subject is `We have your trip request` and that message goes to the visitor. The notice subject is `Trip request — Forever Memories Travel`. That notice is sent to `ryanhocking@gmail.com` and to `jennifer@forevermemoriestravel.com`. `ryan_email_status` is `sent` only when both of those sends are accepted. If either send fails, it is `failed`, including when `MAIL_DISABLED=1`. A message to `jennifer@forevermemoriestravel.com` counts toward the Email Sending allowance. A message to `ryanhocking@gmail.com` does not.

## Email status

`mark_inquiry_email(p_id uuid, p_which text, p_status text)` updates one status column. `p_which` is `visitor` or `ryan`. `p_status` is `sent` or `failed`. It does not change a column that is already `sent`. It is `SECURITY DEFINER`, owned by `postgres`.

The API calls this function after each delivery attempt. `fmtinq` has no `UPDATE` grant on the table, so this function is the only way the API records delivery.

## Roles and grants

| Role | Access |
| --- | --- |
| `postgres` | Owns `inquiries`, the trigger function, `submit_inquiry`, and `mark_inquiry_email`. Also owns `inquiry_staff_notes` and the five functions named in Staff functions. Used to apply the schema and to delete test rows. |
| `fmtinq` | `EXECUTE` on `submit_inquiry` and `mark_inquiry_email` only. No select, insert, update, or delete on `inquiries`. No execute on the staff functions. |
| `fmtstaff` | `EXECUTE` on `list_inquiries`, `get_inquiry`, `update_inquiry_staff`, `list_staff_notes`, and `delete_staff_note`. No execute on `purge_expired_staff_notes` or `refresh_inquiry_staff_summary`. No select, insert, update, or delete on `inquiry_staff_notes`. No table privileges on `inquiries`. Login role, peer authentication, no password. |
| `ryanhocking` | `SELECT` on `inquiries` through peer authentication as the operating-system user. |
| `public` | All privileges revoked on `inquiries`, `submit_inquiry`, `mark_inquiry_email`, `inquiries_stamp_submitted_at`, and the staff functions. No execute on `list_staff_notes`, `delete_staff_note`, `update_inquiry_staff`, `purge_expired_staff_notes`, or `refresh_inquiry_staff_summary`. No select on `inquiry_staff_notes`. |

`fmtinq` and `ryanhocking` are login roles. The schema script creates a missing role. It does not set a password.

## Trigger

`inquiries_stamp_submitted_at` runs `BEFORE INSERT` on each row and calls `inquiries_stamp_submitted_at()`. The function sets `NEW.submitted_at` to `clock_timestamp()` and returns the row. There is no update or delete trigger.

## Staff functions

`api/staff.sql` adds `status`, `staff_notes`, and `staff_updated_at`, plus three functions. It does not replace `submit_inquiry` or `mark_inquiry_email`. That file was applied on the laptop on 14 October 2026. Do not apply it again. Do not run all of `schema.sql` against the live database.

`list_inquiries(p_status text, p_limit integer)` returns at most 100 rows, newest first. A null status returns every status. It omits `client_ip`, `idempotency_key`, and `payload_fingerprint`.

`get_inquiry(p_id uuid)` returns one row with the same omissions, or no row.

`update_inquiry_staff(p_id uuid, p_status text, p_staff_notes text, p_author text)` writes `status`. A non-blank trimmed note is inserted into `inquiry_staff_notes` with `created_by` set to `p_author`. That author must be lowercase, trimmed, 3 to 254 characters, with no spaces, one `@`, and a dot in the domain. A note that is empty or only whitespace, including newlines, does not insert a row, does not read the author, and does not delete an older row. `btrim` removes spaces only, so the function also treats a value that does not match `[^[:space:]]` as blank. The function then sets `staff_notes` and `staff_updated_at` from the newest note whose `deleted_at` is null. Email statuses stay unchanged. The older three-argument function is dropped by `api/staff-note-author.sql`.

`inquiry_staff_notes` stores one row per saved staff note.

| Column | Type | Null | Default |
| --- | --- | --- | --- |
| `id` | `uuid` | no | `gen_random_uuid()` |
| `inquiry_id` | `uuid` | no | |
| `body` | `text` | no | |
| `created_at` | `timestamptz` | no | `clock_timestamp()` |
| `deleted_at` | `timestamptz` | yes | |
| `created_by` | `text` | yes | |

`inquiry_staff_notes_pkey` is the primary key on `id`. `inquiry_staff_notes_inquiry_id_fkey` references `inquiries(id)` and deletes the note rows when the inquiry is deleted. `inquiry_staff_notes_body` requires `body` to be trimmed and between 1 and 4000 characters. `inquiry_staff_notes_created_by` allows null. A non-null value is lowercase, trimmed, 3 to 254 characters, and matches one `@` with a dot in the domain. `inquiry_staff_notes_inquiry_idx` is a btree on (`inquiry_id`, `created_at` descending). The table owner is `postgres`. A note saved before `created_by` existed stays null. The screen shows an em dash for that null. It does not invent a username.

`delete_staff_note` sets `deleted_at` to `clock_timestamp()` and does not change `deleted_at` if it is already set. `purge_expired_staff_notes` deletes every note row whose `deleted_at` is not null and is at or before `clock_timestamp() - interval '48 hours'`. On this database, `interval '48 hours'` is 172800 seconds. `interval '2 days'` is not the same across a daylight-saving change: adding it to 2026-10-31 10:00-06 measured 176400 seconds, and adding it to 2026-03-07 10:00-07 measured 169200 seconds. The purge does not use local midnight. `list_staff_notes`, `delete_staff_note`, and `update_inquiry_staff` call that purge before they finish. `list_staff_notes` then returns the one inquiry's remaining rows, including `created_by` and rows still inside the 48 hours, newest `created_at` first. `GET /staff/inquiries` does not call the purge. `GET /staff/inquiries/{id}`, `PATCH /staff/inquiries/{id}`, and `DELETE /staff/inquiries/{id}/notes/{note_id}` do. There is no scheduled job. `fmtstaff` can execute `list_staff_notes`, `delete_staff_note`, and `update_inquiry_staff`. `purge_expired_staff_notes` and `refresh_inquiry_staff_summary` are not granted to `fmtstaff`.

`api/staff-notes.sql` is the change that created this table. `api/staff-note-author.sql` adds `created_by` and replaces `list_staff_notes` and `update_inquiry_staff`. Apply that author file once. Do not apply `api/staff.sql` again. Do not apply `api/staff-notes.sql` again. Do not run all of `schema.sql` against the live database. The author file has no backfill insert.

The staff API is `api/staff_api.py`, systemd unit `forever-memories-staff`, user `fmtstaff`, listen `127.0.0.1:8788`. `GET /staff/inquiries/{id}` adds `staff_note_entries`. `DELETE /staff/inquiries/{id}/notes/{note_id}` soft-deletes one note and returns the inquiry. It requires `Authorization: Bearer`. The public inquiry process on port 8787 does not call these functions. The bearer is stored in `/etc/forever-memories-staff.env` and is not in git.
