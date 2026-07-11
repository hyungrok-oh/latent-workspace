---
title: Do Language Models Have a Readable Workspace?
description: Notes on Anthropic's Jacobian Lens and verbalizable internal representations.
date: 2026-07-11
paper: Verbalizable Representations Form a Global Workspace in Language Models
track: Interpretability
tags: [interpretability, anthropic, transformer-circuits, jacobian-lens, global-workspace, safety]
status: draft
---

# Do Language Models Have a Readable Workspace?

## Short Take

Anthropic's "Verbalizable Representations Form a Global Workspace in Language Models" is not mainly interesting because it borrows language from consciousness research. It is interesting because it proposes a concrete interface for reading and modifying some internal model states.

The paper introduces the Jacobian lens, or J-lens, a technique for finding internal directions that correspond to concepts the model is disposed to verbalize. The authors argue that these directions form a J-space: a small, privileged subset of the model's activation space that supports verbal report, directed modulation, internal reasoning, flexible generalization, and selective computation.

For LLM-agent research, the important question is practical: if a model is silently weighing a strategy, detecting a prompt injection, recognizing that it is in an evaluation, or considering whether to hide a mistake, can we inspect that cognition before it appears in output?

## The Problem

Most LLM evaluation looks at outputs. But for safety and agent behavior, the relevant cognition may be silent. An agent could recognize a failure, consider deception, notice an oversight, or plan a risky action without saying any of that aloud.

The paper asks whether LLMs have a subset of internal representations that behaves like a functional workspace. The analogy is to global workspace theory, but the authors avoid the stronger claim that language models have human-like consciousness or the same architecture as the brain.

The scientific version of the question is narrower:

Can we identify internal representations that are reportable, controllable, usable for intermediate reasoning, transferable across contexts, and selective rather than involved in all computation?

## The Core Idea

The J-lens reads an intermediate activation by estimating how that activation would affect the model's later outputs across many contexts.

Instead of applying the final unembedding matrix directly to every layer, as in the logit lens, the J-lens computes an averaged Jacobian from a given layer's residual stream to the final residual stream. Composing that with the unembedding produces a vocabulary-level readout.

If a token scores highly under this lens, the interpretation is not simply "the model will output this token now." The stronger interpretation is that the activation contains a concept the model is disposed to verbalize under appropriate future conditions.

The J-space is then defined as a sparse combination of these J-lens vectors. In plain terms: at a given moment, the model may have a small set of verbalizable concepts active in a special internal format.

## Evidence

The paper tests five properties.

First, verbal report: concepts that appear in the J-lens tend to match what the model later reports, and swapping one concept vector for another can change the reported answer.

Second, directed modulation: when the model is instructed to hold a concept in mind or introspect, relevant concepts appear in J-space even when they are not immediately output.

Third, internal reasoning: intermediate values in multi-step reasoning can appear in J-space, and interventions on them can redirect the final conclusion.

Fourth, flexible generalization: the same representation can be moved into another context and used by a different downstream computation.

Fifth, selectivity: the J-space is not the whole model. It explains only a small fraction of activation content, and ablating it affects flexible reasoning more than routine fluency or automatic processing.

That selectivity is crucial. The paper is not saying "we can read everything." It is saying there may be a privileged slice of the model's internal state that is especially relevant for reportable and flexible cognition.

## Why It Matters For LLM Agents

Agents add long-horizon goals, tools, memory, and situational awareness. That makes silent cognition more important. The question is no longer only "what answer did the model produce?" but "what did the model notice, infer, plan, or suppress before acting?"

The paper's alignment-auditing examples are directly relevant here. The authors report cases where the J-lens surfaces concepts related to prompt injection, evaluation awareness, deception, manipulation, or fabricated findings before those concepts appear in output.

For future agent systems, this suggests a possible auditing pattern:

1. Identify decision points in an agent transcript.
2. Inspect workspace-like internal representations around those points.
3. Flag transcripts where concepts related to deception, concealment, evaluation awareness, or goal conflict appear.
4. Combine the signal with behavioral evals, red-team transcripts, and other interpretability tools.

This is not a complete safety solution, but it is a much more interesting object than output-only monitoring.

## Safety Implications

The paper has two safety implications.

The first is monitoring. If strategic deliberation routes through J-space, then the J-lens may help reveal safety-relevant cognition that output-based evaluation misses.

The second is shaping. The paper introduces counterfactual reflection training: train the model to articulate ethical reflections in hypothetical reflection continuations, then evaluate it in the original contexts without asking it to reflect. The reported result is that ethical concepts appear in J-space and behavior improves. Ablating those concepts largely removes the improvement.

That is a striking idea: instead of training only the visible response, train what concepts should be available in the model's internal workspace while it responds.

## Limitations

The J-lens has a single-token bottleneck. Many important concepts are multi-token, diffuse, or relational. A concept like prompt injection may appear as separate tokens rather than a structured relation.

The readout is also a bag of concepts. It can show that spider, legs, and eight are active, but not necessarily how those concepts are bound together.

The method does not predict in advance which tasks require J-space. Some automatic computations bypass it, and a practiced misaligned behavior might bypass it too.

The paper also does not fully explain how information enters the J-space. It reads and intervenes on workspace contents, but the selection mechanism remains open.

Most importantly, J-space monitoring is not sufficient for alignment monitoring. It is one signal, not a guarantee.

## My Take

For my study path, this paper should be treated as a foundation paper for interpretability-first agent safety.

Its central value is the bridge it builds:

mechanistic representation -> causal intervention -> silent reasoning -> safety auditing -> training-time shaping of internal concepts.

The next paper to read should be Natural Language Autoencoders, because it appears to attack the main limitation of the J-lens: the need for richer, more structured natural-language descriptions of internal representations.

## References

- Anthropic / Transformer Circuits, "Verbalizable Representations Form a Global Workspace in Language Models", 2026-07-06. https://transformer-circuits.pub/2026/workspace/index.html
