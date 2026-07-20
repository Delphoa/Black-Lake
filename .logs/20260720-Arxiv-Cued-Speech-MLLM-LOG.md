# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P06`
- Public-safe date: 2026-07-20
- Paper: *Lend a Hand: Semi Training-Free Cued Speech Recognition via MLLM-Driven Hand Modeling for Barrier-free Communication*
- Identifier: `arXiv:2503.21785v1`
- URL: https://arxiv.org/abs/2503.21785

## Random Selection

- Enumerated 75,779 PDFs and 75,776 unique parent units using `rg --files -g "*.pdf"`.
- Uniform `Get-Random` selected one-based index 25,944 on the first draw without a derived seed.

## Deduplication and Reselection

- Scanned Black Lake logs, reports, deposits and indexes; automation memory; relevant Black-Lake-Data records; the current-job set; and 24-hour markers since 2026-07-19.
- Keys: arXiv ID, DOI, normalized title, and `Cued-Speech-MLLM` slug.
- Duplicate exclusions: 0; reselections: 0.

## Source Integrity

- Initial state: partial; valid PDF present, full-paper HTML absent.
- One bounded official-source pass retrieved full-paper and metadata HTML.
- PDF: 3,217,991 bytes with valid header/EOF. HTML: 301,714 bytes, 52,368 body characters, 2 document markers, 24 headings, and 47 structure terms.
- Final state: verified complete; sources and integrity records remain local.

## Public Outputs

- `.logs/20260720-Arxiv-Cued-Speech-MLLM-LOG.md`
- `.reports/BL-Arxiv-Cued-Speech-MLLM-20260720/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260720-Cued Speech MLLM/README.md`
- `.lake-data/DEP-E/DEP-E-20260720-Cued Speech MLLM/cued_speech_mllm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`

Only generated Markdown/JSON is eligible for staging. Participant video, datasets, images, PDF, HTML, code, checkpoints, caches, and extracted source text remain local or at public source locators; zero source-document uploads.
