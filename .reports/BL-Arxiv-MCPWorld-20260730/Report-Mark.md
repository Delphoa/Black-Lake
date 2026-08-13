# Report-Mark: MCPWorld

## Source Metadata

| Field | Value |
|---|---|
| Title | *MCPWorld: A Unified Benchmarking Testbed for API, GUI, and Hybrid Computer Use Agents* |
| Authors | Yunhe Yan; Shihe Wang; Jiajun Du; Yexuan Yang; Yuxuan Shan; Qichen Qiu; Xianqing Jia; Xinge Wang; Xin Yuan; Xu Han; Mao Qin; Yinxiao Chen; Chen Peng; Shangguang Wang; Mengwei Xu |
| Primary record | [arXiv:2506.07672](https://arxiv.org/abs/2506.07672), submitted 2025-06-09, cs.AI |
| DOI | [10.48550/arXiv.2506.07672](https://doi.org/10.48550/arXiv.2506.07672) |
| Primary evidence inspected | Verified PDF, verified arXiv full-paper HTML, arXiv metadata, and [official repository](https://github.com/SAAgent/MCPWorld) |
| License and implementation | arXiv metadata exposes CC BY 4.0; the official repository displays an MIT license. Code was inspected at repository/README level only and was not executed. |
| Public-source policy | Source files were verified and retained locally, but no PDF, HTML, source archive, cache, or extracted source text is included here. |

## Research Notes

MCPWorld is an author-proposed white-box benchmark for computer-use agents that operate through GUI controls, MCP/API tools, or both. Its central design is to expose tool-based observation/action spaces while evaluating task completion from internal application signals rather than only screenshots, accessibility trees, or output files.

The paper describes 201 tasks spanning ten open-source desktop applications. It categorizes task difficulty by human GUI-step counts and uses annotated intermediate key steps. Completion checks can use dynamic instrumentation, targeted code injection, or API/log/database state queries, depending on the application.

For one reported evaluation, the authors run Claude 3.7 Sonnet through GUI-only, MCP-only, and hybrid configurations over all tasks, with three attempts per task and a 300-second attempt limit. The reported task-success rates are 70.65% (GUI only), 53.23% (MCP only), and 75.12% (hybrid); key-step completion is 68.82%, 59.78%, and 69.63%, respectively. These are author-reported results in a specific benchmark, agent, tool-surface, and model setup, not a general claim about current agents.

The most useful engineering implication is that an evaluator can separate task outcome from interaction modality when it checks a stable, implementation-aware event. The corresponding risk is maintenance: hooks and state queries are benchmark assets that must remain versioned and audited as applications change. The official repository provides an MIT-licensed implementation and describes a containerized platform, but its README currently describes approximately 170 tasks rather than the paper's 201; this may be a version difference and was not reconciled by executing the release.

## Evidence and Attribution

| ID | Evidence | Supports | Assessment |
|---|---|---|---|
| E1 | [arXiv metadata](https://arxiv.org/abs/2506.07672) | Identity, authors, date, category, DOI, license, and code locator | High confidence for metadata; abstract alone was not used for empirical details. |
| E2 | [Full-paper HTML](https://arxiv.org/html/2506.07672) and verified PDF | Framework architecture, task/app counts, evaluator mechanisms, experiments, tables, limitations | High confidence for transcription; results remain author-reported. |
| E3 | [SAAgent/MCPWorld](https://github.com/SAAgent/MCPWorld) | Public implementation availability, MIT license, containerized setup, white-box-evaluation description | Medium confidence for repository state; no installation or execution was performed. |
| E4 | `Agent State Review` related DEP | State traces, runtime monitoring, and replayable evidence as review objects | Conceptual bridge only; no joint experiment. |
| E5 | `Agent Reliability Gates` related DEP | Explicit evidence, authorization, verification, and state-publication gates | Conceptual bridge only; no joint experiment. |
| E6 | `OMGEval Benchmark` related DEP | Measurement governance, judge limits, and versioned evaluation conditions | Conceptual bridge only; no joint experiment. |

## Related DEP Entries

| Entry | Repository-relative path | Concrete overlap | Source basis |
|---|---|---|---|
| Agent State Review | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | Both treat internal state and evidence traces as first-class objects for assessing agent behavior rather than relying only on terminal text. | Its evidence ledger and executive summary discuss persistent agent state, runtime monitoring, and replayable evidence. |
| Agent Reliability Gates | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` | Both require observable transition checks: MCPWorld validates application events, while the DEP frames gates for evidence intake, action authorization, and result verification. | Its executive summary and detailed sections define explicit decision records and transition-level controls. |
| OMGEval Benchmark | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` | Both expose the limits of a single aggregate score and motivate versioned evaluators, scoped claims, and calibration evidence. | Its methodology and observations distinguish benchmark construction from universal model claims. |

## Synthesis Note

### Concept Bridge

MCPWorld supplies a modality-neutral event oracle for desktop-agent tasks. The three related DEP entries extend that idea into a broader evaluation discipline: retain a trace of the state transition, record the rule that accepted it, expose uncertainty and version boundaries, and keep the benchmark separate from the systems it scores. Together, they support an inspectable agent-evaluation loop rather than a single terminal pass/fail metric.

### Potential Implementations

1. **Event-backed CUA regression suite** — Execute synthetic GUI, API, and hybrid tasks in disposable containers; emit task success, key-step events, tool modality, and evaluator version for each trial.
2. **Evaluator lineage ledger** — Version hook definitions, application build IDs, task manifests, expected events, and known flaky conditions so a score can be traced to the evaluator that produced it.
3. **Tool-surface coverage analyzer** — Compare which task subgoals each MCP tool can express, then distinguish missing capability from planning failure and GUI-control failure.

### Deeper Relationship Observations

1. Internal application events play the same evidentiary role as a reliability gate: they convert an ambiguous behavioral claim into an explicit accept/reject record.
2. Hybrid-agent evaluation is partly a tool-surface design problem; MCP-only failure can indicate incomplete or poorly described tools rather than a pure model-reasoning deficit.
3. Reproducible benchmark results need two lineages: the agent trajectory and the evaluator/application version that interpreted it.

### Conceptual Similarities

1. MCPWorld and Agent State Review both privilege inspectable state over surface-only observations.
2. MCPWorld and Agent Reliability Gates both require a declared rule between observed evidence and an accepted outcome.
3. MCPWorld and OMGEval Benchmark both need scoped, versioned interpretation instead of timeless leaderboard claims.

### MVP Implementations with Code Mock-Ups

1. **Event contract validator**

```python
def validate_event(event: dict, expected: dict) -> bool:
    return (
        event.get("task_id") == expected["task_id"]
        and event.get("kind") == expected["kind"]
        and event.get("payload") == expected["payload"]
    )
```

2. **Modality-aware result ledger**

```python
def record_result(trial: dict) -> dict:
    return {
        "task_id": trial["task_id"],
        "modality": trial["modality"],
        "task_success": bool(trial["task_success"]),
        "key_steps": list(trial.get("key_steps", [])),
        "evaluator_version": trial["evaluator_version"],
    }
```

3. **Fail-closed tool coverage check**

```python
def missing_capabilities(required: set[str], tools: set[str]) -> set[str]:
    missing = required - tools
    if missing:
        return missing
    return set()
```

### Developer Challenges

1. Keeping hooks, schemas, and expected state transitions compatible with changing upstream applications.
2. Containing GUI and tool executions so tasks cannot access credentials, uncontrolled networks, or host state.
3. Distinguishing evaluator defects from agent defects when an event is absent, duplicated, or delayed.

### Author Challenges

1. Expanding beyond one agent/model configuration without conflating model changes with evaluator changes.
2. Quantifying evaluator reliability, including hook false positives, false negatives, and application-version drift.
3. Reconciling paper and repository task counts through explicit release/version mapping.

## Validation Notes

- Source gate passed before synthesis: the PDF and full-paper HTML both satisfied the required completeness checks; the metadata page was treated as metadata only.
- The report uses public URLs and repository-relative paths only. No local absolute path, machine identifier, source payload, cache, or exact local execution timestamp is present.
- Exactly three related DEP entries, three potential implementations, three deeper relationship observations, three conceptual similarities, three code mock-ups, three developer challenges, and three author challenges are included.
- No source file is attached, staged, or uploaded with this report.

## Attribution Block

- Source URL: https://arxiv.org/abs/2506.07672
  - Applies to: this Report-Mark and the MCPWorld DEP-E manuscript.
  - Notes: Canonical metadata, authors, date, category, license locator, DOI, and official code locator.
- Source URL: https://arxiv.org/html/2506.07672
  - Applies to: this Report-Mark and the MCPWorld DEP-E manuscript.
  - Notes: Full-paper method, experiment, result, limitation, and appendix evidence; source copy withheld locally.
- Source URL: https://github.com/SAAgent/MCPWorld
  - Applies to: this Report-Mark and the MCPWorld DEP-E manuscript.
  - Notes: Official implementation availability and MIT-license context; not executed.
- Source file: Withheld locally
  - Applies to: all public artifacts in this deposition.
  - Notes: Verified PDF, full-paper HTML, metadata, provenance, and receipts were not uploaded or redistributed.
