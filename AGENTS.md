# Instructions for people and AI tools

Do not commit directly to `main`.

1. Create a new branch named `feat/<short-description>`.
2. Make the change on that branch.
3. Open a pull request that merges that branch into `main`.
4. Write a description of what changed. Put it in the pull request body. Say what changed and why. A title alone is not the description.
5. Merge only through that pull request.

This applies to every change in this repository, including documentation, site files, and generated content. Do not push fixes, reverts, or follow-up commits straight to `main`.

## Database

The inquiry database is described in [Documentation/DATA-DICTIONARY.md](Documentation/DATA-DICTIONARY.md). Any change to that database requires an update to the data dictionary in the same pull request. That includes tables, columns, types, defaults, constraints, indexes, triggers, functions, roles, and grants. Update [api/schema.sql](api/schema.sql) in that same pull request. Do not commit database rows or credentials.

The database is PostgreSQL database `forever_memories` on `hp-linux-plex-server`, listening on `127.0.0.1:5432` only. Public browsers reach the API through the Cloudflare Tunnel `forever-memories-inquiries` at `https://inquiries.forevermemoriestravel.com`. The setup is on the repository front page, [README.md](README.md).
