# DEP-E-20260820-Spectrum Occupancy

#arxiv #spectrum-occupancy #cognitive-radio #wireless-ml #classification #source-first #black-lake-arxiv-dep

Public-safe context: this DEP preserves a source-grounded review of *Analysis of Spectrum Occupancy Using Machine Learning Algorithms* (arXiv:1503.07104). The review was performed only after the selected local source unit passed the complete PDF and full-paper HTML integrity gate. Original source files remain local and were not uploaded.

## Contents

- `README.md` - DEP inventory, public-safe source policy, summary, relevance, and final attribution block.
- `spectrum_occupancy_ml_manuscript.md` - schema-complete manuscript research artifact with source metadata, evidence ledger, claims map, methods/results review, implementation translations, and validation notes.

No `.source/` directory is present. Public arXiv and DOI URLs preserve provenance without redistributing the PDF, full-paper HTML, metadata HTML, acquisition records, caches, extracted source text, or unavailable TeX/source package.

## Summary of Items

The manuscript reviews a four-month, eight-band radiometer study that compares naive Bayes, decision trees, linear SVM, linear regression, hidden Markov models, and SVM tuned with a firefly algorithm. It preserves the reported accuracy, computation-time, threshold, and secondary-user-outage values while separating source claims from reviewer interpretation.

The artifact also records uniform random selection, candidate and unit counts, deduplication and reselection checks, the initial partial source state, one bounded local repair, final source verification, and the public-output allowlist. No independent experiment or live-radio action was performed.

## Insights and Relevance

The durable insight is that spectrum classification is not an accuracy-only problem. Feature geometry, threshold selection, training/test design, outage consequences, runtime, sensing quality, and radio authority all shape whether a model is useful. The related Black Lake entries on structured wireless learning, sensing/resource optimization, and integrated sensing/communication provide concrete conceptual bridges for future benchmark design, while remaining separate from validation of this paper's numerical claims.

## Attribution Block

- Source URL: https://arxiv.org/abs/1503.07104
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Primary metadata, abstract, authors, submission history, category, and arXiv identifier.
- Source URL: https://arxiv.org/html/1503.07104
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Full-paper method, data description, algorithms, results, figures/captions, table values, and references; local copy withheld.
- Source URL: https://arxiv.org/pdf/1503.07104
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Primary PDF inspected for integrity and text cross-check; local copy withheld.
- Source URL: https://doi.org/10.48550/arXiv.1503.07104
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://doi.org/10.1109/TVT.2015.2487047
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Journal publication locator.
- Source URL: https://dblp.org/rec/journals/tvt/AzmatCS16.html
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Bibliographic cross-check for the journal record.
- Repository file: `Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Related wireless machine-learning and structured-state bridge; not independent validation.
- Repository file: `Black-Lake/.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md`
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Related sensing, freshness, and resource tradeoff bridge; not independent validation.
- Repository file: `Black-Lake/.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
  - Applies to: `spectrum_occupancy_ml_manuscript.md`
  - Notes: Related joint sensing/communication and simulation-gated allocation bridge; not independent validation.
- Source-file policy: original source files were withheld locally.
  - Applies to: the entire DEP.
  - Notes: No PDF, HTML, metadata page, source archive, cache, extracted source text, or `.source/` directory was uploaded or committed.
