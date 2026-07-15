# DEP-E-20260715-Joint Sensing MEC

#age-of-information #mobile-edge-computing #iot #sensing #computation-offloading #game-theory #energy-efficiency #status-updates #research-review

This DEP-E entry preserves a source-grounded review of *Joint Optimization of Sensing and Computation for Status Update in Mobile Edge Computing Systems* (arXiv:2210.17025; journal DOI `10.1109/TWC.2023.3261338`). The source archive was repaired and integrity-verified before review. Original PDF, full-paper HTML, metadata HTML, TeX/source, extracted text, and caches remain local and were not uploaded.

## Contents

- `README.md` - DEP inventory, public-safe context, summary, relevance, and attribution.
- `joint_sensing_mec_manuscript.md` - schema-complete manuscript review with evidence ledger, method/results critique, source-integrity record, implementation translations, and replication checklist.

## Summary of Items

The manuscript analyzes a freshness-energy optimization framework for MEC-assisted IoT status updates. It reconstructs the paper's sensing-validity model, AoI derivation, mixed continuous-discrete objective, sampling/sensing/offloading decomposition, potential-game offloading step, MISCO iteration, and source-reported simulations. It distinguishes source claims from reviewer interpretation and explains why the reported `0.7` sensing-success and `1.4 s` sampling thresholds are scenario-specific.

The artifact also records the uniform random draw, dedup/reselection checks, initial partial archive state, bounded repair, complete-source validation, cache miss-to-cached transition, publisher DOI, missing official-code evidence, and exactly three related Black Lake entries. No experiment, algorithm implementation, or hardware result was reproduced.

## Insights and Relevance

The durable insight is that information freshness depends on more than network latency: sensing validity, sampling cadence, processing location, interference, energy, and server admission all shape the useful age of a status update. The related Self-Learned IDC, RRT-CBF Motion, and iKalibr Calibration entries extend that bridge from scheduling into state representation, hard safety gating, timestamp integrity, and staged optimization. Together they motivate public-safe evidence ledgers that preserve state age, sensing confidence, calibration version, decision latency, admission/fallback, and fairness rather than reporting only a weighted average cost.

## Attribution Block

- Source URL: https://arxiv.org/abs/2210.17025
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Primary metadata, title, authors, submission history, category, DOI, license, and source links.
- Source URL: https://arxiv.org/pdf/2210.17025
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Primary full paper for formulation, algorithms, simulations, appendices, and references; verified local copy withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2210.17025
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Approved full-paper HTML fallback; verified local copy withheld.
- Source URL: https://arxiv.org/e-print/2210.17025
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Primary TeX/source package used through a local extraction cache; source package withheld.
- Source URL: https://doi.org/10.48550/arXiv.2210.17025
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Persistent arXiv identifier.
- Source URL: https://doi.org/10.1109/TWC.2023.3261338
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Publisher DOI for the IEEE Transactions on Wireless Communications article.
- Source URL: https://www.eng.auburn.edu/~szm0001/papers/TWC2023Chen.pdf
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Author-hosted published article used for publication and consistency checks; no file deposited.
- Source URL: https://www.eng.auburn.edu/~szm0001/publications-bib.html
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Author publication list used to cross-check volume, issue, pages, year, and DOI.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `joint_sensing_mec_manuscript.md`
  - Notes: Repository deposition and source-withholding authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`; `joint_sensing_mec_manuscript.md`
  - Notes: DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Companion repository authority used before related-entry and dedup exploration.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Related conceptual source for sensor-state representation and decision latency; does not validate selected-paper claims.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Related conceptual source for fresh-state safety gates and fallbacks; does not validate selected-paper claims.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Related conceptual source for spatiotemporal calibration and staged optimization; does not validate selected-paper claims.
- Source URL: https://doi.org/10.1109/JSAC.2021.3065072
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Near-primary AoI background reading.
- Source URL: https://doi.org/10.1109/JIOT.2024.3443701
  - Applies to: `joint_sensing_mec_manuscript.md`
  - Notes: Later sensing/computation optimization context; not validation evidence.
- Source-file policy: Original source files were withheld locally.
  - Applies to: the entire DEP entry.
  - Notes: No `.source/` directory was created and no PDF, HTML, source archive, cache, or extracted source text was uploaded.
