# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260809-2E4CB30E`
- Deployment item ID: `BLAD-2200-20260809-2E4CB30E-P08`
- Public-safe date: 2026-08-09
- Paper: *Voice Evaluation of Reasoning Ability: Diagnosing the Modality-Induced Performance Gap*
- Identifier: `arXiv:2509.26542`; DOI: `10.48550/arXiv.2509.26542`
- URL: https://arxiv.org/abs/2509.26542

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 59,691 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Voice-Evaluation-of-Reasoning-Ability-Diagnosing` slug; the 24-hour marker cutoff was 2026-08-08.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 6,177,165 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 23; sampled text inspection: true.
- Full-paper HTML: 422,616 bytes, 78,764 body characters, 93 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260809-Arxiv-Voice-Evaluation-of-Reasoning-Ability-Diagnosing-LOG.md`
- `.reports/BL-Arxiv-Voice-Evaluation-of-Reasoning-Ability-Diagnosing-20260809/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260809-Voice Evaluation of/README.md`
- `.lake-data/DEP-E/DEP-E-20260809-Voice Evaluation of/voice_evaluation_of_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` - AV Emotion Fusion - DEP-E; overlap: diagnosing, voice, gap, performance.
2. `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI/beyond_xai_manuscript.md` - Beyond XAI - DEP-E; overlap: diagnosing, reasoning, gap, performance.
3. `.lake-data/DEP-E/DEP-E-20260713-SAILFISH Vetting/sailfish_vetting_manuscript.md` - SAILFISH Review - DEP-E; overlap: ability, reasoning, gap, performance.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
