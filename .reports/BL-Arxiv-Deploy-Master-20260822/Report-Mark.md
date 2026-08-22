# Report-Mark: Deploy-Master

## Source Metadata

| Field | Value |
|---|---|
| Title | *Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scientific Tools in One Day* |
| Authors | Yi Wang; Zhenting Huang; Zhaohan Ding; Ruoxue Liao; Yuan Huang; Xinzijian Liu; Jiajun Xie; Siheng Chen; Linfeng Zhang |
| arXiv | [2601.03513v1](https://arxiv.org/abs/2601.03513), submitted 2026-01-07 |
| arXiv DOI | [10.48550/arXiv.2601.03513](https://doi.org/10.48550/arXiv.2601.03513) |
| Subjects | Software Engineering (cs.SE); Artificial Intelligence (cs.AI) |
| Source formats inspected | Complete local PDF/full-paper HTML/metadata, public arXiv abstract and HTML, official Bohrium product page, and three related Black-Lake DEP-E manuscripts |
| Source status | Complete local source pair verified; all original source files withheld from public output |
| Review boundary | Date-only 2026-08-22 metadata; no exact local execution time or local path is disclosed |

## Concise Research Notes

Deploy-Master treats scientific software deployment as an execution-grounded capability-conversion problem. Its workflow begins with a taxonomy-guided search over more than 500,000 public repositories, reduces the pool to 240,645 tool-like repositories and then 52,550 executable-tool candidates, infers build specifications from repository and web evidence, uses a dual-model review loop to refine those specifications, builds containerized environments, runs a minimal executable validation command, and publishes successful tools with structured metadata.

The paper reports 52,550 build attempts, 50,112 successful validated environments, and 2,438 failures, for a reported 95.36% success rate. It also reports a median build time under ten minutes with a long tail, more than 170 programming languages, and build-process errors as the dominant failure category. These figures are author-reported deployment-trace results, not independently reproduced measurements.

The central practical insight is that documentation is a hypothesis, while execution is the stronger usability test. The system makes a useful distinction between “a repository exists” and “a tool runs,” but a successful smoke test is not semantic validation. The paper itself marks the next boundary: hardware-aware scheduling, distributed workflows, semantic input-output contracts, and laboratory or physical integration require additional governance and evaluation layers.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Complete local arXiv:2601.03513v1 PDF and full-paper HTML | Problem framing, system stages, funnel counts, build workflow, aggregate results, failure signals, figures/captions, and limitations | High for source reporting | Author-reported trace; no independent rerun or per-tool ledger inspected |
| E2 | [arXiv metadata](https://arxiv.org/abs/2601.03513) and [full HTML](https://arxiv.org/html/2601.03513) | Version, title, authors, date, subjects, license, full-paper structure, and primary claims | High | Preprint evidence; no later peer-reviewed version verified |
| E3 | [Deploy-Master on Bohrium](https://www.bohrium.com/en/apps/deploy-master) | Public product locator and operational context for turning GitHub repositories into runnable Docker tools | Medium | Product page was inspected as context, not as independent benchmark evidence |
| E4 | [Local AI Stack](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md) | Runtime, serving, accelerator, compatibility, and local-execution infrastructure context | Medium | Related generated artifact; no joint Deploy-Master experiment |
| E5 | [Agent Reliability Gates](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md) | Calibration, rejection, provenance, intervention, and evidence-gate requirements | Medium | Cross-domain synthesis; not a direct implementation of Deploy-Master |
| E6 | [ToolEmu Audit](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-ToolEmu%20Audit/toolemu-audit.md) | Tool-use evaluation, sandboxing, benchmark lineage, and sim-to-real limitations | Medium | Related safety artifact; no shared benchmark |

## Related DEP Entries

1. **Local AI Stack** — `.lake-data/DEP-E/Series 001/DEP-E-20260709-Local AI Stack/local-ai-research.md`. Its source basis covers local runtimes, serving frameworks, accelerator support, compatibility layers, edge constraints, and tool/state security; this is the infrastructure substrate that Deploy-Master would need to expose and manage.
2. **Agent Reliability Gates** — `.lake-data/DEP-E/Series 001/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md`. Its source basis emphasizes transition-level acceptance rules, calibration, rejection, append-only evidence, and early intervention; these are the governance controls missing between a successful smoke test and safe reuse.
3. **ToolEmu Audit** — `.lake-data/DEP-E/Series 001/DEP-E-20260725-ToolEmu Audit/toolemu-audit.md`. Its source basis separates agent, virtual environment, safety evaluator, and helpfulness evaluator while documenting sim-to-real limits; this supplies a concrete evaluation analogy for testing registered tools without external side effects.

## Synthesis Note

### Concept Bridge

Deploy-Master converts heterogeneous repositories into execution-validated capability units. Local AI Stack supplies the runtime and hardware layer; Agent Reliability Gates supplies acceptance, provenance, calibration, and rejection boundaries; ToolEmu supplies an evaluation layer that keeps risky behavior inside an inert environment. The bridge is therefore a governed capability registry: build evidence proves how a tool was assembled, execution evidence proves that a bounded entrypoint ran, semantic contracts describe what inputs and outputs mean, and safety gates determine when a tool may be composed or only reviewed.

### Potential Implementations

1. **Execution provenance registry**: Record repository revision, inferred build specification, container digest, entrypoint, smoke-test output hash, resource footprint, license signal, and reviewer decision. Use it for read-only search and human-approved invocation.
2. **Semantic tool contract gate**: Add typed input-output schemas, unit conventions, expected invariants, refusal conditions, and representative benign fixtures after the minimal executable test. Reject registration when a tool runs but its contract is missing or ambiguous.
3. **Failure-aware agent tool router**: Rank registered tools using execution history, domain fit, environment requirements, uncertainty, and recent failure signals. Require explicit fallback and human review for high-cost, high-impact, or semantically under-specified calls.

### Deeper Relationship Observations

1. **Runnability is a lower layer of reliability**: Deploy-Master validates that an entrypoint executes; the related reliability work shows that safe reuse also needs calibration, rejection, and evidence completeness.
2. **Execution traces are both outputs and training signals**: Failure categories, resource footprints, and environment deltas can improve build refinement and routing, but only if traces are versioned and separated from unsupported causal explanations.
3. **Scale changes the dominant problem**: At tens of thousands of tools, the bottleneck moves from building one image to governing shared runtime capacity, semantic interoperability, observability, and authorization across composed workflows.

### Conceptual Similarities

1. **Evidence over assertion**: all four artifacts replace documentation-only or headline-only claims with inspectable traces, manifests, gates, or benchmark records.
2. **Intermediate state matters**: build specifications, runtime metadata, tool-emulator state, and reliability decisions are preserved rather than collapsed into one success label.
3. **Bounded composition**: each thread treats composition as conditional on interfaces, policies, resource limits, and explicit validation rather than assuming that a working component is safe in every workflow.

### MVP Implementations

1. **Manifest completeness gate** — reject a registry record when build, execution, or semantic fields are missing.

```python
def registry_gate(record):
    required = {"source_revision", "image_digest", "entrypoint", "smoke_test", "io_schema"}
    missing = sorted(required - record.keys())
    return {"status": "review" if missing else "eligible", "missing": missing}
```

2. **Bounded execution trace** — keep a safe, redacted trace for comparison and routing without storing raw private inputs.

```python
def trace_result(tool_id, version, exit_code, output_hash, resources):
    return {
        "tool_id": tool_id,
        "version": version,
        "exit_code": exit_code,
        "output_hash": output_hash,
        "resources": resources,
        "side_effects": "not_observed_in_fixture",
    }
```

3. **Read-only tool selection** — choose among already registered tools while requiring human review for uncertainty or impact.

```python
def select_tool(candidates, domain, max_cost):
    safe = [c for c in candidates if c["domain"] == domain and c["cost"] <= max_cost]
    safe.sort(key=lambda c: (-c["reliability"], c["tool_id"]))
    return {"decision": "review_only", "candidate": safe[0] if safe else None}
```

### Developer Challenges

1. Define stable, machine-readable semantic I/O contracts that survive language, hardware, and domain differences.
2. Bind build, runtime, smoke-test, resource, license, and authorization evidence into an immutable per-tool provenance record.
3. Design evaluation that distinguishes executable success from scientific correctness, safe behavior, and useful composition.

### Author Challenges

1. Release a reproducible, versioned candidate manifest and per-tool execution ledger so the aggregate deployment trace can be independently audited.
2. Report uncertainty and subgroup results for hardware, language, build-system, domain, and resource classes rather than relying mainly on aggregate success.
3. Demonstrate semantic correctness, distributed execution, and safe tool composition beyond minimal commands and container construction.

## Validation Notes

- Source gate: initial partial state repaired; PDF and full-paper HTML passed the required integrity checks; metadata/provenance/verification records are present; source package unavailable; no partial files remain.
- Evidence gate: the full paper's method, funnel, results, failure analysis, figures/captions, and limitations were inspected and cross-checked against public arXiv and the official Bohrium product locator.
- Dedup gate: the exact arXiv identity, DOI, normalized title, slug, Black-Lake artifacts, automation memory, related Black-Lake-Data entries, and preceding-24-hour markers were checked before acceptance; no owning Arxiv DEP was found.
- Related-entry gate: exactly three concrete conceptual overlaps are listed above with repository-relative paths and public GitHub URLs.
- Public-output gate: derived Markdown, public URLs, repository-relative paths, date-only metadata, and source-withholding statements only; no original source, cache, extracted text, private filesystem detail, or exact execution time is present.

## Attribution Block

- Source URL: https://arxiv.org/abs/2601.03513
  - Applies to: paper identity, authors, date, subjects, abstract, version, and public locator.
- Source URL: https://arxiv.org/html/2601.03513
  - Applies to: method, candidate funnel, build pipeline, reported results, failure analysis, figures/captions, limitations, and references.
- Source URL: https://doi.org/10.48550/arXiv.2601.03513
  - Applies to: arXiv-issued DOI identity.
- Source URL: https://www.bohrium.com/en/apps/deploy-master
  - Applies to: public product context and deployment-service locator.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md
  - Applies to: related runtime and self-hosted infrastructure context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md
  - Applies to: related reliability, calibration, provenance, and rejection context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-ToolEmu%20Audit/toolemu-audit.md
  - Applies to: related tool-evaluation and sandboxing context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: public artifact filing and source-locality rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion repository provenance and source-deposition boundary.
- Source files: withheld locally; none were uploaded, committed, or attached to Slack.
