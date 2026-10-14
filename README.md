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

A change to the inquiry database has one more requirement. Update [Documentation/DATA-DICTIONARY.md](Documentation/DATA-DICTIONARY.md) in the same pull request. The database location and the Cloudflare Tunnel in front of it are described below.

## Google tag

Public HTML pages on `forevermemoriestravel.com` use one Google tag. The measurement ID is `G-GYBCCKG2FJ`. The property, the stream, the key events, and the lead parameters are recorded in [Documentation/GOOGLE-TAG.md](Documentation/GOOGLE-TAG.md). A change to tagging updates that file in the same pull request.

Handle tagging this way on this site and on any new public site created for this domain:

1. Put the Google tag snippet first inside `<head>`. Use one snippet per page. The snippet is in [Documentation/GOOGLE-TAG.md](Documentation/GOOGLE-TAG.md).
2. Use measurement ID `G-GYBCCKG2FJ` for every public page and every new hostname on `forevermemoriestravel.com`. `www` already serves these same files. Do not create a second Analytics property, a second web stream, or a second measurement ID for this domain.
3. Do not add a Google Tag Manager container. A container id starts with `GTM-`. The `googletagmanager.com` address in the snippet is the loader for this Google tag.
4. Do not send a name, email address, phone number, note, or record id to Google. A confirmation address that contains an id uses `page_location: location.origin + location.pathname`, as [thanks.html](thanks.html) does.
5. Send `generate_lead` only after the server has stored the request. This site does that in [site.js](site.js) after the inquiry API returns HTTP 201 with an id. The parameters are `lead_source` `trip_form` and, for a chosen trip kind, `trip_type` of `family`, `park`, `cruise`, or `international`. A new form adds its `lead_source` value to the documentation in the same pull request.
6. Keep the footer privacy notice. It states the Analytics collection and who receives the trip request. If the form changes, change that sentence in the same pull request.
7. Leave the default `purchase` key event in place. Google will not delete it. Do not send a `purchase` event.
8. Do not put the tag on `inquiries.forevermemoriestravel.com`. That hostname is the API.

## Search

The home page is written so a person can tell this is a Colorado Springs travel agency that plans a cruise, a Disney vacation, or an Orlando trip. The words stay inside normal sentences. The record of what was rejected, which social profiles are not this agency, how `robots.txt` and the sitemap work, and what the 14 October 2026 SEOptimer audit changed or left alone is [Documentation/SEO.md](Documentation/SEO.md). [llms.txt](llms.txt) repeats the public facts and says the site lists no street address, phone number, or social profile.

A later edit keeps those five ideas on the home page and updates that file in the same pull request. `thanks.html` stays out of the search index. Do not add a link to another business with a similar name. Add a social link only when Ryan confirms the profile is this agency.

## Inquiry database

Trip requests are stored in PostgreSQL on the home Linux laptop `hp-linux-plex-server`. The database name is `forever_memories`. PostgreSQL 16 listens only on `127.0.0.1:5432`. The inquiry API listens only on `127.0.0.1:8787`. Neither port is open to the home network or the internet. GitHub Pages cannot connect to the laptop.

The data dictionary is [Documentation/DATA-DICTIONARY.md](Documentation/DATA-DICTIONARY.md). It lists the table, every column, the constraints, the indexes, the functions, and the roles. Any change to the database requires that file to be updated in the same pull request. Changing [api/schema.sql](api/schema.sql) without updating the dictionary is incomplete. Inquiry rows stay on the laptop. Do not commit them.

The running API is the `forever-memories-inquiries` service, under the `fmtinq` user, with its code in `/opt/forever-memories-inquiries`. Secrets stay in `/etc/forever-memories-inquiries.env` on the laptop. The sample variable names are in [api/.env.example](api/.env.example). Publishing this repository does not apply a schema change. Apply [api/schema.sql](api/schema.sql) on the laptop as the Postgres superuser.

### Cloudflare Tunnel

Public browsers reach the API through a Cloudflare Tunnel. There is no router port forward.

| Item | Value |
| --- | --- |
| Public API | `https://inquiries.forevermemoriestravel.com` |
| Form endpoint | `POST https://inquiries.forevermemoriestravel.com/inquiries` |
| Health check | `GET https://inquiries.forevermemoriestravel.com/health` |
| Zone | `forevermemoriestravel.com`, Cloudflare zone `d8abd6e253f3f4f48ae4a3f38daa2b70` |
| DNS record | Proxied CNAME `inquiries.forevermemoriestravel.com` to `d0dd55a4-e1fa-49b1-a9ba-75e6e133dc1d.cfargotunnel.com` |
| Tunnel name | `forever-memories-inquiries` |
| Tunnel ID | `d0dd55a4-e1fa-49b1-a9ba-75e6e133dc1d` |
| Connector | `cloudflared` on `hp-linux-plex-server`, systemd unit `cloudflared` |
| Config file | `/etc/cloudflared/config.yml` |
| Ingress | `inquiries.forevermemoriestravel.com` goes to `http://127.0.0.1:8787` |
| Other names | HTTP 404 |
| Credential file | `/etc/cloudflared/d0dd55a4-e1fa-49b1-a9ba-75e6e133dc1d.json`, mode `600`, owner `root` |

The credential file is not in this repository. Do not commit it.

The apex `forevermemoriestravel.com` and `www` stay DNS-only and point at GitHub Pages. The apex MX and the existing apex SPF TXT records stay on DirectNIC. Email Sending uses separate records on `cf-bounce`, recorded in [Documentation/EMAIL-SENDING.md](Documentation/EMAIL-SENDING.md). Do not point the apex, `www`, or mail records at this tunnel. Do not reuse the other Cloudflare tunnels that terminate SSH for other machines.

The send button turns grey and stays disabled while the request is in flight. `thanks.html` opens only after the API accepts the row. If the laptop or the tunnel is down, the form stays on the page and does not say the request was saved. Nothing is sent to dreamstravelconsulting.com.

Trip mail is sent by Cloudflare Email Sending. The From address is Forever Memories Travel `<donotreply@forevermemoriestravel.com>`. That address is not a mailbox. Replies are directed to `ryanhocking@gmail.com`. The visitor message uses the subject `We have your trip request`. The lead notice uses the subject `Trip request — Forever Memories Travel` and goes to `ryanhocking@gmail.com`. `MAIL_DISABLED=1` turns sending off. Workers Paid includes 3,000 counted Email Sending messages per account per month, then $0.35 per 1,000. The limits API also reports 200 per day. A message to `ryanhocking@gmail.com` does not count. A message to a visitor does.

## Product

- Public website for a travel agency: descriptions, images, stories, and listings.
- Admin site with username and password sign-in so staff can update that content.
- In-site tools to take information from clients and track those contacts.

The Colorado trade name is Forever Memories Travel. The registrant on that filing is Forever Memories, LLC.

## Where it is served

The public site is `https://forevermemoriestravel.com`. `https://www.forevermemoriestravel.com` is the www name for the same GitHub Pages site. The apex `https://rshocking.com/` already hosts other content and stays as it is. On 2026-10-03 that apex returned the page titled "CO 2026 GOP Governor Primary — Live Results" through Cloudflare. Do not replace the apex, `www`, `belkin`, `belkinryan`, `ebay`, `mumble`, `spiritualgifts`, `ssh`, or `jefferypi-ssh`.

The logo on the site is the JPEG Jennifer Ramirez sent on 2026-10-03 from jenniferr@dreamstravelconsulting.com, subject "Thank you", body "The idea". Madison's "FMT Logo" message the same day has a larger PNG. That PNG was not copied into the repo because the mail download exceeded the tool size limit.

Cutover to `forevermemoriestravel.com` was approved on 2026-10-13. The nameservers are Cloudflare (`apollo.ns.cloudflare.com` and `gabriella.ns.cloudflare.com`). The apex has GitHub Pages A and AAAA records, and `www` is a CNAME to `ciscokidry.github.io`. Those records are DNS only so GitHub can see its own addresses and issue the certificate. The apex MX and the existing apex SPF TXT records for DirectNIC hosting were left in place. Email Sending was added later on `cf-bounce`. The record is [Documentation/EMAIL-SENDING.md](Documentation/EMAIL-SENDING.md). The lookalike name `forevermemroriestravel.com` is not registered.

## This repository

Changes follow [How to change this repository](#how-to-change-this-repository) and [AGENTS.md](AGENTS.md). Every pull request needs a written description of what changed.

- Visibility: public, because GitHub's free plan will not serve Pages from a private repository. Do not commit client contact records, passwords, or admin credentials. Inquiry rows, the Cloudflare Email Sending token, and the tunnel credential stay on the laptop. The schema and the data dictionary are in this repository.
- The public pages are static HTML. The trip form posts to the inquiry API documented above. A successful save opens `thanks.html`. The admin sign-in and inquiry browser are not built yet.
- DNS for `forevermemoriestravel.com` points at GitHub Pages. It does not point at the rshocking.com origin. `forevermemoriestravel.rshocking.com` was the earlier hostname.

## Never commit

- Passwords, API tokens, private keys, or `.env` files
- Client contact exports or other personal data
- Cloudflare or registrar credentials
