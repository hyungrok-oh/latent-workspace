export type GraphNode = {
  id: string;
  type: "paper" | "concept" | "method" | "risk" | "eval" | "mitigation";
  label: string;
  description: string;
};

export type GraphEdge = {
  source: string;
  target: string;
  relation: string;
  evidence: string;
};

export const nodes: GraphNode[] = [
  {
    id: "global_workspace_lm",
    type: "paper",
    label: "Global Workspace in Language Models",
    description:
      "Transformer Circuits paper on verbalizable representations and global workspace-like structure in language models.",
  },
  {
    id: "jacobian_lens",
    type: "method",
    label: "Jacobian Lens",
    description:
      "A lensing method that maps intermediate activations to token readouts using averaged Jacobians and the model unembedding.",
  },
  {
    id: "j_space",
    type: "concept",
    label: "J-Space",
    description:
      "Sparse nonnegative combinations of J-lens vectors treated as a verbalizable workspace-like subset of activation space.",
  },
  {
    id: "verbalizable_representation",
    type: "concept",
    label: "Verbalizable Representation",
    description:
      "An internal representation that can be mapped into natural-language descriptions or verbal reports.",
  },
  {
    id: "global_workspace",
    type: "concept",
    label: "Global Workspace",
    description:
      "A limited representational medium that supports report, control, flexible reasoning, and selective access.",
  },
  {
    id: "directed_modulation",
    type: "concept",
    label: "Directed Modulation",
    description:
      "The ability to summon, hold, suppress, or compute with an internal concept when a task requires it.",
  },
  {
    id: "flexible_generalization",
    type: "concept",
    label: "Flexible Generalization",
    description:
      "A representation can be moved across contexts and still be used by different downstream computations.",
  },
  {
    id: "selectivity",
    type: "concept",
    label: "Selectivity",
    description:
      "Workspace-like representations are a limited subset of model computation rather than the whole activation space.",
  },
  {
    id: "internal_telemetry",
    type: "eval",
    label: "Internal Telemetry",
    description:
      "Using internal readouts as partial evidence alongside transcripts, tool traces, memory, and visible plans.",
  },
  {
    id: "counterfactual_reflection_training",
    type: "mitigation",
    label: "Counterfactual Reflection Training",
    description:
      "Training on hypothetical reflection continuations to shape internal workspace concepts in original contexts.",
  },
  {
    id: "natural_language_autoencoders",
    type: "paper",
    label: "Natural Language Autoencoders",
    description:
      "Transformer Circuits paper on using a natural-language bottleneck to explain LLM activations.",
  },
  {
    id: "natural_language_autoencoder",
    type: "method",
    label: "Natural Language Autoencoder",
    description:
      "A pair of models that maps activation vectors to text explanations and reconstructs activation vectors from those explanations.",
  },
  {
    id: "activation_verbalizer",
    type: "method",
    label: "Activation Verbalizer",
    description: "The NLA component that maps an activation vector to a natural-language explanation.",
  },
  {
    id: "activation_reconstructor",
    type: "method",
    label: "Activation Reconstructor",
    description: "The NLA component that maps a text explanation back to an activation vector.",
  },
  {
    id: "evaluation_awareness",
    type: "risk",
    label: "Evaluation Awareness",
    description: "A model's internal recognition or suspicion that it is being evaluated or tested.",
  },
  {
    id: "alignment_auditing",
    type: "eval",
    label: "Alignment Auditing",
    description:
      "Inspecting model behavior and internals for safety-relevant cognition such as deception, evaluation awareness, or goal conflict.",
  },
];

export const edges: GraphEdge[] = [
  {
    source: "global_workspace_lm",
    target: "jacobian_lens",
    relation: "introduces",
    evidence: "The paper introduces the J-lens as its main read/write interpretability technique.",
  },
  {
    source: "jacobian_lens",
    target: "j_space",
    relation: "introduces",
    evidence: "J-lens vectors define token-indexed directions whose sparse combinations form the J-space.",
  },
  {
    source: "global_workspace_lm",
    target: "verbalizable_representation",
    relation: "investigates",
    evidence: "The paper studies representations that are available for verbal report and intervention.",
  },
  {
    source: "j_space",
    target: "global_workspace",
    relation: "approximates",
    evidence:
      "The J-space satisfies several functional properties associated with a global workspace without reproducing the full brain architecture.",
  },
  {
    source: "j_space",
    target: "directed_modulation",
    relation: "supports",
    evidence:
      "The paper reports that concepts can be held, summoned, or used internally when the task demands it.",
  },
  {
    source: "j_space",
    target: "flexible_generalization",
    relation: "supports",
    evidence:
      "Workspace vectors moved from one context can be operated on by downstream computations in another context.",
  },
  {
    source: "j_space",
    target: "selectivity",
    relation: "exhibits",
    evidence:
      "Ablating J-space affects some flexible reasoning tasks while leaving much routine processing relatively intact.",
  },
  {
    source: "natural_language_autoencoders",
    target: "natural_language_autoencoder",
    relation: "introduces",
    evidence: "The paper introduces NLAs as a text-bottleneck autoencoding method for explaining activations.",
  },
  {
    source: "natural_language_autoencoder",
    target: "activation_verbalizer",
    relation: "contains",
    evidence: "The AV maps activation vectors to natural-language explanations.",
  },
  {
    source: "natural_language_autoencoder",
    target: "activation_reconstructor",
    relation: "contains",
    evidence: "The AR reconstructs activation vectors from text explanations.",
  },
  {
    source: "natural_language_autoencoder",
    target: "j_space",
    relation: "complements",
    evidence:
      "NLAs provide richer text explanations while J-space/J-lens provides cheaper token-level readouts.",
  },
  {
    source: "natural_language_autoencoder",
    target: "evaluation_awareness",
    relation: "measures",
    evidence: "Anthropic reports NLA explanations indicating evaluation awareness in evaluation settings.",
  },
  {
    source: "j_space",
    target: "alignment_auditing",
    relation: "supports",
    evidence: "J-space readouts can reveal silent strategic or situational assessments.",
  },
  {
    source: "j_space",
    target: "internal_telemetry",
    relation: "enables",
    evidence:
      "For agents, J-space readouts can complement transcripts, tool calls, memory state, and visible plans around decision points.",
  },
  {
    source: "counterfactual_reflection_training",
    target: "j_space",
    relation: "shapes",
    evidence:
      "The paper reports that reflection training implants ethics-related concepts into J-space and changes behavior.",
  },
];
