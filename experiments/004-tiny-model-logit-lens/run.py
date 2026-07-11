#!/usr/bin/env python3
"""
Tiny-model logit-lens scaffold.

This script extracts hidden states from a small causal language model and reads
each layer through the model's output vocabulary. It is intended as the first
real-model step after the dependency-free toy experiment in 002.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import asdict, dataclass
from typing import Iterable, List


DEFAULT_MODEL = "sshleifer/tiny-gpt2"
DEFAULT_PROMPTS = [
    "The capital of France is",
    "The clear daytime sky is",
    "A cat says",
    "Paris, Texas is located in",
]


@dataclass(frozen=True)
class LayerReadout:
    prompt: str
    layer: int
    top_tokens: List[str]
    top_scores: List[float]


def module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def check_environment() -> int:
    checks = {
        "torch": module_available("torch"),
        "transformers": module_available("transformers"),
    }
    for name, available in checks.items():
        state = "ok" if available else "missing"
        print(f"{name}: {state}")

    if not all(checks.values()):
        print("\nInstall optional model dependencies before running activation extraction:")
        print("python3 -m venv .venv")
        print("source .venv/bin/activate")
        print("python -m pip install -r experiments/004-tiny-model-logit-lens/requirements.txt")
        return 2
    return 0


def choose_device(torch_module: object, requested: str) -> str:
    if requested != "auto":
        return requested
    if torch_module.backends.mps.is_available():
        return "mps"
    if torch_module.cuda.is_available():
        return "cuda"
    return "cpu"


def top_token_strings(tokenizer: object, token_ids: Iterable[int]) -> List[str]:
    tokens = []
    for token_id in token_ids:
        text = tokenizer.decode([int(token_id)])
        tokens.append(text.replace("\n", "\\n"))
    return tokens


def run_experiment(args: argparse.Namespace) -> List[LayerReadout]:
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError:
        sys.exit(check_environment())

    device = choose_device(torch, args.device)
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(args.model, output_hidden_states=True)
    model.to(device)
    model.eval()

    readouts: List[LayerReadout] = []
    for prompt in args.prompt:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)

        for layer_index, hidden_state in enumerate(outputs.hidden_states):
            last_token_state = hidden_state[0, -1, :]
            logits = model.lm_head(last_token_state)
            values, indices = torch.topk(logits, k=args.top_k)
            readouts.append(
                LayerReadout(
                    prompt=prompt,
                    layer=layer_index,
                    top_tokens=top_token_strings(tokenizer, indices.detach().cpu().tolist()),
                    top_scores=[round(float(value), 4) for value in values.detach().cpu().tolist()],
                )
            )

    return readouts


def print_markdown(readouts: List[LayerReadout]) -> None:
    print("| Prompt | Layer | Top tokens |")
    print("| --- | ---: | --- |")
    for readout in readouts:
        tokens = ", ".join(
            f"`{token}` ({score:.2f})"
            for token, score in zip(readout.top_tokens, readout.top_scores)
        )
        print(f"| `{readout.prompt}` | {readout.layer} | {tokens} |")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--prompt", action="append", default=None)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--device", default="auto", choices=["auto", "cpu", "mps", "cuda"])
    parser.add_argument("--markdown", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--check-env", action="store_true")
    args = parser.parse_args()

    if args.prompt is None:
        args.prompt = DEFAULT_PROMPTS
    return args


def main() -> None:
    args = parse_args()
    if args.check_env:
        sys.exit(check_environment())

    readouts = run_experiment(args)
    if args.json:
        print(json.dumps([asdict(readout) for readout in readouts], indent=2))
    elif args.markdown:
        print_markdown(readouts)
    else:
        for readout in readouts:
            pairs = ", ".join(
                f"{token}={score:.2f}"
                for token, score in zip(readout.top_tokens, readout.top_scores)
            )
            print(f"{readout.prompt} | layer {readout.layer}: {pairs}")


if __name__ == "__main__":
    main()
