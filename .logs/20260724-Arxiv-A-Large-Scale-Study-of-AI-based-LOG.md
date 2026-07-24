# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260724-CF53BCCB`
- Deployment item ID: `BLAD-2200-20260724-CF53BCCB-P10`
- Public-safe date: 2026-07-24
- Paper: *A Large Scale Study of AI-based Binary Function Similarity Detection Techniques for Security Researchers and Practitioners*
- Identifier: `arXiv:2511.01180`; DOI: `10.48550/arXiv.2511.01180`
- URL: https://arxiv.org/abs/2511.01180

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 55,632 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `A-Large-Scale-Study-of-AI-based` slug; the 24-hour marker cutoff was 2026-07-23.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 822,379 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 262,298 bytes, 80,120 body characters, 60 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260724-Arxiv-A-Large-Scale-Study-of-AI-based-LOG.md`
- `.reports/BL-Arxiv-A-Large-Scale-Study-of-AI-based-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-A Large Scale Study of/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-A Large Scale Study of/a_large_scale_study_of_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-WorkflowLLM Enhancing/workflowllm_enhancing_manuscript.md` - WorkflowLLM Enhancing - DEP-E; overlap: capability, orchestration, workflow.
2. `.lake-data/DEP-E/DEP-E-20260724-OmniSQL Synthesizing/omnisql_synthesizing_manuscript.md` - OmniSQL Synthesizing - DEP-E; overlap: high-quality, scale.
3. `.lake-data/DEP-E/DEP-E-20260714-ComfyUI R1/comfyui_r1_manuscript.md` - ComfyUI-R1 Workflow - DEP-E; overlap: workflows, workflow.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
