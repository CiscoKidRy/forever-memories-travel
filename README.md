# Forever Memories Travel

Private code store for the Forever Memories Travel website.

## Product

- Public website for a travel agency: descriptions, images, stories, and listings.
- Admin site with username and password sign-in so staff can update that content.
- In-site tools to take information from clients and track those contacts.

The Colorado trade name is Forever Memories Travel. The registrant on that filing is Forever Memories, LLC.

## Where it is served

Temporary access is a hostname under `rshocking.com`. The apex `https://rshocking.com/` already hosts other content and stays as it is. On 2026-10-03 that apex returned the page titled "CO 2026 GOP Governor Primary — Live Results" through Cloudflare. `www.rshocking.com`, `belkin.rshocking.com`, and `ssh.rshocking.com` also resolved. Do not replace those names.

On that same date, `fmt.rshocking.com`, `travel.rshocking.com`, `forever.rshocking.com`, and `memories.rshocking.com` had no A or CNAME records. The temporary portal hostname is not chosen yet. No DNS record has been created for this project.

Production domain, after the cutover is explicitly approved: `forevermemoriestravel.com`.

Do not change nameservers or records for `forevermemoriestravel.com` until that approval. The lookalike name `forevermemroriestravel.com` is not registered.

## This repository

- Visibility: private. Client contact records do not belong in git.
- No application stack is selected in this first commit.
- No deploy and no DNS change are included.

## Never commit

- Passwords, API tokens, private keys, or `.env` files
- Client contact exports or other personal data
- Cloudflare or registrar credentials
