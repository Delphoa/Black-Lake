---
title: "Report-Mark - AgentEconomist"
artifact_type: "Black-Lake Arxiv research report"
primary_subject: "AgentEconomist: An End-to-end Agentic System Translating Economic Intuitions into Executable Computational Experiments"
source_id: "arXiv:2604.27725v1"
public_date: "2026-08-05"
source_status: "complete local PDF and full-paper HTML verified; source files withheld locally"
---

# Report-Mark - AgentEconomist

## Source Metadata

| Field | Value |
|---|---|
| Title | *AgentEconomist: An End-to-end Agentic System Translating Economic Intuitions into Executable Computational Experiments* |
| Authors | Jiaju Chen; Jinghua Piao; Xia Xu; Songwei Li; Tong Xia; Xiangnan He; Yong Li |
| arXiv | [arXiv:2604.27725v1](https://arxiv.org/abs/2604.27725) |
| arXiv full-paper HTML | [Full-paper HTML](https://arxiv.org/html/2604.27725) |
| arXiv DOI | [10.48550/arXiv.2604.27725](https://doi.org/10.48550/arXiv.2604.27725) |
| Official code repository | [Jiaju-Chen/AgentEconomist](https://github.com/Jiaju-Chen/AgentEconomist) |
| Code license | MIT license visible in the inspected repository |
| Source integrity | Initial PDF-only partial state was repaired with one bounded official HTML fetch; final PDF and full-paper HTML passed the local gate. |
| Redistribution | Source PDF, HTML, metadata, extracted text, large data, model inputs, and provenance records remain local and were not uploaded. |

## Research Notes

AgentEconomist targets the intuition-to-experiment gap in economics. Its thesis is that a research copilot should preserve human sense-making while making the path from an abstract intuition to a testable simulation explicit. The proposed system combines a literature-grounded retrieval pipeline, specialized agent stages, structured textual memory, an MCP-based simulator toolbox, and the AgentEconomy agent-based environment.

The agent core has three stages. Idea Development retrieves economics evidence, proposes mechanisms and hypotheses, checks simulator feasibility, and uses a parameter-first strategy. Experimental Design maps the accepted hypothesis to control/treatment structures, minimum necessary changes, and computable metrics. Experimental Execution configures and runs AgentEconomy through MCP, records state and errors, and returns structured metrics and visualizations. The paper states that fixed seeds and versioned configurations support reproducible reruns.

AgentEconomy models households, firms, government, and a bank interacting through labor and product markets. Agents use LLM-based reasoning with empirical initialization such as PSID profiles. This enables policy-shock simulations, but it also makes the results dependent on behavioral prompts, agent population design, data provenance, model choice, and the simulator’s institutional assumptions.

The evaluation compares AgentEconomist with general-purpose LLM baselines, primarily GPT-5.2 and Gemini 3-Pro, under matched user intuitions. Eight dimensions are scored on a 5-point Likert scale. The paper reports 15 participants, 14 usable interaction logs for hypothesis-level paired comparisons, and a within-subject design. For Literature Grounding, LLM judging moves from 3.36 to 4.93 with reported p=0.00195, while human judging moves from 3.11 to 4.50 with p=0.0117. For Novelty & Insight, LLM judging moves from 3.00 to 4.43 with p=0.0039, while human judging moves from 3.12 to 4.05 with p=0.0185. These are author-reported paired comparisons, not independently reproduced results.

The qualitative study uses open-ended prompts with uneven response counts: Q1 has n=8, Q2–Q4 have n=7, and Q5 has n=3. Reported themes include grounded trust, operationalization support, and mechanistic scaffolding; reported pain points include latency, limited process transparency, and instruction-following drift. A case study of innovation support in the simulator reports +4.3% cumulative household consumption, +27.9% income, and +21.7% wealth, alongside higher savings and slightly higher inequality. The authors explicitly frame this as interpretable simulation evidence, not discovery of real economic laws.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Confidence and boundary |
|---|---|---|---|
| E1 | [arXiv metadata and abstract](https://arxiv.org/abs/2604.27725) | Identity, authors, arXiv version, subject, abstract, keywords, and public source links | High for identity and abstract-level claims; abstract alone is insufficient for method or empirical claims |
| E2 | [Verified arXiv full-paper HTML](https://arxiv.org/html/2604.27725) | Architecture, RAG corpus, structured memory, MCP toolbox, AgentEconomy, experimental protocol, scores, p-values, case study, limitations, and references | High for directly inspected sections; reported measurements were not independently reproduced |
| E3 | Local verified PDF of arXiv:2604.27725 | Source-integrity confirmation and cross-check of the full-paper document | High for integrity; the source file is withheld from this public artifact |
| E4 | [Author repository README](https://github.com/Jiaju-Chen/AgentEconomist), [LICENSE](https://github.com/Jiaju-Chen/AgentEconomist/blob/main/LICENSE), and [indexer](https://github.com/Jiaju-Chen/AgentEconomist/blob/main/database/scripts/build_index.py) | Public implementation identity, MIT license, setup/data requirements, SPECTER2 indexing path, and repository limitations | Medium-high; no code or large data was executed or independently verified |
| E5 | [ADKO Knowledge Agents DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260805-ADKO%20Knowledge%20Agents/2605.07863-whitepaper-review.md) | Related state decisions and knowledge exchange across agents | Medium; related artifact is a repository-derived review, not a new primary source for AgentEconomist |
| E6 | [Agent State Review DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md) | Related persistent-state, evidence replay, structured memory, and auditability context | Medium; related artifact contains mixed-depth source coverage |
| E7 | [MASS Social Simulation DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260719-MASS%20Social%20Simulation/2606.09198-whitepaper-review.md) | Related memory-augmented social simulation and simulation-versus-real-world evidence boundary | Medium; related artifact is contextual comparison rather than independent validation |

The distinction between author claims and reviewer synthesis is maintained throughout. The reported gains, p-values, participant counts, and simulation effect sizes are source claims from E2. The recommendation to expose retrieval identity, simulator configuration, memory state, and execution traces as auditable artifacts is reviewer synthesis grounded in E2 and the related entries.

## Related DEP Entries

Exactly three existing Black Lake entries were selected for concrete conceptual overlap:

| DEP entry | Public path | Relevance reason | Source basis |
|---|---|---|---|
| ADKO Knowledge Agents | [DEP-A-20260805-ADKO Knowledge Agents](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260805-ADKO%20Knowledge%20Agents/2605.07863-whitepaper-review.md) | Makes decentralized knowledge exchange, compact state, and decision surfaces explicit, which parallels AgentEconomist’s RAG, structured memory, and multi-stage coordination. | The related review describes knowledge tokens, agent communication, explicit resource/information constraints, and mechanism-level evaluation. |
| Agent State Review | [DEP-E-20260708-Agent State Review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md) | Supplies the state, replay, provenance, and audit lens needed to evaluate AgentEconomist’s memory and MCP execution traces. | The related review treats persistent intermediate state and evidence replay as first-class review objects. |
| MASS Social Simulation | [DEP-A-20260719-MASS Social Simulation](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260719-MASS%20Social%20Simulation/2606.09198-whitepaper-review.md) | Directly overlaps with memory-augmented agent-based simulation and reinforces that simulated social or economic outcomes are hypothesis-generation evidence, not real-population causal evidence. | The related review discusses dynamic memory, social simulation, model-judged quality, and external-validity limits. |

## Synthesis Note

### Concept Bridge

AgentEconomist’s durable bridge is from **epistemic context** to **executable state**. A user intuition is not treated as a prompt to answer; it becomes a versioned chain of retrieved evidence, parameter choices, hypothesis constraints, simulator configuration, run status, and metric outputs. ADKO contributes the idea that intermediate knowledge decisions should be explicit and resource-aware. Agent State Review contributes replayable evidence and state auditability. MASS Social Simulation contributes the warning that a rich simulated trajectory can improve reasoning support without becoming a measurement of society. Together, these links suggest that a scientific agent should publish a traceable experiment object, not merely a fluent conclusion.

### Potential Implementations

1. **Research-loop ledger:** store synthetic or authorized research sessions as immutable intuition, retrieved-source IDs, hypothesis revisions, parameter maps, configuration hashes, run status, and metric outputs; expose an abstain state when feasibility or provenance is incomplete.
2. **Grounded hypothesis benchmark:** compare a general LLM with a domain-grounded agent on public economics prompts using a fixed corpus snapshot, matched retrieval budget, blinded human scoring, citation checks, and simulator-feasibility labels.
3. **Simulation audit gateway:** wrap an agent-based simulator with a review-only MCP interface that validates allowed parameters, binds each run to a configuration and seed, records tool calls, and emits a report that labels simulated findings as hypotheses.

### Deeper Relationship Observations

1. Structured memory is not merely a context extension: it is the connective tissue that lets a later researcher explain why a parameter, mechanism, or rejection entered the experiment.
2. RAG and simulation form a coupled evidence loop. Better retrieval can improve hypotheses, but simulator feasibility can also expose that a retrieved mechanism cannot be operationalized under the current environment.
3. The strongest practical claim is process compression with auditability, not autonomous economic discovery; the reported case study is valuable because its assumptions and effect magnitudes are inspectable, not because they generalize to policy reality.

### Conceptual Similarities

1. AgentEconomist, ADKO, and Agent State Review all treat intermediate knowledge/state as a first-class object whose selection or update should be observable.
2. AgentEconomist and MASS Social Simulation both translate high-level social or economic questions into multi-agent simulations while requiring an explicit boundary between simulated behavior and real-world claims.
3. All three related entries and the paper separate an outcome proxy from the mechanism that produced it: judged quality or simulated metrics do not by themselves establish factual grounding, causal validity, or deployment readiness.

### MVP Implementations with Code Mock-ups

1. **Synthetic research-loop ledger**

   ```python
   from dataclasses import dataclass

   @dataclass(frozen=True)
   class ExperimentTrace:
       intuition: str
       source_ids: tuple[str, ...]
       config_hash: str
       seed: int
       status: str

   def reviewable(trace: ExperimentTrace) -> bool:
       return bool(trace.source_ids and trace.config_hash and trace.status in {"planned", "complete"})
   ```

   This toy model stores synthetic provenance only; it does not claim citation correctness or causal validity.

2. **Parameter-feasibility gate**

   ```python
   ALLOWED = {"innovation_support", "tax_rate", "households", "months"}

   def validate_design(parameters: dict[str, float]) -> tuple[bool, list[str]]:
       unknown = sorted(set(parameters) - ALLOWED)
       errors = [f"unsupported parameter: {name}" for name in unknown]
       if parameters.get("households", 0) <= 0:
           errors.append("households must be positive")
       return not errors, errors
   ```

   This bounded gate demonstrates capability-boundary checking without running a simulator or accepting external side effects.

3. **Simulation result labeler**

   ```python
   def label_result(metrics: dict[str, float], evidence_complete: bool) -> dict[str, object]:
       return {
           "metrics": metrics,
           "claim_status": "simulation_hypothesis" if evidence_complete else "blocked",
           "requires_human_review": True,
       }
   ```

   The labeler prevents a toy simulation output from being presented as a real-world economic finding.

### Developer Challenges

1. Build deterministic, versioned interfaces across retrieval, memory, simulator configuration, execution, and result export while retaining enough trace detail for audit.
2. Control cost and latency: the paper reports roughly 20 minutes and 500K tokens for a representative five-household, five-iteration workflow, with simulation-time agent interactions dominating usage.
3. Evaluate grounding and novelty without leaking the answer through retrieval parity, allowing judge-model preference, or confusing fluent mechanism descriptions with valid economic identification.

### Author Challenges

1. Establish baseline parity by giving comparison systems the same corpus scope, retrieval opportunity, citation verification, prompt budget, and task information.
2. Expand the human study beyond 15 participants and report task-level dispersion, missingness, inter-rater reliability, and sensitivity to judge/model choice.
3. Release versioned corpus manifests, model/data provenance, run configurations, seeds, raw aggregate traces, and independent reproduction guidance without redistributing restricted papers, microdata, or participant material.

## Validation Notes

- Manuscript and Report-Mark were generated only after the local PDF/full-paper HTML integrity gate passed.
- The initial partial state was repaired once; no blind retry or destructive cleanup was used, and no partial remained.
- The YAML title and H1 are identical, `AgentEconomist - DEP-E`, and are within the 40-character limit.
- The public DEP short description is `AgentEconomist`, within the 25-character limit.
- Source files, extracted text, caches, local archive metadata, and source packages are withheld; no `.source/` directory is created.
- Public claims cite arXiv, the official author repository, or repository-relative Black Lake entries. No local absolute path, home directory, username, drive path, machine name, timezone label, or exact local execution timestamp is included.

## Final Attribution Block

- Source URL: https://arxiv.org/abs/2604.27725
  - Applies to: paper identity, authors, version, abstract, keywords, and public locators.
- Source URL: https://arxiv.org/html/2604.27725
  - Applies to: full-paper method, experiments, metrics, limitations, conclusion, and references.
- Source URL: https://arxiv.org/pdf/2604.27725
  - Applies to: primary paper integrity and layout cross-check; the PDF remains local and was not deposited.
- Source URL: https://doi.org/10.48550/arXiv.2604.27725
  - Applies to: persistent paper identity.
- Source URL: https://github.com/Jiaju-Chen/AgentEconomist
  - Applies to: public implementation context, repository README, and code availability statement.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260805-ADKO%20Knowledge%20Agents/2605.07863-whitepaper-review.md
  - Applies to: related-entry synthesis on decentralized knowledge and explicit state decisions.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md
  - Applies to: related-entry synthesis on persistent state, evidence replay, and auditability.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260719-MASS%20Social%20Simulation/2606.09198-whitepaper-review.md
  - Applies to: related-entry synthesis on memory-augmented simulation and external-validity boundaries.
- Source files: none deposited; the verified local PDF, full-paper HTML, metadata, and provenance records remain withheld locally.
  - Applies to: all generated public artifacts.
