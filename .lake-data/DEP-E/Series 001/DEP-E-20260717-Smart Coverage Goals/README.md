# DEP-E-20260717-Smart Coverage Goals

#software-testing #search-based-testing #unit-testing #coverage #genetic-algorithms #multi-objective-optimization #evosuite #research-review

Public-safe deposition context: this DEP-E preserves a source-first review of *Selectively Combining Multiple Coverage Goals in Search-Based Unit Test Generation* (`arXiv:2208.04096v1`; DOI `10.1145/3551349.3556902`). The selected archive unit was repaired to a verified complete PDF/full-paper-HTML state before review. All original source files, metadata HTML, TeX/source material, extracted text, caches, local locations, and exact execution details remain withheld.

## Contents

- `README.md`
  - This DEP inventory, public-safe source policy, synthesis context, and final attribution record.
- `smart_coverage_goals_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence, smart-selection mechanics, evaluation results, limitations, implementation paths, exactly three exercise paths, and exactly three related DEP entries.

No `.source/` directory exists. The PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, and local cache were intentionally kept outside the public repository.

## Summary of Items

### `README.md`

Records the deposit boundary, complete file inventory, source-withholding policy, relationship to the operational log and detailed Report-Mark, and annotated public sources.

### `smart_coverage_goals_manuscript.md`

Reviews the paper's three-stage selector: group eight criteria by coverage correlation, choose representative criteria whose fitness functions better guide search, then preserve omitted properties through subsuming goal subsets. It records the evaluation on 400 Java classes with WS, MOSA, and DynaMOSA; the strongest gains on larger classes; the weaker and sometimes adverse behavior with DynaMOSA or the subsumption ablation; and practical paths for auditable coverage-goal budgeting.

## Insights and Relevance

The durable contribution is not simply “use fewer objectives.” It is a traceable reduction rule: identify correlated properties, prefer objectives with smoother search guidance, and retain a minimal set of goals that subsume omitted properties. That mechanism is useful anywhere evaluation or generation becomes less effective when too many partially redundant goals compete for a fixed budget.

The evidence also resists a universal-efficiency reading. Smart selection is strongest for WS and for classes with at least 200 branches; MOSA gains are concentrated in larger classes; DynaMOSA already reduces active goals through dependency structure and shows only slight differences overall. The paper's own subsumption ablation further shows that shrinking the goal set can improve some criteria while weakening others. The matching operational note is `.logs/20260717-Arxiv-Smart-Coverage-Selection-LOG.md`; the detailed cross-DEP synthesis and code mock-ups are in `.reports/BL-Arxiv-Smart-Coverage-Selection-20260717/Report-Mark.md`.

## Attribution Block

- Source URL: https://arxiv.org/abs/2208.04096
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Canonical title, authors, arXiv ID, submission date, abstract, subjects, and public source locators.
- Source URL: https://arxiv.org/pdf/2208.04096
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Public equivalent of the complete primary PDF inspected locally; file not redistributed.
- Source URL: https://ar5iv.labs.arxiv.org/html/2208.04096
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Approved full-paper HTML fallback used after the official arXiv HTML endpoint returned 404; file not redistributed.
- Source URL: https://arxiv.org/e-print/2208.04096
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: TeX/source package used locally to cross-check equations, tables, figures, and threats to validity; file not redistributed.
- Source URL: https://doi.org/10.1145/3551349.3556902
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Persistent DOI for the ASE 2022 paper.
- Source URL: https://conf.researchr.org/details/ase-2022/ase-2022-research-papers/14/Selectively-Combining-Multiple-Coverage-Goals-in-Search-Based-Unit-Test-Generation
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Official ASE program record for authorship, venue, abstract, DOI, and preprint link.
- Source URL: https://conf.researchr.org/details/ase-2022/ase-2022-artifact-evaluation/7/Artifact-for-Selectively-Combining-Multiple-Coverage-Goals-in-Search-Based-Unit-Test
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Official ASE artifact-evaluation record and artifact DOI; the artifact itself was not executed in this review.
- Source URL: https://doi.org/10.5281/zenodo.6467640
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Online-artifact DOI cited in the paper source; recorded but not downloaded or executed.
- Source URL: https://doi.org/10.5281/zenodo.7026797
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Artifact DOI exposed by the official ASE artifact-evaluation page; recorded separately because it differs from the preprint's locator.
- Source URL: https://chrisyttang.org/pages/publications.html
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Author publication list confirming the conference record and the later journal extension, *Coverage Goal Selector for Combining Multiple Criteria in Search-Based Unit Test Generation*.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `smart_coverage_goals_manuscript.md`
  - Notes: Live authority for repository layout, source withholding, DEP contents, logs, reports, attribution, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `smart_coverage_goals_manuscript.md`
  - Notes: Live authority for DEP-E container filing and publication-index maintenance.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Live companion-repository authority read before its DEP context was used for deduplication and relationship synthesis.
- Repository file: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260714-Tech Intel 1106/daily_research_findings_2026-07-14_1106.md`
  - Public URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260714-Tech%20Intel%201106/daily_research_findings_2026-07-14_1106.md
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Related DEP entry on SCATE's coverage-guided supervision for automated test generation; primary source basis is https://arxiv.org/abs/2607.08983.
- Repository file: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104/daily_research_findings_2026-07-17_0104.md`
  - Public URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/daily_research_findings_2026-07-17_0104.md
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Related DEP entry on SWE-Bench Pro benchmark defects, including low-coverage and overly strict tests; primary source basis is https://openai.com/index/separating-signal-from-noise-coding-evaluations/.
- Repository file: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260716-Tech Intel 1303/daily_research_findings_2026-07-16_1303.md`
  - Public URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/daily_research_findings_2026-07-16_1303.md
  - Applies to: `smart_coverage_goals_manuscript.md`
  - Notes: Related DEP entry on AgentCompass's modular benchmark, harness, environment, and trajectory-analysis infrastructure; primary source basis is https://arxiv.org/abs/2607.13705.
