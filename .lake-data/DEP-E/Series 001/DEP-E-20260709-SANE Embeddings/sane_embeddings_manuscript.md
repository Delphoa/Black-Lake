---
title: "SANE Embeddings - DEP-E"
generated_at: "2026-07-09 (public-safe date; exact local execution timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "SANE proposes a locality-based attributed-network embedding method that aligns topology and attribute neighborhoods."
source_status: "URLs only with local archive metadata observed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-09"
temporal_cutoff: "Sources inspected through 2026-07-09."
primary_url: "https://arxiv.org/abs/1804.07152"
stable_identifier: "arXiv:1804.07152v2"
confidence_summary: "Medium-high for paper metadata, method, reported metrics, and future work from arXiv metadata and source TeX; lower for reproducibility because experiments and code were not rerun."
safety_scope: "research review, implementation planning, non-sensitive graph and retrieval systems"
distribution_notes: "No source PDF, TeX package, or local archive file is redistributed; local paths are withheld."
---

# SANE Embeddings - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract page | Primary paper metadata | HTML | arXiv:1804.07152 | https://arxiv.org/abs/1804.07152 | Public arXiv metadata and abstract page; license not separately reviewed. | 2026-07-09 | Inspected. |
| S2 | arXiv versioned abstract page | Primary paper metadata | HTML | arXiv:1804.07152v2 | https://arxiv.org/abs/1804.07152v2 | Public arXiv metadata page. | 2026-07-09 | Inspected. |
| S3 | arXiv API query | Canonical metadata | Atom XML | arXiv:1804.07152v2 | https://export.arxiv.org/api/query?id_list=1804.07152 | Used for title, authors, dates, categories, and version metadata. | 2026-07-09 | Inspected. |
| S4 | arXiv source package | Primary paper full source | TeX/source package | arXiv:1804.07152v2 | https://arxiv.org/e-print/1804.07152 | Source package inspected temporarily; not redistributed. | 2026-07-09 | Inspected. |
| S5 | SANE DOI | Persistent identifier | DOI page | 10.48550/arXiv.1804.07152 | https://doi.org/10.48550/arXiv.1804.07152 | arXiv DOI. | 2026-07-09 | Referenced. |
| S6 | Local arXiv archive metadata | Selection provenance | Local readme/PDF presence | arXiv:1804.07152 | Local path withheld | Local archive metadata confirmed paper URL and PDF presence; not redistributed. | 2026-07-09 | Observed. |
| S7 | Black-Lake README | Repository standard | Markdown | main branch checkout | Black-Lake/README.md | Repository rules for DEP classes, README, logs, reports, attribution, and commit messages. | 2026-07-09 | Inspected. |
| S8 | Black-Lake-Data README | Related repository standard | Markdown | main branch checkout | Black-Lake-Data/README.md | Related repository rules for DEP layout and attribution. | 2026-07-09 | Inspected. |
| S9 | Graph topology inference DEP | Related DEP entry | Markdown | DEP-20260630-Tech Intel 0104 | Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md | Related graph-learning source thread. | 2026-07-09 | Inspected. |
| S10 | Structured-vector-graph memory DEP | Related DEP entry | Markdown | DEP-20260708-Tech Intel 1104 | Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 1104/daily_research_findings_2026-07-08_1104.md | Related memory, ability-graph, and graph/vector source thread. | 2026-07-09 | Inspected. |
| S11 | Study fork topics DEP | Related DEP entry | Markdown | DEP-20260629-Study Fork Topics | Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/study_fork_related_topics_2026-06-29_2346.md | Related embedding, vector database, GraphRAG, and provenance-preserving ingestion topic map. | 2026-07-09 | Inspected. |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S3 | Primary arXiv metadata | Title, authors, arXiv ID/version, categories, publication date, update date, and abstract. | Source identity and high-level problem/method summary. | High | Abstract alone is insufficient for detailed empirical claims. |
| E2 | S4 | Primary arXiv source TeX | Abstract, SANE objective, algorithm sketch, dataset table, result table, scalability section, conclusion and future work. | Method, reported metrics, scalability, and limitations. | High | TeX source was inspected; figures were not visually audited beyond source references. |
| E3 | S6 | Local archive metadata | Randomly selected archive unit had a readme and PDF for arXiv:1804.07152. | Selection provenance. | Medium | Local paths are withheld; PDF text extraction tooling was unavailable. |
| E4 | S7 | Repository standard | DEP-E class, required DEP README, attribution block, logs/reports roles, commit message standard. | DEP format and placement. | High | Repository policy, not research evidence. |
| E5 | S8 | Related repository standard | Black-Lake-Data DEP layout and attribution handling. | Related DEP source use. | High | Repository policy, not research evidence. |
| E6 | S9 | Related DEP entry | Directed graph topology inference finding and source reference. | Related-entry bridge for graph structure inference. | Medium | Full related paper was not re-reviewed in this pass. |
| E7 | S10 | Related DEP entry | MRMS structured-vector-graph memory and EvoAgentBench Ability Graphs findings. | Related-entry bridge for graph/vector memory and procedure graphs. | Medium | Full related papers were not re-reviewed in this pass. |
| E8 | S11 | Related DEP entry | Topic map for embeddings, vector stores, GraphRAG, dependency graph retrieval, and provenance-preserving ingestion. | Related-entry bridge for Black-Lake graph-native ingestion. | Medium | Source repositories were not re-cloned or re-reviewed in this pass. |

## Executive Summary

SANE is a locality-based attributed-network embedding method. It tries to learn node vectors that reflect both graph topology and node attributes without relying on global matrix factorization. The paper's central mechanism is to align local linear relationships from attribute-space K-nearest neighbors with node2vec-style topology embeddings, then optimize the combined objective with stochastic updates and negative sampling.

The paper reports node classification results on Cora, BlogCatalog, Flickr, and PPI. In the result table, SANE reports F1 scores of 0.83, 0.91, 0.72, and 0.77, respectively, with gains over node2vec of 5.1%, 40%, 71.4%, and 11.6%. The authors also report linear scalability on synthetic Barabasi-Albert graphs up to 100,000 nodes, with about 20 minutes total processing and about 10 seconds for the C++ joint-representation step.

Reviewer confidence is medium-high for the metadata, method, and reported metrics because the arXiv API, abstract, and source TeX were inspected directly. Confidence is lower for reproducibility because the experiments were not rerun, public implementation availability was not verified beyond source statements, and source figures were not independently audited. For Black-Lake, SANE is useful as a conceptual bridge from source archives to graph-native knowledge infrastructure: sources can be nodes, attribution fields can be attributes, repository references can be edges, and locality can control scalable relation discovery.

## Detailed Summary

### Problem

Attributed networks are graphs whose nodes carry feature vectors, tags, text-derived attributes, biological signatures, or other descriptors. The paper argues that topology-only embeddings can miss useful node-level information, while attribute-only embeddings can ignore graph relationships. Existing attributed-network embedding approaches cited by the paper often depend on global matrix factorization or eigen-decomposition, which creates scale problems for large graphs and evolving networks.

### Method

SANE combines two neighborhood views. For topology, it uses a node2vec-style process: random-walk-derived node contexts are optimized with a word2vec-like objective. For attributes, it uses locally linear embedding: each node is reconstructed from its K-nearest neighbors in attribute space, producing local reconstruction weights. SANE then enforces alignment so the topology embedding of a node remains consistent with the weighted combination of its attribute-space neighbors.

The paper's algorithm sketch has three steps: build a topology corpus from the node2vec procedure, build attribute neighbors and weights from the LLE procedure, and optimize the joint embedding objective. The authors state that the method avoids eigen-decomposition and instead uses stochastic gradient updates, accepting local optima in exchange for scalability.

### Experiments

The paper evaluates label classification on nodes. It uses BlogCatalog, Flickr, Cora, and PPI. The dataset table reports 2,708 nodes for Cora, 5,196 for BlogCatalog, 7,575 for Flickr, and 56,944 for PPI. The evaluation uses 5-fold cross-validation, logistic regression from scikit-learn, 80% training labels in each fold, and a joint embedding dimension of 96.

The baselines are LLE, node2vec, LANE, AANE, and MultiView. LANE receives label information as an extra training input, which makes it a stronger but less directly comparable baseline. The paper does not report matrix-factorization baselines on PPI because the authors consider them impractical at that scale.

### Results

SANE reports F1 scores of 0.83 on Cora, 0.91 on BlogCatalog, 0.72 on Flickr, and 0.77 on PPI. It is competitive with the strongest baselines on Cora and BlogCatalog, wins among reported methods on PPI, and trails MultiView and LANE on Flickr. The table reports gains over node2vec of 5.1%, 40%, 71.4%, and 11.6% for Cora, BlogCatalog, Flickr, and PPI.

The parameter sensitivity section states that embedding dimension, lambda, and K affect performance differently across datasets. For Flickr, the paper says stronger tuning can improve SANE from the table result of 0.72 to about 0.79 under a different setting, which supports the authors' point that the method depends on base embedding and hyperparameter quality.

### Scalability

The scalability experiment uses synthetic Barabasi-Albert graphs from 100 to 100,000 nodes with a fixed attachment edge count. The paper reports that SANE scales roughly linearly with node count. At 100,000 nodes, it reports about 20 minutes total runtime and about 10 seconds for the C++ joint-representation step. The authors note that preprocessing dominates and could improve with implementation optimization.

### Limitations and Future Work

The paper explicitly identifies future work on incremental updates for evolving attributed networks, selective alignment where topology and attribute spaces are truly aligned, and incorporating label information. Reviewer-added limitations are that the experiments were not reproduced, code availability was not verified from a public repository, and the method's baselines reflect the 2018 graph-embedding landscape rather than current graph neural network practice.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | SANE learns joint node representations by aligning local attribute-space relationships with topology embeddings. | Author claim supported by method section | E2 | Directly supported by the SANE method and algorithm sections in the TeX source. | High |
| C2 | SANE reports F1 scores of 0.83, 0.91, 0.72, and 0.77 on Cora, BlogCatalog, Flickr, and PPI. | Author empirical result | E2 | Directly supported by the result table; not independently reproduced. | High for reporting, low for reproducibility |
| C3 | SANE reports gains over node2vec of 5.1%, 40%, 71.4%, and 11.6% across the four datasets. | Author empirical result | E2 | Directly supported by the result table; interpretation depends on baseline settings. | High for reporting, low for reproducibility |
| C4 | The paper's scalability argument depends on avoiding global matrix factorization and using locality plus stochastic optimization. | Author claim with reviewer interpretation | E2 | Supported by the method and scalability discussion. | Medium-high |
| C5 | SANE is relevant to Black-Lake source-thread graphs because it joins topology, attributes, and scalable local relation preservation. | Reviewer interpretation | E2, E6-E8 | Conceptual bridge grounded in inspected paper mechanisms and related DEP entries. | Medium |
| C6 | The selected paper was eligible for this run because no prior Black Lake Arxiv DEP artifact was found for arXiv:1804.07152. | Process claim | E3-E5 | Supported by repository and memory marker scan; exact local paths withheld. | High |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv paper, review it source-first, synthesize it with three related DEP entries, and deposit a `.logs` note, `.reports` Report-Mark, and DEP-E manuscript in Black-Lake.
- `Sources inspected`: Local archive metadata for the selected paper, arXiv abstract page, arXiv versioned metadata, arXiv API metadata, arXiv source package TeX, Black-Lake README, Black-Lake-Data README, and three related Black-Lake-Data DEP entries.
- `Discovery strategy`: Enumerated local archive PDFs with `rg --files -g "*.pdf"` and selected uniformly by random index. Public arXiv metadata and source package were then inspected. Related DEP entries were selected by repository search for graph, embedding, vector, locality, retrieval, and knowledge-graph overlap.
- `Inclusion criteria`: Sources were included when they identified the selected paper, supported method/result/limitation notes, defined repository deposition rules, confirmed random selection provenance, or provided concrete conceptual overlap for synthesis.
- `Exclusion criteria`: No source files were redistributed. The local PDF was not text-extracted because available runtime tooling lacked PDF extraction support. Related papers referenced by DEP entries were not fully re-reviewed beyond repository DEP files and source URLs.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, and DEP-ready provenance analysis.
- `Evidence handling`: Author claims and reported metrics are tied to arXiv source TeX or metadata. Reviewer synthesis is labeled as interpretation and connected to related DEP entries.
- `Uncertainty handling`: Reproducibility limits, missing PDF extraction, unverified public code availability, uninspected related full papers, and source-file non-redistribution are stated explicitly.
- `Random selection`: The run used a uniform random index over 64,626 PDF candidates. The selected zero-based index was 24,529. The selected paper unit was arXiv:1804.07152, with adjacent local readme metadata and PDF presence observed. Local archive paths are withheld.
- `Deduplication and eligibility`: The used-paper index scanned `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, repository README, automation memory, and related Black-Lake-Data context for arXiv ID, title, DOI, and slug markers. No duplicate marker was found, no same-paper marker appeared within the public-safe 24-hour cutoff date 2026-07-08, and no reselection was required.

## Scope, Constraints, and Assumptions

- `Scope`: Review SANE as the selected Black Lake Arxiv DEP paper and connect it to three related DEP entries about graph topology inference, structured-vector-graph memory, ability graphs, embeddings, vector stores, GraphRAG, and provenance-preserving ingestion.
- `Temporal boundary`: Sources available and inspected on 2026-07-09.
- `Evidence limits`: arXiv metadata and TeX source were inspected; PDF text extraction was unavailable; experiments were not reproduced; source figures were not visually audited; code and datasets were not obtained.
- `Assumptions`: The arXiv source package corresponds to the reviewed arXiv version. The local archive readme correctly identifies the selected PDF. Related DEP entries accurately preserve their cited source references.
- `Constraints`: Public artifacts must omit local absolute paths, user home names, machine names, local timezone labels, and exact local execution timestamps. No source PDF or TeX package is redistributed.
- `Out of scope`: Reimplementing SANE, running benchmarks, collecting datasets, verifying author-email code availability, or deep-reviewing every related DEP source paper.
- `Intended use`: DEP deposition, future Black-Lake relation-graph design, graph-memory implementation planning, and source-first review continuity.
- `Audience`: Black-Lake reviewers, graph/retrieval engineers, agent-memory developers, and research operators building provenance-preserving source graphs.
- `Reproducibility boundary`: Paper metrics are preserved from inspected source but not independently reproduced.
- `Data sensitivity`: Public paper metadata and repository artifacts; local archive path withheld.

## Observations

- `Observed pattern`: SANE and the related DEP entries all treat representation as more than an isolated dense vector; topology, attributes, provenance, and local neighborhoods matter.
- `Technical implication`: Black-Lake relation discovery should preserve separate channels for source attributes, explicit citation edges, inferred similarity edges, and reviewer-approved relationship edges.
- `Contradiction or tension`: The paper's scalability comes from local alignment, but Black-Lake review quality depends on global provenance rules that prevent unsupported edges from being admitted.
- `Open question`: Can a modern graph-memory system use SANE-like alignment only as a proposal mechanism while requiring evidence-ledger checks for edge admission?
- `Reviewer hypothesis`: The most useful Black-Lake graph index will combine typed source metadata, embedding similarity, explicit repository references, and evidence-gated relation labels.

## Considerations

SANE should not be treated as a current state-of-the-art graph-learning method without comparison to modern graph neural network and graph-transformer baselines. Its value here is primarily conceptual and architectural: it shows how locality can join attributes and topology while avoiding global matrix costs.

For Black-Lake, the main risk is over-trusting inferred similarity. A DEP relation graph should not admit an edge merely because two artifacts are embedding-near. It should require source evidence, shared identifiers, explicit citation, tag overlap, or reviewer rationale. This is especially important when source archives include mixed domains where superficial terms can create false proximity.

Any implementation that uses local archive metadata must preserve the sanitization boundary: local path details can inform private selection and deduplication, but public artifacts should use arXiv IDs, public URLs, repository-relative paths, and source-withheld notes.

## Strengths

- SANE has a clear mechanism: combine topology-derived neighborhoods with attribute-space local linear relationships.
- The method directly targets scalability by avoiding global eigen-decomposition.
- The evaluation spans citation, social media, and protein interaction graphs, giving a broader test surface than a single benchmark.
- The paper reports both classification performance and scalability behavior.
- The future-work section usefully acknowledges evolving networks, misalignment between topology and attributes, and label incorporation as open problems.

## Weaknesses

- The experiments were not reproduced in this run.
- Public code availability was not verified; the paper source notes that datasets and a reference implementation were available by email to first authors.
- The method trails stronger baselines on Flickr in the reported table.
- The approach depends on the quality of the base node2vec and LLE signals; weak base neighborhoods can hurt the joint embedding.
- Modern graph neural network baselines are outside the paper's 2018 comparison set.
- Figure-level details were not visually audited, so this review relies primarily on TeX source text and tables.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add selective alignment gating | Method | The authors identify topology/attribute misalignment as future work. | Prevents forcing unrelated neighborhoods into one embedding. | Requires an alignment confidence model. | Measure downstream F1 and false-neighbor rates under controlled noise. |
| Compare with modern GNN baselines | Evaluation | The baseline set is from the earlier embedding era. | Clarifies current relevance. | Requires datasets, implementations, and tuned baselines. | Reproduce on Cora, BlogCatalog, Flickr, PPI, and one newer attributed graph. |
| Publish reproducible scripts | Reproducibility | Code availability was not verified from a public repo. | Enables independent review and DEP extension. | May require reconstructing old dependencies. | Provide environment files, dataset download scripts, and expected metrics. |
| Add provenance-aware edge labels | Black-Lake implementation | Inferred relation edges need evidence. | Makes source-thread graphs auditable. | Adds schema and review overhead. | Check every graph edge against attribution and evidence-ledger references. |
| Test incremental updates | Dynamic graphs | The paper names evolving attributed networks as future work. | Supports streaming source archives and changing DEP relation graphs. | Requires update algorithms and drift checks. | Compare full recomputation with incremental updates under source additions. |

## Potential Implementations

1. Black-Lake DEP Relation Graph
   - `User`: Black-Lake reviewer or automation maintainer.
   - `Goal`: Discover related DEP entries without relying on keyword search alone.
   - `Core mechanism`: Represent DEP files, papers, source URLs, claims, tags, and evidence IDs as nodes with typed attributes and edges.
   - `Required inputs`: DEP README files, Report-Mark files, manuscripts, source references, tags, dates, arXiv IDs, and reviewer-selected related entries.
   - `Outputs`: Graph-ready Markdown or JSON, candidate related entries, edge evidence ledger, and follow-up review queue.
   - `Risk controls`: Require evidence IDs for admitted edges; keep local archive paths withheld; separate proposed edges from approved edges.
   - `Evaluation`: Compare reviewer usefulness and false-edge rate against keyword-only search.

2. Provenance-Aware Retrieval Index
   - `User`: Research agent building source-first reports.
   - `Goal`: Retrieve sources that are graph-near and attribute-near while preserving citation boundaries.
   - `Core mechanism`: Combine embeddings, tags, source identifiers, citation links, and local neighborhood features into a retrieval layer.
   - `Required inputs`: Public URLs, source IDs, extracted fields, chunk metadata, graph edges, and source status.
   - `Outputs`: Ranked sources with relationship rationale and provenance.
   - `Risk controls`: Do not return local paths; surface source confidence and missing evidence; avoid using inferred edges as citations.
   - `Evaluation`: Citation accuracy, duplicate suppression, related-entry precision, and reviewer correction rate.

3. Attribute-Topology Alignment Auditor
   - `User`: Engineer maintaining graph-based source infrastructure.
   - `Goal`: Detect when attribute similarity and graph topology disagree.
   - `Core mechanism`: Compare nearest neighbors under tag/metadata similarity, embedding similarity, citation topology, and reviewer-approved edges.
   - `Required inputs`: Node attributes, embedding vectors, edge list, relation labels, and evidence confidence.
   - `Outputs`: Misalignment report, suspicious edges, and candidates for manual review.
   - `Risk controls`: Treat outputs as review prompts, not automatic corrections.
   - `Evaluation`: Sample manual review of accepted, rejected, and ambiguous edge cases.

## Three Ways to Exercise This Research

1. `Toy attributed graph`: Objective: build a small public or synthetic graph with node attributes and compare topology-only, attribute-only, and simple joint embeddings. Inputs: synthetic nodes, tags, and edges. Method: compute nearest neighbors under each view and inspect disagreements. Output: a relation table. Success criterion: reviewer can identify where attributes improve or hurt topology. Safety boundary: use synthetic or public data only.
2. `DEP relation prototype`: Objective: convert a handful of DEP entries into nodes, attributes, and source-reference edges. Inputs: repository-relative DEP files and public URLs. Method: extract tags, arXiv IDs, source URLs, and related-entry rationales. Output: graph-ready JSON with evidence IDs. Success criterion: every edge has a source reference. Safety boundary: no local archive paths or private notes.
3. `Alignment audit`: Objective: test whether embedding-near DEP entries are also provenance-near. Inputs: public-safe metadata, tags, and known related entries. Method: compare embedding or keyword similarity with citation overlap and reviewer-selected relationships. Output: accepted, rejected, and review-needed edge list. Success criterion: unsupported edges are flagged before publication. Safety boundary: inferred relationships are not treated as citations.

## Example MVP Product

- `Product name`: DEP Graph Weaver
- `Target user`: Black-Lake reviewers and research automation maintainers.
- `Problem`: Related DEP discovery is currently manual and keyword-heavy, while future source graphs need typed, evidence-backed relationships.
- `Core workflow`: Ingest DEP README and manuscript files, extract source references and tags, build nodes and explicit citation edges, propose locality-based related edges, require evidence-gated admission, and export a reviewer-facing graph index.
- `Data requirements`: Repository-relative DEP files, source URLs, arXiv IDs, tags, evidence ledger IDs, public dates, and reviewer decisions.
- `Architecture`: Markdown parser, source-reference normalizer, graph store, embedding/vector adapter, relation proposer, evidence gate, sanitization scanner, and Markdown/JSON exporter.
- `Success metrics`: Related-entry precision, edge evidence coverage, duplicate-paper detection rate, reviewer correction rate, and zero local-context leaks.
- `Risk controls`: Public-safe path policy, no local archive path storage in output, source evidence required for admitted edges, manual review for low-confidence relations, and immutable attribution records.
- `Limitations`: MVP relation quality depends on source metadata quality; embeddings can create false proximity; graph updates need deduplication and supersession rules.

Minimal illustrative sketch:

```python
def weave_dep_edges(dep, candidates, evidence):
    proposed = []
    for other in candidates:
        shared_tags = set(dep["tags"]) & set(other["tags"])
        shared_sources = set(dep["sources"]) & set(other["sources"])
        if shared_sources or len(shared_tags) >= 2:
            edge = {
                "from": dep["id"],
                "to": other["id"],
                "relation": "related_to",
                "basis": {
                    "shared_tags": sorted(shared_tags),
                    "shared_sources": sorted(shared_sources),
                },
                "evidence_id": evidence.get((dep["id"], other["id"])),
            }
            proposed.append(edge)
    return [edge for edge in proposed if edge["evidence_id"]]
```

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| SANE | Primary arXiv paper | Reviewed paper; locality-based attributed-network embedding. | https://arxiv.org/abs/1804.07152 |
| Directed Graph Topology Inference via Graph Filter Identification | Related arXiv source via Black-Lake-Data DEP | Graph-structure inference neighbor to SANE's graph representation problem. | https://arxiv.org/abs/2606.27455 |
| MRMS: Multi-Resolution Memory Substrate | Related arXiv source via Black-Lake-Data DEP | Structured-vector-graph memory architecture relevant to graph-native source memory. | https://arxiv.org/abs/2607.04617 |
| EvoAgentBench | Related arXiv source via Black-Lake-Data DEP | Ability Graphs connect procedural reuse to graph representation. | https://arxiv.org/abs/2607.05202 |
| GraphRAG | Related source via study-fork DEP | Retrieval graph method relevant to source-thread graph infrastructure. | https://arxiv.org/abs/2404.16130 |
| Microsoft GraphRAG | Official implementation source via study-fork DEP | Implementation reference for graph-based retrieval. | https://github.com/microsoft/graphrag |
| Study Fork Topics DEP | Related DEP artifact | Embedding, vector DB, GraphRAG, dependency graph retrieval, and provenance-preserving ingestion context. | Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/study_fork_related_topics_2026-06-29_2346.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1804.07152 | SANE metadata, abstract, DOI link, and source links. | 2026-07-09 | Primary arXiv metadata page inspected. |
| R2 | https://arxiv.org/abs/1804.07152v2 | Versioned arXiv metadata. | 2026-07-09 | Versioned page referenced. |
| R3 | https://export.arxiv.org/api/query?id_list=1804.07152 | Canonical arXiv title, authors, dates, categories, version, and summary. | 2026-07-09 | API metadata inspected. |
| R4 | https://arxiv.org/e-print/1804.07152 | TeX source package for method, experiments, results, scalability, and future work. | 2026-07-09 | Source package inspected temporarily; not redistributed. |
| R5 | https://doi.org/10.48550/arXiv.1804.07152 | Persistent DOI reference for SANE. | 2026-07-09 | DOI referenced. |
| R6 | Local arXiv archive readme and PDF presence, path withheld | Selection provenance and local paper-unit confirmation. | 2026-07-09 | Local path withheld under sanitization policy. |
| R7 | Black-Lake/README.md | DEP class, README, logs, reports, attribution, and commit-message standard. | 2026-07-09 | Repository standard inspected after remote fetch. |
| R8 | Black-Lake-Data/README.md | Related repository DEP layout and attribution standard. | 2026-07-09 | Repository standard inspected after remote fetch. |
| R9 | Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/README.md | Related DEP manifest and attribution for graph topology inference. | 2026-07-09 | Related DEP README inspected. |
| R10 | Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md | Related graph topology inference finding. | 2026-07-09 | Related DEP artifact inspected. |
| R11 | Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 1104/README.md | Related DEP manifest and attribution for MRMS and EvoAgentBench. | 2026-07-09 | Related DEP README inspected. |
| R12 | Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 1104/daily_research_findings_2026-07-08_1104.md | Related structured-vector-graph memory and ability graph findings. | 2026-07-09 | Related DEP artifact inspected. |
| R13 | Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/README.md | Related DEP manifest and attribution for study-fork topic map. | 2026-07-09 | Related DEP README inspected. |
| R14 | Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/study_fork_related_topics_2026-06-29_2346.md | Related embedding, vector store, GraphRAG, dependency retrieval, and provenance topics. | 2026-07-09 | Related DEP artifact inspected. |
| R15 | https://arxiv.org/abs/2606.27455 | Primary source for directed graph topology inference referenced by related DEP. | 2026-07-09 | Referenced through related artifact; full paper not re-reviewed here. |
| R16 | https://arxiv.org/abs/2607.04617 | Primary source for MRMS referenced by related DEP. | 2026-07-09 | Referenced through related artifact; full paper not re-reviewed here. |
| R17 | https://arxiv.org/abs/2607.05202 | Primary source for EvoAgentBench referenced by related DEP. | 2026-07-09 | Referenced through related artifact; full paper not re-reviewed here. |
| R18 | https://arxiv.org/abs/2404.16130 | GraphRAG source referenced by study-fork related topics DEP. | 2026-07-09 | Referenced through related artifact; full paper not re-reviewed here. |
| R19 | https://github.com/microsoft/graphrag | Official GraphRAG implementation source referenced by related DEP. | 2026-07-09 | Referenced through related artifact; repository not re-reviewed here. |

## Appendix

### Random Selection and Deduplication Record

- `Selection command class`: `rg --files -g "*.pdf"` over the local arXiv source archive, followed by uniform random index selection.
- `Candidate count`: 64,626 PDFs.
- `Selected index`: 24,529, zero-based.
- `Selected paper`: Scalable attribute-aware network embedding with locality.
- `Selected identifier`: arXiv:1804.07152.
- `Paper unit`: PDF parent directory plus adjacent readme metadata; local path withheld.
- `Duplicate scan`: searched `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, repository README, automation memory, and related Black-Lake-Data context for arXiv ID, DOI, normalized title, and slug markers.
- `Duplicate result`: no prior same-paper artifact found.
- `Reselection count`: 0.
- `24-hour marker cutoff`: public-safe cutoff date 2026-07-08; no same-paper marker found.

### Validation Checklist

- Required manuscript headings are present.
- YAML `title` and H1 are identical and no more than 40 characters.
- `## Evidence Ledger` maps evidence IDs to source references.
- `## Key Claims and Evidence` separates author claims from reviewer interpretation.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- `## Example MVP Product` includes product name, target user, problem, workflow, data requirements, architecture, success metrics, risk controls, and limitations.
- Public artifact text avoids local absolute paths, user home names, machine names, local timezone labels, and exact local execution timestamps.
- No source files are redistributed; source URLs and path-withheld provenance notes are used instead.
