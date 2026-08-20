# Report-Mark: LSS Runtime Entropy

## Source Metadata

- Title: *Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems*.
- Authors: Weihao Zhang, Yitong Zhou, Huanyu Qu, and Hongyi Li.
- Identifier: arXiv:2603.15690v1; DOI `10.48550/arXiv.2603.15690`.
- Submitted: 2026-03-16; subject areas: Computer Science—Software Engineering and Artificial Intelligence.
- License shown on the arXiv HTML record: CC BY 4.0.
- Evidence inspected: the official arXiv abstract, full-paper HTML, locally retained PDF-derived text, locally retained HTML-derived text, local archive verification records, and related Black Lake Markdown entries.
- Source package: unavailable; source files remain local and were not redistributed.

## Concise Research Notes

The paper introduces Loosely-Structured Software (LSS) as a software paradigm for systems whose effective behavior is generated and revised at runtime under uncertainty. Its central move is to treat the runtime View, semantic binding topology, and persistent Artifact evolution as engineering surfaces rather than incidental prompt behavior.

The three-layer framework is: View/Context Engineering for Context Entropy; Structure Engineering for Self-Organization Entropy; and Evolution Engineering for Evolutionary Entropy. The paper formalizes four runtime elements—Intent, Global Artifacts, View, and Output—and four primitives—Project, Execute, Update, and Formulate. Proposed patterns include Semantic Lens, Context Curator, Mediator, Semantic Router, Index Generator, Team Generator, Sandbox Mode, Evolver, Semantic Palimpsest, Artifact Maintainer, and End Criteria.

The strongest quantitative evidence is the RepoBench-R retrieval comparison. On the Python `python_cff` test-easy split with a top-5 candidate budget, Worker-only Hit@5 was `0.70`, Lens+Worker was `0.78`, and Lens+Index+Worker was `0.84`; Top-1 Accuracy remained `0.10–0.12`. Worker average input-context tokens fell from `1,543` to `1,395` with Lens+Worker and stayed near `1,422` with Lens+Index+Worker, while total token cost rose because routing work was externalized. The second evaluation describes a file-based research environment with a 10-task-per-round cap, 10 rounds, 23 dynamically generated skills, a single basic experiment-agent round, and subjective AI-reviewer scores.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution |
|---|---|---|
| E1 | Title, authors, date, DOI, subject areas, and CC BY 4.0 license | [arXiv abstract](https://arxiv.org/abs/2603.15690) |
| E2 | LSS definition, runtime elements, Project/Execute/Update/Formulate cycle, and three-layer framework | [arXiv full HTML](https://arxiv.org/html/2603.15690) |
| E3 | Semantic Lens, Context Curator, Mediator, End Criteria, Router, Index, Team, and inheritance patterns | [arXiv full HTML](https://arxiv.org/html/2603.15690) |
| E4 | RepoBench-R setup, Hit@5, Top-1 Accuracy, context-token values, and cost trade-off | [arXiv full HTML](https://arxiv.org/html/2603.15690) |
| E5 | Comprehensive workflow structure, 10 rounds, task cap, 23 generated skills, human-review caveat, and conclusion | [arXiv full HTML](https://arxiv.org/html/2603.15690) |
| E6 | Cache status, extractor fallback, and source-locality result | Local public-summary-derived processing record; source files and cache were withheld |

## Related DEP Entries

Exactly three related entries were selected after reading their repository-relative Markdown content:

1. `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` — concrete overlap in verification, routing, memory, auditability, rejection, and intervention gates around agent inference; source basis is the entry’s evidence ledger and cross-domain gate synthesis.
2. `.lake-data/DEP-E/DEP-E-20260815-Agent Context Systems/agent-context-systems.md` — concrete overlap in context selection, runtime access plans, self-authored verification limits, memory interference, and independent acceptance boundaries; source basis is the entry’s ten-source metadata and evidence ledger.
3. `.lake-data/DEP-E/DEP-E-20260804-Agent Systems/agent-systems.md` — concrete overlap in active shared context, routed observations, structured failure memory, governed longitudinal state, and generation-time verification; source basis is the entry’s source metadata and evidence ledger.

## Synthesis Note

### Concept Bridge

LSS can be read as a control-plane vocabulary for agentic systems whose “program” is partly assembled at inference time. The bridge to Black Lake practice is direct: a public research artifact is an evolving Artifact; source selection and extraction form a View; related DEP pointers form an Index; the Report-Mark is a provenance-bearing Output; and validation plus deduplication are external End Criteria. The useful transfer is therefore not to make agents unconstrained, but to make runtime flexibility observable, scoped, reversible, and evidence-bearing.

### Potential Implementations

1. **Provenance-aware context router** — Route only task-scoped evidence to a worker, record the selected artifact IDs, confidence, reason, and downstream use, and expose an abstention path when no route clears a threshold.
2. **Sandboxed artifact evolver** — Propose changes to skills, indexes, or routing policies in an isolated copy; replay representative synthetic tasks; merge only changes that pass external checks and retain a rollback chain.
3. **Layered research workspace** — Maintain a hot task pool, warm reusable indexes and evidence ledgers, and cold archived reports, with explicit links and retention rules instead of passing the entire workspace into every agent context.

### Deeper Relationship Observations

1. The paper’s Context Entropy and the related Agent Context Systems entry converge on a systems boundary: relevance is not merely retrieval quality; it is the amount and type of state exposed to the next action.
2. The paper’s Binding Provenance and the Agent Reliability Gates entry converge on the idea that routing, verification, and rejection must be first-class records, because a correct final answer cannot explain an opaque or misbound path.
3. The paper’s Evolutionary Entropy and the Agent Systems entry converge on lifecycle governance: durable state should be promoted only after checks, should retain lineage, and should have explicit retirement or rollback semantics.

### Conceptual Similarities

1. All four artifacts treat context or state as an architectural resource rather than passive text.
2. All four artifacts separate capability generation from the controls that constrain, verify, or explain its use.
3. All four artifacts favor structured provenance and bounded evaluation over claims of reliability based only on model capability or terminal outputs.

### MVP Implementations with Code Mock-ups

1. **Bounded View builder**

   ```python
   def build_view(intent, artifacts, max_items=5):
       ranked = sorted(
           artifacts,
           key=lambda item: item.get("relevance", 0.0),
           reverse=True,
       )
       selected = [item for item in ranked if item.get("scope") == intent["scope"]]
       return selected[:max_items]
   ```

2. **Binding-provenance router**

   ```python
   def route_with_provenance(intent, routes):
       candidates = [r for r in routes if intent["kind"] in r["kinds"]]
       if not candidates:
           return {"status": "abstain", "reason": "no compatible route"}
       choice = max(candidates, key=lambda r: r["confidence"])
       return {
           "status": "routed",
           "target": choice["target"],
           "evidence": choice["evidence"],
       }
   ```

3. **Sandboxed evolution gate**

   ```python
   def accept_patch(candidate, checks):
       results = {name: bool(check(candidate)) for name, check in checks.items()}
       accepted = all(results.values())
       return {"accepted": accepted, "checks": results, "rollback": not accepted}
   ```

These snippets are safe, local decision-logic sketches. They do not call external tools, mutate persistent artifacts, or claim production readiness.

### Developer Challenges

1. Define compact, versioned contracts for Views, binding events, artifact patches, and evidence without reintroducing the rigidity that LSS is meant to complement.
2. Build independent evaluators and replay fixtures that measure both task success and the side effects of context expansion, routing cost, and self-modification.
3. Make rollback, permissions, and retention enforceable across filesystem artifacts, tool registries, memories, and generated code rather than relying on agent instructions alone.

### Author Challenges

1. Release enough implementation detail, prompt/schema contracts, candidate pools, and environment configuration to reproduce the RepoBench-R comparison.
2. Replace subjective workflow scores with independent graders, task-level success criteria, and ablations that isolate the Lens, Router, Index, and Evolution components.
3. Test the three-layer framework across models, providers, task domains, and longer horizons while reporting failure cases, cost, drift, and safety outcomes alongside success metrics.

## Validation Notes

- The source-integrity gate was completed before synthesis; the final local unit had a valid PDF and verified full-paper HTML, while the source package was unavailable.
- Cache extraction used the required local-first `missing-only` mode; public-safe cache fields were used only for status and extractor reporting.
- Random selection, cache methodology, dedup/reselection validation, related-entry selection, and source-withheld locality are represented in the public logs and manuscript.
- Public-output allowlist: only the generated `.logs`, `.reports`, `.lake-data` Markdown files, and dedup/status JSON are intended for staging.
- No PDF, HTML source, TeX archive, cache, extracted source text, local path, or source archive appears in the public artifact set.

## Attribution Block

- Source URL: https://arxiv.org/abs/2603.15690
  - Applies to: `Report-Mark.md`, `lss_runtime_entropy_manuscript.md`, and the DEP README.
  - Notes: Official arXiv metadata, title, authors, date, DOI, subjects, and license record.
- Source URL: https://arxiv.org/html/2603.15690
  - Applies to: `Report-Mark.md` and `lss_runtime_entropy_manuscript.md`.
  - Notes: Full-paper method, patterns, evaluation, limitation, and conclusion evidence.
- Source URL: https://doi.org/10.48550/arXiv.2603.15690
  - Applies to: `Report-Mark.md`, `lss_runtime_entropy_manuscript.md`, and the DEP README.
  - Notes: Persistent DOI locator for the arXiv work.
