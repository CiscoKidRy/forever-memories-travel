# Google tag

This file is the record of Google Analytics for `forevermemoriestravel.com`. It was checked against the Analytics property and the published pages on 2026-10-14.

The operating rules are on the repository front page, [README.md](../README.md#google-tag). A change to tagging follows those rules and updates this file in the same pull request.

## Account and property

One Analytics account holds one property for this domain. Public pages use that property's one web stream.

| Item | Value |
| --- | --- |
| Account | `accounts/183860744`, display name ForeverMemoriesTravel.com |
| Property | `properties/558909334`, display name ForeverMemoriesTravel.com |
| Property created | 2026-10-14T03:59:57Z |
| Industry | `TRAVEL` |
| Time zone | `America/Denver` |
| Currency | `USD` |
| Service level | `GOOGLE_ANALYTICS_STANDARD` |
| Web stream | `properties/558909334/dataStreams/16124833071` |
| Stream created | 2026-10-14T04:16:28Z |
| Measurement ID | `G-GYBCCKG2FJ` |
| Stream URL | `https://forevermemoriestravel.com` |

`www.forevermemoriestravel.com` serves the same GitHub Pages files as the apex. It uses the same measurement ID. It does not have its own stream.

The inquiry API at `inquiries.forevermemoriestravel.com` is not a website. The tag does not go on that API, on a JSON response, or in email.

## Property settings

| Setting | Value |
| --- | --- |
| Event data retention | `FOURTEEN_MONTHS` |
| Reset the retention clock on new activity | true |
| User data retention | `FOURTEEN_MONTHS` |
| Google signals | `GOOGLE_SIGNALS_DISABLED` |
| Google Ads link | none |
| Enhanced measurement | on |
| Scrolls, outbound clicks, video, file downloads, page changes | on |
| Form interactions | on |
| Site search | off |

The Admin API omits `siteSearchEnabled` when it is false. A read that shows the other enhanced-measurement switches and does not show `siteSearchEnabled` means site search is off. The stored search-parameter string is still `q,s,search,query,keyword`. This site has no search page, so those parameters are not treated as searches.

Form interaction measurement can record `form_start` and `form_submit`. Those events are diagnostics. `form_submit` is not a key event. A form attempt is not a lead.

Page-change measurement listens for browser history events. The in-page links `#vacations`, `#parks`, `#cruises`, `#international`, and `#plan` are hash links. Do not add a manual `page_view` when someone clicks them.

Google signals stay off. Do not link Google Ads, BigQuery, or a second stream unless Ryan asks for that change and this file is updated in the same pull request. Do not send a user id or a hashed email.

This is a US site. The footer privacy notice is the disclosure. Do not add a Consent Mode default of denied, and do not add a cookie banner, only to make the tag load.

## Key events

| Event | Resource | Counting | What to do |
| --- | --- | --- | --- |
| `generate_lead` | `properties/558909334/keyEvents/16125148821` | `ONCE_PER_EVENT` | This is the lead. It was created 2026-10-14T05:30:49Z, after the site code that sends it was already published. |
| `purchase` | `properties/558909334/keyEvents/16124833070` | `ONCE_PER_EVENT` | Google creates this for a web stream and refuses to delete it. The delete request returned HTTP 400, "The event cannot be deleted." Leave it. The site sends no `purchase` event, so the count stays at zero. |

`close_convert_lead` and `qualify_lead` were removed on 2026-10-14. Do not add them back.

`generate_lead` counts once per event, so two stored requests in one visit count as two leads. Do not switch it to once per session.

A standard property can have 30 custom key events. `purchase` is a default key event and does not use one of those 30. `generate_lead` does.

## The tag on a page

Every public HTML page has one Google tag. The snippet is the first thing inside `<head>`. [index.html](../index.html) uses this snippet:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GYBCCKG2FJ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-GYBCCKG2FJ');
</script>
```

The host `www.googletagmanager.com` is where Google serves this tag. It is not a Tag Manager container. A container on a page would be a second snippet whose id starts with `GTM-`. This site has no container.

On 2026-10-13 Google mailed `ryanhocking@gmail.com` from `tagmanager-noreply@google.com` with the subject "Set up a Google tag on your website." That mail offered two choices: paste the snippet above, or use Tag Manager instead. The site uses the snippet. The mail's install link includes Tag Manager account `6382436523` and container `267082887`. Those identify the setup wizard. The published pages do not load that container. The mail also said Google had not found a tag yet. It was sent before the snippet was published. A later mailbox check found no message that said Google had detected the tag.

A page whose address contains a record id, an email address, or other visitor data in the query string uses the same snippet with one extra config field. [thanks.html](../thanks.html) does this so the inquiry id in `?ref=` is not sent to Google:

```html
gtag('config', 'G-GYBCCKG2FJ', {
  page_location: location.origin + location.pathname
});
```

The confirmation page can still read the query string to show the reference. Only the measured page address drops it.

On 2026-10-14 a browser load of the home page requested `https://www.googletagmanager.com/gtag/js?id=G-GYBCCKG2FJ` and sent collect hits for `page_view` and `user_engagement` with measurement id `G-GYBCCKG2FJ`. No `generate_lead` hit was sent on that load. Realtime in Analytics shows a page view within a few minutes. Standard reports can take up to 24 hours.

## The lead event

[site.js](../site.js) sends `generate_lead` from `recordLeadThen`. That function runs only after the inquiry API returns HTTP 201 and a JSON `id`. The call happens before the browser opens `thanks.html`.

The event parameters are:

| Parameter | Value |
| --- | --- |
| `lead_source` | `trip_form` |
| `trip_type` | `family`, `park`, `cruise`, or `international` |

The select labels map like this:

| Label on the form | `trip_type` |
| --- | --- |
| Family vacation | `family` |
| Theme park | `park` |
| Cruise | `cruise` |
| International | `international` |
| Not sure yet | omitted |

The event does not include the name, email, phone, travel dates, who is going, notes, honeypot, idempotency key, or inquiry id.

The call sets `transport_type` to `beacon` so the hit can leave as the next page opens. `event_callback` opens `thanks.html`. A one-second timer opens that page if the callback does not run, so a blocked tag cannot leave the visitor on the form. The timer and the callback share one guard, so the page opens once.

These paths do not send `generate_lead`:

- The honeypot field `company` has a value.
- The form fails `reportValidity()`.
- The button is already locked.
- The API returns anything other than HTTP 201 with an id, including 409 and 429.
- The request fails on the network.

`form_submit` from enhanced measurement can still fire when the browser submits the form. That event is not the lead and is not a key event.

## Privacy notice

The footer on `index.html` and `thanks.html` says the site uses cookies and Google Analytics, that Analytics collects pages visited and a client id stored in a cookie, and that Google processes that information. The link text is "How Google uses information from sites or apps that use our services" and the address is `https://www.google.com/policies/privacy/partners/`.

The same paragraph says the trip form stores the name, email, phone, and trip details and emails a copy to the visitor and to Forever Memories Travel. If the form's recipients change, change this sentence in the same pull request. Keep the sentence matched to the form.

## A new site on this domain

A new public website on `forevermemoriestravel.com`, including a new hostname, uses this same property, this same web stream, and measurement ID `G-GYBCCKG2FJ`. Do not create a new Analytics property, a new web stream, or a new measurement ID for another page or hostname on this domain.

For each new HTML page:

1. Put the snippet from this file first inside `<head>`.
2. Use one snippet on the page.
3. If the page address can contain a record id or other visitor data, set `page_location` to `location.origin + location.pathname`.
4. If the page saves a request on a server, send `generate_lead` only after that save succeeds. Set `lead_source` to a short name for that form. Set `trip_type` only to `family`, `park`, `cruise`, or `international`. Add the new `lead_source` value to the table below in the same pull request.
5. Put the privacy notice on the page.
6. Leave the `purchase` key event alone and do not send `purchase`.

Current lead sources:

| `lead_source` | Page | When it fires |
| --- | --- | --- |
| `trip_form` | `index.html` through [site.js](../site.js) | Inquiry API returns HTTP 201 with an id |

The API hostname `inquiries.forevermemoriestravel.com` stays untagged.

## Changes that must update this file

Update this file in the same pull request when a change does any of these:

- Adds, removes, or moves the Google tag
- Changes the measurement ID, property, or stream
- Adds a page or a new hostname on this domain
- Adds or changes a `generate_lead` parameter or a `lead_source` value
- Marks or unmarks a key event
- Changes retention, Google signals, enhanced measurement, or an Ads link
- Changes the privacy notice

Do not put tokens, passwords, inquiry rows, or visitor-identifying values in this file.
