---
title: "Tiny-Model Logit Lens"
description: "A real-model scaffold for extracting hidden states from a small causal language model and reading each layer through the model vocabulary."
date: 2026-07-11
status: "activation scaffold"
target: "Open-model hidden-state readouts"
compute: "Current macOS laptop for env check; 48GB Mac recommended for real runs"
sourcePath: "experiments/004-tiny-model-logit-lens.md"
---

## Goal

Move from the dependency-free toy experiment to a real model whose hidden states can be inspected.

This is still not a reproduction of the Jacobian lens. It is a practical bridge:

- use an open causal language model;
- capture hidden states from every layer;
- project each layer's final-token hidden state through the model's language-model head;
- compare top vocabulary readouts across layers;
- document where the readout is stable, misleading, or prompt-sensitive.

## Default Model

The scaffold defaults to `sshleifer/tiny-gpt2` because it is small enough to test the pipeline. It is not scientifically interesting by itself. Once the pipeline works, replace it with a stronger small model such as `distilgpt2`, `gpt2`, or a small model that runs comfortably on the 48GB Mac.

## Environment Check

```bash
python3 experiments/004-tiny-model-logit-lens/run.py --check-env
```

On the current laptop, the expected result is:

```text
torch: missing
transformers: missing
```

That is fine. The script is optional-dependency based so the blog repo can still build without model libraries.

## Setup on a Model-Capable Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r experiments/004-tiny-model-logit-lens/requirements.txt
```

Then run:

```bash
python experiments/004-tiny-model-logit-lens/run.py --markdown
```

## Interpretation Rules

- Treat this as a readout, not a causal explanation.
- A high top token does not prove that the model believes that token.
- Compare multiple prompt phrasings before making claims.
- Use ambiguity cases to find failure modes.
- Do not present tiny-model results as evidence about frontier LLM internals.

## Reproduction Status

Scaffold implemented. Current laptop can run the environment check, but full activation extraction needs optional model dependencies.
