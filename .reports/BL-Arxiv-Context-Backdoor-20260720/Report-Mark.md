# Report-Mark: Context Backdoor Defense

- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P05`
- Review date: 2026-07-20
- Scope: defensive security analysis only

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Compromising Embodied Agents with Contextual Backdoor Attacks* |
| Authors | Aishan Liu; Yuguang Zhou; Tianyuan Zhang; Siyuan Liang; Jiakai Wang; Yanjun Pu; Tianlin Li; Junqi Zhang; Wenbo Zhou; Qing Guo; Dacheng Tao |
| Identifier | arXiv:2408.02882v1; DOI:10.48550/arXiv.2408.02882 |
| Submitted | 2024-08-06 |
| Record | https://arxiv.org/abs/2408.02882 |
| Full paper | https://arxiv.org/html/2408.02882 |
| PDF | https://arxiv.org/pdf/2408.02882 |
| Source state | Verified complete after one bounded official-source repair; all source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260720-8636EDC7`; `BLAD-2200-20260720-8636EDC7-P05` |

## Concise Research Notes

The paper studies a contextual supply-chain threat: untrusted in-context demonstrations can influence a black-box LLM to emit apparently normal programs whose harmful behavior is conditionally activated in downstream embodied agents. Evaluation spans planning, manipulation, visual reasoning, small vehicles, and an autonomous-driving setting. This report omits all trigger, prompt, payload, and reproduction details.

The strongest defensive evidence is that single-layer screening performed poorly in the tested setup. A prompt outlier filter detected 2 of 20 tested poisoned inputs (10%); a Python-like backdoor detector found 5%; five developers detected none of 20 cases when implementation internals were hidden, but detected 65% when full code was exposed, taking 15.4 minutes on average. A behavior-level risk interlock reduced reported attack success from 95% to 25% on 20 cases while reducing clean accuracy by 10 percentage points. These are author-run, small-sample results, not general security guarantees.

The practical conclusion is layered control: signed prompt/example provenance, approved context retrieval, generated-program policy checks, capability isolation, simulation, invariant enforcement, runtime anomaly detection, emergency stops, audit logs, and human authorization. No one detector should be treated as sufficient.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Full-paper Sections 3-7 | Threat model and evaluations across agent tasks | Operational details intentionally omitted; no independent replication |
| Section 8.2 | Prompt-, program-, and agent-level defenses | Small samples and attack-specific settings |
| Defense results | 10% prompt detection, 5% program detection, 65% full-code human detection, runtime interlock delta | Author-reported; denominators mostly 20 |
| Section 10 | Visual-agent focus and ethical framing | Limitations are not exhaustive |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` - trace evidence and post-incident analysis for poisoned agent state.
2. `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md` - controls placed at the layer where failure accumulates.
3. `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md` - provenance, authority, retrieval, and runtime defense layers for persistent state.

## Synthesis Note

### Concept Bridge

Contextual examples are transient agent state with supply-chain properties. Memory forensics records downstream traces, Control Surfaces locates interventions near failure mechanisms, and Memory Defense Layers binds retrieved state to provenance and action authority.

### Potential Implementations

1. Build a signed context registry that accepts only reviewed demonstration bundles and immutable hashes.
2. Gate generated programs through capability allowlists, static checks, simulation, and human approval before physical execution.
3. Add independent runtime invariants and emergency stops that cannot be modified by generated code.

### Deeper Relationship Observations

1. Hidden dependencies defeat human review when auditors cannot inspect the complete transitive implementation.
2. Benign behavior during testing does not prove absence of conditional failure, so evaluation needs counterfactual contexts and environments.
3. Memory and context provenance matter only when authorization also constrains what retrieved state may cause.

### Conceptual Similarities

1. Each related DEP treats agent state as evidence-bearing and potentially adversarial.
2. Each favors layered controls over a universal detector.
3. Each separates model output quality from downstream action safety.

### MVP Implementations with Code Mock-Ups

1. Provenance gate: `assert verify(bundle.signature) and bundle.hash in approved`.
2. Capability gate: `plan = compile_in_sandbox(output); authorize(plan.required_caps)`.
3. Runtime interlock: `if violates_invariant(state, action): emergency_stop()`.

### Developer Challenges

1. Capturing the complete prompt, retrieval, dependency, tool-schema, and generated-code lineage.
2. Testing conditional failures without publishing reusable offensive artifacts.
3. Keeping safety interlocks independent from model-generated control paths.

### Author Challenges

1. Demonstrating external validity beyond selected models, tasks, and small defense samples.
2. Publishing enough evidence for defense replication without enabling misuse.
3. Measuring clean-performance, false-positive, latency, and operator-cost tradeoffs consistently.

## Validation Notes

- First uniform draw, index 31,461 of 75,776; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a valid PDF and official full-paper HTML; metadata was not counted as the paper.
- Defensive scope enforced; operational attack prompts, triggers, code, and procedures are absent.
- Exactly three related entries and three items in each required synthesis subsection are present.
- Public allowlist contains generated Markdown/JSON only; no source file was uploaded.

## Attribution Block

- https://arxiv.org/abs/2408.02882 - canonical metadata, authors, date, DOI, abstract, and locators.
- https://arxiv.org/html/2408.02882 - verified full-paper evidence for threat model, experiments, countermeasures, and limitations; local copy withheld.
- https://arxiv.org/pdf/2408.02882 - verified PDF; local copy withheld.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics - related forensic evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260715-Control%20Surfaces - related control-placement evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Memory%20Defense%20Layers - related layered-memory defense evidence.
- Source files: PDF, official full-paper HTML, metadata HTML, and integrity records; all withheld locally.
