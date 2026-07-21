# Report-Mark: Stealth Memory Injection

- Deployment job ID: `BLAD-MANUAL-20260721-260705189`
- Deployment item ID: `BLAD-MANUAL-20260721-260705189-P01`
- Review date: 2026-07-21
- Selection: explicit user-supplied arXiv record; no random draw
- Scope: defensive security analysis only

## Source Metadata

| Field | Value |
|---|---|
| Paper | *When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents* |
| Authors | Yechao Zhang; Shiqian Zhao; Jiawen Zhang; Jie Zhang; Gelei Deng; Xiaogeng Liu; Chaowei Xiao; Tianwei Zhang |
| Identifier | arXiv:2607.05189v1; DOI:10.48550/arXiv.2607.05189 |
| Submitted | 2026-07-06 |
| Subjects | cs.CR; cs.AI |
| Record | https://arxiv.org/abs/2607.05189v1 |
| Full paper | https://arxiv.org/html/2607.05189v1 |
| PDF | https://arxiv.org/pdf/2607.05189v1 |
| Source state | Complete 25-page PDF, full-paper HTML, abstract HTML, and source archive verified; all source files withheld locally. |
| Deployment IDs | `BLAD-MANUAL-20260721-260705189`; `BLAD-MANUAL-20260721-260705189-P01` |

## Concise Research Notes

The paper studies a one-shot, black-box email attack against persistent personal agents. A malicious message is intended to cause a durable memory write, suppress obvious user-facing evidence, and influence a later session. WhisperBench supplies 108 synthetic cases across five risk categories, with 52 training cases and 56 held-out cases. MemGhost trains a Qwen 4B attacker policy with supervised fine-tuning and GRPO using environment and objective proxies. Operational payloads and attack-construction details are omitted here.

The strongest reported background end-to-end rates for MemGhost are 91.1% on Grok 4.1, 87.5% on GPT-5.4, and 80.4% on Claude Sonnet 4.5. Foreground interaction changes the failure profile rather than uniformly preventing it: GPT-5.4 remains at 75.0% E2E, while MiniMax M2.5 reports 98.2% injection but only 21.4% stealth and E2E. Transfer tests across OpenClaw, NanoClaw, Hermes, and Mem0-backed configurations report background E2E between 80.4% and 87.5% when using GPT-5.4.

These are controlled, author-reported results. Query-based baselines use a 20-case subset rather than the main 56-case held-out set; confidence intervals and independent main-run seeds are not reported; no real users are involved; and code, data, checkpoints, and exact executable configurations were not publicly linked as of 2026-07-21. The source also contains an ESR denominator ambiguity, an unfinished limitations sentence, and a mismatch between the arXiv comment's eight figures and the document's ten numbered figures.

The defensive conclusion is to separate memory storage from authority. Untrusted content can remain searchable for context or forensics while being quarantined from preference mutation and privileged actions. Provenance-bearing writes, memory-diff receipts, expiration and revocation, independent confirmation, action-time evidence checks, and append-only lineage address the mechanism more directly than a single content classifier.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Complete Sections I-VIII and Appendices A-G | Threat model, benchmark, method, results, limitations, rubrics, ethics, and disclosures | Experiments and code were not rerun |
| Table I | Model-specific ISR, SSR, ESR, and E2E results in background and foreground settings | Endpoint and harness conditioned; no confidence intervals |
| Table II | Transfer across agent runtimes and memory backends | Uses GPT-5.4 throughout; historical runtime versions not independently reconstructed |
| Table III | Positive proxy-to-outcome correlations | Association does not establish universal proxy validity |
| Tables IV-V | Defense evasion and adaptive visibility | Thresholds, versions, and small controlled samples limit generality |
| Tables VI-VII, source equations, and appendices | Platform-environment proxy tools, training hyperparameters, and evaluation-rubric detail | No public executable artifact was linked |
| Source consistency audit | Metric ambiguity and editorial defects | Editorial issues do not directly refute measured outcomes |

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260717-FARMA Reasoning Poison/README.md` - forged reasoning and provenance-aware quarantine for retained agent state.
2. `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md` - architecture-layer controls, memory authority, and evaluation-validity criteria.
3. `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` - trace evidence and incident reconstruction for persistent-memory poisoning.

## Synthesis Note

### Concept Bridge

MemGhost targets the transition from untrusted correspondence to durable state. FARMA shows a related route through forged reasoning; Memory Defense Layers asks where controls can actually observe and interrupt persistent state; Agent Memory Forensics asks what evidence remains after the fact. Together they imply that provenance is useful only when write, retrieval, and action authority enforce it.

### Potential Implementations

1. Add a provenance-bearing memory gateway that defaults external-message extractions to quarantined, non-authorizing state.
2. Produce signed memory-diff receipts with approve, restrict, expire, and revoke controls for every durable update.
3. Require action-time evidence bundles and independent confirmation before a retrieved memory can support a high-impact tool call.

### Deeper Relationship Observations

1. A system can suppress visible evidence at ingestion while retaining sufficient internal evidence to change a later action.
2. Detection and authorization solve different problems: a weak detector can coexist with a strong fail-closed authority boundary.
3. Cross-session security requires lineage from source message through extraction, storage, retrieval, planning, tool execution, and revocation.

### Conceptual Similarities

1. All three related DEPs treat persistent state as potentially adversarial rather than inherently trusted.
2. All favor layered controls and evidence-bearing decisions over a universal text classifier.
3. All separate a model's apparent conversational compliance from downstream system integrity.

### MVP Implementations with Code Mock-Ups

1. Quarantine untrusted writes.

```python
record = memory.propose(value, provenance=source_receipt)
record.authority = "search_only" if not source_receipt.trusted else "review_required"
```

2. Require independent approval for sensitive state.

```python
if proposal.affects_sensitive_action:
    approval = approvals.require_independent_channel(proposal.digest)
    memory.commit(proposal, authority="action", approval=approval)
```

3. Enforce evidence at tool invocation.

```python
evidence = lineage.for_plan(plan)
policy.authorize(plan.required_capabilities, evidence=evidence, fail_closed=True)
```

### Developer Challenges

1. Preserving normalized provenance across mail parsing, summarization, memory storage, retrieval, and tool execution.
2. Designing user review that remains usable while exposing every consequential durable-state change.
3. Evaluating adaptive attacks without retaining or distributing reusable offensive payloads.

### Author Challenges

1. Releasing enough code, data, endpoint metadata, and traces for exact replication while protecting users and limiting misuse.
2. Normalizing baseline case sets, metric denominators, seeds, thresholds, and uncertainty reporting.
3. Extending evidence to long horizons, real organizations, multi-agent sharing, multimodal messages, and upstream mail defenses.

## Validation Notes

- Explicit user selection was recorded; no random selection claim is made.
- Duplicate exclusions: 0; reselections: 0; one existing complete source bundle was reused with zero network downloads.
- Complete-source gate passed for PDF, full-paper HTML, abstract HTML, and source archive.
- Full main-text, appendix, table, figure, equation, ethics, and disclosure coverage was recorded.
- Exactly three related entries and three items in each required synthesis subsection are present.
- Exactly three fenced code mock-ups are present.
- Public allowlist contains generated Markdown and the deduplication JSON only; source documents and private evidence remain local.
- Defensive scope was enforced; operational attack prompts, payloads, and procedures are absent.

## Attribution Block

- https://arxiv.org/abs/2607.05189v1 - canonical v1 metadata, authors, date, subjects, abstract, and locators.
- https://arxiv.org/html/2607.05189v1 - complete full-paper evidence for method, experiments, results, limitations, appendices, and disclosures; local copy withheld.
- https://arxiv.org/pdf/2607.05189v1 - complete 25-page source document verified locally and withheld.
- https://doi.org/10.48550/arXiv.2607.05189 - canonical DOI resolver.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/DEP-A-20260717-FARMA%20Reasoning%20Poison - related forged-reasoning and memory-provenance analysis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Memory%20Defense%20Layers - related architecture-layer defense analysis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics - related forensic analysis.
- Source files: PDF, full-paper HTML, metadata HTML, source archive, extracted text, renderings, and integrity records; all withheld locally.
