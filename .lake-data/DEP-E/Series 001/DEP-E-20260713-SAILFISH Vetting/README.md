# DEP-E-20260713-SAILFISH Vetting

#smart-contracts #ethereum #static-analysis #symbolic-execution #formal-methods #cybersecurity #vulnerability-detection #research-review

Public-safe deposition context: This DEP-E research entry reviews arXiv:2104.08638v2 using a local-first extraction cache and public primary metadata. Exact execution timestamps, local paths, machine identifiers, and local timezone details are intentionally omitted. The analysis is defensive and does not reproduce exploit payloads.

## Contents

- `README.md` - DEP manifest, item inventory, relevance summary, and complete source attribution.
- `sailfish_vetting_manuscript.md` - Schema-complete manuscript review covering paper metadata, evidence, mechanism, evaluation, limitations, implementation paths, random selection, cache extraction, dedup validation, and exactly three related DEP entries.

No `.source/` directory is included. A local archive PDF was inspected, but no original source file was collected for redistribution; public URLs provide provenance for the generated artifact.

## Summary of Items

- `README.md` preserves the deposition contract and makes the source policy explicit. It matters because downstream reviewers can verify that every included item is listed and every source URL is annotated.
- `sailfish_vetting_manuscript.md` is the durable research artifact. It explains how SAILFISH combines storage-dependency graph queries with value-summary-guided symbolic evaluation, assesses the reported 89,853-contract evaluation and ablation evidence, records unsoundness and compatibility limits, and translates the mechanism into bounded defensive implementation ideas.

## Insights and Relevance

SAILFISH is valuable beyond smart-contract security because it demonstrates a reusable assurance pattern: use a lightweight, over-approximating stage to compress a large search space, then spend precise analysis only on evidence-bearing candidates. The paper's value-summary analysis also shows that the most precise intermediate representation is not always the most operationally useful when generation and solver costs dominate. Connections to the Antaeus, Chai, and VeriChat DEP entries extend this pattern across repository-level logic-vulnerability detection, dependency-graph propagation, and formal-verification-backed agent workflows. The deposit preserves an important constraint: the reported historical results are author claims until independently reproduced against pinned artifacts and a current corpus.

## Attribution Block

- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `sailfish_vetting_manuscript.md`
  - Notes: Live Black Lake deposition standard inspected before artifact generation.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `README.md`; `sailfish_vetting_manuscript.md`
  - Notes: Related repository deposition standard inspected before related-entry synthesis.
- Source URL: https://arxiv.org/abs/2104.08638
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: Primary arXiv metadata, abstract, version, and paper links.
- Source URL: https://fredfeng.github.io/papers/sailfish.pdf
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: Author-hosted public paper used for full-text and visual-context cross-checking.
- Source URL: https://doi.org/10.1109/SP46214.2022.9833721
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: Publisher DOI for the IEEE S&P 2022 conference paper.
- Source URL: https://seclab.cs.ucsb.edu/publications/priyanka_sailfish_22/
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: UCSB SecLab institutional publication record.
- Source URL: https://github.com/ucsb-seclab/sailfish
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: Official code and experimental-data repository; inspected but not executed.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260702-Tech%20Intel%201102/daily_research_findings_2026-07-02_1102.md
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: Related Antaeus DEP entry; primary basis cross-checked at https://arxiv.org/abs/2607.01138.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260626-Tech%20Intel%201103/daily_research_findings_2026-06-26_1103.md
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: Related Chai DEP entry; primary basis cross-checked at https://arxiv.org/abs/2606.26933.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260706-Tech%20Intel%200104/daily_research_findings_2026-07-06_0104.md
  - Applies to: `sailfish_vetting_manuscript.md`
  - Notes: Related VeriChat DEP entry; primary basis cross-checked at https://arxiv.org/abs/2607.01668.
