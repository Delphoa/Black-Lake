# Arxiv DEP Log: RPDG Incremental Gradient

- Run date: 2026-08-04; exact execution time withheld.
- Actor/tool: Codex, using the manuscript research, arXiv archive, download-safety, PDF-inspection, and DEP submission workflows.
- Action: Randomly select one eligible local arXiv archive unit, enforce the complete-source gate, review it source-first, and prepare a DEP-E research deposit.
- Outcome: Complete and ready for repository submission.
- Blockers: None. The TeX/source package was unavailable under the bounded archive-broker policy; the verified PDF and full-paper HTML satisfy the mandatory paper-integrity gate.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumerated PDF candidates; PDF parent directories were deduplicated as paper units; resolvable arXiv IDs were compared against the used-paper index; PowerShell `Get-Random` drew one uniform zero-based index from the eligible array.
- PDF candidates: 75,960.
- Unique parent-paper units: 75,957.
- Used arXiv base IDs indexed: 2,030.
- Units excluded by used arXiv ID: 565.
- Identifier-incomplete units withheld from the draw: 185.
- Eligible units: 75,207.
- Selected zero-based eligible index: 75,124.
- Selected paper: *An optimal randomized incremental gradient method*.
- Selected identity: arXiv:1507.02000v3; arXiv DOI 10.48550/arXiv.1507.02000; published DOI 10.1007/s10107-017-1173-0.
- Duplicate rejections and reselections: 0.

## Deduplication and Reselection Validation

- Scan locations: live `Delphoa/Black-Lake` `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and live `Delphoa-Labs/Black-Lake-Data` `.logs`, `.reports`, `.lake-data`, and `.staging` where present.
- Keys checked: arXiv ID, arXiv DOI, published DOI, canonical title, normalized title, and planned slug.
- Exact-match result: no prior Arxiv DEP log, Report-Mark, DEP-E manuscript, correction marker, or archive-unit marker for this paper was found.
- Public-safe 24-hour cutoff date: 2026-08-03.
- Recent same-paper marker result: none found.
- Total units withheld before the draw: 750, comprising 565 used-ID units and 185 identifier-incomplete units.

## Source-Integrity Gate

- Initial classification: `partial`. A valid PDF existed, but verified full-paper HTML was absent.
- Repair: preserved the existing PDF and ran one broker-controlled single-paper repair. The official arXiv HTML routes were unavailable, so the approved ar5iv full-paper fallback was collected. Metadata HTML and the archive provenance/verification companions were refreshed.
- PDF verification: 478,223 bytes; `%PDF-` header; trailing `%%EOF`; 31 pages; not encrypted.
- Full-paper HTML verification: 5,577,971 bytes; 219,658 stripped body characters; article/main/LaTeXML marker present; 89 section or heading markers; six independently observed paper-structure terms.
- Metadata HTML: 42,216 bytes.
- Partial files: 0.
- Source package: unavailable after the bounded broker attempt; no blind retry was made.
- Final classification: `complete` because the PDF and full-paper HTML both passed every mandatory validation rule.
- Local archive companions: README, provenance record, machine-readable summary, immutable acquisition receipt, and verification report were updated by the repair process.

## Review Record

- Complete arXiv v3 PDF and full-paper HTML were inspected; representative algorithm, theorem, lower-bound, extension, and conclusion pages were rendered and visually checked.
- Public metadata, the Optimization Online author-deposited record, the published DOI, and DBLP bibliographic record were inspected.
- The review preserved the finite-sum composite problem, the PDG saddle-point/Bregman construction, the one-component RPDG update, non-uniform and uniform sampling policies, upper complexity bounds, the lower-bound model, non-strongly-convex extensions, and the authors' stated future-work boundary.
- No numerical experiments appear in the paper. No official implementation repository was established. Code and experiments were not run.
- Main evidence limitation: the optimality claim is conditional on the paper's oracle model, sufficiently large dimension, independent component sampling, and linear-span iterate restriction; it is not a blanket lower bound for every modern adaptive finite-sum optimizer.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/epsilon_prox_affine_manuscript.md` - composite convex modeling, proximal operators, affine structure, and solver-validation concerns.
2. `.lake-data/DEP-E/DEP-E-20260728-Local Stochastic Bilevel/local_stochastic_bilevel_manuscript.md` - stochastic gradient complexity, variance reduction, and the gap between oracle counts and operational cost.
3. `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` - regularizer-generated Bregman geometry, linear convergence, and bounded-error floors.

Exactly three related entries were inspected and used. Their claims do not independently validate the selected paper.

## Generated Public Artifacts

- `.logs/20260804-Arxiv-RPDG-Incremental-Gradient-LOG.md`
- `.reports/BL-Arxiv-RPDG-Incremental-Gradient-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-RPDG Incremental Grad/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-RPDG Incremental Grad/rpdg_incremental_gradient_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication-index update.

## Public-Safety and Submission Gate

- Original PDF, full-paper HTML, metadata HTML, receipts, provenance, renderings, caches, and other source material remain local.
- No public `.source/` directory was created.
- The intended staged allowlist contains only the five generated or updated Markdown files listed above.
- Before submission, staged paths, source-file extensions, exact-title/schema rules, exact-three synthesis counts, code syntax, URL attribution coverage, and local-context leak patterns must pass validation.

## Attribution Block

- Source URL: https://arxiv.org/abs/1507.02000
  - Applies to: canonical title, authors, version history, subjects, abstract, and source locators.
  - Notes: Metadata evidence only; the abstract was not used as the full paper.
- Source URL: https://arxiv.org/pdf/1507.02000
  - Applies to: full-paper method, theorems, complexity statements, limitations, and visual inspection.
  - Notes: The verified PDF remained local and was not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/1507.02000
  - Applies to: searchable full-paper cross-check and source-integrity repair.
  - Notes: Approved fallback after official arXiv HTML routes were unavailable; the file remained local.
- Source URL: https://arxiv.org/e-print/1507.02000
  - Applies to: source-package acquisition attempt.
  - Notes: The bounded broker attempt did not produce a source package.
- Source URL: https://doi.org/10.48550/arXiv.1507.02000
  - Applies to: persistent arXiv identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://doi.org/10.1007/s10107-017-1173-0
  - Applies to: published article identity.
  - Notes: Mathematical Programming version of record.
- Source URL: https://optimization-online.org/?p=13502
  - Applies to: author-deposited technical-report context and update date.
  - Notes: Primary author deposit.
- Source URL: https://dblp.org/rec/journals/mp/LanZ18
  - Applies to: volume, pages, year, and bibliographic cross-check.
  - Notes: Bibliographic record.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260730-Epsilon%20Prox%20Affine/epsilon_prox_affine_manuscript.md
  - Applies to: proximal-operator and structured convex-solver relationship.
  - Notes: Related processed artifact; not validation of RPDG.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260728-Local%20Stochastic%20Bilevel/local_stochastic_bilevel_manuscript.md
  - Applies to: stochastic-gradient complexity and variance-reduction relationship.
  - Notes: Related processed artifact; not validation of RPDG.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: Bregman geometry and convergence relationship.
  - Notes: Related processed artifact; not validation of RPDG.
