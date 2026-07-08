---
title: "ConMax - DEP-E"
generated_at: "2026-07-08 (public-safe date; exact local execution timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "ConMax proposes confidence-maximizing compression for chain-of-thought reasoning traces in large reasoning models."
source_status: "URLs only with local archive metadata observed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-08"
temporal_cutoff: "Sources inspected through 2026-07-08."
primary_url: "https://arxiv.org/abs/2601.04973"
stable_identifier: "arXiv:2601.04973"
confidence_summary: "Medium-high for paper metadata and reported method/results from arXiv HTML; lower for reproducibility because code and datasets were not inspected."
safety_scope: "research review, implementation planning, non-sensitive efficiency controls"
distribution_notes: "No source PDF or local archive file is redistributed; local paths are withheld."
---

# ConMax - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | ConMax arXiv abstract page | Primary paper metadata | HTML | arXiv:2601.04973 | https://arxiv.org/abs/2601.04973 | arXiv metadata and abstract page; license not separately reviewed. | 2026-07-08 | Inspected. |
| S2 | ConMax arXiv HTML | Primary paper full text | HTML | arXiv:2601.04973v1 | https://arxiv.org/html/2601.04973 | arXiv HTML rendering used for source-grounded review; no PDF redistributed. | 2026-07-08 | Inspected. |
| S3 | ConMax DOI | Persistent identifier | DOI page | 10.48550/arXiv.2601.04973 | https://doi.org/10.48550/arXiv.2601.04973 | arXiv-issued DOI. | 2026-07-08 | Referenced. |
| S4 | Local arXiv archive metadata | Selection provenance | Local readme/PDF presence | arXiv:2601.04973 | Local path withheld | Local archive metadata confirmed paper URL and PDF presence; not redistributed. | 2026-07-08 | Observed. |
| S5 | Black-Lake README | Repository standard | Markdown | main branch checkout | Black-Lake/README.md | Repository rules for DEP classes, README, logs, reports, attribution, and commit messages. | 2026-07-08 | Inspected. |
| S6 | Arxiv DEP log | Prior artifact | Markdown | 20260708-Arxiv-ConMax-LOG | Black-Lake/.logs/20260708-Arxiv-ConMax-LOG.md | Prior brief log from same selected paper run. | 2026-07-08 | Inspected. |
| S7 | Arxiv DEP Report-Mark | Prior artifact | Markdown | BL-Arxiv-ConMax-20260708 | Black-Lake/.reports/BL-Arxiv-ConMax-20260708/Report-Mark.md | Prior detailed Report-Mark from same selected paper run. | 2026-07-08 | Inspected. |
| S8 | Tech Intel Agent Systems Review | Related DEP artifact | Markdown | DEP-E-20260708-Tech Intel Review | Black-Lake/.lake-data/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md | Related artifact containing semantic early stopping source thread. | 2026-07-08 | Inspected. |
| S9 | HCRC daily finding | Related DEP entry | Markdown | DEP-20260708-Tech Intel 0104 | Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 0104/daily_research_findings_2026-07-08_0104.md | Related entry for verification-gated LLM execution. | 2026-07-08 | Inspected. |
| S10 | UltraQuant/context daily finding | Related DEP entry | Markdown | DEP-20260629-Tech Intel 0104 | Black-Lake-Data/.lake-data/DEP-20260629-Tech Intel 0104/daily_research_findings_2026-06-29_0104.md | Related entry for KV-cache compression and structured context eviction. | 2026-07-08 | Inspected. |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary arXiv metadata | Title, authors, submission date, DOI, subjects, abstract-level contribution. | Source identity and high-level research problem. | High | Abstract is not enough for full empirical validation. |
| E2 | S2 | Primary arXiv HTML full text | Introduction, methodology, experiment setup, main results, ablations, limitations, conclusion. | Method and reported quantitative results. | High | HTML extraction may omit visual nuance from figures; no PDF table image inspection was performed. |
| E3 | S4 | Local archive metadata | Randomly selected archive unit had a readme and PDF for arXiv:2601.04973. | Selection provenance. | Medium | Local paths are withheld; PDF text extraction tooling was unavailable. |
| E4 | S6-S7 | Prior Black Lake artifacts | Earlier log and Report-Mark for the same selected ConMax run. | Backfill rationale and continuity with the two existing artifacts. | High | These are generated artifacts, not independent paper evidence. |
| E5 | S8 | Related Black-Lake DEP artifact | Semantic early stopping source thread and agent-loop token control synthesis. | Related-entry bridge. | Medium | Source was not re-reviewed from its full PDF in this pass. |
| E6 | S9 | Related Black-Lake-Data DEP entry | HCRC summary describing predicate-gated LLM execution with independent verification. | Related-entry bridge. | Medium | Daily finding preserved source claims; full HCRC paper was not inspected in this pass. |
| E7 | S10 | Related Black-Lake-Data DEP entry | UltraQuant and structured context eviction summaries for long-context serving and memory control. | Related-entry bridge. | Medium | Daily finding preserved source claims; full related papers were not inspected in this pass. |
| E8 | S5 | Repository standard | DEP-E class, required DEP README, attribution block, logs/reports roles. | DEP format and placement. | High | Repository policy, not research evidence. |

## Executive Summary

ConMax is a reinforcement-learning framework for compressing chain-of-thought reasoning traces while preserving answer fidelity and reasoning coherence. The authors frame the problem as overthinking in large reasoning models: long traces enable self-verification and backtracking, but they also inflate inference cost and can include redundant exploration. ConMax trains a compression policy with a dual confidence reward from a frozen auxiliary reasoning model, combining answer confidence and thinking confidence rather than optimizing for length alone.

The strongest reported result from the inspected arXiv HTML is the Qwen2.5-7B setting, where ConMax reduces average generated token length from 8,603 to 4,906 while average accuracy shifts from 54.2 to 53.5 across the reported benchmark mix. The paper describes this as a 43% inference-length reduction with a 0.7 point average accuracy drop. Reviewer confidence is medium-high for the description of the method and reported metrics because arXiv HTML sections and tables were inspected; confidence is lower for reproducibility because code, datasets, source package, and PDF figure/table rendering were not independently audited.

For Black-Lake, ConMax matters as part of a broader agent-control stack. It complements semantic early stopping, HCRC-style verification gates, and cache/context compression: stop reasoning loops when semantic progress stalls, compress traces when confidence survives, advance state when predicates pass, and store/serve retained context according to infrastructure constraints.

## Detailed Summary

### Problem

Large reasoning models often use long chain-of-thought traces to solve difficult math and science problems. The paper argues that these traces can contain useful cognitive behaviors, including decomposition, verification, backtracking, and correction. The same traces can also become wasteful: redundant checks and over-exploration increase token use, latency, and training or serving cost without always improving final answer quality.

Existing compression approaches have two failure modes in the paper's framing. Heuristic pruning and truncation may damage logical coherence or remove useful substructure, while search-based compression can become expensive because it repeatedly invokes models to refine or select reasoning steps. ConMax targets a middle path: learn a compression policy that preserves reasoning validity and predictive fidelity without needing human-labeled optimal compressed traces.

### Method

ConMax formulates compression as reward-driven optimization. A compression policy receives a query and a verbose reasoning trace, then generates a concise trace. A frozen auxiliary large reasoning model supplies two reward signals.

Answer confidence measures whether the compressed trace retains enough causal logic to support the correct answer. Thinking confidence measures whether the compressed trace remains linguistically coherent and reasoning-like under the auxiliary model. These rewards are combined, and the compression policy is trained with Group Relative Policy Optimization over candidate compressed traces.

A notable design choice is that the main reward is not an explicit length reward. The authors rely on a compression-oriented system prompt and confidence reward structure, arguing that direct compression-rate rewards can constrain exploration or become redundant once the policy internalizes the compression objective.

### Experiments and Results

The paper reports experiments over five reasoning benchmarks: AIME2025, MATH500, AMC23, MINERVA, and GPQA. The setup uses reasoning traces sampled from a subset of OpenThoughts-114k, trains the compression policy, uses compressed traces to construct fine-tuning data, and evaluates Qwen2.5 Instruct model sizes.

In the main results table, the Qwen2.5-7B original fine-tuned baseline reports average accuracy 54.2 with average token length 8,603. The ConMax version reports average accuracy 53.5 with average token length 4,906. The paper also reports that prompt-based compression is much shorter but loses substantially more performance, suggesting that unaligned shortening can erase useful reasoning structure.

The paper further decomposes Qwen2.5-7B results by generated token budget. ConMax shows stronger short-budget behavior at 4k, 8k, and 12k thresholds across the listed benchmarks, even where the original baseline has a marginal overall accuracy advantage. This supports the interpretation that ConMax is primarily a budgeted-reasoning efficiency method rather than a pure accuracy method.

### Limitations

The authors state that evaluation is concentrated on mathematical and scientific reasoning tasks. Generalization to broader domains, including creative writing and code generation, remains open. They also note that ultra-large models above 70B parameters and substantially different model families were not evaluated. The reward mechanism also depends on a frozen auxiliary reasoning model, leaving open whether self-supervised or execution-grounded alternatives could replace it.

### Black-Lake Context

The prior Black Lake Arxiv DEP run produced `.logs` and `.reports` artifacts for ConMax. This DEP-E deposit backfills the missing standard `.lake-data` manuscript layer and connects ConMax to related Black-Lake and Black-Lake-Data entries on semantic early stopping, HCRC verification-gated execution, UltraQuant KV-cache compression, and structured context eviction.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | ConMax uses answer confidence and thinking confidence from a frozen auxiliary reasoning model to train a compression policy. | Author claim supported by method section | E2 | Directly supported by methodology sections in the arXiv HTML. | High |
| C2 | In the inspected Qwen2.5-7B result, ConMax reduces average token length from 8,603 to 4,906 with average accuracy moving from 54.2 to 53.5. | Author empirical result | E2 | Directly supported by the main result table in arXiv HTML; not independently reproduced. | High for reporting, low for reproducibility |
| C3 | ConMax is better viewed as a reasoning-budget control method than a generic summarizer. | Reviewer interpretation | E2, E5-E7 | Reasonable synthesis from ConMax mechanism and related control-plane entries. | Medium |
| C4 | The current DEP is a backfill rather than a new random paper run. | Repository/process claim | E4 | Prior `.logs` and `.reports` ConMax artifacts already existed; user explicitly requested the missing DEP layer. | High |
| C5 | Future Arxiv DEP automation should deduplicate by arXiv ID/title across `.logs`, `.reports`, `.lake-data`, and memory before accepting a random paper. | Process requirement / reviewer implementation claim | E4, E8 | Supported by user instruction and repository stability needs. | High |

## Methodology

- `Research objective`: Produce the missing standard DEP-E manuscript deposit for the already-selected Black Lake Arxiv DEP ConMax run, and update the automation instructions so future runs always create this DEP layer.
- `Sources inspected`: ConMax arXiv abstract page, ConMax arXiv HTML full text, ConMax DOI, local arXiv archive metadata, Black-Lake README, prior ConMax `.logs` and `.reports` artifacts, and three related DEP entries.
- `Discovery strategy`: The prior manual run used fast PDF enumeration from the local arXiv archive and random selection. This backfill used that selected paper and did not reselect because the user explicitly requested the missing DEP for this task.
- `Inclusion criteria`: Sources were included when they identified ConMax, supported method/results/limitations, defined repository deposition rules, preserved prior run context, or provided related DEP concepts for synthesis.
- `Exclusion criteria`: Full local PDF extraction was excluded because extraction tooling was unavailable during the prior run; source files were not redistributed; related papers were not re-reviewed beyond the related DEP artifacts and source URLs.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, and DEP-ready provenance analysis.
- `Evidence handling`: Author claims and reported metrics are tied to arXiv HTML evidence. Reviewer synthesis is labeled as interpretation and connected to related DEP entries.
- `Uncertainty handling`: Reproducibility limits, unavailable extraction tooling, uninspected code/data, and related-entry evidence limits are stated explicitly.
- `Selection and deduplication note`: The original ConMax selection used fast `rg --files -g "*.pdf"` enumeration over the local arXiv archive and random selection from 53,107 PDF candidates. A marker search found no prior ConMax Arxiv DEP artifacts at that time. In this follow-up, deduplication intentionally found existing ConMax `.logs` and `.reports` artifacts; because the user explicitly requested a DEP backfill for the same task, the paper was not reselected.
- `Future cron validation`: The updated automation now requires scanning `.logs`, `.reports`, `.lake-data`, and automation memory for arXiv ID, DOI, title, and slug before accepting a random paper. If a duplicate exists, the cron must randomly reselect and record the duplicate reason privately.

## Scope, Constraints, and Assumptions

- `Scope`: Review ConMax as the selected Black Lake Arxiv DEP paper and create a DEP-ready manuscript plus DEP README.
- `Temporal boundary`: Sources available and inspected on 2026-07-08.
- `Evidence limits`: arXiv HTML and metadata were inspected; local PDF text extraction was unavailable; code, datasets, source package, and official implementation availability were not audited.
- `Assumptions`: The prior Arxiv DEP log and Report-Mark accurately preserve the original random selection context. The arXiv HTML rendering reflects the paper version used for this review.
- `Constraints`: Public artifacts must omit local absolute paths, usernames, exact local execution timestamps, and local timezone labels. Source files are not redistributed.
- `Out of scope`: Reproducing ConMax experiments, validating dataset construction, auditing code, collecting source PDFs, or benchmarking alternate compression methods.
- `Intended use`: DEP deposition, future Black-Lake research review, implementation planning, and automation hardening.
- `Audience`: Black-Lake reviewers, agent-infrastructure developers, and research operators working on reasoning-cost control.
- `Reproducibility boundary`: Reported paper metrics are preserved from the inspected source but not independently reproduced.
- `Data sensitivity`: Public paper metadata and repository artifacts; local archive path withheld.

## Observations

- `Observed pattern`: ConMax, semantic early stopping, HCRC, and cache/context compression all reframe reasoning as a controlled resource rather than an unlimited text stream.
- `Technical implication`: Reasoning-cost control should be layered: loop-level stopping, trace-level compression, action-level verification, and serving-level cache policy each handle a different source of waste or risk.
- `Contradiction or tension`: Compression improves efficiency but can reduce auditability if discarded reasoning is not represented by traceable evidence stubs.
- `Open question`: Can answer confidence and thinking confidence be replaced or supplemented by execution-grounded confidence for code and tool-use agents?
- `Reviewer hypothesis`: A shared confidence ledger across stopping, compression, memory admission, and cache retention would make agent-control decisions more auditable than independent heuristics.

## Considerations

ConMax should not be treated as a universal license to discard reasoning traces. In production settings, traces may carry audit value, source provenance, or debugging evidence. Compression should preserve enough metadata to explain what was removed, what confidence checks passed, and which original sources or executions support the final state.

The method is most directly supported for math and science reasoning benchmarks. Applying it to code agents, medical agents, or repository-changing workflows would require additional validation because correctness may depend on tool execution, external state, and downstream artifact integrity rather than final-answer probability alone.

The updated automation requirement to deduplicate selected papers is important because repeated random selection from tens of thousands of PDFs can still revisit a previously deposited paper over time. The selection process should therefore treat prior `.logs`, `.reports`, `.lake-data`, and memory entries as a used-paper index, not merely as optional context.

## Strengths

- ConMax has a clear operational target: reduce reasoning-token cost while preserving useful reasoning structure.
- The dual-confidence reward distinguishes answer fidelity from reasoning validity, which is stronger than optimizing for brevity alone.
- The inspected experiments include multiple Qwen2.5 model sizes and multiple reasoning benchmarks.
- The paper includes ablations that test reward design choices, including thinking-confidence weighting and explicit compression-rate rewards.
- The method connects naturally to agent-control infrastructure because it can be framed as a post-generation or data-preparation control policy.

## Weaknesses

- Results were not reproduced and code/data availability was not audited in this run.
- Evaluation is concentrated on math and science reasoning, so transfer to code, tool-use, retrieval, or open-ended planning remains uncertain.
- Dependence on a frozen auxiliary reasoning model may add cost, bias, or model-family coupling.
- Compression may discard reasoning details that are useful for audit, safety review, or debugging.
- The paper's effectiveness depends on confidence estimates being meaningful proxies for preserved reasoning quality.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add execution-grounded confidence | Code/tool-use agents | Final answers in agent workflows often depend on tool execution or tests. | Better transfer beyond math QA. | Requires sandboxed execution and task-specific validators. | Compare compressed traces on code repair and tool-use benchmarks with tests. |
| Preserve audit stubs for removed reasoning | Governance | Compression can harm reviewability. | Maintains provenance while reducing token volume. | Requires trace segmentation and metadata schema. | Human review of failure cases and audit reconstruction tests. |
| Evaluate against semantic early stopping | Loop control | Stopping early and compressing after generation solve adjacent waste problems. | Clarifies when each method is better. | Needs common benchmark and telemetry. | Run shared token-quality-cost metrics across iterative RAG/agent tasks. |
| Inspect official implementation availability | Reproducibility | DEP decisions should not assume code exists. | Better replication planning. | May find incomplete or unavailable artifacts. | Record repo, commit, setup instructions, and expected outputs if found. |
| Test cross-model reward robustness | Generalization | Auxiliary LRM confidence may encode model-family biases. | Reduces dependence on one evaluator. | More compute and evaluator variance. | Compare multiple auxiliary models and calibration curves. |

## Potential Implementations

1. Trace Compression Gate
   - `User`: Agent platform engineer.
   - `Goal`: Reduce stored reasoning volume without losing task-critical evidence.
   - `Core mechanism`: Compress traces only when answer confidence and coherence confidence stay above configured deltas.
   - `Required inputs`: Original trace, task answer, source references, confidence scorer, compression policy.
   - `Outputs`: Compressed trace, audit stub, confidence deltas, rejection reason if compression fails.
   - `Risk controls`: Preserve source IDs and failure cases; never compress regulated audit logs without policy approval.
   - `Evaluation`: Compare downstream task success and human audit reconstruction before and after compression.

2. Unified Reasoning Budget Controller
   - `User`: Research operator running iterative RAG or multi-agent workflows.
   - `Goal`: Stop, compress, or continue reasoning based on shared telemetry.
   - `Core mechanism`: Combine semantic delta, quality gain, answer confidence, and cache pressure into one controller.
   - `Required inputs`: Iteration drafts, embeddings, quality metrics, confidence scores, token/cost telemetry.
   - `Outputs`: Continue/stop/compress decisions and explanation records.
   - `Risk controls`: Escalate to full trace retention for low-confidence or high-impact tasks.
   - `Evaluation`: Token savings at fixed quality on multi-hop RAG and review workflows.

3. DEP Review Trace Minimizer
   - `User`: Black-Lake automation maintainer.
   - `Goal`: Store durable review artifacts without preserving unnecessary internal working traces.
   - `Core mechanism`: Convert verbose review notes into schema-complete manuscripts with evidence ledgers and attribution blocks.
   - `Required inputs`: Source URLs, local metadata, related DEP entries, generated reports, validation logs.
   - `Outputs`: DEP README, manuscript, Report-Mark, and log with minimal sensitive context.
   - `Risk controls`: Sanitization scan, dedup validation, source-only treatment of external documents.
   - `Evaluation`: Required-section pass rate, zero local-path leaks, and reviewer usefulness ratings.

## Three Ways to Exercise This Research

1. `Compression replay`: Objective: take a public toy reasoning dataset and compare original traces against manually compressed traces scored by a simple answer checker and coherence rubric. Inputs: public examples, synthetic scorer, and token counter. Method: compress, score, and compare token-quality tradeoffs. Output: small evaluation table. Success criterion: measurable token reduction without answer loss. Safety boundary: use public or synthetic data only.
2. `Agent-loop comparison`: Objective: compare ConMax-style post-hoc compression with semantic early stopping on an iterative RAG toy task. Inputs: public documents, queries, draft iterations, and embedding deltas. Method: run fixed-iteration, semantic-stop, and compress-after methods. Output: cost-quality comparison. Success criterion: identify which controller saves more tokens under parity answer quality. Safety boundary: no private documents or hidden chain-of-thought storage.
3. `Audit-stub prototype`: Objective: design a minimal metadata record for compressed traces. Inputs: source IDs, confidence deltas, removed segment labels, and final answer. Method: create an audit stub without preserving full reasoning. Output: JSON schema and sample artifact. Success criterion: reviewer can trace final answer to evidence and validation checks. Safety boundary: avoid storing sensitive raw traces.

## Example MVP Product

- `Product name`: Reasoning Trace Budgeter
- `Target user`: Engineers operating long-running LLM agents or research automations.
- `Problem`: Agents generate, store, and serve more reasoning text than necessary, but naive summarization can damage correctness and auditability.
- `Core workflow`: Ingest task trace, compute semantic progress and confidence scores, decide whether to continue/stop/compress, write a compressed trace plus audit stub, and route low-confidence cases to full retention.
- `Data requirements`: Public or authorized traces, final answers or validators, source IDs, token counts, confidence scores, and reviewer feedback.
- `Architecture`: Local controller service with pluggable scorers, compression policy, evidence-ledger writer, sanitization gate, and dashboard for rejected compressions.
- `Success metrics`: Token reduction, answer-quality parity, audit reconstruction success, false compression rejection rate, and zero sensitive-path leaks in durable artifacts.
- `Risk controls`: Local-only processing by default, no raw secret logging, human review for high-impact tasks, source-reference preservation, and rollback to full trace retention.
- `Limitations`: MVP confidence scorers may not generalize; code/tool tasks need execution validators; compressed traces may still omit useful debugging details.

Minimal illustrative sketch:

```python
from dataclasses import dataclass

@dataclass
class TraceDecision:
    action: str
    answer_delta: float
    coherence_delta: float
    audit_stub: dict


def decide_trace_policy(original, compressed, score):
    answer_delta = score.answer(original) - score.answer(compressed)
    coherence_delta = score.coherence(original) - score.coherence(compressed)
    if answer_delta <= 0.01 and coherence_delta <= 0.03:
        return TraceDecision(
            action="retain_compressed",
            answer_delta=answer_delta,
            coherence_delta=coherence_delta,
            audit_stub={"source_ids": compressed.source_ids, "policy": "conmax-like"},
        )
    return TraceDecision("retain_full", answer_delta, coherence_delta, {"reason": "confidence_drop"})
```

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| ConMax | Primary arXiv paper | Reviewed paper; confidence-maximizing compression for CoT reasoning. | https://arxiv.org/abs/2601.04973 |
| Semantic early stopping for iterative LLM agent loops | Related arXiv source via Black-Lake DEP | Loop-level token-control neighbor to trace compression. | https://arxiv.org/abs/2606.27009 |
| HCRC verification-gated LLM execution | Related arXiv source via Black-Lake-Data DEP | Execution-control neighbor using independent verification predicates. | https://arxiv.org/abs/2607.04562 |
| UltraQuant 4-bit KV caching | Related arXiv source via Black-Lake-Data DEP | Serving-layer memory and throughput neighbor for long-context agents. | https://arxiv.org/abs/2606.20474 |
| Structured context eviction | Related arXiv source via Black-Lake-Data DEP | Context lifecycle neighbor for long-horizon agent memory. | https://arxiv.org/abs/2606.11213 |
| Black-Lake Arxiv ConMax Report-Mark | Prior local artifact | Detailed synthesis note for same selected ConMax run. | Black-Lake/.reports/BL-Arxiv-ConMax-20260708/Report-Mark.md |
| Black-Lake Arxiv ConMax log | Prior local artifact | Selection and validation record for same selected ConMax run. | Black-Lake/.logs/20260708-Arxiv-ConMax-LOG.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2601.04973 | ConMax metadata, abstract, authors, DOI link, submitted date. | 2026-07-08 | Primary arXiv metadata page inspected. |
| R2 | https://arxiv.org/html/2601.04973 | ConMax method, experiments, result tables, ablations, limitations. | 2026-07-08 | arXiv HTML full text inspected. |
| R3 | https://doi.org/10.48550/arXiv.2601.04973 | Persistent DOI reference for ConMax. | 2026-07-08 | DOI referenced. |
| R4 | Local arXiv archive readme.md, path withheld | Selection provenance and local PDF/readme presence. | 2026-07-08 | Local path withheld under sanitization policy. |
| R5 | Black-Lake/README.md | DEP class, README, logs, reports, attribution, and commit-message standard. | 2026-07-08 | Local repository file inspected. |
| R6 | Black-Lake/.logs/20260708-Arxiv-ConMax-LOG.md | Prior brief ConMax Arxiv DEP log. | 2026-07-08 | Existing artifact from prior run. |
| R7 | Black-Lake/.reports/BL-Arxiv-ConMax-20260708/Report-Mark.md | Prior detailed ConMax Arxiv DEP Report-Mark and synthesis note. | 2026-07-08 | Existing artifact from prior run. |
| R8 | Black-Lake/.lake-data/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md | Related semantic early stopping entry. | 2026-07-08 | Related DEP artifact inspected. |
| R9 | Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 0104/daily_research_findings_2026-07-08_0104.md | Related HCRC verification-gated execution entry. | 2026-07-08 | Related DEP entry inspected. |
| R10 | Black-Lake-Data/.lake-data/DEP-20260629-Tech Intel 0104/daily_research_findings_2026-06-29_0104.md | Related UltraQuant and context lifecycle entries. | 2026-07-08 | Related DEP entry inspected. |
| R11 | https://arxiv.org/abs/2606.27009 | Primary source for semantic early stopping referenced by related DEP. | 2026-07-08 | Referenced through related artifact; full paper not re-reviewed here. |
| R12 | https://arxiv.org/abs/2607.04562 | Primary source for HCRC referenced by related DEP. | 2026-07-08 | Referenced through related artifact; full paper not re-reviewed here. |
| R13 | https://arxiv.org/abs/2606.20474 | Primary source for UltraQuant referenced by related DEP. | 2026-07-08 | Referenced through related artifact; full paper not re-reviewed here. |
| R14 | https://arxiv.org/abs/2606.11213 | Primary source for structured context eviction referenced by related DEP. | 2026-07-08 | Referenced through related artifact; full paper not re-reviewed here. |

## Appendix

### Random Selection Methodology Added to the Automation

Future `Black Lake Arxiv DEP` runs now use this process:

1. Enumerate PDF candidates with `rg --files -g "*.pdf"` from the local arXiv archive root.
2. Treat each PDF parent directory as one paper unit and attach nearby readme/metadata files when present.
3. Derive normalized paper identifiers from PDF names, readmes, and folder titles, preferring canonical arXiv IDs.
4. Randomly select by reservoir sampling or uniform random index over the `rg` output.
5. Build a used-paper index from `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, automation memory, and relevant Black-Lake-Data entries.
6. If the selected paper appears in prior Arxiv DEP artifacts or a prior DEP-E manuscript, reject it, record the duplicate privately, and randomly reselect.
7. If the run is an explicit user-requested backfill or correction, allow reuse only when the final artifact states that it is a backfill rather than a fresh random selection.

### Current Backfill Validation

- Existing ConMax `.logs` and `.reports` artifacts were found, so a normal future cron run would reselect.
- This run did not reselect because the user explicitly requested the missing standard DEP manuscript for the already-selected ConMax task.
- Required manuscript headings are present.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- `## Example MVP Product` includes product name, target user, problem, workflow, data requirements, architecture, success metrics, risk controls, and limitations.
- Public artifacts were written without local absolute paths, home directory names, local timezone labels, or exact local execution timestamps.
