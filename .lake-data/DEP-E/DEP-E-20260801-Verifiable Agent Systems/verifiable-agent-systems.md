---
title: "Verifiable Agent Systems - DEP-E"
generated_at: "2026-08-01"
artifact_type: "DEP research artifact"
primary_subject: "How explicit state, evidence, verification, and resource controls shape reliable agentic systems."
source_status: "mixed; temporary review copies inspected and withheld, public URLs cited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-01"
temporal_cutoff: "2026-08-01"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/2bebe12af935e746e37ccc8354beebe03c0694b7/.lake-data/DEP-20260713-Tech%20Intel%201104"
stable_identifier: "DEP-20260713-Tech Intel 1104"
confidence_summary: "Medium-high for source descriptions; medium for cross-source transfer because most evidence is preprint, benchmark-specific, or deployment-specific."
safety_scope: "defensive security, evaluation, non-diagnostic clinical analysis, and bounded implementation planning"
distribution_notes: "Public-safe derived artifact; temporary paper copies, extracted text, and rendered review images are not redistributed."
---

# Verifiable Agent Systems - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | `DEP-20260713-Tech Intel 1104` | Primary source bundle | Repository DEP | Black-Lake-Data snapshot `2bebe12` | [Source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/2bebe12af935e746e37ccc8354beebe03c0694b7/.lake-data/DEP-20260713-Tech%20Intel%201104) | Repository content used as deposited; no external source files redistributed | 2026-08-01 | README and findings inspected |
| S1 | Hsu and Lu, *Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift* | Primary paper | arXiv PDF | arXiv:2607.09175v1 | [arXiv](https://arxiv.org/abs/2607.09175) | Preprint; paper reports code under Apache-2.0 | 2026-08-01 | Complete PDF inspected |
| S2 | Bogdanov, Rosen, and Vafa, *Statistically Undetectable Backdoors in Deep Neural Networks* | Primary paper | arXiv PDF | arXiv:2607.09532v1 | [arXiv](https://arxiv.org/abs/2607.09532) | Preprint; theoretical and preliminary empirical evidence | 2026-08-01 | Complete PDF inspected |
| S3 | Li et al., *Long-Horizon-Terminal-Bench* | Primary paper | arXiv PDF | arXiv:2607.08964v2 | [arXiv](https://arxiv.org/abs/2607.08964) | Preprint; benchmark and results are revision-sensitive | 2026-08-01 | Complete PDF inspected |
| S4 | Kuang et al., *KV-PRM* | Primary paper | arXiv PDF | arXiv:2607.09153v1 | [arXiv](https://arxiv.org/abs/2607.09153) | Preprint; architecture-coupled evaluation | 2026-08-01 | Complete PDF inspected |
| S5 | Pedada, Dhavala, and Patil, *Shared Selective Persistent Memory for Agentic LLM Systems* | Primary paper | arXiv PDF | arXiv:2607.09493v1 | [arXiv](https://arxiv.org/abs/2607.09493) | Preprint; includes enterprise and public-dataset evaluations | 2026-08-01 | Complete PDF inspected |
| S6 | Li et al., *SherAgent* | Primary paper | arXiv PDF | arXiv:2607.09176v1 | [arXiv](https://arxiv.org/abs/2607.09176) | Defensive security research; production data is not public | 2026-08-01 | Complete PDF inspected |
| S7 | Qu et al., *SAGEAgent* | Primary paper | arXiv PDF | arXiv:2607.09521v1 | [arXiv](https://arxiv.org/abs/2607.09521) | Preprint; retrospective, non-diagnostic evidence | 2026-08-01 | Complete PDF inspected |
| S8 | Zhan et al., *Seeing is Free, Speaking is Not* | Primary paper | arXiv PDF | arXiv:2607.09520v1 | [arXiv](https://arxiv.org/abs/2607.09520) | Preprint accepted to ACM MM 2026; hardware-conditioned results | 2026-08-01 | Complete PDF inspected |
| S9 | Schmitt et al., *ProofCouncil* | Primary paper | arXiv PDF | arXiv:2607.09474v1 | [arXiv](https://arxiv.org/abs/2607.09474) | Preprint; some researcher-provided problems and solutions remain private | 2026-08-01 | Complete PDF inspected |
| S10 | Qian et al., *Malaika* | Primary paper | arXiv PDF | arXiv:2607.09179v1 | [arXiv](https://arxiv.org/abs/2607.09179) | Defensive Android malware analysis; static-analysis scope | 2026-08-01 | Complete PDF inspected |
| S11 | GRACE official repository | Official implementation | Git repository | commit `b8b6b9a` | [GitHub](https://github.com/RedMind-Research/GRACE/tree/b8b6b9adbb1cd868a7298c8526b2f2e3774ccab4) | Apache-2.0 indicated by repository | 2026-08-01 | README inspected at pinned commit |
| S12 | LHTB official repository | Official benchmark implementation | Git repository | commit `b695ed2` | [GitHub](https://github.com/zli12321/LHTB/tree/b695ed2eaa41b95fd60949e595955fc8e60eac32) | Repository includes a modified Harbor harness; license visible in repository | 2026-08-01 | README inspected at pinned commit |
| S13 | SAGEAgent official repository | Official implementation | Git repository | commit `5fcb694` | [GitHub](https://github.com/Chongyu1117/SAGEAgent/tree/5fcb6941879d3bc25a99aaec203bc23f56e0e1af) | Requirements and evaluation scripts exposed; dataset rights not inferred | 2026-08-01 | README inspected at pinned commit |
| S14 | ProofCouncil official repository | Official implementation | Git repository | commit `2555c79` | [GitHub](https://github.com/eth-sri/proof-council/tree/2555c798013603748c5556866c89a9eae5795d48) | MIT license indicated by repository | 2026-08-01 | README inspected at pinned commit |

Temporary paper copies, text extractions, and first-page renders were used only for local review. Public provenance is expressed through stable repository-relative paths, canonical URLs, version identifiers, and immutable repository commits.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S0 | Repository DEP | README, ten-item findings synthesis, source URLs, and attribution notes | Research-object identity, source inventory, and original synthesis boundary | High | The inaccessible recap referenced by the DEP was not available |
| E2 | S1 and S11 | Primary paper and official repo | Typed semantic graph, local structural validation, ten-batch shift protocol, five replications, ablation, and implementation contract | Explicit structure can localize verification of evolving instructions | Medium-high | One telecom-derived harness, fixed model, and fixed evaluation set |
| E3 | S2 | Primary theoretical paper | Backdoor definition, architectural assumptions, statistical-undetectability result, proof-of-concept, and preliminary collision experiments | White-box weight inspection is not a universal integrity guarantee | Medium | Restricted architecture, cryptographic assumptions, proof-of-concept scale, no broad modern-model demonstration |
| E4 | S3 and S12 | Primary benchmark paper and official repo | Forty-six containerized tasks, dense hidden grading, model results, failure analysis, and harness behavior | Long-horizon reliability needs artifact-grounded progress signals and calibrated stopping | Medium-high | Expensive single benchmark; paper and live repository snapshots differ in model coverage |
| E5 | S4 | Primary paper | Verify-token KV-cache readout, complexity analysis, theorem assumptions, benchmark results, and KV Steering proof-of-concept | Reusing internal state can cut verifier cost while preserving or improving scoring | Medium | Generator and verifier must share architecture; theory uses the Linear Representation Hypothesis |
| E6 | S5 | Primary paper | Four-part memory taxonomy, enterprise ablation, public-dataset replication, user study, and zero-token refresh | Selective reusable state can outperform both statelessness and full-history persistence | Medium | Small task and user samples; manual memory categories; stable structured schemas |
| E7 | S6 | Primary security paper | Query-filter backtracking, 53,849-alert production deployment, curated comparisons, user study, and failure cases | Provenance-aware search can mitigate broken chains and dependency explosion | Medium | Private production data, selected evaluation subsets, placeholder venue metadata, LLM/log-injection risks |
| E8 | S7 and S13 | Primary medical-AI paper and official repo | Ordered modality acquisition, 962-patient source cohort, 170 complete-patient nested evaluation, burden model, ablation, and code layout | Acquisition decisions can explicitly trade predictive performance against measurement burden | Medium | Retrospective and single disease setting; derived burden weights; no prospective clinical validation |
| E9 | S8 | Primary systems paper | Five VLMs, two hardware platforms, phase timing, constant-power observation, token-cost ratios, and prompt-length intervention | Output policy can dominate edge inference energy and latency | Medium-high | Two NVIDIA platforms, selected models and prompts, no broader accelerator survey |
| E10 | S9 and S14 | Primary paper and official repo | Author-critic loop, fresh-critic resets, council and compute nodes, FirstProof results, open-problem feedback, cost accounting, and released DAG runner | Independent review and checkable computation improve research-agent usefulness but not certainty | Medium | Human judgment remains incomplete; high cost; adaptive development evaluation; timeout and interpretation failures |
| E11 | S10 | Primary security paper | Tri-grounded architecture, 255-application MalEval evaluation, ATT&CK attribution subset, ablations, case study, and threats to validity | Grounding structure affects precision and auditability beyond base-model capability | Medium | Android-only static analysis; 20-sample ATT&CK subset; partial LLM-as-judge evaluation; no runtime/native-code coverage |
| E12 | E2-E11 | Cross-source triangulation | Recurring roles for explicit state, independent checks, provenance, dense progress, and resource budgets | Reviewer inference: verifiability is an architectural property distributed across the workflow | Medium | No shared benchmark jointly evaluates all mechanisms |

## Executive Summary

The ten works in this DEP converge on one practical thesis: reliable agentic behavior depends less on a single model score than on how a system represents state, exposes intermediate evidence, verifies changes, and accounts for resource or human burden. This is a reviewer synthesis supported across E2-E12, not a claim made by any one source.

The clearest state-management evidence comes from GRACE and shared selective persistent memory. GRACE reports final-checkpoint pass^3 of `0.673 +/- 0.136` across five replications, compared with `0.191 +/- 0.051` for flat-text evolution and `0.242` for a stronger zero-shot reference in the same held-out telecom setting (E2). The selective-memory system reports `96%` completion across 24 recurring artifact tasks, versus `79%` without memory and `71%` with full history, while its structured-data refresh path removes the model call entirely in compatible cases (E6). These results support explicit, scoped state rather than unrestricted history, but neither establishes general cross-domain superiority.

Evaluation and verification also need artifact-grounded feedback. Long-Horizon-Terminal-Bench v2 uses 46 containerized tasks with dense hidden graders; across 17 models in the paper, the strongest reported model solved `13/46` at reward `>= 0.95`, while runs averaged 9.8 million tokens, 239 episodes, and 88.9 minutes (E4). ProofCouncil's fresh-critic resets prevented repeated stateful-critic acceptance of one incomplete proof, yet another incorrect proof still passed the critic, and official costs were about `$3,186` across nine analyzed FirstProof problems (E10). Dense grading and independent criticism improve observability; neither replaces external ground truth.

Three papers make evidence provenance central. SherAgent reports gains in attack-investigation success while retaining an investigation tree, but its production comparisons use selected cases from a private alert stream (E7). Malaika improves report-level and ATT&CK attribution precision by requiring domain, semantic, and knowledge grounding, while remaining limited to static Android evidence and benchmark-specific ground truth (E11). The backdoor paper gives a theoretical warning that even full model weights may not reveal certain planted capabilities under its assumptions, shifting assurance toward training provenance, builder trust, reproducible pipelines, and behavioral audits (E3).

Finally, verification has a resource envelope. KV-PRM reports up to 5,000x fewer scoring FLOPs, 37x lower latency, and 34x lower per-sequence memory by reusing a generator's KV cache, subject to architecture coupling (E5). The edge-VLM study finds each output token costs 11-39x more wall-clock time than an input token on the tested systems, with output-length control saving up to 97% of total energy (E9). SAGEAgent reports a 55% modeled acquisition-burden reduction while remaining within 0.012 C-index of its full-modality backbone, but this retrospective result is not evidence that clinical tests can safely be omitted (E8).

Overall confidence is medium-high that the sources support their reported mechanisms and source-specific results, and medium that the shared design pattern transfers across domains. The evidence base is rich but heterogeneous: most works are recent preprints; several depend on private data, model APIs, hardware, or benchmark harnesses; and no experiment here was independently reproduced.

## Detailed Summary

### Explicit state and scoped change

GRACE treats the persistent instruction inside an agent context as a typed semantic graph. Proposed updates modify atomic instruction nodes, local typed neighborhoods are checked for conflict, and accepted changes are reconstructed into the deployed text checkpoint. The fixed telecom-derived harness isolates the representation and verification substrate: the model, tools, diagnosis process, and held-out evaluation remain fixed while graph-based and flat-text evolution vary. The ten-batch alternating shift protocol shows not only later-checkpoint gains but better backward transfer after distribution changes. Its ablation indicates that contradiction avoidance alone is insufficient; consolidation of the growing instruction substrate is also necessary (E2).

Shared selective persistent memory reaches a related result through a different system boundary. It retains task specifications, data schemas, tool configurations, and output constraints while discarding session-specific reasoning traces. In 24 enterprise artifact tasks, selective memory improved completion and reduced turns, output tokens, and time. Full-history persistence used roughly nine times the no-memory input tokens yet performed worse. The public-dataset experiment achieved `12/12` successful zero-token refresh trials, but those trials reused generated programs against compatible structured schemas; they did not demonstrate zero-token generation of new artifacts (E6).

Together these sources distinguish durable declarative control state from transient reasoning traces. The transferable mechanism is not "more memory" but governed state with typed scope, lineage, compatibility checks, and an explicit deletion or consolidation policy.

### Progress, independent review, and stop conditions

Long-Horizon-Terminal-Bench decomposes 46 terminal tasks into deterministic, environment-grounded subtasks. The paper's v2 evaluation uses 17 frontier models and primarily the Terminus-2 harness, with GPT-5.3 evaluated through Codex. Dense reward separates partial progress from completion and exposes timeout, looping, premature exit, and self-verification failure. The official repository snapshot has expanded to 21 models and documents an important harness condition: 30 tasks continue after a claimed completion, run a hidden verifier, return feedback, and resume until pass or timeout. Stock Harbor ignores that flag, so reproduction requires the repository's modified harness (E4).

ProofCouncil applies a comparable principle to mathematics. An author iteratively edits a proof, a stateful critic reviews it, a fresh critic periodically resets context, and optional council and computer-algebra nodes provide targeted checks. Expert referees judged six of ten FirstProof submissions correct up to at most minor revisions; among 21 researcher responses on a separate 30-problem set, five were complete, two were promising pending verification, eight provided useful partial progress, four made no progress without identified errors, and two misinterpreted the problem. The fresh critic was essential on one incomplete result, but a critic still accepted a different invalid proof. The workflow therefore demonstrates the value of independent review without establishing autonomous mathematical correctness (E10).

Across both systems, stopping is part of the evaluated algorithm. A system should stop only when an external artifact check passes, evidence is exhausted, or an explicit cost/time boundary is reached. Self-reported completion is weak evidence.

### Representation reuse and physical budgets

KV-PRM reads a generator's existing KV cache with a single verify token rather than re-encoding the full trajectory for every process-reward score. The paper frames this as reducing verifier work from `O(dL^2)` to `O(dL)` and reports comparable or better results across beam search, MCTS, and weighted voting on reasoning benchmarks. The efficiency gains are large, but the approach assumes generator-verifier architecture compatibility, and its information-theoretic argument relies on the Linear Representation Hypothesis. KV Steering is explicitly preliminary (E5).

The edge-VLM study shows why operational budgets must be measured at the system boundary. Across five VLMs, RTX 3070 and Jetson Orin NX, and varied resolutions and prompts, average inference power changed by less than 5% while inference time drove energy. Decode accounted for 86-97% of total energy in the RTX 3070 figure, and a short-answer prompt reduced one model's decode time from 18.0 seconds to 0.07 seconds on Jetson. Dynamic visual tokenizers can still make high-resolution prefill expensive; at 896x896, Qwen2.5-VL-3B approached prefill/decode parity. The result is not that visual processing is universally free, but that output policy is the dominant lever under the tested common-resolution, nontrivial-generation conditions (E9).

### Evidence-grounded security operations

SherAgent addresses two production provenance-graph failures: dependency explosion around highly connected nodes and broken causal chains from missing logs. Its query-filter loop broadens SQL conditions when results are absent, filters branches using semantics, selects the next nodes, and records an investigation tree. The system processed 53,849 production alerts. Comparative evaluation used 125 log-omission cases, 25 cases where the legacy baseline hallucinated success, and 50 complete-log cases, all manually labeled and analyst-validated. The source reports 31.1% and 63.7% end-to-end success gains over enterprise and academic baselines, under `$0.10` and four minutes per investigation. These are deployment signals, but the case selection, private data, generic-process ambiguity, noisy-log failure, and susceptibility to adversarial log content constrain generalization (E7).

Malaika decomposes Android malware understanding into domain grounding for hypotheses, semantic grounding for code localization and connection, and knowledge grounding for ATT&CK attribution. On MalEval's 255 applications, it reports binary F1 `69.39`, report quality `56.21`, false-positive correction `96.00`, true-positive maintenance `93.13`, and category F1 `45.70`, outperforming the paper's MalEval and LAMD baselines on the principal aggregate measures. Its grounding ablations reduce performance in complementary ways. Against Claude Code, Malaika trades recall for lower false-positive attribution; in a GolfSpy case both found eight true positives, while Malaika produced three false positives versus nine. The ATT&CK evaluation, however, covers 20 samples with family-level rather than complete per-sample ground truth, and all methods fail on the Rootkit category in the report-level table (E11).

The backdoor paper widens the assurance boundary. Under cryptographic assumptions and architectural constraints - a frozen compressing Gaussian first layer, discrete bounded inputs, and a bi-Lipschitz remainder - it constructs statistically undetectable backdoors for invariance-based adversarial examples. The proof-of-concept tests dimensions up to `n=100` for several heuristics and reports planted norms orders of magnitude below competing algorithms, but the authors explicitly call the empirical work preliminary. The operational lesson is defensive: weight access alone cannot serve as a universal integrity certificate; provenance and behavior-level testing remain necessary (E3).

### Cost-aware acquisition in clinical prediction

SAGEAgent orders demographics, radiology, pathology, and genomics by a multi-criteria burden score. A frozen Qwen-2.5-7B-Instruct agent consumes tool-generated text, retrieves three stage-matched episodic cases, and consults up to ten semantic rules. Its source cohort contains 962 patients, but the nested `5x5` cross-validation evaluates decisions on the 170 patients with all modalities. SAGEAgent reports C-index `0.813 +/- 0.046` at burden `0.451`, compared with `0.825 +/- 0.050` at burden `1.0` for the full-modality backbone. RL baselines reduce burden further but fall to C-index around `0.73`. Ablations indicate episodic and semantic memory contribute complementary burden reductions (E8).

The paper's conclusion suggests some patients may not require biopsy for prognostication. This manuscript does not carry that conclusion into practice: the study is retrospective, small at the complete-modality evaluation boundary, single-disease, dependent on pretrained 32-dimensional features and modeled burden, and lacks prospective clinical validation. The research supports evaluation of acquisition policies, not clinical omission of indicated tests.

### Cross-source mechanism

The common mechanism has five stages:

1. Represent durable state explicitly and keep transient reasoning separate.
2. Attach changes and claims to inspectable evidence or artifact state.
3. Use independent or hidden verification rather than self-reported completion.
4. Continue, revise, or abstain according to verifier feedback and evidence sufficiency.
5. Stop within explicit compute, energy, financial, privacy, and human-burden constraints.

This mechanism is a reviewer inference from E2-E12. It is not a demonstrated universal architecture, and each stage requires domain-specific evidence and failure tests.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Typed, locally validated state improves long-horizon instruction evolution in the reported telecom setting. | Source claim | E2 | Supported within five replications and an ablation; external validity remains open. | Medium-high |
| C2 | Selective persistent context can outperform both stateless sessions and full-history persistence. | Source claim | E6 | Supported on 24 enterprise tasks and a narrow public structured-data replication; categories are manually designed. | Medium |
| C3 | Dense hidden grading reveals partial progress and premature stopping that binary completion misses. | Source claim | E4 | Directly supported by benchmark construction and score distributions; performance is harness- and snapshot-sensitive. | Medium-high |
| C4 | Independent critics reduce correlated acceptance errors but do not establish proof correctness. | Reviewer interpretation | E10 | Strongly illustrated by the fresh-critic case and the remaining critic failure. | Medium-high |
| C5 | Reusing internal generation state can make verification materially cheaper. | Source claim | E5 | Supported under architecture coupling; broader cross-model use is not established. | Medium |
| C6 | Output-length policy is a first-order energy lever for the evaluated edge VLM systems. | Source claim | E9 | Supported by timing, power, and prompt interventions; not universal across hardware or workload. | Medium-high |
| C7 | Security-agent conclusions become more auditable when tied to provenance, localized program evidence, and external threat knowledge. | Cross-source reviewer interpretation | E7, E11 | Consistent across two defensive domains, but both use constrained/private evaluation boundaries. | Medium |
| C8 | White-box model access is not a complete integrity guarantee. | Source-backed inference | E3 | Theoretical counterexample under explicit assumptions; not evidence that arbitrary deployed models contain such backdoors. | Medium |
| C9 | Acquisition burden should be optimized alongside predictive utility, but retrospective savings do not authorize clinical omission. | Reviewer interpretation | E8 | Strong design lesson; clinical transfer is intentionally rejected without prospective validation. | High |
| C10 | Verifiability is distributed across state, evidence, evaluators, and budgets rather than located in the model alone. | Derived inference | E2-E12 | Coherent synthesis, but no shared experiment compares the complete stack. | Medium |

## Methodology

- `Research objective`: Preserve and critically synthesize the ten works deposited in `Black-Lake-Data/.lake-data/DEP-20260713-Tech Intel 1104`, emphasizing reusable mechanisms for verifiable agent systems.
- `Sources inspected`: The selected DEP README and findings file; canonical arXiv metadata; complete PDFs for all ten papers; first-page visual renders for identity/layout checks; and official repositories for GRACE, LHTB, SAGEAgent, and ProofCouncil at the commits listed in Source Metadata.
- `Discovery strategy`: Source-first repository inspection followed by canonical identifier resolution, full-paper PDF extraction, targeted methods/results/limitations review, visual first-page verification, and official-link chasing only where the paper exposed an implementation or project page.
- `Inclusion criteria`: Every primary paper listed in the selected DEP, plus official implementation surfaces that materially clarified reproducibility, harness behavior, or evaluation scope.
- `Exclusion criteria`: Secondary commentary, unverified mirrors, unrelated bibliography items, inaccessible recap content, and sources discovered but not inspected. Related-reading entries are included only as primary or official follow-up routes.
- `Analytical approach`: Mixed conceptual, empirical, comparative, implementation, safety/ethics, product-research, and replication analysis.
- `Evidence handling`: Each major claim is mapped to a ledger ID. Paper results remain labeled as source claims; cross-paper design patterns are labeled reviewer interpretation or inference.
- `Uncertainty handling`: Version differences, private data, missing artifacts, theory assumptions, benchmark dependence, clinical limits, and non-reproduction are stated rather than smoothed over.
- `Extraction process`: Text was extracted page by page from temporary paper copies. Abstracts, methods, tables, results, conclusions, limitations, and threats-to-validity sections were inspected. First pages were rendered to confirm paper identity and readable layout.
- `Version control`: arXiv versions are listed explicitly. Four official repositories were pinned to immutable commits. The LHTB paper/repository model-count difference is preserved as a snapshot divergence.
- `Cross-checking`: Central metrics were checked against paper tables or conclusion text where available. Repository claims were treated as implementation context, not independent validation.
- `Safety handling`: Malware and incident-response material is defensive and non-operational. The backdoor result is discussed as an assurance boundary without procedural construction guidance. Clinical content is evaluation-only and non-diagnostic.
- `Reviewer stance`: DEP-ready preservation, critical synthesis, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Ten 2026 works covering agent context, model integrity, long-horizon evaluation, process-reward efficiency, persistent memory, security investigation, clinical acquisition, edge energy, mathematical agents, and grounded malware analysis.
- `Temporal boundary`: Sources and repository snapshots accessed through 2026-08-01.
- `Evidence limits`: No source code, model, benchmark, dataset, theorem, hardware trace, clinical workflow, malware sample, or production alert stream was executed or independently audited.
- `Assumptions`: Canonical arXiv records identify the reviewed revisions; official repository heads are the authors' intended implementation surfaces; reported metrics are transcribed accurately from inspected sources.
- `Constraints`: Public-output sanitization, source-redistribution restrictions, defensive security scope, privacy of production/clinical data, finite review time, and no authorization for operational malware or clinical testing.
- `Out of scope`: Independent replication, clinical recommendations, offensive security implementation, proof verification, energy measurement, model-backdoor construction, or production deployment endorsement.
- `Intended use`: DEP deposition, system-design review, evaluation planning, and a follow-on research backlog.
- `Audience`: Agent-system researchers, evaluation engineers, security reviewers, and product or infrastructure teams building auditable workflows.
- `Depth target`: Full manuscript review with source-preserving synthesis.
- `Reproducibility boundary`: Official code exists for four sources, but availability is not proof of reproducibility. Several datasets, production environments, models, or API versions remain inaccessible or costly.
- `Operational boundary`: The artifact may motivate defensive controls and synthetic tests; it does not operationalize backdoors, malware execution, intrusive investigations, or clinical decision making.
- `Data sensitivity`: Public papers and repositories were inspected; private production, malware, and patient data were not obtained.

## Observations

- `Observed pattern`: The strongest systems externalize the object being verified: a graph diff, task artifact, investigation tree, localized code evidence, modality state, or proof file.
- `Observed pattern`: Verification quality degrades when reviewer context becomes entangled with the producer's history. GRACE localizes change; ProofCouncil resets the critic; LHTB uses hidden graders; Malaika inserts a reviewer stage.
- `Technical implication`: A verifier should consume the smallest representation that preserves the decision-relevant evidence. KV-PRM uses cached internal state; GRACE uses affected graph neighborhoods; selective memory discards transient traces.
- `Technical implication`: Stop conditions require evidence, not confidence language. LHTB's continue-until-timeout behavior and ProofCouncil's fresh audit make this explicit.
- `Contradiction or tension`: More context can help or hurt. KV caches preserve high-dimensional signal for scoring, while full textual history can introduce stale or distracting traces. Representation and access policy matter more than raw volume.
- `Contradiction or tension`: Broad exploration raises recall but can reduce attribution precision. Malaika's comparison with frontier agents and SherAgent's dependency-explosion problem expose this tradeoff.
- `Contradiction or tension`: Cost reduction can remove useful evidence. SAGEAgent's RL baselines minimize burden at a large C-index cost, while excessive output truncation could make VLM responses unusable.
- `Open question`: Can one evidence-object schema span prompt evolution, long-horizon tasks, security investigations, and research proofs without erasing domain-specific semantics?
- `Open question`: Which verifier failures are independent enough that composition improves assurance rather than merely duplicating correlated model judgment?
- `Reviewer hypothesis`: The next useful agent-system benchmark should score evidence traceability, verifier independence, resource use, and calibrated abstention alongside task reward.

## Considerations

- **Governance:** Persistent state needs owners, permissions, version history, expiry rules, and rollback. Shared memory without fine-grained authorization can leak or misapply context.
- **Evaluation leakage:** Dense graders and repeated feedback can teach the agent the verifier rather than the task. Hidden checks need leakage analysis and adversarial test maintenance.
- **Verifier capture:** A model-based critic may share the producer's assumptions or prompt interpretation. Independent tools, fresh contexts, or human domain review should cover high-impact claims.
- **Resource accounting:** Token, latency, memory, energy, API cost, hardware, human review time, and acquisition burden are different currencies. A single scalar cost can hide unacceptable tradeoffs.
- **Security:** Logs, retrieved knowledge, tool output, and persistent memory are untrusted inputs. Systems need provenance, escaping, integrity checks, least privilege, and abstention on ambiguous chains.
- **Clinical safety:** Retrospective predictive utility cannot justify changing diagnostic care. Any acquisition policy requires prospective protocols, clinician oversight, subgroup analysis, and regulatory review.
- **Privacy:** Security alerts, patient data, workplace memory, and proof traces may contain sensitive material. Local processing, purpose limitation, access logs, minimization, and retention controls are first-class requirements.
- **Maintenance:** Benchmark harnesses, model APIs, repositories, threat knowledge, schemas, and hardware behavior change. Version pins and scheduled revalidation are required.

## Strengths

1. **Mechanism diversity:** The source set covers representation, evaluation, verification, provenance, physical cost, and human review rather than relying on one benchmark genre.
2. **Inspectability:** Several sources expose concrete artifacts - graph diffs, hidden graders, investigation trees, proof files, or code-grounded findings - that a later reviewer can audit.
3. **Explicit ablations:** GRACE, selective memory, SAGEAgent, and Malaika each isolate components, improving causal interpretation relative to headline-only comparisons.
4. **Operational evidence:** SherAgent includes production deployment; the edge-VLM paper measures real devices; shared memory includes enterprise workflows; ProofCouncil includes expert feedback.
5. **Released implementations:** GRACE, LHTB, SAGEAgent, and ProofCouncil provide official repositories with clearer reproduction surfaces than papers alone.
6. **Negative evidence:** The sources report failures such as stale-history degradation, timeout and critic errors, static-analysis blind spots, noise-overwhelmed investigations, and architecture coupling.

## Weaknesses

1. **Recent and mostly preprint evidence:** Peer review, revisions, and long-term independent replication remain limited.
2. **Heterogeneous evaluation:** Metrics and tasks differ too much for direct quantitative comparison across papers.
3. **Private or constrained data:** SherAgent, shared-memory enterprise tasks, clinical cohorts, and researcher-provided math problems cannot be fully audited from public evidence.
4. **Model and harness confounding:** Agent results depend on prompts, tools, model versions, retry policies, and evaluators; not all studies isolate these equally.
5. **Small or selective samples:** Several evaluations use tens of tasks, a 20-sample attribution subset, 170 complete clinical cases, or selected security incidents.
6. **Limited reproduction:** This review did not run any code, theorem checker, benchmark, dataset, or hardware measurement.
7. **Potential source overreach:** The SAGEAgent biopsy implication and the backdoor paper's broad integrity concern can be misread beyond their empirical or architectural scope.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Define a versioned evidence-object schema | Cross-domain architecture | State and claims need common lineage fields without flattening domain semantics | Easier audit, replay, and cross-tool handoff | Schema rigidity or leakage of sensitive details | Synthetic tasks in three domains plus migration tests |
| Add verifier-independence audits | Evaluation | Multiple LLM reviewers may share correlated errors | Better understanding of residual assurance | More model/tool cost | Compare same-model, fresh-context, different-model, deterministic-tool, and human review |
| Measure full resource vectors | Systems evaluation | Tokens alone omit latency, memory, energy, API cost, and reviewer burden | Honest deployment tradeoffs | Instrumentation complexity | Reproduce one workflow with matched quality and multidimensional cost reporting |
| Introduce calibrated abstention | Security and clinical systems | Ambiguous evidence currently becomes false attribution or unsafe recommendation | Lower harmful overclaiming | Reduced recall or more human work | Risk-coverage curves and subgroup error analysis |
| Freeze and publish evaluation manifests | Reproducibility | Repository and paper snapshots diverge | Repeatable results and clearer updates | Maintenance overhead | Immutable commit, dataset hash, harness patch, model identifier, seed, and expected outputs |
| Test state decay and revocation | Persistent memory | Useful state becomes stale or unauthorized | Safer long-lived reuse | Loss of useful context | Simulated schema drift, role changes, and rollback exercises |
| Separate progress reward from completion proof | Long-horizon agents | Dense partial credit can mask unsatisfied final invariants | Better stopping calibration | More verifier authoring | Holdout tasks with independent end-state reconstruction |
| Add prospective clinical governance before any care use | SAGE-style acquisition | Retrospective burden models cannot authorize omitted tests | Patient-safety boundary | High study and regulatory cost | Prospective silent trial, clinician adjudication, subgroup monitoring, then controlled study |

## Potential Implementations

### 1. Versioned Context Registry

- `User`: Agent-platform engineers and safety reviewers.
- `Goal`: Maintain persistent instructions and reusable workspace context without retaining unrestricted traces.
- `Core mechanism`: Typed state objects, scoped diffs, compatibility checks, review gates, expiry, and rollback.
- `Required inputs`: Current state, proposed update, evidence links, schema, owner, and policy metadata.
- `Outputs`: Accepted/rejected diff, reconstructed instruction, validation report, lineage record, and rollback handle.
- `Risk controls`: Least privilege, sensitive-field redaction, immutable audit log, adversarial-input checks, and mandatory human approval for high-impact changes.
- `Evaluation`: Shifted synthetic tasks measuring retained gains, contradiction rate, rollback correctness, stale-state detection, and reviewer time.

### 2. Progress-Aware Agent Harness

- `User`: Evaluation teams testing long-running coding, research, or data agents.
- `Goal`: Distinguish useful partial work from verified completion and diagnose stop failures.
- `Core mechanism`: Artifact-derived milestone checks, hidden end-state reconstruction, bounded feedback-resume loops, and resource telemetry.
- `Required inputs`: Containerized task, milestone verifier set, final invariant checker, budget, and restart policy.
- `Outputs`: Reward trajectory, verified completion state, cost vector, failure taxonomy, and replay bundle.
- `Risk controls`: Holdout verifiers, leakage tests, sandboxing, deterministic resets, and capped retries.
- `Evaluation`: Compare binary-only and dense-grading variants on matched tasks, measuring solve rate, calibration, loops, and cost.

### 3. Evidence-Grounded Triage Console

- `User`: Authorized SOC or software-security analysts.
- `Goal`: Produce reviewable hypotheses from fragmented logs or static artifacts without converting weak signals into confident attribution.
- `Core mechanism`: Provenance queries, localized evidence retrieval, external knowledge mapping, independent review, and explicit insufficient-evidence outcomes.
- `Required inputs`: Sanitized authorized logs or static-analysis artifacts, schema, threat knowledge, and analyst-defined scope.
- `Outputs`: Evidence graph, hypotheses, confidence/abstention label, cited findings, and analyst review queue.
- `Risk controls`: No active exploitation, command sanitization, log-injection defenses, tenant isolation, data minimization, and human confirmation.
- `Evaluation`: Historical defensive cases with blinded analyst labels, false-attribution cost, evidence coverage, review time, and adversarial-log tests.

### 4. Resource-Budget Controller

- `User`: Edge-AI and multi-agent inference operators.
- `Goal`: Allocate verification and response budgets while preserving task utility.
- `Core mechanism`: KV-state reuse where compatible, output-length policies, per-stage cost telemetry, and quality-aware budget escalation.
- `Required inputs`: Model/hardware profile, task type, quality target, state compatibility, and latency/energy ceiling.
- `Outputs`: Selected verifier route, output cap, predicted cost, measured cost, and fallback decision.
- `Risk controls`: Minimum-answer requirements, architecture compatibility checks, privacy-preserving telemetry, and fail-open prohibition for safety gates.
- `Evaluation`: Matched-quality experiments across short/long outputs, cache reuse, hardware, and verifier configurations.

## Three Ways to Exercise This Research

1. **Synthetic context-shift audit:** Objective: test whether typed, selective state resists stale or conflicting updates. Inputs: a toy support-agent policy, ten synthetic experience batches, a small typed schema, and deterministic tests. Method: compare flat-text rewrite, append-only memory, and scoped typed diffs with consolidation. Output: versioned state, contradiction counts, retained-task scores, and rollback traces. Success criterion: improved shifted-task performance without regression beyond a predefined bound. Stop condition: budget exhausted, a privacy/safety rule is violated, or no method passes the fixed invariants. Safety boundary: synthetic data only and no production policy deployment.
2. **Hidden-verifier stopping study:** Objective: measure whether agents stop when artifacts are actually complete. Inputs: three containerized toy tasks, dense milestone graders, an independent final checker, and a fixed time/token budget. Method: compare self-declared completion, binary final grading, and feedback-resume grading. Output: progress curves, false-completion rate, cost vector, and replay logs. Success criterion: lower false completion without unbounded cost. Stop condition: final checker passes or the fixed budget ends. Safety boundary: local sandbox, no credentials, and no external writes.
3. **Defensive evidence-grounding drill:** Objective: evaluate calibrated attribution from benign synthetic event graphs and toy Android-like code fragments. Inputs: labeled evidence, planted missing edges, ambiguous benign behaviors, and a small public threat taxonomy. Method: run hypothesis generation, evidence localization, knowledge mapping, and an independent reviewer with an explicit abstain option. Output: cited findings, evidence graph, precision/recall, abstention rate, and review time. Success criterion: fewer unsupported attributions than an unguided baseline at an acceptable recall floor. Stop condition: an item lacks authorization, evidence provenance fails, or the evaluation set is exhausted. Safety boundary: no real malware, no offensive actions, and no production telemetry.

## Example MVP Product

- `Product name`: Evidence Loop Workbench
- `Target user`: Teams building or evaluating long-running agents in controlled research and engineering environments.
- `Problem`: Agent runs expose abundant text but weak evidence about what state changed, which milestones truly passed, why a claim was accepted, and how much the process cost.
- `Core workflow`: A user registers a task schema and budget; the workbench snapshots durable state; an agent produces artifacts and evidence links; deterministic or independent verifiers score milestones; failed checks return bounded feedback; accepted updates are committed to a lineage graph; the run stops on verified completion, evidence exhaustion, or budget.
- `Data requirements`: Synthetic or explicitly authorized task inputs, repository artifacts, verifier outputs, cost telemetry, state metadata, and optional reviewer decisions. Raw secrets and unrestricted reasoning traces are excluded.
- `Architecture`: Local-first orchestration service; append-only evidence store; typed state registry; sandboxed task runner; verifier adapters for deterministic checks, fresh-model review, and human approval; policy engine; audit UI; exportable Markdown/JSON report.
- `Success metrics`: Verified-completion rate; false-completion rate; unsupported-claim rate; retained performance after state updates; rollback success; verifier disagreement; token/latency/memory/energy/API/reviewer cost; and time to audit one decision.
- `Risk controls`: Least-privilege tools, explicit destinations, content/provenance validation, state expiry, encrypted local storage, redaction, immutable audit events, capped retries, abstention, and mandatory human review for security, clinical, legal, or irreversible actions.
- `Limitations`: The MVP cannot prove semantic correctness, eliminate correlated evaluator error, validate clinical decisions, safely analyze real malware by default, or normalize every resource type into one objective.
- `MVP boundary`: Synthetic/local tasks, Markdown/JSON artifacts, deterministic verifiers, and one optional fresh-model reviewer. No autonomous deployment, external messaging, clinical workflow, or offensive security capability.
- `Deployment model`: Local desktop or single-tenant service with offline-capable deterministic evaluation.
- `Evaluation plan`: Unit tests for lineage and rollback; three synthetic exercise suites above; red-team tests for prompt/log injection; blinded human audit of twenty decisions; and acceptance thresholds set before evaluation.
- `Failure modes`: Stale schemas, verifier leakage, correlated model judgment, hidden cost, evidence laundering, excessive abstention, and false confidence from passing incomplete tests.
- `Maintenance plan`: Versioned schemas and verifier manifests, pinned dependencies, monthly drift review, rotating hidden tests, and documented deprecation of state or knowledge snapshots.

## Related Research and Reading

This is an initial pass for the selected DEP; all entries below are new to this artifact rather than expansions of an older Report-Mark.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| GRACE official repository at `b8b6b9a` | Official implementation | Reproduction and domain-integration surface for typed context evolution | https://github.com/RedMind-Research/GRACE/tree/b8b6b9adbb1cd868a7298c8526b2f2e3774ccab4 |
| LHTB official repository at `b695ed2` | Official benchmark | Exposes tasks, hidden graders, modified Harbor behavior, and current snapshot differences | https://github.com/zli12321/LHTB/tree/b695ed2eaa41b95fd60949e595955fc8e60eac32 |
| Long-Horizon-Terminal-Bench dataset | Official dataset card | Public task-distribution and benchmark access route | https://huggingface.co/datasets/IntelligenceLab/Long-Horizon-Terminal-Bench |
| SAGEAgent official repository at `5fcb694` | Official implementation | Exposes predictor, uncertainty, memory, reflection, and nested-evaluation scripts | https://github.com/Chongyu1117/SAGEAgent/tree/5fcb6941879d3bc25a99aaec203bc23f56e0e1af |
| ProofCouncil official repository at `2555c79` | Official implementation | Reusable conditional-DAG agent runner, trace UI, cost accounting, and smoke workflows | https://github.com/eth-sri/proof-council/tree/2555c798013603748c5556866c89a9eae5795d48 |
| Tau2-bench | Primary benchmark paper | Underlying dual-control telecom environment used by GRACE | https://arxiv.org/abs/2506.07982 |
| FirstProof Second Batch | Primary challenge report | Independent context for ProofCouncil's ten-problem evaluation | https://arxiv.org/abs/2606.18119 |
| MalEval | Primary benchmark paper | Analyst-validated behavior annotations used by Malaika | https://arxiv.org/abs/2509.14335 |
| MITRE ATT&CK Mobile | Official knowledge base | Standardized mobile threat-technique vocabulary used for knowledge grounding | https://attack.mitre.org/matrices/mobile/ |
| Open Cybersecurity Schema Framework | Official standard repository | Provenance/log schema context for large-scale defensive investigation | https://github.com/ocsf/ocsf-schema |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [Selected source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/2bebe12af935e746e37ccc8354beebe03c0694b7/.lake-data/DEP-20260713-Tech%20Intel%201104) | Source inventory and original ten-finding synthesis | 2026-08-01 | Primary repository source; recap share remained inaccessible |
| R1 | [arXiv:2607.09175v1](https://arxiv.org/abs/2607.09175) | GRACE mechanism, protocol, results, and limits | 2026-08-01 | Complete paper inspected |
| R2 | [arXiv:2607.09532v1](https://arxiv.org/abs/2607.09532) | Undetectable-backdoor theory and preliminary experiments | 2026-08-01 | Complete paper inspected; defensive interpretation only |
| R3 | [arXiv:2607.08964v2](https://arxiv.org/abs/2607.08964) | LHTB task design, paper-snapshot results, and failures | 2026-08-01 | Complete paper inspected |
| R4 | [arXiv:2607.09153v1](https://arxiv.org/abs/2607.09153) | KV-PRM mechanism, efficiency, benchmarks, and assumptions | 2026-08-01 | Complete paper inspected |
| R5 | [arXiv:2607.09493v1](https://arxiv.org/abs/2607.09493) | Selective-memory architecture and evaluations | 2026-08-01 | Complete paper inspected |
| R6 | [arXiv:2607.09176v1](https://arxiv.org/abs/2607.09176) | SherAgent production workflow, evaluation, and failure cases | 2026-08-01 | Complete paper inspected; private production data not accessed |
| R7 | [arXiv:2607.09521v1](https://arxiv.org/abs/2607.09521) | SAGEAgent clinical-acquisition method, results, and limits | 2026-08-01 | Complete paper inspected; non-diagnostic use |
| R8 | [arXiv:2607.09520v1](https://arxiv.org/abs/2607.09520) | Edge-VLM power, timing, energy, and prompt findings | 2026-08-01 | Complete paper inspected |
| R9 | [arXiv:2607.09474v1](https://arxiv.org/abs/2607.09474) | ProofCouncil workflow, evaluation, costs, and limitations | 2026-08-01 | Complete paper inspected |
| R10 | [arXiv:2607.09179v1](https://arxiv.org/abs/2607.09179) | Malaika architecture, results, ablations, and validity threats | 2026-08-01 | Complete paper inspected; defensive static analysis only |
| R11 | [GRACE repository](https://github.com/RedMind-Research/GRACE/tree/b8b6b9adbb1cd868a7298c8526b2f2e3774ccab4) | Reproduction and integration surface | 2026-08-01 | README inspected at immutable commit |
| R12 | [LHTB repository](https://github.com/zli12321/LHTB/tree/b695ed2eaa41b95fd60949e595955fc8e60eac32) | Current harness, tasks, and leaderboard snapshot | 2026-08-01 | README inspected at immutable commit; 21-model live snapshot differs from 17-model paper |
| R13 | [LHTB dataset](https://huggingface.co/datasets/IntelligenceLab/Long-Horizon-Terminal-Bench) | Public benchmark distribution route | 2026-08-01 | Discovered through official project page; not downloaded |
| R14 | [SAGEAgent repository](https://github.com/Chongyu1117/SAGEAgent/tree/5fcb6941879d3bc25a99aaec203bc23f56e0e1af) | Code layout and evaluation protocol | 2026-08-01 | README inspected at immutable commit; code not executed |
| R15 | [ProofCouncil repository](https://github.com/eth-sri/proof-council/tree/2555c798013603748c5556866c89a9eae5795d48) | Conditional-DAG implementation and run surfaces | 2026-08-01 | README inspected at immutable commit; code not executed |
| R16 | [Tau2-bench](https://arxiv.org/abs/2506.07982) | GRACE environment context | 2026-08-01 | Related primary paper; used for context only |
| R17 | [FirstProof Second Batch](https://arxiv.org/abs/2606.18119) | ProofCouncil challenge context | 2026-08-01 | Related primary report; used for context only |
| R18 | [MalEval](https://arxiv.org/abs/2509.14335) | Malaika benchmark context | 2026-08-01 | Related primary paper; used for context only |
| R19 | [MITRE ATT&CK Mobile](https://attack.mitre.org/matrices/mobile/) | Mobile threat-knowledge context | 2026-08-01 | Official knowledge base; used for context only |
| R20 | [OCSF](https://github.com/ocsf/ocsf-schema) | Security-event schema context | 2026-08-01 | Official repository; used for context only |

## Appendix

### Public Source Inventory

- Source DEP: README and `daily_research_findings_2026-07-13_1104.md` at snapshot `2bebe12`.
- Primary papers: ten canonical arXiv records and complete PDFs, versions listed in Source Metadata.
- Official implementations: GRACE, LHTB, SAGEAgent, and ProofCouncil at immutable commits.
- No PDF, extracted text, rendered page, repository clone, dataset, model, malware sample, patient record, production alert, benchmark payload, or execution trace is deposited in this DEP-E entry.

### Replication Checklist

- [ ] Freeze paper, code, dataset, harness, model/API, and dependency versions.
- [ ] Record task/sample inclusion rules and exclusions before running.
- [ ] Separate producer, stateful reviewer, fresh reviewer, deterministic checker, and human ground truth.
- [ ] Capture artifacts and evidence links rather than only narrative traces.
- [ ] Record tokens, latency, memory, energy, API cost, hardware, and human review time where relevant.
- [ ] Define completion, abstention, timeout, and rollback conditions in advance.
- [ ] Report negative results, disagreements, and inaccessible evidence.
- [ ] Apply domain-specific safety review before security, clinical, or high-impact use.

### Review Limitations

The review verified document identity, source metadata, reported methods, principal tables/results, explicit limitations, and selected official repositories. It did not verify theorem proofs, regenerate figures, reproduce statistics, execute code, audit licenses beyond visible repository statements, or validate private evaluation data. Quantitative claims should be read as source-reported results tied to the exact versions and conditions above.
