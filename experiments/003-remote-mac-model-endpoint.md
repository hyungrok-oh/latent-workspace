# Experiment 003: Remote 48GB Mac Model Endpoint

Status: optional
Target: lightweight open-model inference
Local feasibility: depends on separate 48GB macOS machine availability

## Goal

Use a separate 48GB macOS machine as a local-network model endpoint when the current laptop is too limited for model execution.

## Candidate Backends

- Ollama: easiest for text completion, weaker for activation access.
- llama.cpp server: good for local inference, limited internal activation access.
- MLX: strong fit for Apple Silicon models, potentially better for custom inspection.
- Custom Python/HTTP service: more work, but can expose hidden states if the model stack supports it.

## Recommended Use

Use the 48GB Mac for:

- small model completions;
- prompt-response experiments;
- toy agent evaluations;
- possibly activation extraction if using a framework that exposes hidden states.

Do not assume it will run NLA as-is. NLA's public path is built around SGLang and released checkpoints that are likely CUDA-oriented.

## Expected Output

- A small endpoint contract.
- A health-check script.
- A decision note: completion-only endpoint or activation-capable endpoint.

## Reproduction Status

Optional future infrastructure. Not required for the next local toy experiment.
