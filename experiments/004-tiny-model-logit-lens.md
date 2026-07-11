# Experiment 004: Tiny-Model Logit Lens

Status: activation scaffold
Target paper: Verbalizable Representations Form a Global Workspace in Language Models
Local feasibility: medium on current macOS laptop, high on 48GB macOS machine

## Goal

Move from the dependency-free toy experiment to a real model whose hidden states can be inspected.

This is still not a reproduction of the Jacobian lens. It is a practical bridge:

- use an open causal language model;
- capture hidden states from every layer;
- project each layer's final-token hidden state through the model's language-model head;
- compare the top vocabulary readouts across layers;
- document where the readout is stable, misleading, or prompt-sensitive.

## Default Model

The scaffold defaults to `sshleifer/tiny-gpt2` because it is small enough to test the pipeline. It is not scientifically interesting by itself. Once the pipeline works, replace it with a stronger small model.

Good next candidates:

- `distilgpt2`
- `gpt2`
- a small Qwen or Llama-family model that runs comfortably on the 48GB Mac

## Environment Check

On the current laptop, run:

```bash
python3 experiments/004-tiny-model-logit-lens/run.py --check-env
```

Expected current result:

```text
torch: missing
transformers: missing
```

That is fine. The script is intentionally optional-dependency based so the blog repo can still build without model libraries.

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

For a specific model:

```bash
python experiments/004-tiny-model-logit-lens/run.py \
  --model distilgpt2 \
  --prompt "The capital of France is" \
  --markdown
```

## Output Contract

Each row records:

- prompt;
- layer index;
- top decoded vocabulary tokens;
- raw LM-head scores.

The first useful analysis is not whether a token appears once, but whether the readout changes systematically across layers and across prompt variants.

## Interpretation Rules

- Treat this as a readout, not a causal explanation.
- A high top token does not prove that the model "believes" that token.
- Compare multiple prompt phrasings before making claims.
- Use ambiguity cases to find failure modes.
- Do not present tiny-model results as evidence about frontier LLM internals.

## Reproduction Status

Scaffold implemented. Current laptop can run the environment check, but full activation extraction needs optional model dependencies.
