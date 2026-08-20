# DEP-E-20260803-QFT Tuning

#llm-finetuning #quantization #training-memory #optimizer #low-precision #model-compression #resource-aware-training #arxiv

Public-safe DEP-E research deposit for the 2026-08-03 Black Lake Arxiv DEP review of *QFT: Quantized Full-parameter Tuning of LLMs with Affordable Resources* (arXiv:2310.07147v3). The paper was selected from the local archive by a uniform random draw, passed a complete-source integrity gate after one bounded repair, and was reviewed from the full paper. Source files remain private and were not uploaded.

## Contents

- `README.md` - public-safe DEP manifest, classification, item inventory, synthesis context, and attribution.
- `qft_tuning_manuscript.md` - schema-complete manuscript reviewing QFT's quantized training-state design, reported evidence, limitations, implementation implications, and exactly three related DEP bridges.

## Summary of Items

- `README.md` makes the deposit auditable without exposing private archive paths or source files. It records the public paper identifiers, source-withheld boundary, and the relationship to the operational log and detailed Report-Mark.
- `qft_tuning_manuscript.md` preserves source-grounded notes on QFT's quantized Lion states, hybrid dense/sparse weight quantization, stack-based gradient flow, memory/performance results, evidence limits, and safe MVP directions.

## Insights and Relevance

QFT is relevant to Black Lake because it treats fine-tuning memory as a representation and systems problem: persistent state, sparse exceptions, update direction, and gradient movement are co-designed. The manuscript bridges that design with the llama.cpp Runtime DEP's quantization compatibility evidence, the KDFlow LLM Distill DEP's workload-aware transfer and training evidence, and the RandLoRA Full-rank DEP's parameter-efficiency/full-rank tradeoff. The `.logs` note records selection, eligibility, source integrity, and validation; the `.reports` Report-Mark provides the detailed synthesis and exact-count implementation challenges. Together they support future experiments that compare memory, bandwidth, compute, quality, and reproducibility under one evidence ledger.

## Attribution Block

- Source URL: https://arxiv.org/abs/2310.07147
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Canonical metadata, authors, version history, abstract, and DOI locator.
- Source URL: https://arxiv.org/html/2310.07147
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Full-paper method, tables, appendices, and conclusion.
- Source URL: https://arxiv.org/pdf/2310.07147
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Canonical PDF reference; private source copy was withheld.
- Source URL: https://doi.org/10.48550/arXiv.2310.07147
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Persistent identifier.
- Source URL: https://openreview.net/forum?id=PcKjjZOnfc
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: SPOT/ICLR 2026 workshop and publication context.
- Source URL: https://github.com/ggml-org/llama.cpp/releases/tag/b9789
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related runtime quantization evidence.
- Source URL: https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related compatibility correction evidence.
- Source URL: https://arxiv.org/abs/2603.01875
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related KDFlow paper basis.
- Source URL: https://github.com/songmzhang/KDFlow
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related KDFlow implementation context.
- Source URL: https://arxiv.org/abs/2502.00987
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related RandLoRA paper basis.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md`
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related processed DEP on quantization runtime and compatibility evidence.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related processed DEP on workload-aware distillation and memory/throughput tradeoffs.
- Repository path: `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md`
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Related processed DEP on full-rank parameter-efficient tuning.
- Source file: private verified arXiv source bundle, withheld locally.
  - Applies to: `qft_tuning_manuscript.md`
  - Notes: Source files were used for review but were not deposited or uploaded.
