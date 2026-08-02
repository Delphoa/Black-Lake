# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260802-0D11B2FA`
- Deployment item ID: `BLAD-2200-20260802-0D11B2FA-P04`
- Public-safe date: 2026-08-02
- Paper: *NLP-AKG: Few-Shot Construction of NLP Academic Knowledge Graph Based on LLM*
- Identifier: `arXiv:2502.14192`; DOI: `10.48550/arXiv.2502.14192`
- URL: https://arxiv.org/abs/2502.14192

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 30,672 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `NLP-AKG-Few-Shot-Construction-of-NLP` slug; the 24-hour marker cutoff was 2026-08-01.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 875,533 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 218,049 bytes, 55,454 body characters, 56 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260802-Arxiv-NLP-AKG-Few-Shot-Construction-of-NLP-LOG.md`
- `.reports/BL-Arxiv-NLP-AKG-Few-Shot-Construction-of-NLP-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-NLP-AKG Few-Shot/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-NLP-AKG Few-Shot/nlp_akg_few_shot_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` - OMGEval Benchmark - DEP-E; overlap: nlp, knowledge, llm, construction.
2. `.lake-data/DEP-E/DEP-E-20260802-COVID Fake News/covid_fake_news_manuscript.md` - COVID Fake News - DEP-E; overlap: nlp, knowledge, graph, construction.
3. `.lake-data/DEP-E/DEP-E-20260710-BEAGLE Learner/beagle_learner_manuscript.md` - BEAGLE Learner - DEP-E; overlap: few-shot, knowledge, llm.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
