# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P273`
- Public-safe date: 2026-08-19
- Paper: *Causal Disentanglement Hidden Markov Model for Fault Diagnosis*
- Identifier: `arXiv:2308.03027`; DOI: `10.48550/arXiv.2308.03027`
- URL: https://arxiv.org/abs/2308.03027

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 18,833 on draw 16.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: markov, model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Causal-Disentanglement-Hidden-Markov-Model-for` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 13; source-gate exclusions: 0; reselections: 15.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,225,974 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 239,901 bytes, 62,561 body characters, 62 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Causal-Disentanglement-Hidden-Markov-Model-for-LOG.md`
- `.reports/BL-Arxiv-Causal-Disentanglement-Hidden-Markov-Model-for-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Causal Disentanglement/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Causal Disentanglement/causal_disentanglement_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-Stock Market Trend/stock_market_trend_manuscript.md` - Stock Market Trend - DEP-E; overlap: markov, hidden, causal.
2. `.lake-data/DEP-E/DEP-E-20260819-Inference of collective/inference_of_collective_manuscript.md` - Inference of collective - DEP-E; overlap: markov, hidden, causal.
3. `.lake-data/DEP-E/DEP-E-20260812-Multi-Step Alignment as/multi_step_alignment_as_manuscript.md` - Multi-Step Alignment as - DEP-E; overlap: markov, causal.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
