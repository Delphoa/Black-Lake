# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260728-EB036F17`
- Deployment item ID: `BLAD-2200-20260728-EB036F17-P10`
- Public-safe date: 2026-07-28
- Paper: *CiteEval: Principle-Driven Citation Evaluation for Source Attribution*
- Identifier: `arXiv:2506.01829`; DOI: `10.48550/arXiv.2506.01829`
- URL: https://arxiv.org/abs/2506.01829

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75825 PDFs and 75822 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 25866.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant deposited identifiers, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CiteEval-Principle-Driven-Citation-Evaluation-for-Source-Attribution` slug; the 24-hour marker cutoff was 2026-07-27.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1957097 bytes with valid `%PDF-` header and trailing `%%EOF`; page markers: 24.
- Full-paper HTML: 265750 bytes, 41841 body characters, 61 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260728-Arxiv-CiteEval-Principle-Driven-Citation-Evaluation-for-Source-Attribution-LOG.md`
- `.reports/BL-Arxiv-CiteEval-Principle-Driven-Citation-Evaluation-for-Source-Attribution-20260728/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260728-CiteEval Principle-Driven/README.md`
- `.lake-data/DEP-E/DEP-E-20260728-CiteEval Principle-Driven/citeeval_principle_driven_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260727-Evidence-Gated Systems/evidence-gated-systems.md` - Evidence-Gated Systems - DEP-E; overlap: access, assessment, context.
2. `.lake-data/DEP-E/DEP-E-20260728-Reliability Proof Chains/reliability-proof-chains.md` - Reliability Proof Chains - DEP-E; overlap: access, assessment, but.
3. `.lake-data/DEP-E/DEP-E-20260721-Agent Evidence Loops/agent-evidence-loops.md` - Agent Evidence Loops - DEP-E; overlap: access, context, directly.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
