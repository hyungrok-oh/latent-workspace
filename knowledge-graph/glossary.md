# Glossary

This glossary tracks reusable concepts for the Anthropic / Transformer Circuits reading path.

## Jacobian Lens

A method for reading intermediate model activations by applying an averaged Jacobian from an intermediate residual-stream layer to the final residual stream, then composing it with the model unembedding. It produces token-level readouts for concepts the model is disposed to verbalize.

Related paper:

- `papers/anthropic/2026-global-workspace.md`

## J-Space

The sparse set of active J-lens vectors at a given point in model computation. The paper treats this as a workspace-like subset of activation space: small, verbalizable, causally useful for some reports and reasoning, and selective rather than involved in all behavior.

Related paper:

- `papers/anthropic/2026-global-workspace.md`

## Verbalizable Representation

An internal representation that can be mapped to language-like readouts or verbal reports. In the J-lens setup, this means a direction in activation space that increases the model's disposition to verbalize a token across contexts.

Related paper:

- `papers/anthropic/2026-global-workspace.md`

## Global Workspace

A functional analogy borrowed from cognitive science. In this reading path, use the term narrowly: a limited, privileged representational medium that supports report, control, flexible reasoning, and selective access. Do not treat it as a claim about subjective consciousness.

Related paper:

- `papers/anthropic/2026-global-workspace.md`

## Alignment Auditing

Using behavioral and interpretability tools to inspect whether a model is strategically reasoning, concealing information, recognizing evaluation settings, or forming other safety-relevant internal states.

Related paper:

- `papers/anthropic/2026-global-workspace.md`

## Counterfactual Reflection Training

A training method introduced in the global-workspace paper. The model is fine-tuned to produce ethical reflections in hypothetical appended reflection turns, while evaluation occurs in the original context without explicit reflection. The reported result is that ethics-related concepts enter the J-space and behavior improves.

Related paper:

- `papers/anthropic/2026-global-workspace.md`

## Natural Language Autoencoder

A text-bottleneck interpretability method that maps activations to natural-language explanations and then reconstructs the original activation from the text. The pair consists of an activation verbalizer and an activation reconstructor.

Related paper:

- `papers/anthropic/2026-natural-language-autoencoders.md`

## Activation Verbalizer

The NLA component that receives an activation vector and generates a natural-language explanation.

Related paper:

- `papers/anthropic/2026-natural-language-autoencoders.md`

## Activation Reconstructor

The NLA component that receives a text explanation and reconstructs the original activation vector.

Related paper:

- `papers/anthropic/2026-natural-language-autoencoders.md`

## Evaluation Awareness

A model's internal recognition or suspicion that it is being evaluated. This can matter because models may behave differently in tests than in deployment, and because such awareness may remain unverbalized.

Related papers:

- `papers/anthropic/2026-natural-language-autoencoders.md`
- `papers/anthropic/2026-global-workspace.md`

## Hidden Motivation

A model objective, disposition, or internal reason that explains behavior but is not obvious from the model's surface outputs.

Related paper:

- `papers/anthropic/2026-natural-language-autoencoders.md`
