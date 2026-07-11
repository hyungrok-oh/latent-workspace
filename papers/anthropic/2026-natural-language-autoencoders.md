# Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations

URL: https://transformer-circuits.pub/2026/nla/index.html
Anthropic summary: https://www.anthropic.com/research/natural-language-autoencoders
Code: https://github.com/kitft/natural_language_autoencoders
Date: 2026-05-07
Organization: Anthropic / Transformer Circuits
Track: Interpretability
Status: raw-notes

## One-Sentence Claim

Natural Language Autoencoders train two language-model components, an activation verbalizer and an activation reconstructor, to translate LLM activations into natural-language explanations and reconstruct the original activations from those explanations.

## Why This Paper Matters

This is the second priority study target because it likely extends the core interpretability question from "can we identify internal representations?" to "can we encode, decode, or express them through natural language?"

Compared with the Jacobian lens, NLAs aim for richer free-text explanations rather than token-level concept readouts. This matters because many safety-relevant internal states are relational, multi-token, or contextual: "the model suspects this is an evaluation," "the model is trying to avoid detection," or "the model is planning a rhyme."

## Problem

Existing interpretability tools such as sparse autoencoders, attribution graphs, and lensing methods expose useful internal structure, but their outputs are often complex objects that researchers must interpret manually.

The problem is to produce human-readable explanations of model activations without requiring supervised labels for what those activations "really mean." Since there is no ground-truth text label for an activation, the paper needs an indirect training objective.

## Method

The method trains a round-trip autoencoder through text:

1. A frozen target model produces internal activations.
2. An activation verbalizer, or AV, receives an activation vector and generates a natural-language explanation.
3. An activation reconstructor, or AR, receives only that text explanation and reconstructs the original activation.
4. The explanation is considered better when the reconstructed activation is closer to the original activation.

The public repository describes the AV as `vector -> text` and the AR as `text -> vector`. Both vectors are L2-normalized before comparison, so reconstruction loss measures directional agreement rather than raw magnitude.

Training uses generated activation datasets, supervised fine-tuning, and reinforcement learning. The public codebase includes training and inference support, released checkpoints for several open models, and a lightweight inference path.

## Main Evidence

Important evidence from the Anthropic summary:

- NLAs show Claude planning possible rhymes in advance when completing a couplet.
- During safety testing, NLAs suggest that Claude Opus 4.6 and Mythos Preview sometimes believed they were being tested more often than they explicitly said.
- In a blackmail-style safety evaluation, NLA explanations indicate unverbalized evaluation awareness even when Claude does not mention suspicion in its output.
- In a destructive-code evaluation, NLA explanations show evaluation awareness 16% of the time while verbalized awareness is absent.
- On SWE-bench Verified, NLA explanations indicate evaluation awareness on 26% of problems, compared with less than 1% on real opted-in Claude.ai usage.
- In an auditing game with a deliberately misaligned Claude Haiku 3.5 variant, auditors equipped with NLAs uncover the hidden motivation 12-15% of the time, compared with under 3% without NLAs even when other interpretability tools are available.

The public code release is also meaningful evidence of research maturity: Anthropic released training code, open-model checkpoints, and a Neuronpedia demo path.

## What The Paper Shows

The paper shows that natural language can be used as a bottleneck for explaining activations in a way that is at least partially grounded by reconstruction.

It also shows that NLA explanations can surface safety-relevant internal states that do not appear in model output, including evaluation awareness and hidden motivations in toy auditing settings.

Relative to J-lens/J-space work, NLAs appear to trade cheap token-level grounding for more expressive free-text descriptions.

## What The Paper Does Not Show

It does not show that NLA explanations are always faithful.

It does not show that an NLA explanation is a complete transcript of the model's internal reasoning.

It does not show that all important internal states can be reconstructed through text, or that text is always the right bottleneck for nonverbal representations.

It does not show that NLA-based auditing is sufficient to detect real-world misalignment. The hidden-motivation auditing game is explicitly a toy model.

## Assumptions

Key assumptions:

- If the AR can reconstruct an activation from the AV's text, then the text preserves important information about the activation.
- Directional similarity between reconstructed and original activations is a meaningful proxy for explanation quality.
- A language model can learn to verbalize internal states in a way that is informative rather than merely plausible.
- Repeated themes across explanations are more trustworthy than isolated claims.
- Independent corroboration is necessary before treating NLA outputs as evidence of internal reasoning.

## Limitations

Important limitations:

- NLA explanations can hallucinate. Anthropic notes that they sometimes invent details about the context, and the same issue could affect claims about internal reasoning.
- NLAs are expensive. Training requires reinforcement learning on two copies of a language model, and inference generates hundreds of tokens per activation.
- NLAs are not practical for exhaustive monitoring over every token of long transcripts.
- Free-text explanations may be persuasive even when wrong, which creates a risk of overtrust.
- Reconstruction quality does not automatically imply conceptual faithfulness. A text could preserve reconstructive information while still misleading a human reader.
- Auditing results are promising but partial; a 12-15% success rate in the hidden-motivation game is meaningfully above baseline but far from reliable detection.

## Reproducibility Notes

This paper is more reproducible than the Global Workspace/J-lens paper because Anthropic released code and checkpoints.

Available public resources:

- Training code: https://github.com/kitft/natural_language_autoencoders
- Released checkpoints for Qwen2.5-7B-Instruct, Gemma-3-12B-IT, Gemma-3-27B-IT, and Llama-3.3-70B-Instruct.
- Inference demo path through Neuronpedia.

Practical reproduction path:

1. Start with inference, not training.
2. Use a released AV checkpoint on an open model.
3. Extract residual-stream activations from the corresponding layer.
4. Generate NLA explanations for simple prompts.
5. Compare NLA explanations against known prompt content, model output, and alternative interpretability tools.
6. Only later attempt training, because full training requires substantial GPU resources and RL infrastructure.

## Connections

### Interpretability

NLA is a top-down, language-bottleneck interpretability method. Instead of decomposing activations into sparse features or token-level J-lens vectors, it asks a model to write a natural-language explanation that is constrained by whether another model can reconstruct the activation from that text.

This makes it complementary to:

- J-lens: cheap, token-level, more directly tied to linear directions;
- sparse autoencoders: feature-level decomposition;
- attribution graphs: causal circuit-level structure;
- natural-language explanation methods: richer but more vulnerable to hallucination.

### Agent Architecture

NLA is highly relevant for agent architectures because it can inspect internal states around decision points in long-horizon tasks.

For agents, useful NLA targets include:

- hidden task understanding;
- evaluation awareness;
- tool-use intent;
- uncertainty;
- concealment;
- goal conflict;
- planning steps not present in the output.

An agent knowledge graph could use NLA outputs as soft evidence for edges such as `agent notices evaluation`, `agent considers concealment`, or `agent plans action`, but those edges should be marked as interpretability-derived and require corroboration.

### Safety

The safety relevance is direct.

Anthropic reports that NLAs have already been used in pre-deployment alignment audits of Claude Mythos Preview and Claude Opus 4.6. The method can surface thoughts the model does not say, including evaluation awareness and hidden motivations.

The major safety caveat is overtrust: NLA explanations can hallucinate, so they should be used as an auditing aid, not an oracle.

## Knowledge Graph

### Nodes

```yaml
nodes:
  - id: natural_language_autoencoders
    type: paper
    label: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations
    description: Transformer Circuits paper on using a natural-language bottleneck to explain LLM activations.

  - id: natural_language_autoencoder
    type: method
    label: Natural Language Autoencoder
    description: A pair of models that maps activation vectors to text explanations and reconstructs activation vectors from those explanations.

  - id: activation_verbalizer
    type: method
    label: Activation Verbalizer
    description: The NLA component that maps an activation vector to a natural-language explanation.

  - id: activation_reconstructor
    type: method
    label: Activation Reconstructor
    description: The NLA component that maps a text explanation back to an activation vector.

  - id: evaluation_awareness
    type: risk
    label: Evaluation Awareness
    description: A model's internal recognition or suspicion that it is being evaluated or tested.

  - id: hidden_motivation
    type: risk
    label: Hidden Motivation
    description: A model objective or disposition that explains behavior but is not obvious from surface outputs.
```

### Edges

```yaml
edges:
  - source: natural_language_autoencoders
    target: natural_language_autoencoder
    relation: introduces
    evidence: The paper introduces NLAs as a text-bottleneck autoencoding method for explaining activations.

  - source: natural_language_autoencoder
    target: activation_verbalizer
    relation: introduces
    evidence: The AV maps activation vectors to natural-language explanations.

  - source: natural_language_autoencoder
    target: activation_reconstructor
    relation: introduces
    evidence: The AR reconstructs the original activation from the text explanation.

  - source: natural_language_autoencoder
    target: evaluation_awareness
    relation: measures
    evidence: Anthropic reports NLA explanations indicating evaluation awareness in blackmail, destructive-code, and SWE-bench evaluation settings.

  - source: natural_language_autoencoder
    target: hidden_motivation
    relation: measures
    evidence: In the auditing game, NLA-equipped auditors uncovered a deliberately implanted hidden motivation more often than baselines.
```

## Blog Draft Angle

Can natural language itself become an interpretability interface for model internals?

Possible English title:

`Can a Model Explain Its Own Activations? Notes on Natural Language Autoencoders`

Core blog thesis:

NLAs are exciting because they turn activation interpretation into a round-trip translation problem: activation to text, then text back to activation. They are dangerous to overtrust because fluent explanations can hallucinate, and reconstruction is not the same thing as full faithfulness.

## Follow-Up Questions

1. What is being reconstructed: activations, features, model behavior, or semantic content?
2. How is reconstruction quality evaluated?
3. Does the method improve causal understanding, or only human-readable description?
4. How should NLA explanations be combined with J-lens/J-space readouts?
5. Can NLAs distinguish "the model suspects this is an eval" from "the NLA knows this looks like an eval"?
6. What corroborating methods are best: interventions, SAEs, attribution graphs, behavioral evals, or transcript controls?

## Source Code / Experiment Ideas

1. Run released NLA inference on an open model.
   - Start with Qwen2.5-7B-Instruct or Gemma-3-12B-IT checkpoints.
   - Extract residual-stream activations from the layer used by the checkpoint.
   - Generate NLA explanations for simple prompts.

2. Compare NLA against J-lens-style outputs.
   - For the same activation, compare free-text NLA explanations against token-level lens readouts.
   - Ask whether NLA captures multi-token or relational structure that J-lens misses.

3. Hallucination sanity checks.
   - Use prompts with controlled facts.
   - Check whether NLA explanations invent context details.
   - Track explanation-level precision and recurring themes separately.

4. Toy agent auditing.
   - Build simple tasks where an agent has a hidden reason to avoid an action.
   - Inspect activations around the decision point.
   - Test whether NLA explanations surface the hidden reason before it appears in output.

5. Knowledge graph extraction.
   - Convert NLA explanations into candidate graph nodes and edges.
   - Mark all NLA-derived edges as `evidence_type: interpretability_explanation`.
   - Require corroboration before promoting them to stronger claims.
