# 2026-07-21 - Arxiv RepoMasterEval Code Completion

## Job Context

- Actor: Codex recurring Arxiv DEP workflow.
- Deposit class: `DEP-E` research.
- Selected paper: *RepoMasterEval: Evaluating Code Completion via Real-World Repositories*.
- Stable identifier: `arXiv:2408.03519v2`; arXiv-issued DOI `10.48550/arXiv.2408.03519`.
- Canonical records: https://arxiv.org/abs/2408.03519 and https://conf.researchr.org/details/ase-2025/ase-2025-industry-showcase/50/RepoMasterEval-Evaluating-Code-Completion-via-Real-World-Repositories.
- Source policy: original PDF, full-paper HTML, metadata HTML, TeX/source, extracted material, renderings, and repair records were retained locally and withheld from the repository.

## Random Selection

- Candidate enumeration used `rg --files -g "*.pdf"` against the local arXiv archive.
- Enumeration found 75,779 PDF files in 75,776 distinct PDF-parent paper units.
- A normalized arXiv-ID set was derived from existing Black Lake Arxiv DEP artifacts and automation memory. It excluded 220 paper units, leaving 75,556 eligible units.
- PowerShell `Get-Random` selected zero-based eligible index 45,351 uniformly on the first draw.
- Selected base identifier: `2408.03519`.
- Duplicate reselections: 0.

## Deduplication and Acceptance

- Acceptance keys: base and versioned arXiv ID, arXiv-issued DOI, normalized title, and `RepoMasterEval` / code-completion slug variants.
- Scanned scopes: Black Lake `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and relevant Black-Lake-Data `.lake-data`, `.reports`, and `.lists` records.
- No prior Arxiv DEP log, report, or `DEP-E` deposit owns this paper.
- Black-Lake-Data contains one metadata inventory row for the paper; it is not a review or deposition and therefore is not a duplicate.
- The selected identity had no same-paper marker from the preceding 24 hours.

## Local Source-Integrity Gate

- Initial state: `partial`.
- The existing 774,901-byte PDF passed the 10 KB minimum, `%PDF-` header, trailing `%%EOF`, and SHA-256 checks.
- Full-paper HTML, metadata HTML, source archive, machine-readable summary, and verification report were initially absent.
- Repair preserved the valid PDF and used a bounded single-paper companion-bundle pull. The official full-paper HTML available for this work resolved to the v1 document while the preserved current PDF and source bundle correspond to the revised record.
- Final full-paper HTML: 461,536 bytes, 66,400 body characters, a document marker, 56 section/heading markers, and six paper-structure terms.
- Metadata HTML: 44,080 bytes.
- Source archive: 484,515 bytes with 30 readable entries.
- Final state: `complete`; zero partial files remained.
- No source file was copied into `.lake-data`, staged, committed, uploaded, or attached to Slack.

## Review Summary

- RepoMasterEval constructs 288 executable fill-in-the-middle code-completion tasks from six post-March-2023 Python and TypeScript repositories.
- Each task combines prefix, masked code, suffix, up to five BM25-retrieved repository snippets, and executable tests.
- Mutation-guided augmentation added 186 tests to 1,105 existing tests. The paper reports mutation-score increases from 73.6% to 84.5% for Python and 58.0% to 68.2% for TypeScript, while all ten evaluated model configurations lose pass rate under the stronger suites.
- DeepSeek-Coder-Base-33B has the strongest reported Pass@1 for both Python (44.87%) and TypeScript (34.57%). The paper also reports a 0.9601 Spearman correlation between offline RepoMasterEval scores and online acceptance for a small sequence of confidential internal model versions.
- Principal evidence boundary: only six repositories and two languages are represented; benchmark code/data and the industrial observations were not independently reproduced; production values are mostly reported as deltas; and no uncertainty analysis accompanies the correlation claim.

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260716-Repo Context Modalities/2604.13725-whitepaper-review.md`
   - Relevance: repository-level code completion depends on selecting useful cross-file context; this DEP evaluates compression modalities and matched code-task budgets.
2. `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/clover_test_benchmark_manuscript.md`
   - Relevance: both benchmarks use real repositories, executable tests, coverage-aware task construction, and explicit context budgets while separating runnable outputs from requirement-satisfying outputs.
3. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md`
   - Relevance: both use coverage and mutation behavior to improve test adequacy; this DEP adds the objective-selection tradeoff that RepoMasterEval leaves implicit.

## Outputs

- `.logs/20260721-Arxiv-RepoMasterEval-Code-Completion-LOG.md`
- `.reports/BL-Arxiv-RepoMasterEval-Code-Completion-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-RepoMasterEval/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-RepoMasterEval/repomastereval_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Does the benchmark ranking remain stable when repository snapshots, model versions, tokenizers, and BM25 retrieval parameters are pinned and rerun today?
2. How much of the reported offline-online correlation survives confidence intervals, more model versions, additional teams, and a preregistered acceptance-rate analysis?
3. Can mutation score, coverage, and task-level pass rate be combined without rewarding test overfitting or excluding valid alternative implementations?

## Challenges

1. The initially partial archive required a bounded repair before synthesis, and the verified HTML fallback is v1 while the current PDF/source record is v2.
2. The paper's industrial evidence withholds absolute scores, cohort details, and most operational metadata, limiting independent assessment of the correlation claim.
3. No verified public benchmark implementation was established, so the review can assess the design and reported tables but cannot claim reproducibility.
