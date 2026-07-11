---
title: "Logit-Lens Toy Baseline"
description: "A dependency-free synthetic residual-stream experiment for building intuition about vocabulary readouts."
date: 2026-07-11
status: "local toy"
target: "J-lens / workspace-style interpretability"
compute: "Current macOS laptop; dependency-free Python toy"
sourcePath: "experiments/002-logit-lens-toy.md"
---

## Goal

Build a tiny local baseline for reading intermediate states through an output vocabulary.

This is not a reproduction of the Jacobian lens. It is a concept check that makes the core idea concrete before moving to real model activations.

## Method

The script defines:

- a small concept space;
- vocabulary directions over that concept space;
- synthetic layer-like states for input, relation update, and answer update;
- a shared unembedding readout applied to every state.

Run:

```bash
python3 experiments/002-logit-lens-toy/run.py
python3 experiments/002-logit-lens-toy/run.py --markdown
```

## First Result

In simple association cases, the readout shifts from prompt concepts to answer concepts across synthetic layers. In the ambiguity case, early readouts over-focus on `paris`, while later states move toward `texas`.

## Interpretation

The toy demonstrates the intuition behind lensing, but also its danger: a vocabulary readout is not automatically a faithful explanation of a model's computation.

Useful rule:

- readouts can be suggestive;
- readouts can be wrong;
- causal claims need stronger evidence than top-token inspection.

## Next Step

Replace synthetic states with hidden states from a tiny open model.
