# Report-Mark: SANE Embeddings

Run date: 2026-07-09
Automation: Black Lake Arxiv DEP
Artifact type: arXiv paper review and cross-DEP synthesis mark

## Source Metadata

| Field | Value |
|---|---|
| Title | Scalable attribute-aware network embedding with locality |
| Authors | Weiyi Liu, Zhining Liu, Toyotaro Suzumura, Guangmin Hu |
| Identifier | arXiv:1804.07152v2 |
| DOI | https://doi.org/10.48550/arXiv.1804.07152 |
| arXiv URL | https://arxiv.org/abs/1804.07152 |
| arXiv source package | https://arxiv.org/e-print/1804.07152 |
| Published | 2018-04-17 |
| Updated | 2018-04-30 |
| Subjects | Machine Learning; Artificial Intelligence; Information Retrieval; Machine Learning Statistics |
| Local archive status | Local arXiv archive readme and PDF presence were observed; local path withheld and source files were not redistributed. |

## Concise Research Notes

### Problem

The paper addresses attributed network embedding: learning node representations that preserve both graph topology and node attributes. The authors argue that prior attributed-network methods based on global matrix factorization can be difficult to scale because they require large adjacency or similarity matrices and expensive decomposition.

### Method

SANE, the proposed method, combines node2vec-style topology embedding with locally linear embedding over node attributes. The core idea is to enforce alignment between a node's local linear relationship to its attribute-space K-nearest neighbors and its representation in topology-derived embedding space. The method optimizes this objective with stochastic gradient updates and negative sampling rather than eigen-decomposition.

### Evidence and Results

The paper evaluates node label classification on Cora, BlogCatalog, Flickr, and PPI. Reported F1 scores for SANE are 0.83 on Cora, 0.91 on BlogCatalog, 0.72 on Flickr, and 0.77 on PPI. The authors report gains over node2vec of 5.1%, 40%, 71.4%, and 11.6% on those datasets, respectively. The scalability experiment uses Barabasi-Albert synthetic graphs up to 100,000 nodes and reports approximately 20 minutes for total processing, with the C++ joint-representation step taking about 10 seconds.

### Limitations

The authors note that SANE underperforms MultiView on Flickr and attribute the weakness partly to poor base performance from the node2vec and LLE components. They also leave three future-work areas open: incremental updates for evolving attributed networks, selectively aligning only truly compatible topology and attribute neighborhoods, and incorporating labels into the current algorithm. The review did not reproduce the experiments or verify code availability.

### Implementation Relevance

SANE is relevant to Black-Lake because it treats a knowledge surface as both a graph and an attribute table. That is close to DEP source-thread graphs, agent memory systems that combine structured records with vectors and graph relations, and ingestion systems that need embeddings without losing provenance or local neighborhood structure.

### Reviewer Interpretation

SANE is best read as an early locality-first bridge between graph topology, attributes, and scalable embedding. Its strongest implementation lesson is not that node2vec plus LLE remains a modern baseline, but that graph representations can be made more operational when local topology, local attributes, and scalable update paths are designed together.

## Evidence and Attribution

| Evidence ID | Source | Evidence Used | Supports | Confidence |
|---|---|---|---|---|
| E1 | arXiv API and abstract page | Title, authors, arXiv version, dates, categories, abstract, source links. | Source metadata and abstract-level claims. | High |
| E2 | arXiv source package TeX | Abstract, method, algorithm sketch, dataset table, result table, scalability section, future work. | Research notes on method, experiments, results, and limitations. | High |
| E3 | Local archive readme | Confirms selected archive unit, arXiv URL, and local PDF presence. | Selection provenance. | Medium |
| E4 | Black-Lake README | Repository layout, `.logs`, `.reports`, DEP-E naming, README, attribution, and commit-message rules. | Output placement and artifact hygiene. | High |
| E5 | Black-Lake-Data README | Related repository DEP layout and attribution conventions. | Related DEP context handling. | High |
| E6 | Related DEP entries | Graph topology inference, structured-vector-graph memory, ability graphs, embeddings, vector stores, GraphRAG, and dependency-graph retrieval. | Synthesis Note anchors. | Medium |

## Related DEP Entries

1. `Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md`
   - Reason selected: It includes "Directed Graph Topology Inference via Graph Filter Identification," which overlaps with SANE's concern for recovering or representing graph structure from observed node-level data.
   - Source basis: The DEP README and finding 9 cite https://arxiv.org/abs/2606.27455 as the primary source for directed graph topology inference.

2. `Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 1104/daily_research_findings_2026-07-08_1104.md`
   - Reason selected: It includes MRMS structured-vector-graph memory and EvoAgentBench Ability Graphs, both of which depend on hybrid graph/vector representations and local reuse of learned relationships.
   - Source basis: The DEP README and findings 4 and 6 cite https://arxiv.org/abs/2607.04617 and https://arxiv.org/abs/2607.05202.

3. `Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/study_fork_related_topics_2026-06-29_2346.md`
   - Reason selected: It maps embedding model choice, vector database abstraction, GraphRAG, code-aware dependency graph retrieval, and provenance-preserving source transformation into an ingestion-to-artifact architecture.
   - Source basis: The DEP README and topic map cite Delphoa study forks plus GraphRAG and vector database references, including https://arxiv.org/abs/2404.16130 and https://github.com/microsoft/graphrag.

## Synthesis Note

### Concept Bridge

SANE, directed graph topology inference, structured-vector-graph memory, and source-ingestion topic maps all ask how to represent connected objects when topology alone is insufficient. SANE aligns graph neighborhoods with attribute-space neighborhoods. Directed topology inference estimates graph structure from node measurements. MRMS-style memory combines structured records, vectors, and graph relations with provenance. The study-fork topic map turns documents and repositories into chunks, embeddings, typed metadata, and graph retrieval. Together they describe a Black-Lake path from paper review to graph-native knowledge infrastructure: every source becomes a node with attributes, every relationship is an edge with provenance, and every embedding must preserve enough locality to remain auditable.

### Potential Implementations

1. Build a DEP relation graph where each paper, source URL, artifact, and claim is a node; attributes capture dates, tags, evidence IDs, and source status; SANE-like locality alignment suggests candidate related-reading edges.
2. Add a structured-vector-graph memory layer for Black-Lake artifacts that stores DEP metadata, embedding vectors, citation edges, and supersession relationships while preserving source attribution.
3. Create a graph-topology audit tool that compares inferred relationships from embeddings against explicit repository links, attribution blocks, tags, and reviewer-selected related entries.

### Deeper Relationship Observations

1. Locality is the shared control point: SANE uses local neighborhoods, MRMS uses scoped memory projection, and ingestion pipelines use chunk-local provenance to avoid global recomputation.
2. Attributes determine whether graph edges are meaningful: source dates, tags, licenses, and evidence quality can prevent visually close embeddings from becoming unsupported relationships.
3. Scalability and auditability are in tension: fast embeddings can create useful relation candidates, but Black-Lake needs every graph edge to carry inspectable evidence.

### Conceptual Similarities

1. All three related entries treat representation as a combination of structure and metadata rather than isolated vectors.
2. All three favor reusable relation surfaces: graph topology, ability graphs, memory graphs, retrieval graphs, or dependency graphs.
3. All three expose the same failure mode as SANE: if the base neighborhood signal is weak or misaligned, the joint representation can amplify noise.

### MVP Implementations with Code Mock-Ups

1. **DEP relation graph builder**

```python
def build_dep_graph(entries):
    graph = {"nodes": {}, "edges": []}
    for entry in entries:
        graph["nodes"][entry["id"]] = {
            "kind": "dep",
            "tags": entry["tags"],
            "sources": entry["source_ids"],
        }
        for ref in entry["references"]:
            graph["nodes"].setdefault(ref["url"], {"kind": "source"})
            graph["edges"].append({
                "from": entry["id"],
                "to": ref["url"],
                "relation": "cites",
                "evidence": ref["evidence_id"],
            })
    return graph
```

2. **Locality-aware relation proposer**

```python
def propose_edges(node, candidates, embed_sim, tag_overlap):
    scored = []
    for other in candidates:
        score = 0.65 * embed_sim(node["vector"], other["vector"])
        score += 0.35 * tag_overlap(node["tags"], other["tags"])
        if score >= 0.72:
            scored.append({"target": other["id"], "score": round(score, 3)})
    return sorted(scored, key=lambda x: x["score"], reverse=True)[:5]
```

3. **Evidence-gated graph edge admission**

```python
def admit_edge(candidate, evidence_index):
    evidence = evidence_index.get(candidate["evidence_id"])
    if not evidence:
        return {"status": "reject", "reason": "missing evidence"}
    if evidence["confidence"] not in {"high", "medium"}:
        return {"status": "review", "reason": "weak evidence"}
    return {"status": "admit", "edge": candidate}
```

### Developer Challenges

1. Implement relation proposals so embeddings can suggest edges but cannot admit edges without source evidence.
2. Design a graph schema that records topology, attributes, provenance, and dedup markers without storing local archive paths.
3. Benchmark whether source-thread graphs improve future DEP selection compared with keyword-only related-entry search.

### Author Challenges

1. Revisit SANE with modern attributed-graph benchmarks and graph neural network baselines while preserving the paper's locality-first scalability thesis.
2. Publish a reproducible implementation package with scripts for Cora, BlogCatalog, Flickr, PPI, and one evolving attributed graph.
3. Study selective alignment explicitly: detect when topology neighborhoods and attribute neighborhoods disagree before forcing them into one embedding.

## Validation Notes

- Candidate count was measured from local PDF files in the arXiv archive using `rg --files -g "*.pdf"`.
- Duplicate marker search covered `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, repository README, automation memory, and related Black-Lake-Data context.
- No prior artifact for arXiv:1804.07152 was found; no reselection was required.
- arXiv metadata, arXiv source package TeX, local metadata, target repository README, Black-Lake-Data README, and three related DEP entries were inspected.
- No source files were collected or redistributed in this repository run.
- No local absolute paths, usernames, machine names, local timezone labels, or exact local execution timestamps are intentionally included in this public artifact.

## Attribution Block

- Source URL: https://arxiv.org/abs/1804.07152
  - Applies to: Report-Mark.md
  - Notes: Primary arXiv abstract and metadata page for the selected paper.
- Source URL: https://arxiv.org/abs/1804.07152v2
  - Applies to: Report-Mark.md
  - Notes: Versioned arXiv metadata for the reviewed paper.
- Source URL: https://export.arxiv.org/api/query?id_list=1804.07152
  - Applies to: Report-Mark.md
  - Notes: Canonical arXiv API metadata source for title, authors, version, dates, categories, and summary.
- Source URL: https://arxiv.org/e-print/1804.07152
  - Applies to: Report-Mark.md
  - Notes: Public arXiv source package used for TeX-based method, experiment, result, scalability, and future-work inspection; source files were not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.1804.07152
  - Applies to: Report-Mark.md
  - Notes: arXiv DOI for the selected paper.
- Source file: local arXiv archive readme and PDF presence, path withheld
  - Applies to: Report-Mark.md and `.logs/20260709-Arxiv-SANE-LOG.md`
  - Notes: Local archive metadata confirmed the selected paper URL and PDF presence; local path withheld by public-output sanitization policy.
- Repository file: `Black-Lake/README.md`
  - Applies to: Report-Mark.md, `.logs/20260709-Arxiv-SANE-LOG.md`, and `.lake-data/DEP-E-20260709-SANE Embeddings/README.md`
  - Notes: Repository layout, DEP class, README, attribution, log/report, and commit-message source of truth.
- Repository file: `Black-Lake-Data/README.md`
  - Applies to: Report-Mark.md
  - Notes: Related repository DEP layout and attribution source of truth.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/README.md`
  - Applies to: Report-Mark.md
  - Notes: Related DEP manifest and attribution source for graph topology inference.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md`
  - Applies to: Report-Mark.md
  - Notes: Related finding for directed graph topology inference.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 1104/README.md`
  - Applies to: Report-Mark.md
  - Notes: Related DEP manifest and attribution source for MRMS and EvoAgentBench.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 1104/daily_research_findings_2026-07-08_1104.md`
  - Applies to: Report-Mark.md
  - Notes: Related findings for structured-vector-graph memory and ability graphs.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/README.md`
  - Applies to: Report-Mark.md
  - Notes: Related DEP manifest and attribution source for study-fork topic map.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/study_fork_related_topics_2026-06-29_2346.md`
  - Applies to: Report-Mark.md
  - Notes: Related topic map for embeddings, vector databases, GraphRAG, dependency graph retrieval, and provenance-preserving ingestion.
- Source URL: https://arxiv.org/abs/2606.27455
  - Applies to: Report-Mark.md
  - Notes: Primary source referenced by related graph topology inference DEP entry.
- Source URL: https://arxiv.org/abs/2607.04617
  - Applies to: Report-Mark.md
  - Notes: Primary source referenced by related MRMS memory DEP entry.
- Source URL: https://arxiv.org/abs/2607.05202
  - Applies to: Report-Mark.md
  - Notes: Primary source referenced by related EvoAgentBench DEP entry.
- Source URL: https://arxiv.org/abs/2404.16130
  - Applies to: Report-Mark.md
  - Notes: GraphRAG source referenced by the study-fork related topics DEP entry.
- Source URL: https://github.com/microsoft/graphrag
  - Applies to: Report-Mark.md
  - Notes: Official GraphRAG implementation source referenced by the study-fork related topics DEP entry.
