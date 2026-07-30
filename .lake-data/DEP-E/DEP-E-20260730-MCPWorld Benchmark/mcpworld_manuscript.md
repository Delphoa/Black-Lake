---
title: "MCPWorld - DEP-E"
generated_at: "2026-07-30 (public-safe date)"
artifact_type: "DEP research artifact"
primary_subject: "MCPWorld, a white-box benchmark for GUI, MCP/API, and hybrid computer-use agents."
source_status: "Verified local source files; public deposit contains URLs and derived analysis only."
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-30"
temporal_cutoff: "Paper v1 and public repository state inspected on the listed public-safe date."
primary_url: "https://arxiv.org/abs/2506.07672"
stable_identifier: "arXiv:2506.07672; DOI:10.48550/arXiv.2506.07672"
confidence_summary: "High for source identity, integrity, and reported table transcription; medium for generalization because no experiment was reproduced."
safety_scope: "Defensive evaluation, authorized testbeds, and non-consequential research planning."
distribution_notes: "Source documents, extracted text, provenance records, and receipts remain withheld locally."
---

# MCPWorld - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | MCPWorld arXiv record | Primary metadata | HTML | arXiv:2506.07672v1 | https://arxiv.org/abs/2506.07672 | CC BY 4.0 locator visible on arXiv | 2026-07-30 | Inspected; metadata only for empirical claims |
| S2 | MCPWorld full paper | Primary research artifact | PDF and full-paper HTML | 37-page PDF; arXiv v1 | https://arxiv.org/pdf/2506.07672 and https://arxiv.org/html/2506.07672 | Public source locators; verified copies withheld locally | 2026-07-30 | Inspected in full |
| S3 | SAAgent/MCPWorld | Official implementation | GitHub repository | main branch observed | https://github.com/SAAgent/MCPWorld | MIT license displayed; code not executed | 2026-07-30 | README and repository inventory inspected |
| S4 | Agent State Review | Related Black Lake DEP | Markdown | DEP-E-20260708 | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | Public repository artifact | 2026-07-30 | Inspected for conceptual overlap |
| S5 | Agent Reliability Gates | Related Black Lake DEP | Markdown | DEP-E-20260728 | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` | Public repository artifact | 2026-07-30 | Inspected for conceptual overlap |
| S6 | OMGEval Benchmark | Related Black Lake DEP | Markdown | DEP-E-20260717 | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` | Public repository artifact | 2026-07-30 | Inspected for conceptual overlap |

Paper authors: Yunhe Yan; Shihe Wang; Jiajun Du; Yexuan Yang; Yuxuan Shan; Qichen Qiu; Xianqing Jia; Xinge Wang; Xin Yuan; Xu Han; Mao Qin; Yinxiao Chen; Chen Peng; Shangguang Wang; Mengwei Xu.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Identity, authors, submission date, category, DOI, license locator, and code link | Paper identity and source locators | High | Abstract is not used as the sole evidence for empirical claims |
| E2 | S2 | Primary paper | Framework sections, app/task tables, evaluator mechanisms, experiment setup, result tables, limitations, and appendices | Method and author-reported results | High for transcription | No independent reproduction |
| E3 | S3 | Official repository | MIT license display, containerized platform description, task count wording, setup shape | Availability and version-alignment observation | Medium | Repository was not run; README task count differs from paper |
| E4 | S4 | Related DEP | Persistent state, replayable evidence, and runtime-monitoring synthesis | State-trace implementation bridge | Medium | Separate evidence base; no joint experiment |
| E5 | S5 | Related DEP | Explicit evidence, authorization, verification, and state-publication gates | Reliability-control bridge | Medium | Cross-domain synthesis, not MCPWorld measurement |
| E6 | S6 | Related DEP | Evaluation scope, calibration, versioning, and judge limitations | Measurement-governance bridge | Medium | Multilingual generation differs from computer use |

## Executive Summary

MCPWorld is an author-proposed benchmarking testbed for computer-use agents that can interact through GUI controls, MCP/API tools, or a hybrid of both. Its key contribution is a white-box evaluator: rather than treating a screenshot, action trace, or output file as the only completion oracle, it monitors application-internal signals that correspond to task goals and annotated intermediate key steps [E2].

The paper reports 201 tasks across ten open-source desktop applications. In its Claude 3.7 Sonnet experiment, hybrid access achieved a reported 75.12% task-success rate, above GUI-only at 70.65% and MCP-only at 53.23%; hybrid key-step completion was 69.63% [E2]. These are author-reported, configuration-specific results. They support the narrower conclusion that, in this benchmark and agent setup, combining modalities helped more than either restricted interface alone.

The most transferable idea is evaluator design, not the reported ranking. An auditable benchmark should record task state, expected events, evaluator version, tool surface, and the reasons a run did or did not satisfy a goal. The implementation is publicly available under MIT terms, but the inspected README describes approximately 170 tasks while the paper reports 201, so release-version alignment remains an explicit follow-up question [E3].

## Detailed Summary

### Problem and contribution

The paper argues that computer-use-agent benchmarks have concentrated on GUI interaction and external-state matching. That framing misses application functions exposed through APIs such as MCP and can make completion checks brittle under UI changes. MCPWorld proposes a unified tool-based environment for GUI, MCP, and hybrid agents, using open-source “white-box” applications so evaluators can observe internal state transitions [E2].

### Framework and evaluator

The framework initializes task-specific state in a container, exposes observations and actions through a unified tool space, and sends application events to an evaluator. For different application architectures, the authors use dynamic instrumentation, targeted code injection, or API/log/database state queries. The point is not merely to see a final screen: the evaluator can check a task's definitive internal outcome or intermediate key event, including transient state that might not reach a UI or file [E2].

### Benchmark suite

The paper lists ten open-source applications: Zotero, OBS Studio, Zulip, Joplin, FreeCAD, QGIS, Anki, Visual Studio Code, qBittorrent, and Blender. The benchmark contains 201 tasks: 73 with 0–5 GUI steps, 83 with 5–10, and 45 with more than 10. Designers used task materials from user scenarios and documentation, cross-validated examples, and recorded human executions; they also annotated most tasks with intermediate key steps [E2].

### Evaluation and results

The reported experiment uses the official Claude computer-use demo with `claude-3-7-sonnet-20250219`, a ReAct-style prompting approach, three attempts per task/configuration, and a 300-second limit. GUI-only uses screen capture, mouse/keyboard emulation, and shell commands; MCP-only uses exposed MCP tools; hybrid combines both without an explicit heuristic for tool selection. The reported task-success and key-step-completion rates are:

| Configuration | Task success | Key-step completion |
|---|---:|---:|
| GUI-only | 70.65% | 68.82% |
| MCP-only | 53.23% | 59.78% |
| Hybrid | 75.12% | 69.63% |

The authors attribute MCP-only weakness mainly to limited tool coverage, and report that hybrid performance becomes more helpful on the longest task bucket. This should not be read as proof that MCP tools are intrinsically weaker than GUI interaction: it is evidence that tool completeness, descriptions, and agent planning jointly determine outcomes [E2].

### Limitations and implementation status

The paper acknowledges a single evaluated agent framework, the open-source/white-box restriction, task-annotation effort, and limited cross-application or multi-turn scenarios. The official repository is public, describes Docker-based environments and white-box evaluators, and displays an MIT license. No installation, task execution, dependency audit, or result reproduction was attempted here. The apparent paper/repository task-count discrepancy is retained as a version question rather than resolved by inference [E2, E3].

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | MCPWorld evaluates GUI, MCP/API, and hybrid computer-use agents using application-aware completion checks. | Author method claim | E2 | Directly supported by the framework and evaluator sections. | High |
| C2 | The benchmark contains 201 tasks in ten open-source applications. | Author dataset claim | E2 | Directly supported by Tables 2–3 and the benchmark section. | High |
| C3 | Hybrid access achieved the highest reported task-success rate in the authors' experiment. | Author empirical claim | E2 | Table 4 reports 75.12% hybrid versus 70.65% GUI-only and 53.23% MCP-only. | High for transcription; medium for transfer |
| C4 | Missing MCP coverage is a material explanation for MCP-only failures in the reported setup. | Author analysis claim | E2 | Failure analysis identifies insufficient coverage as the largest MCP-only failure category. | Medium-high |
| C5 | Application-internal event checks can make agent evaluation more robust than surface-only matching. | Reviewer-supported interpretation | E2 | The mechanism supports the claim, but comparative evaluator error rates were not independently measured. | Medium |
| C6 | A durable agent benchmark should version evaluator rules alongside task and model versions. | Reviewer interpretation | E2, E3, E4–E6 | Strong engineering implication; not a direct experiment result. | Medium-high |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E manuscript about MCPWorld's benchmark design, evidence, limitations, and safe implementation relevance.
- `Sources inspected`: Verified local PDF; verified full-paper HTML; arXiv metadata; official implementation README/repository inventory; fetched Black Lake and Black-Lake-Data README rules; and exactly three related Black Lake DEP manuscripts.
- `Discovery strategy`: `rg --files -g "*.pdf"` enumerated 75,959 PDFs in 75,956 unique parent units. A uniform PowerShell `Get-Random` draw selected zero-based unit index 50,457. Adjacent metadata was read, and public arXiv plus official implementation pages were inspected.
- `Inclusion criteria`: Evidence had to identify the paper, describe the framework or experiment, establish public implementation status, verify source integrity, or provide a concrete related-DEP bridge.
- `Exclusion criteria`: Abstract-only material was excluded from empirical support. No unexecuted code, unverified benchmark release claim, private path, source file, cache, or speculative current-model claim was included.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Reported values are labeled as author-reported and traced to the full paper. Reviewer interpretations are separately labeled. The official repository is used for availability/context, not unexecuted performance validation.
- `Uncertainty handling`: The manuscript preserves the single-model evaluation, unmeasured evaluator error rates, release version difference, unexecuted code, and lack of independent reproduction.
- `Random selection`: Selection was uniform over parent units, not title-normalized works; there were zero pre-draw exclusions, zero post-draw duplicate exclusions, and zero reselections.
- `Dedup and recency validation`: Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data entries were searched using the arXiv ID, DOI, normalized title, and `mcpworld` slug. No owning deposit or same-paper marker in the preceding 24-hour review window was found. Black-Lake-Data's matching inventory records were metadata-only.
- `Source-integrity handling`: The selected unit was initially partial because full-paper HTML was absent. A bounded brokered repair preserved the valid PDF and collected official metadata and full-paper HTML. The PDF is 1,442,366 bytes with `%PDF-` header and trailing `%%EOF`; the HTML is 774,129 bytes with 123,748 body characters, a document marker, 91 heading/section markers, and seven checked structure terms. The local README, provenance, machine-readable summary, verification report, and receipt were updated. No partial files remained. The source package was unavailable, but PDF plus complete HTML passed the required gate.

## Scope, Constraints, and Assumptions

- `Scope`: MCPWorld's stated problem, framework, evaluator, benchmark composition, reported experiment, limitations, official implementation context, and related-DEP synthesis.
- `Temporal boundary`: arXiv v1 and the public repository state inspected on 2026-07-30.
- `Evidence limits`: The benchmark, applications, MCP servers, agent, and official implementation were not executed. No evaluator error rate or independent reproduction was established.
- `Assumptions`: The arXiv record and DOI correctly identify the reviewed paper; the verified local source records correspond to the public paper URLs.
- `Constraints`: Source locality, public-artifact sanitization, no source redistribution, no credential handling, and authorized/synthetic testbed framing are mandatory.
- `Out of scope`: Current-model leaderboard claims, code reproduction, deployment in third-party applications, security testing, and conclusion beyond the reported evaluation setup.
- `Intended use`: Research review, evaluator-design planning, safe benchmark governance, and future replication design.
- `Audience`: Agent-systems researchers, benchmark maintainers, evaluation engineers, and product teams building authorized computer-use testing.
- `Reproducibility boundary`: The research is inspectable from cited public sources, but a reproduction needs pinned application builds, task manifests, hook definitions, MCP server versions, model/provider access, and isolated compute.
- `Data sensitivity`: Public scholarly and repository sources only; the verified source files and derived local records remain withheld.

## Observations

- `Observed pattern`: Hybrid access can help, but the paper's own failure analysis shows that a tool surface's completeness is a major confounder in interpreting modality scores.
- `Observed pattern`: Key-step completion makes partial progress visible and is more informative than a terminal outcome alone for long or stateful tasks.
- `Technical implication`: Event-based verification is most valuable when its event schema, instrumentation version, and application build are retained with the result.
- `Contradiction or tension`: The paper reports 201 tasks, whereas the observed official repository README describes approximately 170; no reconciliation was inferred.
- `Open question`: How stable are hook-based verifiers across upstream application releases and platform-specific builds?
- `Reviewer hypothesis`: A benchmark that publishes evaluator-lineage records can diagnose whether score changes come from the agent, tool surface, task, or verifier.

## Considerations

- `Security`: Run agents only in isolated, disposable, authorized environments with no credentials and a default-deny network posture.
- `Evaluator integrity`: Treat hook scripts, task setup, and expected events as versioned test assets; test them against seeded positive and negative fixtures.
- `Measurement`: Report task success, key steps, modality, tool availability, timeout, evaluator errors, and state-reset outcomes separately.
- `Maintenance`: Application updates can invalidate instrumentation and MCP schemas; a release should include compatibility status and known flaky tasks.
- `Fairness`: Modality comparisons should disclose tool descriptions, tool counts, prompt budget, agent model, retries, and time limits.
- `Privacy`: Task fixtures, logs, screenshots, and application state can contain sensitive data in downstream deployments; use synthetic or explicitly authorized data.
- `Cost`: Hybrid evaluation can increase prompt/tool complexity; measure token use, latency, reset cost, and human maintenance alongside success rate.

## Strengths

1. A unified GUI, MCP/API, and hybrid evaluation frame addresses an increasingly realistic agent interface landscape.
2. White-box application events can verify transient intermediate state that UI and file checks may miss.
3. The paper provides task/application counts, difficulty groups, key-step framing, and a modality comparison.
4. The official repository and MIT license improve inspectability and possible follow-on replication.
5. The authors state meaningful boundaries around model coverage, white-box scope, annotation work, and task complexity.

## Weaknesses

1. The reported results use one dated agent/model configuration and do not establish general performance ordering.
2. White-box evaluation excludes many closed or difficult-to-instrument applications.
3. Tool coverage and tool-description quality confound the MCP-only and hybrid comparisons.
4. Evaluator false-positive/false-negative rates and drift resilience are not quantified in the inspected paper.
5. The paper/repository task-count difference makes version pinning essential before reuse.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Versioned evaluator manifests | Reproducibility | Bind task, app build, hook, MCP schema, and expected event | Traceable score changes | More release maintenance | Replay a fixed smoke corpus after every dependency update |
| Evaluator calibration set | Measurement validity | Measure positive, negative, delayed, and malformed event cases | Known verifier error envelope | Requires hand-authored fixtures | Compare hooks against deterministic task-state oracles |
| Tool-surface coverage matrix | Modality analysis | Separate absent APIs from planning/tool-choice failures | Better interpretation of MCP scores | Taxonomy can become stale | Score required subgoals against exposed tools per task |
| Cross-agent, pinned replication | Generalization | Test multiple agent families with unchanged benchmark assets | Stronger external validity | Provider drift and cost | Pre-register models, prompts, retries, and success criteria |

## Potential Implementations

1. `Event-backed desktop-agent evaluator`
   - `User`: benchmark maintainer.
   - `Goal`: score an authorized agent by task and key-step state events rather than self-report.
   - `Core mechanism`: containerized task fixture, versioned hook manifest, modality ledger, and fail-closed evaluator.
   - `Required inputs`: synthetic/authorized application build, task config, expected-event schema, tool surface, and resource policy.
   - `Outputs`: outcome, key-step vector, event evidence, evaluator version, timeout/reset state, and review flags.
   - `Risk controls`: no credentials, no unrestricted network, disposable state, process/time limits, and log redaction.
   - `Evaluation`: deterministic positive/negative event fixtures plus manual audit samples.

2. `MCP tool-surface gap map`
   - `User`: application and agent developers.
   - `Goal`: identify task capabilities unavailable or poorly described through MCP tools.
   - `Core mechanism`: map task subgoals to API, GUI, or hybrid action affordances; retain explicit abstentions.
   - `Required inputs`: task graph, tool schemas/descriptions, GUI affordance inventory, and version IDs.
   - `Outputs`: coverage matrix, gap list, ambiguity score, and candidate tool-description improvements.
   - `Risk controls`: use synthetic tasks and review proposed tool exposure for least privilege.
   - `Evaluation`: compare gap predictions with annotated task failures under pinned agents.

3. `Evaluator-lineage dashboard`
   - `User`: research and quality teams.
   - `Goal`: explain benchmark score deltas without conflating agent and environment changes.
   - `Core mechanism`: join trial results to task, app, hook, tool-surface, and model-version records.
   - `Required inputs`: immutable manifests and public-safe run summaries.
   - `Outputs`: per-version trend view, regression alerts, and replay queue.
   - `Risk controls`: redact task content and logs; require review before declaring a regression.
   - `Evaluation`: seeded changes to a hook, tool schema, and agent policy should be separately attributable.

## Three Ways to Exercise This Research

1. `Synthetic event-oracle task`: Build a tiny open application fixture with one GUI path and one tool path to the same state change. Record the expected internal event. Success means both paths score identically when correct; stop if the fixture cannot be isolated from host state.
2. `Tool-gap audit`: Choose five authorized tasks and map each required subgoal to GUI, MCP, or both. Compare the matrix with observed failures. Success means every “missing capability” conclusion names the absent affordance; stop if tool exposure would increase privileges unnecessarily.
3. `Evaluator-drift replay`: Pin a small task corpus and replay it after one controlled application or hook change. Success means score changes are attributed to the changed manifest component; stop if any expected event is ambiguous or the environment cannot reset cleanly.

## Example MVP Product

- `Product name`: TraceBench CUA.
- `Target user`: an engineering team validating an internal desktop automation agent before authorized rollout.
- `Problem`: terminal success labels do not reveal whether the agent used a valid route, completed critical steps, or was judged by a stable evaluator.
- `Core workflow`: select a synthetic or approved application fixture; run GUI, tool, or hybrid trials in a disposable container; capture versioned events; validate against task contracts; publish a redacted result card.
- `Data requirements`: versioned task manifests, synthetic/authorized state fixtures, event schemas, application build IDs, tool schemas, and evaluation policies.
- `Architecture`: manifest validator -> isolated environment -> agent adapter -> event collector -> contract evaluator -> lineage store -> result dashboard.
- `Success metrics`: deterministic evaluator agreement on smoke fixtures, zero host-state leakage, explicit attribution for every score change, and bounded reset/latency cost.
- `Risk controls`: no secrets, no default network, read-only source where possible, disposable write layer, resource limits, audit logs, and human approval for non-synthetic data.
- `Limitations`: an MVP cannot prove production reliability, and hook coverage may not represent closed applications or evolving upstream software.
- `MVP boundary`: one application, ten synthetic tasks, GUI plus mock-MCP paths, no autonomous deployment, and one evaluator backend.
- `Deployment model`: local isolated runner or controlled CI environment.
- `Evaluation plan`: contract unit tests, event-fault injection, environment-reset checks, and repeated deterministic smoke trials.
- `Failure modes`: stale hook, incomplete tool schema, false completion event, delayed event, unsafely exposed tool, or unreset task state.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| MCPWorld | Primary paper | Reviewed benchmark and white-box evaluator | https://arxiv.org/abs/2506.07672 |
| MCPWorld official repository | Official implementation | Public code, containerization, and task/evaluator context | https://github.com/SAAgent/MCPWorld |
| Agent State Review | Related DEP | State trace, runtime monitoring, and evidence replay overlap | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` |
| Agent Reliability Gates | Related DEP | Explicit verification and action-authorization gates | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` |
| OMGEval Benchmark | Related DEP | Benchmark governance, calibration, and scoped-score overlap | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` |
| AgentStudio | Related work cited by MCPWorld | Prior interface comparison context described in the paper | https://arxiv.org/abs/2505.10627 |
| OSWorld | Related work cited by MCPWorld | Desktop GUI-agent benchmark comparison point | https://arxiv.org/abs/2404.07972 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2506.07672 | Identity, authors, date, category, DOI, license, and code link | 2026-07-30 | Metadata only for empirical purposes |
| R2 | https://arxiv.org/pdf/2506.07672 | Full paper and visual/table cross-check | 2026-07-30 | Verified locally; not redistributed |
| R3 | https://arxiv.org/html/2506.07672 | Full paper, sections, tables, limitations, and appendices | 2026-07-30 | Verified full document; not abstract-only HTML |
| R4 | https://doi.org/10.48550/arXiv.2506.07672 | Persistent arXiv DOI | 2026-07-30 | DataCite-issued arXiv DOI |
| R5 | https://github.com/SAAgent/MCPWorld | Implementation availability, README, and MIT license context | 2026-07-30 | Not executed |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public-artifact and source-locality rules | 2026-07-30 | Fetched before drafting |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-07-30 | Fetched before drafting |
| R8 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository rules and dedup context | 2026-07-30 | Fetched before reliance |
| R9 | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | State-trace bridge | 2026-07-30 | Related repository artifact |
| R10 | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` | Reliability-gate bridge | 2026-07-30 | Related repository artifact |
| R11 | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` | Evaluation-governance bridge | 2026-07-30 | Related repository artifact |

## Appendix

### Source Integrity and Public-Output Gate

- Local source status before review: partial because the full-paper HTML was missing.
- Local repair result: complete after a bounded brokered repair collected official metadata and full-paper HTML while preserving the valid existing PDF.
- PDF checks: size above 10 KB; `%PDF-` header present; trailing `%%EOF` present.
- HTML checks: size above 5 KB; body above 2,000 characters after scripts/styles removal; document marker present; at least two headings; at least two paper-structure terms present.
- Source package: unavailable through the bounded source request; this was recorded locally and does not replace the verified PDF/HTML pair.
- Public-output rule: this DEP contains only Markdown derived artifacts and public locators. No `.source/` directory exists, and no original source document, cache, extracted text, provenance record, or receipt is staged or uploaded.
