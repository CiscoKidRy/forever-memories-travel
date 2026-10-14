# Forever Memories Travel

Private code store for the Forever Memories Travel website.

## How to change this repository

Do not commit directly to `main`.

1. Create a new branch named `feat/<short-description>`.
2. Make the change on that branch.
3. Open a pull request that merges that branch into `main`.
4. Write a description of what changed. Put it in the pull request body. Say what changed and why. A title alone is not the description.
5. Merge only through that pull request.

This applies to every change, including documentation, site files, and generated content. It applies to people and to AI tools. The same instructions are in [AGENTS.md](AGENTS.md). GitHub starts a new pull request from [.github/pull_request_template.md](.github/pull_request_template.md). Fill that in.

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

Changes follow [How to change this repository](#how-to-change-this-repository) and [AGENTS.md](AGENTS.md). Every pull request needs a written description of what changed.

- Visibility: public, because GitHub's free plan will not serve Pages from a private repository. Do not commit client contact records, passwords, or admin credentials. When the contact database is built, that data stays out of this repository.
- The first pages are static HTML. The trip form posts to the inquiry API, which stores the request in Postgres and emails the visitor and ryanhocking@gmail.com. A successful save opens `thanks.html`. The button stays grey until that page opens. Nothing is sent to dreamstravelconsulting.com. The admin sign-in and contact database browser are not built yet.
- DNS for `forevermemoriestravel.com` points at GitHub Pages. It does not point at the rshocking.com origin. `forevermemoriestravel.rshocking.com` was the earlier hostname.

## Never commit

- Passwords, API tokens, private keys, or `.env` files
- Client contact exports or other personal data
- Cloudflare or registrar credentials
