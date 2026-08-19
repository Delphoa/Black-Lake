# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P485`
- Public-safe date: 2026-08-19
- Paper: *Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning*
- Identifier: `arXiv:2504.06438`; DOI: `10.48550/arXiv.2504.06438`
- URL: https://arxiv.org/abs/2504.06438

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 48,117 on draw 117.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Don-t-Let-It-Hallucinate-Premise-Verification` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 30; focus exclusions: 81; source-gate exclusions: 5; reselections: 116.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 988,211 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 24; sampled text inspection: true.
- Full-paper HTML: 383,400 bytes, 71,532 body characters, 74 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Don-t-Let-It-Hallucinate-Premise-Verification-LOG.md`
- `.reports/BL-Arxiv-Don-t-Let-It-Hallucinate-Premise-Verification-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Don t Let It Hallucinate/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Don t Let It Hallucinate/don_t_let_it_hallucinate_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-How Much Reasoning Do/how_much_reasoning_do_manuscript.md` - How Much Reasoning Do - DEP-E; overlap: retrieval-augmented, reasoning, verification.
2. `.lake-data/DEP-E/DEP-E-20260819-Improving Context/improving_context_manuscript.md` - Improving Context - DEP-E; overlap: retrieval-augmented, reasoning, verification.
3. `.lake-data/DEP-E/DEP-E-20260819-Reasoning in Trees/reasoning_in_trees_manuscript.md` - Reasoning in Trees - DEP-E; overlap: retrieval-augmented, reasoning, verification.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
