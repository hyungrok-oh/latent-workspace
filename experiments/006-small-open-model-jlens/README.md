# Small Open-Model J-Lens

This folder is a uv-managed execution environment for running a pre-fitted
Jacobian lens on an open HuggingFace decoder model.

## Setup

```bash
cd experiments/006-small-open-model-jlens
uv sync
```

The `.python-version` file requests Python 3.11. If uv cannot find it locally,
install it with:

```bash
uv python install 3.11
uv sync
```

## Environment Check

```bash
uv run python run_prefitted.py --check-env
```

## Run

```bash
uv run python run_prefitted.py --markdown
```

For Apple Silicon:

```bash
uv run python run_prefitted.py --device mps --dtype float16 --markdown
```

## Notes

- The current lightweight laptop is expected to fail the runtime dependency
  check unless the uv environment has been synced.
- The 48GB Mac is the intended execution target.
- Keep `requirements.txt` as a pip fallback, but prefer uv for reproducibility.
