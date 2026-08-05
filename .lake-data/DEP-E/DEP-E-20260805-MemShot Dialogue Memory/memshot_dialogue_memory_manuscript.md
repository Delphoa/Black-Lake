---
title: "MemShot Dialogue Memory - DEP-E"
generated_at: "2026-08-05"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of MemShot visual memory construction for long-term dialogue."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-05"
temporal_cutoff: "arXiv v1 and public repository state inspected on 2026-08-05"
primary_url: "https://arxiv.org/abs/2606.28338"
stable_identifier: "arXiv:2606.28338v1; DOI:10.48550/arXiv.2606.28338"
confidence_summary: "Medium-high for paper identity and reported method/results; low for independent reproducibility because no experiments were rerun."
safety_scope: "Public-safe, defensive, evaluation-oriented, source files withheld locally"
distribution_notes: "Only derived Markdown and public-safe provenance are deposited; local source files and caches are not redistributed."
---

# MemShot Dialogue Memory - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Memory Shot for Long-Term Dialogue | Primary paper | PDF and full-paper HTML | arXiv:2606.28338v1; 2026-05-30 | [arXiv record](https://arxiv.org/abs/2606.28338), [HTML](https://arxiv.org/html/2606.28338), [PDF](https://arxiv.org/pdf/2606.28338) | arXiv source; full source files retained privately and not redistributed | 2026-08-05 | Complete local PDF and full-paper HTML verified before review |
| S2 | ArXiv-issued DOI | Stable locator | DOI | 10.48550/arXiv.2606.28338 | [doi.org/10.48550/arXiv.2606.28338](https://doi.org/10.48550/arXiv.2606.28338) | Persistent identifier; not treated as an independent reproduction | 2026-08-05 | Inspected |
| S3 | NEUIR/MemShot | Official implementation | GitHub repository | README SHA `af01f8b20fbc8bddcad34b73725b4989d9424ec4` | [repository](https://github.com/NEUIR/MemShot) | MIT license shown by repository; code was inspected, not executed | 2026-08-05 | README, requirements, rendering, and retrieval launcher inspected |
| S4 | C-DIC Dialogue Memory DEP | Related research | Black Lake DEP-A manuscript | arXiv:2606.12411v1 | [repository artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-C-DIC%20Dialogue%20Memory/2606.12411-whitepaper-review.md) | Derived review; source paper not deposited here | 2026-08-05 | Read for conceptual comparison |
| S5 | MemRouter DEP | Related research | Black Lake DEP-A manuscript | arXiv:2605.00356v1 | [repository artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-MemRouter/2605.00356-whitepaper-review.md) | Derived review; source paper not deposited here | 2026-08-05 | Read for conceptual comparison |
| S6 | Agent Memory Forensics DEP | Safety and governance context | Black Lake DEP-A intake review | arXiv:2606.30566 | [repository artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-Agent%20Memory%20Forensics/agent-memory-forensics-intake-review.md) | Derived defensive review; source files not copied | 2026-08-05 | Read for operational and provenance comparison |

The private source set was complete for the selected paper after repair: a valid PDF and a valid full-paper HTML document were present before synthesis. The abstract page was treated as metadata only. No source package was available, and no local source file, extracted text, cache, or private integrity record is part of this DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, arXiv metadata | Primary paper record | Title, authors, version, date, subject, DOI, abstract, public URLs | Work identity and scope | High | Metadata does not support detailed empirical claims |
| E2 | S1, full-paper HTML | Primary paper | Method equations, rendering design, benchmark setup, tables, ablations, retrieval and saliency analysis, appendix | Technical mechanism and paper-reported results | High | No independent reproduction; HTML conversion has minor encoding noise |
| E3 | S1, PDF | Primary paper | Figures, printed tables, implementation details, metrics, paper header | Cross-check of reported values and layout | High | PDF text extraction has symbol encoding noise |
| E4 | S3, official repository | Official implementation | README setup, benchmark scripts, model dependencies, fixed-height renderer, retrieval launcher | Implementation boundary and reproducibility requirements | Medium-high | Code and checkpoints were not executed; repository scripts use configured paths |
| E5 | Private cache summary | Processing record | `cached` status; pypdf PDF text; html-regex HTML text; no source text; `pdftotext` unavailable | Extraction provenance and review coverage | High | Private processing record is not publicly redistributed |
| E6 | S4, C-DIC DEP | Related review | Revisable latent state, retrieval-aware write-back, closed-loop and storage-growth analysis | Comparison with latent memory and lifecycle state | Medium | Different source and evaluation; not independent validation of MemShot |
| E7 | S5, MemRouter DEP | Related review | Learned admission separated from retrieval and answering; latency and budget analysis | Comparison with write-policy decomposition | Medium | Different source and evaluation; official code was unavailable to that review |
| E8 | S6, Agent Memory Forensics DEP | Defensive related review | Provenance-minimized traces, memory poisoning boundaries, detection limitations | Safety, audit, and governance implications | Medium | Review artifact and not a direct experiment on MemShot |

## Executive Summary

MemShot proposes a lightweight visual memory interface for long-term dialogue. Instead of repeatedly asking a language model to summarize, update, or merge text memories, it splits local contiguous dialogue into shots, preserves session metadata and speaker-aware turn order, and renders each shot as an image for multimodal retrieval and generation. The paper reports competitive results on LoCoMo and LongMemEval and a 70x memory-construction speedup against selected text-memory baselines.

The method is conceptually strong because it preserves evidence structure that text rewriting can erase: who spoke, when a session occurred, where turns are adjacent, and which utterances form a local episode. The evidence is persuasive as an internal paper comparison. It is not yet evidence of production readiness or universal memory superiority. The results depend on Qwen3-VL models, a shared retriever, an LLM judge, rendering settings, and a specialized serving stack. Code is public, but no experiment, checkpoint, dataset, or inference pipeline was run in this review.

Reviewer confidence is medium-high for identity, method reconstruction, and transcription of reported numbers; medium for causal interpretation of individual components; and low for independent reproducibility and deployment claims.

## Detailed Summary

### Problem and context

Long-term dialogue systems must retrieve and use information distributed across sessions. Raw context creates attention and localization problems, while text-centered memory systems can impose iterative extraction, compression, integration, and update costs. The paper's central critique is that these systems may flatten structural cues that help a model interpret evidence.

### Method

Let a dialogue history be split into local chunks. Each chunk is mapped to a hierarchical template with a header and a chat region. The header can include session identifiers and timestamps. The chat region preserves speaker identity, turn order, and local adjacency through a speaker-aware layout. The template is rendered as a visual memory shot. The collection of shots becomes the external memory set used by retrieval and generation.

The reported default rendering uses a 948-pixel width and 768-pixel target height. Complete turn-pairs are packed until the height limit, and the next shot can prepend up to two preceding turn-pairs to preserve continuity. Retrieval uses Qwen3-VL-Embedding-8B with top-10 memory units for generation. Generation is evaluated with Qwen3-VL-Instruct at 2B, 8B, and 32B scales.

### Evaluation

The paper evaluates LoCoMo, which emphasizes multi-session conversational memory, and LongMemEval, which includes user/assistant knowledge, multi-session reasoning, temporal reasoning, and knowledge updates. Baselines include Text RAG, LightMem, MemOS, MemoryOS, EverMemOS, and MemOCR. Accuracy and F1 are judged by GLM-5 using the paper's evaluation prompt.

On LoCoMo, the paper reports MemShot overall accuracy/F1 of 64.48/48.64 with Qwen3-VL-2B, 75.13/56.46 with 8B, and 79.61/58.43 with 32B. The corresponding Text RAG rows report 54.81/42.70, 70.39/53.28, and 77.34/55.69. On LongMemEval, the paper reports MemShot at 66.00/50.91 with Qwen3-VL-8B and 74.80/55.53 with Qwen3-VL-32B, compared with Text RAG at 60.60/46.33 and 72.40/51.89 respectively. The category-level values and the paper's table should be consulted together because the metric mix is not uniform across all baselines. The additional 2B table reports 45.60/38.24 for MemShot.

The ablations support structure as a mechanism. Removing rendering lowers performance even when the textual content is retained. Removing the header reduces the benefit of retrieving more units. A 768-pixel maximum height performs best among the tested 512, 768, 1024, and full-session alternatives under the selected Qwen3-VL-8B setting. Retrieval analysis reports approximately five percentage points of top-10 retrieval improvement and over two percentage points of conditional generation improvement, while saliency and rubric-based judge analyses favor more localized, structured evidence attribution.

### Implementation and reproducibility

The official repository provides rendering, retrieval, inference, and judge scripts. It expects Qwen3-VL generation and embedding checkpoints, vLLM serving, benchmark preparation, and configured file paths. The dependency file pins NumPy, Pillow, FAISS, PyTorch, Transformers, and vLLM versions. The public repository is useful evidence of an implementation path, but its existence does not prove that the paper's exact tables can be reproduced without the precise data, checkpoints, hardware, prompts, seeds, and evaluation outputs.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | MemShot directly renders local dialogue spans into structured visual memory units. | Author claim | E2, E3 | Supported by equations, rendering description, and official renderer inspection. | High |
| C2 | MemShot preserves metadata, speaker identity, turn order, and local adjacency. | Author claim | E2, E4 | Mechanism supports the claim at the representation level; semantic correctness after rendering is not guaranteed. | High |
| C3 | MemShot achieves competitive benchmark performance and up to 70x faster memory construction. | Author claim | E2, E3 | Supported as a paper-reported result under the stated models, baselines, and judge; not independently reproduced or normalized to total serving cost. | Medium-high |
| C4 | Visual structure improves retrieval and evidence utilization. | Author claim plus reviewer interpretation | E2 | Ablations, retrieval analysis, rubric scores, saliency patterns, and case studies are convergent but judge- and setup-dependent. | Medium |
| C5 | The approach is a production-ready replacement for text memory. | Reviewer assessment | E2, E4, E6-E8 | Not established. Storage, privacy, deletion, contradiction, accessibility, and concurrent serving remain open. | Low |
| C6 | The official repository establishes reproducibility. | Reviewer assessment | E4 | Not established. It establishes an implementation lead, not a complete reproduction package. | Low |

## Methodology

- `Research objective`: Preserve a source-grounded review of MemShot's method, evidence, limitations, and implementation relevance for long-term dialogue memory.
- `Sources inspected`: The repaired local PDF and full-paper HTML; local metadata; public arXiv abstract and HTML; the official MemShot README, requirements, renderer, and retrieval launcher; and exactly three related Black Lake DEP manuscripts.
- `Discovery strategy`: Enumerated local PDF files with `rg --files -g "*.pdf"`; collapsed PDF parents into paper units; used a uniform PowerShell `Get-Random` draw; checked local/public dedup surfaces; then inspected primary and official implementation sources.
- `Inclusion criteria`: Full-paper evidence from the complete PDF/HTML unit, stable public identifiers, official implementation materials, and related DEP entries with concrete conceptual overlap.
- `Exclusion criteria`: Abstract-only evidence for method claims; source files, caches, and local archive paths from public outputs; metadata-only author-inventory rows as duplicate artifacts; and unrelated or unverifiable neighboring research.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication-oriented review.
- `Evidence handling`: Claims were assigned evidence IDs and labeled as author claims, reviewer interpretations, or reviewer assessments. Reported metrics remain attributed to the paper.
- `Uncertainty handling`: Missing source packages, unexecuted code, unavailable raw predictions, judge dependence, and unresolved lifecycle behavior are recorded as limitations rather than inferred away.
- `Source integrity gate`: The initial unit was partial because full-paper HTML was absent. One bounded archive repair produced a PDF passing size/header/EOF checks and full-paper HTML passing size/body/marker/heading/structure checks before any review or synthesis.
- `Cache methodology`: A local `missing-only` extraction was run after source repair. The first cache lookup was a miss; the final record was `cached` with pypdf PDF text and html-regex HTML text. `pdftotext` was unavailable, and no source package or source-text output was available. Extraction used no network backfill.
- `Dedup/reselection validation`: The dedup index, Black Lake logs/reports/DEP surfaces, automation memory, and relevant Black-Lake-Data searches were checked by arXiv ID, DOI, normalized title, slug, and artifact markers. No prior Arxiv DEP or same-paper recent marker was found; reselections were zero.

## Scope, Constraints, and Assumptions

- `Scope`: Review of arXiv:2606.28338v1, its reported method and experiments, official implementation inventory, and three related DEP records.
- `Temporal boundary`: Public source and repository state inspected on 2026-08-05; paper version limited to v1.
- `Evidence limits`: No independent model inference, benchmark rerun, metric recomputation, judge call, or visual rendering was performed. No source package, checkpoint manifest, raw prediction file, or environment lock sufficient for exact reproduction was available.
- `Assumptions`: The printed tables and HTML text refer to the same v1 paper; discrepancies caused by HTML/PDF encoding are interpreted using cross-checked headings and table context.
- `Constraints`: Public outputs must not contain local paths, source documents, caches, usernames, machine identifiers, exact local timestamps, or timezone labels. Source redistribution is intentionally withheld.
- `Out of scope`: Clinical, legal, or user-facing deployment claims; universal superiority over all memory systems; security certification; and reproduction of author experiments.
- `Intended use`: DEP deposition, follow-on research planning, safe implementation ideation, and evidence-aware comparison of memory representations.
- `Reproducibility boundary`: A future reviewer can identify public sources and implementation entry points, but cannot reproduce the paper's tables from this DEP alone.
- `Operational boundary`: Examples are local, synthetic, provenance-aware, and evaluation-oriented; they do not process private conversations or bypass user consent.

## Observations

1. `Observed pattern`: The best evidence is not only the headline score. Rendering, header metadata, chunk height, retrieval behavior, and conditional generation analyses collectively support a representation effect, although they do not isolate every pathway.
2. `Technical implication`: A visual memory shot can preserve local conversational structure with less semantic rewriting, but it transfers cost into image generation, storage, multimodal indexing, model serving, and access control.
3. `Contradiction or tension`: The paper presents visual memory as lightweight while its official runtime requires large multimodal checkpoints, vLLM, FAISS, and benchmark-specific conversion scripts. Construction latency and total system cost are different quantities.
4. `Open question`: The representation preserves what was said, not whether it remains correct, authorized, current, or safe to retrieve.
5. `Reviewer hypothesis`: MemShot may be most valuable as a memory interface that exposes provenance and structure to a multimodal model, with write admission, lifecycle governance, and answer calibration supplied by separate modules.

## Considerations

- `Privacy`: Rendered images may make sensitive text easier to retain, copy, or accidentally expose. A production system needs field-level redaction, retention labels, deletion propagation, and access logging.
- `Correctness`: High-fidelity replay can preserve stale facts, contradictory statements, or model-generated errors. Retrieval should surface authority, time, and uncertainty metadata rather than treating visual layout as truth.
- `Accessibility`: Image-only memory can disadvantage text-only interfaces, screen readers, low-vision users, and audit workflows. A synchronized text representation and deterministic provenance map are required.
- `Operations`: Image rendering and multimodal inference introduce GPU, storage, indexing, and concurrency costs. The 70x construction figure does not establish end-to-end throughput or tail latency.
- `Evaluation`: LLM-as-a-judge and saliency analyses need multiple judges, raw outputs, confidence intervals, prompt sensitivity tests, and human or task-grounded checks.
- `Governance`: The related Agent Memory Forensics DEP suggests an evidence-minimization posture: retain enough event and source linkage for audit while limiting raw content exposure.

## Strengths

- The method has a clear representation boundary and a simple pipeline that can be explained and inspected.
- The design preserves structural metadata that text summarization can weaken.
- The paper includes ablations, retrieval analysis, rubric-based reasoning analysis, saliency analysis, and qualitative cases rather than only a single leaderboard.
- The official repository provides a concrete implementation path, benchmark scripts, and dependency inventory.
- The evaluation spans two long-term dialogue benchmarks and multiple multimodal model scales.

## Weaknesses

- Reported results were not independently reproduced, and raw predictions, environment locks, and checkpoint hashes were not available in the inspected sources.
- The judge model and prompt are material parts of the evaluation, but judge sensitivity and uncertainty are not fully exposed.
- Construction-speed comparisons do not fully account for rendering, image storage, indexing, multimodal prefill, or concurrency.
- The paper does not establish deletion, contradiction resolution, source authority, privacy leakage, accessibility, or multilingual robustness.
- The visual format may create new failure modes when text is dense, fonts are unavailable, layouts overflow, or OCR/vision perception is imperfect.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add matched end-to-end cost accounting | Systems | Separate construction speed from total memory lifecycle cost | Better deployment decisions | Requires instrumenting storage, retrieval, prefill, and concurrency | Report p50/p95 latency, bytes, GPU time, and throughput under fixed workloads |
| Add lifecycle and authority controls | Safety and correctness | Structure does not establish truth or authorization | Safer updates, deletion, and conflict handling | More metadata and policy complexity | Synthetic contradictions, deletion audits, privacy probes, and provenance checks |
| Release exact reproduction bundle | Reproducibility | Public code alone does not recover tables | Independent verification | Dataset/checkpoint licenses and storage burden | Versioned manifests, seeds, raw predictions, evaluator, and expected tolerances |
| Expand representation controls | Generalization | Layout and chunking may interact with language, accessibility, and modality | Robustness across users and languages | Rendering and annotation cost | Text/image equivalence tests, multilingual sets, screen-reader review, and OCR stress tests |

## Potential Implementations

1. `Local structured-memory workbench`: ingest synthetic or authorized dialogue, render shots, build a provenance map, run a selected retriever, and expose the exact shots and source turn IDs used for each answer. It should be local-only, versioned, and explicit about deletion and abstention.
2. `Governed multimodal memory gateway`: place retention, access, authority, and contradiction policies between the renderer/index and the answer model. The gateway should deny retrieval when a memory is deleted, blocked, unlabelled, or outside the user's scope.
3. `Representation comparison harness`: run text RAG, visual shots, latent summaries, and learned admission against the same data, retriever, answer model, budget, judge, seeds, and concurrency. Separate retrieval recall, answer correctness, evidence grounding, latency, storage, and privacy metrics.

## Three Ways to Exercise This Research

1. `Synthetic dialogue rendering`: Use a small synthetic conversation with timestamps and two speakers. Render fixed-size shots, verify that each shot maps back to source turn IDs, and test that chunk overlap does not duplicate or omit turns. Success means every source turn is accounted for exactly as specified; stop if the renderer cannot provide a deterministic provenance map.
2. `Text-versus-shot retrieval test`: Create a public-safe toy set with temporal and multi-session questions. Compare text chunks and rendered shots with the same embedding/retrieval budget and a deterministic lexical scorer before adding a model. Success means retrieval differences are measurable and attributable to representation; stop before using personal or unlicensed conversations.
3. `Lifecycle safety simulation`: Add synthetic deletion, correction, contradiction, authority, and retention labels to a memory index. Exercise retrieval and audit rules without a model or external service. Success means deleted or blocked shots never reach the answer input and every returned shot has a source-turn and policy record; stop on any provenance mismatch.

## Example MVP Product

- `Product name`: Traceable Dialogue Memory Lab
- `Target user`: Research engineers evaluating long-context and agent-memory designs.
- `Problem`: Memory benchmarks often mix representation, retrieval, answer generation, and judging, making it difficult to know why a system succeeds or fails.
- `Core workflow`: Import a synthetic or authorized dialogue; produce text, visual-shot, and optional latent representations; retrieve evidence for a query; display the exact source turns, policy labels, and returned units; record metrics and failure categories.
- `Data requirements`: Public or synthetic dialogue, timestamps, speaker labels, question/evidence annotations, representation hashes, and a versioned evaluation configuration. No raw private dialogue is required for the MVP.
- `Architecture`: Local Python orchestrator; deterministic renderer; local metadata/provenance store; pluggable text or image retriever; optional authorized multimodal model adapter; Markdown/JSON audit export.
- `Success metrics`: 100% source-turn accounting; zero retrieval of deleted synthetic units; reproducible top-k results; representation-specific retrieval recall; end-to-end latency and storage measurement; reviewer agreement on failure labels.
- `Risk controls`: Local-only default; synthetic data; explicit consent/license field; deletion and retention states; no raw secret logging; abstention on missing provenance; human review before any public export.
- `Limitations`: It is an evaluation workbench, not a production assistant; it will not establish model truthfulness, clinical safety, or universal memory superiority.
- `MVP boundary`: Exclude private-user deployment, autonomous actions, hidden memory writes, and unreviewed external uploads.
- `Deployment model`: Local CLI or notebook with versioned artifacts.
- `Evaluation plan`: Unit tests for turn accounting and lifecycle policy, deterministic retrieval smoke tests, representation comparison on synthetic dialogues, and manual audit of exported records.
- `Failure modes`: Layout truncation, OCR/vision misread, stale memory, contradictory evidence, policy mismatch, judge bias, and storage/index growth.
- `Maintenance plan`: Pin renderer/model versions, regenerate provenance maps when layouts change, review retention policies, and re-run the synthetic lifecycle suite on every dependency update.

Illustrative safe gate:

```python
def public_export(record):
    required = {"source_url", "representation_hash", "policy_state"}
    if not required.issubset(record):
        return {"status": "abstain", "reason": "incomplete-provenance"}
    if record["policy_state"] != "approved-derived-only":
        return {"status": "abstain", "reason": "policy-blocked"}
    return {"status": "export", "source_url": record["source_url"]}
```

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| C-DIC Dialogue Memory | Related DEP review | Revisable latent memory and retrieval-aware write-back | [Black Lake artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-C-DIC%20Dialogue%20Memory/2606.12411-whitepaper-review.md) |
| MemRouter | Related DEP review | Learned memory admission separated from retrieval and answering | [Black Lake artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-MemRouter/2605.00356-whitepaper-review.md) |
| Agent Memory Forensics | Defensive related DEP | Provenance, memory poisoning, telemetry, and audit boundaries | [Black Lake artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-Agent%20Memory%20Forensics/agent-memory-forensics-intake-review.md) |
| LoCoMo | Benchmark | Long-term conversational memory evaluation used by the paper | [snap-research/locomo](https://github.com/snap-research/locomo) |
| LongMemEval | Benchmark | Long-term interactive memory evaluation used by the paper | [xiaowu0162/LongMemEval](https://github.com/xiaowu0162/LongMemEval) |
| MemOCR | Methodological neighbor | Visual memory built from structured textual memory | [arXiv:2601.21468](https://arxiv.org/abs/2601.21468) |
| Retrieval-Augmented Generation | Foundation method | Retrieval-mediated generation baseline and conceptual origin | [NeurIPS 2020 paper](https://arxiv.org/abs/2005.11401) |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2606.28338 | Identity, authors, version, abstract, dates, and public source links | 2026-08-05 | Primary metadata record |
| R2 | https://arxiv.org/html/2606.28338 | Method, experiments, ablations, analysis, limitations, and conclusion | 2026-08-05 | Full-paper HTML inspected |
| R3 | https://arxiv.org/pdf/2606.28338 | Tables, figures, printed implementation details, and cross-checks | 2026-08-05 | PDF inspected locally; not redistributed |
| R4 | https://doi.org/10.48550/arXiv.2606.28338 | Persistent paper identifier | 2026-08-05 | ArXiv-issued DOI |
| R5 | https://github.com/NEUIR/MemShot | Official implementation inventory, setup, renderer, dependencies, and pipeline | 2026-08-05 | README and selected scripts inspected at pinned file SHAs; no execution |
| R6 | https://github.com/snap-research/locomo | Benchmark identity and public data locator | 2026-08-05 | Related benchmark referenced by the paper |
| R7 | https://github.com/xiaowu0162/LongMemEval | Benchmark identity and public data locator | 2026-08-05 | Related benchmark referenced by the paper |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Black Lake layout, DEP class, source-file policy, and attribution standard | 2026-08-05 | Live README fetched before writing |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related raw-data repository context and source-file policy | 2026-08-05 | Live README fetched before writing |
| R10 | `.lake-data/DEP-A/DEP-A-20260714-C-DIC Dialogue Memory/2606.12411-whitepaper-review.md` | Related research comparison | 2026-08-05 | Repository-relative path only; no local absolute path disclosed |
| R11 | `.lake-data/DEP-A/DEP-A-20260714-MemRouter/2605.00356-whitepaper-review.md` | Related research comparison | 2026-08-05 | Repository-relative path only; no local absolute path disclosed |
| R12 | `.lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics/agent-memory-forensics-intake-review.md` | Defensive governance comparison | 2026-08-05 | Repository-relative path only; no local absolute path disclosed |

## Appendix

### Replication checklist

- Pin arXiv v1 and the official repository commit.
- Obtain benchmark versions and document licenses, splits, and image availability.
- Pin Qwen3-VL generation and embedding checkpoints, vLLM, FAISS, PyTorch, Transformers, Pillow, and NumPy.
- Reproduce the 948-pixel width, 768-pixel target height, turn-pair packing, and two-turn-pair overlap rules.
- Run Text RAG, MemShot, and all selected baselines under the same retriever, generation model, top-k, prompts, judge, and hardware budget.
- Record seeds, raw predictions, retrieval mappings, rendered-image hashes, judge outputs, and metric scripts.
- Add multi-judge, human-audit, privacy, deletion, contradiction, accessibility, multilingual, and concurrency tests.
- Compare construction, storage, indexing, retrieval, multimodal prefill, and end-to-end tail latency separately.

### Public-output and provenance check

This manuscript intentionally contains public URLs and repository-relative paths only. The selected paper's PDF, full-paper HTML, metadata page, source-package status, extraction cache, extracted text, repair receipts, and verification records remain in the private local archive. No `.source/` folder was created, and no source file was staged, committed, uploaded, or attached.
