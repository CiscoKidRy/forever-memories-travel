# Inquiry API

This process runs on the home Linux laptop and listens on `127.0.0.1:8787`. Cloudflare Tunnel publishes it as `https://inquiries.forevermemoriestravel.com`. GitHub Pages cannot reach the laptop, and Postgres is not open to the network.

The service account is `fmtinq`. It may execute `submit_inquiry` and `mark_inquiry_email`. It cannot select, update, or delete rows. The OS user `ryanhocking` can select rows through peer authentication.

The database is `forever_memories` on `hp-linux-plex-server`. PostgreSQL listens on `127.0.0.1:5432` only. The column-by-column description is [Documentation/DATA-DICTIONARY.md](../Documentation/DATA-DICTIONARY.md). Any change to the database requires that data dictionary to be updated in the same pull request.

Secrets stay in `/etc/forever-memories-inquiries.env` on the laptop. Do not commit that file.

Apply `schema.sql` as the Postgres superuser. Run `test_inquiries.py` with `DATABASE_URL` pointing at the local database as a role that can delete test rows.
