---
title: "Small Open-Model J-Lens Runbook"
description: "A 48GB Mac execution protocol for loading a pre-fitted Jacobian lens and comparing it against a vanilla logit-lens baseline."
date: 2026-07-12
status: "runbook"
target: "Official Jacobian Lens on an open-weights decoder model"
compute: "Current macOS laptop for env check; 48GB Mac for real execution"
sourcePath: "experiments/006-small-open-model-jlens.md"
---

## Goal

Turn the official `anthropics/jacobian-lens` code audit into an execution protocol.

This experiment is not a full reproduction of the Workspace paper. It is the first practical attempt to run the released J-lens method on an open model and compare it against a vanilla logit-lens baseline.

## Success Criteria

Minimum success:

- install the official `jlens` package;
- load an open HuggingFace decoder model;
- load a pre-fitted Jacobian lens;
- run one controlled prompt;
- print J-lens and vanilla logit-lens top tokens side by side.

Good success:

- run at least two prompts;
- inspect a mid-layer where J-lens is more interpretable than vanilla logit lens;
- paste the markdown output back into this note.

## UV Environment

This experiment is managed as a small uv project under `experiments/006-small-open-model-jlens/`.

Preferred setup:

```bash
cd experiments/006-small-open-model-jlens
uv sync
```

The `.python-version` file requests Python 3.11. If uv cannot find it:

```bash
uv python install 3.11
uv sync
```

## Current Laptop Check

```bash
cd experiments/006-small-open-model-jlens
uv run python run_prefitted.py --check-env
```

The current laptop is expected to fail the runtime dependency check. That is acceptable; it is for setup and documentation.

## 48GB Mac Setup

```bash
cd experiments/006-small-open-model-jlens
uv sync
uv run python run_prefitted.py --check-env
```

## Pre-Fitted Lens Path

Default command:

```bash
cd experiments/006-small-open-model-jlens
uv run python run_prefitted.py --markdown
```

Defaults follow the official walkthrough:

- model: `Qwen/Qwen3.5-4B`
- lens repo: `neuronpedia/jacobian-lens`
- lens revision: `qwen-n1000`
- lens file: `qwen3.5-4b/jlens/Salesforce-wikitext/Qwen3.5-4B_jacobian_lens_n1000.pt`

## Interpretation Rules

- Treat this as method validation, not a paper reproduction.
- Compare J-lens against `use_jacobian=False` vanilla logit lens.
- Look for systematic improvements across prompts, not one striking token.
- Record failures.
- Do not infer anything about Claude-scale behavior from a single small-model run.

## Result Log

No model run yet. Runbook and script scaffold implemented on the current laptop.
