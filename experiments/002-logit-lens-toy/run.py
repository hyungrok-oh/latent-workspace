#!/usr/bin/env python3
"""
Dependency-free toy logit-lens experiment.

This is not a reproduction of the Jacobian Lens paper. It is a small, local
baseline for building intuition about reading intermediate residual states
through an output vocabulary.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


Vector = List[float]


def add(a: Vector, b: Vector) -> Vector:
    return [x + y for x, y in zip(a, b)]


def scale(k: float, v: Vector) -> Vector:
    return [k * x for x in v]


def dot(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(v: Vector) -> float:
    return math.sqrt(dot(v, v))


def unit(v: Vector) -> Vector:
    n = norm(v)
    if n == 0:
        return v
    return [x / n for x in v]


def top_tokens(state: Vector, unembedding: Dict[str, Vector], k: int) -> List[Tuple[str, float]]:
    scored = [(token, dot(unit(state), unit(direction))) for token, direction in unembedding.items()]
    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]


@dataclass(frozen=True)
class PromptCase:
    name: str
    prompt: str
    input_concepts: List[str]
    relation_concepts: List[str]
    answer_concepts: List[str]
    note: str


DIRECTIONS: Dict[str, Vector] = {
    # Dimensions:
    # animal, place, color, relation, answer, france, japan, cat, sky, texas
    "animal": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "place": [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "color": [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "relation": [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "answer": [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "france": [0.0, 0.7, 0.0, 0.4, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    "paris": [0.0, 0.7, 0.0, 0.2, 0.9, 1.0, 0.0, 0.0, 0.0, 0.0],
    "japan": [0.0, 0.7, 0.0, 0.4, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
    "tokyo": [0.0, 0.7, 0.0, 0.2, 0.9, 0.0, 1.0, 0.0, 0.0, 0.0],
    "sky": [0.0, 0.1, 0.9, 0.3, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    "blue": [0.0, 0.0, 0.9, 0.1, 0.9, 0.0, 0.0, 0.0, 1.0, 0.0],
    "meow": [0.8, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    "cat": [0.8, 0.0, 0.0, 0.1, 0.9, 0.0, 0.0, 1.0, 0.0, 0.0],
    "texas": [0.0, 0.7, 0.0, -0.2, 0.9, 0.0, 0.0, 0.0, 0.0, 1.0],
    "ambiguous": [0.0, 0.6, 0.0, -0.6, 0.0, -0.2, 0.0, 0.0, 0.0, 0.7],
}


UNEMBEDDING: Dict[str, Vector] = {
    token: direction
    for token, direction in DIRECTIONS.items()
    if token
    in {
        "animal",
        "place",
        "color",
        "relation",
        "answer",
        "france",
        "paris",
        "japan",
        "tokyo",
        "sky",
        "blue",
        "meow",
        "cat",
        "texas",
        "ambiguous",
    }
}


CASES = [
    PromptCase(
        name="capital-france",
        prompt="What is the capital of France?",
        input_concepts=["france", "place"],
        relation_concepts=["relation"],
        answer_concepts=["paris", "answer"],
        note="Answer concept becomes visible only after the relation layer.",
    ),
    PromptCase(
        name="sky-color",
        prompt="What color is the clear daytime sky?",
        input_concepts=["sky", "color"],
        relation_concepts=["relation"],
        answer_concepts=["blue", "answer"],
        note="The readout shifts from the prompt entity to the expected answer.",
    ),
    PromptCase(
        name="meow-animal",
        prompt="Which animal says meow?",
        input_concepts=["meow", "animal"],
        relation_concepts=["relation"],
        answer_concepts=["cat", "answer"],
        note="A toy association task where the answer appears after a relation update.",
    ),
    PromptCase(
        name="paris-texas",
        prompt="Paris, Texas is in which US state?",
        input_concepts=["paris", "place"],
        relation_concepts=["ambiguous"],
        answer_concepts=["texas", "answer"],
        note="A failure-style case: early readouts over-focus on Paris before disambiguation.",
    ),
]


def sum_concepts(concepts: Iterable[str]) -> Vector:
    state = [0.0 for _ in next(iter(DIRECTIONS.values()))]
    for concept in concepts:
        state = add(state, DIRECTIONS[concept])
    return state


def states_for(case: PromptCase) -> List[Tuple[str, Vector]]:
    input_state = sum_concepts(case.input_concepts)
    relation_state = add(scale(0.75, input_state), sum_concepts(case.relation_concepts))
    answer_state = add(scale(0.4, relation_state), sum_concepts(case.answer_concepts))
    return [
        ("layer_0_input", input_state),
        ("layer_1_relation", relation_state),
        ("layer_2_answer", answer_state),
    ]


def markdown_table(k: int) -> str:
    lines = [
        "| Case | Layer | Top tokens | Note |",
        "| --- | --- | --- | --- |",
    ]
    for case in CASES:
        for layer, state in states_for(case):
            tokens = ", ".join(f"{token} ({score:.2f})" for token, score in top_tokens(state, UNEMBEDDING, k))
            lines.append(f"| `{case.name}` | `{layer}` | {tokens} | {case.note} |")
    return "\n".join(lines)


def plain_report(k: int) -> str:
    chunks = []
    for case in CASES:
        chunks.append(f"\n## {case.name}: {case.prompt}")
        chunks.append(case.note)
        for layer, state in states_for(case):
            tokens = ", ".join(f"{token}={score:.2f}" for token, score in top_tokens(state, UNEMBEDDING, k))
            chunks.append(f"- {layer}: {tokens}")
    return "\n".join(chunks).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--top-k", type=int, default=4)
    parser.add_argument("--markdown", action="store_true")
    args = parser.parse_args()

    if args.markdown:
        print(markdown_table(args.top_k))
    else:
        print(plain_report(args.top_k))


if __name__ == "__main__":
    main()
