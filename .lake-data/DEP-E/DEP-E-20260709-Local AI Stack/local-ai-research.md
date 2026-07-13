---
title: "Local AI - DEP-20260625"
generated_at: "2026-07-09T00:08:08Z"
artifact_type: "DEP research artifact"
primary_subject: "Local and self-hosted AI deployment stack evidence from DEP-20260625-Local AI Intel 2343."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-09"
temporal_cutoff: "2026-07-09"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260625-Local%20AI%20Intel%202343"
stable_identifier: "DEP-20260625-Local AI Intel 2343"
confidence_summary: "Medium: DEP files and public release/arXiv pages were inspected, but PDFs, code, datasets, and benchmark artifacts were not collected."
safety_scope: "defensive, privacy-preserving, evaluation-oriented"
distribution_notes: "Repository-relative paths and public URLs only; local execution context withheld."
---

# Local AI - DEP-20260625

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected DEP README | Primary source package manifest | Markdown | DEP-20260625-Local AI Intel 2343 | Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343/README.md | Repository material; exact local run timestamp in source is not repeated here. | 2026-07-09 | Inspected |
| S2 | Daily research findings artifact | Primary source package artifact | Markdown | daily_research_findings_2026-06-25_2343.md | Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343/daily_research_findings_2026-06-25_2343.md | Generated source artifact; treated as evidence about the DEP, not as independent authority for external claims. | 2026-07-09 | Inspected |
| S3 | Black-Lake-Data README | Repository standard | Markdown | origin/main | Black-Lake-Data/README.md | Source repository deposition and attribution rules. | 2026-07-09 | Inspected |
| S4 | Black-Lake README | Repository standard | Markdown | origin/main | Black-Lake/README.md | Output repository DEP-E and log rules. | 2026-07-09 | Inspected |
| S5 | llama.cpp b9789 release | Primary project release | GitHub release | b9789 / b3ce5ce | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 | Public GitHub release page; assets not downloaded. | 2026-07-09 | Inspected |
| S6 | llama.cpp release commit | Primary project commit | GitHub commit | b3ce5cedf4c007b78a45befe839fa3abada03c0b | https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b | Public GitHub commit page. | 2026-07-09 | Inspected |
| S7 | vLLM v0.23.0 release | Primary project release | GitHub release | v0.23.0 / 0fc695f | https://github.com/vllm-project/vllm/releases/tag/v0.23.0 | Public GitHub release page; assets not downloaded. | 2026-07-09 | Inspected |
| S8 | Ollama v0.30.10 release | Primary project release | GitHub release | v0.30.10 / e1f7f9c | https://github.com/ollama/ollama/releases/tag/v0.30.10 | Public GitHub release page; assets not downloaded. | 2026-07-09 | Inspected |
| S9 | Transformers v5.12.1 release | Primary project release | GitHub release | v5.12.1 / ddb849a | https://github.com/huggingface/transformers/releases/tag/v5.12.1 | Public GitHub release page; assets not downloaded. | 2026-07-09 | Inspected |
| S10 | FactoryLLM | Primary research source | arXiv abstract page | arXiv:2606.14119v1 | https://arxiv.org/abs/2606.14119 | arXiv abstract and metadata inspected; PDF not collected. | 2026-07-09 | Inspected |
| S11 | Cloud to Edge SBC benchmark | Primary research source | arXiv abstract page | arXiv:2604.24785v1 | https://arxiv.org/abs/2604.24785 | arXiv abstract and metadata inspected; PDF not collected. | 2026-07-09 | Inspected |
| S12 | OpenRad | Primary research source | arXiv abstract page | arXiv:2603.02062v1 | https://arxiv.org/abs/2603.02062 | arXiv abstract and metadata inspected; PDF not collected. | 2026-07-09 | Inspected |
| S13 | Open-source LLM agents for SAST | Primary research source | arXiv abstract page | arXiv:2606.11672v1 | https://arxiv.org/abs/2606.11672 | arXiv abstract and metadata inspected; PDF not collected. | 2026-07-09 | Inspected |
| S14 | Agent Memory | Primary research source | arXiv abstract page | arXiv:2606.06448v1 | https://arxiv.org/abs/2606.06448 | arXiv abstract and metadata inspected; PDF not collected. | 2026-07-09 | Inspected |
| S15 | Toward Secure LLM Agents | Primary research source | arXiv abstract page | arXiv:2606.10749v1 | https://arxiv.org/abs/2606.10749 | arXiv abstract and metadata inspected; PDF not collected. | 2026-07-09 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S2 | DEP package | Manifest, tags, item summaries, attribution block, and ten ranked findings. | Selected DEP identity, source inventory, and local-AI stack framing. | High | The findings artifact is a generated summary and does not replace primary source inspection. |
| E2 | S3, S4 | Repository standards | Canonical `.lake-data` placement, DEP-E class rules, attribution block requirements, and log conventions. | File placement, README structure, and provenance handling. | High | Repository standards are process evidence, not technical research evidence. |
| E3 | S5, S6 | GitHub release and commit | llama.cpp b9789 release date, broad binary/platform assets, and MoE/MTP quantization commit summary. | Runtime breadth and release-level local inference evidence. | Medium | GitHub page was inspected; release assets and source diff were not downloaded. |
| E4 | S7 | GitHub release | vLLM v0.23.0 release highlights: Model Runner V2 expansion, Rust frontend growth, KV cache offloading, and accelerator work. | Private/self-hosted serving as memory-tiered infrastructure. | Medium | Release notes are primary project claims; no performance benchmarks were reproduced. |
| E5 | S8 | GitHub release | Ollama v0.30.10 notes for Command A/North family MLX support, llama.cpp engine update, and MLX artifact fixes. | Apple Silicon local-hosting evidence. | Medium | Release notes were inspected; binaries were not tested. |
| E6 | S9 | GitHub release | Transformers patch notes for PEFT lower bound and Mistral tokenizer resolution. | Open-model tooling compatibility risk. | Medium | Patch notes were inspected; compatibility behavior was not reproduced. |
| E7 | S10 | arXiv abstract | FactoryLLM claims local/open-source LLM support, dual RAGAS and LLM-as-judge evaluation, 30 maintenance queries, about 600 pages of documentation, and groundedness above 0.88. | Domain-specific local RAG evaluation. | Medium | Abstract-level inspection only; full methods and results were not checked. |
| E8 | S11 | arXiv abstract | Single-board benchmark motivation, four edge platform configurations, and token-throughput, power, size, and privacy/connectivity tradeoffs. | Edge hardware evaluation framing. | Medium | Abstract-level inspection only; device details and measurements were not extracted. |
| E9 | S12 | arXiv abstract | OpenRad metadata: PubMed/arXiv/Scopus search to Dec. 2025, 5,239 records, locally hosted gpt-oss:120b extraction, ten expert reviewers, 1,694 included articles, and modality/subspecialty metadata. | Local LLM curation for medical model discovery. | Medium | Abstract-level inspection only; repository and reviewer workflow were not inspected. |
| E10 | S13 | arXiv abstract | Ollama-hosted open-source model agents compared against Bandit using precision, recall, false positives, and composite score; authors reject replacement under realistic conditions. | Negative evidence for local AI SAST replacement. | Medium | Abstract-level inspection only; benchmark dataset and scores were not extracted. |
| E11 | S14, S15 | arXiv abstracts | Agent memory taxonomy/profiling claims and secure-agent survey of 247 papers around information flow, authority, state, prompt injection, tools, and state corruption. | Memory and security as deployment infrastructure for self-hosted agents. | Medium | Abstract-level inspection only; detailed taxonomies and paper list were not collected. |

## Executive Summary

`DEP-20260625-Local AI Intel 2343` is a source package about local and self-hosted AI as a deployment stack. The selected DEP links model runtimes, serving frameworks, compatibility layers, edge hardware, domain RAG, medical-model curation, SAST evaluation, memory systems, and secure-agent deployment. The strongest supported reviewer interpretation is that local AI cannot be evaluated as a model-only choice: the operational outcome depends on runtime binaries, accelerator support, tokenizer/adapter compatibility, KV-cache and memory behavior, power and physical constraints, data governance, and tool/state security.

The inspected primary project releases support the DEP's runtime/tooling claims at release-note level. llama.cpp b9789 exposes a broad cross-platform local inference release surface; vLLM v0.23.0 emphasizes memory-tiered serving and multi-accelerator hardening; Ollama v0.30.10 expands Apple Silicon MLX support; and Transformers v5.12.1 patches PEFT and Mistral tokenizer compatibility. The inspected arXiv pages add domain evidence: FactoryLLM evaluates local/open-source RAG for smart-factory maintenance, edge-inference benchmarking frames token throughput against power and form factor, OpenRad uses a locally hosted LLM for radiology model curation, the SAST paper reports that Ollama-hosted open-source agents do not yet replace Bandit under realistic scanning, and the memory/security papers show why persistent state and authority boundaries matter for self-hosted agents.

Confidence is medium. The repository DEP files, GitHub release pages, and arXiv metadata/abstracts were inspected directly, but no PDFs, release artifacts, code repositories beyond release pages, datasets, benchmark scripts, or model binaries were collected or reproduced. Numerical claims from arXiv abstracts are preserved as source claims unless independently validated in a later pass.

## Detailed Summary

### Problem Context

Local AI is often described as a privacy or cost alternative to cloud inference. The selected DEP presents a richer view: local AI is a stack with interacting layers. A working local deployment may require model weights, tokenizer behavior, adapter compatibility, runtime kernels, accelerator support, server memory policy, edge-device power constraints, data-local RAG, persistent memory, and security boundaries for tools and state.

### Runtime and Tooling Layer

The project-release evidence shows the stack changing at several layers. llama.cpp b9789 is relevant because its release page lists multiple operating-system and accelerator asset families, including macOS, Linux, Android, Windows, CUDA, ROCm, Vulkan, OpenVINO, SYCL, HIP, and OpenCL Adreno paths. The release also links to a commit described as a quantization fix for MoE models with MTP. This supports the DEP's claim that local inference depends on low-level runtime packaging and quantization correctness, not just on model availability.

vLLM v0.23.0 represents the private-cluster side of self-hosted AI. Its release notes report 408 commits from 200 contributors and highlight Model Runner V2 expansion for Llama and Mistral dense models, Rust frontend growth, and KV-cache offloading features such as object-store secondary tier, connector policy hooks, selective offload, and CPU/GPU swap-path improvements. These details support the interpretation that self-hosted serving has become a memory-management and hardware-placement problem.

Ollama v0.30.10 adds a smaller but practical local-hosting signal: Command A and North family models running on Apple Silicon through MLX, an underlying llama.cpp engine update, and MLX artifact fixes. Transformers v5.12.1 adds tooling compatibility evidence by patching the PEFT lower bound and fixing Mistral tokenizer resolution when `mistral-common` is installed. Together, these sources show why local users can be blocked by adapter/tokenizer/runtime compatibility even when model weights exist.

### Domain and Edge Evidence

FactoryLLM gives the DEP a concrete industrial RAG example. Its arXiv abstract describes a safe, open-source AI playground for evaluating LLM-based RAG over smart-factory documents, using local or open-source LLMs to avoid sharing sensitive industrial data. The reported case study uses three LLMs, 30 maintenance queries, and about 600 pages of cross-machine documentation, with groundedness above 0.88. This is direct source evidence for local AI as operational technology support, although a later pass should inspect the full paper and code before treating the results as verified.

The single-board-computer benchmark paper adds hardware selection structure. Its abstract argues that local LLM inference on edge accelerators is feasible but difficult to optimize without multi-dimensional evaluation. It proposes benchmarking across four IoT-suitable edge platform configurations and explicitly frames tradeoffs among power efficiency, physical device size, token throughput, privacy, and connectivity limits.

OpenRad extends the local-AI theme into medical AI curation. The abstract describes 5,239 indexed records, locally hosted `gpt-oss:120b` extraction, ten expert reviewers, 1,694 included articles, and metadata about pretrained weights, interactive applications, modalities, subspecialties, and intended use. The reviewer interpretation is that local LLMs can support sensitive model-indexing workflows, but medical deployment claims remain out of scope without inspecting the repository, data governance, and review protocol.

### Security, Memory, and Governance Evidence

The SAST paper provides a useful negative result: its abstract says open-source Ollama-hosted agents were tested against Bandit using precision, recall, false positives, and a composite score, and that the authors reject current open-source GenAI agents as replacements for specialized SAST scanning in realistic conditions. This matters because local deployment does not automatically mean reliable or safe automation.

Agent Memory and Toward Secure LLM Agents make memory and authority first-class deployment concerns. Agent Memory's abstract describes a system-oriented taxonomy, phase-aware profiling harness, ten representative systems, and recommendations around scheduling, freshness-latency tradeoffs, query-volume amortization, and fleet management. The secure-agent survey synthesizes 247 papers and emphasizes information flow, delegated authority, persistent state, prompt injection, tool-mediated control-flow hijacking, state corruption, and weakly compositional defenses. For Black-Lake, these sources connect local AI with durable memory, provenance-aware state, and security boundaries.

### Conclusion

The selected DEP is best preserved as a baseline local-AI stack artifact. Future review passes should narrow from the broad bundle to one primary thread, preferably FactoryLLM for local industrial RAG, the single-board benchmark for edge deployment measurement, or the Agent Memory/Secure LLM Agents pair for stateful local-agent governance.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The selected DEP is a broad local-AI stack package, not a single-model report. | Reviewer interpretation | E1 | Strongly supported by the DEP's tags, findings, and attribution block. | High |
| C2 | Current local AI deployment depends on runtime, accelerator, tokenizer, adapter, and serving-memory compatibility. | Reviewer interpretation | E3, E4, E5, E6 | Supported by inspected release notes across llama.cpp, vLLM, Ollama, and Transformers. | Medium |
| C3 | Local/open-source AI has domain-specific evaluation value where data locality matters, such as smart factories and edge operations. | Source claim and reviewer interpretation | E7, E8 | Supported at abstract level; full papers should be inspected before stronger empirical conclusions. | Medium |
| C4 | Locally hosted LLMs can support sensitive model curation workflows, but medical claims require stricter validation. | Source claim and reviewer interpretation | E9 | OpenRad abstract supports local extraction plus expert verification; deployment and clinical value are not validated here. | Medium |
| C5 | Open-source local agents should not replace specialized security scanners without stronger evidence. | Source claim | E10 | Supported by SAST abstract's reported conclusion against replacement under realistic conditions. | Medium |
| C6 | Persistent memory, delegated authority, tool use, and state corruption are core governance concerns for self-hosted agents. | Source claim and reviewer interpretation | E11 | Supported by Agent Memory and secure-agent survey abstracts; details remain to be inspected. | Medium |
| C7 | No prior same-family Black-Lake DEP Class artifact or Report-Mark was found for this exact source DEP, so this pass is an initial baseline. | Repository status claim | E1, Appendix | Supported by marker checks across source `.reports`, source DEP Report-Mark files, output `.logs`, and output `.lake-data`. | High |

## Methodology

- `Research objective`: Randomly select one eligible Black-Lake-Data DEP, review it source-first, generate a schema-complete manuscript research document, deposit it as a Black-Lake DEP-E artifact, and add a source-side Report-Mark preserving the manuscript's related-reading and source-reference sections.
- `Sources inspected`: The selected DEP README, selected DEP generated findings artifact, Black-Lake-Data README, Black-Lake README, GitHub release/commit pages for llama.cpp, vLLM, Ollama, and Transformers, and arXiv abstract/metadata pages for FactoryLLM, the single-board-computer benchmark, OpenRad, Ollama-hosted SAST agents, Agent Memory, and Toward Secure LLM Agents.
- `Discovery strategy`: Repository inspection of canonical `Black-Lake-Data/.lake-data/DEP-*` directories, same-family marker checks across source `.reports`, source Report-Mark files, output `.logs`, and output `.lake-data`, random selection among eligible DEP directories, then direct inspection of URLs listed in the selected DEP attribution block.
- `Inclusion criteria`: Sources were included when they appeared in the selected DEP attribution block or defined repository deposition/reporting requirements.
- `Exclusion criteria`: External PDFs, release binaries, source archives, benchmark datasets, and code repositories beyond inspected GitHub release/commit pages were excluded from this first baseline pass to avoid over-collecting and because no prior Report-Mark narrowed the expansion target.
- `Analytical approach`: Mixed conceptual, implementation, safety/ethics, product research, and replication-oriented review.
- `Evidence handling`: Claims from the selected DEP are treated as source-package claims unless independently checked against inspected release pages or arXiv pages. Reviewer interpretations are labeled separately.
- `Uncertainty handling`: Missing PDFs, uncollected source files, unreproduced benchmarks, untested binaries, and abstract-only paper inspection are stated explicitly and reduce confidence.
- `Extraction process`: Markdown DEP files were inspected locally; public GitHub and arXiv pages were inspected by URL; no assets were downloaded into `.source`.
- `Version control`: Repository READMEs were read after fetching `origin/main`; release tags and arXiv version identifiers are recorded where visible.
- `Reviewer stance`: DEP-ready preservation, baseline synthesis, implementation translation, and future-review planning.

## Scope, Constraints, and Assumptions

- `Scope`: This artifact reviews `DEP-20260625-Local AI Intel 2343` as a local/self-hosted AI deployment-stack evidence bundle.
- `Temporal boundary`: Public source access date is 2026-07-09. The selected DEP itself was created on 2026-06-25. Same-family duplicate avoidance used a UTC cutoff of 2026-07-08T00:08:08Z.
- `Evidence limits`: No PDFs, release artifacts, model binaries, code repositories, benchmark datasets, or appendices were downloaded or deeply inspected. Several claims rely on arXiv abstracts or project release notes.
- `Assumptions`: The selected DEP attribution block is treated as the complete source list for this baseline pass. Repository-relative paths identify source files without exposing local execution context.
- `Constraints`: Public artifacts use repository-relative paths and public URLs only. Local absolute paths, local timezone labels, usernames, machine names, and exact local execution context are withheld. Medical, security, and industrial examples are treated as evaluation and governance topics, not deployment approvals.
- `Out of scope`: Reproducing benchmarks, testing local inference binaries, validating clinical or security tool performance, downloading model weights, and operational deployment guidance for sensitive settings.
- `Intended use`: Black-Lake DEP-E deposition, source provenance preservation, future review seeding, and product/implementation ideation.
- `Audience`: Research reviewers, local-AI systems engineers, security reviewers, and Black-Lake automation maintainers.
- `Reproducibility boundary`: Repository inspection and public URL review are reproducible from the source references; empirical results require full-paper/code/data follow-up.
- `Data sensitivity`: Public repository files and public URLs only; sensitive local execution context is withheld.

## Observations

- `Observed pattern`: Local AI is becoming a stack problem across runtime packaging, server memory policy, edge hardware, model tooling, and state governance.
- `Observed pattern`: The selected DEP pairs positive capability evidence with negative readiness evidence. Local model tooling is expanding, but the SAST study argues against replacing specialized scanners with current open-source agents.
- `Technical implication`: Black-Lake should track runtime, hardware, and memory/control-plane metadata alongside model names; otherwise later reviewers cannot determine whether a local deployment claim is practical.
- `Technical implication`: Source packages that mention local AI in sensitive domains should preserve evidence boundaries around privacy, clinical use, cybersecurity, and industrial safety.
- `Open question`: Which of the listed sources has the strongest available code/data package for a deeper second pass: FactoryLLM, the single-board benchmark, Agent Memory, or the SAST evaluation?
- `Reviewer hypothesis`: The most valuable next semantic-web expansion would connect Agent Memory and secure-agent threat surfaces to local runtime logs, RAG stores, and tool-permission manifests.

## Considerations

Local AI can reduce data exposure to external providers, but it also shifts responsibility to the operator. Hardware selection, patch cadence, model provenance, tokenizer behavior, memory stores, tool privileges, logging, and update management become part of the safety case. The selected DEP's medical, cybersecurity, and industrial sources should be treated as high-consequence evaluation evidence, not immediate deployment approval.

Operationally, the stack creates maintenance pressure. A private vLLM cluster and a Mac-based Ollama workflow have different failure modes; an edge single-board deployment has power and thermal constraints; a local RAG system must preserve document provenance; a stateful agent must prevent memory poisoning and over-privileged tool use. Future artifacts should make these boundaries explicit so downstream systems can compare claims without flattening them into generic local-model enthusiasm.

## Strengths

- The selected DEP has a coherent and useful theme: local AI as an operational stack rather than isolated model releases.
- The source inventory is clean and public: every finding is tied to a GitHub or arXiv URL in the DEP attribution block.
- The mix of sources is balanced across tooling releases, edge hardware, domain RAG, medical curation, security evaluation, memory systems, and agent security.
- The bundle contains useful negative evidence through the SAST paper, which reduces the risk of treating local agents as automatically production-ready.
- The selected DEP is well suited for future graph expansion because the sources naturally connect to tags such as local inference, serving, edge computing, RAG, agent memory, and security.

## Weaknesses

- The selected DEP includes generated summaries but no collected PDFs, release artifacts, source code snapshots, benchmark tables, or datasets.
- Most research-paper evidence in this pass is abstract-level. Detailed methods, baselines, sample construction, numerical tables, and limitations were not validated.
- The release-note evidence is project-primary but not independently tested; binary availability does not prove reliability on every listed hardware path.
- Medical and security claims are sensitive and need deeper validation before operational use.
- The bundle is broad. A single manuscript can preserve the cross-source signal, but it cannot fully validate every paper or release.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Deep-review FactoryLLM paper and code | Industrial RAG | It is the clearest domain-specific local-RAG source. | Stronger evidence on local/private document reasoning. | Requires PDF/code inspection and possible license review. | Extract methods, datasets, queries, metrics, and repository availability. |
| Extract edge benchmark tables | Edge hardware | Hardware claims need device-level metrics. | Better comparison of throughput, power, size, and deployment constraints. | Requires full paper and possibly hardware-specific context. | Build a table of devices, accelerators, metrics, and limits. |
| Pair Agent Memory with secure-agent survey | Stateful local agents | Memory and authority are central to safe self-hosting. | Better governance model for local agents with tools and RAG stores. | Requires full-paper taxonomy extraction. | Map memory phases to attack surfaces and controls. |
| Verify release-note claims against source diffs | Runtime tooling | Release notes can omit details. | Better confidence in runtime and compatibility claims. | More repository inspection time. | Inspect linked PRs/commits and note changed files. |
| Create a source-thread graph | Semantic web | The bundle spans many related concepts. | Easier future random expansion and related-reading selection. | Requires normalized tags and identifiers. | Store source nodes and edges in a follow-on DEP-E artifact. |

## Potential Implementations

1. `Local AI Stack Ledger`
   - `User`: Local-AI infrastructure reviewer.
   - `Goal`: Track whether a local deployment claim is supported by runtime, hardware, memory, and safety evidence.
   - `Core mechanism`: Ingest DEP source lists, release notes, arXiv metadata, and repository-relative artifacts into a structured ledger.
   - `Required inputs`: DEP README, generated findings artifact, release URLs, paper URLs, hardware tags, runtime tags, and security/memory tags.
   - `Outputs`: Stack-readiness scorecard, source graph, missing-evidence checklist, and next-review candidates.
   - `Risk controls`: No secrets, no model weights, no clinical/security deployment claims without validation, and explicit source-access dates.
   - `Evaluation`: Compare ledger completeness against manually reviewed DEP artifacts.

2. `Private RAG Evaluation Harness`
   - `User`: Manufacturing or internal-document AI evaluator.
   - `Goal`: Test local RAG quality without exporting sensitive documents.
   - `Core mechanism`: Use synthetic or authorized documents, local embedding/indexing, local LLMs, and groundedness/answer-quality metrics.
   - `Required inputs`: Authorized document corpus, query set, model/runtime configuration, retrieval logs, and evaluation rubric.
   - `Outputs`: Grounding report, failure examples, privacy notes, and deployment blockers.
   - `Risk controls`: Synthetic default dataset, no external API calls by default, document access controls, and human review before operational use.
   - `Evaluation`: Reproduce a small FactoryLLM-style query set with transparent metrics.

3. `Stateful Agent Control Plane`
   - `User`: Engineer operating local agents with tools and memory.
   - `Goal`: Reduce memory poisoning, over-privileged actions, and unverifiable long-horizon state.
   - `Core mechanism`: Log memory construction/retrieval/generation phases, tool permission boundaries, provenance links, and state-change approvals.
   - `Required inputs`: Agent memory events, tool manifests, retrieval traces, source references, and policy rules.
   - `Outputs`: State audit trail, risk alerts, provenance map, and review-ready Report-Mark sections.
   - `Risk controls`: Least privilege, sensitive-data redaction, no autonomous external actions without approval, and retention limits.
   - `Evaluation`: Simulated benign and adversarial memory updates in an authorized test environment.

## Three Ways to Exercise This Research

1. `Build a source matrix`: Objective: turn the selected DEP's 11 public URLs into a table of runtime layer, evidence type, sensitive domain, and missing validation. Inputs: DEP README, findings artifact, and public URLs. Method: inspect each source page and classify claims as release note, abstract claim, reviewer interpretation, or missing. Output: source matrix. Success criterion: every DEP finding has one traceable evidence row. Safety boundary: no downloading restricted files or making deployment claims.
2. `Run a synthetic local RAG smoke test`: Objective: test the FactoryLLM idea with non-sensitive synthetic machine manuals. Inputs: synthetic documents, local embedding/index, local LLM, and ten maintenance-style questions. Method: retrieve passages, generate answers, and score grounding manually or with a local rubric. Output: grounding and failure report. Success criterion: all answers cite retrieved passages and uncertain answers are flagged. Safety boundary: no real industrial documents without authorization.
3. `Map memory to threat surfaces`: Objective: connect Agent Memory phases to secure-agent risks. Inputs: Agent Memory abstract/full paper in a later pass, secure-agent survey abstract/full paper in a later pass, and a toy agent memory log. Method: label memory construction, retrieval, generation, tool use, and state mutation events with risk controls. Output: state-risk map. Success criterion: every state transition has provenance and a permission boundary. Safety boundary: authorized toy logs only and no offensive attack instructions.

## Example MVP Product

- `Product name`: LocalStack Review Board
- `Target user`: Engineers and reviewers evaluating local or self-hosted AI deployments.
- `Problem`: Local AI decisions are often made from model names alone, while real readiness depends on runtime, hardware, memory, security, and data-governance evidence.
- `Core workflow`: Import a DEP source package, parse public URLs and repository-relative files, classify sources by stack layer, attach evidence IDs, flag missing validation, and generate a review-ready manuscript/Report-Mark bundle.
- `Data requirements`: DEP README files, generated findings artifacts, public release pages, public arXiv pages, optional authorized PDFs/code snapshots, runtime/hardware tags, and reviewer notes.
- `Architecture`: Local Markdown parser, source inventory table, evidence ledger, browser-assisted source inspection, rules-based sanitization gate, static report generator, and optional graph export.
- `Success metrics`: Percentage of claims with evidence IDs, number of unsupported deployment claims caught, source-reference completeness, reviewer time to next-pass decision, and absence of local-context leaks in public artifacts.
- `Risk controls`: Repository-relative paths only, no local execution context in public output, no secrets, no model weights by default, safety labels for medical/security/industrial sources, and human review before deployment guidance.
- `Limitations`: Does not reproduce benchmarks, run models, validate medical performance, or guarantee release compatibility without deeper source/code inspection.
- `MVP boundary`: Markdown/URL review only; no automated downloading of PDFs, binaries, or model weights.
- `Deployment model`: Local CLI or repository automation step.
- `Evaluation plan`: Run on existing DEP packages and compare generated evidence ledgers with manual review.
- `Failure modes`: Over-trusting generated DEP summaries, misclassifying release-note claims as validated results, missing local-context leaks, or under-labeling high-consequence domains.
- `Maintenance plan`: Update source classifiers, sanitization patterns, and schema checks as repository conventions evolve.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| llama.cpp b9789 release | Official runtime release | Local inference runtime packaging and accelerator support. | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 |
| llama.cpp b3ce5ce commit | Official runtime commit | MoE/MTP quantization fix tied to the selected release. | https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b |
| vLLM v0.23.0 release | Official serving release | Self-hosted serving, Model Runner V2, Rust frontend, accelerator work, and KV-cache offload. | https://github.com/vllm-project/vllm/releases/tag/v0.23.0 |
| Ollama v0.30.10 release | Official local runtime release | Apple Silicon MLX support for Command A and North-family models. | https://github.com/ollama/ollama/releases/tag/v0.30.10 |
| Transformers v5.12.1 release | Official model-tooling release | PEFT and Mistral tokenizer compatibility for open-model stacks. | https://github.com/huggingface/transformers/releases/tag/v5.12.1 |
| FactoryLLM | arXiv preprint | Local/open-source RAG evaluation over smart-factory maintenance documentation. | https://arxiv.org/abs/2606.14119 |
| Cloud to Edge SBC benchmark | arXiv preprint | Edge hardware methodology for token throughput, power, size, and connectivity/privacy constraints. | https://arxiv.org/abs/2604.24785 |
| OpenRad | arXiv preprint | Local LLM-assisted radiology AI model curation with expert verification. | https://arxiv.org/abs/2603.02062 |
| Open-source LLM agents for SAST | arXiv preprint | Negative evidence for replacing specialized SAST tools with current Ollama-hosted agents. | https://arxiv.org/abs/2606.11672 |
| Agent Memory | arXiv preprint | Systems characterization of stateful long-horizon agent memory. | https://arxiv.org/abs/2606.06448 |
| Toward Secure LLM Agents | arXiv preprint | Threat surfaces around information flow, authority, tools, memory, and persistent state. | https://arxiv.org/abs/2606.10749 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343/README.md | Selected DEP identity, tags, file inventory, source inventory, and attribution block. | 2026-07-09 | Repository-relative source file; no local path published. |
| R2 | Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343/daily_research_findings_2026-06-25_2343.md | Ten ranked findings and local-AI synthesis. | 2026-07-09 | Repository-relative source file; generated artifact treated as source-package evidence. |
| R3 | Black-Lake-Data/README.md | Source DEP placement, `.reports` use, and attribution expectations. | 2026-07-09 | Repository README inspected after fetch. |
| R4 | Black-Lake/README.md | Output DEP-E placement, README, attribution, and log expectations. | 2026-07-09 | Repository README inspected after fetch. |
| R5 | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 | llama.cpp b9789 release assets and summary. | 2026-07-09 | Release page inspected; assets not downloaded. |
| R6 | https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b | llama.cpp MoE/MTP quantization commit evidence. | 2026-07-09 | Commit page inspected. |
| R7 | https://github.com/vllm-project/vllm/releases/tag/v0.23.0 | vLLM release highlights, serving, KV offload, and hardware support. | 2026-07-09 | Release page inspected; assets not downloaded. |
| R8 | https://github.com/ollama/ollama/releases/tag/v0.30.10 | Ollama MLX and Apple Silicon release evidence. | 2026-07-09 | Release page inspected; assets not downloaded. |
| R9 | https://github.com/huggingface/transformers/releases/tag/v5.12.1 | Transformers PEFT and Mistral tokenizer patch evidence. | 2026-07-09 | Release page inspected; assets not downloaded. |
| R10 | https://arxiv.org/abs/2606.14119 | FactoryLLM metadata, local/open-source RAG claim, case-study scale, and groundedness claim. | 2026-07-09 | Abstract/metadata inspected; PDF not collected. |
| R11 | https://arxiv.org/abs/2604.24785 | Single-board edge inference benchmark motivation and evaluation dimensions. | 2026-07-09 | Abstract/metadata inspected; PDF not collected. |
| R12 | https://arxiv.org/abs/2603.02062 | OpenRad curation workflow, local LLM extraction, expert review, and scale claims. | 2026-07-09 | Abstract/metadata inspected; PDF not collected. |
| R13 | https://arxiv.org/abs/2606.11672 | Ollama-hosted SAST agent evaluation and negative replacement claim. | 2026-07-09 | Abstract/metadata inspected; PDF not collected. |
| R14 | https://arxiv.org/abs/2606.06448 | Agent memory taxonomy, profiling, and systems recommendations. | 2026-07-09 | Abstract/metadata inspected; PDF not collected. |
| R15 | https://arxiv.org/abs/2606.10749 | Secure-agent threat-surface survey and persistent-state security framing. | 2026-07-09 | Abstract/metadata inspected; PDF not collected. |

## Appendix

### Automation Run Notes

- Automation: Black-Lake Data Processing & Review 0900.
- Automation family: Black-Lake Data Processing & Review; Black-Lake Data Processing & Review 0900.
- Run timestamp: 2026-07-09T00:08:08Z.
- Exact local execution timestamp: withheld from public artifact.
- Candidate count: 33 canonical source DEP directories.
- Excluded count: 3 exact same-family recent markers.
- Excluded candidates: DEP-20260624-Tech Intel 2338; DEP-20260626-Tech Intel 1103; DEP-20260704-Tech Intel 0102.
- Eligible count: 30.
- Eligibility cutoff: 2026-07-08T00:08:08Z.
- Selected DEP: Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343.
- Prior material for selected DEP: none found in source `.reports`, selected source DEP Report-Mark files, output `.logs`, or output `.lake-data` entries checked during this run.
- Source files collected: none. Public URLs and repository-relative source files were preserved instead.

### Validation Checklist

- Required manuscript headings are present.
- YAML `title` and H1 are identical and under 40 characters.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- Repository-relative paths and public URLs are used instead of local paths.
- Claims are tied to evidence ledger IDs or source references.
- Missing PDFs, release artifacts, code, datasets, and benchmark reproduction are explicitly stated.
