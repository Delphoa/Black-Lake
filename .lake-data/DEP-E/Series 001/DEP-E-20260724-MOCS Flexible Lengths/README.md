# DEP-E-20260724-MOCS Flexible Lengths

#information-theory #complementary-codes #sequence-design #wireless-communications #radar

DEP class: DEP-E

Subject: Source-grounded review of generalized-Boolean-function constructions for mutually orthogonal complementary sets with flexible non-power-of-two lengths.

Public-safe context: The local paper unit was repaired from partial to verified complete before review. The generated artifact cites public sources only. PDFs, full-paper HTML, metadata HTML, renderings, private verification records, and other source-derived material were withheld locally; no `.source/` directory was created.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summary, research relevance, and source attribution.
- `mocs_flexible_lengths_manuscript.md`
  - Schema-complete manuscript review of `arXiv:2003.06991v1`, including formal construction notes, evidence ledger, limitations, implementation paths, and exactly three related DEP bridges.

## Summary of Items

`mocs_flexible_lengths_manuscript.md` reviews the paper's `(M,N,L)` MOCS formulation, flexible length family `2^(m-1) + 2^t`, generalized Boolean function construction, proof strategy, worked examples, and `M/N = 1/2` Corollary 5 result. It distinguishes formal source evidence from reviewer interpretation, records notation and table inconsistencies, and translates the work into bounded code-generation, correlation-verification, and simulation concepts.

`README.md` explains why the manuscript belongs in DEP-E, inventories the deposited files, and preserves public attribution without redistributing source documents.

## Insights and Relevance

The paper contributes an algebraic route from binary-variable structure to exact complementary and mutual-orthogonality identities at lengths that need not be powers of two. Its most reusable engineering idea is proof-carrying code generation: a sequence family should be accompanied by parameters, source identity, and exhaustive correlation residuals. The three related DEP entries extend that idea across sequence complexity, OTFS receiver geometry, and multi-point sensing/communications allocation. Together they define a research path from formal code properties to end-to-end wireless evidence without treating correlation optimality as automatic security or deployment readiness.

## Attribution Block

- Source URL: https://arxiv.org/abs/2003.06991
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Canonical arXiv metadata, authors, date, version, abstract, subject, and public artifact links.
- Source URL: https://arxiv.org/pdf/2003.06991
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Complete paper used for theorem, example, table, conclusion, appendix, and visual review; local copy withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2003.06991
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Approved verified full-paper HTML fallback; local copy withheld.
- Source URL: https://arxiv.org/e-print/2003.06991
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Public source-package locator; no source package is included.
- Source URL: https://doi.org/10.48550/arXiv.2003.06991
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Persistent arXiv identifier.
- Source URL: https://doi.org/10.1109/TIT.2020.2980818
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: IEEE published-record identifier.
- Source URL: https://repository.essex.ac.uk/30464/
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Institutional publication and accepted-version metadata.
- Source URL: https://researchoutput.ncku.edu.tw/en/publications/how-to-construct-mutually-orthogonal-complementary-sets-with-non--2/
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Institutional venue, volume, issue, page, and publication metadata.
- Related DEP: `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md`
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Sequence-complexity and optimal-autocorrelation bridge grounded in `https://arxiv.org/abs/2209.10279`.
- Related DEP: `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: OTFS delay-Doppler receiver bridge grounded in `https://arxiv.org/abs/2311.08543`.
- Related DEP: `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
  - Applies to: `mocs_flexible_lengths_manuscript.md`
  - Notes: Radar/communications, fusion, power, and interference bridge grounded in `https://arxiv.org/abs/2208.07592`.
- Source-file policy
  - Applies to: Entire DEP entry.
  - Notes: Source files were withheld locally. No PDF, HTML, metadata page, source archive, extracted text, cache, render, verification record, or `.source/` directory was uploaded.
