# Arxiv DEP Log: Document Fraud LLM

## Public-Safe Run Summary

- Deposition date: 2026-07-15.
- Selected paper: *Can Multi-modal (reasoning) LLMs detect document manipulation?*
- Stable identifier: arXiv:2508.11021v1; DOI: 10.48550/arXiv.2508.11021.
- Selection method: `rg --files -g "*.pdf"` enumerated the archive; PDF parent directories were deduplicated into paper units; PowerShell `Get-Random` selected one zero-based index uniformly.
- Candidate units: 75,776.
- Selected zero-based index: 2,983.
- Duplicate exclusions: 0.
- Reselections: 0; the first draw was accepted after identifier, DOI, normalized-title, slug, related-repository, memory, and recent-marker checks.
- Source policy: all original paper documents, extracted text, caches, and repair records remain local. No source file was copied into the repository, staged, committed, attached, or sent to Slack.

## Deduplication and Eligibility

The acceptance scan covered `.logs`, `.reports`, `.lake-data`, `.staging`, the automation memory, and relevant `Delphoa-Labs/Black-Lake-Data` search results. Searches for `2508.11021`, `10.48550/arXiv.2508.11021`, the normalized title, and the `Document Fraud LLM` slug found no prior Arxiv DEP artifact and no same-paper marker in the preceding 24-hour window. The related arXiv record 2503.20084 was not treated as the same paper; it is separately identified by arXiv and appears here only because the selected record carries an arXiv administrator text-overlap note.

## Source-Integrity Gate

- Initial classification: `partial`. The archive unit contained a valid full PDF but lacked full-paper HTML and the required companion integrity records.
- Repair: preserved the existing PDF; collected official arXiv full-paper HTML, abstract/metadata HTML, and TeX/source package; refreshed the paper README, attribution record, machine-readable summary, and verification report.
- Final classification: `complete`.
- PDF validation: 428,818 bytes, `%PDF-` header present, trailing `%%EOF` present.
- Full-paper HTML validation: 105,063 bytes, 37,580 body characters after script/style/tag removal, 57 heading/section markers, seven paper-structure terms, and a recognized document marker.
- Partial state: zero remaining partial files.
- Extraction cache: PDF, HTML, and source-package extraction succeeded; `pypdf` was used because `pdftotext` was unavailable.
- Upload gate: source documents and extraction outputs were withheld locally. No public `.source/` directory was created.

## Research Outcome

The paper evaluates zero-shot multimodal language models, a linear SVM, and JPEG-forensic CNN baselines on receipt manipulation. GPT-O1 leads the reported model table at AUC 0.71, while most systems cluster close to random. Gemini-2.5 Flash rises from 0.55 to 0.59 AUC with thinking, and Gemini-2.5 Pro rises from 0.51 to 0.63. The GPT-O1 error analysis names 218 receipt images but reports 192 scored decisions, 161 correct predictions, two false positives, and 29 false negatives. Because unparseable, refused, or missing model responses were omitted, the reported denominators and calibration evidence do not support unattended fraud decisions.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` — supplies an architecture-aware probe methodology for testing whether multimodal representations encode alignment, modality preference, and relations rather than relying on aggregate task scores.
2. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` — supplies interval-valued confidence, support counts, distribution-envelope assumptions, and fail-closed decision gating for the selected paper's underconfident and selectively omitted predictions.
3. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` — distinguishes stated confidence, sampled-consistency proxies, factual correctness, and user-facing uncertainty, directly sharpening interpretation of GPT-O1's probability histogram.

## Output Paths

- `.logs/20260715-Arxiv-Document-Fraud-LLM-LOG.md`
- `.reports/BL-Arxiv-Document-Fraud-LLM-20260715/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/README.md`
- `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. How do AUC, calibration error, abstention coverage, and failure rate change when every model response—including refusals and parse failures—is retained in a fixed evaluation denominator?
2. Does the reported reasoning uplift persist across repeated seeds, locked prompts, independent judges, and additional document-forgery datasets with source- and manipulation-held-out splits?
3. Can a hybrid detector combine forensic image features with multimodal semantic checks while preserving calibrated human-review thresholds under distribution shift?

## Challenges

1. The paper uses the names “FindIt Again,” “find-it-2,” and RDDFD around the benchmark, while the reference identifies *Receipt dataset for document forgery detection*; a replication needs a pinned data manifest.
2. The evaluation omits unparseable or missing model outputs and does not report per-model retained counts, which can bias comparisons and conceal operational failure.
3. The selected arXiv record has an administrator note for text overlap with arXiv:2503.20084, so novelty and version lineage require explicit author clarification rather than inference.

## Validation Notes

The manuscript title contract, required headings, evidence ledger, exact three exercise paths, MVP fields, Report-Mark synthesis counts, DEP README inventory, public-safe scans, source-withholding statement, and staged-file allowlist are validated before submission. The final commit is limited to generated Markdown under `.logs`, `.reports`, and `.lake-data`.
