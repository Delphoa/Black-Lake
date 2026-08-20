# DEP-E-20260724-Shuffled Autoregress

Tags: `DEP-E`, `arXiv`, `motion-interpolation`, `human-motion`, `autoregression`, `dependency-graph`, `attention-mask`, `Transformer`

This DEP-E deposits a public-safe, source-grounded review of *Shuffled Autoregression For Motion Interpolation*. The paper reorganizes sequence generation around a directed acyclic dependency graph and realizes that graph with a Flexible Dependency Attention Mask in a spatial-temporal Transformer. The public package contains derived Markdown only. All locally verified source documents, source packages, renders, extraction caches, and validation records were withheld from publication.

## Contents

- `README.md` — deposit description, inventory, relevance summary, and source attribution.
- `shuffled_autoregression_manuscript.md` — schema-complete research manuscript with evidence ledger, claim review, implementation paths, validation notes, and reproducibility appendix.

No `.source/` directory is present. The local PDF, full-paper HTML, metadata HTML, TeX/source package, rendered pages, extraction caches, provenance records, and verification reports were not copied, staged, or uploaded.

## Summary of Items

The manuscript reviews Shuffled AutoRegression (SAR) as a dependency-order intervention for motion interpolation. SAR replaces fixed left-to-right generation with a topological order over a directed acyclic graph. The paper instantiates that graph as keyframe interpolation, local frame-by-frame generation, and global smoothing, then converts graph adjacency into a Flexible Dependency Attention Mask for a Transformer decoder.

The reported AMASS experiment uses 166,696 windowed sequences and finds that the full model reaches MPJAE `0.0102`, MPJPE `0.0365`, and NPSS `0.089`. The ablations strongly disfavor original chronological autoregression, but the review also records important boundaries: evaluation is limited to one constructed dataset and one short-paper setting, the Neighbor-L2 normalization is ambiguous, visually selected examples are not a user study, extension claims are not tested, and no official code release was established.

## Insights and Relevance

- A generation order is part of the model, not merely a decoding convenience. Changing the dependency topology changes how prediction error can propagate.
- An attention mask can act as an executable graph specification, but training and inference must agree on edge direction, topological order, positional handling, and state updates.
- The three-stage graph balances global anchors, local continuity, and final smoothing; each stage addresses a distinct failure mode and should be measured separately.
- The paper's deterministic ground-truth losses compress a non-deterministic motion problem into one target trajectory. Physical validity, diversity, foot contact, and human preference need separate evaluation.
- A useful MVP is therefore a graph-and-mask verifier with synthetic sequence tests and stage-aware telemetry, not an animation product that assumes the reported results transfer unchanged.

## Attribution Block

| Source | Role in this deposit | Attribution and access note |
|---|---|---|
| [arXiv abstract record: 2306.06367v1](https://arxiv.org/abs/2306.06367v1) | Canonical title, author list, submission date, subject classes, abstract, and public locators | Shuo Huang, Jia Jia, Zongxin Yang, Wei Wang, Haozhe Wu, Yi Yang, and Junliang Xing; accessed 2026-07-24. Metadata only. |
| [Full-paper ar5iv HTML fallback](https://ar5iv.labs.arxiv.org/html/2306.06367) | Searchable full-paper evidence for methods, experiments, table values, conclusions, and references | Same authors; converted full-paper representation inspected after integrity validation. A verified local copy was withheld. |
| [arXiv PDF](https://arxiv.org/pdf/2306.06367) | Primary paper, layout, figures, Table 1, and five-page visual verification | Same authors; arXiv v1. The verified local PDF was withheld. |
| [arXiv DOI](https://doi.org/10.48550/arXiv.2306.06367) | Persistent identifier for the arXiv record | DOI assigned by DataCite/arXiv. |
| [IEEE DOI](https://doi.org/10.1109/ICASSP49357.2023.10095312) | Publisher locator for the ICASSP 2023 paper | IEEE International Conference on Acoustics, Speech and Signal Processing, 2023. |
| [ICASSP 2023 program](https://icassp23-static-program.pages.dev/) | Official conference-program confirmation | Conference schedule lists the paper and complete author set. |
| [Author-group publication page](https://hcsi.cs.tsinghua.edu.cn/) | Author-maintained publication context | Tsinghua HCSI publication page lists the paper under ICASSP 2023. |
| `2306.06367.pdf`, `2306.06367.html`, `2306.06367.abs.html`, and `2306.06367.source.tar` (withheld locally) | Complete primary-paper and provenance evidence | Original paper materials retained only in the private archive; none were uploaded. |
| Local render, extraction, attribution, summary, and verification records (withheld locally) | Visual inspection and integrity evidence | Derived private review materials; none were uploaded. |
| `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Related DEP: autoregressive motion generation and inference-aligned history | Delphoa/Black-Lake repository-relative artifact; inspected 2026-07-24. |
| `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md` | Related DEP: custom visibility masks and runtime dependency semantics | Delphoa/Black-Lake repository-relative artifact; inspected 2026-07-24. |
| `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` | Related DEP: human-motion generation and temporal evaluation | Delphoa/Black-Lake repository-relative artifact; inspected 2026-07-24. |
