# Report-Mark: CLOVER Test Benchmark

## Source Metadata

- `Title`: *CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification*.
- `Authors`: Jiacheng Xu; Bo Pang; Jin Qu; Hiroaki Hayashi; Caiming Xiong; Yingbo Zhou.
- `Organization`: Salesforce AI Research.
- `arXiv`: `2502.08806v1`, submitted 2025-02-12.
- `DOI`: https://doi.org/10.48550/arXiv.2502.08806.
- `Subjects`: Software Engineering (`cs.SE`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`).
- `Venue context`: DL4C @ ICLR 2025 long-paper track, https://openreview.net/forum?id=gPpQa4PGEZ.
- `Primary sources`: https://arxiv.org/abs/2502.08806, https://arxiv.org/pdf/2502.08806, https://arxiv.org/html/2502.08806, and https://arxiv.org/e-print/2502.08806.
- `License visibility`: arXiv version shows CC BY-NC-SA 4.0; OpenReview record shows CC BY 4.0 for its hosted workshop version.
- `Access date`: 2026-07-19.
- `Source state`: verified complete locally after bounded repair; PDF, full-paper HTML, metadata HTML, and source package are present in the private archive.
- `Public-source policy`: all original source documents and local verification records are withheld. Only generated Markdown and public locators are deposited.
- `Release status`: the paper promises code, data, a Docker environment, and recipes. No official CLOVER implementation or dataset repository was established from the inspected paper source, arXiv/OpenReview records, author page, Hugging Face paper record, or exact GitHub searches. The benchmark was not run.

## Concise Research Notes

### Research Question

Can language models complete or generate executable Python tests that satisfy explicit target and coverage requirements when given repository-scale code context?

### Benchmark Design

CLOVER starts from 42 Python repositories, automatically configures 25, and retains 12. It constructs 845 unique problems and 5,312 context-expanded instances. The benchmark cutoff is 2024-08-30. Tasks are executed in Dockerized Python 3.10 environments with pytest and pytest-cov; the paper describes timeouts, error handling, batching, and repository restoration.

The three tasks form a difficulty ladder:

1. `Task I - assertion mask prediction`: 513 unique problems; fill one missing assertion expression. Metrics are exact match, execution rate, and refined execution rate.
2. `Task II - targeted test implementation`: 151 unique problems; generate a test using a specified class or function. Success requires executable code and target use.
3. `Task III - coverage-oriented test implementation`: 181 unique problems; generate tests that cover up to ten specified code blocks across up to ten files. Success requires execution and coverage of every requested block.

### Coverage-Calibrated Context

The paper builds oracle context from ground-truth test execution. It compares ordinary test coverage with an empty test to identify repository-baseline files, then finds lines uniquely covered by a peer test. Context priority is peer-unique files, other informative files, then repository-baseline files; random selection is used within a tier when the token budget cannot fit every file.

This is a valuable experiment because it reduces the retrieval problem and tests model context utilization. It is not a deployable retriever by itself because a genuinely new test does not have a ground-truth coverage trace.

### Evidence and Results

- Task I Table 4 reports Claude 3.5 Sonnet at 75.4% best RER, versus 72.4% problem-only. The prose reports 72.6% to 75.6%; the table/PDF values are treated as authoritative and the discrepancy is retained.
- Longer context harms several open models. Codestral-22B falls from 63.3% problem-only RER to 22.1% at 32k; Qwen 2.5 Coder 14B falls from 59.8% to 30.7%.
- Task II best reported success is 48.4%, reached by Claude 3.5 Sonnet and GPT-4o in their strongest contextual settings.
- Task III best reported success is GPT-4o at 32.7% with 64k context; no evaluated open-source model exceeds 10%.
- Task III execution consistently exceeds requirement-satisfying success. GPT-4o at 64k reports 42.1% execution and 32.7% success; Gemini 1.5 Flash reports 38.3% and 28.0%; Claude 3.5 Sonnet reports 34.6% and 29.0%.

### Reviewer Assessment

CLOVER's durable contribution is a benchmark contract: generated tests must be evaluated at multiple layers—parse, execution, anti-triviality, required target, and requested coverage—while context selection is measured rather than assumed. The evidence supports difficulty and non-monotonic context utilization under the tested 2024 model snapshots. It does not support a current leaderboard, cross-language generalization, production safety, or reproducibility without a released artifact.

### Principal Strengths

- Executable repository grounding rather than text-only comparison.
- Three tasks that separate completion, target satisfaction, and coverage satisfaction.
- Coverage-derived context prioritization with an explicit baseline.
- Multiple metrics that reveal the gap between runnable and requirement-compliant tests.
- Transparent appendix material on repositories, exclusions, prompts, and alternate results.

### Principal Limitations

- Python/pytest and 12 repositories only.
- Ground-truth coverage makes the context policy oracle rather than production-realistic.
- Environment construction requires heuristics and manual mapping.
- Line/block coverage does not establish assertion quality, mutation adequacy, or defect revelation.
- Model/provider snapshots and serving configuration are dated.
- Main results do not foreground repeated-run uncertainty.
- Official code/data/container release was not established, so the study was not reproduced.
- Docker containment did not prevent resource exhaustion in some excluded repository cases.

## Evidence and Attribution

| Evidence ID | Evidence | Claim Support | Reviewer Handling |
|---|---|---|---|
| E1 | Complete PDF, full-paper HTML, and TeX/source package for arXiv:2502.08806v1 | Mechanism, task counts, tables, prompts, results, limitations, safety, appendices | Inspected fully; PDF result pages visually checked; no long quotations copied |
| E2 | https://arxiv.org/abs/2502.08806 | Identity, authors, date, subjects, DOI, license | Metadata only; not used alone for empirical claims |
| E3 | https://openreview.net/forum?id=gPpQa4PGEZ | DL4C @ ICLR 2025 status, track, dates, license | Official venue context; not an independent replication |
| E4 | https://jiacheng-xu.github.io/ | Author-maintained publication listing | Identity/context only |
| E5 | Exact release searches plus paper/source inspection | No official CLOVER repository was established | Recorded as an availability limitation, not proof of permanent absence |
| E6 | Three fetched Black Lake DEP artifacts | Coverage-objective, context-filtering, and dependency-memory synthesis | Related-entry claims remain attributed to their own reviewed sources |
| E7 | Live Black Lake and Black-Lake-Data READMEs | Deposit layout, attribution, source locality, dedup scope | Treated as repository authority, not research evidence |
| E8 | Local verification receipt | Complete-source gate | Public summary only; local paths and source files withheld |

### Random Selection and Dedup Evidence

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent units, used-ID exclusion, then uniform PowerShell `Get-Random` selection.
- Counts: 75,778 PDFs; 75,776 paper units; 810 used IDs; 192 units excluded by used ID; 185 identifier-incomplete units withheld; 75,399 eligible units.
- Selected zero-based eligible index: 33,124.
- Selected ID/title: `2502.08806v1`, *CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification*.
- Dedup scan: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; Black-Lake-Data `.lake-data` and `.reports`.
- Keys: arXiv ID, DOI, exact/normalized title, and slug.
- Duplicate reselections: zero.
- Public-safe 24-hour cutoff: 2026-07-18; no same-paper or same-unit marker was found on or after the cutoff.

### Source-Integrity Evidence

- Initial classification: partial because full-paper HTML was missing.
- Preserved PDF: 827,506 bytes, `%PDF-` header, trailing `%%EOF`.
- Repaired official full-paper HTML: 526,611 bytes, 88,981 body characters, full-document marker, 55 headings/sections, seven structure terms.
- Metadata HTML: 42,490 bytes; metadata-only.
- Source package: 330,636 bytes.
- Partials after repair: zero.
- Local records updated: README, attribution/provenance note, CSV summary, and JSON verification report.
- Final classification: complete; review began only after this gate passed.

## Related DEP Entries

Exactly three related entries were selected from fetched live repository state:

| Entry | Concrete Relevance | Source Basis |
|---|---|---|
| [Smart Coverage Goals](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md) | Both systems turn coverage into an explicit control signal. The related DEP reviews goal selection for search-based unit tests; CLOVER uses peer-unique coverage to choose requirements and order context. | Review of https://arxiv.org/abs/2208.04096 and the ASE publication/artifact records |
| [TACO Terminal Context](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-TACO%20Terminal%20Context/2604.19572-whitepaper-review.md) | Both study whether software-engineering systems can preserve useful evidence under long observations. TACO compresses terminal output adaptively; CLOVER measures model success as code context expands. | Review of https://arxiv.org/abs/2604.19572v3 and https://github.com/multimodal-art-projection/TACO |
| [ContextWeaver Selective Context](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-ContextWeaver%20Selective%20a/2604.23069-whitepaper-review.md) | Both select prior evidence for coding tasks. ContextWeaver preserves dependency and validation lineage; CLOVER ranks whole files from coverage tiers without dependency edges. | Review of https://arxiv.org/abs/2604.23069v1 |

## Synthesis Note

### Concept Bridge

The four artifacts can be organized around a single question: what evidence should a test-generation or coding system preserve, optimize, and verify under a bounded budget? Smart Coverage Goals operates on the objective budget, CLOVER on the code-context and evaluator contract, TACO on terminal-observation compression, and ContextWeaver on dependency-structured interaction memory. Together they suggest a governed evidence pipeline:

`authorized source -> objective selection -> evidence retrieval/compression -> generated action -> isolated execution -> layered verification -> lineage-aware feedback`.

CLOVER supplies the middle benchmark contract. It makes clear that context quantity, executability, and coverage compliance are distinct variables. The related entries supply mechanisms for reducing redundant objectives, suppressing noisy observations, and retaining dependency/validation lineage.

### Potential Implementations

1. `Traceable coverage-to-context builder`: rank code slices using coverage, static dependencies, and failed-test lineage; emit inclusion and exclusion reasons with a token budget.
2. `Layered generated-test gate`: classify parse, collection, execution, target-use, assertion quality, block coverage, resource use, and repository mutation separately.
3. `Adaptive benchmark controller`: allocate context and evaluation effort based on task difficulty while preserving deterministic manifests and comparable budgets.

### Deeper Relationship Observations

1. Coverage is both a goal and an information channel. Smart Coverage Goals uses it to steer search; CLOVER uses it to choose evidence and score output. Treating both roles as one metric risks leakage unless construction traces are separated from evaluation traces.
2. Compression errors and context-utilization failures have the same downstream symptom: the model misses a requirement. TACO's complaint repair and ContextWeaver's dependency lineage offer diagnostic signals that CLOVER's aggregate context-utilization metric lacks.
3. Verification creates memory. A failed or superseded test run should not be discarded as mere noise; it can explain which context was missing and which requirement remains unsatisfied. ContextWeaver's validation states make that history explicit.

### Conceptual Similarities

1. All four artifacts replace raw quantity with selective structure: fewer objectives, ranked files, filtered observations, or dependency-linked memory.
2. All require explicit budgets—search goals, tokens, observations, iterations, CPU time, or sandbox resources—and fail when the budget policy is hidden.
3. All separate a proxy from the desired outcome: coverage from fault detection, token reduction from task success, remembered steps from useful causality, and execution from requirement satisfaction.

### MVP Implementations with Code Mock-Ups

1. `Layered evaluator result`

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class TestOutcome:
    parsed: bool
    executed: bool
    target_used: bool
    required_blocks_covered: bool

    @property
    def success(self) -> bool:
        return all((self.parsed, self.executed,
                    self.target_used, self.required_blocks_covered))
```

This preserves the CLOVER distinction between runnable code and requirement-compliant tests. A production version also needs timeout, resource, mutation, and provenance fields.

2. `Evidence-budget selector`

```python
def select_evidence(nodes, token_budget):
    ranked = sorted(
        nodes,
        key=lambda n: (n["required"], n["peer_unique"],
                       n["dependency_score"], -n["tokens"]),
        reverse=True,
    )
    chosen, used = [], 0
    for node in ranked:
        if used + node["tokens"] <= token_budget:
            chosen.append(node)
            used += node["tokens"]
    return chosen
```

This combines CLOVER's priority tiers with ContextWeaver-style dependency scoring. It is illustrative; real selection must preserve access controls and dynamic dependencies.

3. `Safe task-manifest validation`

```python
from pathlib import PurePosixPath

def validate_task(task):
    assert task["network"] is False
    assert 0 < task["timeout_seconds"] <= 120
    assert task["memory_mb"] <= 2048
    for path in task["allowed_files"]:
        p = PurePosixPath(path)
        assert not p.is_absolute() and ".." not in p.parts
    return True
```

This is a narrow preflight check, not a sandbox. The runner still needs process, filesystem, network, and host-kernel isolation.

### Developer Challenges

1. Reconstructing historical repository environments without confusing dependency failure, flaky tests, or harness bugs with model failure.
2. Building an evaluator that recognizes meaningful equivalent tests while rejecting trivial assertions, target omission, partial coverage, and workspace side effects.
3. Enforcing strong isolation and reproducible resource budgets for untrusted generated code across heterogeneous projects.

### Author Challenges

1. Publishing and maintaining a versioned artifact that binds repository SHAs, licenses, prompts, containers, evaluator semantics, model snapshots, and result tables.
2. Demonstrating that coverage-ranked oracle context predicts performance with deployable non-oracle retrieval rather than only with ground-truth test traces.
3. Reporting uncertainty, per-repository effects, cost, and semantic test quality strongly enough to support conclusions beyond one Python/pytest benchmark slice.

## Validation Notes

- Required manuscript skill and full artifact schema were read before drafting the DEP manuscript.
- Live `Delphoa/Black-Lake` README and `.lake-data/README.md` were fetched and treated as submission authority.
- Live `Delphoa-Labs/Black-Lake-Data` README was fetched before its history was used for deduplication.
- Source integrity passed only after the missing full-paper HTML was repaired; abstract-only evidence was never treated as a complete paper.
- PDF pages covering title, benchmark construction, Tables 3-6, limitations, safety, and legal notes were visually inspected.
- Exactly three related DEP entries are used, each with a repository locator, concrete overlap, and source basis.
- The `Synthesis Note` contains one concept bridge and exactly three items in each required three-item subsection.
- The three Python mock-ups are designed for synthetic/authorized inputs and will be syntax-checked before submission.
- Public-output scan scope includes Windows/macOS home paths, usernames, local workspace text, timezone labels, exact local timestamps, source extensions, and other private host context.
- Submission allowlist is limited to the generated `.logs`, `.reports`, `.lake-data` Markdown files and the DEP-E publication index.
- No `.source/` directory is created. No PDF, HTML, source archive, cache, extracted paper text, or local verification file may be staged or uploaded.
- Reproduction gap: benchmark code and experiments were not run; no official CLOVER release repository was established.
- Blockers: none for a source-grounded review deposit.

## Attribution Block

- Source URL: https://arxiv.org/abs/2502.08806
  - Applies to: paper identity, authors, date, subjects, DOI, license, and source locators.
  - Notes: Canonical arXiv metadata; abstract alone was not used for empirical claims.
- Source URL: https://arxiv.org/pdf/2502.08806
  - Applies to: benchmark method, tables, figures, results, limitations, safety, and appendices.
  - Notes: Public equivalent of the verified local PDF; not redistributed.
- Source URL: https://arxiv.org/html/2502.08806
  - Applies to: searchable full-paper evidence and table/section cross-checking.
  - Notes: Verified full document; not the metadata-only abstract page.
- Source URL: https://arxiv.org/e-print/2502.08806
  - Applies to: TeX tables, prompts, bibliography, and paper-source structure.
  - Notes: Source package inspected locally and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2502.08806
  - Applies to: persistent paper identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://openreview.net/forum?id=gPpQa4PGEZ
  - Applies to: DL4C @ ICLR 2025 venue context, dates, track, and hosted license.
  - Notes: Official venue record; not an independent reproduction.
- Source URL: https://jiacheng-xu.github.io/
  - Applies to: author-maintained publication context.
  - Notes: No empirical result imported from the page.
- Source URL: https://huggingface.co/papers/2502.08806
  - Applies to: discovery-only release cross-check.
  - Notes: No linked model or dataset was observed at access time.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository layout, attribution, naming, source locality, and submission rules.
  - Notes: Fetched live before drafting.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E container and publication-index rules.
  - Notes: Fetched live before drafting.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related-repository dedup authority.
  - Notes: Fetched live before reliance.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md
  - Applies to: Smart Coverage Goals related DEP bridge.
  - Notes: Coverage-objective selection and test-generation relevance.
- Source URL: https://arxiv.org/abs/2208.04096
  - Applies to: source basis named by the Smart Coverage Goals DEP.
  - Notes: Related-entry source locator; not re-reviewed in full here.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-TACO%20Terminal%20Context/2604.19572-whitepaper-review.md
  - Applies to: TACO related DEP bridge.
  - Notes: Long-observation filtering and software-engineering evaluation relevance.
- Source URL: https://arxiv.org/abs/2604.19572v3
  - Applies to: primary source named by the TACO DEP.
  - Notes: Related-entry source basis.
- Source URL: https://github.com/multimodal-art-projection/TACO
  - Applies to: official implementation context named by the TACO DEP.
  - Notes: Not executed in this review.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-ContextWeaver%20Selective%20a/2604.23069-whitepaper-review.md
  - Applies to: ContextWeaver related DEP bridge.
  - Notes: Dependency-aware memory and validation-lineage relevance.
- Source URL: https://arxiv.org/abs/2604.23069v1
  - Applies to: primary source named by the ContextWeaver DEP.
  - Notes: Related-entry source basis.
