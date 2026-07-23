# DEP-E-20260723-ANCHOR Audit

#ai-safety #agentic-ai #cli-agents #alignment-auditing #reproducibility #evaluation #research

Public-safe DEP-E research deposit generated from an iterative, source-first review of `DEP-20260714-Tech Intel 1305`. This pass expands the randomly selected persistent-alignment-auditing thread by re-inspecting the complete ANCHOR paper and pinning the official implementation release.

## Contents

- `README.md` - DEP inventory, summary, relevance, source policy, and attribution.
- `anchor-audit.md` - Schema-complete manuscript covering the ANCHOR method, evidence, release integrity, reproducibility limits, defensive implementation paths, and follow-on reading.

No `.source/` directory is present. A filtered temporary checkout was used to inspect the pinned repository tree and six small release files, then removed after review. No paper PDF, task dataset, harmful prompt set, model weights, trajectory, generated artifact, credential, or experiment output is deposited.

## Summary of Items

### `anchor-audit.md`

The manuscript distinguishes three evidence layers: the paper's reported evaluation, the public repository's actual release surface, and reviewer inference. The paper reports that a persistent multi-turn auditor reduced refusal to zero across eight tested models in its evaluation setting, but the release is not a frozen reproduction package. Its ablation report omits raw per-case runs and records a vanilla-model result that differs from the paper's table. The pinned tree also lacks a dependency lock, test suite, continuous-integration workflow, and visible repository license file.

The review treats ANCHOR as high-risk defensive research. It does not reproduce adversarial prompts, harmful task content, or execution procedures. The practical translation is a benign persistence-safety harness that measures authorization stability, cumulative tool effects, judge disagreement, rollback, and containment using synthetic fixtures.

## Insights and Relevance

The main semantic-web contribution is a versioned distinction between a source claim and the public evidence required to audit that claim. ANCHOR provides strong evidence that one-shot refusal is an incomplete safety metric, while its release illustrates why aggregate tables, mutable model endpoints, stateful CLI configuration, and missing run artifacts should not be collapsed into a claim of turnkey reproducibility. A downstream reviewer can now follow the source DEP, prior bundle review, canonical paper, exact repository commit, and release-specific ablation discrepancy without handling operational harmful content.

## Attribution Block

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/0069e91f03438d2e17c5569a057c284a6ce4d055/.lake-data/DEP-20260714-Tech%20Intel%201305
  - Applies to: `anchor-audit.md` and `README.md`.
  - Notes: Selected source DEP and its prior Report-Mark lineage.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/716d07d43cb4007980d1fbdd73ec0245d42776ea/.lake-data/DEP-E/DEP-E-20260721-Agent%20Evidence%20Loops
  - Applies to: `anchor-audit.md`.
  - Notes: Latest prior same-family DEP-Class artifact reviewed before iterative expansion.
- Source URL: https://arxiv.org/abs/2607.10455v1
  - Applies to: `anchor-audit.md`.
  - Notes: Canonical ANCHOR metadata and primary paper record.
- Source URL: https://arxiv.org/html/2607.10455v1
  - Applies to: `anchor-audit.md`.
  - Notes: Complete paper text, tables, appendices, impact statement, and references inspected.
- Source URL: https://github.com/garified/ICML-anchor/tree/9a6bd1cb6960b690f27bb5c797f33ce15e4bb0ad
  - Applies to: `anchor-audit.md`.
  - Notes: Official implementation pinned to the inspected one-commit release tree.
- Source URL: https://github.com/garified/ICML-anchor/blob/9a6bd1cb6960b690f27bb5c797f33ce15e4bb0ad/ablation/ABLATION_REPORT.md
  - Applies to: `anchor-audit.md`.
  - Notes: Release-specific aggregate ablation evidence and reproducibility limitations.
