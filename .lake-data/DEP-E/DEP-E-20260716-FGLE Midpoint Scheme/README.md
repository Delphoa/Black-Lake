# DEP-E-20260716-FGLE Midpoint Scheme

**Title:** Fractional Ginzburg-Landau midpoint scheme review
**Tags:** numerical-analysis, fractional-pde, finite-difference, convergence, source-first-review

Public-safe context: on 2026-07-16, one local arXiv paper unit was selected uniformly from 75,776 unique PDF-parent units and accepted on the first draw after ID, DOI, normalized-title, slug, repository, memory, companion-repository, and 24-hour checks. Its valid PDF lacked full-paper HTML, so an approved ar5iv fallback repaired the unit after official arXiv HTML was unavailable. The repaired unit passed the mandatory integrity gate. No local path, exact execution timestamp, private cache, or source file appears here.

## Contents

- `fgle_midpoint_scheme_manuscript.md` - schema-complete, source-grounded research manuscript.
- `README.md` - deposit context, inventory, synthesis, and attribution.

## Summary of Items

The manuscript reconstructs a fully implicit midpoint/weighted-shifted Grünwald difference scheme for a one-dimensional nonlinear fractional complex Ginzburg-Landau equation. It distinguishes the a priori bound, existence, second-order convergence, conditional uniqueness, linearized inner iteration, and synthetic numerical evidence. Random selection, deduplication, archive repair, extraction-cache behavior, publisher metadata, and the no-source-upload gate are recorded as evidence.

## Insights and Relevance

The paper gives a rigorous path from a nonlocal fractional operator to a second-order discrete method. Its strongest claim is an `l2_h` error bound of order `O(tau^2 + h^2)` without tying the convergence theorem's time step to the mesh size. Numerical tables show approximately second-order refinement for the classical case and self-convergence for three fractional orders.

The main audit boundary is narrower than the abstract may suggest. The full-line problem is truncated to a finite interval with a homogeneous exterior volume constraint; uniqueness is proved under a `tau <= C h` relation even though boundedness and convergence avoid a mesh-ratio condition; and fractional-order accuracy uses the same scheme on a finer grid as reference. Global NS Existence, Flag Hardy Operators, and Acoustic Phase Retrieval sharpen proof-dependency, nonlocal-operator, and independent-solver validation questions.

## Attribution Block

- Primary paper: *An implicit midpoint difference scheme for the fractional Ginzburg-Landau equation*, Pengde Wang and Chengming Huang.
- arXiv: https://arxiv.org/abs/1601.02301v1
- Full paper: https://arxiv.org/pdf/1601.02301 and https://ar5iv.labs.arxiv.org/html/1601.02301
- arXiv DOI: https://doi.org/10.48550/arXiv.1601.02301
- Journal DOI: https://doi.org/10.1016/j.jcp.2016.02.018
- This deposit is an independent review. Source files, metadata HTML, cache outputs, and extracted text were withheld locally and were not uploaded.
