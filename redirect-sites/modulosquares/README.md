# modulosquares.com redirect site

Redirect-only Firebase Hosting site (`modulosquares-redirect` in `nelson-grey-prod`) serving
modulosquares.com after the game moved to `nelsongrey.com/games/modulo-squares/`.
Config: `/firebase.modulosquares.json`. Keep the domain for at least a year.

- Old paths 301 to their nelsongrey.com equivalents (`/how-it-works` -> `/how-to-play`;
  `/download`, `/pricing`, `/leaderboard` -> game home).
- `app-ads.txt` is served here directly (AdMob does not follow cross-domain redirects).
- Unknown paths get a 404 page that links to the new home.
- Redirects take precedence over static files in Firebase Hosting, so never add a catch-all redirect.

Deploy: `firebase deploy --only hosting --config firebase.modulosquares.json --project prod`
