---
title: "DHR Retrieval - DEP-E"
generated_at: "2026-08-18 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of Dense Hierarchical Retrieval for Open-Domain Question Answering."
source_status: "complete local PDF and full-paper HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-18"
temporal_cutoff: "arXiv v1, Findings of EMNLP 2021, and public repository context inspected through 2026-08-18"
primary_url: "https://arxiv.org/abs/2110.15439"
stable_identifier: "arXiv:2110.15439v1; DOI:10.48550/arXiv.2110.15439; ACL DOI:10.18653/v1/2021.findings-emnlp.19"
confidence_summary: "High for identity, method transcription, and source integrity; medium for reported empirical transfer and reproducibility because experiments were not rerun."
safety_scope: "Offline research evaluation, bounded implementation planning, and nonbinding decision support only."
distribution_notes: "Original PDF, full-paper HTML, metadata, cache, extracted text, receipts, and source package remain local and are not redistributed."
---

# DHR Retrieval - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | 2110.15439v1 | https://arxiv.org/abs/2110.15439 | Metadata and public locators; source file withheld | 2026-08-18 | Inspected |
| S2 | Full paper | Primary artifact | HTML and PDF | 2110.15439v1 | https://arxiv.org/html/2110.15439; https://arxiv.org/pdf/2110.15439 | Full-paper evidence; local copies withheld | 2026-08-18 | Integrity checked and inspected |
| S3 | ACL Anthology record | Publication metadata | HTML | 2021.findings-emnlp.19 | https://aclanthology.org/2021.findings-emnlp.19/ | Publication record and DOI; source file not collected | 2026-08-18 | Inspected |
| S4 | Author implementation repository | Official implementation context | GitHub | yeliu918/DHR, main branch | https://github.com/yeliu918/DHR | README and setup.py inspected; code, data, and checkpoints not executed or redistributed | 2026-08-18 | Inspected |
| S5 | Related DEP: RAG Chunking Study | Related research | Markdown | DEP-A; arXiv:2607.01852v1 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-RAG%20Chunking%20Study/2607.01852-whitepaper-review.md | Derived review only; no source file collected | 2026-08-18 | Inspected |
| S6 | Related DEP: PlanRAG Query Trees | Related research | Markdown | DEP-A; arXiv:2607.00508v2 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-PlanRAG%20Query%20Trees/2607.00508-whitepaper-review.md | Derived review only; no source file collected | 2026-08-18 | Inspected |
| S7 | Related DEP: SchemaFirst Retrieval | Related research | Markdown | DEP-A; arXiv:2606.28387v1 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260725-SchemaFirst%20Retrieval/2606.28387-whitepaper-review.md | Derived review only; no source file collected | 2026-08-18 | Inspected |

The original paper source unit was local-only. The final PDF passed the minimum-size, `%PDF-`, and trailing `%%EOF` checks. The full-paper HTML passed the minimum-size, visible-body, article/main/LaTeXML-marker, heading, and paper-structure checks after one bounded repair. The optional TeX/source package was unavailable. Public artifacts therefore expose stable public URLs and source status, not local filesystem paths.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official arXiv metadata | Title, six authors, submission date, v1, subject, abstract, DOI, and public locators | Identity, scope, and source version | High | Abstract is not sufficient for method or empirical claims |
| E2 | S2 | Primary paper | Introduction, structural document, DHR-D, DHR-P, iterative training, inference, preprocessing, datasets, tables, ablations, timing, reader evaluation, conclusion, and appendices | Method, evidence, limitations, and implementation boundary | High for transcription | Author-reported results were not independently reproduced |
| E3 | S3 | Official venue record | Findings of EMNLP 2021, pages 188–200, publication DOI, abstract, and software locator | Publication identity and bibliographic cross-check | High | Venue metadata does not validate the experiments |
| E4 | S4 | Official author repository | Structural-document and in-section-split description, training commands, data formats, two-stage inference, dependencies, and public corpus pointer | Code availability and reproducibility boundary | Medium | No code, checkpoint, dataset, or GPU run was inspected locally |
| E5 | S5 | Related DEP manuscript | RAG chunking, representation-unit choice, evaluation boundary, and failure-aware deployment observations | Cross-source comparison about segmentation and evidence units | Medium | Derived artifact, not independent validation of DHR |
| E6 | S6 | Related DEP manuscript | Query-tree decomposition, staged retrieval planning, concurrency, cost, and contradiction boundaries | Cross-source comparison about cascades and search-space reduction | Medium | Derived artifact, not independent validation of DHR |
| E7 | S7 | Related DEP manuscript | Typed retrieval objects, embedding/reranking pipeline, lineage, ACL boundaries, and downstream SQL generation | Cross-source comparison about structure, provenance, and access control | Medium | Derived artifact, not independent validation of DHR |

## Executive Summary

Dense Hierarchical Retrieval (DHR) is a two-stage dense retriever for open-domain question answering. It responds to a weakness in Dense Passage Retrieval (DPR): short, fixed passages can omit document context, conflate nearby topics, and make the passage encoder distinguish evidence without enough structural information. DHR represents a document as a title-tree structure, retrieves candidate documents with DHR-D, retrieves passages within those documents with DHR-P, and combines passage and document relevance for final ranking. It also uses section-consistent passage splitting, title-path augmentation, hard negatives, and iterative training.

The primary paper reports experiments on Natural Questions, TriviaQA, WebQuestions, and CuratedTREC using a December 20, 2018 English Wikipedia snapshot. The processed corpus contains 5,380,681 documents and 25,992,490 passages. In the two-iteration setting, the reported NQ passage retrieval is 57.04 top-1 and 85.60 top-20 for DHR versus 52.67 and 84.67 for the paper’s reimplemented DPR* baseline. On CuratedTREC, DHR is reported at 48.42 top-1 and 84.17 top-20 versus 41.35 and 79.68 for DPR*. The paper also reports roughly 2.94×–4.02× lower index-search time than DPR, but the comparison is not a whole-request latency result because embeddings are precomputed and reader cost is separate.

The evidence is strong for what the paper implemented and reported, and medium for general deployment value. The author repository provides implementation context and command-line workflows, but no experiment was rerun here and no claim of current reproducibility is made. The key transferable idea is not simply “use two retrievers”; it is to preserve document-to-section lineage as a calibrated retrieval signal, then evaluate that structure against the cost, freshness, access, and evidence requirements of the target corpus.

## Detailed Summary

### Problem and background

Open-domain QA normally separates retrieval from reading or generation. DPR uses a question encoder and passage encoder to search a large collection of fixed passages. The paper argues that the fixed splitting process can create local or biased context and can cause distracting passages to receive strong dense representations. The motivating failure case is a question whose lexical or semantic cues match a nearby but incorrect section; a document and title hierarchy can help distinguish the relevant context.

### Structural representation

The paper formalizes a Wikipedia-like article as a title tree. The document title is the root, section titles are intermediate nodes, and text under a title is a leaf content node. Each passage retains its document and section path. This structure enables a representation that carries macroscopic document semantics and microscopic passage semantics together.

### DHR-D document-level retrieval

DHR-D is a BERT-based dual encoder. The document encoder consumes a summary made from the document title, abstract, and a linearized table of contents. The table of contents is traversed in preorder and title nodes are separated with a special token or comma. The document encoder and question encoder are trained with contrastive loss. The paper tests abstract negatives and all-text negatives in addition to in-batch negatives.

### DHR-P passage-level retrieval

DHR-P is a second BERT-based dual encoder. Rather than splitting across arbitrary document boundaries, it splits within a section leaf, with a maximum passage length of 100 words in the described preprocessing. Each passage is augmented with the title path from document root to its content leaf. The hard negatives include BM25 and in-batch negatives plus In-Doc negatives from the same document and In-Sec negatives from the same section that do not contain the answer.

### Iteration and inference

The first retriever checkpoint generates semantically related hard negatives for a second training iteration. At inference, DHR-D embeds all documents and searches a FAISS index for top-k documents. DHR-P then searches passages from the retrieved documents. The final score adds the passage score to a weighted document score. The paper reports that a weight near one is robust, while the best development-set weight varies by dataset and iteration.

### Data and experimental protocol

The source uses an English Wikipedia dump from 2018-12-20 and WikiExtractor preprocessing. It removes semi-structured data such as tables, infoboxes, lists, and disambiguation pages. The four QA datasets are NQ, TriviaQA, WebQuestions, and CuratedTREC. Positive document/passage selection differs by dataset: some use human-provided context or title matching, while others use BM25 to find a top passage containing the answer. Questions can be discarded when matching fails or no top-100 BM25 passage contains the answer.

### Reported retrieval results

The paper reports DHR improvements over its DPR* reimplementation across the four benchmark datasets and in both one- and two-iteration settings. The largest highlighted differences are on NQ and CuratedTREC. The NQ two-iteration values are 57.04/85.60/90.64 for top-1/top-20/top-100 passage retrieval, while DPR* is 52.67/84.67/89.95. CuratedTREC two-iteration values are 48.42/84.17/91.34 for DHR and 41.35/79.68/91.21 for DPR*.

### Ablations and efficiency

The ablations indicate separate contributions from table-of-contents context, title-path representation, section-aware negatives, document-aware negatives, and document-score reranking. On NQ, the two-iteration document-level setup with abstract negatives and title context reaches 93.16 top-100 document accuracy in the reported table. The paper’s first-iteration timing table reports DHR-D plus DHR-P index search totals that are about 4.02×, 2.94×, 3.20×, and 3.80× faster than DPR on NQ, TriviaQA, WebQ, and TREC respectively. The timing claim is bounded: embeddings are encoded once and only index-search time is compared.

### End-to-end QA and conclusion

For an extractive BERT reader, the paper reports DHR exact-match scores of 43.6, 57.0, 36.6, and 27.3 on NQ, TriviaQA, WebQuestions, and TREC, versus 42.4, 56.9, 35.5, and 26.0 for DPR*. The direction is positive on all four datasets, but the reader-level gains are smaller than several retrieval-level gains. The paper concludes that hierarchy and hard negatives improve both precision and efficiency under its benchmark and corpus setup.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | DHR combines document-level and passage-level dense retrieval with document-score calibration. | Author claim | E2; Sections 3.2–3.5 and Eq. 3 | Directly supported by the described architecture and inference procedure. | High |
| C2 | Section-consistent splitting and title-path augmentation improve passage representations. | Author claim | E2; Sections 3.1, 3.3, 5.2 and Table 4 | Supported by ablations, but the effects are entangled with other preprocessing choices. | Medium-high |
| C3 | DHR improves passage retrieval over DPR* across the four reported datasets. | Author claim | E2; Table 2 and Section 5.1 | Supported within the paper’s corpus, filtering, baselines, and benchmark protocol; not independently reproduced. | Medium-high |
| C4 | DHR reduces retrieval search time relative to DPR. | Author claim | E2; Section 5.4 and Table 7 | Supported for the reported index-search slice, not for end-to-end serving latency. | Medium |
| C5 | Retrieval improvements transfer to end-to-end extractive QA. | Author claim | E2; Section 5.5 and Table 13 | Direction is supported on four datasets, but the absolute reader gains are modest and source-dependent. | Medium |
| C6 | The method is ready for current production RAG without further adaptation. | Reviewer assessment | E2, E4, E5–E7 | Not established. Modern encoders, corpus drift, access control, tail latency, and evidence governance require new evaluation. | Low |

## Methodology

- `Research objective`: Preserve a source-grounded, reusable review of DHR and translate its document-to-passage mechanism into bounded retrieval and RAG implementation questions.
- `Sources inspected`: Repaired local PDF and full-paper HTML; arXiv metadata; ACL Anthology publication record; author DHR repository README, setup.py, and retrieval scripts; and exactly three related Black-Lake DEP manuscripts.
- `Discovery strategy`: Random local paper selection from `rg --files -g "*.pdf"`, parent-unit normalization, prior-artifact deduplication, local source-integrity validation, public arXiv/venue inspection, repository inspection, and related-DEP comparison.
- `Inclusion criteria`: Complete source pair after repair; primary paper sections covering method, experiments, ablations, timing, end-to-end QA, appendices, and conclusion; official publication and author implementation context; related DEP entries with concrete retrieval or structure overlap.
- `Exclusion criteria`: Abstract-only evidence for technical claims; inaccessible or unverified source documents; unreviewed citations; source packages and large source artifacts for public deposition; and claims of independent reproducibility not established by the run.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, safety and ethics, and replication-oriented review.
- `Evidence handling`: Evidence IDs map claims to inspected sources. Author claims, reviewer interpretations, source metadata, and implementation suggestions are labeled separately. Numerical values are transcribed from identified source tables and bounded by dataset, corpus, and timing context.
- `Uncertainty handling`: Missing source package, no independent rerun, unclear current license surface, old corpus snapshot, dataset-specific positive matching, and index-search-only timing scope are stated as limitations rather than filled by inference.
- `Random selection`: 75,967 PDFs and 75,964 parent units were enumerated; 75,782 units had identifiers; 185 incomplete-identifier units were withheld; 729 prior-identifier matches were excluded; 75,053 units remained; PowerShell `Get-Random` selected zero-based index 74,067 from the sorted pool; duplicate and same-paper checks were zero; no reselection occurred.
- `Source integrity`: The selected unit began partial and was repaired once through the brokered archive collector. The final PDF and full-paper HTML passed the required byte, marker, body, heading, structure-term, and EOF checks. Source files remain local.
- `Cross-checking`: The arXiv record was cross-checked with ACL metadata; method and result claims were checked against full-paper HTML and PDF structure; code availability and workflow were checked against the author repository without execution.
- `Reviewer stance`: Source-first DEP research artifact with skeptical paper review, bounded implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: One arXiv v1 paper, its EMNLP 2021 publication record, author implementation context, and three related Black-Lake DEP artifacts.
- `Temporal boundary`: Public sources inspected through 2026-08-18; primary paper is arXiv v1 from 2021 and uses a 2018-12-20 Wikipedia snapshot.
- `Evidence limits`: No independent training or inference run; no dataset, checkpoint, source package, or large corpus collected; current repository default-branch state not pinned to a commit in this artifact; timing claims are index-search-only.
- `Assumptions`: The local verified PDF and HTML correspond to arXiv:2110.15439v1; the ACL record and arXiv record describe the same work; DHR* is the paper’s reimplemented DPR baseline under its preprocessing.
- `Constraints`: Public artifacts must not expose local paths or upload original source files. Implementation examples are safe, local, synthetic, nonbinding, and do not access private corpora.
- `Out of scope`: Production deployment approval, current benchmark ranking, security certification, license clearance for redistribution, and independent scientific replication.
- `Intended use`: DEP deposition, follow-on research, retrieval architecture comparison, and bounded MVP planning.
- `Audience`: Retrieval researchers, RAG engineers, evidence-governance reviewers, and product/system designers.
- `Reproducibility boundary`: The paper and public repository provide substantial workflow context, but reproduction still requires the exact Wikipedia processing, datasets, checkpoints, dependency versions, hardware, and configuration.
- `Operational boundary`: The artifact discusses retrieval structure and evidence handling conceptually; it does not operationalize access to private or restricted data.
- `Data sensitivity`: Public scholarly sources and public repository metadata; original files withheld locally.

## Observations

- `Observed pattern`: The method’s strongest conceptual move is to keep document lineage active after passage construction. A passage is not treated as an isolated vector; its document and title path remain available for routing and calibration.
- `Observed pattern`: The reported end-to-end reader gains are smaller than the retrieval gains. This implies that better retrieval is necessary but not sufficient for answer quality; reader behavior, evidence selection, and answer extraction remain separate bottlenecks.
- `Technical implication`: DHR reduces the passage search space by first selecting documents, but the optimal top-k document count varies by dataset. A deployment therefore needs calibration and monitoring rather than a universal top-k constant.
- `Technical implication`: Section-aware splitting and title augmentation are data-model choices. They can help when headings encode topical structure, but may fail on flat, noisy, poorly authored, multilingual, or frequently edited documents.
- `Contradiction or tension`: The paper presents efficiency as a major advantage while measuring only index-search time after embedding precomputation. The practical claim is plausible but narrower than end-to-end serving efficiency.
- `Open question`: Whether hard negatives and hierarchical structure remain beneficial when a newer encoder, stronger reranker, hybrid sparse+dense retriever, or long-context reader changes the baseline frontier.
- `Reviewer hypothesis`: DHR’s reusable primitive is lineage-aware score fusion, not a fixed two-stage architecture. A typed retrieval system could apply the same primitive to sections, entities, tables, policies, and evidence spans.

## Considerations

The method adds offline preprocessing, two retriever models, multiple embeddings, index management, and score calibration. A service must budget memory and refresh costs for document and passage indexes, distinguish document-level from passage-level failures, and expose enough telemetry to explain why a passage was selected. The paper’s 2018 Wikipedia snapshot makes freshness a central operational concern: a stale structural index can return obsolete or missing evidence even when the score is high.

Access control and provenance become more important when the corpus is private. The document-level candidate stage must not leak titles or scores for inaccessible documents, and the passage stage must enforce authorization before generating evidence. Any downstream generator should receive stable evidence IDs, source versions, section paths, and coverage/abstention signals rather than untyped text alone.

The author repository points to processed Wikipedia data and an eight-A100 training setup. That is useful reproducibility context but also a deployment constraint. A modern MVP should separate a small CPU or single-GPU smoke test from a full-corpus reproduction, publish achieved resource use, and compare a structure-aware path with a cost-matched simple baseline. RAG deployments should monitor retrieval recall proxies, evidence coverage, stale-index rates, answer quality, and P95/P99 latency jointly.

## Strengths

1. The mechanism is legible: document summary, title tree, section-consistent passages, hard negatives, cascade, and score fusion are separately named and ablated.
2. The evaluation spans four open-domain QA datasets and reports both retrieval metrics and end-to-end reader metrics.
3. The paper reports a large processed corpus and provides concrete training/inference details, while the author repository exposes data formats and command-line workflow context.
4. The timing analysis connects hierarchy to search-space reduction rather than claiming an unexplained speedup.
5. The case study makes the failure mode intuitive: a passage in a related document section can be semantically close but answer the wrong interpretation.

## Weaknesses

1. The main comparison changes more than one factor: DHR adds hierarchy, a new passage split, title-path input, hard negatives, iteration, and reranking. Ablations help but do not fully isolate each causal contribution.
2. Positive-context construction and question filtering differ by dataset and depend on BM25 matching, Wikipedia version alignment, and answer containment. These choices can affect both difficulty and comparability.
3. The efficiency result excludes embedding generation, index construction, memory movement, reader/generator cost, and tail latency. It is an index-search result, not a complete service-level result.
4. Evidence is bounded to one English Wikipedia snapshot and four benchmarks. It does not establish robustness under corpus drift, domain shift, multilingual documents, access control, or current hybrid retrieval baselines.
5. The public code context does not by itself prove reproducibility. Checkpoints, exact data state, environment, and a verified end-to-end run were not established in this review.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Factorial component ablation | Causal attribution | Separate hierarchy, section split, title path, negatives, iteration, and rerank effects | Clearer mechanism attribution | More runs and larger compute budget | Matched baselines with one-factor and interaction ablations |
| Full-request accounting | Systems evaluation | Index-search time omits encoding, memory, reader, and tail behavior | Deployment-relevant latency and cost | Requires instrumentation and hardware controls | Report P50/P95/P99 by stage and end-to-end |
| Drift and domain transfer suite | Generalization | One 2018 Wikipedia snapshot is narrow | Evidence for current and domain-specific use | Dataset licensing and annotation effort | Test temporal snapshots, technical corpora, multilingual corpora, and long-tail questions |
| Provenance and authorization layer | Safety and governance | Retrieval can expose stale or inaccessible evidence | Safer private-corpus adaptation | Identity and policy integration | Authorized/unauthorized gold sets, leakage tests, stale-index tests, abstention audit |
| Reproducible release bundle | Replication | Code availability is weaker than reproducible results | Faster independent validation | Storage and maintenance cost | Pin commit, data hashes, checkpoints, dependencies, configs, seeds, and expected outputs |

## Potential Implementations

1. **Structure-aware document QA retriever**
   - `User`: Researcher or knowledge-base operator.
   - `Goal`: Retrieve evidence from structured public documents.
   - `Core mechanism`: Precompute document summaries and section-consistent passage vectors; route question retrieval through document then passage stages; fuse scores.
   - `Required inputs`: Public corpus with headings, a question encoder, passage encoder, and versioned index.
   - `Outputs`: Ranked evidence passages with document IDs, section paths, scores, and source versions.
   - `Risk controls`: Public or authorized corpus only, stale-index alarms, no generation when evidence coverage is below threshold, and source IDs preserved.
   - `Evaluation`: Top-k retrieval, answer exact match/F1, evidence coverage, stage latency, and tail latency against DPR/BM25/hybrid baselines.

2. **Structure-aware RAG ingestion service**
   - `User`: Engineer maintaining a document ingestion pipeline.
   - `Goal`: Preserve hierarchy and provenance when converting documents to retrieval units.
   - `Core mechanism`: Parse heading trees, create a structural summary, split only within compatible leaves, attach title paths, and emit lineage records.
   - `Required inputs`: Versioned documents, parser rules, tokenizer limits, and a schema for parent-child IDs.
   - `Outputs`: Passage records with stable lineage, index-ready embeddings, and parse warnings.
   - `Risk controls`: Quarantine malformed documents, do not merge across access boundaries, preserve old index versions, and support rollback.
   - `Evaluation`: Chunk integrity, retrieval recall, lineage completeness, re-ingestion determinism, and corpus-drift tests.

3. **Evidence-governed retrieval controller**
   - `User`: Platform or governance reviewer.
   - `Goal`: Decide whether retrieved evidence is strong and current enough for downstream use.
   - `Core mechanism`: Combine document/passage scores with coverage, freshness, authorization, and provenance checks; abstain or route to a conservative baseline on failure.
   - `Required inputs`: Ranked candidates, source versions, access decisions, timestamps, and calibrated thresholds.
   - `Outputs`: Allow, abstain, or retry decision with reason codes and evidence ledger.
   - `Risk controls`: Fail closed on authorization uncertainty, no raw sensitive-text logging, immutable audit records, and human review for policy exceptions.
   - `Evaluation`: Calibration, abstention quality, leakage resistance, stale-source detection, and task-level answer quality.

## Three Ways to Exercise This Research

1. **Synthetic title-tree retrieval smoke test**: Objective—measure whether title-path features resolve deliberately constructed near-miss passages. Inputs—synthetic documents with nested headings, 20 safe questions, and gold passage IDs. Method—compare fixed-window DPR-like scoring with document-gated title-tree scoring. Output—top-k hits, score contributions, and lineage records. Success criterion—improved gold-passage recall without losing evidence IDs. Stop condition—stop if the test begins using private or non-synthetic text.
2. **Public-corpus component ablation**: Objective—separate the value of document gating, section-aware splits, title paths, hard negatives, and reranking. Inputs—one licensed public corpus, fixed encoder, and a small question set. Method—run a cost-matched matrix with one factor changed at a time and record full-request latency. Output—component effect table and failure examples. Success criterion—each claimed improvement has an identifiable evidence boundary. Stop condition—stop if baseline parity or data licensing cannot be established.
3. **Authorized evidence-governance evaluation**: Objective—test freshness, authorization, provenance, and abstention around hierarchical retrieval. Inputs—synthetic or authorized documents with version changes and access labels. Method—introduce stale, inaccessible, and contradictory candidates; require the controller to return reason-coded abstentions. Output—audit log, leakage checks, calibration chart, and answer/evidence coverage metrics. Success criterion—no unauthorized evidence is returned and low-coverage cases abstain. Stop condition—stop on any policy bypass or raw sensitive-text logging.

## Example MVP Product

- `Product name`: LineageQA Lite
- `Target user`: Small research or documentation team with a structured public or authorized corpus.
- `Problem`: Fixed-window RAG loses document context and makes retrieved evidence difficult to audit.
- `Core workflow`: Parse headings; create document and passage records; embed summaries and passages; retrieve documents; retrieve passages within them; fuse scores; check freshness/authorization; return evidence or abstain.
- `Data requirements`: Versioned documents with headings, safe question/evidence pairs, corpus metadata, and access labels where required.
- `Architecture`: Local ingestion worker, document and passage embedding jobs, FAISS-compatible indexes, a retrieval API, provenance store, and an optional downstream reader/generator.
- `Success metrics`: Evidence recall@20, answer exact match or task-specific score, evidence coverage, abstention precision, index freshness, P95/P99 latency, and resource cost per query.
- `Risk controls`: Local-only default, no raw sensitive-text telemetry, authorization before candidate exposure, stale-index checks, source-version display, and conservative fallback.
- `Limitations`: MVP is not a proof of DHR’s benchmark results, does not include current large-scale training, and may underperform when documents lack meaningful hierarchy.
- `MVP boundary`: Public or authorized text, one language, one fixed encoder family, small corpus, and offline evaluation; no autonomous policy exceptions.
- `Deployment model`: Local batch ingestion plus a private API or notebook for authorized users.
- `Evaluation plan`: Synthetic smoke tests, public-corpus retrieval evaluation, matched simple baseline, provenance audit, and failure-injection tests.
- `Failure modes`: Flat or malformed headings, stale index, access-label mismatch, duplicate evidence, score miscalibration, and reader hallucination after weak retrieval.
- `Maintenance plan`: Version indexes and parser rules, refresh on corpus changes, monitor drift and tail latency, and revalidate thresholds after encoder or tokenizer updates.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Dense Passage Retrieval for Open-Domain Question Answering | Baseline paper | Direct baseline discussed and reimplemented by DHR | https://arxiv.org/abs/2004.04906 |
| DHR author repository | Official implementation context | Structural preprocessing, data formats, training, embedding, and two-stage retrieval workflow | https://github.com/yeliu918/DHR |
| Findings of ACL: EMNLP 2021 record | Publication record | Venue, pages, DOI, and software locator | https://aclanthology.org/2021.findings-emnlp.19/ |
| RAG Chunking Study | Related DEP | Chunk construction and evidence-unit boundary | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-RAG%20Chunking%20Study/2607.01852-whitepaper-review.md |
| PlanRAG Query Trees | Related DEP | Hierarchical planning, staged retrieval, and cost/latency control | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-PlanRAG%20Query%20Trees/2607.00508-whitepaper-review.md |
| SchemaFirst Retrieval | Related DEP | Typed embeddings, reranking, lineage, authorization, and downstream generation | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260725-SchemaFirst%20Retrieval/2606.28387-whitepaper-review.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2110.15439 | Identity, authors, version, abstract, DOI, and public links | 2026-08-18 | Primary metadata; abstract-only evidence is not used for detailed claims |
| R2 | https://arxiv.org/html/2110.15439 | Method, experiments, tables, appendices, and conclusion | 2026-08-18 | Full-paper HTML inspected locally after verification; local copy withheld |
| R3 | https://arxiv.org/pdf/2110.15439 | PDF cross-check and source integrity | 2026-08-18 | Local copy withheld |
| R4 | https://doi.org/10.48550/arXiv.2110.15439 | Durable arXiv DOI | 2026-08-18 | Public locator |
| R5 | https://aclanthology.org/2021.findings-emnlp.19/ | EMNLP Findings venue, pages, DOI, abstract, and software locator | 2026-08-18 | Official publication record |
| R6 | https://doi.org/10.18653/v1/2021.findings-emnlp.19 | Publication DOI | 2026-08-18 | Official ACL DOI |
| R7 | https://github.com/yeliu918/DHR | Author code context and README workflow | 2026-08-18 | Code and data not executed or redistributed |
| R8 | https://github.com/yeliu918/DHR/blob/main/setup.py | Dependency and license-classifier signals | 2026-08-18 | Root license file was not relied upon or redistributed |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-RAG%20Chunking%20Study/2607.01852-whitepaper-review.md | Related DEP evidence about RAG chunking and evidence-unit boundaries | 2026-08-18 | Derived review, not independent DHR validation |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-PlanRAG%20Query%20Trees/2607.00508-whitepaper-review.md | Related DEP evidence about query trees, staged retrieval, and cost | 2026-08-18 | Derived review, not independent DHR validation |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260725-SchemaFirst%20Retrieval/2606.28387-whitepaper-review.md | Related DEP evidence about typed retrieval, reranking, provenance, and ACLs | 2026-08-18 | Derived review, not independent DHR validation |
| R12 | Local verified PDF; path withheld | Detailed paper cross-check and source-integrity gate | 2026-08-18 | Original source remains local and was not uploaded |
| R13 | Local verified full-paper HTML; path withheld | Detailed paper extraction and source-integrity gate | 2026-08-18 | Original source remains local and was not uploaded |

## Appendix

### Selection and dedup validation

The source archive was enumerated with `rg --files -g "*.pdf"`. Each PDF parent directory was treated as one paper unit. Normalized arXiv IDs were derived from filenames, nearby metadata, and folder names. The final frozen pool contained 75,053 units after withholding 185 identifier-incomplete units and excluding 729 units matching 1,881 prior arXiv identifiers found across local `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data searches. A sorted-pool PowerShell `Get-Random` draw selected zero-based index 74,067. Exact post-draw checks for the arXiv ID, DOI, normalized title, slug, and preceding-24-hour marker found no prior owning artifact; no reselection was needed.

### Source-integrity validation

The selected unit was initially classified as partial because the PDF existed without full-paper HTML. One bounded brokered repair preserved the valid PDF and obtained metadata HTML and official full-paper HTML. The final PDF was 1,164,987 bytes, began with `%PDF-`, and contained `%%EOF`. The final HTML was 213,659 bytes with 57,325 visible body characters, article/main/LaTeXML markers, 62 heading markers, and six structure terms. The source package was unavailable. No original source file, cache, extracted source text, or `.source/` directory is part of this public DEP.

### Replication checklist

- Pin arXiv:2110.15439v1, the ACL publication record, the DHR repository revision, encoder/tokenizer versions, and the 2018-12-20 Wikipedia snapshot.
- Reproduce structural-document parsing, section-consistent 100-word passage construction, positive matching, dataset filtering, and title-path serialization.
- Train DHR-D and DHR-P with the reported token lengths, batch size, epochs, optimizer, and GPU budget; record achieved resource use.
- Compare DPR, DPR*, DHR, and a hybrid sparse+dense baseline under identical corpus, split, and reader conditions.
- Report retrieval, answer, evidence coverage, end-to-end latency, P95/P99 tails, index refresh cost, memory, and failure cases.
- Add temporal, domain, multilingual, authorization, stale-index, and abstention tests before any production claim.

## Attribution Block

- https://arxiv.org/abs/2110.15439 — canonical metadata and public source locators.
- https://arxiv.org/html/2110.15439 — full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2110.15439 — primary PDF evidence; local copy withheld.
- https://doi.org/10.48550/arXiv.2110.15439 — arXiv-issued DOI.
- https://aclanthology.org/2021.findings-emnlp.19/ — official publication record and software locator.
- https://doi.org/10.18653/v1/2021.findings-emnlp.19 — publication DOI.
- https://github.com/yeliu918/DHR — official author implementation context; not executed or redistributed.
- Related DEP sources: R9, R10, and R11 above; these are public derived reviews, not original source deposits.
- Source files: verified PDF, full-paper HTML, metadata HTML, provenance, verification, receipts, and optional-source failure evidence remain local and were not uploaded or attached to Slack.
