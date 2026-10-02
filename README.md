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
- `games/<game-slug>/`: Privacy/Terms/Support pages for a published game that doesn't have its own site (e.g. `games/intercept-echo/`), reusing this site's design system; not linked from the main nav, only from that game's store listing and in-app links

## Run Locally

```bash
npm run dev
```

Open:

```text
http://127.0.0.1:4173
```

## Direction

The repository is intentionally scoped to support a modern, professional business homepage and related website assets, plus the legal/support pages for Nelson Grey's published games — not full per-game marketing sites (Modulo Squares' promotional site is its own separate repo/domain; games without one of their own get lightweight pages here instead, under `games/<game-slug>/`).

## Firebase Environments

This project is configured for Firebase Hosting across three environments:

- `dev` -> `nelson-grey-dev`
- `staging` -> `nelson-grey-staging`
- `prod` -> `nelson-grey-prod`

Configuration files:

- `.firebaserc`: project alias mapping
- `firebase.json`: hosting setup (static site + SPA rewrites)

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
