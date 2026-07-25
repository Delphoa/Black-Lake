# DEP-E-20260725-DASD Reasoning

#research #arxiv #llm #reasoning #distillation #evaluation

Public-safe context: this DEP-E reviews arXiv:2601.09088 after a verified local PDF-plus-full-paper-HTML gate. The initially partial source bundle was repaired locally before review. Local paths, exact execution timestamps, source documents, source archives, caches, extracted text, and review renders are withheld.

## Contents

- `README.md` - public-safe inventory, source boundary, synthesis, and attribution.
- `dasd_reasoning_manuscript.md` - schema-complete research manuscript with evidence ledger, limits, implementation paths, and related DEP synthesis.

No `.source/` directory exists. No PDF, HTML, TeX archive, cache, extracted source text, review render, credential, dataset, model checkpoint, or executable artifact is deposited.

## Summary of Items

The manuscript reviews Distribution-Aligned Sequence Distillation for a 4B long-reasoning model. It preserves the author-reported temperature-scheduled, divergence-aware, and mixed-policy stages; the reported five-benchmark result table; release context; limitations; and a bounded implementation translation. Results are not represented as independently reproduced.

## Insights and Relevance

This deposit connects DASD's training-time distribution and rollout controls to three existing research records. WorkflowLLM supplies an orchestration context, MOSS supplies a context-managed agent setting, and Shuffled Autoregression supplies a cross-domain account of generation-order error control. The combined lesson is to record stage provenance, make train/inference mismatch measurable, and require a bounded validation gate before turning improved reasoning into autonomous action.

## Attribution Block

- Source URL: https://arxiv.org/abs/2601.09088
  - Applies to: `dasd_reasoning_manuscript.md`.
  - Notes: canonical identity, author attribution, abstract, and public locators.
- Source URL: https://arxiv.org/pdf/2601.09088
  - Applies to: `dasd_reasoning_manuscript.md`.
  - Notes: complete paper was inspected from a verified private copy; source file withheld.
- Source URL: https://arxiv.org/html/2601.09088
  - Applies to: `dasd_reasoning_manuscript.md`.
  - Notes: verified full-paper HTML was inspected; source file withheld.
- Source URL: https://github.com/D2I-ai/dasd-thinking
  - Applies to: `dasd_reasoning_manuscript.md`.
  - Notes: official code/release context inspected statically; code not executed.
- Source URL: https://huggingface.co/collections/Alibaba-Apsara/dasd-thinking
  - Applies to: `dasd_reasoning_manuscript.md`.
  - Notes: official model/data collection inspected; no model or dataset file downloaded.
- Source files: PDF, full-paper HTML, metadata HTML, TeX archive, cache, extracted text, repair records, and rendered pages.
  - Applies to: every item in this DEP.
  - Notes: withheld locally; no source files were uploaded.
