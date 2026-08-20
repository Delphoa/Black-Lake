# DEP-E-20260722-Causal DP Workloads

#differential-privacy #causal-inference #synthetic-data #uncertainty-quantification #responsible-ai

Deposited 2026-07-22 as a DEP-E research artifact expanding the workload-preserving differential-privacy thread preserved by `Black-Lake-Data/.lake-data/DEP-20260712-Tech Intel 1100`.

## Contents

- `README.md`
- `causal-dp-workloads.md`

## Item Summaries

- `README.md` inventories the DEP, states its research role, and preserves public attribution.
- `causal-dp-workloads.md` is the schema-complete manuscript. It expands arXiv:2607.08122 through the current v2 full text and the paper's official implementation repository, while retaining the selected source DEP's prior research graph.

## Insights and Relevance

The reviewed work separates privacy-preserving data release from valid causal inference. Its central design choice is to spend privacy budget on treatment-arm and outcome moments that identify an orthogonal causal score, then propagate release noise into uncertainty rather than treating synthetic rows as ordinary observations. The paper and code support a practical research program, but the comparison boundary matters: the repository labels its MST comparator as a simplified MST-style product baseline rather than the official Private-PGM implementation. This artifact therefore preserves the reported coverage result while treating broad baseline superiority as unresolved.

## Source Inventory

- Selected source DEP: `Black-Lake-Data/.lake-data/DEP-20260712-Tech Intel 1100`.
- Prior DEP Class artifacts: `Black-Lake/.lake-data/DEP-E/DEP-E-20260713-Tech Intel 1100 Review` and `Black-Lake/.lake-data/DEP-E/DEP-E-20260716-Contravariance Study`.
- Newly expanded primary source: arXiv:2607.08122v2, canonical record and complete public HTML manuscript.
- Official implementation: `AsiaeeLab/causal-aim` at commit `cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f`.
- External source files collected for public deposition: none.

## Attribution Block

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/e09ab977fedb25f03690b731d751ab93d4ede947/.lake-data/DEP-20260712-Tech%20Intel%201100
  - Applies to: `causal-dp-workloads.md` and this README.
  - Notes: Selected source DEP, original digest, prior Report-Marks, and iterative context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/b8f1fc50c914447de0b7818ff427e55d2dbaee2e/.lake-data/DEP-E/DEP-E-20260716-Contravariance%20Study/contravariance-study.md
  - Applies to: `causal-dp-workloads.md`.
  - Notes: Latest prior DEP Class manuscript and preserved related-reading graph.
- Source URL: https://arxiv.org/abs/2607.08122v2
  - Applies to: `causal-dp-workloads.md`.
  - Notes: Canonical primary record for title, authorship, revision, venue claim, and license link.
- Source URL: https://arxiv.org/html/2607.08122v2
  - Applies to: `causal-dp-workloads.md`.
  - Notes: Complete primary manuscript inspected online; no source file was deposited.
- Source URL: https://github.com/AsiaeeLab/causal-aim/tree/cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f
  - Applies to: `causal-dp-workloads.md`.
  - Notes: Official implementation, reproduction notebooks, data instructions, and code-level comparison boundary.
