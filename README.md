# Nelson Grey Website

[![License](https://img.shields.io/badge/license-proprietary-lightgrey.svg)](https://github.com/NelsonGrey/nelson-grey/blob/develop/LICENSE)

## Contents

- [Stack](#stack)
- [Project Files](#project-files)
- [Run Locally](#run-locally)
- [Direction](#direction)
- [Firebase Environments](#firebase-environments)
  - [First-Time Setup](#first-time-setup)
  - [Deploy Commands](#deploy-commands)
  - [Automated Deploys](#automated-deploys)

This repository contains the public-facing business website for Nelson Grey, an artificial intelligence fueled consulting and creative publishing company.

## Stack

- Static HTML, CSS, and JavaScript
- Lightweight local Node.js static server

## Project Files

- `index.html`: Main website markup
- `styles.css`: Visual system, layout, and responsive styling
- `app.js`: Interaction behavior (mobile navigation, reveal animations, contact UX)
- `dev-server.js`: Local static server for development and preview
- `marketing/developer-profile-kit-2026-08/`: Working developer-profile brand, platform, and promotional assets; excluded from Firebase Hosting
- `games/index.html`: Games hub linked from the main navigation
- `games/<game-slug>/`: Public pages for a Nelson Grey game, reusing this site's design system and linked from `/games`

## Run Locally

```bash
npm run dev
```

Open:

```text
http://127.0.0.1:4173
```

## Direction

The repository holds the public Nelson Grey site and the game pages under `games/<game-slug>/`. The Games page in the main navigation links to those games. The old modulosquares.com host is configured in the separate Modulo Squares repository, not here.

## Firebase Environments

This project is configured for Firebase Hosting across three environments:

- `dev` -> `nelson-grey-dev`
- `staging` -> `nelson-grey-staging`
- `prod` -> `nelson-grey-prod`

Configuration files:

- `.firebaserc`: project alias mapping
- `firebase.json`: hosting setup (static site, clean URLs, and a real 404 for unknown paths)

### First-Time Setup

```bash
npm run firebase:login
```

### Deploy Commands

```bash
npm run firebase:deploy:dev
npm run firebase:deploy:staging
npm run firebase:deploy:prod
```

### Automated Deploys

[`.github/workflows/firebase-deploy.yml`](.github/workflows/firebase-deploy.yml)
deploys automatically on push:

- `develop` -> `nelson-grey-dev`
- `staging` -> `nelson-grey-staging`
- `main` -> `nelson-grey-prod`

Promote a change through environments by merging forward:
`develop` -> `staging` -> `main`.

Each job authenticates with a Firebase service account key stored as the
`FIREBASE_SERVICE_ACCOUNT` secret on the corresponding GitHub Environment
(`development`, `staging`, `production`). To set this up:

1. Create a service account with the **Firebase Hosting Admin** role on
   each Firebase project (or one service account per project).
2. Generate a JSON key for each and paste its contents into the
   `FIREBASE_SERVICE_ACCOUNT` secret on the matching GitHub Environment
   under repo Settings -> Environments.

## Environment protection

GitHub branch protection is unavailable on this repo's plan, so protection lives in the deploy and in the hosting layer instead.

- **Access gate (dev and staging only).** The deploy workflow injects a Google sign-in wall (`assets/auth-gate.js`) into every page of the `nelson-grey-dev` and `nelson-grey-staging` copies. The allowlist comes from the `ALLOWED_EMAIL_DOMAINS` and `ALLOWED_EMAILS` secrets of the `development` / `staging` GitHub Environments and is written to `assets/env-config.js` at deploy time. An empty allowlist fails the deploy. This keeps the public out; it is not a hard auth boundary because the allowlist ships to the browser. Production is never gated.
- **Hosting policy.** `firebase.dev.json` and `firebase.staging.json` add security headers and `noindex`; the workflow copies the right one to `firebase.json`.
- **Keyless deploys (dev and staging).** The workflow authenticates with Workload Identity Federation as `github-deploy@<project>`, trusted only for this repository and that environment's branch. `WIF_PROVIDER` is a variable on each GitHub Environment. Production still uses the `FIREBASE_SERVICE_ACCOUNT` key.
- **CI checks (advisory).** `ci.yml` validates the site and config, scans history with gitleaks, and flags PRs that skip an environment (`develop` → `staging` → `main`). Without branch protection these cannot block a merge.
