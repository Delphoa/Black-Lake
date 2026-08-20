---
title: "CogEvo-Edu - DEP-E"
generated_at: "2026-07-14"
artifact_type: "DEP research artifact"
primary_subject: "CogEvo-Edu's coupled student-memory, knowledge-lifecycle, and multi-agent teaching-control architecture."
source_status: "Verified complete local source set; source files withheld and public URLs deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-14"
temporal_cutoff: "2026-07-14"
primary_url: "https://arxiv.org/abs/2512.00331"
stable_identifier: "arXiv:2512.00331v1"
confidence_summary: "Medium-high for reporting the paper; low for independent efficacy because the benchmark and implementation were not reproduced."
safety_scope: "Educational research, privacy-aware agent memory, defensive monitoring, and bounded implementation design"
distribution_notes: "No PDF, HTML, source package, extracted text, cache, local path, machine identifier, or exact local execution time is redistributed."
---

# CogEvo-Edu - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *CogEvo-Edu: Cognitive Evolution Educational Multi-Agent Collaborative System* | Primary research artifact | Verified PDF and full-paper HTML | arXiv:2512.00331v1 | https://arxiv.org/abs/2512.00331 | arXiv nonexclusive distribution license is exposed in the paper metadata; source files remain local | 2026-07-14 | Complete source paper inspected |
| S2 | arXiv experimental HTML | Primary full text | HTML | arXiv:2512.00331v1 | https://arxiv.org/html/2512.00331 | Used for body sections, equations, benchmark design, and Table I | 2026-07-14 | Inspected and integrity-verified |
| S3 | arXiv PDF | Primary full text | PDF | arXiv:2512.00331v1 | https://arxiv.org/pdf/2512.00331 | Verified locally; not deposited | 2026-07-14 | Inspected and integrity-verified |
| S4 | arXiv TeX/source package | Primary source representation | Source archive | arXiv:2512.00331v1 | https://arxiv.org/e-print/2512.00331 | Used to cross-check extracted text and table values; not deposited | 2026-07-14 | Inspected through local extraction |
| S5 | Related publication DOI | Publication locator | DOI record | DOI:10.1109/CSCWD68734.2026.11582082 | https://doi.org/10.1109/CSCWD68734.2026.11582082 | Listed by the canonical arXiv record; not treated as an independent paper version | 2026-07-14 | Locator verified through arXiv metadata |
| S6 | Agent State Review | Related DEP-E | Markdown manuscript | DEP-E-20260708-Agent State Review | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | Public repository artifact | 2026-07-14 | Inspected |
| S7 | Memory Forensics | Related DEP-E | Markdown manuscript | DEP-E-20260711-Agent Memory Forensics | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` | Public repository artifact | 2026-07-14 | Inspected |
| S8 | CompressKV Semantic Heads | Related DEP-A | Whitepaper-grade Markdown review | DEP-A-20260714-CompressKV Semantic Heads | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md` | Public repository artifact | 2026-07-14 | Inspected |

Authors: Yefeng Wu, Yuchen Song, Yecheng Zhao, Ling Wu, and Shan Wan. The arXiv record lists Artificial Intelligence and Multiagent Systems as subjects and reports submission on 2025-11-29. No official code or DSP-EduBench release was identified in the inspected paper or canonical arXiv record.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S4 | Primary paper and source representations | Complete paper body, equations, figures, Table I, and conclusion | Architecture, benchmark, scores, and paper-disclosed framing | High for source reporting | No implementation execution or benchmark reproduction |
| E2 | S1, S2 | Canonical metadata and HTML | Title, authors, submission date, subjects, abstract, related DOI | Source identity and high-level contribution | High | Abstract claims alone are not used for empirical validation |
| E3 | S2, Sections III-A through III-C | Primary method | CPL confidence update, KEL value function and lifecycle thresholds, MCL inner/outer control | Mechanism reconstruction | High for described design | Several operational details and optimizer choices are absent |
| E4 | S2, Sections IV-V and Table I | Primary empirical report | DSP-EduBench design, simulated profiles, judge ensemble, five configurations, six scores | Reported comparative evidence | Medium-high for reporting | No sample counts, error bars, judge-agreement statistics, or human validation found |
| E5 | S6 | Related DEP manuscript | Persistent state, evidence replay, and online monitoring synthesis | Governance bridge for CPL/MCL state | Medium | Related synthesis is not evidence that CogEvo-Edu works |
| E6 | S7 | Related DEP manuscript | Explicit-memory threat model and trace-based detection boundary | Defensive bridge for persistent student memory | Medium-high for the related source's scoped claims | Different domain and threat model; not experimentally combined |
| E7 | S8 | Related DEP review | Semantic evidence retention, bounded cache, drift, and recovery analysis | Compression and lifecycle bridge for KEL | High-quality review context | KV-cache control differs from knowledge-base lifecycle control |

## Executive Summary

CogEvo-Edu proposes that long-horizon tutoring should evolve three coupled objects: a structured student profile, a pedagogical knowledge base, and the policy that selects teaching agents and strategies. Its Cognitive Perception Layer consolidates short-term dialogue into confidence-weighted long-term features; its Knowledge Evolution Layer scores chunks by frequency, recency, and semantic density before retaining, compressing, or deleting them; and its Meta-Control Layer routes specialist agents while conceptually adapting memory and knowledge hyperparameters over longer horizons.

The paper evaluates five configurations on DSP-EduBench, a constructed digital-signal-processing tutoring benchmark with heterogeneous materials, simulated learners, and scripted long interactions. A three-model LLM-as-a-Judge ensemble reports an average of 9.23 for CogEvo-Edu versus 5.32 for LLM Only, 5.97 for Static RAG, 6.45 for Simple Memory, and 6.42 for a Single Agent using CPL and KEL without meta-control. The result is a strong internal signal for the coupled architecture, but it is not independent evidence of learning gain: the benchmark, judge prompts, run counts, code, and statistical analysis were not available for reproduction.

The three related DEP entries turn the architecture into a more operational research program. Agent State Review suggests that evolving state should be versioned, replayable, and monitored. Memory Forensics shows why persistent memory needs trace-level safety controls. CompressKV shows how semantic retention can reduce resource use while introducing calibration and irreversible-eviction risks. The synthesis therefore recommends evidence-backed profiles, recoverable knowledge paging, and trace-aware meta-control before destructive forgetting or autonomous controller updates.

## Detailed Summary

### Problem and Context

Static RAG tutors typically query a fixed vector store with a fixed top-k and let one LLM diagnose, explain, question, and retrieve. The paper argues that this design does not preserve a coherent student model over long conversations, accumulates redundant retrieved context, and cannot systematically adapt the choice of teaching strategy or specialist. DSP is selected because it requires movement among theory, mathematical derivation, intuition, and MATLAB/Python-style implementation.

### Cognitive Perception Layer

CPL separates recent raw question-answer pairs from structured long-term student features. Each long-term feature contains a key, value, and confidence weight. When short-term memory saturates, an LLM extracts candidate features and a semantic-consistency rule compares them with prior features. Agreement raises confidence by `eta * (1 - confidence)`; contradiction lowers it by `eta * confidence`. This is an interpretable update form, but the paper does not fully specify contradiction classification, identity resolution, evidence retention, privacy boundaries, or error recovery.

### Knowledge Evolution Layer

KEL assigns each chunk a weighted value from normalized retrieval/adoption frequency, exponential recency decay, and average cosine similarity to nearest neighbors as a semantic-density proxy. Two thresholds split the store into active chunks, compressed summaries, and deleted chunks. The design directly addresses retrieval piling and storage growth. Its sharp boundary is epistemic: a low score may reflect sparse use or a niche learner need rather than low future value, and physical deletion removes the evidence needed to correct a bad estimate.

### Meta-Control Layer

MCL observes the student profile, the active knowledge subset, and the current task. Its action includes a leading agent role, teaching strategy, difficulty, and retrieval configuration. The paper describes an inner policy for per-turn actions and an outer objective that periodically updates policy parameters plus CPL/KEL hyperparameters using mastery improvement, error-pattern extinction, and retention. The formulation is conceptually coherent, but the full paper does not give enough optimizer, schedule, reward, or governance detail to reproduce the outer loop.

### Benchmark and Evaluation

DSP-EduBench combines heterogeneous DSP sources with simulated profiles representing novice, misconception-prone, and advanced engineering learners. Long-range scripts include conceptual discrimination, fault diagnosis, and code debugging. Ground truth includes correct solutions, key-point checklists, and an ideal pedagogical strategy.

All instructional configurations use Qwen3-14B. GLM-4.5, DeepSeek-V3.1, and Qwen3-max independently score each turn from 1 to 10 on factual correctness, contextual relevance, memory consistency, personalization alignment, knowledge guidance, and strategy flexibility. The reported scores are:

| Configuration | Factual | Contextual | Memory | Personalization | Guidance | Flexibility | Average |
|---|---:|---:|---:|---:|---:|---:|---:|
| LLM Only | 5.8 | 6.5 | 4.2 | 4.8 | 5.5 | 5.1 | 5.32 |
| Static RAG | 8.4 | 6.9 | 4.5 | 5.0 | 5.8 | 5.2 | 5.97 |
| Simple Memory | 6.1 | 6.7 | 7.6 | 6.8 | 6.0 | 5.5 | 6.45 |
| Single Agent | 7.9 | 7.5 | 6.2 | 5.8 | 6.2 | 4.9 | 6.42 |
| CogEvo-Edu | 9.3 | 9.1 | 9.5 | 9.2 | 8.9 | 9.4 | 9.23 |

### Interpretation

Static RAG mainly improves factual correctness, Simple Memory mainly improves memory consistency, and the Single Agent remains weak in strategy flexibility. The full system improves all reported dimensions. Because the configurations change multiple mechanisms and the full system is judged only inside the constructed benchmark, the evidence supports the value of testing coupled evolution more strongly than it proves that the proposed coupling caused every gain or will transfer to real learners.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Retrieval, memory, and teaching control should be optimized as a coupled cognitive-evolution process. | Author thesis | E1, E3, E4 | Architecturally coherent and supported by favorable bundled comparisons; causal separation remains incomplete. | Medium |
| C2 | CPL can maintain a structured, self-correcting learner profile under finite context. | Author method claim | E3 | The update rule is specified, but self-correction quality, contradiction errors, and privacy were not independently evaluated. | Medium |
| C3 | KEL uses frequency, time decay, and semantic density to control activation, compression, and forgetting. | Direct method description | E3 | Clearly present in the source. The paper's statement of a theoretically optimal storage-coverage balance is not established by a proof or exhaustive experiment. | High for mechanism; low for optimality |
| C4 | CogEvo-Edu raises the DSP-EduBench average from 5.32 to 9.23. | Author empirical result | E4 | Table I supports the reported result for the paper's evaluation; no independent reproduction or uncertainty estimate exists here. | Medium-high for reporting |
| C5 | The full system improves all six reported indicators over the four baselines. | Author empirical result | E4 | Numerically supported by Table I; judge calibration and sample-level variability are unknown. | Medium-high for reporting |
| C6 | Evolving student memory should carry evidence and forensic traces. | Reviewer interpretation | E5, E6 | Strong operational implication when persistent memory influences consequential agent actions. | Medium |
| C7 | KEL deletion should be replaced by recoverable paging until false-forgetting risk is measured. | Reviewer recommendation | E3, E7 | Not tested by the paper, but directly addresses calibration drift and irreversible loss. | Medium |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E manuscript on one randomly selected eligible arXiv paper and synthesize it with exactly three related Black Lake DEP entries.
- `Sources inspected`: Verified local PDF, official full-paper HTML, metadata HTML, TeX/source extraction, canonical arXiv record, the related DOI locator, live Black Lake README and `.lake-data/README.md`, live Black-Lake-Data README, and the three related DEP manuscripts and READMEs.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, normalized unique parent-directory paper units, and used a uniform `Get-Random` index. Repository paths and automation memory were searched by arXiv ID, exact title, and slug before acceptance.
- `Random selection record`: 75,774 PDF candidates and 75,774 unique paper units; zero-based index 56,651; excluded candidates 0; duplicate reselections 0.
- `Eligibility record`: No prior Black Lake Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, memory record, or Black-Lake-Data match was found for arXiv:2512.00331 or the normalized title. The public 24-hour cutoff date was 2026-07-13.
- `Integrity process`: The selected unit was initially partial because full-paper HTML was absent. The valid PDF was preserved; official full-paper HTML, metadata HTML, and source package were collected locally with bounded attempts. PDF and HTML integrity checks passed before review.
- `Extraction process`: Local-only extraction used the verified HTML, PDF, and source package. The PDF extractor fell back to `pypdf`; HTML and source extraction both succeeded. Extracted text and caches remain local.
- `Inclusion criteria`: Direct paper sections, equations, Table I, source metadata, paper-stated limitations, and related DEP entries with concrete overlap in state, memory safety, or semantic compression.
- `Exclusion criteria`: Abstract-only synthesis, unrelated DEP entries, unverified code or dataset claims, source-file deposition, and claims that require experiment reproduction.
- `Analytical approach`: Empirical reporting, conceptual mechanism review, comparative architecture analysis, implementation translation, privacy/safety review, and DEP provenance synthesis.
- `Evidence handling`: Author claims, exact table values, reviewer interpretations, and recommendations are labeled separately and mapped to evidence IDs.
- `Uncertainty handling`: Missing sample counts, code, benchmark release, statistical analysis, human evaluation, and outer-loop details are kept visible rather than inferred.
- `Reviewer stance`: Skeptical source preservation plus bounded product and evaluation translation.

## Scope, Constraints, and Assumptions

- `Scope`: One full-paper review of CogEvo-Edu plus synthesis with exactly three Black Lake DEP entries.
- `Temporal boundary`: Primary paper version 2512.00331v1; sources accessed on 2026-07-14.
- `Evidence limits`: No code repository or benchmark release was identified, no experiments were rerun, no judge prompts were inspected, and no human-learning study was available.
- `Assumptions`: The verified arXiv PDF, HTML, and source package represent the same v1 work. Table I values are reported exactly as the source presents them.
- `Constraints`: No source files, extracted text, caches, local paths, credentials, private learner data, or execution identifiers are redistributed.
- `Out of scope`: Clinical or classroom deployment, collection of real student data, production deletion of knowledge, autonomous policy updating, and claims of causal or educational effectiveness beyond the inspected evidence.
- `Intended use`: DEP deposition, research review, architecture critique, evaluation planning, and privacy-aware prototype design.
- `Audience`: Educational-AI researchers, agent-platform engineers, memory-system designers, safety reviewers, and Black Lake curators.
- `Reproducibility boundary`: The architecture and table can be inspected, but independent reproduction needs DSP-EduBench, prompts, configurations, run counts, and implementation artifacts not available here.
- `Data sensitivity`: Public paper and repository artifacts only; any future learner data must be treated as sensitive educational data.

## Observations

- `Observed pattern`: The largest reported improvements appear only when memory, knowledge lifecycle, and agent orchestration are combined.
- `Technical implication`: CPL, KEL, and MCL should share a typed state contract so routing decisions can be traced to a specific profile and knowledge snapshot.
- `Contradiction or tension`: The paper calls the student profile self-correcting, while KEL physically deletes low-valued knowledge; correction requires recoverable evidence, so destructive forgetting works against auditability.
- `Evaluation implication`: A three-model judge ensemble reduces dependence on one judge but does not establish agreement, calibration, or correspondence with human learning.
- `Reviewer hypothesis`: Much of the benefit may come from explicit role and state decomposition rather than from the precise confidence and value formulas; a factorial ablation could test that.

## Considerations

Student profiles can encode ability, preferences, and persistent mistakes, so implementations need consent, minimization, retention limits, access control, correction rights, and separation between pedagogical state and identity. Confidence values should not be interpreted as psychological truth.

KEL's value function rewards use and neighborhood similarity. That can suppress rare prerequisites, minority learning paths, or contradictory evidence. Cold storage, protected curriculum anchors, diversity constraints, and recovery tests are safer than physical deletion in early systems.

MCL's outer loop changes the controller that governs both memory and forgetting. Updates need versioning, offline evaluation, canaries, rollback, and approval gates. Judge feedback can become a self-reinforcing objective if the same model families shape both benchmark and policy.

The paper reports response-quality scores, not longitudinal mastery, retention, transfer, motivation, equity, or instructor workload. Deployment decisions need human-centered outcomes and failure reviews rather than a single composite score.

## Strengths

- The paper organizes a difficult systems problem into three responsibilities with explicit state flow between them.
- CPL's confidence update and KEL's value function are compact enough to inspect and challenge.
- DSP-EduBench attempts to test long-horizon personalization rather than only isolated question answering.
- Baselines expose distinct weaknesses of static retrieval, unstructured memory, and fixed single-agent control.
- The full source paper is concise, internally consistent, and includes exact comparative table values.

## Weaknesses

- DSP-EduBench, code, configurations, and judge prompts were not identified as released artifacts.
- Sample counts, variance, statistical tests, inter-judge agreement, and human validation are absent from the inspected paper.
- Simulated profiles and LLM judges may reward benchmark-conforming pedagogy without measuring durable learning.
- The comparison is not a full factorial ablation, so component attribution is uncertain.
- The outer-loop optimization is described more completely as an objective than as a reproducible algorithm.
- Physical deletion in KEL lacks a recovery, protected-evidence, or false-forgetting evaluation.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release DSP-EduBench, prompts, configurations, seeds, and scoring code | Reproducibility | Table I cannot be independently recreated | Verifiable comparisons and external baselines | License and maintenance burden | Reproduce every table row from a pinned environment |
| Add human educators and learner outcomes | External validity | LLM judge scores are not learning gains | Evidence about mastery, retention, and usefulness | Higher cost and privacy review | Pre/post tests, delayed retention, blinded rubric scoring |
| Run a factorial CPL/KEL/MCL ablation | Causal attribution | Current configurations change multiple mechanisms | Identifies which interactions drive the gain | Larger experiment matrix | Fixed backbone, retrieval budget, data, and judge protocol |
| Replace deletion with recoverable paging | Knowledge safety | Value estimates can be wrong or drift | Reduces false forgetting and enables audits | Additional storage and recovery latency | Measure restoration rate, miss cost, and tail quality |
| Add evidence IDs and trace schemas | State governance | Confidence without lineage is hard to correct | Explainable updates and forensic review | Metadata/privacy overhead | Trace-completeness tests and minimization audits |
| Calibrate and publish judge agreement | Evaluation quality | Averaging three judges can hide systematic bias | Interpretable uncertainty and disagreement | More annotations | Human reference set, agreement metrics, calibration curves |

## Potential Implementations

1. **Evidence-backed learner model**
   - `User`: Tutor platform engineer and educator.
   - `Goal`: Preserve long-term learning state without turning summaries into unauditable facts.
   - `Core mechanism`: Store each feature with confidence, supporting event IDs, contradictions, policy version, and expiry.
   - `Required inputs`: Consent-governed interaction events, curriculum skill graph, and teacher corrections.
   - `Outputs`: Minimal profile view, confidence history, and correction queue.
   - `Risk controls`: Data minimization, role-based access, correction rights, encryption, and retention limits.
   - `Evaluation`: Trace completeness, false-profile rate, teacher agreement, and deletion compliance.
2. **Recoverable knowledge lifecycle service**
   - `User`: RAG and curriculum maintainers.
   - `Goal`: Control context and storage while protecting rare or future-use evidence.
   - `Core mechanism`: Combine KEL values with protected anchors and move low-value chunks to versioned cold pages before deletion.
   - `Required inputs`: Retrieval/adoption counts, access age, semantic graph, provenance, and curriculum protections.
   - `Outputs`: Active, compressed, and cold tiers plus restoration metrics.
   - `Risk controls`: No destructive deletion during MVP, signed provenance, recovery tests, and drift alarms.
   - `Evaluation`: Quality at equal token/storage budgets, tail retrieval, restoration success, and false-forgetting cost.
3. **Auditable multi-agent teaching controller**
   - `User`: Educational-AI operations team.
   - `Goal`: Route specialist agents while keeping every decision reviewable.
   - `Core mechanism`: Versioned policy selects role, strategy, difficulty, and retrieval; a trace ledger records inputs and consequential transitions.
   - `Required inputs`: Minimal learner state, active knowledge snapshot, task, policy version, and judge feedback.
   - `Outputs`: Teaching action, rationale record, trace ID, and review flag.
   - `Risk controls`: Offline policy updates, canaries, rollback, privacy-minimized events, and human override.
   - `Evaluation`: Learning outcomes, strategy-switch precision, trace coverage, false alerts, and policy-regression tests.

## Three Ways to Exercise This Research

1. `Reproduce the comparison table`: Objective: determine whether Table I is recoverable. Inputs: released or author-provided DSP-EduBench, prompts, configurations, and judge rubric. Method: pin models and seeds, run all five configurations, publish sample counts and judge agreement. Output: a reproduction table with uncertainty. Success criterion: every reported score is reproduced or explained. Stop condition: stop if the benchmark or license cannot be verified.
2. `Test evidence-backed profile correction`: Objective: measure whether CPL corrects stale beliefs. Inputs: synthetic consent-safe learner traces with reinforcement, contradiction, and identity-drift cases. Method: compare confidence-only updates with evidence-linked updates. Output: correction accuracy and trace-completeness report. Success criterion: contradictions are resolved without losing provenance. Stop condition: stop if raw sensitive data is required.
3. `Measure recoverable forgetting`: Objective: compare KEL deletion against cold paging. Inputs: public toy curriculum, retrieval traces, and rare-need queries. Method: apply both lifecycle policies at equal active-storage budgets. Output: quality, tail-miss, recovery, latency, and storage curves. Success criterion: a policy meets a declared quality floor with auditable restoration. Stop condition: stop destructive tests if the only source copy is at risk.

## Example MVP Product

- `Product name`: Cognitive Tutor State Lab
- `Target user`: Educational-AI research and platform teams evaluating long-horizon tutors.
- `Problem`: Teams need to test evolving student state, knowledge lifecycle, and agent routing without exposing real learner data or enabling irreversible forgetting.
- `Core workflow`: Load synthetic learner scripts and a public toy curriculum; run evidence-backed profile updates; tier knowledge into active, compressed, and cold states; route specialist agents; inspect trace and judge dashboards; compare against static RAG and simple memory.
- `Data requirements`: Synthetic profiles, public curriculum chunks, answer and pedagogy rubrics, versioned model outputs, and privacy-safe event metadata.
- `Architecture`: Local evaluation runner, typed profile ledger, recoverable knowledge pager, policy router, multi-judge adapter, and immutable public-safe result report.
- `Success metrics`: Profile correction accuracy, evidence trace coverage, retrieval quality at fixed budget, cold-page recovery rate, human-rubric agreement, strategy-switch precision, and zero source/privacy leaks.
- `Risk controls`: Synthetic-only default, no destructive deletion, offline outer-loop updates, human override, minimized logs, version pinning, sanitization scans, and no production claims.
- `Limitations`: The MVP cannot establish real learning gains, fairness, classroom usability, or safe production autonomy. Model and judge access may also make exact reproduction difficult.
- `MVP boundary`: No real student data, no autonomous curriculum changes, no production tool actions, and no physical source deletion.
- `Deployment model`: Local CLI plus a review dashboard in an authorized research environment.
- `Evaluation plan`: Unit tests for profile and lifecycle rules, golden trace cases, ablations, human rubric spot checks, and public-output sanitization.
- `Failure modes`: False confidence, profile identity drift, protected-knowledge eviction, judge bias, incomplete traces, and policy feedback loops.
- `Maintenance plan`: Version models, judges, prompts, schemas, policies, and calibration sets; rerun drift checks before accepting updates.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| Agent State Review | Black Lake DEP-E | Adds replayable evidence, persistent-state monitoring, and state-as-review-object concepts to CPL/MCL. | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` |
| Memory Forensics | Black Lake DEP-E | Adds a scoped persistent-memory threat model and privacy-minimized trace monitoring to the student-memory layer. | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` |
| CompressKV Semantic Heads | Black Lake DEP-A | Adds semantic-retention calibration, bounded-resource comparison, drift, and recovery questions to KEL compression. | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2512.00331 | Canonical title, authors, identifier, subjects, submission date, abstract, PDF/HTML/source links, and related DOI | 2026-07-14 | Primary metadata record inspected online and locally archived as metadata only |
| R2 | https://arxiv.org/html/2512.00331 | Complete paper method, benchmark, Table I, results, and conclusion | 2026-07-14 | Full-paper HTML integrity verified; source file withheld |
| R3 | https://arxiv.org/pdf/2512.00331 | Complete primary paper | 2026-07-14 | PDF integrity verified; source file withheld |
| R4 | https://arxiv.org/e-print/2512.00331 | TeX/source cross-check | 2026-07-14 | Source package retained locally only |
| R5 | https://doi.org/10.1109/CSCWD68734.2026.11582082 | Related publication locator | 2026-07-14 | DOI is linked from arXiv; no separate version comparison performed |
| R6 | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/README.md` | Related DEP scope and provenance | 2026-07-14 | Repository file inspected |
| R7 | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | Evidence replay, persistent state, runtime monitoring, and state governance | 2026-07-14 | Related processed artifact, not validation of CogEvo-Edu |
| R8 | https://arxiv.org/abs/2607.02509 | ReContext source basis recorded by Agent State Review | 2026-07-14 | Used through the inspected related DEP's source-grounded synthesis |
| R9 | https://arxiv.org/abs/2607.02510 | Online monitoring source basis recorded by Agent State Review | 2026-07-14 | Used through the inspected related DEP's source-grounded synthesis |
| R10 | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/README.md` | Related DEP scope and provenance | 2026-07-14 | Repository file inspected |
| R11 | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` | Persistent-memory trajectory detection and limits | 2026-07-14 | Related processed artifact |
| R12 | https://arxiv.org/abs/2606.30566 | Primary source basis recorded by Memory Forensics | 2026-07-14 | Used through the inspected related DEP's review |
| R13 | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/README.md` | Related DEP scope and provenance | 2026-07-14 | Repository file inspected |
| R14 | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md` | Semantic retention, compression evidence, calibration, and recovery analysis | 2026-07-14 | Related processed artifact |
| R15 | https://arxiv.org/abs/2606.24467 | Primary source basis recorded by the CompressKV review | 2026-07-14 | Used through the inspected related DEP's full-paper review |
| R16 | `README.md` and `.lake-data/README.md` | Current Black Lake DEP class, filing, inventory, index, source-withholding, and commit rules | 2026-07-14 | Repository policy, not research evidence |

## Appendix

### Random Selection and Dedup Record

- Method: `rg --files -g "*.pdf"` over the local archive, unique parent-directory units, uniform PowerShell `Get-Random` draw.
- PDF candidates: 75,774.
- Unique paper units: 75,774.
- Selected zero-based index: 56,651.
- Selected paper: arXiv:2512.00331, *CogEvo-Edu: Cognitive Evolution Educational Multi-Agent Collaborative System*.
- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data `.lake-data`, `.reports`, and `.staging`.
- Match keys: arXiv ID, exact title, normalized title, and CogEvo-Edu slug.
- Exclusions: 0.
- Reselections: 0.
- Public 24-hour cutoff: 2026-07-13 at date granularity; exact local run time withheld.

### Local Source Integrity

- Initial state: partial because the PDF existed but full-paper HTML was missing.
- Repair: preserved the valid PDF; collected official full-paper HTML, metadata HTML, and TeX/source package locally.
- PDF: 12,429,300 bytes; `%PDF-` header; trailing `%%EOF`; pass.
- Full-paper HTML: 85,764 bytes; 32,899 body characters; document marker present; 40 section/heading markers; five structure terms; pass.
- Metadata HTML: present and nonempty.
- Source package: present.
- Extraction: PDF, HTML, and source text extracted successfully into a local-only cache.
- Partials: none.
- Public-source gate: no PDF, HTML, source archive, extracted text, or cache is included in this DEP.

### Validation Checklist

- YAML title and H1 are identical and under 40 characters.
- All required manuscript headings are present in the schema order.
- Source claims, exact reported values, reviewer interpretations, and recommendations are distinguished.
- Every evidence-ledger source is represented in Source References.
- `Three Ways to Exercise This Research` contains exactly three bounded paths.
- `Example MVP Product` contains the required product fields and safety boundaries.
- Exactly three related DEP entries are synthesized.
- Public source files are explicitly withheld and no `.source/` directory exists.
