export type Experiment = {
  id: string;
  title: string;
  status: "planned" | "code audit" | "local toy" | "remote candidate";
  target: string;
  compute: string;
  goal: string;
  nextStep: string;
};

export const experiments: Experiment[] = [
  {
    id: "001-nla-code-audit",
    title: "NLA Code Audit",
    status: "code audit",
    target: "Natural Language Autoencoders",
    compute: "Current macOS laptop; no GPU required",
    goal: "Understand the AV/AR interface, parquet activation schema, checkpoint metadata, and inference path before attempting GPU execution.",
    nextStep: "Inspect nla_inference.py, docs/inference.md, released checkpoint metadata, and write a feasibility report.",
  },
  {
    id: "002-logit-lens-toy",
    title: "Logit-Lens Toy Baseline",
    status: "local toy",
    target: "J-lens / workspace-style interpretability",
    compute: "Current macOS laptop; tiny open model or synthetic transformer",
    goal: "Build a small local lensing experiment that reads intermediate activations without needing Claude internals.",
    nextStep: "Start with a tiny model, extract hidden states, apply unembedding readouts, and compare layers on controlled prompts.",
  },
  {
    id: "003-remote-mac-model-endpoint",
    title: "48GB Mac Remote Model Endpoint",
    status: "remote candidate",
    target: "Lightweight open-model inference",
    compute: "Separate 48GB macOS machine",
    goal: "Optionally expose a local-network inference endpoint for small open models so experiments can request completions or activations remotely.",
    nextStep: "Decide later whether to use Ollama, llama.cpp server, MLX, or a small custom HTTP service.",
  },
];
