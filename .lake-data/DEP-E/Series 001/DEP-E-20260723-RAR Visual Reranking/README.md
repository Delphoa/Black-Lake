# DEP-E-20260723-RAR Visual Reranking

Tags: `DEP-E`, `arXiv`, `multimodal-learning`, `retrieval`, `reranking`, `visual-recognition`, `CLIP`, `MLLM`

This DEP-E deposits a public-safe, source-grounded review of *RAR: Retrieving And Ranking Augmented MLLMs for Visual Recognition*. The review examines RAR's use of frozen CLIP retrieval to form a small label candidate set and a multimodal large language model to rerank those candidates. The public package contains derived Markdown only. All locally verified source documents, extraction caches, and validation records were withheld from publication.

## Contents

- `README.md` — deposit description, inventory, relevance summary, and source attribution.
- `rar_visual_reranking_manuscript.md` — schema-complete research manuscript with evidence ledger, reviewer synthesis, implementation ideas, validation notes, and reproducibility appendix.

No `.source/` directory is present. The local PDF, full-paper HTML, metadata HTML, source archive, extracted text, and verification files were not copied, staged, or uploaded.

## Summary of Items

The manuscript reviews the RAR pipeline across fine-grained recognition, few-shot image classification, and open-vocabulary object detection. It distinguishes source-reported findings from reviewer interpretation, records negative and boundary evidence, and highlights the primary architectural constraint: the reranker cannot recover a correct label that retrieval failed to include in the top-k candidate set.

The paper's strongest practical contribution is a modular pattern: keep a fast embedding model as the recall layer, then spend multimodal reasoning only on a bounded candidate set. Reported improvements are substantial on several aggregate metrics, while per-dataset regressions, approximate-index tradeoffs, proposal-quality dependence, and incomplete cost/privacy analysis constrain the generality of the claims.

## Insights and Relevance

- Candidate recall is a hard ceiling. Retrieval and reranking must be evaluated separately, including oracle top-k recall and conditional reranking accuracy.
- A bounded label set can make a general MLLM useful for recognition without asking it to search the full ontology, but output validation remains necessary.
- The architecture supports independent upgrades to memory, retriever, index, prompt, and reranker; it also creates versioning and provenance obligations at each interface.
- The reported LVIS gains use ground-truth proposals in the main comparison. The authors' Detic ablation shows that realistic proposal quality sharply lowers absolute performance, making detector proposal recall a deployment-critical dependency.
- The most useful MVP is therefore an auditable candidate service with abstention, provenance, per-stage metrics, and offline top-k sweeps—not merely a prompt wrapped around an MLLM.

## Attribution Block

| Source | Role in this deposit | Attribution and access note |
|---|---|---|
| [arXiv abstract record: 2403.13805v2](https://arxiv.org/abs/2403.13805v2) | Canonical title, author list, version history, subject classes, and public paper locator | Ziyu Liu, Zeyi Sun, Yuhang Zang, Wei Li, Pan Zhang, Xiaoyi Dong, Yuanjun Xiong, Dahua Lin, and Jiaqi Wang; accessed 2026-07-23. |
| [arXiv full-paper HTML](https://arxiv.org/html/2403.13805v2) | Searchable full-paper evidence for methods, experiments, tables, limitations, and references | Same authors; arXiv v2; accessed 2026-07-23. A verified local copy was withheld. |
| [arXiv PDF](https://arxiv.org/pdf/2403.13805v2) | Layout, figure, table, and pagination verification | Same authors; arXiv v2; accessed 2026-07-23. The local PDF was withheld. |
| [arXiv DOI](https://doi.org/10.48550/arXiv.2403.13805) | Persistent identifier for the arXiv record | DOI assigned by DataCite/arXiv. |
| [IEEE DOI](https://doi.org/10.1109/TIP.2025.3644175) | Publisher locator for the journal version | IEEE Transactions on Image Processing, volume 35 (2026), pages 388–401. |
| [Official RAR repository](https://github.com/Liuziyu77/RAR) | Implementation surface, usage notes, and repository-stated license context | Repository maintained by the paper authors; inspected 2026-07-23; code was not executed. |
| [Official RAR project page](https://liuziyu77.github.io/RAR/) | Author-maintained project overview | Maintained by the RAR authors; inspected as supporting context. |
| `2403.13805.abs.html` (withheld locally) | Preserved metadata-page evidence | Original source material; retained only in the private archive. |
| `2403.13805.html` (withheld locally) | Verified full-paper HTML | Original source material; retained only in the private archive. |
| `2403.13805.pdf` (withheld locally) | Verified full PDF | Original source material; retained only in the private archive. |
| `2403.13805.source.tar` (withheld locally) | TeX/source inspection | Original source package; retained only in the private archive. |
| `2403.13805.extracted.txt` and local verification records (withheld locally) | Derived review cache, integrity summary, and provenance validation | Generated locally from the above sources; not redistributed. |
| `.lake-data/DEP-A/DEP-A-20260715-MemReranker Reasoning Awa/2605.06132-whitepaper-review.md` | Related DEP: reasoning-aware retrieval reranking | Black Lake repository-relative source; inspected 2026-07-23. |
| `.lake-data/DEP-E/DEP-E-20260719-MIRA One Touch/mira_one_touch_manuscript.md` | Related DEP: multimodal retrieval and constrained generation | Black Lake repository-relative source; inspected 2026-07-23. |
| `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Related DEP: vision-language fusion and probing | Black Lake repository-relative source; inspected 2026-07-23. |
