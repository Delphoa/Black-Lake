# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260726-1DBD5211`
- Deployment item ID: `BLAD-2200-20260726-1DBD5211-P10`
- Public-safe date: 2026-07-26
- Paper: *Baichuan Alignment Technical Report*
- Identifier: `arXiv:2410.14940`; DOI: `10.48550/arXiv.2410.14940`
- URL: https://arxiv.org/abs/2410.14940

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 8,499 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Baichuan-Alignment-Technical-Report` slug; the 24-hour marker cutoff was 2026-07-25.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,457,275 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 28; sampled text inspection: true.
- Full-paper HTML: 383,418 bytes, 105,554 body characters, 149 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260726-Arxiv-Baichuan-Alignment-Technical-Report-LOG.md`
- `.reports/BL-Arxiv-Baichuan-Alignment-Technical-Report-20260726/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260726-Baichuan Alignment/README.md`
- `.lake-data/DEP-E/DEP-E-20260726-Baichuan Alignment/baichuan_alignment_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-WorkflowLLM Enhancing/workflowllm_enhancing_manuscript.md` - WorkflowLLM Enhancing - DEP-E; overlap: capability, orchestration, workflow.
2. `.lake-data/DEP-E/DEP-E-20260719-MIRA One Touch/mira_one_touch_manuscript.md` - One-Touch Instruction Routing; overlap: instruction, retrieval, recommendation.
3. `.lake-data/DEP-E/DEP-E-20260722-Graph Alignment/graph_alignment_manuscript.md` - Graph Alignment Review - DEP-E; overlap: alignment, recommendation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
