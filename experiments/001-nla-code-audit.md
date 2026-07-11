# Experiment 001: NLA Code Audit

Status: planned
Target paper: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations
Local feasibility: code inspection and mock/schema tests only

## Goal

Understand the Natural Language Autoencoder implementation well enough to explain what can be run locally, what requires GPU compute, and what would count as a meaningful smoke test.

## Reality Check

The current machine is macOS without a dedicated NVIDIA GPU. Full NLA inference is likely not realistic here because the public quick start relies on SGLang serving and 7B+ model checkpoints.

A separate 48GB macOS machine may be useful later for lightweight open-model inference, but NLA's released path is still CUDA/SGLang-oriented. Treat the 48GB machine as a possible remote inference endpoint, not as a guaranteed reproduction environment.

## Audit Checklist

- Inspect `nla_inference.py`.
- Inspect `docs/inference.md`.
- Identify the expected parquet schema.
- Identify the AV and AR checkpoint metadata contract.
- Record model/layer/d_model assumptions.
- Separate inference-only requirements from training requirements.
- Determine whether a mock activation schema test can run locally.

## Expected Output

- A short feasibility report.
- A reproduction status label for the NLA blog post.
- A GPU run plan if real inference is worth attempting.

## Reproduction Status

Code audit planned. No real checkpoint execution yet.
