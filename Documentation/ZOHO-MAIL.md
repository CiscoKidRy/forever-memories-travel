# Zoho Mail

Checked at 2026-10-25 20:24 America/Denver (2026-10-26 02:24 UTC). Ryan asked for Zoho Mail Free mailboxes at `jennifer@forevermemoriestravel.com` and `michael@forevermemoriestravel.com`.

Those mailboxes were not created. No Zoho DNS record was published. Cloudflare Email Routing was not enabled. The inquiry form's Reply-To was not changed. In this repository, `api/app.py` sets `REPLY_TO` to `ryanhocking@gmail.com`.

This file is the record a later person or AI tool should read before touching mail DNS for this domain.

## Why it stopped

Zoho generates the ownership record, the MX hostnames, and the DKIM public key only after an organization exists. Those values were not available.

- The Mail Free plan is the plan on [Zoho's pricing page](https://www.zoho.com/mail/zohomail-pricing.html). That page links Mail Free signup to `https://mail.zoho.com/signup?type=org&plan=free` and also links `https://workplace.zoho.com/signup?type=org&plan=free` from the Forever Free callout. Neither link was opened to create an account. The page says Mail Free is forever free, does not require a credit card, allows up to 5 users on one custom domain, gives 5 GB of mail storage per user, does not include file storage, does not include IMAP, POP, or ActiveSync, and does include the mobile app. A sixth user moves every user onto a paid plan. The Forever Free note says the plan is available only in select data centers. The page does not list those data centers.
- [Zoho's setup guide](https://www.zoho.com/mail/complete-guide-to-setup-zohomail.html), updated 2026-10-13, says signup needs a domain with DNS access, a mobile number that can receive a text message, and an email address. It says the free plan does not require payment details, and that the free plan may be unavailable in some regions. After domain verification, the first mailbox created becomes the super administrator. Adding a user asks for a first name, a last name, and a password of at least 8 characters with one digit, one uppercase letter, one lowercase letter, and one special character.
- No Zoho admin session was available. Windows Credential Manager had no target whose name contained Zoho. The 1Password CLI was installed and `op whoami` returned `no account found for filter`. Gmail search did not run: the local Gmail token refresh returned `invalid_grant`. Display names and passwords were not invented. The Mail API was not called.
- Domain ownership proof is a TXT or CNAME that Zoho shows only after the domain is added at [the Admin Console](https://mailadmin.zoho.com). That value is unique to the account. It was not generated.
- MX hostnames depend on the data center. [Configure Email Delivery](https://www.zoho.com/mail/help/adminconsole/configure-email-delivery.html), updated 2026-10-01, says the TLD varies by data center and that only the MX records in that account's Tools & Configurations should be used. [Zoho's Cloudflare page](https://www.zoho.com/mail/help/adminconsole/cloudflare.html) shows a generic set, `mx.zoho.com` priority 10, `mx2.zoho.com` priority 20, and `mx3.zoho.com` priority 50, and then says those values are generic. Do not publish that generic set.
- DKIM is a TXT Zoho generates in the admin console. It was not generated. A Zoho selector must not replace `cf-bounce._domainkey`.
- Zoho's Cloudflare one-click verification was not used. That flow authorizes Zoho to write DNS. The same Cloudflare help page tells the MX step to delete existing MX records and shows the generic MX set. This zone also has `cf-bounce` MX records, one apex SPF record, and two Google site-verification TXT records. An automatic write can drop or rewrite those.

## What was left in place

Read from the Cloudflare API for zone `d8abd6e253f3f4f48ae4a3f38daa2b70` and from authoritative DNS at `apollo.ns.cloudflare.com` at the time above. The API and the authoritative nameserver agreed.

| Type | Name | Value | Cloudflare record id |
| --- | --- | --- | --- |
| MX | `forevermemoriestravel.com` | `web71.dnchosting.com` priority 0 | `48112d794e723a9ed9b579a00a32b084` |
| TXT | `forevermemoriestravel.com` | `v=spf1 +mx +a +ip4:192.64.150.71 +include:spf.dnchosting.com ~all` | `0b6c3863f317260239b252377817feab` |
| TXT | `forevermemoriestravel.com` | `google-site-verification=1kKYEQptuBPWJNtVMC0G5gf9vGTzLLu7Viz9z92DTW4` | `5119e72e8c614323a9c4d266915fef14` |
| TXT | `forevermemoriestravel.com` | `google-site-verification=Gxq4rbtulg2szN_Lr0nt8Uoy-pezNA5CSOEv0p04Nlc` | `df689df1a54fcd9e96189c1021277b52` |
| TXT | `_dmarc.forevermemoriestravel.com` | `v=DMARC1; p=none; rua=mailto:ryanhocking@gmail.com` | `0acbc7d1094acbae0a424ee17845beb5` |

There is one apex TXT that starts with `v=spf1`. Earlier the same evening, `1.1.1.1` still returned a second TXT, `v=spf1 mx ptr ~all` glued to the second Google site-verification value. Authoritative DNS and the API no longer had that glued record. Do not restore it. `1.1.1.1` can lag the authoritative nameserver.

`web71.dnchosting.com` resolved at `1.1.1.1` on 2026-10-25 to A `192.64.150.71` and AAAA `2602:fc8e:0:688e:150::71`. Ryan said `https://web71.dnchosting.com` does not exist and that the DirectNIC mailbox option is scratched. The MX record was still left in place because there was no Zoho replacement to publish. This file does not claim that host accepts SMTP.

Email Routing for this zone, read from the API in this same check, was `enabled` false and `status` `unconfigured`. Do not enable it. Enabling it replaces the apex MX with Cloudflare. Cloudflare Email Routing and Zoho cannot share the apex MX.

These records stay untouched by mailbox work:

- Apex A `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, DNS-only. GitHub Pages.
- Apex AAAA `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`, DNS-only. GitHub Pages.
- `www` CNAME `ciscokidry.github.io`, DNS-only.
- `inquiries` proxied CNAME to tunnel `d0dd55a4-e1fa-49b1-a9ba-75e6e133dc1d.cfargotunnel.com`.
- `cf-bounce` MX, SPF, and DKIM selector `cf-bounce`. The record is [EMAIL-SENDING.md](EMAIL-SENDING.md).
- DMARC policy `p=none`. Do not run the Email Sending DNS fix. It can write `p=reject`.

The zone had 20 DNS records at this check. A later mailbox change replaces the apex MX, replaces the one apex SPF, adds the Zoho ownership record, and adds the Zoho DKIM TXT. It does not edit GitHub Pages, `www`, `inquiries`, `cf-bounce`, or `rshocking.com`.

## When a Zoho admin exists

1. Sign in at the data center where the organization was created. Do not assume `mail.zoho.com` if the account was created on another Zoho domain.
2. Read the ownership TXT or CNAME from the admin console. Publish only that value. A verification CNAME stays DNS-only.
3. Read MX, SPF, and DKIM from Tools & Configurations for this domain. Publish those strings. If the console shows different hosts from `mx.zoho.com`, `mx2.zoho.com`, and `mx3.zoho.com`, publish the console's hosts.
4. Replace only the apex MX. Leave the three `cf-bounce` MX records in place.
5. Replace the one apex SPF TXT with the one SPF string from the console. Keep both Google site-verification strings as their own TXT records. Do not leave `include:spf.dnchosting.com` or `ip4:192.64.150.71` in a second SPF record. Exactly one TXT on the apex may start with `v=spf1`.
6. Add the generated DKIM TXT under its own selector. Do not edit `cf-bounce._domainkey`.
7. Leave `_dmarc` at `p=none`.
8. Ask Zoho to verify the records. Wait until Zoho reports the domain verified and the MX verified before saying mail is live.
9. Create only `jennifer@forevermemoriestravel.com` and `michael@forevermemoriestravel.com`. Zoho requires a first name, a last name, and a password. Do not invent those. Do not store the passwords in this repository.
10. Update this file in the same pull request with the data center, the published records, Zoho's verification result, and whether each mailbox exists. Remove the sentence that says the mailboxes were not created.

Do not change the form Reply-To to either new address unless Ryan says those people should receive traveler replies and a test has shown the mailbox receiving mail.

Do not give either person the Cloudflare Email Sending API token. That token is not a mailbox password.

## If mail breaks

Separate the two mail paths before changing DNS.

| Path | What it is | First check |
| --- | --- | --- |
| Form confirmation | Cloudflare Email Sending from `donotreply@forevermemoriestravel.com` | [EMAIL-SENDING.md](EMAIL-SENDING.md). Apex MX does not send this mail. |
| A person's mailbox | Apex MX | `Resolve-DnsName forevermemoriestravel.com -Type MX -Server apollo.ns.cloudflare.com` |

Until this file names published Zoho MX hosts, the apex MX is `web71.dnchosting.com`. Mail to `jennifer@` or `michael@` is not a Zoho mailbox.

If the apex MX has been changed to Zoho and new mail does not arrive:

- Compare the live MX, the one apex SPF, and the Zoho DKIM TXT with the current Tools & Configurations screen. A data-center TLD mismatch is a failed setup.
- Confirm there is still exactly one apex TXT that starts with `v=spf1`.
- Confirm `cf-bounce._domainkey` still exists and the Zoho selector is a different name.
- Confirm DMARC is still `p=none`.
- Confirm Email Routing is still disabled. If it was enabled, it took the apex MX.
- On the Mail Free plan, the pricing page says IMAP, POP, and ActiveSync are not included. A desktop mail app that requires one of those protocols will not connect. The page lists the web app and the mobile app. A protocol refusal is not fixed by changing MX.
- Do not add a sixth user. The pricing page says the sixth user moves every user onto a paid plan.

If the form stops sending, follow [EMAIL-SENDING.md](EMAIL-SENDING.md). Do not point the form at Zoho to repair it.

## What this file is not

It is not a statement that Zoho accepted the domain, that either mailbox exists, or that a test message was delivered. None of those happened in this check.
