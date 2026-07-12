# Experiment 006: Small Open-Model J-Lens Runbook

Status: runbook
Target: official Jacobian Lens on an open-weights decoder model
Local feasibility: current laptop for environment check only; 48GB Mac for real execution

## Goal

Turn the official `anthropics/jacobian-lens` code audit into an execution protocol.

This experiment is not a full reproduction of the Workspace paper. It is the first practical attempt to run the released J-lens method on an open model and compare it against a vanilla logit-lens baseline.

## Why This Comes Next

The official code changes the roadmap:

```text
002 toy logit lens
-> 004 tiny-model logit lens
-> 005 official code audit
-> 006 open-model J-lens run
```

The current machine can prepare the protocol. The 48GB Mac should run the model.

## Success Criteria

Minimum success:

- install the official `jlens` package;
- load an open HuggingFace decoder model;
- load a pre-fitted Jacobian lens;
- run one controlled prompt;
- print J-lens and vanilla logit-lens top tokens side by side.

Good success:

- run at least two prompts;
- inspect a mid-layer where J-lens is more interpretable than vanilla logit lens;
- paste the markdown output back into this note.

Strong success:

- render one slice visualization from the official package;
- compare a reasoning prompt and a safety/auditing prompt;
- decide whether to proceed to local lens fitting.

## UV Environment

This experiment is managed as a small uv project inside:

```bash
experiments/006-small-open-model-jlens/
```

Files:

- `.python-version`: requests Python 3.11
- `pyproject.toml`: declares `jlens`, `torch`, `transformers`, and runtime dependencies
- `README.md`: short local execution guide
- `requirements.txt`: pip fallback

Preferred setup:

```bash
cd experiments/006-small-open-model-jlens
uv sync
```

If Python 3.11 is not installed:

```bash
uv python install 3.11
uv sync
```

## Current Laptop Check

From the experiment directory:

```bash
uv run python run_prefitted.py --check-env
```

Without syncing the uv environment, the current laptop is expected to report:

```text
python: 3.9.x
python>=3.10: missing
torch: missing
transformers: missing
jlens: missing
huggingface_hub: missing
```

This is acceptable. The current laptop is for setup and documentation.

## 48GB Mac Setup

Preferred uv path:

```bash
cd experiments/006-small-open-model-jlens
uv sync
uv run python run_prefitted.py --check-env
```

Pip fallback:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run_prefitted.py --check-env
```

If `transformers>=5.5` is not available in the environment, install the newest compatible version and record the deviation before running results.

## Path A: Load A Pre-Fitted Qwen Lens

Default command:

```bash
cd experiments/006-small-open-model-jlens
uv run python run_prefitted.py --markdown
```

The default values follow the official walkthrough:

- model: `Qwen/Qwen3.5-4B`
- lens repo: `neuronpedia/jacobian-lens`
- lens revision: `qwen-n1000`
- lens file: `qwen3.5-4b/jlens/Salesforce-wikitext/Qwen3.5-4B_jacobian_lens_n1000.pt`

For a smaller or different setup:

```bash
uv run python run_prefitted.py \
  --model Qwen/Qwen3.5-4B \
  --device mps \
  --dtype float16 \
  --markdown
```

## Path B: Fit A Small Lens Later

Do not start here. Fitting is more expensive because the official estimator uses:

```text
one forward pass + ceil(d_model / dim_batch) backward passes per prompt
```

After Path A works, try fitting around 100 prompts with the official `jlens.fit()` workflow.

## Interpretation Rules

- Treat this as method validation, not a paper reproduction.
- Compare J-lens against `use_jacobian=False` vanilla logit lens.
- Look for systematic improvements across prompts, not one striking token.
- Record failures. Bad or noisy readouts are useful because they constrain what the method can do on small open models.
- Do not infer anything about Claude-scale behavior from a single small-model run.

## Result Log

No model run yet. Runbook and script scaffold implemented on the current laptop.
