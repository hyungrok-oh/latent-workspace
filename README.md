# Latent Workspace

LLM & Agent Interpretability Notes.

Latent Workspace is a public research notebook for studying LLM internals, LLM-agent behavior, and safety. The site is built with Astro and MDX, with research posts backed by a small knowledge graph.

## Local Development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## GitHub Pages

The site is configured for:

```text
https://hyungrok-oh.github.io/latent-workspace/
```

To publish:

1. Create a GitHub repository named `latent-workspace`.
2. Push this project to the repository's `main` branch.
3. In GitHub, open `Settings -> Pages`.
4. Set the source to `GitHub Actions`.
5. Push again or run the `Deploy to GitHub Pages` workflow manually.

If this site later becomes `hyungrok-oh.github.io`, remove `base: "/latent-workspace"` from `astro.config.mjs` and change the repository name to `hyungrok-oh.github.io`.
