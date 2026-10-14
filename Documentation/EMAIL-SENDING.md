# Email Sending

This file is the record of Cloudflare Email Sending for `forevermemoriestravel.com`. It was checked against the Cloudflare API, public DNS at 1.1.1.1, the live site, and one delivered test message on 2026-10-14.

The inquiry API still sends through Gmail SMTP. This onboarding does not change that code. A later change can send as `donotreply@forevermemoriestravel.com` because the domain is already onboarded. Do not onboard the domain again.

## Account and domain

| Item | Value |
| --- | --- |
| Account | `aac0196dfd6a1ccec84b92a22602ffb3` |
| Zone | `forevermemoriestravel.com`, `d8abd6e253f3f4f48ae4a3f38daa2b70` |
| Sending subdomain id | `6496d34df8614da5a64f13bf7b28ab6a` |
| Sending name | `forevermemoriestravel.com` |
| Enabled | true |
| DKIM selector | `cf-bounce` |
| Return path | `cf-bounce.forevermemoriestravel.com` |
| Created | 2026-10-14T06:20:43Z |
| Email Routing | `unconfigured`, `enabled` false |

Any local-part on the onboarded domain can send. The confirmation address is `donotreply@forevermemoriestravel.com`. The display name is Forever Memories Travel. `donotreply@` is not a mailbox. Human replies to that address would follow the apex MX to DirectNIC. A sender sets `reply_to` to `ryanhocking@gmail.com`.

## DNS this onboarding added

These names are separate from the apex. The apex MX was not changed.

| Type | Name | Value |
| --- | --- | --- |
| MX | `cf-bounce.forevermemoriestravel.com` | `route1.mx.cloudflare.net` priority 71 |
| MX | `cf-bounce.forevermemoriestravel.com` | `route2.mx.cloudflare.net` priority 39 |
| MX | `cf-bounce.forevermemoriestravel.com` | `route3.mx.cloudflare.net` priority 52 |
| TXT | `cf-bounce.forevermemoriestravel.com` | `v=spf1 include:_spf.mx.cloudflare.net ~all` |
| TXT | `cf-bounce._domainkey.forevermemoriestravel.com` | one `v=DKIM1` key, selector `cf-bounce` |
| TXT | `_dmarc.forevermemoriestravel.com` | `v=DMARC1; p=none; rua=mailto:ryanhocking@gmail.com` |

Cloudflare's create call first wrote `_dmarc` as `v=DMARC1; p=reject;`. That record was updated to `p=none` at 2026-10-14T06:21:19Z. `p=none` monitors failures and does not tell receivers to reject other mail from this domain. Do not run the Email Sending DNS fix after this. That fix can write `p=reject` again.

DNS status for subdomain `6496d34df8614da5a64f13bf7b28ab6a` was `ready` with an empty error list after the DMARC update.

## What stayed in place

| Record | Value |
| --- | --- |
| Apex MX | `web71.dnchosting.com` priority 0 only |
| Apex SPF TXT | `v=spf1 +mx +a +ip4:192.64.150.71 +include:spf.dnchosting.com ~all` |
| Apex TXT | `v=spf1 mx ptr ~allgoogle-site-verification=Gxq4rbtulg2szN_Lr0nt8Uoy-pezNA5CSOEv0p04Nlc` |
| Apex A | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, DNS-only |
| Apex AAAA | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`, DNS-only |
| `www` | CNAME `ciscokidry.github.io`, DNS-only |
| `inquiries` | proxied CNAME to tunnel `d0dd55a4-e1fa-49b1-a9ba-75e6e133dc1d` |

The two apex TXT strings were already there. Two `v=spf1` records on the same name make apex SPF a permerror. They were not merged or split. Sending SPF lives on `cf-bounce`, so Cloudflare outbound does not use the apex SPF.

Email Routing stays off. No `rshocking.com` record was changed.

## Allowances

Two ceilings apply to this Cloudflare account. This work did not change either one.

Workers Paid includes 3,000 accepted outbound Email Sending messages per account per billing month. Past that, Cloudflare charges $0.35 per extra 1,000. Accepted messages, including hard bounces, count. Messages rejected before acceptance do not. The allowance is shared with every other sender on the account, including Spiritual Gifts. Do not send a 3,001st counted message in a billing month.

The Email Sending limits API, read on 2026-10-14 before and after the test, reported a separate quota of 200 messages per day and `usage.sent` of 0. That daily quota is what `GET /accounts/aac0196dfd6a1ccec84b92a22602ffb3/email/sending/limits` returns. It is tighter than 3,000 divided across a month. Do not plan past 200 accepted sends in a day.

Sends to a verified Email Routing destination do not count. The only verified destination on the account is `ryanhocking@gmail.com`, verified 2025-11-28. The test below went there, and `usage.sent` stayed 0.

## How a later sender calls it

`POST https://api.cloudflare.com/client/v4/accounts/aac0196dfd6a1ccec84b92a22602ffb3/email/sending/send`

Use a Bearer token that can send mail. On this PC that token is in Windows Credential Manager as `Cloudflare-API-Token-SMTP`. The zone DNS token cannot send. The token stays in `/etc/forever-memories-inquiries.env` on the laptop when the API is switched. Do not commit it.

```json
{
  "from": { "address": "donotreply@forevermemoriestravel.com", "name": "Forever Memories Travel" },
  "to": "visitor@example.com",
  "reply_to": "ryanhocking@gmail.com",
  "subject": "We have your trip request",
  "text": "plain text",
  "html": "<p>html</p>"
}
```

`from` is a string or an object with `address` and `name`. The REST field is `address`, not `email`. `reply_to` is snake case. Provide `text` and `html`. The live visitor subject is `We have your trip request`. The live staff subject is `Trip request — Forever Memories Travel`, and that copy still goes to `ryanhocking@gmail.com`.

`api/app.py` was not changed. `send_mail` still uses `smtp.gmail.com` port 587 and `GMAIL_ADDRESS`.

## Test on 2026-10-14

One message. No retry.

| Check | Result |
| --- | --- |
| API | HTTP 200, `queued`: `ryanhocking@gmail.com`, no permanent bounce |
| Message id | `<kcA5eO0dWISHDSJZGsGXJaxjqSew0UMflfXm@forevermemoriestravel.com>` |
| Gmail id | `1a13913056126a30` |
| Gmail labels | `INBOX`, `UNREAD`, `CATEGORY_UPDATES` |
| From | `Forever Memories Travel <donotreply@forevermemoriestravel.com>` |
| Return-Path | `bounces@cf-bounce.forevermemoriestravel.com` |
| SPF | pass, client `104.30.10.91` |
| DKIM | pass, `header.s=cf-bounce`, `header.i=@forevermemoriestravel.com` |
| DMARC | pass, `p=NONE`, `header.from=forevermemoriestravel.com` |
| Inquiry health | `GET https://inquiries.forevermemoriestravel.com/health` returned `{"ok": true}` |
| Home page | `https://forevermemoriestravel.com` returned HTTP 200 |

No inquiry row was created. The subject was `FMT Email Sending test 2026-10-14 donotreply`.
