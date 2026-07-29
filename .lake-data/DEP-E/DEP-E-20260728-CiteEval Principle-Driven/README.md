# DEP-E-20260728-CiteEval Principle-Driven

#citeeval #principledriven #citation #research-review

Public-safe context: job `BLAD-2200-20260728-EB036F17`, item `BLAD-2200-20260728-EB036F17-P10`, uniformly selected `arXiv:2506.01829`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `citeeval_principle_driven_manuscript.md` - schema-complete review of the paper, its evidence, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper studies citeeval, principle-driven, citation, evaluation. Its abstract frames the contribution as follows: Citation quality is crucial in information-seeking systems, directly influencing trust and the effectiveness of information access. Current evaluation frameworks, both human and automatic, mainly rely on Natural Language Inference (NLI) to assess binary or ternary supportiveness from cited sources, which we argue is a suboptimal proxy for citation evaluation. In this work we introduce CiteEval, a citation evaluation framework driven by principles focusing on fine-grained citation assessment within a broad context, encompassing not only the cited sources but the full retrieval context, user query, and generated text. Guided by the proposed framework, we construct CiteBench, a multi-domain benchmark with high-quality human annotations on citation quality. To enable efficient evaluation, we further develop CiteEval-Auto, a suite of model-based metrics that exhibit strong correlation with human judgments. Experiments across diverse systems demonstrate CiteEval-Auto's superior ability to capture the multifaceted nature of citations compared to existing metrics, offering a principled and scalable approach to evaluate and improve model-generated citations. The full paper was inspected beyond the abstract, including introduction, method, evaluation, limitations/discussion, conclusion, and references. Reported results remain author claims unless independently reproduced.

## Insights and Relevance

The three related DEPs connect the selected work to Evidence-Gated Systems - DEP-E, Reliability Proof Chains - DEP-E, and Agent Evidence Loops - DEP-E. Their concrete shared concepts include citation correctness, source attribution, evidence provenance, verification gates. The combined implementation lesson is to preserve provenance, establish baseline parity, probe failure boundaries, and make downstream use review-gated when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2506.01829 - official metadata and public source locators.
- https://arxiv.org/html/2506.01829 - verified full paper; local copy withheld.
- https://arxiv.org/pdf/2506.01829 - verified PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2506.01829 - durable paper identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260727-Evidence-Gated%20Systems - related DEP: Evidence-Gated Systems - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260727-Evidence-Gated Systems/evidence-gated-systems.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260728-Reliability%20Proof%20Chains - related DEP: Reliability Proof Chains - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260728-Reliability Proof Chains/reliability-proof-chains.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260721-Agent%20Evidence%20Loops - related DEP: Agent Evidence Loops - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260721-Agent Evidence Loops/agent-evidence-loops.md`.
- Source files: PDF, full-paper HTML, metadata HTML, integrity records, and local companions; all withheld locally with zero source-document uploads.
