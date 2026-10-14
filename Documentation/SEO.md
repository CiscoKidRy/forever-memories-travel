# Search

This file tells a later person or AI tool how search works on `forevermemoriestravel.com`, and how to keep going. It was written on 2026-10-14 with the copy in [index.html](../index.html), [robots.txt](../robots.txt), and [sitemap.xml](../sitemap.xml).

The Google tag has its own rules in [GOOGLE-TAG.md](GOOGLE-TAG.md). Follow those rules when a search change touches a page. The tag stays the first thing in `<head>`. This search work does not add a Tag Manager container or a second measurement ID.

## What this site is trying to be found for

The home page should be understood as a Colorado Springs travel agency that plans a cruise, a Disney vacation, or an Orlando trip. The words to keep visible, in normal sentences, are:

- travel
- cruise
- Disney
- Colorado Springs
- Orlando

Use those words when they say what the agency does. Do not repeat them in a list that has no verb. Do not hide them in the page color, off-screen text, or an image description that exists only to rank. Do not add "best", "cheap", "authorized", or "official Disney".

Each of those five words belongs at least twice in the visible home page or in the title and description a search result shows. On 2026-10-14 the placement is:

| Word | Where it appears |
| --- | --- |
| travel | Title, description, heading, opening paragraph, family paragraph, footer |
| Colorado Springs | Title, description, eyebrow, opening paragraph, footer |
| cruise | Description, cruise subheading, cruise paragraph |
| Disney | Description, theme-park heading, theme-park paragraph |
| Orlando | Description, theme-park heading, theme-park paragraph, cruise paragraph |

The title is `Forever Memories Travel | Colorado Springs travel agency`. It does not list every destination. The destinations are in the description and in the sections a person reads.

That five-word table is the home page only. A guide uses the words that belong in a sentence about that trip. Do not copy cruise, Disney, and Orlando onto the family guide or the international guide to satisfy this table. Do not add a bare keyword list, hidden text, or a logo description other than `Forever Memories Travel logo`.

## Topic guides

These four pages are guides. Each one has planning notes, a checklist, short answers, and a link to the trip form. They are not padding added to raise a word count. Do not add another page only to raise a count.

| File | Canonical URL | Title | Title length | Description length |
| --- | --- | --- | --- | --- |
| [family.html](../family.html) | `https://forevermemoriestravel.com/family.html` | A family vacation \| Colorado Springs travel agency | 50 | 134 |
| [parks.html](../parks.html) | `https://forevermemoriestravel.com/parks.html` | Disney and Orlando park days \| Forever Memories Travel | 54 | 138 |
| [cruises.html](../cruises.html) | `https://forevermemoriestravel.com/cruises.html` | Planning a cruise \| Colorado Springs travel agency | 50 | 124 |
| [international.html](../international.html) | `https://forevermemoriestravel.com/international.html` | International trips \| Colorado Springs travel agency | 52 | 140 |

Each guide is indexable. The head starts with the same Google tag snippet as the home page: `gtag('config', 'G-GYBCCKG2FJ')` only. No `page_location`, no Tag Manager container, no `noindex`, and no JSON-LD. The home page keeps the only `WebSite` and `TravelAgency` graph. Do not add `FAQPage`, a second Organization, or a Person block on a guide. A guide does not load `site.js` and does not send `generate_lead`.

The canonical URL, the Open Graph URL, the visible citation line, and the sitemap `<loc>` are the four addresses in the table, plus `https://forevermemoriestravel.com/` for the home page. Open Graph `og:type` is `website`. The Open Graph title, description, and URL match that page. `og:image` and `twitter:image` are `https://forevermemoriestravel.com/assets/logo.jpg`. `twitter:card` is `summary`. The Twitter title and description match the page. `twitter:image:alt` is `Forever Memories Travel logo`. There is no `twitter:site`.

On each guide, the header link "Plan a trip" and both "Start a trip request" buttons use `https://forevermemoriestravel.com/#plan`. The other header links go to the home page and to these four guides. The home page and `thanks.html` keep their current in-page links. Each home-page service card has one text link to its guide. That link sits outside any `data-field` element, so published homepage copy does not remove it.

The parks guide says Forever Memories Travel is not an official Disney partner. That sentence is a limit. It is not a claim of a partnership. Do not add a price or a promise of a place in line.

The logo on each guide is `assets/logo.jpg`, width 1254, height 1254, alt text `Forever Memories Travel logo`, and it links to `index.html`.

The footer order matches the home page: the site name, the Colorado Springs service line, the TikTok link, then the privacy note. The guides do not use `data-field`, because they do not load `site.js`. The footer text is the same sentence the home page shows.

## Sentences that were rejected

A review on 2026-10-14 rejected these patterns. Do not put them back.

- A title, footer, and logo description that each list Colorado Springs, travel, cruises, Disney, and Orlando.
- "Families ask us for a cruise, a Disney vacation, or a week in Orlando." The site does not have a record that families have asked for that.
- A logo description used as a keyword list. The logo description is `Forever Memories Travel logo`.
- Any claim that the agency is an official Disney partner, and any street address, phone number, rating, review count, or price that the page does not show.

## Files a crawler uses

[robots.txt](../robots.txt) allows every crawler and names the sitemap:

```text
User-agent: *
Allow: /

Sitemap: https://forevermemoriestravel.com/sitemap.xml
```

[sitemap.xml](../sitemap.xml) lists five addresses: `https://forevermemoriestravel.com/`, `https://forevermemoriestravel.com/family.html`, `https://forevermemoriestravel.com/parks.html`, `https://forevermemoriestravel.com/cruises.html`, and `https://forevermemoriestravel.com/international.html`. Each entry is a `<loc>` only. Do not add `index.html`, the `www` hostname, `thanks.html`, `llms.txt`, images, CSS, or JavaScript. `www.forevermemoriestravel.com` already redirects to the apex. Do not add `lastmod`, `changefreq`, or `priority`.

Do not disallow `/thanks.html` in `robots.txt`. [thanks.html](../thanks.html) carries `noindex` and a canonical address of `https://forevermemoriestravel.com/thanks.html`. A crawler has to be allowed to see `noindex`. The confirmation address can contain `?ref=`, and that query is an inquiry id. It stays out of the sitemap and out of the Google tag page address. The tag rule for that is in [GOOGLE-TAG.md](GOOGLE-TAG.md).

The home page canonical address is `https://forevermemoriestravel.com/`. The Open Graph title, description, and URL match the title, description, and canonical address. The image is `https://forevermemoriestravel.com/assets/logo.jpg`.

The home page also has Twitter card tags: `twitter:card` is `summary`, and the title, description, image, and image alt match the title, description, and logo. There is no `twitter:site` handle. Do not invent one. `thanks.html` does not need those tags.

[llms.txt](../llms.txt) names the home page, the four guides, and `thanks.html`. It says `thanks.html` is a confirmation page marked `noindex`. It says the site does not publish a street address or a business phone number, and it names the TikTok profile. Do not add a fact there that those pages do not show. Do not put `llms.txt` in the sitemap.

The logo file is 1254 by 1254 pixels. Both logo images set `width="1254"` and `height="1254"`. The stylesheet still sizes the logo for the page.

The footer site name stays the large serif line. The line under it, and the privacy note, stay centered. Both are italic, and the privacy note is the smaller of the two. A 14 October 2026 check of the live page showed the privacy note at nearly the body size, not italic, and stretched wide enough that the lines did not read as a centered footer. Do not put that note back to body size or to a full-width left edge.

## Structured data

The home page has one schema.org graph in `index.html`. It has two nodes:

- `WebSite` for `https://forevermemoriestravel.com/`, with the site name, the same description as the meta description, `inLanguage` `en`, and `publisher` pointing at the agency.
- `TravelAgency` for Forever Memories Travel. `TravelAgency` is already an Organization. Do not add a second Organization or a Person block. The logo is an `ImageObject` for `https://forevermemoriestravel.com/assets/logo.jpg` at 1254 by 1254. The address has only `addressLocality` set to `Colorado Springs`.

The description on both nodes is the same sentence as the meta description. `thanks.html` and the four guides have no structured data. `thanks.html` is a confirmation page. The guides stay indexable without a second agency block.

Do not add `streetAddress`, `postalCode`, `addressRegion`, `addressCountry`, `telephone`, `email`, `contactPoint`, `openingHours`, `geo`, `aggregateRating`, `review`, `priceRange`, a search action, or an offer. The page does not show those facts. This block will not produce a local-business rich result, and that is expected. `sameAs` may contain only `https://www.tiktok.com/@forevermemoriestravel`. Do not add `https://www.instagram.com/forevermemoriestravel/`. Ryan named that profile and then said not to use it.

## Social profiles and backlinks

A search on 2026-10-14 found no Facebook, Instagram, YouTube, or LinkedIn page for `forevermemoriestravel.com`.

These similarly named businesses are not this site. Do not link to them:

- Memories Forever Travel Group, Fair Lawn, New Jersey, `memoriesforevertravel.com`
- Memories Forever Travel, Pierz, Minnesota, `memories4evertravel.com`
- Forever Memories Travel LLC, Land O Lakes, Florida, dissolved in 2022
- Making Memories Travel LLC, Florissant, Colorado
- Other agencies whose names contain "memories" and "travel"

Ryan confirmed on 2026-10-14 that `https://www.tiktok.com/@forevermemoriestravel` represents this website. The footer of the home page and of `thanks.html` links to that exact URL with a TikTok icon and the visible word TikTok. The `TravelAgency` `sameAs` list contains that URL and no other. Do not remove the link unless Ryan says so. The videos on that profile are credited to Jennifer Ramirez. The trip form on this site does not send requests to Jennifer.

On 2026-10-14 Ryan named `https://www.instagram.com/forevermemoriestravel/` and then said not to use that link. Do not add it.

Ryan can create a profile and point it at `https://forevermemoriestravel.com/`. These are the setup pages. They are not links on the public site, and they are not `sameAs` values:

- Facebook Page: `https://www.facebook.com/pages/create`
- Instagram: `https://www.instagram.com/accounts/emailsignup/`
- LinkedIn company: `https://www.linkedin.com/company/setup/new/`
- YouTube: `https://www.youtube.com/create_channel`
- X: `https://x.com/i/flow/signup`

After Ryan creates one, he puts `https://forevermemoriestravel.com/` on that profile and sends the profile URL. Only then does a later pull request add the icon and the `sameAs` entry. Do not add a profile from this list before that URL arrives. Google Business Profile at `https://business.google.com/` is optional and stays outside this repository. Do not file a street address the site does not show.

When Ryan confirms another profile that is actually this agency, add it in the footer with the visible name and the real URL, record the URL in this file, and add that URL to `sameAs` in the same pull request. That profile link is the backlink. Do not buy links, and do not post the site on someone else's page.

## SEOptimer audit, 14 October 2026

SEOptimer graded the live site D+ at 6:34 AM UTC on 14 October 2026, before this branch was published. On-page was D+, GEO was B-, links were F, usability was C, and performance was A-. The lab scores were mobile PageSpeed 76 and desktop 98. The report is a scan kept outside this repository. These decisions are the record. The grade is not a Google ranking.

The title is 56 characters, inside the tool's 50 to 60 character range. The description is 151 characters, inside 120 to 160. Keep that title. The tool also scored phrases it inferred (kind of trip, plan, travel agency, vacation, park, trip). Those phrases are not the five words in the table above. Do not replace the table with the tool's list.

Taken from the report, because the finding was real:

- The canonical URL, Open Graph tags, Twitter card tags, `robots.txt`, and `sitemap.xml`.
- One schema.org graph: a `WebSite` node and a `TravelAgency` node. `TravelAgency` is already an Organization. Do not add a second Organization or a Person block.
- A second heading level. The three step labels are `h3` elements: "You write.", "We plan it with you.", and "You go." The cruise section has an `h3`: "The cruise, the cabin, and the ports."
- Width and height on the logo images, matching the 1254 by 1254 file.
- `llms.txt`, limited to facts the home page and the four guides already state.

Left unchanged on purpose:

- No Facebook pixel.
- No new Facebook, X, Instagram, LinkedIn, or YouTube profile, and no link to a profile this file does not name.
- The audit, on that date, found no social profile. Ryan later confirmed TikTok. `sameAs` now lists only `https://www.tiktok.com/@forevermemoriestravel`.
- No street address, business phone, or email address printed on the page. The phone field on the form is the visitor's number.
- No LocalBusiness block built from an invented address.
- No bought links. The report's referring domains are not partners. It listed quero.party, urls-shortener.eu, bye.fyi, atomizelink.icu, blogsphere.top, metamagic.top, shortenurls.eu, anchorurl.cloud, optimzeflow.top, and dailymusings.top, plus a spam anchor that mentioned RankVA.com and Telegram. Do not link to those domains, and do not treat them as backlink partners.
- SPF and DMARC. The report said the apex has two SPF records. Leave both. Leave DMARC as [EMAIL-SENDING.md](EMAIL-SENDING.md) records it. That file forbids changing the apex MX or the apex SPF records for a search change.
- The logo file. Do not replace `assets/logo.jpg` unless a side-by-side visual check accepts the smaller file. These guides leave the file as it is.
- GitHub Pages cache headers. The host sets them. This repository cannot lengthen them.
- The Google Fonts link stays on these pages. It already uses `display=swap`. Desktop performance in the report was 98. Do not remove the Google tag to chase the mobile score. A later change may self-host only the font files the CSS uses and then remove that stylesheet.
- Page count. The report called the home page thin. The four guides above are the response. Do not add another page, or a sentence, only to raise a count.

HTTPS. During the audit, `http://forevermemoriestravel.com/` returned 200 and the GitHub Pages setting `https_enforced` was false. HTTPS itself already returned 200. Turning enforcement on is a Pages setting, not a file, and it does not need a DNS change. After the pull request that publishes this file is merged, `http://forevermemoriestravel.com/` should redirect to `https://forevermemoriestravel.com/`. If that setting cannot be turned on, write the result in this section. Do not move DNS to force the redirect.

## What does not make the site rank by itself

`robots.txt`, the sitemap, the canonical address, and the `TravelAgency` block tell a crawler what the page is. They do not assign a rank. Search engines can take days to recrawl a new page. A standard report in Google Analytics can take up to 24 hours, and that report is not a ranking.

On 2026-10-14 Ryan submitted `https://forevermemoriestravel.com/sitemap.xml` in Google Search Console and in Bing Webmaster Tools. That submission is done. After these guides are published, that same sitemap URL is the one both tools already have. Resubmitting it asks for a crawl of the new addresses. It does not assign a rank. Do not ask for the first submission again as if it had not happened. Search Console: `https://search.google.com/search-console/sitemaps?resource_id=https://forevermemoriestravel.com/`. Bing: `https://www.bing.com/webmasters/sitemaps?siteUrl=https://forevermemoriestravel.com/`.

## A later change

Update this file in the same pull request when a change does any of these:

- Adds or rewrites a sentence so the five words above move or disappear
- Adds a public page that should be crawled, or a page that should stay out of search
- Changes `robots.txt`, `sitemap.xml`, `llms.txt`, the canonical address, the Twitter card, or the `TravelAgency` block
- Adds a social profile or any other external link that is meant to become a backlink
- Adds a street, phone, rating, or price to the page and then to the structured data
- Links to a domain listed in the SEOptimer section, adds a Facebook pixel, or changes the apex SPF records

A new public page on this domain uses the same Google tag rules as [GOOGLE-TAG.md](GOOGLE-TAG.md). Add its canonical URL to the sitemap only when the page should be indexed. A confirmation page stays `noindex` and stays out of the sitemap.

Keep the footer privacy notice accurate. Search copy does not change who receives a trip request.
