# DEP-E-20260818-AKB-48 Articulation

Tags: `DEP-E`, `arXiv`, `articulated objects`, `knowledge graph`, `RGB-D`, `robot manipulation`, `benchmarking`

This public-safe research deposit reviews *AKB-48: A Real-World Articulated Object Knowledge Base* (`arXiv:2202.08432v1`) and re-conceptualizes its main contribution as a typed interface between articulated perception and manipulation. The selected local source unit passed a complete-paper integrity gate after its missing full-paper HTML was repaired. Original source files and machine context were withheld locally.

## Contents

- `README.md` — deposit map, public context, synthesis, and complete attribution.
- `akb48_articulation_manuscript.md` — schema-complete source-first manuscript with evidence ledger, critique, implementation paths, exercises, and MVP concept.

No `.source/` directory is present. PDF, full-paper HTML, metadata HTML, TeX/source archives, extracted text, caches, and verification records were not copied, staged, uploaded, or attached.

## Summary of Items

The manuscript covers the AKB-48 collection of 2,037 articulated-object models across 48 categories, its Articulation Knowledge Graph (ArtiKG), the FArM acquisition pipeline, and the AKBNet pose-to-reconstruction-to-manipulation benchmark. It separates source-reported findings from reviewer interpretation, records a discrepancy between Table 5 and its surrounding prose, and qualifies the dataset's mixture of directly scanned and model-derived assets.

The deposit also records the uniform random-selection method, cross-repository deduplication, source-integrity repair, and the no-source-upload gate. Three related DEP entries connect AKB-48 to geometric-memory pose estimation, persistent real-world manipulation evaluation, and force-aware contact control.

## Insights and Relevance

AKB-48 is most useful as a representation contract. ArtiKG names the geometry, kinematics, semantics, and physics fields that must cross the perception/control boundary, while AKBNet's ground-truth-versus-predicted comparisons reveal how upstream state error degrades downstream action success.

A credible implementation should add field-level provenance, units, uncertainty, graph conformance, identity-disjoint benchmark manifests, and real-robot trial receipts. The strongest repository-level synthesis is a four-part evaluation stack: MemPose-like geometric priors for articulated state, ArtiKG validation, ManipulationNet-style persistent physical trials, and FAVLA-like feedback for contact-rich execution.

## Attribution Block

- Source URL: https://arxiv.org/abs/2202.08432
  - Applies to: title, arXiv identity, six-author v1 byline, submission date, abstract, and public source locators.
- Source URL: https://arxiv.org/html/2202.08432
  - Applies to: complete-paper methods, dataset description, experiments, tables, discussion, conclusion, and references.
- Source URL: https://arxiv.org/pdf/2202.08432
  - Applies to: complete-paper layout, figures, tables, and page-level cross-checking.
- Source URL: https://arxiv.org/e-print/2202.08432
  - Applies to: TeX/source cross-checking, including exact values in Table 5.
- Source URL: https://doi.org/10.48550/arXiv.2202.08432
  - Applies to: persistent arXiv identity.
- Source URL: https://openaccess.thecvf.com/content/CVPR2022/html/Liu_AKB-48_A_Real-World_Articulated_Object_Knowledge_Base_CVPR_2022_paper.html
  - Applies to: CVPR venue and seven-author published record; conflicting page ranges were not propagated.
- Source URL: https://openaccess.thecvf.com/content/CVPR2022/papers/Liu_AKB-48_A_Real-World_Articulated_Object_Knowledge_Base_CVPR_2022_paper.pdf
  - Applies to: publisher-hosted paper locator and publication cross-check.
- Source URL: https://openaccess.thecvf.com/content/CVPR2022/supplemental/Liu_AKB-48_A_Real-World_CVPR_2022_supplemental.pdf
  - Applies to: official supplemental-material locator; supplemental experiments were not used as primary evidence.
- Source URL: https://doi.org/10.1109/CVPR52688.2022.01439
  - Applies to: persistent CVPR proceedings identity.
- Source URL: https://liuliu66.github.io/AKB-48/
  - Applies to: official project scope and category browsing.
- Source URL: https://liuliu66.github.io/AKB-48/download.html
  - Applies to: official dataset download locator; the external payload was not downloaded or audited.
- Source URL: https://github.com/liuliu66/AKB-48/tree/gh-pages
  - Applies to: observed public project-site repository tree and bounded release-state review.
- Source file: `.lake-data/DEP-A/DEP-A-20260806-MemPose Geometry/2607.04930-whitepaper-review.md`
  - Applies to: category-level pose and geometric-memory relationship.
- Source file: `.lake-data/DEP-A/DEP-A-20260727-ManipulationNet An Intake/whitepaper-intake-review.md`
  - Applies to: persistent real-world robot-skill benchmark relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`
  - Applies to: force-aware contact-control relationship.
- Source-handling note: all original PDF, HTML, metadata, TeX/source, caches, and verification records were withheld locally, and no source files were uploaded.
