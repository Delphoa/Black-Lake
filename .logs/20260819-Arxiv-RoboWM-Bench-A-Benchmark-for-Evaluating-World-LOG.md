# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P113`
- Public-safe date: 2026-08-19
- Paper: *RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation*
- Identifier: `arXiv:2604.19092`; DOI: `10.48550/arXiv.2604.19092`
- URL: https://arxiv.org/abs/2604.19092

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 8,940 on draw 10.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: world model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RoboWM-Bench-A-Benchmark-for-Evaluating-World` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 9; source-gate exclusions: 0; reselections: 9.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 18,408,004 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 24; sampled text inspection: true.
- Full-paper HTML: 472,415 bytes, 72,047 body characters, 85 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-RoboWM-Bench-A-Benchmark-for-Evaluating-World-LOG.md`
- `.reports/BL-Arxiv-RoboWM-Bench-A-Benchmark-for-Evaluating-World-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-RoboWM-Bench A Benchmark/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-RoboWM-Bench A Benchmark/robowm_bench_a_benchmark_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` - Semantic Skill MoE Policies; overlap: manipulation, robotic, benchmark.
2. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md` - FAVLA Fast-Slow - DEP-E; overlap: manipulation, robotic, benchmark.
3. `.lake-data/DEP-E/DEP-E-20260726-See Plan Rewind/see_plan_rewind_manuscript.md` - See Plan Rewind - DEP-E; overlap: manipulation, robotic.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
