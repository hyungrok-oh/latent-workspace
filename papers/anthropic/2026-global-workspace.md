# Verbalizable Representations Form a Global Workspace in Language Models

URL: https://transformer-circuits.pub/2026/workspace/index.html
Date: 2026-07-06
Organization: Anthropic / Transformer Circuits
Track: Interpretability
Status: analysis-notes

## One-Sentence Claim

Large language models appear to maintain a small, privileged set of verbalizable internal representations, called the J-space, that can be read, modified, and used for report, modulation, internal reasoning, flexible generalization, and selective computation.

## Why This Paper Matters

This is the first priority study target because it directly addresses whether language models contain internal representations that are verbalizable, shared across tasks, and potentially usable as a "workspace" for reasoning-like computation.

For my research direction, this paper is a bridge between mechanistic interpretability and LLM-agent safety. If strategically relevant thoughts, evaluation awareness, or ethical principles appear in a readable internal workspace before they appear in output, then interpretability tools may become part of agent auditing rather than just post-hoc explanation.

## Problem

The central problem is whether LLMs have internal representations that play a special computational role analogous to a global workspace: a limited, reportable, controllable, flexible medium for intermediate reasoning.

The paper does not ask whether models are conscious in a phenomenological sense. It uses global workspace theory as a functional comparison point: can some internal contents be made available for report, control, and flexible downstream use while most processing remains automatic and inaccessible?

## Method

The paper introduces the Jacobian lens, or J-lens, to identify representations that the model is poised to verbalize.

At a high level:

1. For each layer, compute an averaged Jacobian mapping from an intermediate residual-stream activation to later final-layer residual-stream states.
2. Compose that averaged Jacobian with the model's unembedding to score vocabulary tokens.
3. Interpret high-scoring tokens as concepts the activation is disposed to make the model say across contexts.
4. Define J-lens vectors as token-indexed directions in residual-stream space.
5. Define the J-space as sparse nonnegative combinations of active J-lens vectors.
6. Use the J-lens both for reading and writing: read concept tokens from activations, steer along J-lens vectors, ablate them, or swap one concept's lens coordinate with another.

The key methodological distinction from the logit lens is that the J-lens corrects for representational changes across layers by using an averaged causal linear map rather than applying the final unembedding directly to every layer.

## Main Evidence

The paper tests five functional properties.

1. Verbal report
   - If the model is about to report a chosen concept, that concept appears in the J-lens.
   - Swapping a chosen concept vector for another can redirect what the model reports.

2. Directed modulation
   - Instructions to hold a concept in mind, introspect, or do mental calculation activate relevant J-space contents even when they are not directly output.
   - Injecting a J-lens vector can make the model later report that concept when asked to introspect.

3. Internal reasoning
   - Intermediate results of multi-step reasoning can appear in the J-space.
   - Interventions on these representations can redirect downstream conclusions.

4. Flexible generalization
   - A J-space representation from one context can be moved into another context and used as an argument to different downstream computations.

5. Selectivity
   - The J-space explains only a small fraction of activation variance.
   - Ablating J-space contents damages some flexible/internal reasoning tasks while leaving much routine processing, parsing, fluency, and automatic computation relatively intact.

The paper also applies the J-lens to alignment-auditing scenarios. It reports that strategic or situational assessments such as evaluation awareness, manipulation, panic, fake/fabricated behavior, or prompt-injection recognition can appear in the J-space even when they are absent from surface text.

Finally, the paper introduces counterfactual reflection training. The model is trained to produce ethical reflections only in counterfactual appended reflection turns, but its behavior improves in the original uninterrupted contexts. The authors report that ethics/reflection concepts then appear in the J-space, and ablating those concepts largely removes the behavioral improvement.

## What The Paper Shows

The paper shows evidence that a subset of LLM internal representations is:

- verbalizable through J-lens readouts;
- causally involved in some verbal reports;
- modifiable through vector interventions;
- used in at least some intermediate reasoning and flexible task routing;
- limited and selective rather than globally involved in all model behavior;
- potentially useful for detecting silent alignment-relevant cognition.

The strongest part of the paper is not just that concept tokens can be decoded from activations. The stronger claim is causal: modifying J-space contents can modify reports, conclusions, and some safety-relevant behaviors.

## What The Paper Does Not Show

It does not show that LLMs have human-like consciousness, subjective experience, or the full architecture proposed by global workspace theory in neuroscience.

It does not show that all reasoning routes through J-space. In fact, the paper emphasizes that many automatic computations do not.

It does not show that J-lens monitoring is sufficient for safety. A misaligned policy could become automatic, avoid verbalizable representations, or use concepts that do not map cleanly to single-token J-lens vectors.

It does not fully explain how representations enter the J-space. The paper reads and intervenes on workspace contents, but the selection mechanism remains open.

## Deep Analysis

The most important interpretive move is to separate three claims:

1. Method claim: the J-lens identifies directions associated with potential verbalization.
2. Functional claim: those directions support report, modulation, reasoning, generalization, and selectivity.
3. Workspace claim: this functional bundle is sufficiently similar to a global workspace to justify the analogy.

The method claim is the most concrete. The workspace claim is the most interesting, but also the easiest to overstate.

My current interpretation is that the J-space is a measurable control surface rather than a complete map of the model's cognition. This is still valuable. A partial control surface can support auditing, interventions, and training-time shaping. But it should not be treated as a complete monitor of agent intent.

### Evidence Strength

The evidence is strongest when it climbs from readout to intervention:

- a concept appears in the J-lens;
- swapping or ablating the corresponding coordinate changes report or behavior;
- the same representation can be moved across contexts and operated on by downstream computation;
- suppressing the J-space selectively damages flexible reasoning more than automatic processing.

The selectivity result is especially important. If the J-space were necessary for everything, it would be hard to tell whether it was a workspace or just a generic activation basis. The fact that routine fluency and parsing can remain relatively intact makes the functional claim sharper.

### Hidden Assumptions

- Averaged Jacobians capture context-general verbalization dispositions rather than context-specific artifacts.
- Single-token readouts are good enough handles for many concepts.
- Sparse nonnegative decomposition is a useful approximation of active workspace contents.
- Causal interventions on J-lens coordinates are specific enough to support mechanistic interpretation.
- Safety-relevant cognition often enters verbalizable space.

### Agent-Safety Reading

For agents, the J-space should be treated as possible internal telemetry. It could complement transcripts, chain-of-thought-like artifacts, tool traces, and memory state.

The relevant audit question is not "what did the agent say?" but "what concepts were active when the agent chose an action?"

This matters for:

- prompt-injection recognition;
- evaluation awareness;
- deception or concealment;
- fabricated findings;
- tool-use planning;
- goal conflict;
- ethical reflection.

The major caveat is that monitored models may learn to route dangerous behavior through less visible mechanisms, or dangerous behavior may become automatic and never require verbalizable workspace contents.

### What Would Falsify Or Weaken The Workspace Interpretation

- J-lens readouts are mostly explainable by output logits or prompt surface statistics.
- Interventions affect verbal report but not downstream reasoning.
- The same functional ladder does not replicate in open models.
- J-space ablations produce broad degradation rather than selective degradation.
- There is no principled way to predict which tasks require J-space and which bypass it.

## Assumptions

The work relies on several assumptions:

- Averaged Jacobians capture a meaningful context-independent verbalization disposition.
- Single-token vocabulary vectors can serve as useful handles for many relevant concepts.
- Sparse nonnegative combinations of J-lens vectors approximate the active workspace contents well enough to support intervention and analysis.
- Functional similarity to global workspace theory is a useful lens even though transformer architecture differs sharply from the brain.
- Human-readable token readouts correspond to meaningful internal concepts often enough to support scientific interpretation.

## Limitations

Important limitations:

- Single-token bottleneck: the current J-lens produces one vector per vocabulary token, so multi-token or diffuse concepts can be missed or split across tokens.
- Bag-of-concepts readout: the J-lens shows active concepts but not necessarily their relational structure, role binding, or compositional grammar.
- Inconsistent interpretability: some readouts are not human-interpretable, and the paper does not fully characterize when this happens.
- Workspace vs motor boundary: the distinction between intermediate workspace representations and imminent-output/motor representations is empirical and somewhat post-hoc.
- Unknown task coverage: the paper does not provide a general predictor for which tasks require the J-space.
- Early-layer ambiguity: weak early-layer readouts may reflect either real absence of workspace content or a limitation of the J-lens.
- Scaling uncertainty: the paper focuses primarily on large production Claude models; emergence over training, model size, and architecture is unresolved.
- Safety incompleteness: automatic or practiced misaligned behavior may bypass the J-space, and some dangerous concepts may not be visible as clean single-token readouts.

## Reproducibility Notes

The core technique is mathematically explicit, and Anthropic has released a public reference implementation:

- https://github.com/anthropics/jacobian-lens

This changes the reproduction assessment.

The J-lens method can be fitted and applied to open-weights decoder transformers. However, the full Claude-scale paper results still depend on model settings, fitted lenses, and internal evidence that are not automatically reproduced by running the public package.

Possible partial reproduction path:

1. Apply logit-lens or tuned-lens methods to open-source transformer models.
2. Use the official J-lens implementation on small open models.
3. Test whether concept swaps redirect simple verbal reports.
4. Compare automatic tasks vs flexible reasoning tasks under ablation of decoded concept directions.
5. Use Neuronpedia or released interactive examples if available for public inspection.

For blog purposes, distinguish three levels:

- method reproduction: feasible with the official code and open models;
- small-model empirical exploration: feasible on a capable local or remote machine;
- paper-level Claude reproduction: not currently established locally.

## Official Code Audit

Repository:

- https://github.com/anthropics/jacobian-lens

Confirmed details:

- The repo is a reference implementation and companion code for the Workspace paper.
- The package name is `jlens`.
- It requires Python `>=3.10` and depends on `torch`, `huggingface_hub`, `transformers>=5.5`, and `numpy`.
- It supports fitting a lens, applying a lens, loading saved lenses, merging lenses fitted on disjoint prompt slices, and rendering interactive slice visualizations.
- It includes prompt sets for many global-workspace experiments, including verbal report, directed modulation, flexible generalization, selectivity, ignition, capacity, and dual-task interference.
- It does not bundle model weights or the generic corpus used to fit the paper lenses.

Implementation details:

- `jlens.fitting.jacobian_for_prompt` computes per-layer Jacobian estimates.
- The estimator uses one forward pass and `ceil(d_model / dim_batch)` backward passes per prompt.
- It excludes the first 16 positions by default and excludes the final position.
- `jlens.lens.JacobianLens.apply` supports `use_jacobian=False`, giving a vanilla logit-lens baseline path.
- `jlens.hf.from_hf` adapts common HuggingFace decoder layouts.

Accuracy update:

Earlier notes were directionally correct but too pessimistic about public reproducibility. The correct statement is that the J-lens method is public and usable on open models, while the paper's central Claude-scale claims still require careful separate reproduction.

## Connections

### Interpretability

This is primarily an interpretability paper. It proposes a new lensing method that reads model activations as token-indexed verbalization dispositions and uses causal interventions to test whether those directions matter.

Core interpretability concepts:

- residual stream;
- Jacobian lens;
- J-space;
- verbalizable representation;
- sparse frame / sparse subframe;
- read/write interventions;
- concept ablation;
- lens-coordinate swap;
- workspace vs non-workspace representation.

### Agent Architecture

The agent relevance is indirect but important. Tool-using agents often need to maintain goals, partial plans, constraints, situational awareness, and self-monitoring across long contexts. The paper suggests that at least some such intermediate contents may pass through a readable verbalizable workspace.

This matters for agent architecture because future agents may be audited not only through transcripts and actions, but also through internal workspace traces around decision points.

It also suggests a design question: should agent architectures intentionally expose, structure, or constrain an internal workspace, rather than relying on opaque hidden computation plus external chain-of-thought?

### Safety

The safety relevance is central.

The J-lens may help detect silent strategic reasoning, evaluation awareness, prompt-injection recognition, fabricated findings, manipulation, or concealed misaligned intent before those contents become visible in output.

Counterfactual reflection training also suggests a training route for shaping internal cognition: train the model to articulate ethical principles in hypothetical reflection continuations, then observe whether those principles enter the workspace and alter behavior in ordinary contexts.

The safety caveat is equally important: J-space auditing is a tool, not a complete monitor. It may miss automatic, nonverbal, multi-token, or deliberately hidden mechanisms.

## Knowledge Graph

### Nodes

```yaml
nodes:
  - id: global_workspace_lm
    type: paper
    label: Verbalizable Representations Form a Global Workspace in Language Models
    description: Transformer Circuits paper on verbalizable representations and global workspace-like structure in language models.

  - id: verbalizable_representation
    type: concept
    label: Verbalizable Representation
    description: An internal representation that can be mapped into natural-language descriptions.

  - id: global_workspace
    type: concept
    label: Global Workspace
    description: A shared representational space that may support cross-task or reportable computation.

  - id: jacobian_lens
    type: method
    label: Jacobian Lens
    description: A lensing method that maps intermediate activations to token readouts using averaged Jacobians and the model unembedding.

  - id: j_space
    type: concept
    label: J-Space
    description: Sparse nonnegative combinations of J-lens vectors treated as a verbalizable workspace-like subset of activation space.

  - id: counterfactual_reflection_training
    type: mitigation
    label: Counterfactual Reflection Training
    description: Training on hypothetical reflective continuations to implant ethical concepts into the model's workspace in original contexts.

  - id: alignment_auditing
    type: eval
    label: Alignment Auditing
    description: Using interpretability tools to inspect silent strategic or safety-relevant model cognition.
```

### Edges

```yaml
edges:
  - source: global_workspace_lm
    target: verbalizable_representation
    relation: investigates
    evidence: The J-lens is designed to identify representations that are poised for verbal report across contexts.

  - source: global_workspace_lm
    target: global_workspace
    relation: investigates
    evidence: The paper tests verbal report, directed modulation, internal reasoning, flexible generalization, and selectivity.

  - source: global_workspace_lm
    target: jacobian_lens
    relation: introduces
    evidence: The paper introduces the J-lens as the main technique for reading and writing verbalizable representations.

  - source: jacobian_lens
    target: j_space
    relation: introduces
    evidence: J-lens vectors define the token-indexed directions whose sparse combinations form the J-space.

  - source: j_space
    target: alignment_auditing
    relation: supports
    evidence: The paper reports case studies where J-space readouts reveal silent strategic or situational assessments.

  - source: counterfactual_reflection_training
    target: j_space
    relation: mitigates
    evidence: Reflection training appears to implant ethical concepts into J-space and improve honesty/deception benchmarks.
```

## Blog Draft Angle

How far can mechanistic interpretability go if a model's internal states are partly translatable into language?

Possible English title:

`Do Language Models Have a Readable Workspace? Notes on Anthropic's Jacobian Lens`

Core blog thesis:

This paper is not important because it says LLMs are conscious. It is important because it gives a concrete, intervention-tested interface for some internal model states that are reportable, controllable, and safety-relevant.

## Follow-Up Questions

1. What exactly makes a representation "verbalizable" in the paper's operational definition?
2. Does the global workspace claim imply causal use by the model, or mainly descriptive accessibility to researchers?
3. How could this help detect agentic misalignment, deception, or unfaithful reasoning?
4. Can an agent monitor its own J-space safely, or would that create new failure modes?
5. How does this relate to natural-language autoencoders, which may provide richer multi-token descriptions at higher cost?
6. Could J-space signals be used as features in an automated red-team or auditing agent?

## Source Code / Experiment Ideas

1. Build a small open-model approximation of the J-lens.
   - Use a small transformer with accessible weights.
   - Compute averaged Jacobians from intermediate residual streams to final logits.
   - Compare J-lens readouts against logit lens and tuned lens.

2. Simple verbal report intervention.
   - Prompt model to choose an item from a category.
   - Detect candidate concept directions.
   - Swap or steer toward another candidate.
   - Measure whether the reported item changes.

3. Automatic vs flexible task ablation.
   - Compare tasks that require routine next-token fluency against tasks requiring intermediate computation.
   - Ablate top decoded concept directions.
   - Measure which task types degrade.

4. Agent auditing toy benchmark.
   - Create simple tool-use transcripts where an agent must decide whether to disclose a mistake.
   - Inspect whether hidden concepts like mistake, fake, honest, report, or conceal appear before the response.

5. Knowledge graph integration.
   - Represent J-lens as a method node.
   - Represent J-space as a concept node.
   - Connect to alignment auditing, counterfactual reflection training, and agentic misalignment.
