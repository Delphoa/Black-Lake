# DEP-E-20260716-Judge Conformal

#llm-evaluation #conformal-prediction #uncertainty #calibration #responsible-ai

Public-safe research deposit reviewing arXiv:2509.18658v1. Original paper documents and extraction caches remain in the local archive and are not included.

## Contents

- `README.md` - deposit inventory, summary, relevance, and attribution.
- `llm_judge_conformal_manuscript.md` - schema-complete source-grounded manuscript review.

## Summary of Items

`llm_judge_conformal_manuscript.md` reconstructs the paper's split-conformal workflow for interval-valued LLM judging, discrete boundary adjustment, empirical evaluation, midpoint scoring, and stated limits. It records the random selection, dedup validation, source repair, cache methodology, official code inventory, related DEP bridges, implementation paths, and reproduction boundaries.

No `.source/` directory is present. PDF, full-paper HTML, metadata HTML, TeX/source archive, cached text, and repository evidence snapshots were deliberately withheld from the public deposit.

## Insights and Relevance

The work turns judge scores into evidence envelopes rather than pretending that a single rating is exact. Its most reusable lesson is governance-oriented: interval width, empirical coverage, calibration support, shift status, and human-review capacity must travel together. RLMF adds the distinction between expressed and factual confidence, PAC Confidence clarifies finite-sample and shift assumptions, and ConMax shows that confidence signals may also control reasoning cost. Together they motivate an auditable evaluation gate rather than a universal trust score.

## Attribution Block

- Source URL: https://arxiv.org/abs/2509.18658v1
  - Applies to: `llm_judge_conformal_manuscript.md`
  - Notes: Canonical metadata and abstract record.
- Source URL: https://arxiv.org/pdf/2509.18658
  - Applies to: `llm_judge_conformal_manuscript.md`
  - Notes: Complete PDF inspected locally and withheld.
- Source URL: https://arxiv.org/html/2509.18658
  - Applies to: `llm_judge_conformal_manuscript.md`
  - Notes: Complete official full-paper HTML inspected locally and withheld.
- Source URL: https://arxiv.org/e-print/2509.18658
  - Applies to: `llm_judge_conformal_manuscript.md`
  - Notes: TeX/source archive inspected locally and withheld.
- Source URL: https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge
  - Applies to: `llm_judge_conformal_manuscript.md`
  - Notes: Official implementation inventory inspected at commit `6c5d8302999b028d460dd1a7b78d698c56f7b7b7`; no repository license was visible.
