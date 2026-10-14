# Developer-profile publication checklist

No account settings or external pages were changed while creating this kit. Complete the following steps with an authorized account owner.

## Decisions before upload

- [ ] Confirm the public brand should be `Nelson Grey` and the legal organization is `Nelson Grey LLC`.
- [ ] Confirm the Google/developer profile uses the dark developer colorway while general company surfaces keep the official core icon.
- [ ] Compare the developer source against `assets/nelson-grey-mark.svg`: internal path and node geometry must be identical; the developer uses the `#101722` field and `#F8F4EA` `N`, keeps teal and gold unchanged, and omits the Core-only light-field keyline.
- [ ] Confirm the Core icon uses the official `#D7CCB8` inset keyline and remains legible on white at 180, 32, and 16 pixels.
- [ ] Keep every logo lockup free of slogans and descriptors. Use the shared raised `LLC` suffix, and use `Software & apps` only as a developer-page label or metadata value.
- [ ] Confirm the exact existing Apple developer name in App Store Connect; it cannot be renamed after the first-app choice.
- [ ] Confirm the exact current Google public developer name and submit any change early enough for review.
- [ ] Use `https://nelsongrey.com/` as the official public website.
- [ ] Use `hello@nelsongrey.com` as the public company contact and verify it is monitored.
- [ ] Keep `marknelson@nelsongrey.com` private as the account owner/login only.
- [ ] Verify the live status, country distribution, links, pricing, and platforms of every product mentioned publicly.

## Google Play Developer Profile

- [ ] Confirm at least one app is published; Google does not allow profile creation before that point.
- [ ] Open Play Console → Developer account → Developer page/profile.
- [ ] Upload `google/developer-icon-512x512.png`.
- [ ] Upload either the PNG or JPG `google/developer-header-4096x2304` file. Prefer the JPG for a smaller transfer; use the PNG when lossless texture is worth the larger file.
- [ ] Paste `copy/google-promotional-text.txt`.
- [ ] Add translations only after the canonical English wording is approved.
- [ ] Add `https://nelsongrey.com/` as the official website.
- [ ] Use `Software & apps` as the developer-page label wherever the console provides an appropriate text field; do not bake it into the icon or header.
- [ ] Feature Modulo Squares only if its listing is published and broadly distributed in the intended countries.
- [ ] Preview the desktop and mobile crops. Google publishes no official safe-area dimensions, so verify the mark is not baked into a vulnerable edge.
- [ ] Save and capture the assigned shareable profile URL.
- [ ] Wait up to one hour for the preview and up to 24 hours for the first public page.
- [ ] Reopen the public page signed out and verify name, legal identity, public address, `hello@nelsongrey.com`, phone, `https://nelsongrey.com/`, featured app, and all listed apps.

## Apple

- [ ] Confirm the exact locked developer name and displayed provider/seller name.
- [ ] Do not search for a developer-profile logo or header upload; Apple exposes no comparable account-level fields.
- [ ] Set `https://nelsongrey.com/` or the appropriate live Nelson Grey portfolio page as the Marketing URL for each app localization.
- [ ] Keep each Support URL product-specific and confirm that it exposes the contact information Apple requires.
- [ ] Verify EU trader status and the public address, phone, and email shown in relevant storefronts.
- [ ] Use Apple's official marketing tools for badges, QR codes, short links, and store-branded assets.
- [ ] Consider audience-specific custom product pages rather than one generic screenshot story.
- [ ] Use product-page optimization for material icon/screenshot/preview decisions.
- [ ] Follow Apple's recommended minimum three-week lead time for featuring nominations tied to a real release, update, event, or developer story.
- [ ] Start from the two paste-ready Apple nomination text files, then add dates, release context, and live supplemental URLs.

## Portfolio site and press surfaces

- [ ] Use `web/nelson-grey-portfolio-hero-2400x1350.png` as the main brand hero.
- [ ] Use `social/nelson-grey-open-graph-1200x630.png` for Open Graph and social-card metadata.
- [ ] Keep `assets/nelson-grey-mark.svg`, the touch icon, PNG favicons, ICO, and the kit's Core export synchronized by running the renderer after any Core-mark change.
- [ ] Use `press/nelson-grey-press-cover-1920x1080.png` as the cover for press material or supplemental featuring links.
- [ ] Use official, product-specific store badges only after the destination listing is live.
- [ ] Keep product support contacts on product pages; keep the company contact on the portfolio/About page.
- [ ] Add actual social links only after handle ownership is verified.

## Final quality gate

```bash
./marketing/developer-profile-kit-2026-08/render-assets.sh
```

- [ ] `asset-manifest.csv` reports `PASS` for every raster deliverable.
- [ ] No logo asset contains a slogan or descriptor lockup.
- [ ] Every visual `Nelson Grey LLC` lockup inherits the standardized raised suffix; ordinary prose and platform fields remain inline.
- [ ] The developer mark matches the Core's internal geometry apart from the documented field, `N`, and Core-only keyline treatments.
- [ ] Both Google header files were rendered from deterministic `sources/header-art-master.svg`.
- [ ] The Google promotional text is no more than 140 characters.
- [ ] The Apple nomination description is no more than 1,000 characters.
- [ ] Apple Helpful Details are no more than 500 characters.
- [ ] Every linked website loads over HTTPS without a login or interstitial.
- [ ] Every public email and phone is actively monitored.
- [ ] No page claims an app is available on a storefront that is not live.
- [ ] No material shows a roadmap feature as current.
