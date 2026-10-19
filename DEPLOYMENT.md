# Deployment Workflow

## Branch strategy
- `feature/*`: New feature development branch
- `dev`: Integration branch for developing features
- `staging`: Pre‑production test environment
- `main`: Production branch

### Flow
1. Developer creates feature branch from `dev`
2. Open Pull Request to `dev`
   - Trigger CI pipeline: ruff lint + black format check + pytest + docker build check
   - CI must pass before merge
3. Merge feature → dev
4. Open PR from dev → staging
   - Run CI checks again
5. Merge to `staging` → CD pipeline triggers
   - Generate staging `.env` from GitHub Secrets
   - Build staging docker image
6. Open PR from staging → main
   - Run CI checks
7. Merge to `main` → CD pipeline triggers
   - Generate production `.env` from GitHub Secrets
   - Build production docker image

## Trigger mapping
- Pull Request to `dev/staging/main`: run CI pipeline (.github/workflows/ci.yml)
- Push merge commit to `staging`: run CD build staging image
- Push merge commit to `main`: run CD build production image
