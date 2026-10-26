# Zoho Mail

Read from the Zoho Mail API at `https://mail.zoho.com` and from the Cloudflare API on 2026-10-26, between 03:06 and 03:15 UTC. Ryan asked for Zoho Mail Free mailboxes at `jennifer@forevermemoriestravel.com` and `michael@forevermemoriestravel.com`.

Cloudflare Email Routing was not enabled. On this read it was `enabled` false and `status` `unconfigured`. The inquiry form's Reply-To was not changed. In this repository, `api/app.py` sets `REPLY_TO` to `ryanhocking@gmail.com`.

## What exists

The organization is on the Zoho US hosts. Mail API calls go to `https://mail.zoho.com`. Token refresh goes to `https://accounts.zoho.com/oauth/v2/token`. The organization id is `944084466`. The mailbox record says `country` `us` and `timeZone` `America/Denver`. The policy id is `1082700000326584555`, named Business Policy.

`forevermemoriestravel.com` is verified in this organization.

| Field | Value |
| --- | --- |
| domainId | `1082700000326584581` |
| primary | true |
| verificationStatus | true |
| verifiedDate | `1792982534778`, which is 2026-10-26 02:42:14 UTC |
| verifiedBy | zuid `944089540`, address `jennifer@forevermemoriestravel.com` |
| mailHostingEnabled | true |
| isRegisteredByZohoMail | false |
| mxstatus | `enabled` |
| spfstatus | false |
| dkimstatus | true |

The first domain read on 2026-10-26, before the apex MX change, returned `mxstatus` `disabled`. After the three Zoho MX records below were published, `verifyMxRecord` returned `mxstatus` true and the next domain read returned `mxstatus` `enabled`. `spfstatus` was still false.

`jennifer@forevermemoriestravel.com` exists and is the super admin. `michael@forevermemoriestravel.com` does not exist. The organization account list has one user.

| Field | Value |
| --- | --- |
| accountId | `7209151000000008002` |
| zuid | `944089540` |
| primaryEmailAddress | `jennifer@forevermemoriestravel.com` |
| firstName | `Jennifer Ramirez` |
| lastName | empty |
| displayName | `Jennifer Ramirez` |
| role | `super_admin` |
| mailboxStatus | `enabled` |
| allowedStorage | `5242880` KB, which is 5 GB |
| usedStorage | `0` |
| imapAccessEnabled | false |
| popAccessEnabled | false |
| activeSyncEnabled | false |
| deliveryType | `LOCAL` |

The same user object lists `ryanhocking@gmail.com` with `isAlias` false, `isPrimary` false, and `isConfirmed` true. That is the confirmed Zoho account identity. It is not a `forevermemoriestravel.com` mailbox and it is not an MX result.

The organization storage call returned `totalStorage` `free` for this user. `subscriptionInfo` did not include a plan-name string. `GET /api/organization` returned `INVALID_OAUTHSCOPE` because the granted scopes do not include `ZohoMail.partner.organization`. The 5 GB quota, the `free` storage string, and IMAP, POP, and ActiveSync being off match the Mail Free plan described on [Zoho's pricing page](https://www.zoho.com/mail/zohomail-pricing.html). This file does not claim that `subscriptionInfo` returned the words Mail Free.

A sixth user moves every user onto a paid plan, according to that pricing page. Do not add one.

## How the API credential was made

Ryan created a Self Client at `https://api-console.zoho.com/`. The client-credentials grant returned an access token, and `https://mail.zoho.com` then returned `INVALID_OAUTHSCOPE` for `/api/organization` and `/api/accounts`. Do not use `grant_type=client_credentials` for this mailbox.

The working grant is a Self Client authorization code. Zoho's Generate Code screen allowed 10 minutes at most. Ryan generated that code. It was exchanged at 2026-10-26 03:06:11 UTC, before its expiry at 2026-10-26 03:15:13 UTC. The token response included a refresh token. A later call refreshes at `https://accounts.zoho.com/oauth/v2/token` with `grant_type=refresh_token`, the same client id, and the same client secret. Do not ask Ryan for a new code unless that refresh call fails.

Mail API requests send `Authorization: Zoho-oauthtoken <access token>`. The token response says `token_type` Bearer. Do not send `Authorization: Bearer` to `mail.zoho.com`.

The granted scope string, separated by spaces, was:

`ZohoMail.accounts.ALL ZohoMail.messages.ALL ZohoMail.folders.ALL ZohoMail.tags.ALL ZohoMail.notes.ALL ZohoMail.links.ALL ZohoMail.tasks.ALL ZohoMail.organization.accounts.ALL ZohoMail.organization.domains.ALL ZohoMail.organization.groups.ALL ZohoMail.organization.policy.ALL ZohoMail.organization.subscriptions.ALL ZohoMail.organization.spam.ALL ZohoMail.organization.audit.ALL`

The refresh token, access token, client secret, and grant code are not in this repository. On the machine that did this setup they are in `Zoho-self-client-tokens.json` in the keys directory beside the site checkout, outside git. Do not copy that file here. Do not print those values into a pull request, a log, or a chat.

## DNS that was published for Zoho

Ryan chose manual configuration. Zoho's one-click "Log in to my DNS" was not used. That flow can verify the domain and add MX and SPF, and Zoho's manual MX instructions say to delete existing MX records. This zone also has `cf-bounce` mail records, one apex SPF, two Google site-verification TXT records, and GitHub Pages addresses.

The ownership TXT was published at 2026-10-25 20:37 America/Denver (2026-10-26 02:37 UTC). Leave it in place. The host `zmverify.zoho.com` is the verification target. It is not an MX hostname.

| Type | Name | Value | Cloudflare record id | TTL |
| --- | --- | --- | --- | --- |
| TXT | `forevermemoriestravel.com` | `zoho-verification=zb42114402.zmverify.zoho.com` | `f50f14cc89227dda409178738e0906ee` | 120 |

DKIM was added through the Mail API for this domain. The request used `mode` `addDkimDetail`, selector `zoho`, `keySize` 2048, and `isDefault` true. The add response returned `isDefault` false. After the TXT below was published, `verifyDkimKey` returned `dkimstatus` true, and `makeDkimDefault` was called. The following domain read returned `isVerified` true and `isDefault` true. The DKIM id is `1082700000326563956`. The hash type is `sha256`.

| Type | Name | Value | Cloudflare record id | TTL |
| --- | --- | --- | --- | --- |
| TXT | `zoho._domainkey.forevermemoriestravel.com` | `v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkI88iGnmjJQI1Hdnzz9XszUPejM+pFAfXkkU+54J1zYh7hBjTngzIM0zt7HSbNY6hJq1sG1owXdlDBvcnTa9oijYTpeIWsz9AAeAcgC82w97HZ/mMz1PVYY1a6VmEueCha+qG+cS7+kKpxTEZurwTTxGZS1N3h6EWZYFvLa0Se320H9iNjxY6DZOgpXGjgK9cCDRS8j651ph/EjBtraCZ30k1DkUYbNQInjzqpNRk7AlUUa+FTJ44RVJ/Byt/nsYOV/cTmNeBFuEyxJ4sIpXT/VwbTnV13ttIwxZlOo4VgXCzI8O/AJ8o5gJ1KpXyyNhp+JVjH4ypQdq+09Yptz2VwIDAQAB` | `dcc298823dab1dd2ce6d00424e10755d` | 120 |

Authoritative DNS at `apollo.ns.cloudflare.com` returned that TXT with length 410, starting `v=DKIM1; k=rsa; p=MI`. `cf-bounce._domainkey` was still present. Do not regenerate this DKIM key. Regeneration replaces the public value and the TXT above stops matching. Do not edit `cf-bounce._domainkey`.

## Apex MX

On 2026-10-26 Ryan pasted the public page [Configure Email Delivery](https://www.zoho.com/mail/help/adminconsole/configure-email-delivery.html), updated 2026-10-01, and said those were the MX settings. That page shows this table and says the table is generic configuration information:

| Host | Mail server | Priority |
| --- | --- | --- |
| `@` | `mx.zoho.com` | 10 |
| `@` | `mx2.zoho.com` | 20 |
| `@` | `mx3.zoho.com` | 50 |

The domain API object does not include MX hostnames. This organization uses `https://mail.zoho.com`, `https://accounts.zoho.com`, and `zmverify.zoho.com`, and the mailbox country is `us`. Those are the US hosts, and the table on that US help page uses the `.com` names. The three records below were published from that page. The old apex MX `web71.dnchosting.com` priority 0, Cloudflare record id `48112d794e723a9ed9b579a00a32b084`, was deleted only after all three creates succeeded. `cf-bounce` MX records were not changed.

| Type | Name | Value | Cloudflare record id | TTL |
| --- | --- | --- | --- | --- |
| MX | `forevermemoriestravel.com` | `mx.zoho.com` priority 10 | `9e2f423a8f886574e1177aa3518e6d9e` | 120 |
| MX | `forevermemoriestravel.com` | `mx2.zoho.com` priority 20 | `4732ab8a4e850e68b56f36eb306628b0` | 120 |
| MX | `forevermemoriestravel.com` | `mx3.zoho.com` priority 50 | `a098638d6e521d1e427f8e286a0b4e94` | 120 |

Authoritative DNS at `apollo.ns.cloudflare.com` returned those three hosts and no other apex MX. Zoho `verifyMxRecord` then returned `mxstatus` true. No test message was sent.

If a later Tools & Configurations screen for this organization shows different hosts, replace these three with that screen's hosts and update this file in the same change.

## DNS that was not changed

The SPF help page on `zoho.com` shows `v=spf1 include:zohomail.com ~all` in its DNS steps and `v=spf1 include:zohomail.com -all` in another paragraph. Ryan did not paste an SPF value from Tools & Configurations. The apex SPF was left as it was. Outbound mail from Zoho can fail SPF until that one apex SPF is replaced with the string from that screen. The current record still contains `+mx`, which now refers to the Zoho MX hosts, plus `ip4:192.64.150.71` and `include:spf.dnchosting.com`.

| Type | Name | Value | Cloudflare record id |
| --- | --- | --- | --- |
| TXT | `forevermemoriestravel.com` | `v=spf1 +mx +a +ip4:192.64.150.71 +include:spf.dnchosting.com ~all` | `0b6c3863f317260239b252377817feab` |
| TXT | `forevermemoriestravel.com` | `google-site-verification=1kKYEQptuBPWJNtVMC0G5gf9vGTzLLu7Viz9z92DTW4` | `5119e72e8c614323a9c4d266915fef14` |
| TXT | `forevermemoriestravel.com` | `google-site-verification=Gxq4rbtulg2szN_Lr0nt8Uoy-pezNA5CSOEv0p04Nlc` | `df689df1a54fcd9e96189c1021277b52` |
| TXT | `_dmarc.forevermemoriestravel.com` | `v=DMARC1; p=none; rua=mailto:ryanhocking@gmail.com` | `0acbc7d1094acbae0a424ee17845beb5` |

There is one apex TXT that starts with `v=spf1`. On 2026-10-25 a glued second TXT, `v=spf1 mx ptr ~all`, was removed. Do not restore it. `1.1.1.1` can lag `apollo.ns.cloudflare.com`.

The zone had 22 DNS records before this MX change and 24 after it: three MX records added and the `web71.dnchosting.com` MX deleted.

These records stay untouched by the mailbox work:

- Apex A `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, DNS-only. GitHub Pages.
- Apex AAAA `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`, DNS-only. GitHub Pages.
- `www` CNAME `ciscokidry.github.io`, DNS-only.
- `inquiries` proxied CNAME to tunnel `d0dd55a4-e1fa-49b1-a9ba-75e6e133dc1d.cfargotunnel.com`.
- `cf-bounce` MX, SPF, and DKIM selector `cf-bounce`. The record is [EMAIL-SENDING.md](EMAIL-SENDING.md).
- DMARC policy `p=none`. Do not run the Email Sending DNS fix. It can write `p=reject`.

## What is still required

1. Read the SPF string from this organization's Tools & Configurations screen at [the Admin Console](https://mailadmin.zoho.com). The domain GET does not return it. Replace the one apex SPF TXT with that string. Keep both Google site-verification strings as their own TXT records. Keep the ownership TXT. Do not leave `include:spf.dnchosting.com` or `ip4:192.64.150.71` in a second SPF record. Exactly one TXT on the apex may start with `v=spf1`.
2. Leave `_dmarc` at `p=none`. Leave the three `cf-bounce` MX records in place.
3. Ask Zoho to verify SPF. Wait until the domain read shows `spfstatus` true before saying Zoho outbound mail passes SPF.
4. Create `michael@forevermemoriestravel.com` only after Ryan supplies a first name, a last name, and a password. Zoho requires a password of at least 8 characters with one digit, one uppercase letter, one lowercase letter, and one special character. Do not invent the name or the password. Do not store the password in this repository. Do not email Jennifer or Michael.
5. Update this file in the same pull request with the published SPF string and whether `michael@` exists.

Do not change the form Reply-To to either address unless Ryan says those people should receive traveler replies and a test has shown the mailbox receiving mail.

Do not give either person the Cloudflare Email Sending API token. That token is not a mailbox password.

## If mail breaks

Separate the two mail paths before changing DNS.

| Path | What it is | First check |
| --- | --- | --- |
| Form confirmation | Cloudflare Email Sending from `donotreply@forevermemoriestravel.com` | [EMAIL-SENDING.md](EMAIL-SENDING.md). Apex MX does not send this mail. |
| A person's mailbox | Apex MX | `Resolve-DnsName forevermemoriestravel.com -Type MX -Server apollo.ns.cloudflare.com` |

The published apex MX hosts are `mx.zoho.com` priority 10, `mx2.zoho.com` priority 20, and `mx3.zoho.com` priority 50. `jennifer@forevermemoriestravel.com` exists in Zoho. `michael@forevermemoriestravel.com` does not exist in Zoho. No test message was sent.

If the apex MX has been changed to Zoho and new mail does not arrive:

- Compare the live MX, the one apex SPF, and the `zoho._domainkey` TXT with this file and with the current Tools & Configurations screen. A data-center TLD mismatch is a failed setup.
- Confirm there is still exactly one apex TXT that starts with `v=spf1`.
- Confirm `cf-bounce._domainkey` still exists and the Zoho selector is still `zoho`.
- Confirm the `zoho._domainkey` TXT still matches the public key in this file. Do not regenerate the DKIM key to "fix" a mismatch. Put the published key back, or update this file only after a regeneration Ryan asked for.
- Confirm DMARC is still `p=none`.
- Confirm Email Routing is still disabled. If it was enabled, it took the apex MX.
- On the Mail Free plan, the pricing page says IMAP, POP, and ActiveSync are not included. This mailbox has all three disabled. A desktop mail app that requires one of those protocols will not connect. The web app and the Zoho Mail mobile app are the clients the pricing page lists. A protocol refusal is not fixed by changing MX.
- Do not add a sixth user. The pricing page says the sixth user moves every user onto a paid plan.
- Refresh the API token from `Zoho-self-client-tokens.json` before concluding that the API credential died. The 10-minute Generate Code limit does not apply to the refresh token.

If the form stops sending, follow [EMAIL-SENDING.md](EMAIL-SENDING.md). Do not point the form at Zoho to repair it.

## What this file is not

It is not a statement that a test message was delivered. Zoho verified the MX records. It is not a statement that `michael@forevermemoriestravel.com` exists. It is not a statement that outbound Zoho mail passes SPF.
