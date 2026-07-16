---
title: "Beyond XAI - DEP-E"
generated_at: "2026-07-16 (public-safe date; exact execution timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-first critical review of a position paper arguing for verification, epistemology, user-sensible systems, and model-centered interpretability beyond post-hoc XAI."
source_status: "verified complete private PDF, full-paper HTML, metadata HTML, and source package; public URLs cited; no source files redistributed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "Sources and repository context inspected through 2026-07-16; paper pinned to arXiv v5."
primary_url: "https://arxiv.org/abs/2602.24176"
stable_identifier: "arXiv:2602.24176v5; DOI:10.48550/arXiv.2602.24176"
confidence_summary: "High for source identity and faithful reporting; medium for synthesis; low-to-medium for the paper's field-wide and formal claims because no systematic-review protocol or independent validation was performed."
safety_scope: "non-sensitive research review, governance design, evaluation-only implementation guidance"
distribution_notes: "No PDF, HTML, source archive, extracted content, cache, local path, machine detail, or exact local execution timestamp is redistributed."
---

# Beyond XAI - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Canonical metadata | HTML | arXiv:2602.24176v5 | https://arxiv.org/abs/2602.24176 | Public metadata; arXiv distribution terms apply. | 2026-07-16 | Inspected. |
| S2 | arXiv full-paper HTML | Primary paper | HTML | arXiv:2602.24176v5 | https://arxiv.org/html/2602.24176 | Official complete rendering; private copy withheld. | 2026-07-16 | Integrity-verified and inspected in full. |
| S3 | arXiv PDF | Primary paper | PDF | arXiv:2602.24176v5 | https://arxiv.org/pdf/2602.24176 | Public paper; private copy withheld. | 2026-07-16 | Integrity-verified and inspected. |
| S4 | arXiv source package | Primary source | TeX archive | arXiv:2602.24176v5 | https://arxiv.org/e-print/2602.24176 | Used locally to cross-check structure, equations, figures, bibliography, and limitations; withheld. | 2026-07-16 | Archive inventory and primary TeX inspected. |
| S5 | arXiv-issued DOI | Persistent identifier | DOI | 10.48550/arXiv.2602.24176 | https://doi.org/10.48550/arXiv.2602.24176 | Persistent metadata locator. | 2026-07-16 | Recorded. |
| S6 | VLM Probing DEP | Related research artifact | Markdown | DEP-E-20260712-VLM Probing | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Repository-generated review; no source files embedded. | 2026-07-16 | Inspected. |
| S7 | Agent State Review DEP | Related research artifact | Markdown | DEP-E-20260708-Agent State Review | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | Repository-generated review; some underlying sources were abstract-level in that review. | 2026-07-16 | Inspected. |
| S8 | Medical Diff VQA DEP | Related research artifact | Markdown | DEP-E-20260716-Medical Diff VQA | `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` | Repository-generated full-paper review; clinical source files withheld. | 2026-07-16 | Inspected. |
| S9 | Black Lake README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository standard. | 2026-07-16 | Fetched and read. |
| S10 | Black Lake DEP filing README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public DEP-E filing and index standard. | 2026-07-16 | Read. |
| S11 | Black-Lake-Data README | Companion-repository authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public companion-repository standard. | 2026-07-16 | Fetched and read. |
| S12 | Local archive integrity records | Private processing evidence | README, CSV, JSON, report | arXiv:2602.24176v5 | Private path withheld | Local provenance only; source documents may not be redistributed. | 2026-07-16 | Verified complete after repair. |

The canonical record lists 49 authors. For readable attribution, this artifact uses Saleh Afroogh, Syed Ishtiaque Ahmed, Petra Ahrweiler, *et al.* in summaries and preserves the complete author list in the Appendix. The paper was first submitted on 2026-02-27 and revised through v5 on 2026-05-25 in Computers and Society (cs.CY). No publisher venue, original dataset, benchmark package, or official code repository is identified by the inspected primary record.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Canonical metadata | Title, authors, dates, version, subject, abstract, DOI, public artifact URLs. | Source identity and publication context. | High | Metadata does not validate arguments. |
| E2 | S2-S4 | Primary paper and source | Full definitions, evidence narrative, formal proxy-model section, four proposed directions, risk discussion, conclusion. | Faithful paper reconstruction. | High for reporting | No cited study or formal result was independently reproduced. |
| E3 | S4 | Source bibliography | 287 bibliography entries and citation keys across XAI, HCI, philosophy, causal inference, healthcare, and agent systems. | Breadth of source base. | High for inventory | Search completeness, inclusion rationale, study quality, and citation correctness were not audited. |
| E4 | S2-S4 | Primary empirical examples | Cited 34-system review, 457-clinician study, trust/overreliance findings, saliency and proxy-model failure examples. | Paper's symptom diagnosis. | Medium-high for transcription | These are secondary reports inside the selected paper; original studies were not re-reviewed here. |
| E5 | S2-S4 | Primary conceptual/formal text | Deep-superficial tension, level confusion, model-world matrix, five assumptions, proxy-model paradox. | Conceptual architecture. | High for faithful reporting | Logical soundness and field-wide applicability remain contestable. |
| E6 | S6-S8 | Related DEP artifacts | Probe limits, runtime evidence, clinical saliency boundary. | Cross-DEP synthesis and implementation relevance. | Medium | Related DEPs do not validate the selected paper. |
| E7 | S9-S11 | Repository authorities | DEP-E location, README contract, publication index, source withholding, attribution, dedup context. | Process compliance. | High | Process evidence only. |
| E8 | S12 and repository scans | Private integrity/process evidence | Random draw, dedup, 24-hour check, repair, PDF/HTML/source validation, zero partials. | Review authorization and selection eligibility. | High | Local paths and source files are intentionally unavailable in the public artifact. |

## Executive Summary

*Beyond Explainable AI* is a 49-author position paper arguing that a large portion of post-hoc XAI has confused several different goals: understanding model internals, explaining real-world phenomena, helping users make sense of outputs, and calibrating reliance. The authors narrow their main target to post-hoc explanations for complex DNNs and LLMs under a DARPA-style end-user-trust objective. They do not argue that all model analysis is useless; instead, they seek to reclassify useful diagnostics as model-centered interpretability and to stop treating them as general explanations of decisions or the world.

The paper's diagnosis has three layers. First, cited studies are organized into four empirical symptom groups: explanations do not reliably calibrate trust, XAI often helps developers more than intended end-users, explanations can backfire through overload or overreliance, and vulnerable or low-literacy users may be poorly served. Second, the authors identify a deep-superficial tension, confusion among algorithmic, psychological, and behavioral levels, correlation-causation confusion, and five challenged assumptions about trust and knowledge formation. Third, they propose a proxy-model paradox: an incomplete or unfaithful proxy invites regress, while a complete and faithful one makes the original effectively interpretable and the proxy unnecessary.

The proposed replacement is four-pronged: Interactive AI emphasizes behavioral verification and scientific-community certification; AI Epistemology defines standards for machine-generated knowledge; User-Sensible AI adapts mediation to particular communities; and Model-Centered Interpretability preserves rigorous internal analysis without claiming external causal explanation. This is a valuable decomposition and a productive governance agenda. It is not yet a validated replacement paradigm. The article is a broad narrative synthesis with 287 bibliography entries, not a preregistered systematic review, meta-analysis, original benchmark, or implementation study. Reviewer confidence is high in this artifact's source reporting, medium in the practical synthesis, and low-to-medium in field-wide conclusions or the universality of the formal paradox.

## Detailed Summary

### Problem and Scope

The paper starts from a practical tension: high-performing DNNs and LLMs can be opaque, yet their outputs increasingly affect consequential domains. XAI became prominent through the DARPA program and regulatory pressure, but the field uses “explainability,” “interpretability,” trust, transparency, and understanding inconsistently. The authors adopt working definitions for analytical coherence and focus on post-hoc explanations aimed at end-user trust. Intrinsically interpretable models, ante-hoc explanations, and developer debugging benefits are explicitly outside the main target.

This boundary matters. Many of the strongest claims concern an intentionally narrow architecture in which a second model or attribution mechanism explains an opaque first model. Reviewer assessment: the narrow scope makes the argument clearer, but later rhetoric sometimes expands toward “XAI” as a whole. Readers should not automatically extend the critique to every contrastive, example-based, interactive, causal, or intrinsically interpretable method.

### Empirical Symptom Layer

The paper groups prior findings into four symptoms:

- **Trust-explanation gap:** explanations can increase reliance on correct and incorrect outputs, and coherent model rationales can be unfaithful to the underlying computation.
- **Stakeholder misalignment:** methods advertised for end-users often deliver more value to ML developers as debugging or analysis tools.
- **Backfire effect:** detailed explanations can overload users, justify a biased answer, reduce error detection, or signal competence merely by being present.
- **Marginalized exclusion:** one explanation format cannot meet the needs of children, low-literacy users, domain experts, regulators, and developers, while fidelity disparities may amplify existing harms.

The most concrete example transcribed in the paper is a study of 457 clinicians diagnosing acute respiratory failure: biased AI accompanied by explanations reduced diagnostic accuracy by 9.1 percentage points, and the explanations did not help clinicians recognize the bias. Another cited review examined 34 qualifying XAI systems from an initial 165 articles and found interactive adaptation most supportive of sense-making but underused. These examples support concern, but the selected paper does not provide a systematic evidence table, effect-size synthesis, or independent quality appraisal.

### Conceptual Root Layer

The **deep-superficial tension** says a technically faithful description of a complex model may remain cognitively inaccessible, whereas a simplified account can become incomplete or unfaithful. The **level-confusion argument** distinguishes algorithmic or biological mechanisms, psychological narratives, and observable behavior. The authors propose shifting user-facing reliance toward a “behavioral box”: outputs are tested and certified without pretending that a user understands the full mechanism.

The **correlation-causation critique** distinguishes model-internal association from real-world causal explanation. The paper uses a model-world matrix: an interpretability tool might correctly or incorrectly characterize model processing, and either result can still be wrongly presented as a cause in the external domain. Feature importance, saliency, and suppressor-variable examples illustrate why an attribution can be useful for diagnosis yet misleading as a scientific explanation.

Five assumptions are challenged: deep algorithmic explanation is necessary for trust; AI processing aligns with human reasoning; data-driven computation is central to both human and machine knowledge formation; autonomous AI can form reliable knowledge without continuing social verification; and explanations can reliably calibrate trust. The authors replace these assumptions with interaction, expert challenge, community verification, and explicit epistemic standards.

### Formal Proxy-Model Argument

Let the black-box model be `M1` and a proxy explanation be `M2`. The paper defines a set of incomplete or unfaithful proxies. If `M2` belongs to this set, another model may be needed to explain the relation between `M2` and `M1`, potentially producing infinite regress. If `M2` is complete and faithful, the paper argues that `M1` is no longer meaningfully opaque and `M2` is superfluous. The claimed dilemma is therefore self-elimination or regress.

Reviewer assessment: the argument exposes a real danger in equating an approximation with complete understanding. Calling it a Russell-type paradox is stronger than the provided derivation establishes. Approximate explanations can be task-bounded, plural, contrastive, decision-local, or explicitly uncertain without claiming to duplicate every mechanism. The key evaluative question may be whether a representation is adequate for a stated task and validated against relevant failure modes, not whether it is globally complete.

### Four Proposed Directions

**Interactive AI** moves from passive explanation to human-AI collaboration, shared agency, behavioral challenge, expert panels, performance certification, audit trails, and community validation. The paper proposes real-time expert feedback, context-adaptive interfaces, co-designed data pipelines, standardized domain tests, review panels, certification records, and validation networks.

**AI Epistemology** asks what counts as machine evidence, how AI-generated hypotheses should be tested against external reality, how peer review and replication should change, and how genuine discovery can be separated from computational byproduct.

**User-Sensible AI** rejects a universal explanation format. It favors expert-mediated and context-specific interfaces adapted to age, cognition, culture, domain expertise, and professional practice.

**Model-Centered Interpretability** preserves intrinsic, model-specific, mechanistic, and causal analysis of model internals for debugging, optimization, safety, and scientific inquiry. Its constraint is semantic and evidential honesty: internal model associations should not be sold as causes in the world.

### Agent-System Implication

The article explicitly extends the critique to agentic AI. Multi-agent and tool-using systems introduce dynamic call order, state changes, external side effects, and non-deterministic control flow. A post-hoc narrative of the final answer cannot reliably reconstruct the execution path. The paper therefore points toward standardized observability, tamper-resistant audit trails, runtime policy enforcement, and replayable traces. This is one of the manuscript's strongest implementation bridges because it converts an abstract philosophical argument into measurable system evidence.

### Limitations and Conclusion

The authors acknowledge that expert verification may create bottlenecks, disciplinary bias, gatekeeping, and unequal access; AI epistemology may become too abstract; user-sensible systems require scarce hybrid expertise; and model-centered interpretability may neglect sociotechnical deployment. Proposed mitigations include diverse panels, transparent participation, iterative frameworks, mediator training, and links between internal analysis and deployment evidence.

The conclusion calls for replacing XAI's broad explanatory promise with a portfolio of verification, epistemology, community-specific mediation, and model analysis. Reviewer assessment: the portfolio is useful even if the “beyond XAI” framing is not accepted. The paper is most decision-useful as a taxonomy of claims and evidence obligations, not as proof that the XAI field is logically incurable.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Post-hoc explanations do not reliably calibrate user trust and may increase overreliance or reduce error detection. | Author synthesis claim | E2, E4 | Supported by cited examples, but no systematic effect-size synthesis was provided. | Medium |
| C2 | XAI often serves developers better than its intended end-users. | Author synthesis claim | E2, E4 | Plausible and supported by selected literature; target definitions and task variation limit generalization. | Medium |
| C3 | Faithfulness and accessibility create a deep-superficial tension for explanations of complex models. | Author conceptual claim | E2, E5 | A useful tension, though not every explanation method promises complete mechanistic duplication. | Medium-high |
| C4 | Model attribution does not establish real-world causation. | Author conceptual claim | E2, E5 | Strong and consistent with causal-evidence discipline. | High |
| C5 | A proxy explanation is driven toward self-elimination or infinite regress. | Author formal claim | E2, E5 | Thought-provoking but not established for bounded, plural, approximate, or explicitly partial explanations. | Low-medium |
| C6 | Interactive verification, AI epistemology, user-sensible systems, and model-centered interpretability form a better research portfolio. | Author proposal | E2 | Coherent agenda; comparative effectiveness and cost remain untested. | Medium-low |
| C7 | Agentic AI requires trajectory-level observability and verification beyond static explanations. | Author implementation claim and reviewer synthesis | E2, E6 | Strong practical fit with dynamic state/tool evidence; specific standards remain open. | Medium-high |
| C8 | The paper was eligible and source-complete before synthesis. | Process claim | E7, E8 | First draw passed dedup; mandatory PDF and full-paper HTML gates passed after repair. | High |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E manuscript for one randomly selected, non-duplicate arXiv paper; preserve its argument, evidence, limitations, and implementation relevance.
- `Sources inspected`: Verified complete PDF, official full-paper HTML, metadata HTML, TeX/source package, canonical arXiv record, DOI, live Black Lake and Black-Lake-Data README authorities, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, grouped parent directories as paper units, made a uniform `Get-Random` draw with rejection for used or identifier-incomplete units, scanned public artifacts and memory for duplicate identifiers, repaired the selected unit, then inspected the complete paper and related DEPs.
- `Inclusion criteria`: Sources had to identify the selected paper, expose its complete argument or limitations, define repository rules, establish source integrity, or provide concrete overlap in model probing, agent verification, or high-stakes interpretability.
- `Exclusion criteria`: Abstract-only material was excluded from paper synthesis. Generic recommendation links, unrelated keyword hits, uninspected cited studies, unavailable code, and local source files were not treated as evidence.
- `Analytical approach`: Conceptual, comparative, implementation, safety-and-ethics, product-research, and replication-oriented review with limited secondary reporting of the paper's cited empirical examples.
- `Evidence handling`: Author claims are mapped to evidence IDs; reviewer interpretations are labeled; quantitative examples are identified as source-reported; related DEPs provide synthesis context only.
- `Uncertainty handling`: Narrative-review limits, non-reproduction, field-definition scope, formal-argument objections, certification risks, and internal counting inconsistency remain visible.
- `Extraction process`: Full-paper HTML and TeX were inspected for every substantive section; the PDF supplied a cross-format integrity source; the source archive exposed 287 bibliography entries and seven figure assets.
- `Version control`: Paper pinned to arXiv:2602.24176v5. Repository rules were fetched from the live default branches before drafting.
- `Random selection`: 75,777 PDFs collapsed to 75,776 parent-directory units. Uniform rejection sampling accepted the first raw draw at zero-based index 28,956.
- `Deduplication`: The primary-record set contained 232 used arXiv IDs; 93 archive units matched those IDs and 185 lacked a derivable identifier, leaving 75,498 eligible under those filters. The selected ID, DOI, normalized title, and slug were absent; reselections were zero.
- `24-hour validation`: No same-paper or same-unit marker was found on or after the public-safe cutoff date 2026-07-15.
- `Source-integrity gate`: Initial state was `partial` because full-paper HTML was missing. The valid PDF was preserved; metadata HTML, official full-paper HTML, and source package were collected with bounded direct-HTTPS attempts. Final PDF, HTML, structure, source-archive, and zero-partial checks passed before review.
- `Reviewer stance`: Critical position-paper review, DEP-ready preservation, evidence-contract design, and explicit boundary between source claims and implementation proposals.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's definitions, empirical symptom taxonomy, conceptual and formal arguments, four proposed directions, agent-system implications, and source-disclosed risks.
- `Temporal boundary`: Sources inspected through 2026-07-16; selected paper pinned to v5 dated 2026-05-25.
- `Evidence limits`: No cited study, benchmark, codebase, user study, formal proof, or alternative paradigm was independently reproduced. No systematic-review protocol was available.
- `Assumptions`: The official v5 PDF, HTML, and source package correspond; the bibliography inventory represents the cited source set; related DEP artifacts accurately report their own stated evidence boundaries.
- `Constraints`: Original sources remain private to the local archive. Public output excludes local paths, usernames, machine identifiers, exact execution timestamps, caches, and source files.
- `Out of scope`: Settling the definition of XAI, proving the proxy-model paradox, legal interpretation of explanation rights, evaluating every cited study, or certifying a production AI system.
- `Intended use`: Research review, DEP deposition, evaluation design, governance planning, and follow-on systematic review.
- `Audience`: XAI and interpretability researchers, HCI practitioners, agent-system engineers, domain-safety reviewers, and AI governance designers.
- `Reproducibility boundary`: Another reviewer can retrieve the public paper and related DEPs; reproducing the paper's field-wide claims requires a new citation-level protocol and reinspection of underlying studies.
- `Data sensitivity`: Public scholarly sources and repository-generated Markdown only; no restricted or personal dataset was processed.

## Observations

- `Observed pattern`: The strongest parts of the paper are distinctions—model versus world, trust versus reliance, interpretation attempt versus achieved interpretability—not the “XAI is incurable” rhetoric.
- `Technical implication`: A useful interpretability artifact should declare its claim type and validation target before showing saliency, probes, examples, or narratives.
- `Contradiction or tension`: The paper narrows its object to post-hoc proxy explanations but sometimes makes conclusions about XAI generally. Its “eight root causes” label also conflicts with the nine items it enumerates.
- `Open question`: Does expert verification improve calibrated reliance after accounting for panel bias, reviewer fatigue, institutional incentives, disagreement, and access cost?
- `Reviewer hypothesis`: Agent systems are a high-value test bed for the post-XAI agenda because trace coverage, state replay, policy invariants, and counterfactual tool denial are measurable without claiming complete mechanistic explanation.

## Considerations

- Verification can become a new black box if certification methods, reviewer disagreements, data coverage, and failure thresholds are hidden.
- Expert panels may reproduce professional, cultural, or commercial bias. Governance needs diverse participation, appeals, rotation, conflict disclosure, and public evidence summaries.
- Behavioral certification can expire under distribution shift, software changes, prompt changes, tool changes, or evolving user needs. Evidence must be versioned and refreshed.
- User-sensible mediation should not become manipulative personalization. Interfaces need accessibility, informed choice, uncertainty disclosure, and boundaries on persuasion.
- Model-centered tools still face privacy and security risks: traces, activations, and explanations can leak sensitive inputs or reveal system vulnerabilities.
- Regulatory “explanation” obligations cannot be assumed to accept verification artifacts as substitutes; legal analysis remains separate.

## Strengths

- The paper states a clear main scope and preserves legitimate roles for intrinsically interpretable models, developer diagnostics, mechanistic analysis, and causal research.
- Its model-versus-world and trust-versus-reliance distinctions are directly useful for evidence review and product governance.
- The four-direction portfolio prevents one tool from being asked to satisfy incompatible scientific, technical, user, and institutional goals.
- Agentic-AI discussion connects conceptual critique to observability, traces, runtime policy, and system-level verification.
- Source breadth is substantial: 287 bibliography entries, 49 authors across many disciplines, and explicit limitations for the proposed alternatives.

## Weaknesses

- The evidence review is narrative. Search sources, queries, dates, screening flow, inclusion criteria, study-quality scoring, and citation-level claim checks are not reported.
- A narrow definition of post-hoc XAI sometimes supports broader claims about the field, risking a scope shift.
- The proxy-model paradox assumes a strong completeness/faithfulness framing and does not fully address useful bounded approximations, contrastive explanations, multiple complementary explanations, or uncertainty-aware claims.
- The proposed alternatives lack comparative experiments, cost models, adoption evidence, workload estimates, and failure thresholds.
- The paper's issue-count arithmetic is internally inconsistent: two paradoxes plus two confusions plus five assumptions is nine, not eight.
- Several empirical claims are persuasive examples rather than a balanced synthesis of supportive, null, and contradictory findings.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a preregistered review protocol and claim-evidence matrix | Evidence synthesis | Broad field claims need reproducible coverage and quality assessment. | Stronger calibration and easier correction. | High review labor; category disagreements. | Independent dual screening, inter-rater agreement, citation audits, and public exclusions. |
| Narrow and formalize the proxy argument | Theory | Current definitions may exclude bounded or plural explanation practices by construction. | A testable theorem or a more defensible design dilemma. | Formalization may weaken rhetorical simplicity. | Expert counterexample workshop and explicit assumptions/countermodels. |
| Compare explanation and verification experimentally | Empirical evaluation | Alternatives are proposed without direct head-to-head evidence. | Measures reliance, errors, workload, accessibility, and cost. | Domain-specific studies are expensive and may not generalize. | Preregistered multi-domain trials with subgroup and disagreement analysis. |
| Define certification lifecycle controls | Operations | Verification can go stale as systems and contexts change. | Versioned, renewable, contestable evidence. | Monitoring burden and institutional capture risk. | Expiry rules, change detection, incident review, and external audits. |
| Add an agent-trace benchmark | Implementation | Agentic claims are concrete but untested in the paper. | Directly evaluates trace coverage and replayability. | Trace privacy and nondeterminism. | Synthetic tool environments, seeded replays, invariant checks, and tamper tests. |

## Potential Implementations

### 1. Evidence-Typed Model Card Gate

- `User`: Model release, safety, and governance teams.
- `Goal`: Prevent a model diagnostic from being published as a causal or reliability claim.
- `Core mechanism`: Require every claim to declare model-internal, behavioral, world-causal, or user-study scope and attach evidence IDs, versions, limitations, and review status.
- `Required inputs`: Release claims, benchmark results, intervention records, subgroup metrics, source provenance.
- `Outputs`: Accepted/rejected claims, missing-evidence findings, versioned release card.
- `Risk controls`: Manual review, appeals, privacy filtering, explicit uncertainty, expiry dates.
- `Evaluation`: Claim-level audit agreement and post-release incident recall.

### 2. Interactive Verification Workbench

- `User`: Qualified domain experts and safety reviewers.
- `Goal`: Test outputs through challenge and comparison rather than passive explanation consumption.
- `Core mechanism`: Counterexamples, ablations, reference swaps, uncertainty, evidence provenance, and recorded reviewer decisions.
- `Required inputs`: Authorized test cases, model outputs, expected evidence, review criteria.
- `Outputs`: Verification cards, dissent records, unresolved cases, coverage metrics.
- `Risk controls`: Access control, reviewer rotation, conflict disclosure, audit logs, non-diagnostic scope where applicable.
- `Evaluation`: Error detection, calibrated reliance, reviewer workload, subgroup coverage, and agreement.

### 3. Agent Trajectory Certification Harness

- `User`: Agent-platform engineers and assurance teams.
- `Goal`: Verify system behavior across tools, state, and nondeterministic execution.
- `Core mechanism`: Capture tool calls and state transitions, replay seeded scenarios, deny optional tools, inject counterevidence, and enforce invariants.
- `Required inputs`: Scenario suite, policy rules, state checkpoints, trace schema, tool mocks.
- `Outputs`: Trace coverage, invariant failures, replay divergence, policy violations, certification status.
- `Risk controls`: Synthetic or authorized data, secret redaction, bounded retries, tamper evidence, human stop controls.
- `Evaluation`: Reproducibility, failure recall, false alarms, privacy leakage, and trace completeness.

## Three Ways to Exercise This Research

1. **Claim taxonomy audit:** Objective: inspect one existing model card; inputs: public claims and evidence; method: label each claim as model-internal, behavioral, world-causal, or user-study and flag category jumps; output: a claim-evidence matrix; success criterion: every high-impact claim has a type, source, limitation, and owner; stop condition: confidential evidence or an unresolvable claim definition appears.
2. **Explanation-versus-verification tabletop:** Objective: compare passive explanations with active challenge; inputs: synthetic decisions containing correct, biased, and uncertain cases; method: have reviewers first assess explanations and then use counterexamples and evidence removal; output: error-detection, reliance, and workload comparison; success criterion: preregistered measures are complete without using personal data; stop condition: participants are misled about stakes or the study lacks informed consent.
3. **Agent trace replay:** Objective: test whether a final narrative matches actual execution; inputs: a sandboxed tool agent, fixed scenarios, and state checkpoints; method: record traces, replay with a denied tool and injected counterevidence, and compare invariants; output: divergence and trace-coverage report; success criterion: every side effect and policy decision is attributable; stop condition: the agent can reach production systems or unapproved external data.

## Example MVP Product

- `Product name`: EvidenceChain Review Console
- `Target user`: AI assurance engineers, domain reviewers, and release approvers.
- `Problem`: Teams receive polished explanations and dashboards but cannot tell whether a claim concerns model internals, behavior, causation, or user perception, nor whether the supporting evidence remains current.
- `Core workflow`: Import a release claim set; type each claim; attach evidence and version pins; run bounded counterfactual tests; collect independent reviewer decisions; publish a public-safe reliance card with unresolved gaps.
- `Data requirements`: Synthetic or authorized evaluation cases, model outputs, trace events, benchmark summaries, intervention results, reviewer decisions, and version metadata.
- `Architecture`: Local or controlled web application with a claim registry, evidence ledger, test runner, trace store, reviewer queue, and redacted export generator.
- `Success metrics`: Percentage of high-impact claims with complete evidence; counterexample detection rate; reviewer agreement and dissent visibility; trace coverage; stale-evidence detection; time to resolution; privacy incidents.
- `Risk controls`: Role-based access, least-privilege test environments, secret and personal-data redaction, immutable review history, evidence expiry, appeal workflow, and explicit “not certified” states.
- `Limitations`: The console organizes evidence but cannot determine truth automatically. It depends on scenario quality, reviewer competence, institutional incentives, and domain-specific standards.
- `MVP boundary`: No autonomous production approval, no legal-compliance determination, no clinical diagnosis, and no ingestion of unrestricted private traces.
- `Deployment model`: Local-first or enterprise-controlled service with exportable Markdown evidence cards.
- `Evaluation plan`: Synthetic acceptance suite, seeded agent replays, reviewer usability study, claim-type agreement test, privacy review, and incident simulation.
- `Failure modes`: Missing traces, persuasive but irrelevant evidence, panel capture, stale certification, metric gaming, and excessive reviewer burden.
- `Maintenance plan`: Versioned schemas, scheduled evidence expiry, policy review, scenario refresh, dependency monitoring, and annual external audit.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| VLM Probing DEP | Related Black Lake review | Shows that probe success and attention patterns reveal recoverable associations but do not by themselves establish causal model use. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md; arXiv:2005.07310 |
| Agent State Review DEP | Related Black Lake review | Provides runtime-state, evidence-replay, online-monitoring, and audit concepts for verification of tool-using and persistent agents. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md |
| Medical Diff VQA DEP | Related Black Lake review | Demonstrates the high-stakes boundary between useful visual inspection aids and causal, calibrated, externally validated evidence. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md; arXiv:2307.11986 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2602.24176 | Canonical metadata, abstract, authors, versions, subject, DOI, public links | 2026-07-16 | Primary metadata. |
| R2 | https://arxiv.org/html/2602.24176 | Complete paper text, figures, equations, argument, limits | 2026-07-16 | Official HTML; private copy withheld. |
| R3 | https://arxiv.org/pdf/2602.24176 | Complete primary paper | 2026-07-16 | Verified private copy withheld. |
| R4 | https://arxiv.org/e-print/2602.24176 | TeX source, bibliography, figure inventory | 2026-07-16 | Verified private source package withheld. |
| R5 | https://doi.org/10.48550/arXiv.2602.24176 | Persistent paper identity | 2026-07-16 | arXiv-issued DOI. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, source policy, DEP and commit rules | 2026-07-16 | Live default-branch README. |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-07-16 | Live repository policy. |
| R8 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion-repository context | 2026-07-16 | Live default-branch README. |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md | Probe/attention evidence boundary | 2026-07-16 | Related DEP; source basis arXiv:2005.07310. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md | Runtime evidence and agent verification | 2026-07-16 | Related DEP; selected sources include arXiv:2607.02510 and arXiv:2607.02514. |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md | High-stakes saliency and validation boundary | 2026-07-16 | Related DEP; source basis arXiv:2307.11986. |
| R12 | Private integrity records, path withheld | Random selection, dedup, repair, PDF/HTML/source verification | 2026-07-16 | Processing evidence only; no private file redistributed. |

## Appendix

### Complete Author List

Saleh Afroogh; Syed Ishtiaque Ahmed; Petra Ahrweiler; David Alvarez-Melis; Mansur Maturidi Arief; Emilia Barakova; Falco J. Bargagli-Stoffi; Erdem Biyik; Hanjie Chen; Xiang “Anthony” Chen; Robert Alan Clements; Keeley Crockett; Amit Dhurandhar; Fethiye Irmak Dogan; Mollie Dollinger; Motahhare Eslami; Aldo A Faisal; Arya Farahi; Melanie F. Pradier; Saadia Gabriel; Diego Garcia-Olano; Marzyeh Ghassemi; Shaona Ghosh; Hatice Gunes; Ehsan Hajiramezanali; Stefan Haufe; Biwei Huang; Angel Hwang; Md Tauhidul Islam; Junfeng Jiao; Amir-Hossein Karimi; Saber Kazeminasab; Anastasia Kuzminykh; William La Cava; Brian Y. Lim; Xiaofeng Liu; Mohammad R. K. Mofrad; Alicia Parrish; Maria Perez-Ortiz; Shriti Raj; Swabha Swayamdipta; Salmonn Talebi; Kush R. Varshney; Mihaela Vorvoreanu; Lily Weng; Alice Xiang; Yiming Xu; Ding Zhao; Jieyu Zhao.

### Selection and Source-Integrity Record

- Candidate enumeration: 75,777 PDFs; 75,776 parent-directory paper units.
- Primary used-ID set: 232; units matching a used ID: 93; units without a derivable ID: 185; units eligible under those filters: 75,498.
- Random acceptance: first raw draw, zero-based index 28,956; duplicate rejections: 0; reselections: 0.
- Initial source state: partial because full-paper HTML was absent.
- Preserved PDF: 1,976,924 bytes; `%PDF-` header; trailing `%%EOF`; SHA-256 verified.
- Repaired official full-paper HTML: 356,861 bytes; 140,055 body characters; document marker; 71 headings/sections; seven structure terms.
- Repaired metadata HTML: provenance only, never counted as the paper.
- Repaired source package: 2,026,164 bytes; readable archive inventory.
- Final source state: complete; review authorized; partial files: 0.
- Publication boundary: no source document, extracted source text, or cache was uploaded; no `.source/` directory exists.

### Follow-On Replication Checklist

- Publish review queries, databases, cutoff dates, screening decisions, and study-quality criteria.
- Map every field-wide claim to underlying studies and record supportive, null, and contradictory evidence.
- Re-evaluate the cited 34-system and 457-clinician findings from their primary sources.
- Formalize the proxy-model definitions and test bounded, plural, contrastive, and uncertainty-aware counterexamples.
- Preregister head-to-head studies of explanation, interactive verification, user-sensible mediation, and model-centered analysis.
- Measure error detection, calibrated reliance, coverage, accessibility, subgroup outcomes, reviewer workload, disagreement, institutional cost, and evidence expiry.
