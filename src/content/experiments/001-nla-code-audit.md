---
title: "NLA Code Audit"
description: "A low-compute audit plan for understanding Natural Language Autoencoders before attempting GPU execution."
date: 2026-07-11
status: "code audit"
target: "Natural Language Autoencoders"
compute: "Current macOS laptop; no GPU required"
sourcePath: "experiments/001-nla-code-audit.md"
---

## Goal

Understand the Natural Language Autoencoders code path before trying to run the released checkpoints.

The first pass should focus on:

- activation-vector and activation-reconstruction interfaces;
- parquet activation schema;
- checkpoint metadata;
- inference entry points;
- assumptions about CUDA, SGLang, and hosted model dependencies.

## Why This Matters

NLA is attractive because it translates internal activations into natural language explanations. It is also compute-sensitive. A code audit lets us learn the architecture and failure modes without pretending that a laptop can reproduce the full paper.

## Local Plan

1. Inspect the public repository structure.
2. Identify inference scripts and checkpoint loading paths.
3. Record required runtime services.
4. Separate CPU-feasible inspection from GPU-required execution.
5. Write a feasibility report before attempting a real run.

## Current Status

Planned as a code audit. No GPU execution claim yet.
