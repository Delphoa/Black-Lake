# Arxiv DEP Job Log

## Selection

- Selected paper: Memory Shot for Long-Term Dialogue.
- arXiv: `2606.28338v1`.
- Authors: Chunyi Peng, Haidong Xin, Xuanshuo Sheng, Xin Dai, Zhenghao Liu, Shuo Wang, Yukun Yan, Zulong Chen, Yu Gu, and Ge Yu.
- Selection method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, sorted list, and uniform PowerShell `Get-Random` index selection.
- Candidate inventory: 75,960 PDFs collapsed to 75,957 parent-paper units.
- Draw: zero-based index 48,270; first draw accepted.
- Exclusions: duplicate/dedup exclusions 0; source-gate exclusions 0; reselections 0; same-paper recent-marker exclusions 0.
- Dedup markers checked: arXiv ID, arXiv DOI, normalized title, slug, repository artifact surfaces, automation memory, and relevant Black-Lake-Data search results. Metadata-only author-inventory rows were not treated as Arxiv DEP artifacts.

## Source Integrity

- Initial source state: partial; the valid PDF existed but full-paper HTML was missing.
- Repair: one bounded single-paper brokered archive repair obtained official full-paper HTML and refreshed the local README, provenance record, machine-readable summary, acquisition receipt, and verification report.
- Final verification: complete. The PDF was 2,801,199 bytes and passed the minimum size, `%PDF-` header, and trailing `%%EOF` checks. The full-paper HTML was 314,154 bytes with 71,442 body characters, document markers, 48 heading/section markers, and six paper-structure terms.
- Source package: unavailable; no TeX/source archive was collected.
- Source policy: PDF, full-paper HTML, metadata HTML, extracted text, cache, and integrity records remain local. No source files were uploaded, staged, committed, or attached.

## Outputs

- `.logs/20260805-Arxiv-MemShot-Dialogue-Memory-LOG.md`
- `.logs/20260805-Arxiv-MemShot-Dialogue-Memory-PHASE-LOG.md`
- `.reports/BL-Arxiv-MemShot-Dialogue-Memory-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-MemShot Dialogue Memory/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-MemShot Dialogue Memory/memshot_dialogue_memory_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Related DEP Entries

- `.lake-data/DEP-A/DEP-A-20260714-C-DIC Dialogue Memory/2606.12411-whitepaper-review.md` - revisable latent dialogue memory, retrieval-aware updates, and long-horizon evaluation.
- `.lake-data/DEP-A/DEP-A-20260714-MemRouter/2605.00356-whitepaper-review.md` - learned memory admission as a separate write policy from retrieval and answer generation.
- `.lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics/agent-memory-forensics-intake-review.md` - defensive memory provenance, trace evidence, and failure-localization boundaries.

## Next-Review Questions

1. Does the 70x construction-speed advantage persist after including image storage, visual retrieval indexing, GPU serving, and end-to-end latency under concurrent users?
2. How do MemShot's visual units behave under privacy-sensitive dialogue, edits/deletions, contradictory facts, multilingual text, accessibility constraints, and image-rendering failures?
3. Can matched-compute, multi-seed studies separate gains from layout structure, header metadata, chunk size, retriever quality, judge behavior, and the Qwen3-VL backbone?

## Challenges

1. The paper reports strong benchmark comparisons, but code, checkpoints, datasets, and environment details were not executed or independently reproduced in this run.
2. The visual-memory pipeline adds a representation and serving dependency: rendering, image storage, multimodal retrieval, OCR/vision reliability, and privacy controls all become operational concerns.
3. LLM-as-a-judge results and saliency/rubric analyses may be sensitive to judge prompts, model versions, and attribution definitions; raw predictions and uncertainty intervals were not available for recalculation.

## Attribution and Public-Safety Note

Public artifacts cite canonical arXiv, DOI, repository, and related-DEP URLs. The complete paper source files, extracted text, caches, and private verification records were withheld locally, and no public artifact discloses local paths, machine data, usernames, timezone labels, or exact local execution timestamps.
