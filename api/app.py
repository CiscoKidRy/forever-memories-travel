"""Local inquiry API for Forever Memories Travel.

Listens on localhost. Cloudflare Tunnel is the public door.
The database password is not in this file.
"""

import json
import os
import re
import smtplib
import traceback
from datetime import datetime
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from ipaddress import ip_address
from zoneinfo import ZoneInfo

import psycopg

ALLOWED_ORIGINS = {
    "https://forevermemoriestravel.com",
    "https://www.forevermemoriestravel.com",
}
TRIPS = {
    "Family vacation",
    "Theme park",
    "Cruise",
    "International",
    "Not sure yet",
}
SOURCE_URL = re.compile(
    r"^https://(www\.)?forevermemoriestravel\.com(/[^\s]*)?$"
)
EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
UUID = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.IGNORECASE,
)
LIMITS = {
    "name": 200,
    "email": 254,
    "phone": 40,
    "when": 300,
    "who": 400,
    "notes": 4000,
}
DENVER = ZoneInfo("America/Denver")
MAX_BODY = 32_000


def database_url():
    url = os.environ.get("DATABASE_URL", "").strip()
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    return url


def clean(value, limit, required):
    if value is None:
        text = ""
    elif not isinstance(value, str):
        raise ValueError("invalid")
    else:
        text = value.strip()
    if len(text) > limit:
        raise ValueError("too_long")
    if required and not text:
        raise ValueError("required")
    return text


def validate(payload):
    if not isinstance(payload, dict):
        raise ValueError("invalid")
    company = payload.get("company")
    if isinstance(company, str) and company.strip():
        return {"honeypot": True}
    name = clean(payload.get("name"), LIMITS["name"], True)
    email = clean(payload.get("email"), LIMITS["email"], True).lower()
    if not EMAIL.match(email):
        raise ValueError("email")
    phone = clean(payload.get("phone"), LIMITS["phone"], False)
    trip = clean(payload.get("trip"), 40, True)
    if trip not in TRIPS:
        raise ValueError("trip")
    travel_when = clean(payload.get("when"), LIMITS["when"], False)
    party = clean(payload.get("who"), LIMITS["who"], False)
    notes = clean(payload.get("notes"), LIMITS["notes"], False)
    source = clean(payload.get("source_url"), 500, True)
    if not SOURCE_URL.match(source):
        raise ValueError("source")
    key = clean(payload.get("idempotency_key"), 36, True).lower()
    if not UUID.match(key):
        raise ValueError("key")
    return {
        "honeypot": False,
        "name": name,
        "email": email,
        "phone": phone,
        "trip": trip,
        "when": travel_when,
        "who": party,
        "notes": notes,
        "source_url": source,
        "idempotency_key": key,
    }


def client_ip(headers, peer):
    forwarded = headers.get("CF-Connecting-IP") or headers.get("Cf-Connecting-Ip")
    if forwarded:
        try:
            return str(ip_address(forwarded.strip()))
        except ValueError:
            pass
    host = peer[0] if isinstance(peer, tuple) else peer
    if host.startswith("::ffff:"):
        host = host[7:]
    return str(ip_address(host))


def submit(fields, address):
    with psycopg.connect(database_url()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select inquiry_id, inquiry_submitted_at, created,
                       out_visitor_email, out_ryan_email
                from submit_inquiry(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    fields["idempotency_key"],
                    fields["source_url"],
                    fields["name"],
                    fields["email"],
                    fields["phone"],
                    fields["trip"],
                    fields["when"],
                    fields["who"],
                    fields["notes"],
                    address,
                ),
            )
            row = cur.fetchone()
        conn.commit()
    return {
        "id": str(row[0]),
        "submitted_at": row[1],
        "created": bool(row[2]),
        "visitor_email": row[3],
        "ryan_email": row[4],
    }


def mark_email(inquiry_id, which, status):
    with psycopg.connect(database_url()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "select mark_inquiry_email(%s, %s, %s)",
                (inquiry_id, which, status),
            )
        conn.commit()


def format_when(moment):
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=ZoneInfo("UTC"))
    return moment.astimezone(DENVER).strftime("%B %-d, %Y at %-I:%M %p %Z")


class MailOff(Exception):
    pass


def send_mail(recipient, subject, body):
    if os.environ.get("MAIL_DISABLED", "").strip() == "1":
        raise MailOff()
    sender = os.environ.get("GMAIL_ADDRESS", "").strip()
    password = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
    if not sender or not password:
        raise RuntimeError("mail is not configured")
    message = EmailMessage()
    message["From"] = f"Forever Memories Travel <{sender}>"
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)


def deliver(fields, stored):
    if not stored["created"]:
        return stored["visitor_email"], stored["ryan_email"]
    when = format_when(stored["submitted_at"])
    visitor_status = "failed"
    ryan_status = "failed"
    try:
        send_mail(
            fields["email"],
            "We have your trip request",
            "\n".join([
                f"Hello {fields['name']},",
                "",
                "Forever Memories Travel has your trip request.",
                f"Reference: {stored['id']}",
                f"Received: {when}",
                f"Trip: {fields['trip']}",
                "",
                "We will reply to this email address.",
            ]),
        )
        visitor_status = "sent"
    except MailOff:
        visitor_status = "failed"
    except Exception:
        traceback.print_exc()
    try:
        details = [
            "New trip request",
            f"Reference: {stored['id']}",
            f"Received: {when}",
            f"Name: {fields['name']}",
            f"Email: {fields['email']}",
            f"Phone: {fields['phone'] or '(none)'}",
            f"Trip: {fields['trip']}",
            f"When: {fields['when'] or '(none)'}",
            f"Who: {fields['who'] or '(none)'}",
            f"Notes: {fields['notes'] or '(none)'}",
            f"Page: {fields['source_url']}",
        ]
        send_mail(
            os.environ.get("GMAIL_ADDRESS", "ryanhocking@gmail.com").strip(),
            "Trip request — Forever Memories Travel",
            "\n".join(details),
        )
        ryan_status = "sent"
    except MailOff:
        ryan_status = "failed"
    except Exception:
        traceback.print_exc()
    try:
        mark_email(stored["id"], "visitor", visitor_status)
        mark_email(stored["id"], "ryan", ryan_status)
    except Exception:
        traceback.print_exc()
    return visitor_status, ryan_status


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} {fmt % args}", flush=True)

    def handle_error(self, request, client_address):
        traceback.print_exc()

    def _cors(self):
        origin = self.headers.get("Origin", "")
        if origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Accept")

    def _send(self, status, payload=None):
        body = b""
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self._cors()
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        if self.path.split("?", 1)[0] != "/inquiries":
            self._send(404, {"error": "not_found"})
            return
        self.send_response(204)
        self._cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if self.path.split("?", 1)[0] != "/health":
            self._send(404, {"error": "not_found"})
            return
        try:
            with psycopg.connect(database_url()) as conn:
                with conn.cursor() as cur:
                    cur.execute("select 1")
                    cur.fetchone()
        except Exception:
            traceback.print_exc()
            self._send(503, {"ok": False})
            return
        self._send(200, {"ok": True})

    def do_POST(self):
        if self.path.split("?", 1)[0] != "/inquiries":
            self._send(404, {"error": "not_found"})
            return
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length <= 0 or length > MAX_BODY:
            self._send(400, {"error": "invalid"})
            return
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
            fields = validate(payload)
        except (ValueError, UnicodeError, json.JSONDecodeError):
            self._send(400, {"error": "invalid"})
            return
        if fields["honeypot"]:
            self._send(400, {"error": "invalid"})
            return
        try:
            address = client_ip(self.headers, self.client_address)
        except ValueError:
            self._send(400, {"error": "invalid"})
            return
        try:
            stored = submit(fields, address)
        except psycopg.Error as exc:
            message = str(exc).splitlines()[0]
            if "rate_limited" in message:
                self._send(429, {"error": "rate_limited"})
                return
            if "idempotency_conflict" in message:
                self._send(409, {"error": "conflict"})
                return
            traceback.print_exc()
            self._send(400, {"error": "invalid"})
            return
        except Exception:
            traceback.print_exc()
            self._send(503, {"error": "unavailable"})
            return
        visitor_status, ryan_status = deliver(fields, stored)
        self._send(201, {
            "id": stored["id"],
            "submitted_at": stored["submitted_at"].isoformat(),
            "visitor_email": visitor_status,
            "ryan_email": ryan_status,
        })


def main():
    host = os.environ.get("BIND", "127.0.0.1")
    port = int(os.environ.get("PORT", "8787"))
    if host not in {"127.0.0.1", "::1"}:
        raise RuntimeError("BIND must stay on localhost")
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"listening on {host}:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
