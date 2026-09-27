# Apple and Google developer-profile requirements

Verified against current official platform documentation on **2026-08-04**. Console rules and organization-verification policies can change; recheck the linked sources before a substantially later publication.

## Executive distinction

Google Play has a customizable public Developer Profile. Apple has a public developer page, but the page is generated from the catalog and does not expose comparable account-level logo, header, bio, email, social, or website controls.

The Nelson Grey brand assets therefore split into two uses:

- **Google:** direct profile uploads for the icon and header, plus paste-ready promotional text.
- **Apple:** a consistent external portfolio/press site, per-app Marketing URLs and product-page media, official marketing tools, custom product pages, optimization tests, events, and featuring nominations.

## Google Play Developer Profile

Google's current [Developer Profile help](https://support.google.com/googleplay/android-developer/answer/9873827?hl=en) documents these fields:

| Field | Requirement | Kit asset or value |
|---|---|---|
| Profile availability | Optional; at least one published app is required before creation | Confirm a published app exists |
| Developer icon | Exactly 512 × 512; 32-bit PNG | `google/developer-icon-512x512.png` |
| Header image | Exactly 4096 × 2304; JPG or 24-bit PNG without alpha | PNG and smaller JPG supplied in `google/` |
| Promotional text | Maximum 140 characters; translations supported | Limit-checked text in `copy/google-promotional-text.txt` |
| Website | Optional; one official brand/company URL | `https://nelsongrey.com/` |
| Featured app | Optional; one published app by name/package | Modulo Squares only after availability verification |
| Profile URL | Assigned by Google and shareable | Capture after first save |

Google documents no account-level social-handle fields. Put social destinations on the linked Nelson Grey portfolio site instead.

Google states that the first preview URL can take up to one hour and the initial public page can take up to 24 hours. Later changes can take up to one hour. No public file-size maximum or official header safe area is stated. The recommended header is therefore text-free, center-balanced, and resilient to responsive cropping. It is deterministically rendered from `sources/header-art-master.svg`.

Use `Software & apps` as the Nelson Grey developer-page label wherever an appropriate text field is available. Treat it as page copy or metadata, not part of the icon or header artwork.

### Organization identity and public contact

Current [Play Console identity-verification guidance](https://support.google.com/googleplay/android-developer/answer/13628312?hl=en) and [account-information requirements](https://support.google.com/googleplay/android-developer/answer/13634081?hl=en) distinguish several layers:

1. The legal organization identity used for verification.
2. The public developer name, which can differ from the legal name and is reviewed when changed.
3. The optional public Developer Profile website.
4. Each app's required public support email and optional support website/phone.

For an organization account, Google says the verified legal organization name, legal address, developer email, and developer phone are displayed on Google Play. The organization website supplied for account identity and verification is required and distinct from the optional website link on the promotional Developer Profile. Use `https://nelsongrey.com/` as the organization website and `hello@nelsongrey.com` as the public company/developer contact. Keep `nelson.grey.arc@gmail.com` private as the Google Account owner/login only.

Each app separately needs a support email. Google's [developer contact guidance](https://support.google.com/googleplay/android-developer/answer/113477?hl=en) allows those per-app details to differ from the account-level profile.

### Profile content policy

The developer name, profile content, and linked developer-website landing page must follow [Play policy](https://support.google.com/googleplay/android-developer/answer/17190352?hl=en). Identity or contact-verification lapses can remove the developer presence and apps until reverification, as described in [developer-verification requirements](https://support.google.com/googleplay/android-developer/answer/10841920?hl=en).

### Do not confuse the two 512-pixel icons

The Developer Profile icon is the company/publisher identity. A Play app icon is per app and has separate masking, shadow, and artwork rules. Do not upload the Nelson Grey developer icon as the Modulo Squares app icon, or vice versa.

Per-app Play listing requirements remain documented in [graphic-asset guidance](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en), [store-listing text guidance](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en), and [app-icon specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications).

## Apple public developer presence

Apple's public developer page is a generated App Store catalog page. Apple's [discovery and engagement analytics schema](https://developer.apple.com/documentation/analytics-reports/app-store-discovery-and-engagement) recognizes `Developer page` as a discovery source, and current pages group a developer's apps and latest releases.

No current App Store Connect metadata field or API resource was found for an account-level developer logo, header, bio, social link, email, or website. This is an inference from Apple's current metadata references and rendered developer pages; Apple does not publish a page that simply says the developer page is not customizable.

Apple's private [Developer Profile](https://developer.apple.com/help/account/basics/profile/) is a separate account-preferences feature. It personalizes Apple news and communications; it is not the public App Store developer page.

### Developer name and legal provider

Apple's [developer-name guidance](https://developer.apple.com/help/app-store-connect/create-an-app-record/set-your-developer-name) states that an organization chooses its developer name while creating its first app. The choice can be the legal name or an eligible registered trade name, DBA, or fictitious business name, and it cannot later be edited.

The verified legal entity is separately shown as the seller/provider. Before publishing Nelson Grey materials, confirm the exact existing developer name in App Store Connect. Do not assume it can be changed to match a new wordmark.

### Website and email path

Each app can have an optional, localizable Marketing URL. Apple labels that destination `Developer Website` on the public product page. Use `https://nelsongrey.com/` or the appropriate live Nelson Grey portfolio page for every app where the destination is relevant.

Each app also requires a Support URL that leads to real contact information. Apple's [platform-version metadata reference](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information) covers both fields.

The Apple Account login email is not automatically a storefront field. Keep `nelson.grey.arc@gmail.com` private as the account owner/login only, and use `hello@nelsongrey.com` for public company contact where appropriate. EU traders have separate verified public contact requirements under Apple's [Digital Services Act guidance](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/).

### Strong Apple promotional routes

- Up to 70 [custom product pages](https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions) per app, with tailored media, promotional text, keywords, localization, and shareable URLs.
- [Product-page optimization](https://developer.apple.com/app-store/product-page-optimization/) tests with up to three alternative icon/screenshot/preview treatments.
- Timely [In-App Events](https://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events) in Apple's supported categories: live event, premiere, challenge, competition, new season, major update, and special event.
- [Featuring nominations](https://developer.apple.com/help/app-store-connect/manage-featuring-nominations/nominate-your-app-for-featuring) with Apple's recommended minimum lead time of three weeks; the current [nomination field reference](https://developer.apple.com/help/app-store-connect/reference/nominations/nominations-template/) allows a 1,000-character description, up to five supplemental URLs, and 500 characters of Helpful Details.
- Apple's [marketing tools](https://developer.apple.com/app-store/promote/) for official short links, QR codes, badges, banners, app-icon embeds, preset messages, and social assets.

Do not recreate an Apple App Store badge. Use Apple's supplied badge artwork and follow the [App Store marketing identity guidelines](https://developer.apple.com/app-store/marketing/guidelines/).

## Apple app-level media reference

These are not developer-profile uploads, but they are the media Apple actually promotes:

| Asset | Current requirement |
|---|---|
| App icon | 1024 × 1024 master; current systems support multiple appearances |
| iPhone screenshots | 1–10 JPEG/JPG/PNG; no alpha; current 6.9-inch portrait sizes include 1260 × 2736, 1290 × 2796, and 1320 × 2868 |
| App previews | Up to 3 per localization/device; 15–30 seconds; maximum 500 MB |
| In-App Event card | 16:9; 1920 × 1080 through 3840 × 2160 |
| In-App Event detail | 9:16; 1080 × 1920 through 2160 × 3840 |
| Promoted IAP image | 1024 × 1024 JPG/PNG; RGB, flattened, no rounded corners |

Official references: [app icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/), [screenshots](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/), [app previews](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications), [event media](https://developer.apple.com/help/app-store-connect/reference/in-app-events/in-app-event-media-and-audio-specifications/), and [IAP information](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information).
