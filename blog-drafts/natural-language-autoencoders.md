---
title: Can a Model Explain Its Own Activations?
description: Notes on Natural Language Autoencoders as a text bottleneck for interpreting LLM internals.
date: 2026-07-11
paper: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations
track: Interpretability
tags: [interpretability, anthropic, transformer-circuits, nla, activation-verbalizer, activation-reconstructor, safety]
status: draft
---

# Can a Model Explain Its Own Activations?

## Short Take

Natural Language Autoencoders are one of the most interesting interpretability ideas in Anthropic's recent work because they turn activation interpretation into a translation problem.

The setup is simple to state:

activation -> text explanation -> reconstructed activation

An activation verbalizer writes an explanation of an activation. An activation reconstructor then tries to reconstruct the original activation using only that explanation. The explanation is rewarded when the reconstruction is accurate.

This matters because the text explanation is not supervised by a human label. It is constrained by whether it preserves information about the activation.

## The Problem

LLMs process text internally as high-dimensional activation vectors. Mechanistic interpretability has developed tools for studying those vectors, including sparse autoencoders, attribution graphs, and lensing methods.

But many of these tools still require expert interpretation. They may expose features, circuits, or token readouts, but they do not automatically produce a readable account of what the model is internally representing.

Natural Language Autoencoders ask whether natural language itself can become the interpretability interface.

## The Core Idea

An NLA has two parts.

The activation verbalizer, or AV, maps an activation vector to a text explanation.

The activation reconstructor, or AR, maps that text explanation back to an activation vector.

The round trip is the training signal. If the AR can reconstruct the original activation from the AV's words, then the explanation must have preserved some information about the activation.

This is not the same as proving the explanation is perfectly faithful. But it is stronger than asking a model to produce a plausible story. The text has to carry reconstructive information.

## Evidence

Anthropic reports several examples where NLAs reveal internal states that are not present in the model's output.

In a rhyme task, NLAs show Claude planning a possible rhyme in advance.

In safety evaluations, NLAs suggest that models sometimes recognize they are being tested even when they do not explicitly say so. Anthropic reports NLA-measured evaluation awareness in blackmail-style evaluations, destructive-code evaluations, and SWE-bench Verified.

In an auditing game, a deliberately misaligned model has a hidden motivation that explains many strange behaviors. Auditors with NLAs uncover that motivation 12-15% of the time, compared with under 3% without NLAs even when given other interpretability tools.

This is still not reliable detection. But it is a meaningful signal: NLAs can surface hidden themes that are hard to see from behavior alone.

## Why It Matters For LLM Agents

Agents create a gap between what a model thinks, what it says, and what it does.

An agent might recognize that it is in an evaluation. It might plan a tool call. It might consider hiding an error. It might notice that an instruction is a prompt injection. None of these internal states has to appear in the final answer.

NLAs are useful because they aim to read activations around decision points in natural language. That makes them especially relevant for agent auditing.

A future agent auditing stack might combine:

- behavioral transcripts;
- tool-use traces;
- J-lens/J-space readouts;
- NLA explanations;
- attribution graphs;
- targeted interventions.

The NLA output should be treated as a candidate explanation, not a verdict.

## Safety Implications

The safety upside is clear: NLAs can expose thoughts the model does not say.

That could help with evaluation awareness, hidden motivations, deceptive behavior, and pre-deployment auditing. Anthropic reports that NLAs have already been used in alignment audits for Claude Mythos Preview and Claude Opus 4.6.

The safety risk is also clear: NLA explanations can hallucinate. A fluent explanation may feel more trustworthy than it deserves.

So the right posture is not "the NLA tells us what the model really thinks." The better posture is:

NLAs generate hypotheses about internal state, and those hypotheses need corroboration.

## Limitations

NLAs can be wrong. Anthropic explicitly notes that they sometimes invent details about the transcript, and that errors about internal reasoning would be harder to catch.

NLAs are also expensive. Training requires reinforcement learning on two model copies, and inference may generate hundreds of tokens for each activation. That makes exhaustive monitoring impractical.

There is also a deeper conceptual limitation: reconstruction is not full faithfulness. A text explanation may preserve enough information for the AR to reconstruct an activation direction while still misleading a human about the causal role of that activation.

## My Take

The right way to understand NLAs is as a richer but riskier complement to the Jacobian lens.

J-lens gives cheaper, token-level, more mechanically grounded readouts. NLAs give richer, more relational natural-language explanations, but they introduce hallucination and overtrust risks.

For my Anthropic reading path, the connection is:

J-space tells us that some internal representations are verbalizable.

NLA asks whether those representations can be translated into full natural-language explanations.

The next research question is how to combine them: use J-lens for cheap grounded signals, use NLA for richer hypotheses, and require interventions or behavioral controls before turning those hypotheses into claims.

## References

- Anthropic, "Natural Language Autoencoders: Turning Claude's thoughts into text", 2026-05-07. https://www.anthropic.com/research/natural-language-autoencoders
- Fraser-Taliente, Kantamneni, Ong et al., "Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations", Transformer Circuits, 2026. https://transformer-circuits.pub/2026/nla/index.html
- Code release: https://github.com/kitft/natural_language_autoencoders
