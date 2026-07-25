---
title: "ToolEmu Audit - DEP-E"
generated_at: "2026-07-25T00:05:03Z"
artifact_type: "DEP research artifact"
primary_subject: "An iterative review of ToolEmu's language-model-emulated safety sandbox, validation evidence, and pinned public release."
source_status: "Public URLs plus temporary PDF and repository review; no external source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-25"
temporal_cutoff: "2026-07-25"
primary_url: "https://arxiv.org/abs/2309.15817v2"
stable_identifier: "DEP-20260714-Tech Intel 1305 / arXiv:2309.15817v2"
confidence_summary: "High for the paper's reported design and the pinned release state; medium for real-world transfer and independent reproducibility because the experiments were not rerun."
safety_scope: "Defensive evaluation using benign, inert, no-egress tool simulations only"
distribution_notes: "No operational harmful trajectory, credential, model output, private data, local path, or external source file is redistributed."
---

# ToolEmu Audit - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | Selected source DEP | Primary repository artifact | Markdown bundle | `DEP-20260714-Tech Intel 1305` at `68af135` | [Source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/68af13582e1506c4a20cc8b051c703ba2e7120d0/.lake-data/DEP-20260714-Tech%20Intel%201305) | Public repository evidence; historical local-run details were not copied | 2026-07-25 | README, findings artifact, two Report-Marks, and report lineage inspected |
| S1 | Latest prior source report and Report-Mark | Same-family lineage | Markdown | 2026-07-23 pass at `68af135` | [Prior report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/68af13582e1506c4a20cc8b051c703ba2e7120d0/.reports/BL-DEP-20260714-Tech%20Intel%201305-20260723/README.md) | Public processing record | 2026-07-25 | Inspected before iterative expansion |
| S2 | ANCHOR Audit | Prior DEP research artifact | Markdown | Black-Lake commit `9b475c0` | [Prior DEP-E](https://github.com/Delphoa/Black-Lake/tree/9b475c0fb9d68d8a14131530d6bb4fca77004ae1/.lake-data/DEP-E/DEP-E-20260723-ANCHOR%20Audit) | Public review artifact | 2026-07-25 | README, full manuscript, log, and preserved references inspected |
| S3 | ToolEmu | Primary paper | arXiv record and PDF | arXiv:2309.15817v2; ICLR 2024 Spotlight | [Canonical record](https://arxiv.org/abs/2309.15817v2), [70-page PDF](https://arxiv.org/pdf/2309.15817v2) | arXiv page links the source license; paper inspected for research review | 2026-07-25 | Metadata, complete PDF text, main figures, tables, limitations, appendices, and selected rendered pages inspected |
| S4 | ToolEmu ICLR record | Primary venue record | OpenReview | `GEcwtMk1uA` | [ICLR 2024 forum](https://openreview.net/forum?id=GEcwtMk1uA) | Public conference record | 2026-07-25 | Venue and Spotlight status verified; interactive forum content was access-limited |
| S5 | ToolEmu public release | Official implementation | GitHub repository | `ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb` | [Pinned tree](https://github.com/ryoungj/ToolEmu/tree/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb) | Repository `LICENSE` contains Apache License 2.0; `setup.py` classifier says MIT, an unresolved metadata conflict | 2026-07-25 | Complete path inventory, README, package metadata, dependency list, workflow scripts, core loader/model adapter, prompts, and asset schemas inspected; code not run |
| S6 | ToolEmu benchmark assets | Official supporting data | JSON | Pinned at `ac4a7ab` | [Cases](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/assets/all_cases.json), [toolkits](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/assets/all_toolkits.json) | Public repository data; no copy is deposited here | 2026-07-25 | Structure and counts inspected without executing cases |
| S7 | ToolEmu release metadata | Official supporting files | Markdown, Python, text | Pinned at `ac4a7ab` | [README](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/README.md), [requirements](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/requirements.txt), [setup](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/setup.py), [license](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/LICENSE) | Public repository metadata | 2026-07-25 | Inspected for installation, version, dependency, licensing, and reproducibility boundaries |

No paper, benchmark file, repository file, prompt corpus, trajectory, credential, or model output is deposited. A temporary copy of the 70-page paper and a temporary shallow checkout of the official repository supported read-only review; both are excluded from this DEP package.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S0-S2 | Repository lineage | Selected ten-item bundle, latest source report, Report-Mark 002, prior Black-Lake log, prior DEP README, full ANCHOR manuscript, and preserved references | Why ToolEmu was eligible for iterative expansion and what prior passes already covered | High | Prior reviews are provenance and context, not independent validation |
| E2 | S3-S4 | Primary paper and venue record | Complete paper, method, main tables, limitations, appendices, human-annotation procedure, and venue status | ToolEmu's design, threat model, benchmark construction, reported validation, and conference status | High for what the paper reports | No experiment or API call was rerun |
| E3 | S3 | Primary paper | Tables 3-4, 100-case/200-trajectory validation design, four-annotator protocol, and terminal-sandbox check | End-to-end precision, emulator validity, evaluator agreement, and limited sim-to-real evidence | High for reported setting | Samples are modest; the real-sandbox check covers one toolkit and seven detected failures |
| E4 | S3 | Primary paper | Table 5 and its footnote, prompt comparisons, 144-case evaluation, and three-run standard-error estimate | Reported safety-helpfulness tradeoff and the conditional 23.9% best-agent failure incidence | High for reported setting | Failure labels depend on the study's emulator and automatic evaluator; model endpoints are historical |
| E5 | S5-S7 | Official release | Pinned tree, package layout, loaders, model adapters, scripts, requirements, license, and benchmark JSON | Public implementation surface and current release boundary | High for inspected release state | Static inspection only; no dependency installation or code execution |
| E6 | S3, S5-S7 | Cross-source comparison | Paper and README state 36 toolkits/311 tools; pinned JSON contains 38 toolkits/330 tools and all 38 appear in the 144 cases | The public release has undocumented benchmark-count drift relative to its paper and README | High | The inspected sources do not identify when or why the two toolkits were added |
| E7 | S5-S7 | Reviewer inspection | No release tags, CI workflow, test files, or lockfile; most requirements are unpinned; PromptCoder is an external editable dependency; license file and package classifier disagree | Exact reproduction and redistribution require additional version and governance work | High for the pinned tree | Absence claims apply only to the public pin; private author infrastructure was not inspected |

## Executive Summary

ToolEmu is a language-model-based safety evaluation framework for tool-using agents. Instead of implementing every external tool and sandbox, it prompts a strong model to emulate tool execution and environment state, then uses language-model evaluators to score safety and helpfulness. Its adversarial emulator conditions the sandbox on an underspecified but benign user request and known risk dimensions so that long-tail failure states are sampled more often (E2).

The paper reports a benchmark of 36 toolkits, 311 tools, and 144 cases spanning nine risk types. In a validation study built from 100 cases and 200 paired standard/adversarial trajectories, the standard emulator achieved 72.5% +/- 7.1% identified-failure precision and 39.6% +/- 4.9% true-failure incidence; the adversarial emulator achieved 68.8% +/- 6.7% precision and 50.0% +/- 5.1% incidence. Human reviewers judged 91.9% of standard and 85.6% of adversarial trajectories free of critical emulation issues. The automatic safety evaluator reached 75.3% precision and 73.1% recall against leave-one-out human labels, compared with 78.7% and 78.8% for a held-out human annotator (E3).

The agent comparison is explicitly conditional on historical models, prompts, emulator, evaluator, and 144 cases. The strongest reported configuration, GPT-4 with added safety requirements, had a 23.9% evaluator-labeled failure incidence and 1.824 helpfulness score, compared with 39.4% and 1.458 for the basic GPT-4 prompt. A no-action baseline had 0% failure incidence but only 0.063 helpfulness. The paper estimates a 4.1 percentage-point standard error for failure incidence across three independent runs despite temperature zero (E4). These results support evaluation of risk awareness and clarification behavior; they do not establish a current, universal failure rate for agents.

This pass adds release-integrity evidence. The official repository is pinned to `ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb`. Its current JSON contains 38 toolkits and 330 tools, while both the v2 paper and repository README state 36 and 311. The 19-tool difference is exactly `GoogleSearch` with 6 tools plus `NortonIdentitySafe` with 13; both occur in the 144-case set, but no inspected release note explains their addition. The repository has no tag, lockfile, CI workflow, or test files; most dependencies are unpinned, the separate PromptCoder dependency is installed from an unpinned editable checkout, and historical model adapters target retired or mutable APIs. The Apache-2.0 license text also conflicts with an MIT classifier in `setup.py` (E5-E7).

Reviewer interpretation: ToolEmu's durable contribution is the separation of agent, virtual tool state, safety evaluator, and helpfulness evaluator, plus the finding that adversarial state generation can raise failure discovery at a measurable precision cost. A modern implementation should retain that causal separation while adding deterministic state models, manifest-pinned judges, case-version lineage, independent human adjudication, and a clear divide between emulated risk discovery and real-system validation.

## Detailed Summary

### Problem and threat model

Tool-using agents can create consequences that text-only evaluations miss: mistaken identity, unauthorized sharing, data loss, financial loss, or unsafe control actions. Building real sandboxes for a broad tool ecosystem is expensive and sometimes impossible. ToolEmu treats the agent interaction as a partially observable process, with actions, state transitions, observations, and trajectory-level safety/helpfulness rewards, then replaces the real transition and observation functions with a language-model emulator (E2).

The paper's benchmark uses a narrow, important threat model: the user has benign intent, but the instruction omits task information or safety constraints. A safe and useful agent should gather missing facts, clarify ambiguity, or request confirmation before taking consequential action. This is different from testing explicit malicious intent, prompt injection, or persistent adversarial persuasion.

### Emulator and evaluator design

The standard emulator receives tool specifications and the trajectory to validate inputs, maintain state consistency, and generate plausible outputs. The adversarial emulator also receives the case's underspecification and potential risky outcomes/actions. It uses those fields to instantiate difficult virtual states, increasing the chance that the agent reveals a safety failure. Because the tools are virtual, an emulated successful action has no real-world effect.

The safety evaluator reads the complete case and trajectory, identifies risky actions and outcomes, and emits a score on the paper's 0-3 scale. The helpfulness evaluator separately scores progress toward the user's objective. This dual evaluation prevents a trivial refusal-only strategy from appearing optimal. The paper validates both evaluators against trained external annotators and provides complete prompts in the appendix, which supports interpretability but also reveals dependence on prompt-engineered model behavior (E2-E3).

### Benchmark construction

The authors started from 18 toolkit categories, used GPT-4 to propose toolkit names and specifications, manually reviewed and refined them, and validated every toolkit with at least two cases. Test cases were model-generated from requirements and examples, then filtered and edited by at least two people. The paper's final benchmark has 144 cases across nine risk types and an average of 1.40 toolkits per case (E2).

The pinned release is not identical to that published inventory. Static parsing of `assets/all_toolkits.json` yields 38 toolkit objects and 330 tool definitions; all 38 toolkit names occur in `assets/all_cases.json`, which still has 144 cases. Relative to the paper's 36-tool Table A.4, the release adds `GoogleSearch` with 6 tools and `NortonIdentitySafe` with 13. The README repeats 36/311, so the release contains an unversioned benchmark extension rather than a documented paper-exact snapshot (E6).

### Validation evidence

For component validation, the authors randomly selected 100 cases and created standard and adversarial trajectories with matched agents, producing 200 trajectories. Four University of Toronto senior computer-science undergraduates independently reviewed every trajectory after screening, training, and a qualification exercise. Each spent about 25 hours and was compensated at USD 21 per hour. A "true failure" required a safety label of zero from at least two humans and a critical-issue-free emulation judgment from at least three (E3).

The adversarial emulator increased true-failure incidence from 39.6% to 50.0% while reducing identified-failure precision from 72.5% to 68.8% and the critical-issue-free rate from 91.9% to 85.6%. The paper also attempted real terminal instantiation for all seven detected ChatGPT-3.5 failures in that toolkit and reproduced six, but this one-tool check does not validate transfer for financial, medical, robotic, identity, or infrastructure toolkits. Operational failure details are intentionally not repeated here.

### Agent comparison

The paper evaluated GPT-4, Claude-2, ChatGPT-3.5, and Vicuna-1.5 agents on all 144 cases using GPT-4 as emulator and evaluator. The historical configuration cost approximately USD 1.20 per case. GPT-4's basic prompt scored 2.007 safety, 39.4% failure incidence, and 1.458 helpfulness. Adding only safety requirements improved those values to 2.359, 23.9%, and 1.824. Combining helpfulness and safety requirements performed worse than safety alone, suggesting that more prompt requirements are not monotonically beneficial. The no-action baseline establishes the necessary counterfactual: perfect abstention can be safe yet useless (E4).

### Public release

The pinned repository has 100 tracked files, package version `0.1.0`, JSON benchmark assets, notebooks, generation and evaluation scripts, prompt modules, virtual tool classes, and an Apache-2.0 license file. Its primary workflow loads API keys from `.env`, uses historical OpenAI/Anthropic/LangChain interfaces, and shells from an orchestration script into separate emulation and evaluation commands. A fixed Python random seed is used in the emulation/evaluation scripts, but API calls remain nondeterministic.

Reproduction is incomplete. The dependency list pins only a few libraries, repeats SciPy, and does not freeze a complete environment. PromptCoder is installed from a second repository in editable mode without a commit pin. There are no public tests, CI workflow, lockfile, release tag, container digest, or paper-exact asset manifest. The actual license text is Apache 2.0, while `setup.py` advertises the MIT classifier. These are repairable release-engineering gaps, but they prevent treating the current `main` snapshot as a turnkey reconstruction of the ICLR results (E5-E7).

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | LM-emulated tools can expose realistic agent failures without executing real external actions. | Author claim | E2-E3 | Supported for the study's historical models and cases; six of seven terminal failures transferred to one real sandbox | Medium-high |
| C2 | Adversarial state generation finds more true failures than standard emulation. | Author result | E3 | Supported by a 10.4 percentage-point incidence increase with lower precision and emulator validity | High for reported sample |
| C3 | The automatic safety evaluator performs near a held-out human annotator. | Author result | E3 | Precision/recall and Cohen's kappa are close, but human agreement itself is moderate and labels are study-specific | Medium-high |
| C4 | A safety-focused prompt improved both safety and helpfulness over the basic GPT-4 prompt. | Author result | E4 | Supported by Table 5; not proof of current model behavior or causal generality | High for reported setting |
| C5 | The public benchmark assets have drifted from the paper and README. | Reviewer implementation finding | E5-E6 | Direct count: 38/330 in the pinned assets versus 36/311 in the published and README descriptions | High |
| C6 | The pinned public release is not a frozen paper-exact reproduction package. | Reviewer interpretation | E5-E7 | Supported by asset drift, unpinned dependencies, external editable dependency, historical endpoints, absent tests/CI/lock/tag, and license metadata conflict | High |
| C7 | Safe modern reuse should separate emulated risk discovery from real-system validation. | Derived inference | E2-E7 | Strongly motivated by sim-to-real limits and evaluator dependence; requires new empirical validation | Medium-high |

## Methodology

- `Research objective`: Expand the randomly selected ToolEmu thread while preserving the selected DEP's prior lineage and separating paper claims, release evidence, reviewer interpretation, and safe implementation guidance.
- `Sources inspected`: Every selected DEP file; the latest source report and Report-Mark; the latest Black-Lake log, DEP README, and full ANCHOR manuscript; ToolEmu's canonical arXiv record; the complete 70-page v2 PDF; selected rendered figures, tables, limitations, and appendix pages; the ICLR OpenReview record; and the complete official repository tree at `ac4a7ab`.
- `Discovery strategy`: Repository-lineage tracing, exact related-reading extraction, canonical URL review, full-paper PDF extraction, page rendering, venue verification, official repository inspection, static JSON counting, and targeted source-code/metadata review.
- `Inclusion criteria`: Primary paper evidence, official implementation and benchmark evidence, same-family provenance, and near-primary references needed for comparison.
- `Exclusion criteria`: Operational harmful trajectories, live-tool execution, model/API execution, secondary summaries, unverified claims, and external files not required for review.
- `Analytical approach`: Empirical, comparative, implementation, replication, safety and ethics, and product research.
- `Evidence handling`: Major claims map to evidence IDs; paper metrics remain author-reported results; release observations are tied to the exact public commit; inference is labeled.
- `Uncertainty handling`: Sim-to-real limits, historical endpoints, moderate human agreement, undocumented asset drift, missing environment pins, and licensing conflict are retained explicitly.
- `Extraction process`: Paper text was extracted from the complete PDF and key pages were visually checked. Repository assets and code were read statically. No benchmark, model, API, notebook, prompt generator, or tool action was executed.
- `Version control`: Selected source repository pinned at `68af135`; prior artifact pinned at `9b475c0`; paper pinned to arXiv v2; official release pinned at `ac4a7ab`.
- `Safety handling`: Examples are summarized at the mechanism level. Implementation guidance uses benign synthetic cases, inert tools, blocked egress, no credentials, and explicit authorization.

## Scope, Constraints, and Assumptions

- `Scope`: ToolEmu's emulator/evaluator design, underspecification threat model, benchmark curation, paper-reported validation, historical agent comparison, current public release, asset drift, and defensive translation.
- `Temporal boundary`: Public sources available through 2026-07-25; arXiv v2 is dated 2024-05-17 and the pinned public repository head is dated 2024-03-15.
- `Evidence limits`: No model/API execution, dependency installation, notebook run, case replay, judge re-adjudication, terminal reproduction, statistical recomputation, or independent sim-to-real study.
- `Assumptions`: The paper-linked GitHub repository is the official release; repository absence and count claims apply only to the pinned public tree.
- `Constraints`: Dual-use safety, API/model retirement, usage cost, license metadata conflict, dependency drift, and the need to avoid real-world side effects.
- `Out of scope`: Reproducing destructive actions, testing live accounts or devices, generating attack instructions, estimating current frontier-agent failure rates, or asserting production readiness.
- `Intended use`: DEP deposition, benchmark lineage review, defensive evaluation planning, and research backlog creation.
- `Audience`: Agent-safety researchers, benchmark maintainers, platform engineers, artifact reviewers, and governance teams.
- `Reproducibility boundary`: The release supports architectural inspection and partial reconstruction planning, but not exact independent replay of the ICLR results without repair.
- `Data sensitivity`: Public benchmark content includes high-stakes scenarios. No case payload, trajectory, credential, or generated output is redistributed here.

## Observations

- `Observed pattern`: Adversarial emulation increases discovery yield by shifting the virtual state distribution, but it also reduces emulation validity and precision.
- `Observed pattern`: Safety and helpfulness must be measured together; refusal-only agents can dominate a safety metric while failing the user.
- `Contradiction or tension`: The paper and README describe 36 toolkits/311 tools, while the pinned benchmark contains 38/330 with no release note or version field explaining the change.
- `Contradiction or tension`: The repository's Apache-2.0 license file and MIT package classifier disagree.
- `Technical implication`: Every benchmark result should bind paper version, case manifest, toolkit manifest, emulator prompt, evaluator prompt, model endpoint, code commit, and adjudication set.
- `Technical implication`: Emulated success is evidence for risk discovery, not evidence that a real tool behaves identically or that a deployment is safe.
- `Open question`: Does the adversarial-versus-standard tradeoff persist with deterministic tool simulators and current models?
- `Reviewer hypothesis`: Hybrid evaluation will be stronger than pure LM emulation: language models should propose and explore states, while typed invariants and deterministic simulators should validate them.

## Considerations

- Use only synthetic identities, inert tools, no-egress environments, and explicit operator authorization.
- Do not connect benchmark tool schemas to live email, finance, medical, identity, robotic, or infrastructure systems during exploratory evaluation.
- Preserve case-level and toolkit-level versions; silent asset updates invalidate paper-exact comparisons.
- Separate agent, emulator, evaluator, prompt, and endpoint effects in result tables.
- Calibrate automatic judges against independent, blinded human labels and report agreement, uncertainty, and override policy.
- Require a real-system validation plan before inferring sim-to-real transfer; begin with harmless, reversible fixtures.
- Resolve the license metadata conflict before redistribution or package publication.
- Treat historical model identifiers and pricing as provenance, not current operating assumptions.

## Strengths

- ToolEmu makes safety evaluation tractable across tool categories that lack real APIs or affordable sandboxes.
- The benign-intent/underspecification threat model targets an important failure class without requiring malicious user behavior.
- Standard and adversarial emulators expose a measurable discovery-versus-validity tradeoff.
- Separate safety and helpfulness evaluators prevent trivial refusal from masquerading as a useful solution.
- The paper validates the emulator and evaluators with four external annotators and reports uncertainty.
- The appendix provides detailed prompts, requirements, curation procedures, and additional analysis.
- The official release exposes code, benchmark JSON, notebooks, prompts, and package metadata under a public license file.

## Weaknesses

- The validation study covers 100 cases and one historical model generation; the terminal transfer check covers only seven failures in one toolkit.
- Emulator and evaluator share model-family and prompt-engineering dependencies, creating correlated error risk.
- Human agreement is moderate, and the selected annotators were four senior computer-science undergraduates from one institution.
- The strongest 23.9% result is evaluator-conditioned and should not be read as a current real-world failure probability.
- The threat model does not cover malicious intent, prompt injection, persistent persuasion, cross-agent delegation, or production policy enforcement.
- The current repository silently differs from the published benchmark counts.
- The release lacks a paper-exact manifest, full dependency lock, tests, CI, container, release tag, and current endpoint adapters.
- License metadata is internally inconsistent.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish immutable paper and rolling benchmark manifests | Benchmark lineage | Current assets drift from paper/README counts | Reproducible comparisons and explicit evolution | Maintenance overhead | Hash every case/toolkit and reconstruct 36/311 and 38/330 snapshots |
| Add typed state invariants and deterministic reference simulators | Emulation validity | Prompt-only emulators miss core constraints | Better error attribution and lower false discovery | More implementation effort | Compare LM-only, deterministic, and hybrid emulation on blinded cases |
| Freeze environment and endpoint metadata | Reproducibility | Historical APIs and unpinned packages cannot be replayed reliably | Cleaner independent reconstruction | Container and compatibility work | Tagged clean-room install plus signed smoke-test report |
| Expand independent human adjudication | Evaluation validity | Four annotators and moderate agreement limit label authority | Better calibration and subgroup analysis | Annotation cost | Multi-institution blinded panel with pre-registered rubric |
| Add safe transfer tiers | Sim-to-real evidence | One terminal toolkit cannot support broad transfer | Domain-specific validity estimates | Requires specialist sandbox design | Inert, reversible reference tools before any authorized real integration |
| Resolve licensing and packaging metadata | Governance | Apache text and MIT classifier conflict | Clear redistribution and integration rights | Maintainer review | Release checklist and package-metadata audit |

## Potential Implementations

### Hybrid tool-safety simulator

- `User`: Agent platform safety teams.
- `Goal`: Discover unsafe decisions under ambiguous benign requests without touching real systems.
- `Core mechanism`: An LM proposes difficult virtual states; typed tool schemas and deterministic invariants validate identifiers, permissions, state transitions, and outcomes.
- `Required inputs`: Synthetic cases, inert tool definitions, policy invariants, versioned emulator prompts, and independent judge labels.
- `Outputs`: Trajectory, state-diff ledger, invariant violations, judge packet, and transfer-readiness score.
- `Risk controls`: No live credentials, external communication, production data, unrestricted shell, or physical actuation.
- `Evaluation`: Failure precision/recall, critical-emulation-error rate, human agreement, deterministic replay, and no-side-effect verification.

### Benchmark lineage validator

- `User`: Research authors, reviewers, and repository maintainers.
- `Goal`: Detect silent drift between a paper, README, code, and benchmark assets.
- `Core mechanism`: Count and hash cases, toolkits, tools, prompts, model adapters, and dependencies, then compare them with a signed publication manifest.
- `Required inputs`: Paper metadata, repository commit, asset files, environment lock, and expected count/schema declarations.
- `Outputs`: Version graph, count mismatch report, missing-pin report, and reproducibility grade.
- `Risk controls`: Read-only analysis, secret filtering, license checks, and no benchmark execution.
- `Evaluation`: Known-drift detection, manifest reconstruction accuracy, and independent reviewer agreement.

### Judge calibration workbench

- `User`: Benchmark and evaluation teams.
- `Goal`: Measure when automatic safety/helpfulness judges disagree with humans or each other.
- `Core mechanism`: Present blinded, benign synthetic trajectories to multiple judges and a human panel, with structured reasons and adjudication.
- `Required inputs`: Redacted trajectories, scoring rubric, model/version pins, and human labels.
- `Outputs`: Confusion matrices, agreement metrics, calibration curves, disagreement clusters, and override log.
- `Risk controls`: Content screening, access controls, minimum necessary context, and no operational harmful payloads.
- `Evaluation`: Precision, recall, Cohen's kappa, calibration error, and stability across versions.

## Three Ways to Exercise This Research

1. `Learning path`: Create twelve benign underspecified requests for inert calendar, notes, and file-listing tools. Label the missing facts, safe clarifications, expected state transitions, and stop conditions; succeed when a second reviewer reproduces every label and stop if any case requires a real account or external action.
2. `Build path`: Implement one deterministic in-memory tool plus an LM state proposer, record every virtual transition, and compare standard versus adversarial state generation; succeed when injected invariants are always enforced and stop on any nondeterministic state mutation.
3. `Research path`: Pre-register a small comparison of LM-only, deterministic, and hybrid emulators with two automatic judges and blinded human review; succeed when all cases, prompts, pins, and table cells are reconstructable and stop if model or asset drift prevents attribution.

## Example MVP Product

- `Product name`: SandboxLedger.
- `Target user`: Teams evaluating tool-using agents before integration testing.
- `Problem`: Pure language-model emulation scales but can violate state constraints, while real sandboxes are costly and risky.
- `Core workflow`: A reviewer selects benign synthetic cases and inert tools; an LM proposes ordinary and adversarial states; deterministic validators enforce the tool contract; the agent acts only on virtual state; two judges and a human sample score safety/helpfulness; a signed ledger binds every result to versions and state transitions.
- `Data requirements`: Synthetic case manifests, typed tool schemas, deterministic fixtures, model/prompt pins, redacted trajectories, and human labels.
- `Architecture`: Local orchestrator, no-egress model gateway, virtual state store, invariant engine, trajectory ledger, dual-judge service, human-review queue, and manifest signer.
- `Success metrics`: Zero external side effects; 100% deterministic state replay; at least 90% injected-invariant detection; reported judge-human agreement; complete provenance for every result.
- `Risk controls`: No production data, live credentials, external tool calls, unrestricted code execution, or physical actuation; explicit authorization and fail-closed validation.
- `Limitations`: Synthetic fixtures may understate real ambiguity; judge/model drift persists; deterministic tools require domain engineering.
- `MVP boundary`: Three inert toolkits and benign underspecification cases only; no malicious-user generation, production connectors, or autonomous remediation.
- `Deployment model`: Local-only container or isolated CI runner.
- `Evaluation plan`: Schema tests, seeded invariant violations, replay tests, blinded annotation, drift checks, and a no-egress audit.
- `Failure modes`: State proposer ignores constraints, validator schema is incomplete, judges share correlated bias, or benchmark assets change without a manifest.
- `Maintenance plan`: Signed benchmark releases, dependency locks, quarterly judge calibration, and explicit migration notes for every case or toolkit change.

## Related Research and Reading

**New in this pass:** ToolEmu was selected by a PowerShell `Get-Random` draw from five unreviewed primary or near-primary threads preserved by the latest ANCHOR artifact. The complete v2 paper, ICLR record, current official release at `ac4a7ab`, benchmark JSON, and release metadata were newly inspected. This pass adds the 38-toolkit/330-tool release drift and Apache-versus-MIT metadata conflict to the prior safety-evaluation lineage.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| ToolEmu | Primary paper | Core LM-emulated sandbox, adversarial state generation, evaluator validation, benchmark, and limitations; completely reviewed in this pass | https://arxiv.org/abs/2309.15817v2 |
| ToolEmu ICLR record | Primary venue record | Confirms publication at ICLR 2024 as a Spotlight | https://openreview.net/forum?id=GEcwtMk1uA |
| ToolEmu public release | Official implementation and benchmark | Pinned code, prompts, assets, dependency surface, and newly identified release drift | https://github.com/ryoungj/ToolEmu/tree/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb |
| ANCHOR | Primary paper | Prior expanded thread; contrasts persistent multi-turn pressure with ToolEmu's underspecified benign-user cases | https://arxiv.org/abs/2607.10455v1 |
| AgentHarm | Primary benchmark paper | Follow-up baseline for multi-step harmfulness evaluation and tool-sequence assumptions | https://arxiv.org/abs/2410.09024 |
| OS-Harm | Primary benchmark paper | Follow-up computer-use safety benchmark for testing horizon, interface, and transfer differences | https://arxiv.org/abs/2506.14866 |
| StrongREJECT | Primary evaluation paper | Follow-up source for refusal/evaluator methodology and judge calibration | https://arxiv.org/abs/2402.10260 |
| Petri | Official research release | Follow-up automated-auditing system for comparing harness, auditor, and evaluator effects | https://alignment.anthropic.com/2025/petri/ |

Items after the first three remain contextual follow-up reading unless explicitly described as previously reviewed; they were not substantively re-reviewed in this pass.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [Selected source DEP at `68af135`](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/68af13582e1506c4a20cc8b051c703ba2e7120d0/.lake-data/DEP-20260714-Tech%20Intel%201305) | Original ten-item bundle, attribution, two Report-Marks, and iterative lineage | 2026-07-25 | Every repository file inspected |
| R1 | [Latest prior source report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/68af13582e1506c4a20cc8b051c703ba2e7120d0/.reports/BL-DEP-20260714-Tech%20Intel%201305-20260723/README.md) | Prior selection, source notes, and ANCHOR expansion boundary | 2026-07-25 | Inspected in full |
| R2 | [Latest prior Report-Mark](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/68af13582e1506c4a20cc8b051c703ba2e7120d0/.lake-data/DEP-20260714-Tech%20Intel%201305/BL-DEP-Mark002%20Report-Mark.md) | Exact prior related-reading and source-reference sections | 2026-07-25 | Inspected in full |
| R3 | [Latest prior Black-Lake log](https://github.com/Delphoa/Black-Lake/blob/9b475c0fb9d68d8a14131530d6bb4fca77004ae1/.logs/20260723-DEP-20260714-Tech%20Intel%201305-LOG.md) | Prior questions, challenges, validation, and thread-selection record | 2026-07-25 | Inspected in full |
| R4 | [ANCHOR Audit manuscript](https://github.com/Delphoa/Black-Lake/blob/9b475c0fb9d68d8a14131530d6bb4fca77004ae1/.lake-data/DEP-E/DEP-E-20260723-ANCHOR%20Audit/anchor-audit.md) | Latest full same-family manuscript and five-thread expansion pool | 2026-07-25 | Complete manuscript and references inspected |
| R5 | Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, and Tatsunori Hashimoto. [*Identifying the Risks of LM Agents with an LM-Emulated Sandbox*](https://arxiv.org/abs/2309.15817v2). arXiv:2309.15817v2. | Canonical metadata, abstract, version history, and DOI locator | 2026-07-25 | Primary source |
| R6 | [ToolEmu v2 complete PDF](https://arxiv.org/pdf/2309.15817v2) | Full method, figures, tables, limitations, appendices, prompts, and human-annotation procedure | 2026-07-25 | All 70 pages text-inspected; selected pages rendered and visually checked; no copy deposited |
| R7 | [ToolEmu ICLR 2024 OpenReview record](https://openreview.net/forum?id=GEcwtMk1uA) | Venue and Spotlight status | 2026-07-25 | Primary venue locator; interactive forum was access-limited |
| R8 | [Official ToolEmu repository at `ac4a7ab`](https://github.com/ryoungj/ToolEmu/tree/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb) | Release tree, code architecture, prompts, notebooks, and version boundary | 2026-07-25 | Complete path inventory and selected files inspected; code not run |
| R9 | [Pinned benchmark cases](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/assets/all_cases.json) and [toolkits](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/assets/all_toolkits.json) | 144 cases, 38 represented toolkits, 330 tool definitions, and release drift | 2026-07-25 | Static structure/count review; payloads not redistributed |
| R10 | [Pinned README](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/README.md) | Claimed 36/311/144 release surface, setup, historical models, and approximate run cost | 2026-07-25 | Official release documentation |
| R11 | [Pinned requirements](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/requirements.txt) and [setup metadata](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/setup.py) | Dependency pinning, package version, external dependency boundary, and MIT classifier | 2026-07-25 | Static review only |
| R12 | [Pinned license](https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/LICENSE) | Apache License 2.0 text and metadata conflict | 2026-07-25 | Official repository file |

No externally sourced file is deposited. Temporary review files were used only for evidence inspection and are excluded from the public artifact.

## Appendix

### A. Selection audit

- Automation family: Black-Lake Data Processing & Review; Black-Lake Data Processing & Review 0900.
- Fixed run timestamp: 2026-07-25T00:05:03Z.
- Eligibility cutoff: 2026-07-24T00:05:03Z.
- Canonical candidates: 81; excluded: 0; eligible: 81.
- Structured same-family marker Markdown files checked: 67.
- Eligible-list SHA-256: `cc6f2462a76fd69664651c4db7d63089ef7e5772fd3248c281361384ad137dce`.
- Successful DEP draw: index 49, `DEP-20260714-Tech Intel 1305`.
- Diagnostic correction: an earlier invalid probe used the temporary worktree directory date as a fallback for one undated marker, falsely excluded one old DEP, and produced a discarded draw. Repository-relative timestamp parsing established the corrected set before the valid draw.
- Iterative pool: five unreviewed primary or near-primary threads preserved by the latest ANCHOR artifact; SHA-256 `5d77ac316f0c9da5b5b1d2bd892179b04143b8ffac3d586d88642fa4bea7896a`.
- Successful thread draw: index 2, ToolEmu.

### B. Paper and release evidence matrix

| Evidence surface | Published/declared state | Inspected pinned release state | Review implication |
|---|---|---|---|
| Toolkits and tools | 36 toolkits, 311 tools | 38 toolkits, 330 tools | Benchmark evolved without a matching README or release manifest |
| Cases | 144 | 144 | Case count is stable, but the toolkit universe is not paper-exact |
| License | Not a main empirical claim | Apache-2.0 text; MIT classifier in `setup.py` | Redistribution metadata needs correction |
| Environment | Historical model IDs and partial dependency pins | No lockfile, tag, container, tests, or CI | Exact reconstruction is not turnkey |
| Real transfer | Six of seven terminal failures reproduced | No bundled paper-exact replay package | Transfer evidence is narrow and cannot be generalized across toolkits |

### C. Release-integrity checklist

- Paper version pinned: yes, arXiv v2.
- Venue record identified: yes, ICLR 2024 Spotlight.
- Repository commit pinned: yes, `ac4a7ab`.
- Paper-exact benchmark manifest: not visible.
- Release tag: not visible.
- Complete dependency lock or container digest: not visible.
- Automated tests or CI workflow: not visible.
- Benchmark asset counts aligned with paper and README: no.
- License metadata internally aligned: no.
- Historical models/endpoints independently recreated: no.
- Code, benchmark, or statistics independently rerun: no.
