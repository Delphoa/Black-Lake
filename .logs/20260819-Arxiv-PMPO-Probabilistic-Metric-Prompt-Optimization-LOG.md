# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P192`
- Public-safe date: 2026-08-19
- Paper: *PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models*
- Identifier: `arXiv:2505.16307`; DOI: `10.48550/arXiv.2505.16307`
- URL: https://arxiv.org/abs/2505.16307

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 21,615 on draw 1.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `PMPO-Probabilistic-Metric-Prompt-Optimization` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,043,808 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 34; sampled text inspection: true.
- Full-paper HTML: 2,479,958 bytes, 136,060 body characters, 116 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-PMPO-Probabilistic-Metric-Prompt-Optimization-LOG.md`
- `.reports/BL-Arxiv-PMPO-Probabilistic-Metric-Prompt-Optimization-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-PMPO Probabilistic Metric/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-PMPO Probabilistic Metric/pmpo_probabilistic_metric_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260810-Prompt Tuning for/prompt_tuning_for_manuscript.md` - Prompt Tuning for - DEP-E; overlap: prompt, language, metric.
2. `.lake-data/DEP-E/DEP-E-20260723-Unveiling the Lexical Sen/unveiling_the_lexical_sen_manuscript.md` - Unveiling the Lexical Sensitivit - DEP-E; overlap: prompt, optimization, language, metric.
3. `.lake-data/DEP-E/DEP-E-20260729-A Systematic Survey of/a_systematic_survey_of_manuscript.md` - A Systematic Survey of - DEP-E; overlap: prompt, optimization, language, metric.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
