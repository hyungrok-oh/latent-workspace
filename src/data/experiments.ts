export type Experiment = {
  id: string;
  title: string;
  status: "planned" | "code audit" | "local toy" | "activation scaffold" | "remote candidate";
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
    compute: "Current macOS laptop; dependency-free Python toy",
    goal: "Run a small synthetic residual-stream experiment that reads intermediate states through an output vocabulary.",
    nextStep: "Replace synthetic states with hidden states from a tiny open model when local model dependencies are available.",
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
  {
    id: "004-tiny-model-logit-lens",
    title: "Tiny-Model Logit Lens",
    status: "activation scaffold",
    target: "Open-model hidden-state readouts",
    compute: "Current macOS laptop for env check; 48GB Mac recommended for real runs",
    goal: "Extract hidden states from a small causal language model and read each layer through the model vocabulary.",
    nextStep: "Install optional torch/transformers dependencies on a model-capable Mac and run the default tiny GPT-2 pipeline.",
  },
  {
    id: "005-official-jacobian-lens-code-audit",
    title: "Official Jacobian Lens Code Audit",
    status: "code audit",
    target: "Anthropic jacobian-lens reference implementation",
    compute: "Current macOS laptop for audit; 48GB Mac recommended for fitting",
    goal: "Audit the official implementation and update the reproduction plan from approximation to public-code execution.",
    nextStep: "Decide whether the 48GB Mac should load a pre-fitted Qwen lens or fit a small lens from around 100 prompts.",
  },
];
