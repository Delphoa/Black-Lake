# Arxiv DEP Job Log: OViP Preference Learning

## Public-Safe Run Context

- `Deposit date`: 2026-07-14.
- `Selected paper`: arXiv:2505.15963v2, *OViP: Online Vision-Language Preference Learning for VLM Hallucination*.
- `Authors`: Shujun Liu, Siyuan Wang, Zejun Li, Jianxiang Wang, Cheng Zeng, and Zhongyu Wei.
- `Source platform`: arXiv preprint; v1 submitted 2025-05-21 and v2 revised 2025-09-28.
- `DOI`: https://doi.org/10.48550/arXiv.2505.15963.
- `Review scope`: Source-first multimodal-alignment review; no model, training job, benchmark, or generated-image pipeline was executed.

## Random Selection and Eligibility

- `Paper unit`: Each unique parent directory containing at least one PDF was treated as one candidate.
- `Enumeration`: `rg --files -g "*.pdf"` found 75,774 PDF-backed paper units and 75,774 candidate PDFs.
- `Selection method`: PowerShell `Get-Random` selected one uniform zero-based index from the complete sorted parent-directory list.
- `Selected index`: 50,425.
- `Candidate PDFs in selected unit`: 1.
- `Exclusions`: 0.
- `Reselections`: 0.
- `Identifier derivation`: The PDF filename and adjacent README yielded arXiv:2505.15963; the normalized title was verified against the canonical arXiv record.

## Local Source Integrity and Repair

- `Initial classification`: Partial. A full PDF and metadata README were present, but full-paper HTML was missing.
- `Repair action`: The bounded arXiv archive workflow preserved the existing PDF and fetched full-paper HTML, metadata HTML, and the TeX source archive. It also refreshed the local README, attribution record, machine-readable summary, and verification report.
- `PDF verification`: 1,648,427 bytes; `%PDF-` header present; trailing `%%EOF` marker present.
- `Full-paper HTML verification`: 293,109 bytes; 79,707 body characters; 132 headings; eight paper-structure terms; article/main/LaTeXML structure present.
- `Final classification`: Complete and verified. No partial files remained.
- `Source locality`: PDF, HTML, metadata HTML, TeX source, extracted text, and caches remained local. No source file was copied into this repository or sent to Slack.

## Dedup Validation

- The public dedup index contained 14 records and no matching arXiv ID, DOI, normalized title, or slug before this deposit.
- Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging` contained no matching Arxiv DEP artifact.
- Automation memory contained no matching paper marker.
- Relevant Black-Lake-Data repository searches contained no matching ID or normalized title marker.
- No same-paper marker appeared in active worktree Markdown or JSON records within the 24-hour exclusion window.
- `Result`: Eligible on the first draw.

## Extraction and Evidence Review

- `Initial cache`: Miss.
- `Refresh mode`: `missing-only`.
- `Extractor result`: `pypdf` extracted PDF text after `pdftotext` was unavailable; `html-regex` extracted HTML; `tarfile` extracted source text.
- `Cache result`: Cached. PDF text (74,898 bytes), HTML text (81,175 bytes), and source text (159,651 bytes) are present.
- `Paper evidence inspected`: Introduction, method, preference-pair construction, inverse negative-image synthesis, dual loss, evaluation design, main tables, ablations, training dynamics, efficiency, ethics, reproducibility, limitations, and appendices.
- `Public primary records inspected`: arXiv v2 metadata/full text, arXiv PDF/source locators, DOI/license record, and the official code repository.
- `Released artifacts`: The official repository exposes modified LLaMAFactory training code, evaluation code, a small data archive, dependency guidance, and model/dataset instructions. The repository and released artifacts were not executed.
- `Source files collected for deposition`: None; no `.source/` directory was created.

## Exactly Three Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - VALUE provides internal fusion, modality-balance, relation, and leakage probes that could test whether OViP improves grounded behavior rather than only benchmark outputs.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - VideoWeave connects diffusion-generated media with explicit consistency evidence, sharpening the need to validate OViP's synthesized hard negatives for semantic and visual fidelity.
3. `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` - BA-LoRA supplies a complementary behavior-preservation view of low-rank adaptation, directly overlapping OViP's LoRA-based effort to reduce failure while retaining general capability.

## Outputs

- `.logs/20260714-Arxiv-OViP-Preference-Learning-LOG.md`
- `.logs/20260714-Arxiv-OViP-Preference-Learning-PHASE-LOG.md`
- `.reports/BL-Arxiv-OViP-Preference-Learning-20260714/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/README.md`
- `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Submission

- `Repository result`: Direct push to the default branch succeeded.
- `Primary artifact commit`: https://github.com/Delphoa/Black-Lake/commit/601536e83c62347c47f33f93ce1882929672431e.
- `Slack notification`: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784009965170939.
- `Blockers`: None. Independent reproduction remains a validation shortfall, not a deposition blocker.

## Next-Review Questions

1. Do OViP's released scripts reproduce the one-epoch 7B results, including HRI 9.58 and General Accuracy Difference +0.88, under a pinned environment and unchanged evaluation inputs?
2. How often do diffusion-generated negative images faithfully isolate the sampled hallucination instead of introducing unrelated artifacts, stereotypes, or label leakage?
3. Does the reported benefit survive alternative multimodal judges, held-out model families, stronger calibration tests, and evaluation protocols whose reference ranges are fixed independently of OViP?

## Challenges

1. The archive unit required repair because a complete PDF was present without full-paper HTML; review correctly waited for a verified two-format source state.
2. HRI normalizes each benchmark against observed reference gains, including OViP two-epoch values in the main setting, so the aggregate is useful for within-paper comparison but not an independent universal scale.
3. The official repository improves inspectability but the seven-GPU training stack, external judge, diffusion service, datasets, and benchmark downloads were not executed or independently audited.
