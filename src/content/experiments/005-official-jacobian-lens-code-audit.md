---
title: "Official Jacobian Lens Code Audit"
description: "A code audit of Anthropic's public jacobian-lens reference implementation and what it changes about the reproduction plan."
date: 2026-07-12
status: "code audit"
target: "Anthropic jacobian-lens reference implementation"
compute: "Current macOS laptop for audit; 48GB Mac recommended for fitting"
sourcePath: "experiments/005-official-jacobian-lens-code-audit.md"
---

## Goal

Audit Anthropic's official Jacobian Lens reference implementation and update the Workspace-paper study plan.

Repository:

- https://github.com/anthropics/jacobian-lens

## Verdict

The repository materially changes the reproduction plan.

Earlier plan:

```text
toy logit lens -> tiny-model logit lens -> later J-lens approximation
```

Updated plan:

```text
toy logit lens -> tiny-model logit lens -> official J-lens code audit -> small open-model J-lens fit
```

The important distinction is that the full Claude-scale paper evidence is still not directly reproduced locally, but the J-lens method itself is public and can be fitted or applied to open-weights decoder transformers.

## Confirmed From The Official Code

The code supports:

- fitting a Jacobian lens on open-weights decoder transformers;
- applying a fitted lens;
- comparing J-lens against a vanilla logit-lens baseline;
- rendering interactive layer-by-position slice visualizations;
- loading pre-fitted lenses from a HuggingFace-style repository;
- running against common HuggingFace decoder layouts, including GPT-2-style models.

It does not bundle model weights or the generic text corpus used to fit paper lenses.

## Key Implementation Detail

The lens is defined as:

```text
lens_l(h) = unembed(J_l @ h)
J_l = E[dh_final / dh_l]
```

The implementation estimates `J_l` by injecting one-hot cotangents at valid target positions, backpropagating Jacobian rows in batches, summing effects over current-and-future target positions, averaging over valid source positions, and then averaging across prompts.

Fitting cost:

```text
one forward pass + ceil(d_model / dim_batch) backward passes per prompt
```

So fitting is dominated by model backward passes. `dim_batch` is mainly the memory knob.

## Accuracy Audit

Our existing Workspace interpretation is broadly sound:

- the claim is functional, not a claim about consciousness;
- causal interventions are central;
- selectivity matters;
- J-space is useful but incomplete for safety auditing;
- single-token readout and bag-of-concepts structure remain limitations.

The main correction is reproducibility:

```text
The central Claude-scale paper results are not directly reproduced locally, but the J-lens method is publicly released and can be fitted/applied to open-weights decoder transformers.
```

## Next Step

Use the 48GB Mac for one of two paths:

1. Load a pre-fitted Qwen lens from `neuronpedia/jacobian-lens`.
2. Fit a small local lens with around 100 WikiText prompts.

The current laptop remains useful for code audit and blog documentation, but not for meaningful fitting.
