# Black Lake Arxiv Report-Mark - Mosaic

Automation: Black Lake Arxiv DEP 0900

Artifact type: arXiv paper review and cross-DEP synthesis mark

## Source Metadata

| Field | Value |
|---|---|
| Paper title | Mosaic: Model-based Safety Analysis Framework for AI-enabled Cyber-Physical Systems |
| Authors | Xuan Xie, Jiayang Song, Zhehua Zhou, Fuyuan Zhang, Lei Ma |
| Identifier | arXiv:2305.03882v1 |
| DOI | https://doi.org/10.48550/arXiv.2305.03882 |
| Submitted | 2023-05-06 |
| Subject | Software Engineering (cs.SE) |
| Primary public source | https://arxiv.org/abs/2305.03882 |
| Source package | https://arxiv.org/e-print/2305.03882 |
| Supplemental site | https://sites.google.com/view/ai-cps-mosaic |
| Official code locator | https://anonymous.4open.science/r/mosaic-code-reviewed-FD6F/ |
| Local archive status | Local arXiv archive readme and PDF presence were observed; local path withheld and source files were not redistributed. |
| Access date | 2026-07-09 |

## Concise Research Notes

Mosaic addresses safety analysis for AI-enabled cyber-physical systems, where learning-based controllers can improve performance while introducing hard-to-explain safety risk. The paper proposes an abstract Markov decision process model built from simulation traces and uses that model in two safety-analysis modes: online safety monitoring with probabilistic model checking and offline model-guided falsification.

The reviewed source package shows a three-part workflow: data collection, model abstraction, and safety analysis. The abstraction begins from a Moore-machine view of the AI-CPS, reduces state/action/transition/label spaces into a safety-analysis-oriented MDP, then refines the model when robustness variance suggests imprecise state labeling. Runtime monitoring uses a probabilistic computation tree logic query over the abstract model to decide whether to keep the AI controller active or switch to a traditional safety controller.

The paper evaluates Mosaic on adaptive cruise control, abstract fuel control, and an exothermic chemical reactor. Reported results include 92.22% average abstract-model labeling preciseness, online safety/performance changes across nine AI-controller settings, falsification success comparisons against Random, Breach, and Mosaic-rand, and safety-query overhead averaging 0.1032 seconds against 35.7501 seconds simulation time. These are author-reported results from inspected TeX source; this run did not reproduce experiments.

The reusable Black-Lake lesson is that safety evidence for AI-controlled systems benefits from explicit model state. Mosaic converts learned-controller behavior into an auditable abstraction, uses formal queries as runtime signals, and uses those same signals to guide search for counterexamples. That aligns with Black-Lake themes around state ledgers, runtime monitors, verification gates, and source-grounded review.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Notes |
|---|---|---|---|---|
| E1 | arXiv API and abstract page for arXiv:2305.03882 | Title, authors, submission date, category, DOI, abstract, and source links | High | Public arXiv metadata inspected. |
| E2 | arXiv TeX source package `main.tex` | Method, algorithms, benchmark setup, RQ design, result tables, threats, and conclusion | High for reporting source claims | Source package inspected temporarily; not redistributed. |
| E3 | Local archive readme and PDF presence | Random-selection provenance and archive availability | Medium | Local path withheld; PDF was not deposited. |
| E4 | Official Mosaic supplemental site | Near-primary workflow, RQ descriptions, source-code locator, and supplementary-results context | Medium | Site text inspected; code repository content not directly inspected. |
| E5 | Black-Lake README and Black-Lake-Data README | Repository layout, DEP naming, README, attribution, log/report conventions | High | Repository policy evidence, not paper evidence. |
| E6 | Three related Black-Lake DEP entries | Cross-DEP synthesis around runtime monitoring, state, verification, and governance | Medium | Related generated artifacts inspected as context, not as validation of Mosaic claims. |

## Related DEP Entries

1. `Black-Lake/.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md`
   - Relevance: connects Mosaic's runtime safety monitoring to state traces, calibrated alarms, and evidence replay for AI systems.
   - Source basis: the entry directly discusses Online Safety Monitoring for LLMs, persistent-state monitors, and audit-oriented state ledgers.

2. `Black-Lake/.lake-data/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md`
   - Relevance: connects Mosaic's model-guided falsification and formal-query control signals to agent reliability, process supervision, semantic stopping, and verification-like gates.
   - Source basis: the entry maps agent memory, evaluation, MCP/tool security, OpenRCA-style process evidence, and semantic early stopping sources.

3. `Black-Lake/.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md`
   - Relevance: connects Mosaic's AI-CPS safety framing to operational AI evaluation, explicit agent-state ledgers, governed tool calls, robotics safety/privacy, and high-stakes domain constraints.
   - Source basis: the entry cites Deployment Simulation, LedgerAgent, AI-agent code-review habituation, FM-powered robotics security/privacy, and related governance sources.

## Synthesis Note

### Concept Bridge

Mosaic is a cyber-physical counterpart to the repository's recent state-and-monitoring artifacts. Where agent-state entries preserve evidence, task state, and monitor alarms for software agents, Mosaic builds an abstract MDP from AI-CPS traces and uses probabilistic queries as the monitor signal. The bridge is not that LLM agents and vehicle/reactor controllers are the same system; it is that both need compact, auditable state representations that can trigger intervention, guide search, and preserve review evidence.

### Potential Implementations

1. `Model-state safety monitor`: Use Mosaic's MDP/PCTL pattern to build a dashboard for simulated AI-CPS traces that shows current abstract state, risk query, suggested controller mode, and evidence trace.
2. `Verification-guided test queue`: Use the falsification queue idea to prioritize test inputs whose abstract state is likely to enter unsafe regions, while retaining random and baseline search for coverage.
3. `Cross-domain state ledger`: Adapt the Black-Lake state-ledger pattern to store physical state, controller action, safety-query result, and intervention rationale for each simulation episode.

### Deeper Relationship Observations

1. Mosaic treats a learned controller as part of a larger controlled system, not as an isolated model; that mirrors Black-Lake's agent-system reviews, where model behavior is inseparable from tools, state, and workflow.
2. Mosaic's safety-query overhead result matters because runtime monitors must be cheap enough to run during operation; Black-Lake's agent monitoring artifacts face the same practical latency constraint.
3. The paper's weaker AFC monitoring results show that switching to a traditional controller is not automatically safer when the fallback is weaker; this is a useful caution for agent fallback policies and human-review handoffs.

### Conceptual Similarities

1. `Explicit state`: Mosaic's abstract MDP, Agent State Review's ledgers, and LedgerAgent-style task state all convert hidden process context into reviewable structure.
2. `Runtime gate`: Mosaic's PCTL safety query, online LLM monitor alarms, and verification-gated execution all use a separate signal to decide whether work may continue.
3. `Search guidance`: Mosaic's falsification queue, semantic early stopping, and process-supervision reviews all use intermediate evidence to guide downstream exploration instead of relying on blind sampling.

### MVP Implementations with Code Mock-Ups

1. `Safety query ledger`

```python
def record_safety_query(run_id, state_id, p_unsafe, threshold=0.8):
    decision = "switch_to_safety_controller" if p_unsafe > threshold else "continue_ai_controller"
    return {
        "run_id": run_id,
        "abstract_state": state_id,
        "p_unsafe_10_steps": round(p_unsafe, 4),
        "decision": decision,
        "evidence": "MDP/PCTL query result from simulation trace"
    }
```

2. `Falsification seed triage`

```python
def enqueue_if_promising(queue, candidate, robustness, unsafe_flag):
    if robustness < 0:
        return "falsifying_input", candidate
    if unsafe_flag:
        queue.append(candidate)
        return "queued_for_local_search", None
    return "discarded_for_now", None
```

3. `Trace-to-review artifact`

```python
def summarize_episode(episode):
    return {
        "controller": episode["controller"],
        "unsafe_query_count": sum(1 for q in episode["queries"] if q["decision"].startswith("switch")),
        "interventions": [q for q in episode["queries"] if q["decision"].startswith("switch")],
        "review_note": "Inspect intervention points and compare against robustness outcomes."
    }
```

### Developer Challenges

1. Building an abstraction pipeline that preserves safety-relevant behavior while keeping state spaces small enough for probabilistic model checking.
2. Integrating simulation, controller interfaces, PRISM/Breach-style tooling, and result ledgers without losing source traceability.
3. Choosing fallback controllers and safety queries that improve safety without creating brittle or performance-destroying switching behavior.

### Author Challenges

1. Demonstrating that abstract-model precision generalizes beyond the selected benchmark systems and parameter settings.
2. Making code, benchmark configurations, and supplementary data easy to inspect after anonymous-review infrastructure changes or expires.
3. Explaining failure cases, especially where Mosaic underperforms baselines or where fallback controllers reduce both safety and performance.

## Validation Notes

- Candidate count was measured from local PDF files in the arXiv archive using `rg --files -g "*.pdf"`.
- Random selection used a uniform random PDF index with `Get-Random`; zero-based selected index was 22,270 from 64,657 candidates.
- Deduplication scanned Black-Lake `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data `.lake-data` and `.reports` entries for arXiv IDs, DOI markers, normalized title, and slug.
- No duplicate marker was found for arXiv:2305.03882; no reselection was required.
- arXiv HTML was unavailable for this paper; the public arXiv source package was inspected instead.
- The official code locator was reachable, but direct static README inspection returned the application shell, so code contents were not used as evidence.
- No original source file was collected into the repository because redistribution permission was not confirmed.
- Generated public files were scanned for local path, home-directory, local timezone, and exact local execution timestamp leaks.

## Attribution Block

- Source URL: https://arxiv.org/abs/2305.03882
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Primary arXiv metadata and abstract page for the selected paper.
- Source URL: https://export.arxiv.org/api/query?id_list=2305.03882
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: arXiv API metadata source for title, authors, submission date, category, version, and summary.
- Source URL: https://arxiv.org/e-print/2305.03882
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Public arXiv source package inspected for method, evaluation setup, tables, and conclusion; source files were not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2305.03882
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Persistent DOI for the selected arXiv paper.
- Source URL: https://sites.google.com/view/ai-cps-mosaic
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Official supplemental site with workflow, RQ, supplementary-results, and code-locator context.
- Source URL: https://anonymous.4open.science/r/mosaic-code-reviewed-FD6F/
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Official code locator from the supplemental site; reachable, but code contents were not directly inspected.
- Source file: local arXiv archive readme and PDF presence, path withheld
  - Applies to: `.logs/20260709-Arxiv-Mosaic-LOG.md`, Report-Mark.md, and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Local archive evidence used only for random-selection provenance; no local path or original source file is published.
- Repository file: `Black-Lake/README.md`
  - Applies to: all generated repository artifacts
  - Notes: Live target repository authority for DEP, log, report, README, attribution, and commit-message rules.
- Repository file: `Black-Lake-Data/README.md`
  - Applies to: all generated repository artifacts
  - Notes: Related source-repository authority for DEP layout and attribution context.
- Repository file: `Black-Lake/.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md`
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Related DEP entry for runtime monitoring, state traces, and evidence replay.
- Repository file: `Black-Lake/.lake-data/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md`
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Related DEP entry for agent-system reliability, verification-like process evidence, and tool/security review.
- Repository file: `Black-Lake/.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md`
  - Applies to: Report-Mark.md and `.lake-data/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
  - Notes: Related DEP entry for operational AI evaluation, structured agent state, governance, and embodied-systems safety.
