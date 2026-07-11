# Experiment 002: Logit-Lens Toy Baseline

Status: planned
Target paper: Verbalizable Representations Form a Global Workspace in Language Models
Local feasibility: high for toy experiment

## Goal

Build a small local experiment that approximates the simplest lensing idea: read intermediate hidden states through the model's output vocabulary.

This is not a reproduction of the Jacobian lens. It is a local baseline that helps build intuition before attempting richer methods.

## Minimal Version

1. Use a tiny open model or a synthetic transformer.
2. Run a small set of controlled prompts.
3. Capture hidden states from each layer.
4. Apply the final unembedding matrix to intermediate hidden states.
5. Compare the top tokens across layers.
6. Write down where the method is informative and where it is misleading.

## Why This Matters

The Global Workspace paper's J-lens is more sophisticated than the logit lens because it accounts for the causal map from intermediate residual-stream states to later final states.

But a logit-lens toy experiment is still useful because it makes the core question concrete:

Can intermediate activations be read as vocabulary-level concepts at all?

## Expected Output

- A small script or notebook.
- A table of layer-wise top-token readouts.
- A short note comparing logit lens, tuned lens, and J-lens.

## Reproduction Status

Local toy experiment planned. No claim of paper-level reproduction.
