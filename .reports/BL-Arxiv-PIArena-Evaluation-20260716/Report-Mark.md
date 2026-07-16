# Report-Mark: PIArena Evaluation

## Review Status

- Review date: 2026-07-16
- Primary source: arXiv:2604.08499v1
- Source state: initial partial archive unit repaired to verified complete before review
- Evidence depth: complete PDF and official full-paper HTML, canonical metadata, official code documentation, and three related DEP artifacts
- Reproduction state: no experiments, APIs, datasets, or code executed
- Distribution: all source documents and extraction products withheld locally

## Source Metadata

| Field | Value |
|---|---|
| Title | PIArena: A Platform for Prompt Injection Evaluation |
| Authors | Runpeng Geng; Chenlong Yin; Yanting Wang; Ying Chen; Jinyuan Jia |
| Identifier | arXiv:2604.08499v1 |
| DOI | 10.48550/arXiv.2604.08499 |
| Submitted | 2026-04-09 |
| Subjects | Cryptography and Security; Artificial Intelligence; Computation and Language; Machine Learning |
| Venue note | arXiv comments and official repository say ACL 2026; proceedings not inspected |
| Paper license | CC BY 4.0 on the canonical arXiv record |
| Official code | https://github.com/sleeepeer/PIArena |
| Code license | MIT in official repository metadata |

## Concise Research Notes

PIArena standardizes prompt-injection evaluation through benchmark, attack, defense, and evaluator modules. Each benchmark example separates the target task from the injected task, and the evaluator reports target utility alongside attack success rate (ASR). The appendix totals 1,700 samples over 13 dataset/task variants, covering short and long context, RAG, retrieval, summarization, information extraction, and code generation.

The paper's strongest methodological finding is that adaptive attacks alter defense conclusions. Its strategy attack generates candidates from a strategy library and rewrites them based on whether a defense detects, sanitizes, or ignores the injected prompt. In Table 2, reported average ASR under Strategy is 0.99 without defense, 0.86 for PISanitizer, 0.58 for DataFilter, 0.92 for PromptArmor, 0.92 for PromptGuard, and 0.79 for PIGuard. SecAlign++ reports 0.21 ASR but also lowers clean average utility from 0.74 without defense to 0.58.

The paper also tests task-aligned knowledge corruption. When misleading content serves the same nominal task as the user's question, the injected behavior may contain no explicit malicious instruction. Table 4 reports high ASR for most tested defenses and shows that a very aggressive detector can suppress both attacks and clean utility. This supports a move from instruction-only filtering toward provenance, corroboration, and system-level action controls.

Measurement remains a central limitation. ASR and some utility decisions come from a Qwen3-4B-Instruct judge. The authors report 98% accuracy on 100 manually inspected samples, but the tables do not propagate judge uncertainty. Utility definitions also vary across datasets, and detection defenses lack attack-time utility because rejected inputs produce no answer.

## Evidence and Attribution

| ID | Evidence | Supports | Status | Caveat |
|---|---|---|---|---|
| R1 | Canonical arXiv record and v1 full text | Identity, threat model, architecture, findings, limitations | Inspected | Author-reported preprint |
| R2 | Tables 2-4 | Defense transfer, adaptive attack, backend models, task alignment | Inspected | Not reproduced; heterogeneous metrics |
| R3 | Tables 5-10 and appendices | Agent/general portability, optimization/search comparisons, dataset counts, judge and attack costs | Inspected | Configuration- and abstraction-dependent |
| R4 | Official GitHub README and repository metadata | Declared implementation, supported modules, MIT license, dataset/leaderboard links | Inspected | No install, dependency audit, or execution |
| R5 | Three related Black Lake manuscripts | Injection surfaces, trace forensics, evaluator uncertainty | Inspected | Conceptual synthesis only |
| R6 | Public-safe process records | Random draw, dedup, source repair, cache extraction | Validated | Operational rather than scientific evidence |

## Problem, Method, Evidence, and Limitations

### Problem

Defense papers are commonly evaluated on different datasets, injected tasks, attacks, backend models, metrics, and integration harnesses. A high score in one setup therefore says little about transfer. PIArena aims to provide a unified surface that lets researchers plug in new datasets, attacks, defenses, and evaluators and compare them across broader conditions.

### Method

The platform standardizes a record with target instruction, context, injected task, reference answers, and category. Attack modules create contaminated context; defense modules detect, sanitize, filter, or robustly process it; evaluator modules score target completion and injected-task success. The strategy attack uses black-box feedback to select and mutate prompts under bounded iterations.

### Evidence

Table 2 is the central matrix. It shows large dataset-by-defense variation and a general increase in ASR under the Strategy attack. Table 3 shows that ten open and closed backend models remain vulnerable in the tested Direct setup, though ASR ranges widely. Table 4 shows that knowledge corruption is difficult for instruction-level controls. Tables 5 and 6 demonstrate adapters for agentic and general prompt-injection benchmarks. Tables 7 and 10 compare GCG, PAIR, TAP, and Strategy under selected settings.

### Limitations

The benchmark does not establish worst-case robustness. Attack strength depends on its generator, strategy pool, search budget, and success judge. Model and defense versions will drift. Cross-dataset averages combine different utility metrics. A small manual judge audit cannot characterize every class of evaluator error. Agentic evaluation sometimes measures an intermediate response rather than end-to-end action. Code availability improves auditability but is not equivalent to reproduction.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md`
   - Relevance: treats tool descriptions and source metadata as distributed prompt-injection surfaces and argues for process-grounded agent evaluation.
   - Source basis: inspected the artifact's agent-security and evaluation sections.
2. `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md`
   - Relevance: separates memory-channel compromise from inline prompt injection and makes ordered tool traces the forensic object.
   - Source basis: inspected the artifact's threat model, observations, and limitations.
3. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`
   - Relevance: converts rating-judge logits into calibrated intervals, directly addressing false precision in PIArena-style judge outputs.
   - Source basis: inspected its evidence ledger, conformal method, and evaluation cautions.

## Synthesis Note

### Concept Bridge

PIArena supplies the adversarial experiment plane; Agent Systems Review expands the input plane to tool descriptions and multi-source metadata; Agent Memory Forensics supplies a trace plane that identifies how contaminated information moved into action; Judge Conformal supplies a measurement plane that represents evaluator uncertainty. Combined, they suggest that prompt-injection safety should be assessed as a pipeline:

`untrusted source -> context/tool/memory channel -> model/defense decision -> tool or state transition -> uncertain evaluator outcome`.

A defense score is decision-useful only when the source channel, tested attack budget, action stage, utility denominator, and evaluator uncertainty are all preserved.

### Potential Implementations

1. **Versioned adversarial-run ledger** - Store a public-safe manifest for each authorized test containing model, defense, dataset, attack budget, evaluator, seed, outcome stage, utility, ASR, and uncertainty.
2. **Channel-aware injection adapter** - Represent inline context, RAG document, tool description, durable memory, and message sources as separate benchmark channels with shared downstream metrics.
3. **Calibrated decision router** - Route low-confidence judge labels or defense/evaluator disagreements to human review instead of forcing a benchmark pass/fail.

### Deeper Relationship Observations

1. **Attack diversity and source diversity are the same systems problem at different layers.** PIArena varies injected tasks and prompt strategies; Agent Systems Review varies malicious tool metadata. Both test whether a control generalizes when adversarial content changes form or location.
2. **A response-only metric cannot locate compromise.** Agent Memory Forensics shows that ordered retrieval and tool traces can distinguish channels even when final text looks similar; PIArena's ASR can label outcome but not necessarily causal path.
3. **Evaluator uncertainty can reorder security decisions.** When defense scores are close or labels ambiguous, Judge Conformal's interval perspective implies that a single binary judge output should not be treated as exact evidence.

### Conceptual Similarities

1. All four artifacts reject single-number success as sufficient: they require cross-task tests, trace structure, or uncertainty.
2. All four depend on explicit interfaces—benchmark modules, tool schemas, memory operations, or rating labels—to make evidence observable.
3. All four separate useful behavior from risk control, whether expressed as utility/ASR, normal/malicious trace, or point score/interval.

### MVP Implementations with Code Mock-ups

1. **Run-manifest validator**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class RunManifest:
    dataset: str
    attack: str
    defense: str
    evaluator: str
    seed: int
    authorized: bool

def validate_manifest(run: RunManifest) -> None:
    if not run.authorized:
        raise PermissionError("authorized evaluation only")
    if not all((run.dataset, run.attack, run.defense, run.evaluator)):
        raise ValueError("incomplete provenance")
```

This defensive mock-up records required provenance and refuses unauthorized tests. A production form should also pin revisions, budgets, hashes, and retention policy.

2. **Compromise-stage ledger**

```python
ALLOWED_STAGES = {"exposure", "response", "tool_request", "policy_block", "state_change"}

def record_stage(events: list[dict], stage: str, evidence_id: str) -> list[dict]:
    if stage not in ALLOWED_STAGES or not evidence_id:
        raise ValueError("invalid stage evidence")
    return [*events, {"stage": stage, "evidence_id": evidence_id}]
```

The ledger stores identifiers rather than sensitive prompt contents. It makes intermediate agent outcomes comparable without authorizing tool execution.

3. **Uncertain-label router**

```python
def route_label(probability: float, lower: float, upper: float) -> str:
    if not 0.0 <= lower <= probability <= upper <= 1.0:
        raise ValueError("invalid calibrated interval")
    if lower >= 0.8:
        return "likely_success"
    if upper <= 0.2:
        return "likely_failure"
    return "human_review"
```

This mock-up converts interval evidence into abstention-aware routing. Thresholds must be calibrated on held-out, representative labels.

### Developer Challenges

1. Pinning rapidly changing models, defenses, datasets, and evaluators while keeping result manifests portable and rerunnable.
2. Normalizing agentic outcome stages without flattening meaningful differences between static text, tool requests, state mutations, and terminal harm.
3. Preserving enough trace evidence for causal review while minimizing secrets, prompt content, personal data, and harmful payload retention.

### Author Challenges

1. Demonstrate ranking stability under multiple evaluators, human labels, repeated sampling, and uncertainty-aware aggregation.
2. Compare adaptive attacks using pre-registered, budget-matched, held-out strategies and attacker models.
3. Evaluate provenance, corroboration, least privilege, and confirmation controls for task-aligned disinformation rather than stopping at instruction detectors.

## Validation Notes

- Full-paper gate passed before synthesis: valid PDF header/trailer and official full-paper HTML above all size, body, document, heading, and structure thresholds.
- Initial source classification was partial; the local archive was repaired once with official arXiv HTML and metadata. Zero partial files remained.
- Extraction cache was initially absent and backfilled in `missing-only` mode. PDF and HTML extraction succeeded; no source package was collected.
- Uniform selection used index 1,108 of 75,776 unique parent units; the first draw was accepted.
- Dedup checked identifiers, title, slug, repository artifacts, index, automation memory, active repository checkouts, companion repository, and 24-hour markers. One metadata-only inventory row was not a prior review.
- Manuscript title/H1, required sections, exact enumerations, Python syntax, JSON uniqueness, publication counts, public safety, and staged allowlist are validated before submission.
- No PDF, HTML, cache, source archive, extracted source text, local archive path, or `.source/` directory is included in the public deposit.

## Attribution Block

- Primary arXiv record: https://arxiv.org/abs/2604.08499v1
  - Use: metadata, abstract, DOI, subject, version, comments, and license.
- Complete PDF: https://arxiv.org/pdf/2604.08499
  - Use: full method, results, tables, appendix, and limitations; local file withheld.
- Official full-paper HTML: https://arxiv.org/html/2604.08499
  - Use: full-paper validation and evidence cross-check; local file withheld.
- DOI: https://doi.org/10.48550/arXiv.2604.08499
  - Use: persistent identifier.
- Official implementation: https://github.com/sleeepeer/PIArena
  - Use: implementation availability, interface documentation, dataset/leaderboard links, and MIT license; not executed.
- Related DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Tech%20Intel%20Review/tech-intel-agent-systems-review.md
  - Use: distributed injection surface and agent-evaluation bridge.
- Related DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics/memory-forensics.md
  - Use: channel-specific trace and observability bridge.
- Related DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md
  - Use: evaluator-uncertainty bridge.
