# DEP-E-20260729-Semantic Password Risk

#password-security #authentication #pcfg #semantic-analysis #multilingual-security #usable-security #privacy #defensive-security #arxiv

Public-safe DEP-E research deposit generated on 2026-07-29 from a source-first review of `DEP-20260707-SEPCFG Paper`. The deposit examines SE#PCFG's multilingual semantic model, SEPCA evaluation, evidence limits, dual-use risk, and defensive use alongside current NIST password guidance.

## Contents

- `README.md` - DEP inventory, source policy, item summary, relevance, and annotated attribution.
- `semantic-password-risk.md` - Schema-complete manuscript covering the paper's model, 17-dataset evaluation, evidence ledger, claims map, limitations, standards boundary, safe implementation paths, and a local-only MVP concept.

No `.source/` directory is present. No password corpus, credential material, hash set, executable cracking tool, implementation repository, or newly collected external source file is deposited. The existing PDF, HTML, TeX archive, and Markdown source artifacts were inspected in the source repository and referenced through public URLs.

## Summary of Items

### `semantic-password-risk.md`

The manuscript separates author claims, reviewer interpretation, and defensive implementation conclusions. It verifies the paper's 43 semantic factor types, 17-dataset scope, 52 train-target evaluations, reported benchmark improvements, runtime table, weak-pattern examples, and ethical statement against the rendered PDF and TeX archive.

The defensive synthesis is deliberately non-generative. It proposes semantic categories only as local, coarse explanations that supplement whole-password blocklists, minimum length, rate limiting, password-manager support, and secure storage. It does not include password guesses, ranking logic, breach data, hashes, or cracking procedures.

## Insights and Relevance

SE#PCFG shows that predictable meaning survives superficial character complexity: names, dates, language-specific words, cultural entities, keyboard patterns, and short semantic combinations can remain modelable. Current NIST guidance creates a useful design constraint: semantic analysis can explain risk, but it should not become a new composition rule or replace required whole-password blocklist checks. This entry supports future work on privacy-preserving password meters, multilingual calibration, synthetic benchmarks, and standards-aware authentication testing.

## Attribution Block

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper
  - Applies to: `semantic-password-risk.md` and `README.md`.
  - Notes: Selected source DEP and fixed source snapshot.
- Source URL: https://arxiv.org/abs/2306.06824
  - Applies to: `semantic-password-risk.md`.
  - Notes: Canonical arXiv record for SE#PCFG.
- Source URL: https://arxiv.org/pdf/2306.06824
  - Applies to: `semantic-password-risk.md`.
  - Notes: Primary paper PDF inspected in full-page rendering.
- Source URL: https://arxiv.org/e-print/2306.06824
  - Applies to: `semantic-password-risk.md`.
  - Notes: Primary TeX/source archive endpoint.
- Source URL: https://doi.org/10.1109/TDSC.2025.3547773
  - Applies to: `semantic-password-risk.md`.
  - Notes: IEEE TDSC DOI recorded by the paper and arXiv metadata.
- Source URL: https://pages.nist.gov/800-63-4/sp800-63b.html
  - Applies to: `semantic-password-risk.md`.
  - Notes: Current password requirements and defensive implementation boundary.
- Source URL: https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/semantic-patterns-passwords-and-their-security-impact/
  - Applies to: `semantic-password-risk.md`.
  - Notes: Official record for the principal semantic-password predecessor.
- Source URL: https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/wheeler
  - Applies to: `semantic-password-risk.md`.
  - Notes: Official zxcvbn paper record and defensive password-meter context.
- Source URL: https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/melicher
  - Applies to: `semantic-password-risk.md`.
  - Notes: Official FLA paper record and benchmark context.
- Source URL: https://doi.org/10.1109/SP.2009.8
  - Applies to: `semantic-password-risk.md`.
  - Notes: Foundational PCFG paper locator cited by SE#PCFG.
