# Arxiv DEP Log: RetinaGAN Sim-to-Real

- Run date: 2026-08-05; exact execution time withheld.
- Actor/tool: Codex, using the manuscript research, arXiv archive, download-safety, PDF-inspection, and DEP submission workflows.
- Action: Randomly select one eligible local arXiv archive unit, enforce the complete-source gate, review it source-first, and prepare a DEP-E research deposit.
- Outcome: Complete and ready for repository submission.
- Blockers: None. The selected unit required a bounded full-paper HTML repair before review.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumerated PDF candidates; PDF parent directories were deduplicated as paper units; resolvable arXiv IDs were compared against the used-paper index; PowerShell `Get-Random` drew one uniform zero-based index from the eligible array.
- PDF candidates: 75,960.
- Unique parent-paper units: 75,957.
- Used arXiv base IDs indexed: 2,118.
- Units excluded by used arXiv ID: 586.
- Identifier-incomplete units withheld from the draw: 185.
- Eligible units: 75,186.
- Selected zero-based eligible index: 20,079.
- Selected paper: *RetinaGAN: An Object-aware Approach to Sim-to-Real Transfer*.
- Selected identity: arXiv:2011.03148v2; arXiv DOI 10.48550/arXiv.2011.03148; published DOI 10.1109/ICRA48506.2021.9561157.
- Duplicate rejections and reselections: 0.

## Deduplication and Reselection Validation

- Scan locations: live `Delphoa/Black-Lake` `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and live `Delphoa-Labs/Black-Lake-Data` `.logs`, `.reports`, `.lake-data`, and `.staging` where present.
- Keys checked: arXiv ID, arXiv DOI, published DOI, canonical title, normalized title, `RetinaGAN`, and the planned slug.
- Exact-match result: no prior Arxiv DEP log, Report-Mark, DEP-E manuscript, correction marker, or archive-unit marker for this paper was found.
- Public-safe 24-hour cutoff date: 2026-08-04.
- Recent same-paper marker result: none found.
- Total units withheld before the draw: 771, comprising 586 used-ID units and 185 identifier-incomplete units.

## Source-Integrity Gate

- Initial classification: `partial`. A valid PDF existed, but verified full-paper HTML was absent.
- Repair: preserved the existing PDF and ran one credential-free, broker-controlled, single-paper repair. Official arXiv full-paper HTML was unavailable, so the approved ar5iv full-paper fallback was collected. Metadata HTML, the TeX/source package, README, attribution/provenance, machine-readable summary, acquisition receipt, and verification report were refreshed locally.
- PDF verification: 3,441,421 bytes; `%PDF-` header; trailing `%%EOF`; nine pages; not encrypted. The repaired copy was byte-identical to the preserved PDF.
- Full-paper HTML verification: 262,341 bytes; 46,688 stripped body characters; article/main/LaTeXML document marker present; 50 section or heading markers; six independently observed paper-structure terms.
- Metadata HTML: 43,425 bytes.
- TeX/source package: 4,031,004 bytes; 37 readable archive entries.
- Partial files: 0.
- Final classification: `complete` because the PDF and full-paper HTML passed every mandatory validation rule.

## Review Record

- The complete arXiv v2 PDF, approved full-paper HTML, and TeX source were inspected; all nine PDF pages were rendered and visually checked.
- The canonical arXiv record, official project page, arXiv DOI, ICRA DOI metadata, and project-linked Tensor2Robot component locators were inspected.
- The review preserved the CycleGAN base, frozen EfficientDet-D1 constraint, Huber box consistency, Focal Consistency Loss for soft class targets, bidirectional/cycled-image loss structure, grasping/pushing/door-opening protocols, reported metrics, appendix hyperparameters, and visible limitations.
- No author-released RetinaGAN implementation repository was established. The official project page links upstream Tensor2Robot components but not a RetinaGAN training release. Code and experiments were not run.
- Main evidence limitations: pushing uses only 10 real attempts; door opening uses 30 trials on doors seen during training and includes a best-of-three selection note; grasping uses 90 trials per condition; detector blind spots are inherited by the generator constraint; and printed loss/hyperparameter notation contains values that should be reconciled against an implementation before replication.

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260726-Habitat Synthetic Intake/whitepaper-intake-review.md` - synthetic 3D training infrastructure, controllability, realism, and explicit synthetic-to-real gap measurement.
2. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` - mixed real/synthetic perception training, domain adaptation, and evidence that synthetic-only training retains a domain gap.
3. `.lake-data/DEP-A/DEP-A-20260727-ManipulationNet An Intake/whitepaper-intake-review.md` - standardized physical robot-manipulation evaluation, calibration, safety, and the limits of simulation-only benchmarks.

Exactly three related entries were inspected and used. Their claims do not independently validate RetinaGAN.

## Generated Public Artifacts

- `.logs/20260805-Arxiv-RetinaGAN-Sim-to-Real-LOG.md`
- `.reports/BL-Arxiv-RetinaGAN-Sim-to-Real-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-RetinaGAN Sim-to-Real/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-RetinaGAN Sim-to-Real/retinagan_sim_to_real_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication-index update.

## Public-Safety and Submission Gate

- Original PDF, full-paper HTML, metadata HTML, TeX/source archive, receipts, provenance, renderings, caches, and other source material remain local.
- No public `.source/` directory was created.
- The intended staged allowlist contains only the five generated or updated Markdown files listed above.
- Before submission, staged paths, source-file extensions, exact-title/schema rules, exact-three synthesis counts, code syntax, URL attribution coverage, and local-context leak patterns must pass validation.

## Attribution Block

- Source URL: https://arxiv.org/abs/2011.03148
  - Applies to: canonical title, authors, version history, subjects, venue comment, abstract, and source locators.
  - Notes: Metadata evidence only; the abstract was not used as the complete paper.
- Source URL: https://arxiv.org/pdf/2011.03148
  - Applies to: complete method, experiments, tables, figures, appendix, and visual review.
  - Notes: The verified PDF remained local and was not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/2011.03148
  - Applies to: searchable full-paper cross-check and source-integrity repair.
  - Notes: Approved fallback after official arXiv full-paper HTML was unavailable; the file remained local.
- Source URL: https://arxiv.org/e-print/2011.03148
  - Applies to: TeX/source inspection and provenance.
  - Notes: The source package remained local and was not uploaded.
- Source URL: https://doi.org/10.48550/arXiv.2011.03148
  - Applies to: persistent arXiv identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://doi.org/10.1109/ICRA48506.2021.9561157
  - Applies to: ICRA 2021 publication identity.
  - Notes: Publisher DOI metadata.
- Source URL: https://retinagan.github.io/
  - Applies to: author project context, task examples, videos, and public component links.
  - Notes: Official project page; it does not expose an author-released RetinaGAN implementation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260726-Habitat%20Synthetic%20Intake/whitepaper-intake-review.md
  - Applies to: synthetic-scene and reality-gap relationship.
  - Notes: Related processed artifact; not validation of RetinaGAN.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260724-Spiking%20Pose%20Tracking/spiking_pose_tracking_manuscript.md
  - Applies to: synthetic/real perception and domain-adaptation relationship.
  - Notes: Related processed artifact; not validation of RetinaGAN.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260727-ManipulationNet%20An%20Intake/whitepaper-intake-review.md
  - Applies to: physical robot benchmark and evaluation-governance relationship.
  - Notes: Related processed artifact; not validation of RetinaGAN.
