# Instructions for people and AI tools

Do not commit directly to `main`, except the staff publish button described under CMS publish.

## CMS publish

The staff admin publishes `content/site.json` and files under `assets/media/` to `main` through the GitHub Contents API. That write is the publish button. Do not open a second pull request for a file the admin just published. Every other change, including the first copy of those paths, still uses a feature branch and a pull request.

1. Create a new branch named `feat/<short-description>`.
2. Make the change on that branch.
3. Open a pull request that merges that branch into `main`.
4. Write a description of what changed. Put it in the pull request body. Say what changed and why. A title alone is not the description.
5. Merge only through that pull request.

This applies to every change in this repository, including documentation, site files, and generated content. Do not push fixes, reverts, or follow-up commits straight to `main`.

## Database

The inquiry database is described in [Documentation/DATA-DICTIONARY.md](Documentation/DATA-DICTIONARY.md). Any change to that database requires an update to the data dictionary in the same pull request. That includes tables, columns, types, defaults, constraints, indexes, triggers, functions, roles, and grants. Update [api/schema.sql](api/schema.sql) in that same pull request. Do not commit database rows or credentials.

The database is PostgreSQL database `forever_memories` on `hp-linux-plex-server`, listening on `127.0.0.1:5432` only. Public browsers reach the API through the Cloudflare Tunnel `forever-memories-inquiries` at `https://inquiries.forevermemoriestravel.com`. The setup is on the repository front page, [README.md](README.md).

## Email sending

Trip confirmations leave through Cloudflare Email Sending from the inquiry API as `donotreply@forevermemoriestravel.com`. The record is [Documentation/EMAIL-SENDING.md](Documentation/EMAIL-SENDING.md). Do not enable Email Routing. Do not onboard the domain again. Do not run the Email Sending DNS fix.

`jennifer@forevermemoriestravel.com` exists in Zoho Mail and is the super admin. `michael@forevermemoriestravel.com` does not exist. The domain is verified. The apex MX is `mx.zoho.com` priority 10, `mx2.zoho.com` priority 20, and `mx3.zoho.com` priority 50. The `zoho._domainkey` TXT from this organization is published. The apex SPF is `v=spf1 include:zohomail.com ~all`. The record is [Documentation/ZOHO-MAIL.md](Documentation/ZOHO-MAIL.md). Do not delete the ownership TXT, the `zoho._domainkey` TXT, or those three MX records. Do not add `web71.dnchosting.com` back. Do not add a second apex SPF. Do not put `include:spf.dnchosting.com` back.

## Google tag

Public pages on `forevermemoriestravel.com`, and any new public site on that domain, use one Google tag with measurement ID `G-GYBCCKG2FJ`. The rules are on the repository front page, [README.md](README.md#google-tag). The property record is [Documentation/GOOGLE-TAG.md](Documentation/GOOGLE-TAG.md).

Do not add a Tag Manager container. Do not create a second property, stream, or measurement ID for a new hostname on this domain. Do not send names, email addresses, phone numbers, notes, or record ids to Google. Send `generate_lead` only after a stored request. Update `Documentation/GOOGLE-TAG.md` in the same pull request when tagging changes.

## Search

Search copy, `robots.txt`, the sitemap, `llms.txt`, and the travel-agency structured data are recorded in [Documentation/SEO.md](Documentation/SEO.md). The public guides are `family.html`, `parks.html`, `cruises.html`, and `international.html`. They follow that file and [Documentation/GOOGLE-TAG.md](Documentation/GOOGLE-TAG.md). They do not load `site.js`. Keep the words travel, cruise, Disney, Colorado Springs, and Orlando in ordinary sentences on the home page. Do not copy that list onto a guide that is not about those trips. Do not stuff them into a list, the logo description, or hidden text. Do not link to a similarly named agency. Do not add a social link unless Ryan confirms the profile is this agency, and then record it in `Documentation/SEO.md` in the same pull request. The confirmed TikTok profile is `https://www.tiktok.com/@forevermemoriestravel`. Do not remove it unless Ryan says so. `thanks.html` stays `noindex` and stays out of the sitemap. Do not disallow it in `robots.txt`. The 14 October 2026 SEOptimer audit is recorded in that file. Do not add a Facebook pixel, a bought link, or a link to a referring domain named there. Do not change the apex SPF records as part of a search edit. Apex mail DNS is recorded in [Documentation/ZOHO-MAIL.md](Documentation/ZOHO-MAIL.md).
