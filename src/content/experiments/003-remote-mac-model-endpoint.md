---
title: "48GB Mac Remote Model Endpoint"
description: "An optional infrastructure plan for using a separate 48GB macOS machine as a local model endpoint."
date: 2026-07-11
status: "remote candidate"
target: "Lightweight open-model inference"
compute: "Separate 48GB macOS machine"
sourcePath: "experiments/003-remote-mac-model-endpoint.md"
---

## Goal

Use a separate 48GB macOS machine as a local-network model endpoint when the current laptop is too limited for model execution.

## Candidate Backends

- Ollama: easiest for text completion, weaker for activation access.
- llama.cpp server: good for local inference, limited internal activation access.
- MLX: strong fit for Apple Silicon models, potentially better for custom inspection.
- Custom Python HTTP service: more work, but can expose hidden states if the model stack supports it.

## Recommended Use

Use the 48GB Mac for:

- small model completions;
- prompt-response experiments;
- toy agent evaluations;
- activation extraction if using a framework that exposes hidden states.

Do not assume it will run NLA as-is. NLA's public path is likely CUDA-oriented.

## Status

Optional future infrastructure. Not required for the next local model experiment.
