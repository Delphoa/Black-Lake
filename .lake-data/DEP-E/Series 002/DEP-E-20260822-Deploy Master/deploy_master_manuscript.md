---
title: "Deploy-Master - DEP-E"
generated_at: "2026-08-22"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of Deploy-Master's large-scale execution-validated deployment workflow for scientific software."
source_status: "local files only; public artifact contains URLs and derived analysis"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-22"
temporal_cutoff: "2026-08-22"
primary_url: "https://arxiv.org/abs/2601.03513"
stable_identifier: "arXiv:2601.03513v1; DOI:10.48550/arXiv.2601.03513"
confidence_summary: "High for source identity and reported workflow/results; medium for infrastructure interpretation; low for independent reproducibility because no code, data, or deployment trace was executed."
safety_scope: "research review, bounded synthetic evaluation, and human-supervised tool governance"
distribution_notes: "Derived Markdown only; original PDF, HTML, metadata, source archive, caches, and extracted source text remain private and are not redistributed."
---

# Deploy-Master - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Deploy-Master | Primary research artifact | PDF and full-paper HTML | arXiv:2601.03513v1; submitted 2026-01-07 | https://arxiv.org/abs/2601.03513; https://arxiv.org/html/2601.03513; private local source pair, path withheld | arXiv HTML displays CC BY 4.0; source files are retained locally and not redistributed | 2026-08-22 | Complete local source pair verified and inspected |
| S2 | Deploy-Master metadata | Primary metadata record | arXiv abstract page | arXiv:2601.03513v1; cs.SE and cs.AI | https://arxiv.org/abs/2601.03513 | Public metadata; no local path disclosed | 2026-08-22 | Inspected |
| S3 | Deploy-Master DOI | Stable identity | DataCite/arXiv DOI | 10.48550/arXiv.2601.03513 | https://doi.org/10.48550/arXiv.2601.03513 | DOI identity only; no independent result validation | 2026-08-22 | Inspected |
| S4 | Deploy-Master on Bohrium | Official product context | Product page | Public deployment locator | https://www.bohrium.com/en/apps/deploy-master | Product page is context evidence, not a benchmark artifact | 2026-08-22 | Inspected |
| S5 | Local AI Stack | Related DEP-E manuscript | Repository Markdown | Series 001, 2026-07-09 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md | Generated related research; no source files copied | 2026-08-22 | Inspected |
| S6 | Agent Reliability Gates | Related DEP-E manuscript | Repository Markdown | Series 001, 2026-07-28 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md | Generated related research; no source files copied | 2026-08-22 | Inspected |
| S7 | ToolEmu Audit | Related DEP-E manuscript | Repository Markdown | Series 001, 2026-07-25 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-ToolEmu%20Audit/toolemu-audit.md | Generated related research; no source files copied | 2026-08-22 | Inspected |

The primary source pair was complete only after a bounded local repair. The PDF passed the minimum-size, header, and trailing-EOF checks. The full-paper HTML passed the minimum-size, visible-body, document-marker, heading, and paper-structure checks. The optional source package was unavailable; no source file is included in this public artifact.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary paper | Full introduction, system overview, funnel, build stages, results, failure analysis, figures/captions, outlook, and limitations | C1-C6 | High for source claims | No independent deployment or trace audit |
| E2 | S2-S3 | Primary metadata and DOI | Title, authors, date, subjects, version, license, and stable identity | Source identity | High | Metadata does not validate experiments |
| E3 | S4 | Official product context | Public description of turning a GitHub repository into a runnable Docker tool | Product availability and context | Medium | Product page is not a reproducibility package |
| E4 | S5 | Related DEP-E | Runtime, serving, accelerator, compatibility, edge, memory, and tool/state constraints | Implementation context | Medium | Related synthesis, not a joint experiment |
| E5 | S6 | Related DEP-E | Calibration, rejection, provenance, intervention, and evidence-gate patterns | Governance requirements | Medium | Cross-domain transfer |
| E6 | S7 | Related DEP-E | Tool-use sandboxing, evaluator separation, benchmark lineage, and sim-to-real limits | Safe evaluation context | Medium | Methodological neighbor, not Deploy-Master evidence |

## Executive Summary

Deploy-Master presents a one-stop agentic workflow for converting heterogeneous scientific software repositories into runnable, containerized capabilities. The authors describe a 91-domain taxonomy, a recall-oriented pool of more than 500,000 repositories, reduction to 240,645 tool-like repositories and 52,550 executable candidates, dual-model build-specification review, container construction, minimal executable validation, and registration in SciencePedia [E1-E3].

The paper reports 52,550 build attempts, 50,112 successful validated environments, 2,438 failures, and a 95.36% success rate. It also reports a median build time under ten minutes with a long tail and a corpus spanning more than 170 programming languages [E1]. These are author-reported deployment-trace results; the inspected source set did not include a public per-tool manifest, execution ledger, code repository, or independent reproduction.

The strongest reviewer conclusion is narrower than “scientific tools are solved”: execution-centered deployment is a valuable lower layer for AI-for-Science and agentic workflows because it turns documentation claims into observable runtime evidence. The next layer must add semantic I/O contracts, scientific correctness checks, hardware-aware scheduling, authorization, provenance, and failure-aware composition. Confidence is high for the paper's identity and described mechanism, medium for its infrastructure implications, and low for independent reproducibility.

## Detailed Summary

### Problem

Scientific software is abundant but often difficult to compile, configure, reproduce, and invoke. The paper frames this as a “small-workshop mode” in which each researcher or group hand-builds environment assumptions. As tool ecosystems grow, the migration cost of installation, dependencies, interfaces, and environment debugging becomes a bottleneck for reuse, evaluation, and agentic planning [E1].

### Method and Architecture

Deploy-Master has two major agentic stages. The Search Agent uses a 91-domain taxonomy, language-model keyword expansion, repository/web retrieval, iterative expansion through dependency and documentation signals, metadata enrichment, heuristic filtering, and semantic filtering. The Build Agent clones a candidate, traverses README/install/build/CI artifacts, supplements missing information through web search, proposes a build specification, uses a second model to critique and refine it, constructs a container, runs a minimal executable command, and publishes successful results with structured metadata [E1].

The dual-model loop is important because the paper reports early single-model Dockerfile generation at only 50-60% success under documentation mismatch. The authors present build specifications as hypotheses that require execution-based testing rather than as authoritative instructions [E1].

### Evidence and Results

The candidate funnel is reported as more than 500,000 repositories, 240,645 tool-like repositories after heuristic filtering and deduplication, and 52,550 final executable-tool candidates. The deployment trace contains 52,550 build attempts, 50,112 validated tools, and 2,438 failures, yielding 95.36% reported success. The paper says the successful corpus covers more than 170 programming languages, with Python dominant and C/C++, Fortran, and R showing more environmental coupling. The median build time is under ten minutes, but a long tail creates backpressure and resource-management costs [E1].

The dominant failure category is build-process error, defined through observable compiler errors or non-zero exit states. The paper treats failures as debugging signals for specification inference, scheduling, and remediation rather than as fixed properties of a tool. The presence or absence of explicit build artifacts such as `setup.py`, `pyproject.toml`, `requirements.txt`, `Makefile`, and `CMakeLists.txt` is used as a proxy for specification availability, not as proof of causation [E1].

### Boundary and Outlook

The paper positions Deploy-Master as a capability-conversion layer for broader Bohrium/SciMaster-style agentic science ecosystems. It explicitly states that runnable containers are not a complete scientific environment. Hardware heterogeneity, distributed multi-node workflows, semantic I/O and interoperability, and laboratory or physical integration require additional systems, safety, and governance work [E1, E3].

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Large-scale scientific-tool deployment can be organized as a discovery, build-specification, execution-validation, and publication pipeline. | Author claim | E1 | Directly described across the system overview; mechanism is clear. | High |
| C2 | Deploy-Master reduced a large repository pool to 52,550 build candidates and produced 50,112 validated environments from 52,550 attempts. | Author-reported result | E1-E2 | Numerically consistent within the paper and arXiv record; not independently audited. | Medium-high |
| C3 | Execution-centered validation is more reliable than documentation-only build inference for heterogeneous repositories. | Author claim and reviewer interpretation | E1 | Strong conceptual support and reported early-vs-stabilized success contrast; causal attribution remains incomplete. | Medium |
| C4 | Build-process errors and environmental coupling are major operational signals at scale. | Author analysis | E1 | Supported by failure discussion and language/build-artifact analysis; per-tool raw data unavailable. | Medium |
| C5 | Registered executable tools can support more grounded agentic-science planning and evaluation. | Reviewer interpretation | E1, E3-E6 | Plausible infrastructure implication, but no agent benchmark or long-horizon composition experiment was shown. | Medium-low |
| C6 | A passing minimal command does not establish semantic correctness, scientific validity, or safe autonomous composition. | Reviewer interpretation | E1, E5-E6 | Directly follows from the paper's stated limitations and related evaluation evidence. | High |

## Methodology

- `Research objective`: Preserve and critique Deploy-Master as a source-grounded DEP-E research artifact, with emphasis on mechanism, evidence, reproducibility, safe implementation, and relevance to Black-Lake tooling.
- `Sources inspected`: Complete local PDF and full-paper HTML; local metadata/provenance/verification records; public arXiv abstract and HTML; arXiv-issued DOI; official Bohrium product page; and the three related DEP-E manuscripts listed in Source Metadata.
- `Discovery strategy`: Randomized source selection from a metadata-only immutable candidate snapshot generated from `rg --files -g "*.pdf"`; repository/memory/DOI/title/slug and 24-hour marker deduplication; local source-integrity gate; public arXiv and product-page inspection; recursive DEP-E search for conceptual overlaps.
- `Inclusion criteria`: Complete primary paper evidence, stable public identity, implementation-relevant workflow details, reported results and limitations, official product context, and exactly three concrete related DEP-E entries.
- `Exclusion criteria`: Abstract-only candidates, unresolved or duplicate identities, prior or recent owning markers, source PDFs/HTML/source archives in public outputs, unverified code repositories, operational deployment instructions, credentials, private data, and autonomous real-world actuation.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication-oriented review.
- `Evidence handling`: Major claims map to evidence IDs. Author-reported counts remain labeled as source claims. Reviewer conclusions about semantic correctness, governance, and composition are explicitly labeled interpretations or inferences.
- `Uncertainty handling`: Missing per-tool traces, absent verified code repository, aggregate-only metrics, no independent rerun, product-page limitations, and source-package unavailability are preserved rather than smoothed over.
- `Extraction process`: Paper sections, figures/captions, tables where represented in HTML, results, failure discussion, outlook, and references were inspected from the complete local source pair and public arXiv HTML. No code, model, dataset, or deployment was executed.
- `Version control`: Paper pinned to arXiv v1 and its arXiv-issued DOI; related DEP links use their canonical Series paths; public source URLs are recorded without local archive paths.
- `Safety handling`: Implementation examples are local, read-only, synthetic, or human-supervised. No production repository, live connector, credential, unrestricted shell, physical device, or laboratory system is invoked.
- `Reviewer stance`: DEP-ready preservation, skeptical paper review, implementation translation, safe MVP design, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Deploy-Master's discovery funnel, build-specification inference, dual-model review, container construction, minimal executable validation, publication layer, aggregate trace, failure signals, and stated future boundary.
- `Temporal boundary`: Sources available through 2026-08-22; primary paper is arXiv v1 submitted 2026-01-07.
- `Evidence limits`: No public per-tool manifest, execution ledger, code repository, dataset snapshot, container digest, statistical recomputation, benchmark replay, or independent deployment was inspected.
- `Assumptions`: The arXiv v1 full-paper HTML and PDF represent the same paper version; aggregate counts are transcribed as author-reported results; the Bohrium page is the official product locator named by the paper.
- `Constraints`: Public-source copyright and license boundaries; source-document locality; no redistribution of original source files; no live or consequential tool execution; no credentials or private data.
- `Out of scope`: Proving scientific correctness, auditing every deployed tool, reproducing the 50,000-tool trace, evaluating current product access, operating containers, testing MPI/accelerator hardware, or connecting tools to laboratory/physical systems.
- `Intended use`: DEP deposition, architecture review, research backlog, safe MVP planning, and future replication design.
- `Audience`: Platform engineers, AI-for-Science researchers, agent-tooling teams, benchmark maintainers, reviewers, and governance stakeholders.
- `Reproducibility boundary`: The source describes a reproducible-environment goal and aggregate deployment trace, but the inspected public sources do not provide enough artifacts for paper-exact replay.
- `Operational boundary`: Discuss tool deployment conceptually and through inert records only; do not treat the manuscript as permission to run arbitrary repositories or connect agents to consequential systems.
- `Data sensitivity`: Public source material; original paper files remain private archive artifacts.

## Observations

- `Observed pattern`: The paper's key contribution is a shift from declared build instructions to execution-produced evidence.
- `Technical implication`: Build specifications should be versioned hypotheses with provenance, not mutable text blobs that disappear after an image is built.
- `Technical implication`: A registry needs two separate scores: runnability evidence and semantic/goal validity evidence.
- `Contradiction or tension`: The workflow emphasizes agent-readiness, but minimal executable validation can be far weaker than the contracts required for reliable multi-step agent composition.
- `Open question`: Whether execution traces improve agent tool selection depends on trace quality, semantic labels, and resistance to distribution shift across hardware and domains.
- `Reviewer hypothesis`: A typed, evidence-gated registry could turn Deploy-Master's deployment trace into a reusable benchmark for tool selection and failure-aware planning.

## Considerations

- `Adoption`: Containerization reduces setup friction but does not remove accelerator, license, data, or domain-runtime requirements.
- `Operations`: Long-tail builds require queueing, resource budgets, isolation, cancellation, retries, and observability; aggregate success alone is not a service-level objective.
- `Safety`: Repository build and smoke-test automation can execute untrusted code. Sandboxing, network policy, artifact scanning, least privilege, and human review are prerequisites for any real deployment.
- `Evaluation`: Runnability, correctness, reproducibility, semantic contract compliance, and safe behavior should be separate metrics.
- `Governance`: Tool registration should retain source revision, build evidence, image digest, license signals, maintainer status, input/output schema, authorization scope, and correction history.
- `Composition`: Agents should see only tools whose domain, resource, data, and authorization requirements match the current task; uncertain or high-impact tools should abstain or route to review.
- `Maintenance`: Tool images and external repositories drift. Revalidation must be version-bound and should not silently mutate a previously approved capability.

## Strengths

- The paper studies deployment at a scale where long-tail cost, failure categories, language heterogeneity, and resource backpressure become visible.
- The discovery-to-publication pipeline is clearly decomposed into stages with inspectable intermediate artifacts.
- Dual-model specification critique addresses a concrete weakness of documentation-only automation.
- Minimal executable validation is a simple, operationally legible criterion that can be automated across heterogeneous repositories.
- The authors state meaningful limitations instead of presenting runnable containers as complete scientific environments.

## Weaknesses

- Aggregate deployment counts are not accompanied by a public per-tool manifest or execution ledger in the inspected sources.
- The paper does not establish that a passing minimal command validates scientific correctness, stable APIs, meaningful outputs, or safe side effects.
- Search, semantic filtering, build inference, and dual-model review are described at system level; model versions, prompts, thresholds, and decision traces are not fully reproducible from the paper.
- Language-level comparisons can confound language with tool type, dependency topology, hardware, compiler, and repository quality.
- The official product locator provides context but not the code, environment lock, benchmark harness, or independently verifiable deployment trace.
- Hardware heterogeneity, distributed workflows, semantic I/O, and laboratory integration remain future work.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish an immutable candidate and execution manifest | Reproducibility | Aggregate counts cannot be independently audited | Paper-exact trace reconstruction | Storage and privacy review | Hash candidate repositories, decisions, images, tests, and outputs |
| Add typed semantic I/O contracts | Composition | Smoke tests do not specify meaning | Safer tool chaining and better agent planning | Domain schema effort | Contract tests, unit checks, and human-reviewed fixtures |
| Separate runnability, correctness, and safety gates | Evaluation | One success label collapses different claims | More informative routing and abstention | Additional evaluation cost | Multi-axis scorecard with calibration and error analysis |
| Add hardware/distributed execution profiles | Systems | Single-node/container assumptions exclude important tools | Better coverage of MPI, accelerators, and device drivers | Infrastructure complexity | Repeated validation across pinned hardware profiles |
| Version the dual-model review loop | Method transparency | Prompts and model drift can change build decisions | Reproducible inference and regression analysis | Artifact/version maintenance | Replay held-out repositories with frozen prompts and models |

## Potential Implementations

1. **Public scientific-tool registry**: User: researchers and agents. Goal: discover execution-validated tools. Mechanism: index versioned source, image, entrypoint, I/O schema, smoke-test evidence, resource profile, and authorization scope. Inputs: public repositories and inert fixtures. Outputs: searchable records and review links. Risk controls: sandboxed builds, no-egress defaults, license checks, and human approval for consequential tools. Evaluation: reproducibility, semantic-contract coverage, safe-failure rate, and freshness.
2. **Failure-aware build service**: User: platform maintainers. Goal: convert incomplete repository evidence into bounded build hypotheses. Mechanism: staged search, dual review, build, smoke test, and structured failure classification. Inputs: repository snapshot, build artifacts, model configuration, and resource budget. Outputs: candidate specification, image, test trace, and remediation queue. Risk controls: isolation, quotas, timeouts, retry ceilings, artifact scanning, and no secret inheritance. Evaluation: build success, false-success rate, cost tail, and recovery quality.
3. **Agent tool-governance layer**: User: scientific-agent operators. Goal: allow agents to plan over reliable but bounded capabilities. Mechanism: policy-aware selection over registered tools with semantic schemas, reliability history, domain fit, and authorization. Inputs: task description, typed data, tool registry, and operator policy. Outputs: ranked options, abstention, or human-review packet. Risk controls: read-only default, explicit authorization, provenance, resource caps, and side-effect simulation. Evaluation: task success, invalid-call rate, abstention quality, and audit completeness.

## Three Ways to Exercise This Research

1. `Synthetic registry audit`: Objective: test whether a registry distinguishes runnable from semantically valid tools. Inputs: three inert local tools, versioned manifests, fixed fixtures, and intentionally incomplete schemas. Method: apply runnability, schema, invariant, and provenance gates. Output: gate matrix and correction log. Success criterion: no tool with a missing contract reaches `eligible`; stop if any test invokes a real external system.
2. `Build-trace replay`: Objective: measure whether structured failure signals improve bounded retry or human routing. Inputs: synthetic build records with compile, dependency, resource, and network failure labels. Method: compare static rules with a reviewed hypothesis loop under a fixed retry and resource budget. Output: replayable cost, latency, and routing table. Success criterion: fewer blind retries without reducing correctly identified recoverable cases; stop at the preset compute budget.
3. `Agent selection benchmark`: Objective: test whether execution and semantic evidence improve tool choice. Inputs: a public or synthetic task set, typed tool cards, frozen reliability traces, and a read-only selector. Method: compare name-only, documentation-only, and evidence-gated routing. Output: selection accuracy, invalid-call rate, abstention rate, and provenance completeness. Success criterion: evidence-gated routing reduces invalid selections while preserving task coverage; stop before any live connector or physical actuation.

## Example MVP Product

- `Product name`: Runnable Capability Ledger.
- `Target user`: AI-for-Science platform teams and researchers who need auditable tool reuse.
- `Problem`: Repository presence and successful installation do not prove that a tool has stable semantics, reproducible execution, or safe agent-facing boundaries.
- `Core workflow`: Import a pinned public repository snapshot; register build hypotheses and reviewer decisions; run an inert smoke fixture in an isolated runner; capture output hash, resources, and environment; attach typed I/O and authorization metadata; publish a read-only tool card or human-review packet.
- `Data requirements`: Public repository metadata, source revision, build specification, container digest, fixture inputs/outputs, resource measurements, I/O schema, license signals, and reviewer decisions. No private data or credentials.
- `Architecture`: Local-first manifest store, isolated build runner, deterministic fixture runner, schema validator, evidence ledger, policy gate, static registry view, and correction history.
- `Success metrics`: Complete provenance for every record; zero unapproved external side effects; reproducible fixture outputs; lower invalid tool selection; bounded build retry cost; explicit semantic-contract coverage.
- `Risk controls`: Network isolation, least privilege, resource/time caps, secret scrubbing, immutable source revisions, manual approval for side effects, and fail-closed missing-evidence handling.
- `Limitations`: Synthetic fixtures may miss real domain behavior; semantic schemas require expert effort; aggregate reliability can hide subgroup failures; registry freshness is not guaranteed without revalidation.
- `MVP boundary`: Three inert public or synthetic tools, local execution only, one typed schema family, no arbitrary repository execution, no production connectors, and no autonomous remediation.
- `Deployment model`: Local CLI plus static Markdown/JSON report bundle.
- `Evaluation plan`: Golden manifests, schema-missing cases, deterministic replay, resource-limit tests, redaction checks, reviewer agreement, and no-egress audit.
- `Failure modes`: Stale images, false smoke-test success, incomplete schema, incorrect license inference, tool drift, resource exhaustion, and evaluator overconfidence.
- `Maintenance plan`: Revalidate pinned revisions, rotate dependency policy, preserve correction history, rerun fixtures after changes, and review tool authorization scopes.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| Deploy-Master | Primary paper | Discovery, build-specification inference, execution validation, publication, aggregate trace, and limitations | https://arxiv.org/abs/2601.03513 |
| Deploy-Master full HTML | Primary full text | Complete method, funnel, results, failure signals, and outlook | https://arxiv.org/html/2601.03513 |
| Deploy-Master on Bohrium | Official product context | Public tool-deployment service named by the paper | https://www.bohrium.com/en/apps/deploy-master |
| Local AI Stack | Related DEP-E | Runtime, serving, hardware, compatibility, memory, and tool/state infrastructure | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md |
| Agent Reliability Gates | Related DEP-E | Calibration, rejection, provenance, intervention, and reliability boundary design | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md |
| ToolEmu Audit | Related DEP-E | Tool-use sandboxing, evaluator separation, benchmark lineage, and sim-to-real caution | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-ToolEmu%20Audit/toolemu-audit.md |
| Model Context Protocol transports | Standards context cited by the paper | Agent-facing interface context; not independently re-reviewed in this pass | https://modelcontextprotocol.io/specification/2025-06-18/basic/transports |
| Best Practices for Scientific Computing | Near-primary practice reference cited by the paper | Reproducibility and software-practice context | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2601.03513 | Title, authors, version, date, subjects, abstract, license, and canonical identity | 2026-08-22 | Primary metadata record |
| R2 | https://arxiv.org/html/2601.03513 | Introduction, workflow, candidate funnel, build/refinement stages, results, failure analysis, figures/captions, limitations, and references | 2026-08-22 | Complete full-paper HTML inspected locally and by URL |
| R3 | https://doi.org/10.48550/arXiv.2601.03513 | arXiv-issued DOI identity | 2026-08-22 | Stable identifier |
| R4 | https://www.bohrium.com/en/apps/deploy-master | Official product context named by the paper | 2026-08-22 | Context only; no code or deployment executed |
| R5 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md | Related runtime and local-infrastructure evidence | 2026-08-22 | Related generated artifact |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md | Related reliability, provenance, and rejection evidence | 2026-08-22 | Related generated artifact |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-ToolEmu%20Audit/toolemu-audit.md | Related tool-evaluation and sandboxing evidence | 2026-08-22 | Related generated artifact |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public filing layout and source-locality policy | 2026-08-22 | Live repository README inspected |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository provenance and source-deposition policy | 2026-08-22 | Live repository README inspected |

## Appendix

### Selection and source-gate validation

- Selection was reservation-bound to the canonical family `black-lake-arxiv-dep-v1` and the automation run key, with only the returned identity opened.
- Candidate discovery used the required PDF enumeration and parent-directory paper units. Identity derivation used filenames and nearby metadata/readme files; source bodies were not opened during candidate freezing.
- The frozen snapshot recorded 75,967 PDF paths, 75,964 parent units, 67,988 resolved identities, 6,801 collapsed duplicate identity mirrors, 2 unresolved units, 2,000 permanent exclusions, and 18 recent-marker exclusions. The reservation helper reported 61,187 candidate rows, 59,187 eligible rows, zero active reservations, one cooldown exclusion, and a direct cryptographic random selection of arXiv:2601.03513.
- Initial source state was partial because the PDF was present but full-paper HTML was absent. The bounded repair preserved the valid PDF, obtained official full-paper HTML and metadata through the archive broker, refreshed local provenance/summary/verification records, and confirmed no partial files remained.
- Source package status: unavailable. Source files collected: yes, locally only. Public source files uploaded: none. Public DEP `.source/` directory: not created.

### Reproducibility checklist

- [x] Primary identity and version recorded.
- [x] PDF and full-paper HTML source gate passed.
- [x] Method, results, limitations, and public product context inspected.
- [x] Author claims separated from reviewer interpretation.
- [x] Exactly three related DEP entries recorded.
- [x] Exactly three exercise paths provided.
- [x] Public-safe source-withholding boundary preserved.
- [ ] Independent deployment-trace replay: not available from inspected sources.
- [ ] Per-tool manifest and semantic I/O audit: not available from inspected sources.

## Attribution Block

- Source URL: https://arxiv.org/abs/2601.03513
  - Applies to: paper identity, authors, date, subjects, version, and abstract.
- Source URL: https://arxiv.org/html/2601.03513
  - Applies to: full method, results, figures/captions, failure analysis, limitations, and references.
- Source URL: https://doi.org/10.48550/arXiv.2601.03513
  - Applies to: stable DOI identity.
- Source URL: https://www.bohrium.com/en/apps/deploy-master
  - Applies to: official product context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md
  - Applies to: related local runtime and infrastructure synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md
  - Applies to: related reliability and evidence-gate synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-ToolEmu%20Audit/toolemu-audit.md
  - Applies to: related tool-evaluation and sandboxing synthesis.
- Source files: withheld locally; none were uploaded, committed, or attached to Slack.
