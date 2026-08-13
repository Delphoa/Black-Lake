# Black Lake Arxiv DEP Log: QFT Tuning

- Run date: 2026-08-03
- Automation: `Black Lake Arxiv DEP` selected and reviewed one arXiv archive paper.
- Selected paper: *QFT: Quantized Full-parameter Tuning of LLMs with Affordable Resources* (arXiv:2310.07147, v3).
- Source provenance: verified private source unit with PDF, full-paper HTML, metadata HTML, and integrity companions; source files were withheld locally and not uploaded.
- Random selection: `rg --files -g "*.pdf"`; 75,960 PDF candidates collapsed to 75,957 unique parent-directory paper units; uniform zero-based `Get-Random` index 11,795.
- Eligibility: scanned Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and related Black-Lake-Data search context for arXiv ID, DOI, normalized title, slug, and recent markers. Duplicate exclusions: 0. Reselections: 0. Public 24-hour cutoff: 2026-08-02.
- Source gate: the first unit was partial because full-paper HTML was absent. One bounded brokered repair completed the unit; PDF and full-paper HTML integrity checks passed. Source package was unavailable. No source files were staged or uploaded.
- Related DEP entries: `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md`; `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md`.
- Outputs: `.reports/BL-Arxiv-QFT-Tuning-20260803/Report-Mark.md`; `.lake-data/DEP-E/DEP-E-20260803-QFT Tuning/README.md`; `.lake-data/DEP-E/DEP-E-20260803-QFT Tuning/qft_tuning_manuscript.md`; `.lake-data/DEP-E/.index/pubs-index.md`.
- Validation: manuscript schema/title checks, exact-three Report-Mark sections, three code-mock-up parses, DEP inventory, public-output sanitization, staged allowlist, and no-source-upload checks passed before submission.

## Questions for Next Reviewer

1. Can QFT's reported memory savings be reproduced on a small public model with version-pinned kernels and exact quantizer settings?
2. Which layers and task families are most sensitive to the one-percent sparse outlier policy during longer or shifted fine-tuning runs?
3. Can a unified evaluation ledger compare QFT, KDFlow, RandLoRA, and runtime quantization under matched quality, memory, throughput, and energy budgets?

## Challenges for Next Review Pass

1. Reconcile the paper's memory table with measured allocator peaks and quantization metadata on an authorized small-model test.
2. Separate the contribution of Lion, sparse outlier preservation, and stack-based gradient flow with controlled ablations.
3. Establish whether the reported benchmark parity survives repeated seeds, newer model families, and independent evaluators.
