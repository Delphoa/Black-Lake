# DEP-E-20260716-Medical Diff VQA

#medical-vqa #chest-xray #multimodal-learning #graph-neural-networks #longitudinal-imaging #visual-grounding #clinical-ai #dataset-review #research-review

Public-safe deposition context: this DEP-E preserves a source-first review of *Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering* (`arXiv:2307.11986v2`; DOI `10.1145/3580305.3599819`). The selected archive unit was repaired to a verified complete PDF/full-paper-HTML state before review. All original source files, metadata HTML, TeX/source material, extracted text, caches, local locations, and exact execution details remain withheld.

## Contents

- `README.md`
  - This DEP inventory, public-safe source policy, synthesis context, and final attribution record.
- `medical_diff_vqa_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence, dataset construction, the expert-knowledge graph method, reported results, limitations, implementation paths, exactly three exercise paths, and three related DEP entries.

No `.source/` directory exists. The PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, and local cache were intentionally kept outside the public repository.

## Summary of Items

### `README.md`

Records the deposit boundary, complete file inventory, source withholding policy, relationship to the operational log and detailed Report-Mark, and annotated public sources.

### `medical_diff_vqa_manuscript.md`

Reviews the Medical-Diff-VQA dataset, its Extract-Check-Fix construction cycle, patient-paired longitudinal question design, anatomical/disease-region features, spatial/semantic/implicit relation graphs, relation-aware attention, and answer generation. It preserves the reported 700,703 QA pairs from 164,324 image pairs, the 1,700-sample human validation, benchmark results, ablation tension, safety constraints, and implementation implications.

## Insights and Relevance

The durable contribution is a structured comparison pipeline for subtle change: align present and reference observations by anatomy, represent explicit spatial and domain-semantic relations alongside an implicit graph, compute a difference representation, and answer a bounded question. The accompanying dataset makes longitudinal change a first-class VQA target rather than forcing it into single-image classification or unconstrained report generation.

The strongest evidence remains source-reported. The dataset's sampled QA validation is useful, but the paper does not establish prospective clinical benefit, patient-level leakage resistance, subgroup fairness, calibration, or causal faithfulness of attention maps. The graph ablation also deserves a careful reading: the full three-graph model leads or ties several BLEU measures, but the implicit-only or semantic-only variants are stronger on some METEOR, ROUGE-L, and CIDEr values. The matching operational note is `.logs/20260716-Arxiv-Medical-Diff-VQA-LOG.md`; the detailed cross-DEP synthesis and code mock-ups are in `.reports/BL-Arxiv-Medical-Diff-VQA-20260716/Report-Mark.md`.

## Attribution Block

- Source URL: https://arxiv.org/abs/2307.11986
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Canonical title, authors, arXiv ID, version history, abstract, subjects, DOI, and public artifact locators.
- Source URL: https://arxiv.org/pdf/2307.11986
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Public equivalent of the complete primary PDF inspected locally; file not redistributed.
- Source URL: https://arxiv.org/html/2307.11986
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Official full-paper HTML used to verify structure, methods, experiments, tables, and limitations; file not redistributed.
- Source URL: https://arxiv.org/e-print/2307.11986
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: TeX/source package used locally to cross-check equations, tables, figures, and appendices; file not redistributed.
- Source URL: https://doi.org/10.1145/3580305.3599819
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Persistent DOI for the KDD 2023 paper.
- Source URL: https://physionet.org/content/medical-diff-vqa/1.0.1/
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Official credentialed dataset record, version, category counts, construction description, data-use boundary, and publication citation.
- Source URL: https://physionet.org/content/mimic-cxr/2.1.0/
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Official source-dataset record and data-use restrictions for MIMIC-CXR.
- Source URL: https://github.com/Holipori/MIMIC-Diff-VQA
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Official dataset-generation repository and regeneration instructions.
- Source URL: https://github.com/Holipori/EKAID
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Official feature-extraction, training, testing, and interface implementation; observed main commit is recorded in the manuscript.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `medical_diff_vqa_manuscript.md`
  - Notes: Live authority for repository layout, source withholding, DEP contents, logs, reports, attribution, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `medical_diff_vqa_manuscript.md`
  - Notes: Live authority for DEP-E container filing and publication-index maintenance.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Live companion-repository authority read before its DEP context was used for deduplication.
- Repository file: `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Related DEP on multimodal fusion, visual relations, modality use, probe leakage, and evidence limits; primary source basis is https://arxiv.org/abs/2005.07310.
- Repository file: `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Related DEP on visual grounding, hallucination, coverage, and multimodal preference evaluation; primary source basis is https://arxiv.org/abs/2505.15963.
- Repository file: `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: `medical_diff_vqa_manuscript.md`
  - Notes: Related DEP on paired visual representations, geometry consistency, and evaluation beyond surface appearance; primary source basis is https://arxiv.org/abs/2606.14162.
