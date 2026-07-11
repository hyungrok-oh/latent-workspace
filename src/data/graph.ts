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
];
