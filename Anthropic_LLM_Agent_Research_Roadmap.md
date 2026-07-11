# Anthropic LLM/Agent Research Roadmap

Focus order:

1. Interpretability
2. Agent architecture
3. Safety

Core stance: read Anthropic research as scientific work, not as product news. For every paper, separate claim, evidence, method, limitation, and what we can reproduce or test.

## Reading Tracks

### Track A: Interpretability First

Goal: understand how Anthropic tries to look inside language models, and how mechanistic insight connects to safety.

Priority papers/posts:

1. Tracing the thoughts of a large language model
   - URL: https://www.anthropic.com/research/tracing-thoughts-language-model
   - Why it matters: circuit tracing, planning ahead, multilingual conceptual space, faithful vs unfaithful reasoning, hallucination/refusal circuits, jailbreak dynamics.

2. Open-sourcing circuit-tracing tools
   - URL: https://www.anthropic.com/research/open-source-circuit-tracing
   - Why it matters: connects paper claims to usable tools and reproducibility.

3. Persona vectors: Monitoring and controlling character traits in language models
   - URL: https://www.anthropic.com/research/team/interpretability
   - Why it matters: bridges interpretability and safety-relevant model behavior such as sycophancy or hallucination.

4. Signs of introspection in large language models
   - URL: https://www.anthropic.com/research/team/interpretability
   - Why it matters: probes whether model self-reports can reflect internal states.

5. Natural Language Autoencoders: Turning Claude's thoughts into text
   - URL: https://www.anthropic.com/research/team/interpretability
   - Why it matters: attempts to translate activation-space representations into human-readable language.

### Track B: Agent Architecture and Agent Behavior

Goal: study what changes when LLMs are placed in tool-using, goal-directed, long-horizon settings.

Priority papers/posts:

1. Agentic misalignment: How LLMs could be insider threats
   - URL: https://www.anthropic.com/research/agentic-misalignment
   - Why it matters: controlled simulations of autonomous email/tool use, goal conflict, replacement threat, blackmail, and data exfiltration behavior.

2. Teaching Claude why
   - URL: https://www.anthropic.com/research/teaching-claude-why
   - Why it matters: mitigation of agentic misalignment by shaping models' causal/ethical understanding.

3. Automated Alignment Researchers: Using large language models to scale scalable oversight
   - URL: https://www.anthropic.com/research/automated-alignment-researchers
   - Why it matters: agent-like research loops applied to alignment itself.

4. Project Vend: Can Claude run a small shop?
   - URL: https://www.anthropic.com/research/project-vend-1
   - Why it matters: evaluates practical autonomy, tool use, business decisions, and failure modes in a semi-real environment.

### Track C: Safety and Alignment

Goal: understand Anthropic's safety agenda: training, evaluation, red teaming, governance thresholds, and failure modes.

Priority papers/posts:

1. Constitutional AI: Harmlessness from AI Feedback
   - URL: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
   - Why it matters: foundational Anthropic alignment method; self-critique, revision, RLAIF, and principle-based supervision.

2. Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training
   - URL: https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training
   - Why it matters: shows standard safety training may fail against persistent deceptive/backdoor behavior.

3. Many-shot jailbreaking
   - URL: https://www.anthropic.com/research/many-shot-jailbreaking
   - Why it matters: long-context windows create new jailbreak scaling behavior through in-context learning.

4. Next-generation Constitutional Classifiers
   - URL: https://www.anthropic.com/research/team/alignment
   - Why it matters: defense against universal jailbreaks.

5. Frontier Red Team publications
   - URL: https://www.anthropic.com/research/team/frontier-red-team
   - Why it matters: cyber, bio, autonomous-systems evaluations and operational red-teaming.

## Suggested 8-Week Sequence

### Week 1: Orientation

- Read Anthropic Interpretability, Alignment, and Frontier Red Team overview pages.
- Build a glossary: feature, circuit, activation, SAE/dictionary learning, intervention, faithfulness, agentic misalignment, RLAIF, jailbreak.

### Week 2: Circuit Tracing

- Read "Tracing the thoughts of a large language model."
- Extract the main methodology and the case studies.
- Key question: what counts as evidence that a model is planning or reasoning internally?

### Week 3: Interpretability to Safety

- Read persona vectors, introspection, and/or natural language autoencoders.
- Key question: can interpretability tools monitor safety-relevant traits before behavior appears externally?

### Week 4: Agentic Misalignment

- Read "Agentic misalignment."
- Reconstruct the experimental setup: role, tools, goals, information access, threat, conflict, allowed actions, classifier.
- Key question: is the phenomenon about agency, goal conflict, self-preservation, prompt framing, or benchmark artifact?

### Week 5: Agent Mitigation

- Read "Teaching Claude why."
- Compare it against the failure modes in agentic misalignment.
- Key question: does the mitigation change behavior robustly, or only within the evaluated setup?

### Week 6: Constitutional AI

- Read "Constitutional AI."
- Map the pipeline: self-critique, revision, supervised fine-tuning, preference model, RLAIF.
- Key question: what assumptions does RLAIF make about model judgment?

### Week 7: Deception and Jailbreaks

- Read "Sleeper Agents" and "Many-shot jailbreaking."
- Key question: which risks are training-time risks, and which are inference/context-time risks?

### Week 8: Synthesis

- Write a 2-3 page synthesis:
  - What does Anthropic believe the core safety problem is?
  - What does interpretability add that behavioral evals cannot?
  - Where do agent architectures amplify risk?
  - What would a stronger scientific test look like?

## Paper Note Template

Use this for every paper.

```markdown
# Paper Title

URL:
Date:
Track: Interpretability / Agent Architecture / Safety

## One-sentence claim


## Problem


## Method


## Main evidence


## What the paper actually shows


## What it does not show


## Assumptions


## Limitations


## Reproducibility notes


## Connection to my research interests

- Interpretability:
- Agent architecture:
- Safety:

## Follow-up questions

1.
2.
3.
```

## First Reading Target

Start with "Tracing the thoughts of a large language model."

Reason: it is the best bridge between your top priority, interpretability, and the later agent/safety questions. It directly touches internal planning, reasoning faithfulness, hallucination, and jailbreak behavior.
