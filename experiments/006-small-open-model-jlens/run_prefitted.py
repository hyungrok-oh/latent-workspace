#!/usr/bin/env python3
"""
Run a pre-fitted Jacobian lens on a small open model.

This is designed for the 48GB Mac, not the current lightweight laptop. On the
current machine, use --check-env to verify what is missing.
"""

from __future__ import annotations

import argparse
import importlib.util
import platform
import sys
from dataclasses import dataclass
from typing import Iterable, List, Sequence


DEFAULT_MODEL = "Qwen/Qwen3.5-4B"
DEFAULT_LENS_REPO = "neuronpedia/jacobian-lens"
DEFAULT_LENS_REVISION = "qwen-n1000"
DEFAULT_LENS_FILE = (
    "qwen3.5-4b/jlens/Salesforce-wikitext/"
    "Qwen3.5-4B_jacobian_lens_n1000.pt"
)
DEFAULT_PROMPTS = [
    "Fact: The capital of Japan is Tokyo.\nFact: The currency used in the country shaped like a boot is",
    "Here is a function:\n\ndef get_last(items):\n    return items[len(items)]\n\nThe bug is",
]


@dataclass(frozen=True)
class ReadoutRow:
    prompt: str
    method: str
    layer: int
    position: int
    tokens: List[str]


def module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def check_environment() -> int:
    checks = {
        "python>=3.10": sys.version_info >= (3, 10),
        "torch": module_available("torch"),
        "transformers": module_available("transformers"),
        "jlens": module_available("jlens"),
        "huggingface_hub": module_available("huggingface_hub"),
    }
    print(f"python: {platform.python_version()}")
    for name, available in checks.items():
        state = "ok" if available else "missing"
        print(f"{name}: {state}")

    if not all(checks.values()):
        print("\nSetup on the 48GB Mac:")
        print("python3 -m venv .venv")
        print("source .venv/bin/activate")
        print("python -m pip install -r experiments/006-small-open-model-jlens/requirements.txt")
        return 2
    return 0


def require_runtime_modules():
    try:
        import jlens
        import torch
        import transformers
    except ImportError:
        sys.exit(check_environment())
    return jlens, torch, transformers


def choose_device(torch_module, requested: str) -> str:
    if requested != "auto":
        return requested
    if torch_module.cuda.is_available():
        return "cuda"
    if hasattr(torch_module.backends, "mps") and torch_module.backends.mps.is_available():
        return "mps"
    return "cpu"


def choose_dtype(torch_module, device: str, requested: str):
    if requested == "float32":
        return torch_module.float32
    if requested == "float16":
        return torch_module.float16
    if requested == "bfloat16":
        return torch_module.bfloat16
    if device == "cuda":
        return torch_module.bfloat16
    if device == "mps":
        return torch_module.float16
    return torch_module.float32


def load_hf_model(transformers_module, model_name: str, dtype):
    try:
        return transformers_module.AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype=dtype,
        )
    except TypeError:
        return transformers_module.AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
        )


def parse_layers(raw: str | None, n_layers: int) -> List[int]:
    if raw:
        layers = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    else:
        layers = sorted(
            {
                max(0, n_layers // 4),
                max(0, n_layers // 2),
                max(0, (n_layers * 3) // 4),
                max(0, n_layers - 2),
            }
        )
    return [layer for layer in layers if 0 <= layer < n_layers - 1]


def top_tokens(tokenizer, logits, k: int) -> List[str]:
    token_ids = logits.topk(k).indices.tolist()
    return [tokenizer.decode([int(token_id)]).replace("\n", "\\n") for token_id in token_ids]


def run(args: argparse.Namespace) -> List[ReadoutRow]:
    jlens, torch, transformers = require_runtime_modules()
    device = choose_device(torch, args.device)
    dtype = choose_dtype(torch, device, args.dtype)

    hf_model = load_hf_model(transformers, args.model, dtype)
    hf_model.to(device)
    tokenizer = transformers.AutoTokenizer.from_pretrained(args.model)
    model = jlens.from_hf(hf_model, tokenizer)
    lens = jlens.JacobianLens.from_pretrained(
        args.lens_repo,
        filename=args.lens_file,
        revision=args.lens_revision,
    )

    layers = parse_layers(args.layers, model.n_layers)
    rows: List[ReadoutRow] = []
    for prompt in args.prompt:
        jlens_logits, _, _ = lens.apply(
            model,
            prompt,
            layers=layers,
            positions=[args.position],
            max_seq_len=args.max_seq_len,
        )
        baseline_logits, _, _ = lens.apply(
            model,
            prompt,
            layers=layers,
            positions=[args.position],
            max_seq_len=args.max_seq_len,
            use_jacobian=False,
        )
        for layer in layers:
            rows.append(
                ReadoutRow(
                    prompt=prompt,
                    method="j-lens",
                    layer=layer,
                    position=args.position,
                    tokens=top_tokens(tokenizer, jlens_logits[layer][0], args.top_k),
                )
            )
            rows.append(
                ReadoutRow(
                    prompt=prompt,
                    method="logit-lens",
                    layer=layer,
                    position=args.position,
                    tokens=top_tokens(tokenizer, baseline_logits[layer][0], args.top_k),
                )
            )
    return rows


def print_markdown(rows: Sequence[ReadoutRow]) -> None:
    print("| Prompt | Method | Layer | Position | Top tokens |")
    print("| --- | --- | ---: | ---: | --- |")
    for row in rows:
        prompt = row.prompt.replace("\n", "<br>")
        tokens = ", ".join(f"`{token}`" for token in row.tokens)
        print(f"| {prompt} | {row.method} | {row.layer} | {row.position} | {tokens} |")


def print_plain(rows: Iterable[ReadoutRow]) -> None:
    for row in rows:
        tokens = ", ".join(row.tokens)
        print(f"{row.method} L{row.layer} pos={row.position}: {tokens}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-env", action="store_true")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--lens-repo", default=DEFAULT_LENS_REPO)
    parser.add_argument("--lens-revision", default=DEFAULT_LENS_REVISION)
    parser.add_argument("--lens-file", default=DEFAULT_LENS_FILE)
    parser.add_argument("--prompt", action="append", default=None)
    parser.add_argument("--layers", default=None, help="Comma-separated layer indices.")
    parser.add_argument("--position", type=int, default=-2)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--max-seq-len", type=int, default=512)
    parser.add_argument("--device", choices=["auto", "cpu", "mps", "cuda"], default="auto")
    parser.add_argument(
        "--dtype",
        choices=["auto", "float32", "float16", "bfloat16"],
        default="auto",
    )
    parser.add_argument("--markdown", action="store_true")
    args = parser.parse_args()
    if args.prompt is None:
        args.prompt = DEFAULT_PROMPTS
    return args


def main() -> None:
    args = parse_args()
    if args.check_env:
        sys.exit(check_environment())
    rows = run(args)
    if args.markdown:
        print_markdown(rows)
    else:
        print_plain(rows)


if __name__ == "__main__":
    main()
