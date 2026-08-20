---
title: "Prompt Compression - DEP-E"
generated_at: "2026-08-16"
artifact_type: "DEP research artifact"
primary_subject: "An iterative review of prompt compression as a cost-saving complement and contrast to evidence replay in stateful agent systems."
source_status: "URLs and repository files only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-16"
temporal_cutoff: "2026-08-16"
primary_url: "https://arxiv.org/abs/2310.05736"
stable_identifier: "DEP-20260706-Tech Intel 1110; arXiv:2310.05736v2"
confidence_summary: "High for the inspected LLMLingua mechanism and reported tables; medium for transfer and implementation readiness; low for independent reproducibility because no code, model, dataset, or benchmark was executed."
safety_scope: "Defensive evaluation, evidence preservation, and authorized research"
distribution_notes: "No source payloads are redistributed; repository-relative provenance and canonical public URLs are preserved."
---

# Prompt Compression - DEP-E

## Source Metadata

This artifact is the third review pass for `Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 1110`. The source DEP contains a ten-finding synthesis centered on memory, context governance, agent safety, evaluation, AI-for-science, and constrained computation. Earlier passes produced a broad memory-and-agent-safety manuscript and an evidence-replay expansion. This pass randomly selected LLMLingua from the prior pass's retained primary reading list and inspected its canonical arXiv record and full HTML paper. The official Microsoft implementation repository was inspected as a contextual implementation locator; no code was executed.

| ID | Source | Role | Type | Identifier / Version | URL / Repository-relative path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | Selected source DEP | Research-object boundary and source inventory | Markdown repository deposit | Source commit `3b50d2d` | `Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 1110/` | Public repository evidence; no source file copied into this deposit | 2026-08-16 | README, findings, and iterative lineage inspected |
| S1 | Prior source report, Report-Mark 002, output log, and DEP-E manuscript | Iterative provenance and prior evidence boundary | Markdown repository records | 2026-07-31 pass | `Black-Lake-Data/.reports/BL-DEP-20260706-Tech Intel 1110-20260731/README.md`; `Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 1110/BL-DEP-Mark002 Report-Mark.md`; `Black-Lake/.logs/20260731-DEP-20260706-Tech Intel 1110-LOG.md`; `Black-Lake/.lake-data/DEP-E/DEP-E-20260731-Evidence Replay/` | Prior synthesis is context, not independent revalidation | 2026-08-16 | Inspected before the new draw |
| S2 | *LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models* | Newly expanded primary work | arXiv HTML and canonical record | arXiv:2310.05736v2; revised 2023-12-06 | https://arxiv.org/abs/2310.05736; https://arxiv.org/html/2310.05736v2 | Paper page identifies EMNLP 2023 acceptance; no source payload collected | 2026-08-16 | Full HTML inspected beyond the abstract |
| S3 | `microsoft/LLMLingua` | Official implementation context | GitHub repository | Main branch as accessed | https://github.com/microsoft/LLMLingua | Repository presents an MIT license; code was not downloaded or executed | 2026-08-16 | README and public structure inspected |
| S4 | Prior retained primary threads | Comparative context | arXiv records and prior manuscript references | ReContext, RULER, Lost in the Middle, SnapKV, LongLLMLingua, and earlier memory/safety works | See `## Related Research and Reading` and `## Source References` | Prior evidence is not treated as a new independent experiment | 2026-08-16 | Retained from the prior artifact |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | `Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 1110/` at source commit `3b50d2d` | Primary repository deposit | README, ten-finding synthesis, attribution, and prior lineage | Research boundary, memory/context framing, and provenance | High | The source DEP is a curated synthesis rather than a single controlled study |
| E2 | `Black-Lake/.lake-data/DEP-E/DEP-E-20260731-Evidence Replay/` and matching Report-Mark 002 | Prior DEP research artifact | Prior evidence ledger, ReContext expansion, comparative reading list, and open replication agenda | Iterative relationship between replay and compression | Medium | Prior claims were not independently rerun in this pass |
| E3 | https://arxiv.org/html/2310.05736v2 | Primary full paper | Method sections, equations, experiment settings, tables, ablations, overhead analysis, limitations, and appendices | LLMLingua mechanism, reported results, cost model, and boundaries | High | Results are author-reported; no independent reproduction was performed |
| E4 | https://arxiv.org/abs/2310.05736 | Primary canonical record | Authors, v2 date, abstract, venue note, DOI, and code locator | Work identity and headline scope | High | Abstract-level evidence is incomplete for detailed empirical claims |
| E5 | https://github.com/microsoft/LLMLingua | Official implementation context | Public repository structure, README, quick-start surface, and stated series scope | Implementation availability and practical integration surface | Medium | Repository claims were not audited against execution, versions, or benchmark outputs |
| E6 | https://arxiv.org/abs/2404.06654 and related prior record | Primary benchmark context | RULER retained as a long-context evaluation neighbor | Need for task-complexity-sensitive evaluation | Medium | This pass did not reopen the full RULER paper |
| E7 | https://arxiv.org/abs/2307.03172 and related prior record | Primary analysis context | Lost-in-the-Middle retained as a position-sensitivity neighbor | Context placement as a comparison dimension | Medium | This pass did not reopen the full paper |

## Executive Summary

The selected source DEP treats memory and context as system boundaries: they can improve long-horizon capability while also creating provenance, safety, and evaluation risks. The prior pass expanded ReContext, which retains the full context and replays a query-conditioned evidence pool. This pass adds LLMLingua as a complementary and contrasting mechanism: it removes lower-scored prompt content using a smaller language model, a component-aware budget controller, iterative token-level compression, and optional distribution alignment.

The LLMLingua paper reports experiments on GSM8K, BBH, ShareGPT, and Arxiv-March23. Under the reported settings, its method reaches 5x compression on GSM8K in a one-shot constraint with 79.08 exact match versus 78.85 for the full-shot reference, and 20x compression with 77.33 exact match in the quarter-shot setting. On BBH, the reported exact match is 70.11 at 3x compression in the one-shot setting, falling to 56.85 at 7x in the quarter-shot setting. The paper also reports 1.7x to 5.7x end-to-end speedups on a V100-32G setup across tested compression rates.

Those results support a narrower conclusion than “compression preserves meaning.” They show that a particular compressor, small-model configuration, prompt budget, target model, dataset, and metric combination can preserve or improve selected task scores while reducing prompt tokens. The paper itself reports substantial degradation at approximately 25x–30x compression and notes tokenizer mismatch as a source of length-estimation error. The reviewer inference is that prompt compression is a resource-optimization layer, not a source-integrity or outcome-verification layer.

For the Black-Lake lineage, the important relationship is architectural: compression reduces what the target model receives, while evidence replay retains the original context and adds selected evidence near generation. A provenance-preserving system may use either approach, or compare them under matched evidence, latency, and failure-accounting rules. It must not treat a shorter prompt as proof that discarded material was irrelevant.

## Detailed Summary

### Research object and problem

LLMLingua addresses the cost and context-length pressure created by long prompts containing demonstrations, instructions, questions, conversations, or retrieved documents. The paper formulates compression as producing a shorter prompt whose target-model generation distribution is as close as possible to the original prompt's output distribution, while reducing the compression rate `tau` and therefore input length.

The selected DEP's broader context matters because prompt length is only one part of stateful AI reliability. The earlier ten findings connect memory to persistent-state attacks, executable safety evaluation, context governance, exact or fixed-footprint memories, reasoning drift, clinical evaluation, grounded scientific work, and quantum memory limits. LLMLingua contributes a distinct mechanism for the efficiency side of that map.

### Method and mechanism

The method is coarse-to-fine:

1. A budget controller allocates different compression rates to instructions, demonstrations, and questions. The paper assigns more protection to instructions and questions and uses sentence- or demonstration-level selection when aggressive compression would make token-level deletion linguistically brittle.
2. A small language model scores demonstrations and prompt segments using perplexity. Demonstrations are selected in descending perplexity order until the component budget is reached.
3. Iterative token-level prompt compression recalculates conditional probabilities after each segment's compressed tokens are carried into the following segment. Tokens above a dynamically computed perplexity threshold are retained.
4. Distribution alignment instruction-tunes the small compressor on data generated by the target LLM, attempting to reduce the gap between the small model's token distribution and the black-box target model's distribution.

This mechanism differs from simple random or sentence selection because it uses component-specific budgets and iterative context dependence. It also differs from generation-based summarization: the paper argues that generated summaries have less controllable length and may omit reasoning paths or introduce unrelated content.

### Experimental design

The paper evaluates reasoning and in-context learning with GSM8K and BBH, conversation with ShareGPT, and summarization with Arxiv-March23. It reports Exact Match for GSM8K and BBH, and BLEU, ROUGE, and BERTScore for the two contextual-understanding tasks. Target models include GPT-3.5-Turbo-0301 and Claude-v1.3; greedy decoding at temperature 0 is used in the reported experiments. The compressor uses Alpaca-7B or GPT2-Alpaca, a granular control coefficient of 2, instruction and question compression rates of 0.85 and 0.9, and a segment size of 100 tokens.

The appendix states that experiments used a Tesla V100 with 32 GB memory, GPT2-Alpaca was trained on the Alpaca dataset for eight epochs at learning rate 1e-4 with AdamW, and token counting used tiktoken and GPT-3.5-Turbo. These details make the results more auditable, but they also bound transfer: current model APIs, tokenizer behavior, pricing, and hardware may differ.

### Reported results

On GSM8K, the paper reports 79.08 Exact Match with 446 tokens at 5x compression in the one-shot setting, compared with 78.85 and 2,366 tokens for the full-shot reference. In the half-shot and quarter-shot settings, the reported scores are 77.41 at 14x and 77.33 at 20x. On BBH, the corresponding reported scores are 70.11 at 3x, 61.60 at 5x, and 56.85 at 7x, compared with a full-shot score of 70.07.

For ShareGPT and Arxiv-March23, the paper reports that the method reaches 1.9x and 4x compression under one constraint, with BERTScore F1 values of 89.52 and 90.33, respectively. Under a more aggressive constraint, it reports 3.3x and 9x compression with BERTScore F1 values of 87.70 and 89.03. These are table-specific claims and should not be generalized to arbitrary conversations or documents.

The ablation table attributes measurable changes to the named components. On GSM8K in the one-shot setting, removing iterative token-level compression reduces Exact Match from 79.08 to 72.93; removing the budget controller reduces it to 73.62; replacing budgeted selection with random selection reduces it to 72.78; and removing distribution alignment reduces it to 78.62. These comparisons are informative about the paper's internal design, but they do not isolate all interactions or establish transfer beyond the tested configuration.

The paper models total computation as compressor work plus target-model inference. Under an assumption that the small model's per-token cost is approximately one twenty-fifth of the target model's cost, it estimates about four-fold computational savings at a 5x compression rate. Its latency table reports 8.6 seconds without LLMLingua and 4.9, 2.3, and 1.3 seconds end-to-end at 2x, 5x, and 10x compression, with compressor-only times of 0.8, 0.3, and 0.2 seconds. The latency result is conditioned on the V100 setup and the paper's accounting.

### Limitations and relation to evidence replay

The paper reports substantial performance drops at approximately 25x–30x compression on GSM8K and states that the upper compression limit varies by prompt length, task type, and sentence count. It also warns that different tokenizers between the small model and target LLM can underestimate prompt length. The small-model distribution is an additional dependency: experiments with GPT2-Alpaca trail Alpaca-7B by 2.06, 0.99, and 1.06 Exact Match points at the reported compression settings even after alignment.

ReContext and LLMLingua optimize different failure modes. ReContext retains the full prompt and replays selected spans to improve use of long-context information; LLMLingua deletes or condenses content to reduce input and inference cost. Compression can remove provenance-bearing qualifiers, counterexamples, or contradictory evidence; replay can amplify a stale or injected span if eligibility is not governed. A combined evaluation should therefore measure answer quality, evidence coverage, discarded-span risk, selection provenance, latency, memory, and end-to-end failure handling.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | LLMLingua uses a budget controller, iterative token-level compression, and distribution alignment to compress prompts for black-box target LLMs. | Author claim supported by method sections | E3 | Directly supported by the full paper's method and equations. | High |
| C2 | The paper reports up to 20x compression with little performance loss in selected settings. | Author claim | E3, E4 | Supported for the reported GSM8K and related tables; “little” is task- and ratio-dependent, not universal. | High |
| C3 | Component-aware budgets and iterative selection matter to the reported GSM8K result. | Reviewer interpretation of ablations | E3 | Ablations show lower scores when these components are removed, but the causal attribution is limited to the paper's configuration. | Medium-high |
| C4 | Compressor overhead can be outweighed by target-model token savings under the paper's cost assumptions. | Author claim with implementation interpretation | E3 | Supported by the reported V100 latency table and stated cost model; transfer to current services is unverified. | Medium-high |
| C5 | Prompt compression is not a provenance or truth-preservation guarantee. | Derived reviewer inference | E1, E2, E3 | Compression changes the evidence boundary and can remove qualifiers; the paper does not claim source authorization or answer verification. | High |
| C6 | Compression and evidence replay should be compared as complementary resource policies rather than interchangeable methods. | Derived reviewer inference | E2, E3, E5 | The mechanisms operate on different axes: deletion/condensation versus retention plus replay. | Medium-high |

## Methodology

- `Research objective`: Extend the selected source DEP's living research record with one randomly chosen primary related work, and determine how prompt compression relates to evidence replay, provenance, cost, and evaluation.
- `Sources inspected`: The selected source DEP README and daily findings, prior source report, prior Report-Mark 002, prior output log, prior DEP-E README and manuscript, LLMLingua's canonical arXiv record, the complete LLMLingua v2 HTML paper, and the official Microsoft LLMLingua repository README and public structure.
- `Discovery strategy`: Enumerated canonical DEP directories and recent markers through live repository trees; inspected prior lineage; drew one supporting thread from the retained primary reading list using an operating-system cryptographic random source; opened the canonical arXiv abstract and full HTML paper; inspected the official implementation locator.
- `Inclusion criteria`: Evidence that defined the selected DEP, the most recent iterative lineage, LLMLingua's mechanism, reported experiments, ablations, overhead, limitations, and direct comparative neighbors.
- `Exclusion criteria`: No source PDF, TeX package, dataset, model, dependency, prompt corpus, execution trace, or benchmark payload was collected. Other retained papers were kept as prior context and were not treated as newly re-reviewed in this pass.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication planning.
- `Evidence handling`: Major claims receive evidence IDs and are labeled as source claims, reviewer interpretations, or derived inferences. Reported numbers retain their task, model, compression, and hardware conditions.
- `Uncertainty handling`: Missing execution, unavailable payloads, configuration transfer, licensing details for cited datasets, tokenizer mismatch, and untested production behavior are stated explicitly rather than inferred away.
- `Extraction process`: The paper's abstract, introduction, method, experiment settings, result tables, ablations, overhead section, limitations, conclusion, and appendices were inspected in HTML. The official repository was used for implementation context only.
- `Version control`: The selected source repository was pinned to commit `3b50d2ddfc471398e3647abe76d6d748ea8bf5f0`; LLMLingua was reviewed at arXiv v2, revised 2023-12-06. Prior artifacts retain their own pinned commits in the source references.
- `Claim selection`: Central mechanism, exact reported metrics, component ablations, latency, cost assumptions, failure boundaries, and the compression-versus-replay relationship were prioritized.
- `Cross-checking`: Paper identity was checked against the canonical arXiv record; reported values were read from the HTML tables and surrounding text. No independent numeric recomputation was performed.
- `Safety handling`: Proposed uses are limited to authorized evaluation, synthetic or public data, provenance-aware compression, and human-reviewed research. Compression is not proposed as a safety or clinical decision authority.
- `Reviewer stance`: Iterative DEP-ready research artifact combining literature expansion, comparative analysis, implementation planning, and replication-gap preservation.

## Scope, Constraints, and Assumptions

- `Scope`: The selected ten-finding DEP lineage plus one newly expanded supporting work, LLMLingua, with emphasis on prompt compression, evidence preservation, cost, and evaluation.
- `Temporal boundary`: Public artifact date 2026-08-16; LLMLingua evidence is arXiv:2310.05736v2 and repository context was inspected as accessed on that date.
- `Evidence limits`: No code, model, dataset, dependency, prompt corpus, benchmark payload, or execution trace was collected or executed. Several related works are retained from prior review rather than reopened in this pass.
- `Assumptions`: The prior Report-Mark's related-reading list is an accurate provenance record for its earlier pass; the LLMLingua HTML rendering faithfully exposes the cited tables and appendices; the source commit identified by the live repository is the selected DEP snapshot.
- `Constraints`: Public repository artifacts must exclude private filesystem context and restricted source payloads. Dataset rights, API pricing, model versions, and current repository behavior require separate verification before deployment.
- `Out of scope`: Clinical advice, production performance guarantees, security certification, unauthorized prompt extraction, private-data processing, independent reproduction, or judgment about the correctness of unrelated prior papers.
- `Intended use`: DEP deposition, follow-on review, provenance-aware system design, safe benchmark planning, and research backlog formation.
- `Audience`: Research engineers, evaluation designers, agent-memory reviewers, provenance/governance reviewers, and future Black-Lake maintainers.
- `Depth target`: Schema-complete iterative manuscript research artifact.
- `Reproducibility boundary`: A reviewer can locate the paper and repository and reconstruct the reported setup conceptually; reproducing tables requires the stated models, data, dependencies, prompts, hardware, and access to any external services.
- `Operational boundary`: The artifact may discuss compression and selection mechanisms conceptually, but it does not provide instructions for bypassing safety controls or handling private prompts.
- `Data sensitivity`: Public research sources and repository metadata only; no personal, restricted, or proprietary data was collected.

## Observations

- **Observed pattern:** LLMLingua treats prompt length as a controllable budget across instructions, demonstrations, and questions rather than applying one global deletion rate. This aligns with the broader DEP theme that state needs typed boundaries and explicit policies.
- **Technical implication:** The ablations suggest that selection policy is part of the method. A benchmark that compares only final token counts without recording the budget controller, small model, segment size, and alignment regime is not comparing the same system.
- **Observed tension:** Compression reduces target-model work, while replay increases the salience of selected evidence. The two can trade cost against evidence visibility in opposite directions.
- **Observed limitation:** The paper's most aggressive ratios show clear task sensitivity: GSM8K remains comparatively strong at 20x in the reported quarter-shot setting, whereas BBH falls materially at 7x. This is evidence for a task-conditioned envelope, not a universal ratio.
- **Reviewer hypothesis:** Provenance-bearing compression that retains source IDs, offsets, version labels, and dropped-span summaries could make deletion auditable, but the hypothesis requires a matched evaluation.
- **Open question:** Whether a single compression policy transfers across unseen task families is unresolved; the prior evidence-replay log identifies the analogous configuration-transfer problem for replay.

## Considerations

Prompt compression changes what a downstream model can inspect. For evidence-rich or high-impact use, the original prompt should remain available in a controlled audit store, and the compressed prompt should carry a manifest of source identifiers, spans retained, spans dropped, compression model, tokenizer, target model, budget, and version. A shorter prompt must not be treated as a complete evidence record.

The paper uses public benchmark families, API-accessed target models, and a small model trained on Alpaca. Dataset licenses, data collection terms, model access, and current API pricing are separate questions from the reported metrics. The official repository's quick-start surface indicates practical accessibility, but repository presence is not proof of reproducibility or production readiness.

For security and safety work, compression may delete adversarial indicators, policy qualifiers, or the evidence needed to explain a refusal. For medical, legal, financial, or scientific uses, loss of caveats can be more important than average score preservation. Safe use therefore requires human review, task-specific retention rules, held-out tests, and a fail-closed path when compression uncertainty exceeds a threshold.

Operationally, compressor latency, model loading, tokenizer mismatch, cache behavior, retries, API cost, and storage of the original prompt must be measured end to end. The paper's V100 results are useful baselines but should not be copied as current service-level expectations.

## Strengths

- The method is decomposed into named, testable components rather than presented as an opaque summary step.
- The paper reports multiple task families, compression regimes, ablations, target models, small models, latency, and appendix details.
- The reported tables preserve exact task metrics and token counts, making the main resource-quality tradeoff inspectable.
- The limitations section explicitly names extreme-ratio degradation and tokenizer mismatch, which are relevant to downstream governance.
- The official repository provides a public implementation and integration surface that can support an authorized replication plan, subject to dependency and version review.

## Weaknesses

- The empirical evidence is author-reported and was not independently executed in this pass.
- The evaluation uses a bounded set of datasets and model versions; the paper does not establish task-agnostic transfer to modern long-context or agent workloads.
- Compression quality is measured primarily through downstream task metrics, not through a general evidence-coverage, contradiction-preservation, or provenance-retention metric.
- The reported compute savings depend on assumptions about relative small-model and target-model costs and a specific hardware/API environment.
- The source and benchmark payloads, external model calls, prompt construction, and dependency environment were not deposited, so a later reviewer must reconstruct them.
- The official repository README includes broad series-level claims; those claims were treated as implementation context, not as independent evidence for the paper's tables.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add source-span retention and deletion manifests | Provenance | Compression can remove qualifiers or contradiction evidence silently | Auditable prompt transformation | More storage and schema work | Compare claim support and omission rates with and without manifests |
| Freeze compression policy on one task family and test unseen families | Generalization | Current results are configuration-specific | Separates transfer from tuning | Requires new held-out data and compute | Preregister ratios, models, and failure accounting before evaluation |
| Compare compression, replay, and full-context baselines at matched budgets | Comparative evaluation | Token ratio alone hides different evidence boundaries | Clarifies cost-quality frontier | More experimental cells | Use identical prompts, target models, latency budget, and per-case outputs |
| Add contradiction and critical-qualifier retention tests | Safety and evidence | Average scores can conceal high-impact deletions | Detects unsafe evidence loss | Requires labeled synthetic or public cases | Measure retention of required clauses and refusal triggers |
| Report end-to-end costs with current tokenizer/API/hardware coordinates | Operations | The paper's cost model is conditional | Improves deployment decisions | Requires access to current services | Include compressor loading, retries, caching, and storage in cost ledger |

## Potential Implementations

### Provenance-aware prompt compression sidecar

- `User`: Evaluation engineer or research agent operating on authorized public or synthetic documents.
- `Goal`: Reduce prompt cost while preserving an auditable map from compressed tokens to source spans.
- `Core mechanism`: Run a version-pinned compressor with component budgets; emit compressed prompt plus retained/dropped span manifest and uncertainty flags.
- `Required inputs`: Original prompt, source IDs and offsets, tokenizer, compressor version, target-model identifier, budget, and retention policy.
- `Outputs`: Compressed prompt, manifest, token counts, estimated cost, and a review warning when critical spans are dropped.
- `Risk controls`: Local-only processing for sensitive inputs, no raw prompt logging, protected original store, human approval for high-impact tasks, and fail-closed critical-span rules.
- `Evaluation`: Synthetic evidence sets with known qualifiers, contradiction pairs, and held-out task families; compare answer quality, evidence coverage, cost, and omission rate.

### Compression-versus-replay evaluation harness

- `User`: Long-context systems researcher.
- `Goal`: Compare full context, LLMLingua-style compression, ReContext-style replay, and governed combinations under matched resource budgets.
- `Core mechanism`: Reuse identical versioned corpora and questions; vary only the context policy; log selected, removed, replayed, and cited spans.
- `Required inputs`: Public or synthetic corpus, question set, target model, compressor/replay configurations, budget, and scoring rules.
- `Outputs`: Per-case answers, latency, token counts, evidence manifests, contradiction outcomes, and failure categories.
- `Risk controls`: Synthetic data by default, no unauthorized prompt collection, bounded rate, no deployment decisions from one benchmark, and independent review of scoring.
- `Evaluation`: Preregistered comparison with repeated seeds where applicable, held-out tasks, critical-error floors, and matched cost accounting.

### Evidence-preserving document gateway

- `User`: Research or knowledge-management team.
- `Goal`: Prepare large public document bundles for downstream agents without losing source identity or auditability.
- `Core mechanism`: Store immutable originals, produce compressed views for routine queries, retain source-aware manifests, and escalate to full-context review when confidence or coverage is low.
- `Required inputs`: Public documents, source metadata, retention policy, query, and approved model configuration.
- `Outputs`: Versioned compressed view, source map, coverage report, and escalation decision.
- `Risk controls`: License review, access control, deletion policy, privacy filtering, no model-generated provenance, and human review for high-impact outputs.
- `Evaluation`: Retrieval/answer quality, source attribution accuracy, coverage of critical sections, cost, latency, and escalation precision.

## Three Ways to Exercise This Research

1. **Synthetic qualifier-retention test:** Objective: measure whether compression preserves required caveats. Inputs: a synthetic corpus containing positive claims, exceptions, dates, and contradictions. Method: run full-context and version-pinned compression at 2x, 5x, 10x, and 20x; record retained spans and answer support. Output: a coverage/omission table. Success criterion: every marked critical qualifier is either retained or triggers escalation. Stop condition: stop if raw prompts cannot be kept in a protected audit store or if outputs are used for real decisions.
2. **Matched compression-versus-replay benchmark:** Objective: compare deletion and replay as context policies. Inputs: public or synthetic long-context tasks, identical target model, fixed token and latency budgets. Method: evaluate full context, compression, replay, and a governed hybrid with per-case provenance. Output: paired quality, cost, latency, and evidence-coverage results. Success criterion: the tradeoff is reported without hiding critical failures. Stop condition: stop when one policy lacks a comparable evidence manifest or when the budget cannot be matched.
3. **Configuration-transfer audit:** Objective: test whether a compression setting transfers beyond its tuning task. Inputs: one calibration family and at least two unseen synthetic task families. Method: freeze compressor, small model, tokenizer, budgets, and target model after calibration; evaluate without retuning. Output: transfer report with confidence intervals and failure categories. Success criterion: any claimed transfer is supported by preregistered thresholds and per-task outcomes. Stop condition: stop if the unseen tasks are selected after seeing results or if model/data rights are unclear.

## Example MVP Product

- `Product name`: Evidence Budget Gateway
- `Target user`: Research engineer building a provenance-aware long-context agent.
- `Problem`: Long prompts increase cost and latency, but naive deletion can remove qualifiers, contradictions, and source traceability.
- `Core workflow`: Ingest an authorized versioned document bundle; create a compression manifest; generate a compressed view with configurable component budgets; score source coverage; answer only when critical-span and integrity checks pass; otherwise escalate to full-context review.
- `Data requirements`: Public or synthetic documents, stable source IDs, offsets, version metadata, critical-span annotations, tokenizer, compressor, target model, and evaluation set.
- `Architecture`: Local manifest store plus immutable original store, compressor sidecar, policy/coverage validator, target-model adapter, result ledger, and human-review queue. Sensitive content remains local by default.
- `Success metrics`: Prompt-token reduction, end-to-end latency, cost per task, critical-span retention, citation/source-map accuracy, contradiction detection, escalation precision, and task quality under held-out workloads.
- `Risk controls`: No raw secrets in logs, access-controlled originals, license review, version pinning, critical-span fail-closed rules, model/provider allowlist, human approval for high-impact domains, and rollback to full context.
- `Limitations`: The MVP cannot certify truth, safety, fairness, or production readiness; it depends on task-specific retention policies and may increase cost when escalation is frequent.
- `MVP boundary`: Synthetic/public text and offline evaluation only; no clinical, legal, financial, or autonomous external actions.
- `Deployment model`: Local service or batch CLI with an optional approved target-model adapter.
- `Evaluation plan`: Unit tests for span mapping and token accounting, synthetic qualifier/contradiction tests, matched full-context baseline, held-out transfer test, and human audit of sampled manifests.
- `Failure modes`: Omitted qualifiers, tokenizer mismatch, unstable compression across versions, misleading coverage scores, compressor overhead exceeding savings, and false confidence from high aggregate task scores.
- `Maintenance plan`: Pin models and tokenizers, refresh cost assumptions, review retention policies, re-run held-out suites after dependency changes, and archive manifests with each result.

## Related Research and Reading

**New in this pass:** LLMLingua was selected by an OS-cryptographic draw from the 15 primary threads retained by Report-Mark 002. The full v2 paper and official implementation context were inspected. The prior evidence-replay and memory/safety lineage is retained for comparison; it was not re-run as a new experiment.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| **New — LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models** | Primary paper | Budget-controlled coarse-to-fine prompt compression, iterative token selection, alignment, results, ablations, and overhead | https://arxiv.org/abs/2310.05736; https://arxiv.org/html/2310.05736v2; https://doi.org/10.48550/arXiv.2310.05736 |
| **New — microsoft/LLMLingua** | Official implementation | Public package surface, prompt-compression examples, and series-level implementation context | https://github.com/microsoft/LLMLingua |
| ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning | Prior primary paper | Retains full context while replaying a query-conditioned evidence pool; direct contrast to deletion-based compression | https://arxiv.org/abs/2607.02509; https://arxiv.org/html/2607.02509v1; https://doi.org/10.48550/arXiv.2607.02509 |
| RULER | Prior primary benchmark paper | Long-context evaluation across varied task complexity and retrieval demands | https://arxiv.org/abs/2404.06654; https://doi.org/10.48550/arXiv.2404.06654 |
| Lost in the Middle | Prior primary analysis paper | Position-sensitive context use and a failure mode relevant to compression and replay | https://arxiv.org/abs/2307.03172; https://doi.org/10.48550/arXiv.2307.03172 |
| SnapKV | Prior primary systems paper | Prompt-internal attention signals for KV selection; a neighboring but distinct optimization target | https://arxiv.org/abs/2404.14469; https://doi.org/10.48550/arXiv.2404.14469 |
| LLMLingua-2 | Near-primary follow-up | Later task-agnostic compression direction surfaced by the official implementation repository | https://aclanthology.org/2024.findings-acl.57/ |
| LongLLMLingua | Prior/near-primary long-context compression work | Long-context compression and retrieval-quality comparison | https://arxiv.org/abs/2310.06839; https://aclanthology.org/2024.acl-long.91/ |
| Distributed Attacks in Persistent-State AI Control | Prior primary context | Stateful threat model showing why persistent source and code state needs monitoring | https://arxiv.org/abs/2607.02514 |
| Safety Testing LLM Agents at Scale | Prior primary context | Executable safety cases and state-grounded verification | https://arxiv.org/abs/2607.01793 |
| ContextNest | Prior primary context | Context eligibility, version identity, deterministic selection, and audit traces | https://arxiv.org/abs/2607.02116 |
| A Hippocampus for Linear Attention | Prior primary context | Bounded exact memory as an alternative to pure compression or recurrence | https://arxiv.org/abs/2607.02303 |
| InduceKV | Prior primary context | Fixed-footprint continual adaptation through retrieved KV memories | https://arxiv.org/abs/2607.02010 |
| DRIFTLENS | Prior primary context | Memory-induced reasoning drift and the need for evaluation beyond final answers | https://arxiv.org/abs/2607.02374 |
| Rubric-based clinical reasoning comparison | Prior primary context | Consequence-weighted evaluation and critical-failure visibility; not clinical guidance | https://arxiv.org/abs/2607.02175 |
| Grounded autonomous research | Prior primary context | Durable state, anchor reproduction, and calibration checkpoints for agentic research | https://arxiv.org/abs/2607.02329 |
| Optimal Stabilizer Testing and Learning with Limited Quantum Memory | Prior theory context | Memory as a formal resource boundary in a different computational setting | https://arxiv.org/abs/2607.02444 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [Selected source DEP at commit `3b50d2d`](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/3b50d2ddfc471398e3647abe76d6d748ea8bf5f0/.lake-data/DEP-20260706-Tech%20Intel%201110) | Research boundary, inventory, tags, and original ten-finding synthesis | 2026-08-16 | Repository files inspected; no source files copied |
| R1 | [Selected DEP README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/3b50d2ddfc471398e3647abe76d6d748ea8bf5f0/.lake-data/DEP-20260706-Tech%20Intel%201110/README.md) | Contents, source roles, and original attribution | 2026-08-16 | Source metadata |
| R2 | [Daily research findings](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/3b50d2ddfc471398e3647abe76d6d748ea8bf5f0/.lake-data/DEP-20260706-Tech%20Intel%201110/daily_research_findings_2026-07-06_1110.md) | Ten original findings and their memory/context framing | 2026-08-16 | Inspected as source context |
| R3 | [Prior source report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/b0cb541844ca7eb9cf32407a49fef6d81d6a8310/.reports/BL-DEP-20260706-Tech%20Intel%201110-20260727/README.md) | First-pass selection, evidence boundary, and prior limitations | 2026-08-16 | Prior operational record |
| R4 | [Prior Report-Mark 002](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/b0cb541844ca7eb9cf32407a49fef6d81d6a8310/.lake-data/DEP-20260706-Tech%20Intel%201110/BL-DEP-Mark002%20Report-Mark.md) | Prior exact related-reading and reference baseline | 2026-08-16 | Inspected before the new draw |
| R5 | [Prior output log](https://github.com/Delphoa/Black-Lake/blob/e103b6df0b685381091fa1e472495e238149a929/.logs/20260731-DEP-20260706-Tech%20Intel%201110-LOG.md) | Prior selection record, questions, challenges, and validation gaps | 2026-08-16 | Operational lineage |
| R6 | [Prior DEP-E manuscript](https://github.com/Delphoa/Black-Lake/blob/e103b6df0b685381091fa1e472495e238149a929/.lake-data/DEP-E/DEP-E-20260731-Evidence%20Replay/evidence-replay.md) | ReContext mechanism, replay contrast, and prior replication agenda | 2026-08-16 | Prior artifact; not independently rerun |
| R7 | [LLMLingua canonical record](https://arxiv.org/abs/2310.05736) | Title, authors, v2 date, venue note, abstract, DOI, and code locator | 2026-08-16 | Primary record |
| R8 | [LLMLingua full v2 HTML](https://arxiv.org/html/2310.05736v2) | Method, equations, experiment settings, tables, ablations, overhead, limitations, and appendices | 2026-08-16 | Primary full-text evidence |
| R9 | [LLMLingua DOI](https://doi.org/10.48550/arXiv.2310.05736) | Persistent canonical locator | 2026-08-16 | Locator, not separate empirical evidence |
| R10 | [Microsoft LLMLingua repository](https://github.com/microsoft/LLMLingua) | Official implementation structure, package surface, license visibility, and examples | 2026-08-16 | README context; code not executed |
| R11 | [RULER](https://arxiv.org/abs/2404.06654) | Retained long-context benchmark context | 2026-08-16 | Prior artifact reference; not reopened |
| R12 | [Lost in the Middle](https://arxiv.org/abs/2307.03172) | Retained position-sensitivity context | 2026-08-16 | Prior artifact reference; not reopened |
| R13 | [SnapKV](https://arxiv.org/abs/2404.14469) | Retained KV-selection neighbor | 2026-08-16 | Prior artifact reference; not reopened |
| R14 | [LongLLMLingua](https://arxiv.org/abs/2310.06839) and [ACL record](https://aclanthology.org/2024.acl-long.91/) | Long-context compression neighbor and official venue record | 2026-08-16 | Retained from prior context; not reopened |
| R15 | [LLMLingua-2](https://aclanthology.org/2024.findings-acl.57/) | Near-primary follow-up surfaced by official repository context | 2026-08-16 | Locator/context, not newly reviewed |
| R16 | [Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514) | Prior persistent-state threat context | 2026-08-16 | Retained prior context |
| R17 | [Safety Testing LLM Agents at Scale](https://arxiv.org/abs/2607.01793) | Prior executable-verification context | 2026-08-16 | Retained prior context |
| R18 | [ContextNest](https://arxiv.org/abs/2607.02116) | Prior context-governance context | 2026-08-16 | Retained prior context |
| R19 | [A Hippocampus for Linear Attention](https://arxiv.org/abs/2607.02303) | Prior exact-memory context | 2026-08-16 | Retained prior context |
| R20 | [InduceKV](https://arxiv.org/abs/2607.02010) | Prior fixed-footprint adaptation context | 2026-08-16 | Retained prior context |
| R21 | [DRIFTLENS](https://arxiv.org/abs/2607.02374) | Prior memory-drift context | 2026-08-16 | Retained prior context |
| R22 | [Clinical reasoning comparison](https://arxiv.org/abs/2607.02175) | Prior consequence-weighted evaluation context | 2026-08-16 | Retained prior context; not clinical guidance |
| R23 | [Grounded autonomous research](https://arxiv.org/abs/2607.02329) | Prior durable-state and calibration context | 2026-08-16 | Retained prior context |
| R24 | [Limited quantum memory](https://arxiv.org/abs/2607.02444) | Prior formal memory-resource context | 2026-08-16 | Retained prior context |

No external PDF, TeX source, code repository, dataset, model, benchmark payload, dependency, prompt corpus, or execution trace was collected or deposited. The official LLMLingua repository was inspected as a public locator only.

## Appendix

### Selection and Eligibility Record

- `Automation`: Black-Lake Data Processing & Review
- `Run date`: 2026-08-16
- `Run timestamp (UTC)`: 2026-08-15T15:02:57Z
- `Eligibility cutoff (UTC)`: 2026-08-14T15:02:57Z
- `Canonical candidate count`: 112
- `Excluded within the 24-hour window`: 1
- `Excluded DEP`: `DEP-20260728-Tech Intel 1305`
- `Eligible candidate count`: 111
- `Eligibility checks`: 49 source Report-Mark files were inspected for recent run dates; the excluded DEP also had a source report and output log dated within the window. No source `.logs` directory was present at the checked source snapshot.
- `Random method`: OS-cryptographic UInt32 with rejection sampling over the sorted eligible list.
- `DEP draw`: UInt32 `4147003871`; successful zero-based index `26`.
- `Selected DEP`: `DEP-20260706-Tech Intel 1110`.

### Supporting-Thread Draw

- `Candidate pool`: 15 primary research threads retained by Report-Mark 002.
- `Random method`: OS-cryptographic UInt32 with rejection sampling.
- `Supporting-thread draw`: UInt32 `133423819`; successful zero-based index `4`.
- `Selected thread`: LLMLingua, arXiv:2310.05736v2.
- `Accessibility result`: Accessible. Canonical arXiv record and complete HTML paper were inspected; official repository context was inspected without code execution.

### Replication Checklist

- [x] Live source and output repository READMEs and filing rules read before writing.
- [x] Selected DEP and prior iterative lineage pinned to public commits.
- [x] Candidate and eligibility counts recorded with the UTC cutoff.
- [x] Prior source report, Report-Mark, output log, DEP README, and prior manuscript inspected.
- [x] Supporting-thread draw recorded and LLMLingua evidence expanded beyond the abstract.
- [x] New material labeled in `Related Research and Reading` and `Source References`.
- [ ] Download and hash the official implementation in an authorized replication task.
- [ ] Review exact benchmark payloads, data licenses, prompt construction, and dependency lock.
- [ ] Reproduce one LLMLingua table under pinned model, hardware, and service coordinates.
- [ ] Compare compression, replay, and full-context policies with source-span retention metrics.

### Source Inventory

- `Collected source files`: None.
- `Inspected repository files`: Selected source README, daily findings, prior source report, prior Report-Mark 002, prior output log, prior DEP-E README and manuscript, and official LLMLingua repository README/public structure.
- `Inspected external sources`: LLMLingua canonical record, complete v2 HTML paper, and retained related-work locators.
- `Not collected`: PDFs, TeX packages, repositories, datasets, models, benchmark payloads, dependencies, prompts, traces, and private files.

### Public-Safe Provenance Note

Repository artifacts intentionally preserve only public repository-relative paths, GitHub URLs, source identifiers, access dates, and UTC-only operational timestamps. Private filesystem context and exact local execution context are withheld. This sanitation does not remove required evidence, source attribution, related reading, or reference sections.
