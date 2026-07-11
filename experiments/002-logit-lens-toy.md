# Experiment 002: Logit-Lens Toy Baseline

Status: local toy implemented
Target paper: Verbalizable Representations Form a Global Workspace in Language Models
Local feasibility: high for toy experiment

## Goal

Build a small local experiment that approximates the simplest lensing idea: read intermediate hidden states through the model's output vocabulary.

This is not a reproduction of the Jacobian lens. It is a local baseline that helps build intuition before attempting richer methods.

## Minimal Version

Implemented as a dependency-free synthetic residual-stream toy:

1. Define a small concept space.
2. Define a vocabulary unembedding over that concept space.
3. Create layer-like hidden states: input, relation update, answer update.
4. Apply the same unembedding to every intermediate state.
5. Compare top-token readouts across layers.
6. Include one ambiguity case where early readouts are misleading.

Script:

```bash
python3 experiments/002-logit-lens-toy/run.py
python3 experiments/002-logit-lens-toy/run.py --markdown
```

## Why This Matters

The Global Workspace paper's J-lens is more sophisticated than the logit lens because it accounts for the causal map from intermediate residual-stream states to later final states.

But a logit-lens toy experiment is still useful because it makes the core question concrete:

Can intermediate activations be read as vocabulary-level concepts at all?

## Expected Output

- A small script or notebook.
- A table of layer-wise top-token readouts.
- A short note comparing logit lens, tuned lens, and J-lens.

## Reproduction Status

Local toy implemented. No claim of paper-level reproduction.

## First Run

Date: 2026-07-11
Environment: macOS, Python 3.9.6, no numpy/torch/transformers

The script runs without external dependencies and produces layer-wise vocabulary readouts for four controlled cases.

Key observation:

- In simple association cases, the top readout shifts from prompt concepts to answer concepts across synthetic layers.
- In the ambiguity case, early readouts over-focus on `paris`, while later states move toward `texas`.
- This demonstrates the intuition behind lensing, but also the danger: a vocabulary readout is not automatically a faithful explanation of the model's computation.

## Result Table

Generated with:

```bash
python3 experiments/002-logit-lens-toy/run.py --markdown
```

| Case | Layer | Top tokens | Note |
| --- | --- | --- | --- |
| `capital-france` | `layer_0_input` | france (0.91), place (0.84), paris (0.74), japan (0.52) | Answer concept becomes visible only after the relation layer. |
| `capital-france` | `layer_1_relation` | france (0.85), relation (0.66), place (0.65), paris (0.63) | Answer concept becomes visible only after the relation layer. |
| `capital-france` | `layer_2_answer` | paris (0.97), answer (0.70), france (0.70), tokyo (0.65) | Answer concept becomes visible only after the relation layer. |
| `sky-color` | `layer_0_input` | sky (0.94), color (0.88), blue (0.78), relation (0.14) | The readout shifts from the prompt entity to the expected answer. |
| `sky-color` | `layer_1_relation` | sky (0.86), color (0.70), blue (0.66), relation (0.61) | The readout shifts from the prompt entity to the expected answer. |
| `sky-color` | `layer_2_answer` | blue (0.97), sky (0.73), answer (0.68), color (0.53) | The readout shifts from the prompt entity to the expected answer. |
| `meow-animal` | `layer_0_input` | meow (0.92), animal (0.87), cat (0.76), relation (0.14) | A toy association task where the answer appears after a relation update. |
| `meow-animal` | `layer_1_relation` | meow (0.85), animal (0.68), cat (0.63), relation (0.62) | A toy association task where the answer appears after a relation update. |
| `meow-animal` | `layer_2_answer` | cat (0.97), meow (0.71), answer (0.70), animal (0.49) | A toy association task where the answer appears after a relation update. |
| `paris-texas` | `layer_0_input` | paris (0.91), france (0.81), place (0.78), tokyo (0.61) | A failure-style case: early readouts over-focus on Paris before disambiguation. |
| `paris-texas` | `layer_1_relation` | place (0.84), texas (0.79), ambiguous (0.71), paris (0.70) | A failure-style case: early readouts over-focus on Paris before disambiguation. |
| `paris-texas` | `layer_2_answer` | texas (0.96), answer (0.74), paris (0.69), tokyo (0.64) | A failure-style case: early readouts over-focus on Paris before disambiguation. |

## Interpretation

This toy makes the logit-lens idea concrete:

- The same output vocabulary can be used to read intermediate states.
- Readouts can change as the internal state changes.
- Early readouts can be suggestive but wrong.
- A top token is not automatically a belief, intention, or causal explanation.

The next real experiment should replace the synthetic states with hidden states from a tiny open model.
