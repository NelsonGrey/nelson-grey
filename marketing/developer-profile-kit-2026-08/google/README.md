# Google Play Developer Profile package

## Direct uploads

| Field | Preferred file/value |
|---|---|
| Developer icon | `developer-icon-512x512.png` |
| Header image | `developer-header-4096x2304.jpg` for a smaller upload, or the lossless PNG |
| Promotional text | `../copy/google-promotional-text.txt` |
| Website | `https://nelsongrey.com/` |
| Developer-page label | `Software & apps` where an appropriate text field is available |
| Public contact | `hello@nelsongrey.com` |
| Featured app | Modulo Squares only after publication and country-distribution verification |

`developer-profile-preview-1600x1200.png` is a concept preview, not an upload. Google controls the final page layout.

The developer icon uses the dark build-environment colorway documented in `../DEVELOPER_MARK.md`. Its geometry is identical to the official Nelson Grey mark: the field is `#101722`, the `N` is `#F8F4EA`, and the original teal and gold are unchanged. It is intentionally different from every app icon. Do not use it in the Play app-icon field.

`Software & apps` is page copy, not a slogan or logo descriptor. Do not bake it into the icon or header. Keep `marknelson@nelsongrey.com` private as the account owner/login only.

## Preflight facts

- At least one published app is required before the profile can be created.
- The 512 × 512 developer icon is a 32-bit PNG.
- The 4096 × 2304 header is supplied as both 24-bit PNG without alpha and JPEG.
- The promotional text is validated within the allowed 140 characters.
- Google publishes no official header safe-area dimensions, so the recommended header keeps the center quiet and contains no baked-in words or logo.
- Both header formats are deterministically rendered from `../sources/header-art-master.svg`.
- The initial profile may take up to 24 hours to become public.

Complete the organization-contact and signed-out public-page checks in `../UPLOAD_CHECKLIST.md` before sharing the assigned profile URL.
