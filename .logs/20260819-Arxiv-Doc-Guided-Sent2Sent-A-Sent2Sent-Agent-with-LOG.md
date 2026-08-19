# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P186`
- Public-safe date: 2026-08-19
- Paper: *Doc-Guided Sent2Sent++: A Sent2Sent++ Agent with Doc-Guided memory for Document-level Machine Translation*
- Identifier: `arXiv:2501.08523`; DOI: `10.48550/arXiv.2501.08523`
- URL: https://arxiv.org/abs/2501.08523

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 44,696 on draw 29.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: agent, memory.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Doc-Guided-Sent2Sent-A-Sent2Sent-Agent-with` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 26; source-gate exclusions: 0; reselections: 28.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,095,265 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 186,546 bytes, 46,264 body characters, 69 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Doc-Guided-Sent2Sent-A-Sent2Sent-Agent-with-LOG.md`
- `.reports/BL-Arxiv-Doc-Guided-Sent2Sent-A-Sent2Sent-Agent-with-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Doc-Guided Sent2Sent A/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Doc-Guided Sent2Sent A/doc_guided_sent2sent_a_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-RAPL Relation-Aware/rapl_relation_aware_manuscript.md` - RAPL Relation-Aware - DEP-E; overlap: document-level, translation, memory.
2. `.lake-data/DEP-E/DEP-E-20260723-ScaleEnv Scaling Environm/scaleenv_scaling_environm_manuscript.md` - ScaleEnv Scaling Environment Syn - DEP-E; overlap: agent, translation, memory.
3. `.lake-data/DEP-E/DEP-E-20260730-Personalized Safety in/personalized_safety_in_manuscript.md` - Personalized Safety in - DEP-E; overlap: agent, translation, memory.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
