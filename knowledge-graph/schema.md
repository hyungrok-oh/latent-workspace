# Knowledge Graph Schema

The knowledge graph connects papers, concepts, methods, risks, evaluations, mitigations, models, and implementation ideas.

## Node Types

- `paper`: a research paper, technical report, or official research post
- `concept`: an abstract idea such as faithful reasoning or goal conflict
- `method`: a technique such as circuit tracing or constitutional AI
- `risk`: a failure mode such as deception, jailbreak, or agentic misalignment
- `eval`: an evaluation setup, benchmark, probe, or experiment
- `model`: a model or model family
- `dataset`: data used for training, evaluation, or analysis
- `mitigation`: a safety intervention or defense
- `code`: reproducible implementation or experiment

## Edge Relations

- `introduces`: a paper introduces a concept, method, or evaluation
- `investigates`: a paper studies a concept or risk
- `supports`: evidence supports a claim
- `challenges`: evidence weakens or complicates a claim
- `mitigates`: a method reduces a risk
- `causes`: one factor contributes to another
- `measures`: an evaluation measures a behavior or risk
- `related_to`: loose but meaningful connection

## Minimal YAML Example

```yaml
nodes:
  - id: tracing_thoughts_language_model
    type: paper
    label: Tracing the thoughts of a large language model
    description: Anthropic research on circuit tracing in Claude.

  - id: circuit_tracing
    type: method
    label: Circuit Tracing
    description: A method for tracing model computations through interpretable features.

edges:
  - source: tracing_thoughts_language_model
    target: circuit_tracing
    relation: introduces
    evidence: The paper uses circuit tracing to analyze internal computations.
```
