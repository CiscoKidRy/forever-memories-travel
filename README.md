# Forever Memories Travel

Private code store for the Forever Memories Travel website.

## Product

- Public website for a travel agency: descriptions, images, stories, and listings.
- Admin site with username and password sign-in so staff can update that content.
- In-site tools to take information from clients and track those contacts.

The Colorado trade name is Forever Memories Travel. The registrant on that filing is Forever Memories, LLC.

## Where it is served

The public site is `https://forevermemoriestravel.com`. `https://www.forevermemoriestravel.com` is the www name for the same GitHub Pages site. The apex `https://rshocking.com/` already hosts other content and stays as it is. On 2026-10-03 that apex returned the page titled "CO 2026 GOP Governor Primary — Live Results" through Cloudflare. Do not replace the apex, `www`, `belkin`, `belkinryan`, `ebay`, `mumble`, `spiritualgifts`, `ssh`, or `jefferypi-ssh`.

The logo on the site is the JPEG Jennifer Ramirez sent on 2026-10-03 from jenniferr@dreamstravelconsulting.com, subject "Thank you", body "The idea". Madison's "FMT Logo" message the same day has a larger PNG. That PNG was not copied into the repo because the mail download exceeded the tool size limit.

Cutover to `forevermemoriestravel.com` was approved on 2026-10-13. The nameservers are Cloudflare (`apollo.ns.cloudflare.com` and `gabriella.ns.cloudflare.com`). The apex has GitHub Pages A and AAAA records, and `www` is a CNAME to `ciscokidry.github.io`. Those records are DNS only so GitHub can see its own addresses and issue the certificate. The MX and SPF records for DirectNIC hosting were left in place. The lookalike name `forevermemroriestravel.com` is not registered.

## This repository

- Visibility: public, because GitHub's free plan will not serve Pages from a private repository. Do not commit client contact records, passwords, or admin credentials. When the contact database is built, that data stays out of this repository.
- The first pages are static HTML. The trip form sends the request to Jennifer Ramirez at jenniferr@dreamstravelconsulting.com through FormSubmit, and FormSubmit copies ryanhocking@gmail.com. She must confirm that address once before delivery starts. The first time the copy address is used, FormSubmit may ask ryanhocking@gmail.com to confirm before those copies arrive. The admin sign-in and contact database are not built yet.
- DNS for `forevermemoriestravel.com` points at GitHub Pages. It does not point at the rshocking.com origin. `forevermemoriestravel.rshocking.com` was the earlier hostname.

## Never commit

- Passwords, API tokens, private keys, or `.env` files
- Client contact exports or other personal data
- Cloudflare or registrar credentials
