# Security Policy

## Supported Versions

This repository holds the public-facing marketing website for Nelson Grey, an AI-fueled consulting and creative publishing company. Only the code currently deployed on each environment branch is supported — there is no long-term support for older commits.

| Branch | Environment | Status |
|---|---|---|
| `main` | Production | Supported |
| `staging` | Staging | Supported |
| `develop` | Development | Supported |

## Reporting a Vulnerability

This repository doesn't have a public issue tracker, so please don't report security concerns that way. Use one of:

- GitHub's [private vulnerability reporting](https://github.com/NelsonGrey/nelson-grey/security/advisories/new), or
- Email **support@nelsongrey.com**

Either way, include:

- A description of the vulnerability and its potential impact
- Steps to reproduce, or a proof of concept if available
- Any relevant logs, request/response samples, or affected endpoints

You should get an acknowledgement within a few business days.

## Automated Dependency Scanning

Dependabot alerts are enabled on this repository. Native GitHub secret scanning and code scanning (CodeQL) require GitHub Advanced Security, which isn't currently licensed for this org's private repositories, so neither is enabled here. Avoid committing credentials or secrets regardless — runtime secrets (e.g. the `FIREBASE_SERVICE_ACCOUNT` deploy key) are managed via GitHub Actions secrets scoped per GitHub Environment, never committed to source.
