---
title: "Memory Depth - DEP-E"
generated_at: "2026-07-19T00:04:48Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of selective parametric consolidation for durable goal-conditioned behavior in long-running language agents."
source_status: "URLs only in public deposit; main paper and ancillary supplement inspected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "Sources inspected through 2026-07-19; primary work pinned to arXiv v1"
primary_url: "https://arxiv.org/abs/2606.26806"
stable_identifier: "arXiv:2606.26806v1; DOI 10.48550/arXiv.2606.26806"
confidence_summary: "High for reporting the inspected protocol and tables; medium for generalization because the protocol is synthetic and no code or experiment was executed."
safety_scope: "authorized research, synthetic evaluation, privacy-preserving memory governance"
distribution_notes: "No paper, supplement, repository clone, dataset, or model artifact is redistributed; public URLs and repository-relative provenance only."
---

# Memory Depth - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Memory Depth, Not Memory Access* arXiv record | Primary metadata | HTML | arXiv:2606.26806v1; DOI 10.48550/arXiv.2606.26806 | https://arxiv.org/abs/2606.26806 | arXiv perpetual non-exclusive license is linked from the record | 2026-07-19 | Inspected |
| S2 | Complete paper HTML | Primary full text | HTML | arXiv:2606.26806v1 | https://arxiv.org/html/2606.26806 | Public arXiv rendering; some equations lose symbols in extraction | 2026-07-19 | Inspected end to end |
| S3 | Main paper PDF | Primary full text | PDF, 6 pages | arXiv:2606.26806v1 | https://arxiv.org/pdf/2606.26806 | Inspected; not redistributed | 2026-07-19 | Text and layout inspected |
| S4 | EVAF supplementary material | Primary ancillary evidence | PDF, 5 pages | `EVAF_supplement.pdf` for arXiv v1 | https://arxiv.org/src/2606.26806v1/anc/EVAF_supplement.pdf | Official ancillary file; inspected temporarily and not redistributed | 2026-07-19 | Every page rendered and inspected; text extracted |
| S5 | Selected source DEP | Primary discovery artifact | Markdown | DEP-20260628-Tech Intel 0102 | `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/README.md` | Repository artifact | 2026-07-19 | Inspected |
| S6 | Selected daily findings | Primary discovery artifact | Markdown | finding 2 of DEP-20260628-Tech Intel 0102 | `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md` | Generated research queue; claims rechecked against S1-S4 | 2026-07-19 | Inspected in full |
| S7 | Prior Tech Intel review | Prior processed artifact | Markdown | DEP-E-20260708-Tech Intel Review | `Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md` | Prior abstract-level treatment of the same paper | 2026-07-19 | Inspected; explicitly superseded in depth, not removed |
| S8 | HERMES World Model context | Prior processed artifact | Markdown | DEP-E-20260712-HERMES World Model | `Black-Lake/.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` | Latest prior DEP-Class context linked to the selected source DEP | 2026-07-19 | Inspected in full for iterative continuity |

The primary work is authored by Haoliang Han of the Institute of Biomedical Strategy, China Pharmaceutical University. It was submitted to arXiv on 2026-06-25 and was available only as v1 in the inspected record. The arXiv page exposes no official code-repository URL. The supplement refers to a merged repository and names repository-relative scripts and result files, but the repository itself was not locatable from the inspected primary record; reproducibility claims are therefore bounded to the paper's artifact inventory rather than a public code audit.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Author, affiliation, v1 date, abstract, DOI, subjects, license link, ancillary-file presence | Work identity, version, headline claims, source availability | High | Metadata and abstract are not enough for experimental verification |
| E2 | S2, S3 | Primary paper | Definitions, EVAF gate, actuation controllers, loop-drift protocol, Tables 1-4, limitations, related work | Access/depth distinction, mechanism, main metrics, boundary claims | High for reporting | Author-reported; no independent rerun |
| E3 | S4 | Primary supplement | Protocol constants, Tables 1-11, seed-level matched gates, fixed-inner audits, Memora statistics, negative results, reproducibility paths | Exact audit values, selection/actuation factorization, contamination and deletion boundaries | High for reporting | Repository files named by the supplement were not publicly located or executed |
| E4 | S5, S6 | Repository discovery evidence | DEP identity, ten-paper pool, original finding and source URLs | Selection provenance and why this paper was expanded | High | Original finding is a summary, not evidence for final technical claims |
| E5 | S7 | Prior processed artifact | Explicit abstract-only evidence boundary for this paper | What is new in this pass | High | Prior entry derives from another source DEP and did not inspect full text |
| E6 | S8 and its log/Report-Mark/README | Prior processed context | Latest prior DEP-Class context connected to the selected source DEP | Iterative continuity and source-thread relationship | Medium | HERMES does not validate EVAF |
| E7 | Repository marker scan and random draws | Process evidence | 63 canonical candidates, 58 same-family files, strict 24-hour cutoff, two uniform PowerShell draws | Eligibility and selection claims | High | Randomness is operational rather than cryptographically auditable |

## Executive Summary

*Memory Depth, Not Memory Access* argues that a long-running agent needs two distinct memory properties. Retrieval supplies **access** to stored facts by reinserting text. Parametric consolidation supplies **depth** when prior experience continues to shape behavior after working context is unloaded and without retrieving the relevant text. The paper operationalizes that distinction with a synthetic loop-drift protocol and evaluates EVAF, a surprise- and valence-gated LoRA write mechanism.

The main result is a task-dependent “depth flip,” not a universal memory win. Across four-seed GPT-2 and TinyLlama runs with 10 synthetic users and 200 events per user, RAG is best at short factual recall: 0.956 for GPT-2 and 0.973 for TinyLlama. EVAF is deliberately weak on that layer, but reports goal persistence/post-unload recovery of 0.904/0.900 on GPT-2 and 0.833/0.812 on TinyLlama while triggering only about 2.4-2.6 buffer consolidations per 200 events. Naive LoRA writes every event and does not match EVAF on the goal layer. Routed EVAF+RAG demonstrates complementarity but also model-specific tradeoffs.

The more important mechanistic result is that selective consolidation has two controls: **selection**, which events enter the write buffer, and **actuation**, how strongly the selected buffer changes the adapter. A matched random gate shows a positive semantic-selection effect on GPT-2 but mixed evidence on TinyLlama. Mistral-7B then shows why the two controls cannot be collapsed: under the original five-step actuation, random matched writes outperform EVAF on goal/post-unload, while weaker fixed-inner actuation restores EVAF behavior. Strong actuation can also saturate sibling contamination, so goal persistence alone is unsafe as an optimization target.

The paper and supplement are unusually candid about negative evidence. Held-out paraphrase does not establish broad semantic generalization; the public Memora stale-memory diagnostic is directionally positive but not significant; balanced forgetting variants cost more writes and drift without robust improvement; and no complete deletion/update-valid memory system is claimed. Reviewer confidence is high for reporting the source tables and medium for generalization. The practical implication is an evaluation and governance design: combine retrieval with opt-in, tightly scoped parametric writes only when selection quality, actuation calibration, contamination, invalidation, privacy, and rollback are all measured.

## Detailed Summary

### Problem and Vocabulary

Retrieval systems answer “what can be fetched?” They keep model parameters fixed, store past text externally, and reintroduce selected records at inference time. That is appropriate for recent or explicit factual access. The paper defines memory depth as a different property: a durable goal-conditioned tendency that survives interference and context unload, then affects choices without reinserting the original record.

The distinction is intentionally narrower than “better memory.” Four probe layers are separated: short factual access, old/noisy factual access, goal persistence, and post-unload goal recovery. The RAG index survives context unload, so a retrieval loss cannot be blamed on deleting the store. Instead, the protocol asks whether an agent's behavior changes when the relevant goal is not inserted into its current prompt.

### EVAF Selection Gate

For each event, EVAF combines token-level surprise with valence: embedding similarity to the user's durable goal and preferences. Sigmoid-transformed surprise and valence scores are multiplied. Events above a write threshold enter a buffer. When four events accumulate, the mechanism updates a LoRA adapter using the buffer plus four replay samples and an L2 anchor to the original adapter.

The supplement pins the main constants: gate slopes 1.0 and 10.0, valence/write thresholds 0.5 and 0.5, LoRA rank 32 and alpha 16, RAG top-k 3, and five default inner LoRA steps. Model-specific learning rates are 5e-3 for GPT-2 124M, 2e-3 for TinyLlama 1.1B, and 2e-4 for Mistral 7B. Absolute LoRA L2 values are not comparable across model families because model geometry, dtype, embedding source, and learning rate differ.

### Selection and Actuation

Selection determines which experiences deserve a parametric imprint. Actuation determines the magnitude of that imprint. They are separable controls but coupled online: selection triggers a write, while the changed adapter alters the surprise scores that govern later selections. Mistral makes this feedback visible. In its four-seed audit, reducing inner steps from five to one increases mean consolidation triggers from 3.9 to 9.4, consistent with weaker individual writes leaving future similar events surprising enough to pass the gate.

Fixed-inner controllers use the same EVAF gate but vary one, two, or three inner steps. A behavior-margin controller is also reported, but the paper explicitly treats it as an engineering proof of concept because Mistral variance is high. Routed EVAF+RAG sends factual probes to retrieval and goal probes to the adapter; it is a complementarity check rather than the core mechanism claim.

### Loop-Drift Protocol

Each run has 10 synthetic users and 200 events per user. Four seeds are used: 42, 0, 1, and 2. The event mixture is 45% stable goal/preference reinforcement, 25% off-topic distractors, 10% transient opposite requests, 10% conflicts, and 10% sibling-user contamination. Long facts are injected at steps 6, 9, and 12, then buried under same-key noise. Short facts appear five steps before a probe. Probes run every 20 steps; context unload occurs every 50 steps and clears working context but not the RAG index.

The evaluated methods are Frozen, Summary, RAG, Naive-LoRA, EVAF, and Routed EVAF+RAG. Higher scores are better for factual, goal, post-unload, and held-out probes. Lower scores are better for contamination, transient overwrite, memory tokens, write count, and adapter drift. A “write” is one buffer-consolidation trigger, not one gradient step.

### Main Depth-Split Results

On TinyLlama, RAG reports short/long fact scores of 0.973/0.660 but goal/post-unload of 0.396/0.394. EVAF reports 0.483/0.565 on facts and 0.833/0.812 on goal/post-unload, with 2.625 mean writes. Routed EVAF+RAG restores short fact to 0.975 but lowers goal/post-unload to 0.773/0.750. Naive-LoRA writes 200 times yet reaches only 0.623/0.575 on goal/post-unload and exhibits much higher drift.

On GPT-2, RAG reports short/long fact scores of 0.956/0.733 and goal/post-unload of 0.398/0.394. EVAF reports 0.463/0.558 on facts and 0.904/0.900 on goal/post-unload, with 2.4 mean writes. Routed EVAF+RAG reaches 0.935 short fact and 0.927/0.925 goal/post-unload. These values support a division of labor within the synthetic protocol: retrieval is appropriate for explicit access; selective parametric consolidation is appropriate for held-in goal-conditioned depth.

### Matched-Gate and Actuation Controls

The matched random gate preserves EVAF's write counts and online feedback but admits random events. GPT-2 EVAF beats the random gate on goal and post-unload in all four listed seeds. TinyLlama is mixed, demonstrating that sparse writing alone is not enough and that semantic selection does not guarantee useful behavior under an arbitrary actuation setting.

At Mistral-7B, the original five-step controller produces an inversion: EVAF averages 0.362 goal and 0.312 post-unload, while the random matched gate averages 0.688/0.681. EVAF nevertheless has lower sibling contamination, 0.787 versus 0.825. The fixed-inner audit explains the inversion as miscalibrated actuation. Audit-5 reports 0.354/0.306 goal/post; Fixed-2 recovers to 0.796/0.775; Fixed-1 reaches 0.919/0.938. Yet Fixed-1 contamination is 1.000 across all four seeds, saturating the probe. The narrow supported conclusion is factorization and calibration, not that one-step updates solve memory at scale.

### Negative Results and Memora Boundary

Held-out tendency is not a load-bearing success. TinyLlama EVAF is directional at 0.554 plus or minus 0.10; GPT-2 EVAF is 0.483 plus or minus 0.06. The paper therefore claims held-in goal-conditioned persistence, not robust paraphrase generalization.

Public Memora streams introduce memory mutation and stale evidence absent from append-only loop drift. On the full population, EVAF changes forgetting absence from Frozen's 91/222 (0.410) to 95/222 (0.428). On the pre-registered high-mutation slice, it changes 49/126 (0.389) to 52/126 (0.413). The reported McNemar test is p=0.359 with a 95% confidence interval of [-0.079, 0.167], so the result is not significant. A balanced EVAF forgetting variant costs 51 writes and L2 drift 70.0, but does not robustly improve over vanilla EVAF. The source concludes that negative cross-entropy and anti-training suppress text rather than represent validity; deletion likely needs tombstones, validity gating, or reconsolidation.

### Reproducibility Boundary

The supplement names `results/MERGE_MANIFEST.md`, `scripts/loop_drift/loop_drift_bench.py`, `matched_gate_ablation.py`, `adaptive_margin_ablation.py`, and `aggregate_fixed_inner_controls.py` as starting points for reproducing paper tables. It also says a legacy held-out aggregation helper was intentionally excluded because of stale metric-key mismatches. That transparency improves the audit trail, but the inspected arXiv record did not expose a public repository URL. No code, seed JSON, manifest, model, dataset, or result file was executed in this pass.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Memory access and memory depth are distinct evaluation targets. | Author conceptual claim | E2 | The protocol operationalizes a useful distinction, but it is one proposed taxonomy rather than a universal definition. | High for conceptual clarity |
| C2 | RAG owns shallow factual access in loop drift. | Author empirical claim | E2, E3 | Supported by 0.956-0.973 short-fact scores and the durable-index control. | High for reported protocol |
| C3 | EVAF owns held-in goal persistence/post-unload depth in GPT-2 and TinyLlama main runs. | Author empirical claim | E2, E3 | Supported by 0.812-0.904 EVAF scores with about 2-3 writes; does not establish broad semantic or real-world persistence. | High for tables; medium beyond protocol |
| C4 | Semantic selection matters beyond sparse writing. | Author mechanism claim | E2, E3 | Positive in all GPT-2 seeds, mixed on TinyLlama, and inverted on Mistral under miscalibrated actuation. The qualified claim is model/controller dependent. | Medium-high |
| C5 | Actuation is a separable, model-dependent control factor. | Author mechanism claim | E2, E3 | Fixed-inner grids strongly support this claim across three model families. | High for reported audits |
| C6 | Selection and actuation interact through asymmetric online feedback. | Author mechanism interpretation | E2, E3 | Monotonic Mistral write-count changes are consistent with feedback, but the internal causal path was not independently instrumented. | Medium-high |
| C7 | EVAF solves stale-memory invalidation. | Unsupported claim explicitly rejected by source | E2, E3 | Memora is non-significant; balanced forgetting variants do not provide a robust win. | High confidence that this must not be claimed |
| C8 | Goal persistence alone is an unsafe optimization target. | Reviewer interpretation | E3 | Mistral Fixed-1 reaches high goal/post while contamination saturates at 1.000, motivating multi-objective gates. | High within audit |
| C9 | This pass materially expands prior Black Lake coverage of the paper. | Process/reviewer claim | E4, E5, E6 | Prior entry was abstract-only; this pass inspected complete HTML, main PDF, ancillary PDF, exact tables, negative evidence, and reproducibility paths. | High |

## Methodology

- `Research objective`: Expand one randomly selected Black-Lake-Data DEP source into a full, schema-complete DEP-E manuscript while preserving evidence, prior-artifact continuity, and public-safe provenance.
- `Sources inspected`: The selected DEP README and daily findings; prior Tech Intel, HERMES, and related operational artifacts; live repository READMEs; canonical arXiv metadata; complete paper HTML; the six-page main PDF; and every page of the five-page official ancillary supplement.
- `Discovery strategy`: Fetched both repositories, enumerated canonical source DEPs, scanned reports/logs/Report-Marks/prior artifacts for the shared automation family, drew uniformly from the eligible set with PowerShell `Get-Random`, inspected prior material, then drew uniformly from the selected DEP's ten primary papers.
- `Inclusion criteria`: Evidence was included when it established source identity, protocol design, quantitative results, negative evidence, reproducibility boundaries, repository rules, selection provenance, or concrete related-work context.
- `Exclusion criteria`: Search-result summaries, unrelated Memora products/datasets, and non-authoritative commentary were excluded. No code or dataset was treated as available without a public locator.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Main claims are mapped to evidence IDs; author claims, reviewer interpretation, process claims, and rejected overclaims are labeled separately. Exact numerical values come from inspected paper/supplement tables.
- `Uncertainty handling`: Synthetic-protocol scope, missing public code locator, non-reproduction, weak paraphrase transfer, contamination, and non-significant stale-memory results remain explicit.
- `Extraction process`: arXiv HTML was inspected end to end; the main PDF supplied formulas and page-layout checks; the ancillary PDF was rendered page by page and its text extracted to cross-check Tables 1-11.
- `Version control`: The work is pinned to arXiv:2606.26806v1. No later revision or public repository commit was available from inspected sources.
- `Claim selection`: Priority went to the access/depth split, protocol controls, exact main metrics, selection/actuation factorization, negative evidence, privacy implications, and reproducibility boundary.
- `Cross-checking`: Abstract values were reconciled with main and supplemental tables. HTML extraction omissions were checked against PDF text/layout. Prior Black Lake coverage was compared to identify new material.
- `Safety handling`: Implementation ideas use synthetic streams, local evaluation, explicit consent, reversible adapters, and no covert personalization.
- `Reviewer stance`: Critical paper report, iterative literature expansion, DEP-ready preservation, safe product translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's conceptual split, EVAF mechanism, loop-drift design, main results, audits, negative evidence, Memora boundary, related work, and safe implementation implications.
- `Temporal boundary`: Sources inspected through 2026-07-19; primary work pinned to v1 submitted 2026-06-25.
- `Evidence limits`: No repository clone, code execution, seed replay, model download, dataset audit, hardware run, or independent statistical reproduction occurred. The exact public Memora event-stream locator and merged code repository were not exposed by inspected primary sources.
- `Assumptions`: The arXiv HTML, main PDF, and official ancillary PDF describe the same v1 evidence package. Table extraction is accurate where reconciled visually and textually.
- `Constraints`: Any durable per-user parametric write raises privacy, consent, cross-user contamination, deletion, and rollback concerns. Public artifacts exclude private paths and temporary source locations.
- `Out of scope`: Production personalization, covert preference learning, medical or legal decision support, universal memory benchmarking, and claims of complete deletion/update validity.
- `Intended use`: Research review, DEP deposition, benchmark design, memory-governance planning, safe prototype evaluation, and follow-on replication.
- `Audience`: Agent-memory researchers, long-running agent engineers, privacy/security reviewers, evaluation teams, and Black Lake maintainers.
- `Depth target`: Full manuscript with table-level evidence and negative-result preservation.
- `Reproducibility boundary`: Exact reproduction requires a publicly locatable merged repository, pinned dependencies/models/data, seed JSONs, and expected outputs; those were not available in this run.
- `Operational boundary`: Parametric writes should remain opt-in, isolated, inspectable, reversible, and subordinate to explicit external records until invalidation is solved.
- `Data sensitivity`: The inspected research is public; any real deployment would process personal behavioral data and must be treated as sensitive.

## Observations

- `Observed pattern`: The strongest evidence is not the raw EVAF score but the change in winner across probe depth under a durable retrieval index.
- `Observed mechanism`: Mistral's write count rises as inner steps fall, making actuation-to-future-selection feedback empirically visible.
- `Observed tradeoff`: High goal persistence can coexist with severe sibling contamination; Mistral Fixed-1 saturates the contamination probe.
- `Negative evidence`: Held-out paraphrase and stale invalidation fail to support broad memory-generalization claims.
- `Technical implication`: A memory controller needs at least four axes: factual access, goal depth, contamination/selectivity, and validity/forgetting.
- `Governance implication`: Parametric memories are harder to inspect, revoke, and attribute than external records. Retrieval remains the safer default for facts and mutable personal data.
- `Cross-DEP pattern`: The prior abstract-level Tech Intel review correctly identified EVAF as an expansion seed; this pass replaces unverified summary metrics with paper/supplement traces while preserving that provenance.
- `Open question`: Can validity-gated reconsolidation preserve post-unload behavior while guaranteeing user-level deletion and limiting sibling contamination?
- `Reviewer hypothesis`: A reversible adapter ledger with signed event provenance and a deletion tombstone gate will matter more operationally than another small increase in goal-persistence score.

## Considerations

Parametric consolidation changes model behavior using user-derived events. That can encode durable preferences without a transparent record, create cross-user leakage, and resist deletion after a user revokes consent. A production design should not infer “durable goals” from ambient conversation and silently fine-tune. Writes should require an explicit scope, purpose, owner, retention period, provenance record, and rollback path.

Evaluation must be multi-objective. Optimizing goal persistence alone can overfit stable goals, mis-handle transient reversals, or contaminate sibling users. Every write controller should report factual recall, goal/post-unload behavior, transient overwrite, cross-user contamination, drift, write counts, privacy/consent status, invalidation success, and rollback fidelity.

The paper's synthetic protocol is appropriate for isolating a mechanism, but deployment claims need naturalistic streams, adversarial preference conflicts, multilingual paraphrases, consent changes, deletion requests, model upgrades, and failure-recovery tests. Personalization quality is not equivalent to user benefit: a system can faithfully preserve an outdated, harmful, or misattributed goal.

The source package is also a reproducibility caution. The supplement names scripts and result files but the arXiv record does not expose their repository. A future review should locate an author-controlled release, pin a commit, verify licenses for models and event streams, and reproduce one table before treating EVAF as implementable.

## Strengths

- The access/depth distinction is precise and makes baseline expectations falsifiable.
- The RAG index survives context unload, preventing a trivial “retrieval was erased” explanation.
- Synthetic event composition and probe timing are disclosed in enough detail to understand the intended mechanism.
- Main results preserve negative tradeoffs rather than claiming EVAF wins every memory task.
- Matched random gates isolate semantic selection from write sparsity.
- Fixed-inner audits isolate actuation strength and expose model-specific calibration.
- Four-seed Mistral controls replace a weaker single-seed scale story.
- The supplement publishes full aggregate and seed-level tables, explicit claim boundaries, and named reproduction paths.
- Memora is framed as a non-significant boundary diagnostic, not a benchmark victory.

## Weaknesses

- The main loop-drift protocol is synthetic and small: 10 users, 200 events, and four seeds per main model.
- Continuation-score probes do not establish useful behavior in open-ended agent tasks.
- Broad paraphrase generalization is not supported.
- Stale-memory deletion/update validity remains unsolved.
- High actuation can produce unacceptable sibling contamination.
- Only GPT-2, TinyLlama, and Mistral-7B are tested; scale behavior is not monotonic or complete.
- Model-specific learning rates, embedders, and adapter geometries complicate cross-family comparison.
- The behavior-margin controller is high variance on Mistral and not load-bearing.
- No public code-repository URL or commit pin was exposed by inspected primary sources.
- This review did not execute code or independently reproduce the statistics.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add explicit validity and tombstone state | Forgetting/update | Anti-training suppresses text rather than represents invalidity | Auditable deletion and stale-memory rejection | More state and policy complexity | Mutation suites with verified deletion and no resurrection |
| Optimize a Pareto objective | Controller calibration | Goal depth alone can saturate contamination | Safer balance among persistence, selectivity, drift, and write cost | Harder tuning and threshold governance | Pre-register acceptable fronts by model/user slice |
| Use opt-in typed goal records | Privacy/provenance | Inferred valence can misidentify durable goals | Clear consent, scope, and attribution | More user friction | Human confirmation and revoke/rollback acceptance tests |
| Expand naturalistic and multilingual probes | Generalization | Held-out paraphrase is weak | More realistic evidence for semantic transfer | Higher annotation cost and privacy risk | Public/synthetic benchmark with language and paraphrase slices |
| Add model-upgrade portability tests | Operations | LoRA memories may not transfer across base versions | Safer maintenance and migration | Adapter incompatibility | Migrate, replay, and compare behavior/contamination across versions |
| Publish a pinned reproduction bundle | Reproducibility | Named scripts without a public locator are insufficient | Independent table verification | Maintenance and model-license burden | Clean-room reproduction of Tables 4-10 from one commit |
| Add privacy attacks and leakage tests | Security | Parametric memories can encode sensitive events | Evidence for isolation and safe retention | Dual-use and disclosure risks | Authorized canary, membership, and cross-user extraction tests |

## Potential Implementations

1. `Memory-Depth Benchmark Harness`
   - `User`: Agent-memory researchers and evaluation teams.
   - `Goal`: Separate factual access, durable goal behavior, contamination, and invalidation in one deterministic report.
   - `Core mechanism`: Generate synthetic typed event streams, retain the retrieval index across unload, run matched probes, and compare external-store, adapter, and routed methods.
   - `Required inputs`: Synthetic personas, typed goals, fact schedules, distractors, model adapters, retrieval configuration, and seed manifest.
   - `Outputs`: Metric tables, confidence intervals, write/drift ledgers, invalidation failures, and provenance hashes.
   - `Risk controls`: Synthetic inputs, local execution, no real user histories, bounded models, and explicit non-production labeling.
   - `Evaluation`: Reconcile the paper's table arithmetic, then add deletion and contamination fixtures.

2. `Consent-Bound Dual-Store Memory`
   - `User`: Teams building long-running assistants for opt-in, non-sensitive workflows.
   - `Goal`: Combine retrieval for explicit/mutable facts with reversible parametric tendencies for user-confirmed durable preferences.
   - `Core mechanism`: Route typed factual queries to an external store; admit only confirmed goal events to a per-user adapter; gate writes by contamination, drift, validity, and rollback tests.
   - `Required inputs`: Signed user confirmations, event provenance, purpose/retention policy, external memory store, isolated adapter, and deletion ledger.
   - `Outputs`: Retrieved records, scoped behavioral bias, audit trail, and revocation evidence.
   - `Risk controls`: Explicit consent, per-user isolation, no covert inference, encryption, adapter snapshots, tombstones, hard deletion, and human override.
   - `Evaluation`: Post-unload goal tests plus factual accuracy, cross-user canaries, revoke/rollback tests, and privacy review.

3. `Actuation Calibration Auditor`
   - `User`: ML engineers reviewing online or periodic adapter updates.
   - `Goal`: Prevent over-actuation and contamination before a controller is enabled.
   - `Core mechanism`: Replay a fixed selected buffer across inner-step/LR grids, measure goal movement, contamination, drift, future write counts, and rollback fidelity, then reject dominated settings.
   - `Required inputs`: Approved synthetic buffer, adapter snapshots, probe suite, actuation grid, and safety thresholds.
   - `Outputs`: Pareto frontier, rejected regimes, calibration recommendation, and signed audit report.
   - `Risk controls`: Offline-only, no production weights, no personal data, strict resource caps, and automatic rollback.
   - `Evaluation`: Detect the Mistral-style inversion and contamination saturation in known fixtures.

## Three Ways to Exercise This Research

1. `Reconcile the published tables`: Objective - verify the depth flip and audit arithmetic. Inputs - the main PDF and ancillary tables. Method - transcribe the GPT-2, TinyLlama, Mistral, and Memora rows into a typed ledger; recompute differences and confidence-bound statements. Output - a signed Markdown/CSV metric map. Success criterion - every headline value and negative claim resolves to a table cell. Stop condition - any incompatible run or ambiguous denominator is kept separate rather than averaged.
2. `Build a synthetic actuation sweep`: Objective - test whether selection and write strength factorize in an authorized toy setting. Inputs - synthetic users, a small open model, one adapter, fixed selected buffers, and one/two/three-step controllers. Method - replay identical buffers, measure goal/post-unload, contamination, writes, and drift, and include null/random gates. Output - a Pareto report. Success criterion - results are deterministic enough to identify dominated regimes without using real user data. Stop condition - contamination or drift exceeds the pre-registered bound.
3. `Prototype deletion-first memory`: Objective - test validity gating before optimizing persistence. Inputs - synthetic create/update/delete events, external records, reversible adapter snapshots, and tombstones. Method - confirm a goal, consolidate it, issue an update/delete, unload context, and test both non-resurrection and unrelated-memory retention. Output - a deletion evidence ledger. Success criterion - deleted content cannot reactivate through retrieval, adapter behavior, or replay. Stop condition - any deletion failure blocks further personalization testing.

## Example MVP Product

- `Product name`: DepthGate Memory Auditor.
- `Target user`: Research and privacy teams evaluating memory controllers for long-running agents.
- `Problem`: Standard recall benchmarks do not show whether an agent preserves goals after unload, contaminates other users, or can delete stale behavior.
- `Core workflow`: Import a synthetic event manifest; run external-store, adapter, and routed baselines; unload working context while retaining retrieval; compute access/depth/contamination/invalidation metrics; sweep approved actuation settings; export a signed evidence bundle.
- `Data requirements`: Synthetic personas and events, typed goal/fact/update/delete labels, fixed seeds, model and adapter pins, retrieval configuration, and acceptance thresholds. Real user histories are excluded from the MVP.
- `Architecture`: Local CLI, deterministic stream generator, adapter sandbox, retrieval baseline, probe runner, metric library, policy file, and Markdown/JSON report generator.
- `Success metrics`: Exact fixture reconciliation; deterministic reruns; zero cross-user canary leakage; complete event provenance; successful update/delete fixtures; and no accepted setting outside contamination/drift bounds.
- `Risk controls`: Local-only, synthetic data, no production model writes, explicit resource caps, per-run adapter reset, signed provenance, and automatic rejection/rollback.
- `Limitations`: Cannot establish real-world personalization quality, user benefit, safety, privacy compliance, or scale behavior; depends on the realism of synthetic probes.
- `MVP boundary`: Evaluation and evidence packaging only; no live assistant integration, background learning, or real-user adapter persistence.
- `Deployment model`: Local CLI or isolated batch job.
- `Evaluation plan`: Unit-test metric directions and unload semantics; replay paper-derived fixtures; add contamination and deletion failures; conduct an independent privacy review.
- `Failure modes`: Hidden retrieval deletion, prompt leakage across users, nondeterministic adapter updates, metric-key mismatches, stale replay, and false confidence from small seeds.
- `Maintenance plan`: Version event schemas, models, seeds, metric definitions, thresholds, and expected-output fixtures; require review for every controller change.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents | Primary paper | **Expanded in this pass:** complete method, loop-drift protocol, main results, mechanism controls, limitations, and references were inspected. | https://arxiv.org/abs/2606.26806; https://arxiv.org/html/2606.26806; https://doi.org/10.48550/arXiv.2606.26806 |
| EVAF supplementary material | Primary ancillary evidence | **New in this pass:** all five pages and Tables 1-11 were inspected for exact constants, aggregate/seed-level results, negative evidence, contamination, Memora statistics, and reproduction paths. | https://arxiv.org/src/2606.26806v1/anc/EVAF_supplement.pdf |
| Selected source DEP finding | Repository research artifact | Original finding 2 and ten-paper expansion pool; the paper was selected uniformly from this pool. | `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md` |
| Tech Intel Agent Systems Review | Prior Black Lake artifact | Prior abstract-level treatment of arXiv:2606.26806; **this pass newly adds full-paper, supplement, and table-level evidence.** | `Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md` |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Retrieval baseline | Establishes external retrieval as the factual-access design that EVAF complements rather than replaces. | https://arxiv.org/abs/2005.11401 |
| MemGPT: Towards LLMs as Operating Systems | Agent-memory system | Related external-memory/context-management design cited by the selected paper. | https://arxiv.org/abs/2310.08560 |
| HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models | Retrieval-side memory | Related long-term retrieval architecture cited by the selected paper. | https://arxiv.org/abs/2405.14831 |
| LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | Benchmark | Related factual, temporal, and update-oriented benchmark that does not isolate the paper's post-unload depth target. | https://arxiv.org/abs/2410.10813 |
| Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo) | Benchmark | Related long-conversation memory benchmark cited as access/update context. | https://arxiv.org/abs/2402.17753 |
| Scaling Self-Evolving Agents via Parametric Memory | Related parametric-memory paper | Near-neighbor using online LoRA fast weights for self-evolving agents; not independently full-text reviewed in this pass. | https://arxiv.org/abs/2606.04536 |
| How LoRA Remembers? A Parametric Memory Law for LLM Finetuning | Related parametric-memory paper | Related analysis of LoRA memory behavior; not independently full-text reviewed in this pass. | https://arxiv.org/abs/2605.30260 |
| RaMem: Contextual Reinstatement for Long-Term Agentic Memory | Related retrieval-validity paper | Related work on retrieval-side context validity, relevant to the selected paper's unresolved invalidation boundary. | https://arxiv.org/abs/2606.22844 |
| User as Engram: Internalizing Per-User Memory as Local Parametric Edits | Related local-edit paper | Alternative parametric-memory direction aimed at reducing per-user contamination; not independently full-text reviewed in this pass. | https://arxiv.org/abs/2606.19172 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/README.md` | Selected DEP identity, inventory, ten source locators, and original synthesis. | 2026-07-19 | Repository file inspected. |
| R2 | `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md` | Ten-item expansion pool and original arXiv:2606.26806 finding. | 2026-07-19 | Repository file inspected in full. |
| R3 | `Black-Lake/.logs/20260712-Arxiv-HERMES-World-Model-LOG.md` | Latest prior DEP-Class operational context linked to the selected source DEP. | 2026-07-19 | Older than cutoff; inspected. |
| R4 | `Black-Lake/.reports/BL-Arxiv-HERMES-World-Model-20260712/Report-Mark.md` | Prior related-entry references and evidence boundary for the selected source DEP. | 2026-07-19 | Inspected in full. |
| R5 | `Black-Lake/.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/README.md` | Prior DEP manifest and attribution. | 2026-07-19 | Inspected. |
| R6 | `Black-Lake/.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` | Full latest prior DEP-Class context linked to the selected DEP. | 2026-07-19 | Inspected; context only for EVAF claims. |
| R7 | `Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/README.md` | Prior abstract-level scope and source-policy statement for the selected paper. | 2026-07-19 | Inspected. |
| R8 | `Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md` | Prior metadata/abstract treatment and explicit full-text gap. | 2026-07-19 | This pass supplies the missing full-paper expansion. |
| R9 | https://arxiv.org/abs/2606.26806 | Title, author, v1 history, abstract metrics, DOI, subjects, license link, and ancillary-file locator. | 2026-07-19 | Canonical arXiv record. |
| R10 | https://arxiv.org/html/2606.26806 | Complete method, protocol, main results, controls, related work, limitations, and references. | 2026-07-19 | Primary full text inspected end to end. |
| R11 | https://arxiv.org/pdf/2606.26806 | Formulas, affiliation, exact table values, and main-paper layout. | 2026-07-19 | Six-page primary PDF inspected; not collected into DEP. |
| R12 | https://arxiv.org/src/2606.26806v1/anc/EVAF_supplement.pdf | Protocol constants; full aggregate and seed-level tables; negative results; Memora statistics; named reproduction paths. | 2026-07-19 | Five-page official supplement rendered and inspected; temporary copy not deposited. **New in this pass.** |
| R13 | https://doi.org/10.48550/arXiv.2606.26806 | Persistent identifier. | 2026-07-19 | DOI exposed by canonical arXiv metadata. |
| R14 | `Black-Lake/README.md` | DEP class, README, attribution, log, and commit rules. | 2026-07-19 | Live default-branch authority inspected after fetch. |
| R15 | `Black-Lake/.lake-data/README.md` | DEP-E placement and publication-index maintenance rules. | 2026-07-19 | Live default-branch authority inspected after fetch. |
| R16 | `Black-Lake-Data/README.md` | Source DEP, report, and attribution expectations. | 2026-07-19 | Live default-branch authority inspected after fetch. |

## Appendix

### Selection Record

- Automation: Black-Lake Data Processing & Review 0900.
- Shared family: Black-Lake Data Processing & Review; Black-Lake Data Processing & Review 0900.
- Run timestamp: 2026-07-19T00:04:48Z.
- Eligibility cutoff: 2026-07-18T00:04:48Z.
- Canonical candidate count: 63.
- Same-family marker files checked across reports, logs, Report-Marks, and prior DEP artifacts: 58.
- Excluded inside the strict 24-hour window: 0.
- Eligible count: 63.
- DEP draw: PowerShell `Get-Random` over sorted eligible canonical DEP names selected `DEP-20260628-Tech Intel 0102`.
- Prior material: HERMES and VideoWeave DEP-Class references existed; the latest HERMES log, Report-Mark, README, full manuscript, and every preserved reference were reviewed. No source-side Report-Mark or same-family report existed for this DEP.
- Expansion pool: the selected DEP's ten primary arXiv works.
- Expansion draw: PowerShell `Get-Random` over the sorted ten-item pool selected arXiv:2606.26806.
- Prior same-paper artifact: DEP-E-20260708-Tech Intel Review contained an abstract-level review only; the current pass adds full-text and ancillary evidence.

### Replication Checklist

- Locate an author-controlled public repository and pin the exact commit matching arXiv v1.
- Verify `results/MERGE_MANIFEST.md`, seed JSONs, aggregate Markdown, and the five named loop-drift scripts.
- Pin GPT-2 124M, TinyLlama 1.1B, Mistral 7B, tokenizer, dtype, embeddings, LoRA targets, learning rates, and dependencies.
- Recreate 10-user, 200-event streams for seeds 42, 0, 1, and 2 with the published event proportions and probe schedule.
- Confirm unload clears working context but preserves the RAG index.
- Reproduce Tables 4-10 and preserve independent audit-run boundaries.
- Add deterministic deletion, update, cross-user contamination, and rollback fixtures.
- Report compute, wall time, memory, adapter hashes, stream hashes, and all failed runs.

### Source Inventory

- External source files deposited: None.
- External source files inspected temporarily: official six-page main PDF and five-page ancillary supplement.
- Repository clones, code, datasets, seed JSONs, models, and result archives collected: None.
- Public provenance: canonical arXiv/DOI URLs and repository-relative Black Lake paths only.
