# DEP-E-20260728-Local Stochastic Bilevel

#local #stochastic #bilevel #research-review

Public-safe context: job `BLAD-2200-20260728-EB036F17`, item `BLAD-2200-20260728-EB036F17-P02`, uniformly selected `arXiv:2205.01608`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `local_stochastic_bilevel_manuscript.md` - schema-complete review of the paper, its evidence, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper studies local, stochastic, bilevel, optimization. Its abstract frames the contribution as follows: Bilevel Optimization has witnessed notable progress recently with new emerging efficient algorithms and has been applied to many machine learning tasks such as data cleaning, few-shot learning, and neural architecture search. However, little attention has been paid to solve the bilevel problems under distributed setting. Federated learning (FL) is an emerging paradigm which solves machine learning tasks over distributed-located data. FL problems are challenging to solve due to the heterogeneity and communication bottleneck. However, it is unclear how these challenges will affect the convergence of Bilevel Optimization algorithms. In this paper, we study Federated Bilevel Optimization problems. Specifically, we first propose the FedBiO, a deterministic gradient-based algorithm and we show it requires $O(\epsilon^{-2})$ number of iterations to reach an $\epsilon$-stationary point. Then we propose FedBiOAcc to accelerate FedBiO with the momentum-based variance-reduction technique under the stochastic scenario. We show FedBiOAcc has complexity of $O(\epsilon^{-1.5})$. Finally, we validate our proposed algorithms via the important Fair Federated Learning task. More specifically, we define a bilevel-based group fair FL objective. Our algorithms show superior performances compared to other baselines in numerical experiments. The full paper was inspected beyond the abstract, including introduction, method, evaluation, limitations/discussion, conclusion, and references. Reported results remain author claims unless independently reproduced.

## Insights and Relevance

The three related DEPs connect the selected work to Provably Faster Algorithms for B - DEP-E, Schwarz Neural Inference - DEP-E, and Dataset Baselines Review - DEP-E. Their concrete shared concepts include algorithms, baselines, bilevel, convergence, due, experiments, local. The combined implementation lesson is to preserve provenance, establish baseline parity, probe failure boundaries, and make downstream use review-gated when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2205.01608 - official metadata and public source locators.
- https://ar5iv.labs.arxiv.org/html/2205.01608 - verified full paper; local copy withheld.
- https://arxiv.org/pdf/2205.01608 - verified PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2205.01608 - durable paper identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260723-Provably%20Faster%20Algorithm - related DEP: Provably Faster Algorithms for B - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260723-Provably Faster Algorithm/provably_faster_algorithm_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260723-Schwarz%20Neural%20Inference - related DEP: Schwarz Neural Inference - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260721-Dataset%20Baselines - related DEP: Dataset Baselines Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260721-Dataset Baselines/dataset_baselines_manuscript.md`.
- Source files: PDF, full-paper HTML, metadata HTML, integrity records, and local companions; all withheld locally with zero source-document uploads.
