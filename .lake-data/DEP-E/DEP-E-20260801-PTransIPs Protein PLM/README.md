# DEP-E-20260801-PTransIPs Protein PLM

#protein-language-models #phosphorylation #bioinformatics #deep-learning #transformers #biomedical-evaluation #reproducibility #evidence-ledger

Public-safe context: This DEP-E preserves a source-grounded review of PTransIPs, a protein-language-model-enhanced phosphorylation-site classifier. Complete paper evidence was verified and inspected locally. Only derived Markdown, public URLs, stable identifiers, and repository-relative related-artifact paths are deposited. No PDF, HTML, metadata page, source archive, dataset, model, embedding, cache, extracted source text, receipt, render, or local verification file is included.

## Contents

- `README.md` - DEP inventory, public-safe context, item summaries, synthesis relevance, source-locality statement, and final Attribution Block.
- `ptransips_protein_plm_manuscript.md` - Schema-complete manuscript review with source metadata, evidence ledger, detailed method/results analysis, code-paper conformance findings, implementation paths, three exercises, MVP design, references, and appendices.

No `.source/` directory exists. All original source files and private verification material were withheld locally.

## Summary of Items

### `README.md`

Defines the deposit boundary and makes every public source locator auditable. It records that the DEP contains derived research text only and that the local source-integrity repair did not authorize source publication.

### `ptransips_protein_plm_manuscript.md`

Reviews arXiv `2308.05115v3` and the published IEEE record. It explains the fusion of learned amino-acid/position embeddings, ProtTrans sequence embeddings, EMBER2 structural representations, residual CNN processing, Transformer processing, and the TIM-inspired loss. It preserves sample counts, ablation metrics, prior-method comparisons, cross-bioactivity results, and source-reported limitations.

The manuscript highlights four evidence boundaries:

- the Y independent test contains only 21 positive and 21 negative examples;
- the abstract/conclusion Y AUC (`0.9660`) conflicts with the tables/plot (`0.9683`);
- DE-MHAIPs has higher displayed Y AUC (`0.9778`) even though PTransIPs leads four other Y metrics; and
- the inspected public code differs from the paper in entropy signs, split semantics, apparent Transformer composition, learning rate, and environment completeness.

The code findings are tied to one pinned current repository commit and are not presented as proof of the unpinned experiment-time implementation.

## Insights and Relevance

PTransIPs provides credible evidence that protein-PLM sequence representations can improve a narrow phosphosite benchmark, but the structure channel's displayed incremental value is small and the Y evidence is statistically fragile. The most useful downstream lesson is procedural: a scientific representation claim should pass data-lineage, component-ablation, uncertainty, code-paper conformance, and external-transfer gates before it becomes an implementation or biological claim.

Three inspected Black Lake manuscripts sharpen that lesson. FGBench Chemistry contributes dependency-aware scientific benchmark discipline; ViT Semantic Robustness separates embedding geometry from stable semantic meaning; and MSAIC ECG contributes limited-data biomedical evaluation, calibration, external-validation, and non-deployment boundaries. Together they motivate the manuscript's PhosphoBench Gate MVP: a research-only conformance and evaluation layer, not a diagnostic or wet-lab substitute.

## Attribution Block

- Source URL: https://arxiv.org/abs/2308.05115
  - Applies to: `ptransips_protein_plm_manuscript.md` and `README.md`.
  - Notes: Canonical title, authors, version history, subjects, abstract, DOI links, and source locators. Metadata only; not substituted for full text.
- Source URL: https://arxiv.org/pdf/2308.05115
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Complete PDF used for method, table, figure, equation, discussion, and visual review. Local file withheld.
- Source URL: https://arxiv.org/html/2308.05115
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Official complete full-paper HTML used for searchable review and integrity validation. Local file withheld.
- Source URL: https://arxiv.org/e-print/2308.05115
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Bounded source-package availability check; package unavailable and no source file uploaded.
- Source URL: https://doi.org/10.48550/arXiv.2308.05115
  - Applies to: `ptransips_protein_plm_manuscript.md` and `README.md`.
  - Notes: Persistent arXiv identity.
- Source URL: https://doi.org/10.1109/JBHI.2024.3377362
  - Applies to: `ptransips_protein_plm_manuscript.md` and `README.md`.
  - Notes: Published IEEE paper identity.
- Source URL: https://pubmed.ncbi.nlm.nih.gov/38483806/
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Near-primary journal, issue, page, DOI, and PMID cross-check.
- Source URL: https://github.com/StatXzy7/PTransIPs
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Official repository availability, README workflow, and inventory. Repository not run or copied.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/src/PTransIPs_model.py
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Pinned forward-path, fusion, and Transformer-conformance inspection; not executed.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/src/train.py
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Pinned loss, split, seed, and training-configuration inspection; not executed.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/requirements.txt
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Pinned dependency inventory used for reproducibility assessment.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md` and `ptransips_protein_plm_manuscript.md`.
  - Notes: Live repository authority for DEP class, filing, source locality, attribution, commit, and publication-index rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `README.md` and `ptransips_protein_plm_manuscript.md`.
  - Notes: Live related-repository authority and dedup-context source.
- Source URL: https://doi.org/10.1109/TPAMI.2021.3095381
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: ProtTrans primary reading and sequence-embedding basis.
- Source URL: https://github.com/agemagician/ProtTrans
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Official ProtTrans implementation and model context.
- Source URL: https://doi.org/10.1016/j.str.2022.05.001
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: EMBER2 protein structure representation primary reading.
- Source URL: https://doi.org/10.1093/bib/bbab244
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: DeepIPs direct benchmark predecessor and preprocessing lineage.
- Source URL: https://doi.org/10.1016/j.compbiomed.2023.106935
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: DE-MHAIPs direct comparator and Y-AUC qualification.
- Source URL: https://doi.org/10.1093/bib/bbaf242
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Later protein-PLM/feature-fusion phosphosite research.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/fgbench_chemistry_manuscript.md`
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Inspected related DEP for scientific benchmark construction, dependency, imbalance, and downstream-validity controls.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md`
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Inspected related DEP for representation geometry and semantic robustness boundaries.
- Repository file: `.lake-data/DEP-E/DEP-E-20260715-MSAIC ECG/msaic_ecg_manuscript.md`
  - Applies to: `ptransips_protein_plm_manuscript.md`.
  - Notes: Inspected related DEP for imbalanced biomedical evaluation, uncertainty, calibration, and non-deployment boundaries.
