# DEP-E-20260716-Acoustic Phase Retrieval

#acoustics #inverse-problems #phase-retrieval #phaseless-data #fourier-method #helmholtz-equation #reference-sources #measurement-design #source-reconstruction #research-review

Public-safe deposition context: this DEP-E preserves a source-first review of *Retrieval of acoustic sources from multi-frequency phaseless data* (`arXiv:1803.11323v1`). The selected local archive unit was repaired to a verified complete PDF/full-paper-HTML state before review. All original source files, extracted text, caches, local locations, and exact execution details remain withheld.

## Contents

- `README.md`
  - This DEP inventory, source policy, synthesis context, and final attribution record.
- `acoustic_phase_retrieval_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence, method, stability, numerical results, limitations, implementation paths, exactly three exercise paths, and synthesis with three related DEP entries.

No `.source/` directory exists. The PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, and local cache were intentionally kept outside the public repository.

## Summary of Items

### `README.md`

Records the deposit boundary, complete file inventory, public-safe run context, relationship to the operational log and detailed Report-Mark, and annotated public sources.

### `acoustic_phase_retrieval_manuscript.md`

Reviews the paper's two-reference-source phase formula, determinant lower bounds, perturbation theorem, Fourier reconstruction, and synthetic noise results. It separates source claims from reviewer interpretation, records the random selection/dedup/source-integrity gates, and connects the paper to Hypercomplex MRI, Irregular Clipped SR, and iKalibr Calibration.

## Insights and Relevance

The paper's durable mechanism is measurement intervention with a conditioning certificate. Two known point-source probes convert an ambiguous modulus-only field into a small linear solve for complex phase; a Fourier method then reconstructs the source. The synthesis extends that mechanism into a broader engineering contract: co-design measurements and decoders, validate calibration and observability before inversion, preserve representation structure, and carry conditioning/residual evidence into the final artifact. The strongest evidence remains the analytic phase-recovery argument and one synthetic two-dimensional experiment. Hardware, mismatch, calibration, runtime, repeated-seed, and field-generalization evidence remain open.

The matching operational note is `.logs/20260716-Arxiv-Acoustic-Phase-Retrieval-LOG.md`. The detailed synthesis and code mock-ups are in `.reports/BL-Arxiv-Acoustic-Phase-Retrieval-20260716/Report-Mark.md`. This DEP manuscript is the durable schema-complete research artifact; the log is operational, and the Report-Mark carries the richer cross-DEP concept bridge.

## Attribution Block

- Source URL: https://arxiv.org/abs/1803.11323
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Canonical title, authors, abstract, arXiv identifier, category, version history, and public source locators.
- Source URL: https://arxiv.org/pdf/1803.11323
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Public equivalent of the complete primary PDF inspected locally; file not redistributed.
- Source URL: https://ar5iv.labs.arxiv.org/html/1803.11323
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Approved full-paper HTML fallback inspected after official arXiv HTML was unavailable; not an abstract page.
- Source URL: https://arxiv.org/e-print/1803.11323
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: TeX/source package used locally to cross-check equations, tables, and structure; file not redistributed.
- Source URL: https://doi.org/10.1088/1361-6420/aaccda
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Persistent journal DOI.
- Source URL: https://scholars.hkbu.edu.hk/en/publications/retrieval-of-acoustic-sources-from-multi-frequency-phaseless-data/
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Official institutional publication record for journal, volume, issue, article number, date, and DOI.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `acoustic_phase_retrieval_manuscript.md`
  - Notes: Live authority for repository layout, source withholding, DEP contents, logs, reports, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `acoustic_phase_retrieval_manuscript.md`
  - Notes: Live authority for DEP-E container filing and the publications index.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Live companion-repository authority read before deduplication context was used.
- Repository file: `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Related DEP on physics-grounded MRI reconstruction; primary source basis is https://arxiv.org/abs/2503.05063.
- Repository file: `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Irregular%20Clipped%20SR/irregular_clipped_sr_manuscript.md
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Related DEP on nonlinear measurement intervention and decoding; primary source basis is https://arxiv.org/abs/2106.01573.
- Repository file: `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: `acoustic_phase_retrieval_manuscript.md`
  - Notes: Related DEP on excitation, calibration, and observability; primary source basis is https://arxiv.org/abs/2407.11420.
