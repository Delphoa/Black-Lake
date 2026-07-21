# Report-Mark: RepoMasterEval

## Source Metadata

- `Title`: *RepoMasterEval: Evaluating Code Completion via Real-World Repositories*.
- `Authors`: Qinyun Wu, Chao Peng, Pengfei Gao, Ruida Hu, Haoyu Gan, Bo Jiang, Jinhe Tang, Zhiwen Deng, Zhanming Guan, Cuiyun Gao, Xia Liu, and Ping Yang.
- `Stable identifier`: `arXiv:2408.03519v2`; arXiv-issued DOI https://doi.org/10.48550/arXiv.2408.03519.
- `Dates`: submitted 2024-08-07; revised 2025-10-31.
- `Subjects`: Software Engineering (`cs.SE`) and Artificial Intelligence (`cs.AI`).
- `Venue`: ASE 2025 Industry Showcase, verified through the official program record.
- `Primary records`: https://arxiv.org/abs/2408.03519, https://arxiv.org/pdf/2408.03519, https://arxiv.org/html/2408.03519v1, and https://arxiv.org/e-print/2408.03519.
- `License`: CC BY-NC-SA 4.0 as linked by the arXiv record.
- `Source status`: complete local PDF, full-paper HTML, metadata HTML, and source archive inspected; all originals and intermediate files withheld locally.

## Research Notes

### Problem

RepoMasterEval targets a mismatch between common coding benchmarks and in-editor completion. Description-led function or class synthesis provides information that is often absent at the cursor, omits fill-in-the-middle behavior, and can score by textual similarity even when multiple implementations are functionally correct. Real completion also depends on cross-file repository evidence and a test oracle strong enough to reject plausible but faulty alternatives.

### Method

The benchmark contains 288 tasks from six repositories: 115 Python and 173 TypeScript. Coverage identifies test-exercised source regions that can be masked at line, block, or function granularity. A model receives prefix, suffix, up to five BM25-ranked snippets from other files, and the task metadata; its completion is reinserted into the repository and evaluated by tests.

The authors audit the tests with mutation operators. Surviving mutants motivate additional tests written through human-LLM collaboration and repaired by developers when necessary. Across the six repositories, 186 tests are added to 1,105 existing tests.

### Evidence and Results

- Reported mutation score increases from 73.6% to 84.5% for Python and from 58.0% to 68.2% for TypeScript. Code coverage moves only from 71% to 72% for Python and remains 42% for TypeScript.
- All ten evaluated model configurations lose pass rate under the augmented suites. This is direct evidence that the original suites admitted outputs killed by the stronger tests, within the chosen mutation and test process.
- DeepSeek-Coder-Base-33B leads reported Pass@1 at 44.87% for Python and 34.57% for TypeScript. GPT-3.5 leads Python Pass@5 at 55.65%; DeepSeek-Coder-Base-33B leads TypeScript Pass@5 at 40.46%.
- Exact match and Jaccard similarity do not align cleanly with functional pass rate. The source examples also show format-specific failures: an instruct model emits extra functions, and GPT-4 repeats prefix/import content.
- The industry section reports Spearman correlation 0.9601 between offline benchmark scores and online acceptance across confidential internal versions. This is an author-reported association, not an independently verified or causal result.

### Limitations

- Six repositories, two languages, and 288 tasks cannot cover the diversity of production code completion.
- A post-March-2023 repository cutoff mitigates but does not eliminate training contamination.
- Fixed BM25 retrieval entangles model ability with one context policy.
- Mutation score depends on the operator set and may include equivalent mutants; no false-rejection audit for valid alternatives is reported.
- The ten-model table lacks confidence intervals and repository-stratified uncertainty.
- The industrial result withholds absolute scores, cohort sizes, usage distributions, and most confounders.
- No verified public benchmark implementation, immutable task manifest, repository SHA set, environment lock, or output bundle was established.

## Evidence and Attribution

| ID | Evidence | Supports | Assessment |
|---|---|---|---|
| E1 | Complete current PDF and TeX/source | Task construction, test augmentation, model tables, industry result | High confidence in transcription; experiments not rerun |
| E2 | Verified full-paper HTML fallback | Structural and section cross-checks | Complete v1 companion; not used to override v2 PDF/source |
| E3 | arXiv record | Identity, version, dates, authors, DOI, subjects, license | High confidence |
| E4 | Official ASE 2025 program | Venue placement and public abstract | High confidence |
| E5 | Five rendered PDF table/result pages | Benchmark structure, mutation results, model metrics, category and industry tables | Visually inspected; no clipping or extraction-only reliance |
| E6 | Exactly three related DEP artifacts | Repository context, executable evaluator, and coverage/mutation synthesis | Conceptual overlap; no joint experiment |

## Selection and Deduplication

- `Enumeration method`: `rg --files -g "*.pdf"` over the local arXiv archive; PDF parent directory treated as one paper unit.
- `Population`: 75,779 PDFs and 75,776 paper units.
- `Exclusions`: 220 normalized-ID matches from prior Black Lake artifacts and automation memory.
- `Eligible population`: 75,556 units.
- `Random method`: PowerShell `Get-Random`; zero-based eligible index 45,351; first draw; zero reselections.
- `Acceptance keys`: base/versioned arXiv ID, DOI, normalized title, and `RepoMasterEval` slug variants.
- `Acceptance scopes`: Black Lake `.logs`, `.reports`, `.lake-data`, dedup index, automation memory, and relevant Black-Lake-Data `.lake-data`, `.reports`, and `.lists` entries.
- `Result`: no prior owning review/deposit and no same-paper marker in the preceding 24 hours. A Black-Lake-Data inventory row is metadata only.

## Local Source-Integrity Validation

- Initial classification: `partial` because full-paper HTML was missing.
- Existing PDF: 774,901 bytes; `%PDF-` header and trailing `%%EOF` present; 12 pages; preserved unchanged.
- Repair: bounded single-paper companion acquisition; no blind retries, no credential use, and no partial files left behind.
- Full-paper HTML: 461,536 bytes, 66,400 body characters, a document marker, 56 section/heading markers, and six paper-structure terms.
- Metadata HTML: 44,080 bytes.
- Source archive: 484,515 bytes and 30 readable entries.
- Final classification: `complete`.
- Version boundary: the current PDF/source evidence governs v2 claims; the verified complete-paper HTML fallback is v1.
- Source locality: all source files, extracted text, caches, renderings, and repair records were withheld. No `.source/` directory was created and no source file was uploaded.

## Related DEP Entries

1. [Repository Context Modalities](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-Repo%20Context%20Modalities/2604.13725-whitepaper-review.md)
   - `Concrete overlap`: both center repository-level code completion/generation and the value of cross-file evidence under a context budget.
   - `Source basis`: Black Lake review of https://arxiv.org/abs/2604.13725v1 and its complete paper.
2. [CLOVER Test Benchmark](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-CLOVER%20Test%20Benchmark/clover_test_benchmark_manuscript.md)
   - `Concrete overlap`: both construct executable repository tasks from coverage and evaluate model-generated code; CLOVER distinguishes execution from target and coverage satisfaction.
   - `Source basis`: Black Lake review of https://arxiv.org/abs/2502.08806 and official venue context.
3. [Smart Coverage Goals](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md)
   - `Concrete overlap`: both use coverage and mutation behavior to improve test objectives and expose weaknesses hidden by raw coverage.
   - `Source basis`: Black Lake review of https://arxiv.org/abs/2208.04096 and ASE artifact context.

## Synthesis Note

### Concept Bridge

The paper and the three DEP entries form one evaluation pipeline. RepoMasterEval defines the realistic completion surface and tests generated code. Repository Context Modalities asks which cross-file evidence should fit into a bounded prompt. CLOVER strengthens the evaluator by separating parse/execution success from satisfaction of explicit target and coverage requirements. Smart Coverage Goals shows that the oracle itself is a budgeted multi-objective system: adding criteria can improve fault sensitivity while diluting search guidance or growing the suite. The joint design implication is a versioned gate with separately auditable context, oracle, model, and product-validity layers.

### Potential Implementations

1. `Repository completion release gate`: execute pinned fill-in-the-middle tasks across context policies, report repository-stratified Pass@k and format failures, and block rollout on significant regression.
2. `Test-oracle adequacy service`: combine coverage, mutation, seeded-defect detection, and valid-alternative review before a test suite may score model output.
3. `Offline-online calibration monitor`: join signed benchmark receipts to deidentified aggregate acceptance metrics and report intervals, drift, and confounder notes without claiming causality.

### Deeper Relationship Observations

1. Context retrieval and test adequacy are dual selection problems: one chooses evidence presented to the model, while the other chooses behavioral distinctions enforced after generation. Bias in either side changes the apparent model score.
2. RepoMasterEval's nearly static coverage but rising mutation score and Smart Coverage Goals' criterion-specific tradeoffs both show that more observed or optimized structure is not automatically more informative structure.
3. CLOVER's gap between execution and requirement success explains why RepoMasterEval should evolve beyond one repository-wide pass/fail outcome toward typed evaluator failures that identify missing target use, insufficient coverage, or unsafe workspace effects.

### Conceptual Similarities

1. All four artifacts treat repository evidence as structured and budget constrained rather than as an undifferentiated text blob.
2. All four distinguish proxy metrics from downstream utility: compression ratio from code quality, execution from requirement success, coverage from mutation strength, and benchmark pass rate from user acceptance.
3. All four require provenance and version pinning because repositories, tests, models, context policies, and product behavior change over time.

### MVP Implementations with Code Mock-Ups

1. `Adequacy gate`

```python
def adequate_suite(coverage, mutation, seeded_faults):
    return {
        "coverage_ok": coverage >= 0.70,
        "mutation_ok": mutation >= 0.80,
        "seeded_faults_ok": seeded_faults == 1.0,
    }
```

This MVP refuses to reduce oracle quality to one metric. Thresholds are placeholders and must be calibrated per repository.

2. `Context-policy experiment`

```python
POLICIES = ("problem_only", "bm25", "dependency", "compressed")

def planned_trials(task_id, token_budget):
    return [
        {"task_id": task_id, "policy": policy, "budget": token_budget}
        for policy in POLICIES
    ]
```

Each trial holds the task and token budget fixed so context selection can be compared without hiding cost.

3. `Typed completion verdict`

```python
def verdict(syntax_ok, tests_ok, target_ok, coverage_ok, source_leak=False):
    checks = (syntax_ok, tests_ok, target_ok, coverage_ok)
    return "pass" if all(checks) and not source_leak else "fail"
```

The real harness should preserve every component result rather than storing only the final string.

### Developer Challenges

1. Rebuilding old repositories and dependencies deterministically without exposing the host or network to model-generated code.
2. Designing tests that accept valid alternatives while still killing realistic faults and rejecting evasive or malformed completions.
3. Comparing context policies and model versions under equal token, latency, sampling, and repository conditions.

### Author Challenges

1. Publish immutable task manifests, repository commits, environment locks, prompts, test patches, and generated outputs sufficient for independent replay.
2. Quantify statistical uncertainty and repository/slice variance instead of relying on aggregate point estimates.
3. Expand industrial validation with more model versions, organizations, cohorts, and preregistered analyses while protecting user and source privacy.

## Validation Notes

- Required Report-Mark sections, source metadata, evidence labels, related DEP reasons, source basis, and final attribution are present.
- The Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- Source-first review covered methods, experiments, results, discussion, conclusion, tables, figures, TeX/source, metadata, and official venue context.
- Numerical claims were transcribed from inspected paper tables/prose and remain attributed to the authors.
- Public-safety review found no local path, username, machine name, workspace root, local timezone label, or exact local execution timestamp.
- No source file or `.source/` directory is included.

## Attribution Block

- Primary paper: https://arxiv.org/abs/2408.03519
- Canonical PDF: https://arxiv.org/pdf/2408.03519
- Verified full-paper HTML fallback: https://arxiv.org/html/2408.03519v1
- TeX/source locator: https://arxiv.org/e-print/2408.03519
- arXiv-issued DOI: https://doi.org/10.48550/arXiv.2408.03519
- Official venue record: https://conf.researchr.org/details/ase-2025/ase-2025-industry-showcase/50/RepoMasterEval-Evaluating-Code-Completion-via-Real-World-Repositories
- License: https://creativecommons.org/licenses/by-nc-sa/4.0/
- Related DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-Repo%20Context%20Modalities/2604.13725-whitepaper-review.md
- Related DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-CLOVER%20Test%20Benchmark/clover_test_benchmark_manuscript.md
- Related DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md
- Source-file policy: all original and intermediate source files were retained locally and withheld from this repository.
