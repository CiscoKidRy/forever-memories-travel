# Forever Memories Travel

Private code store for the Forever Memories Travel website.

## Product

- Public website for a travel agency: descriptions, images, stories, and listings.
- Admin site with username and password sign-in so staff can update that content.
- In-site tools to take information from clients and track those contacts.

The Colorado trade name is Forever Memories Travel. The registrant on that filing is Forever Memories, LLC.

## Where it is served

Temporary access is `https://forevermemoriestravel.rshocking.com` (the same name as `ForeverMemoriesTravel.rshocking.com`). The apex `https://rshocking.com/` already hosts other content and stays as it is. On 2026-10-03 that apex returned the page titled "CO 2026 GOP Governor Primary — Live Results" through Cloudflare. Do not replace the apex, `www`, `belkin`, `belkinryan`, `ebay`, `mumble`, `spiritualgifts`, `ssh`, or `jefferypi-ssh`.

The logo on the site is the JPEG Jennifer Ramirez sent on 2026-10-03 from jenniferr@dreamstravelconsulting.com, subject "Thank you", body "The idea". Madison's "FMT Logo" message the same day has a larger PNG. That PNG was not copied into the repo because the mail download exceeded the tool size limit.

Production domain, after the cutover is explicitly approved: `forevermemoriestravel.com`.

Do not change nameservers or records for `forevermemoriestravel.com` until that approval. The lookalike name `forevermemroriestravel.com` is not registered.

## This repository

- Visibility: public, because GitHub's free plan will not serve Pages from a private repository. Do not commit client contact records, passwords, or admin credentials. When the contact database is built, that data stays out of this repository.
- The first pages are static HTML. Trip requests open an email to Jennifer Ramirez at jenniferr@dreamstravelconsulting.com. The admin sign-in and contact database are not built yet.
- DNS for this hostname is a CNAME to GitHub Pages. It does not point at the apex origin.

## Never commit

- Passwords, API tokens, private keys, or `.env` files
- Client contact exports or other personal data
- Cloudflare or registrar credentials
