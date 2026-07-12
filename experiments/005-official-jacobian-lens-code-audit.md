# Experiment 005: Official Jacobian Lens Code Audit

Status: code audit
Target: Anthropic `anthropics/jacobian-lens`
Local feasibility: high for code audit, low for fitting on current laptop, medium on 48GB Mac

## Goal

Audit Anthropic's official Jacobian Lens reference implementation and update the Workspace-paper study notes accordingly.

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

The important distinction:

- The full Claude-scale paper evidence is still not directly reproduced locally.
- The J-lens method itself is public and can be fitted/applied to open-weights decoder transformers.

## Confirmed From The Official Code

The README describes the code as a reference implementation and companion code for `Verbalizable Representations Form a Global Workspace in Language Models`.

It supports:

- fitting a Jacobian lens on open-weights decoder transformers;
- applying a fitted lens;
- comparing J-lens against a vanilla logit-lens baseline;
- rendering interactive layer-by-position slice visualizations;
- loading pre-fitted lenses from a HuggingFace-style repository;
- running against HuggingFace decoder layouts such as Llama/Qwen/Mistral/Gemma/OLMo/StableLM/Phi/GPT-2/GPT-NeoX-style models.

It does not bundle:

- model weights;
- the generic text corpus used to fit paper lenses;
- a maintained production package guarantee.

## Key Implementation Details

The lens is defined as:

```text
lens_l(h) = unembed(J_l @ h)
J_l = E[dh_final / dh_l]
```

The fitting implementation uses a specific estimator:

- replicate the prompt along the batch axis by `dim_batch`;
- run one forward pass;
- inject one-hot cotangents at every valid target position;
- backpropagate rows of the Jacobian in batches;
- at each source position, sum effects over current-and-future target positions;
- average over valid source positions;
- average per-prompt Jacobians over the prompt set.

The code excludes:

- the first 16 positions by default, because early positions can behave like attention sinks;
- the final position, because it has no next-token target.

Compute cost:

```text
one forward pass + ceil(d_model / dim_batch) backward passes per prompt
```

This means fitting is dominated by the model's backward pass. `dim_batch` is mainly the memory knob.

## Prompt And Evaluation Assets

The repo includes synthetic prompt sets for:

- verbal report;
- verbal introspection;
- directed modulation;
- top-down summoning;
- flexible generalization;
- selectivity;
- ignition;
- capacity;
- dual-task interference.

It also includes lens-quality evaluation prompts for:

- multihop reasoning;
- multilingual reasoning;
- poetry;
- order of operations;
- association;
- typo correction.

This is important because the public code contains not just the lens mechanics, but also a partial public scaffold for testing the paper's functional claims.

## Accuracy Audit Of Our Existing Notes

### Still Correct

- The paper's central claim is functional, not phenomenological.
- J-space should not be interpreted as consciousness.
- J-lens is stronger than pure decoding because the paper uses causal interventions.
- J-space is selective rather than a complete basis for all model computation.
- J-space auditing is useful but incomplete for safety.
- Single-token readout and bag-of-concepts structure are real limitations.

### Needs Correction

Our earlier wording was too pessimistic about reproduction.

Better wording:

```text
The central Claude-scale paper results are not directly reproduced locally, but the J-lens method is publicly released and can be fitted/applied to open-weights decoder transformers.
```

Our earlier local path treated J-lens as something we would approximate later. Now the right path is to audit and use the official implementation.

### Still Unknown

- Whether the 48GB Mac can fit a usable lens for a small open model in acceptable time.
- Whether small-model J-lens behavior will show the same functional ladder as the paper's Claude-scale examples.
- Whether pre-fitted Qwen lenses can be loaded and run locally without CUDA.
- Whether `transformers>=5.5` is easy to satisfy in the target environment.

## Practical Next Step

On the current laptop:

```bash
python3 --version
python3 -c "import torch"
python3 -c "import transformers"
```

On a 48GB Mac:

```bash
git clone https://github.com/anthropics/jacobian-lens
cd jacobian-lens
python3 -m venv .venv
source .venv/bin/activate
pip install -e . datasets
```

Then attempt one of two paths:

1. Load a pre-fitted Qwen lens from `neuronpedia/jacobian-lens`.
2. Fit a small local lens with around 100 WikiText prompts.

## Source Files Audited

- `README.md`
- `pyproject.toml`
- `jlens/fitting.py`
- `jlens/lens.py`
- `jlens/hf.py`
- `jlens/protocol.py`
- `jlens/examples.py`
- `data/experiments/README.md`
- `data/evaluations/README.md`
- `tests/test_fitting.py`
