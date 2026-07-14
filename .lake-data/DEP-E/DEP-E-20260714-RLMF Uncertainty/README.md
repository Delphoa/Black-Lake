# DEP-E-20260714-RLMF Uncertainty

#large-language-models #reinforcement-learning #metacognition #uncertainty #calibration #alignment #evaluation #research-review

Public deposition date: 2026-07-14. This DEP-E preserves a source-grounded manuscript review of **Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs** (arXiv:2606.32032v1). The source paper, appendices, figures, TeX, and official implementation were inspected; no source file or private processing path is redistributed.

## Contents

- `README.md` - package inventory, review context, synthesis, and attribution.
- `rlmf_uncertainty_manuscript.md` - schema-complete `manuscript-research-document` artifact covering the full paper, official code at a pinned commit, evidence ledger, claim audit, limitations, exactly three practical exercise paths, and a bounded MVP.

Supporting artifacts for the same Black Lake Arxiv DEP run are stored at:

- `.logs/20260714-Arxiv-RLMF-Uncertainty-LOG.md`
- `.reports/BL-Arxiv-RLMF-Uncertainty-20260714/Report-Mark.md`
- `.lake-data/DEP-A/DEP-A-20260714-RLMF Uncertainty/` for the independent whitepaper-grade review.

No `.source/` directory is included. PDF, full-paper HTML, metadata HTML, TeX source, extracted text, figures, and the filtered code cache remain private. Public URLs and version pins preserve provenance without duplicating source material.

## Summary of Items

The manuscript reconstructs RLMF as conditional advantage gain control. The policy emits sentence-level confidence, an intrinsic-confidence proxy is estimated from sampled-response consistency, and the policy predicts how faithfully its own confidence matched that proxy. The resulting metacognitive score amplifies only the centered faithfulness advantage of above-average completions. A companion data-selection stage selects both high- and low-self-rated examples; a separate rewriting stage maps calibrated numbers to contextual natural-language hedges.

The artifact records the main reported results without treating them as reproduced. Average cMFG-star rises from 0.60 to 0.84 for Llama3.1-8B-Instruct and from 0.54 to 0.83 for Qwen3-8B after RLMF. The paper reports strong cross-task results, extensive ablations, and 95-98 percent human preference over FUT on four linguistic-quality criteria. The review also preserves the principal qualifications: the “intrinsic” target is a judge-dependent consistency proxy; the main tables lack multi-seed uncertainty; in-domain test performance is used for checkpoint selection; and the full pipeline is compute intensive.

The official MIT-licensed repository was inspected at commit `a087e7a1e49f52aaa701add19cd80699b709fdef`. The central trainer and reward code match the paper's mechanism. One minor specification difference is documented: the displayed paper equation uses a strict `< tau` comparison while the pinned code counts exact-threshold cases with `<= mc_threshold`.

## Insights and Relevance

The transferable idea is not that self-reported confidence is inherently trustworthy. It is that a self-evaluation signal can change learning priority while remaining subordinate to an independently measured task component. This makes RLMF relevant to Black Lake work on auditable agent control, evaluator governance, and confidence-aware release gates.

Exactly three related DEP-E records ground the cross-repository synthesis:

- PAC Confidence adds finite-sample support, interval width, and distribution-shift boundaries to point estimates.
- OViP Preference shows how on-policy feedback loops can amplify judge or generator blind spots unless provenance and disagreement are retained.
- ConMax Reasoning provides a neighboring confidence-shaped optimization pattern in which an auxiliary evaluator protects task quality while another objective is optimized.

Together they motivate a release architecture that keeps task correctness, faithful calibration, confidence support, evaluator disagreement, rewrite preservation, and shift state separately observable. Natural uncertainty language can help users calibrate reliance, but it is not correctness evidence and must not replace verification or abstention in high-impact settings.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.32032
  - Applies to: `README.md` and `rlmf_uncertainty_manuscript.md`.
  - Notes: Canonical title, authors, abstract, categories, v1 submission date, DOI, and code link.
- Source URL: https://arxiv.org/pdf/2606.32032
  - Applies to: `rlmf_uncertainty_manuscript.md`.
  - Notes: Complete 62-page paper supporting method, results, appendices, human study, figures, tables, and limitations. The verified private copy was not deposited.
- Source URL: https://arxiv.org/html/2606.32032
  - Applies to: `rlmf_uncertainty_manuscript.md`.
  - Notes: Public full-paper rendering used to cross-check the archived PDF and extracted source.
- Source URL: https://arxiv.org/e-print/2606.32032
  - Applies to: `rlmf_uncertainty_manuscript.md`.
  - Notes: Public source locator used for equations, captions, prompts, and table reconstruction. The source package was not deposited.
- Source URL: https://doi.org/10.48550/arXiv.2606.32032
  - Applies to: both deposited files.
  - Notes: Stable arXiv-issued DOI.
- Source URL: https://github.com/yale-nlp/RLMF
  - Applies to: implementation and reproducibility analysis in `rlmf_uncertainty_manuscript.md`.
  - Notes: Official MIT-licensed implementation inspected at commit `a087e7a1e49f52aaa701add19cd80699b709fdef` without execution.
- Source URL: https://aclanthology.org/2025.emnlp-main.1505/
  - Applies to: predecessor and baseline context in `rlmf_uncertainty_manuscript.md`.
  - Notes: Primary EMNLP 2025 record for MetaFaith.
- Source URL: https://arxiv.org/abs/2409.12180
  - Applies to: baseline context in `rlmf_uncertainty_manuscript.md`.
  - Notes: Primary paper record for the uncertainty-language fine-tuning baseline called FUT.
- Source URL: https://aclanthology.org/2023.emnlp-main.557/
  - Applies to: sampling-consistency context in `rlmf_uncertainty_manuscript.md`.
  - Notes: Primary EMNLP record for SelfCheckGPT.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence
  - Applies to: cross-DEP synthesis in both deposited files.
  - Notes: Related DEP 1 of exactly 3; statistical confidence and distribution-envelope context.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference
  - Applies to: cross-DEP synthesis in both deposited files.
  - Notes: Related DEP 2 of exactly 3; on-policy feedback-loop and judge-governance context.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260708-ConMax%20Reasoning
  - Applies to: cross-DEP synthesis in both deposited files.
  - Notes: Related DEP 3 of exactly 3; confidence-shaped optimization context.
- Source file: Withheld locally by policy.
  - Applies to: PDF, full-paper HTML, metadata HTML, TeX source, extracted text, figures, and code cache used during review.
  - Notes: No source files, local paths, or private execution metadata were committed.
