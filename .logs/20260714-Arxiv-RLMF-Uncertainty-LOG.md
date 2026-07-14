# Black Lake Arxiv DEP Log: RLMF Uncertainty

## Run Summary

- `Date`: 2026-07-14
- `Selection mode`: User-directed paper selection; random selection was not used.
- `Selected paper`: Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs.
- `Identifier`: arXiv:2606.32032v1; DOI 10.48550/arXiv.2606.32032.
- `Authors`: Gabrielle Kaili-May Liu; Avi Caciularu; Gal Yona; Idan Szpektor; Arman Cohan.
- `Primary record`: https://arxiv.org/abs/2606.32032
- `Official code`: https://github.com/yale-nlp/RLMF at commit `a087e7a1e49f52aaa701add19cd80699b709fdef`.
- `Source-file policy`: Private source artifacts were inspected and retained locally; none were copied into the public repository.

## Eligibility and Dedup

The paper was eligible because the user explicitly selected it and no substantive same-paper DEP, report, or log was found in the Black Lake repository. A related repository contains author-inventory pointers to this title; those pointers are not research deposits and did not block review. The private DEP-A review ledger likewise contained no completed record for arXiv:2606.32032 before this run.

Dedup keys checked:

- arXiv base ID `2606.32032`
- arXiv version ID `2606.32032v1`
- DOI `10.48550/arXiv.2606.32032`
- normalized full title
- slug `RLMF-Uncertainty`

## Source Integrity

- The archived PDF is 62 pages, parses successfully, begins with a valid PDF header, and ends with the expected end marker.
- Full-paper HTML contains the introduction, method, experimental setup, results, conclusion, references, and appendices rather than only an abstract page.
- TeX source exposes equations, complete tables, prompts, figure captions, human-study instructions, and appendix details.
- PDF, HTML, and source extraction all completed successfully. A missing optional external text utility did not affect extraction because the available PDF parser succeeded.
- The official code repository was inspected through a shallow blob-filtered checkout, limiting private disk use while pinning the implementation version.

## Evidence Reviewed

The review covered the two-stage RLMF pipeline; faithful versus factual calibration; sampled-response intrinsic-confidence estimation; `F_gold`, `F_pred`, and `Z_g`; piecewise advantage scaling; metacognitive data selection; numerical-to-linguistic rewriting; cMFG-star; all main result tables; training-task robustness; reward, prompt, data-size, scaling, threshold, and rewriting ablations; smaller-model results; human evaluation; ethics and limitations; and the official trainer, reward, configuration, requirements, and reproduction instructions.

External primary context included MetaFaith, FUT, SelfCheckGPT, semantic uncertainty, and the official RLMF code. Exactly three existing Black Lake records were used in the synthesis: PAC Confidence, OViP Preference, and ConMax Reasoning.

## Outputs

- `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/README.md`
- `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md`
- `.reports/BL-Arxiv-RLMF-Uncertainty-20260714/Report-Mark.md`
- `.lake-data/DEP-A/DEP-A-20260714-RLMF Uncertainty/README.md`
- `.lake-data/DEP-A/DEP-A-20260714-RLMF Uncertainty/2606.32032-whitepaper-review.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication entry
- `.lake-data/DEP-A/.index/pubs-index.md` publication entry
- `.staging/arxiv-dep-dedup-index.json` public dedup pointer
- Private canonical whitepaper review, validation records, and completed ledger entry retained outside the public repository

## Review Findings

The central result is promising but narrower than broad “metacognitive awareness.” RLMF improves a model's ability to predict and express alignment to a sampled-consistency proxy for intrinsic confidence. The proxy depends on generation settings and Qwen3-32B judgments; it is not direct access to a latent belief state.

The paper reports average cMFG-star of 0.84 for Llama3.1-8B-Instruct and 0.83 for Qwen3-8B after RLMF, with 0.82 and 0.83 after linguistic rewriting. Human experts prefer rewritten RLMF outputs over FUT on all four rated linguistic dimensions. These remain author-reported outcomes: training and evaluation were not rerun, main tables lack multi-seed uncertainty, and the documented workflow selects checkpoints using in-domain test faithful calibration.

Static code inspection confirms the intended piecewise scaling. A minor boundary mismatch exists between the paper's strict `< tau` equation and the code's inclusive `<= mc_threshold` comparison.

The source tables also contain an unresolved numeric mismatch: Qwen3-8B random-selection accuracy is 0.23 in the compact table and 0.53 in the full appendix table, while the row's cMFG-star and Brier values agree.

## Validation Status

- Full-paper source gate: passed.
- Same-paper substantive dedup gate: passed.
- Manuscript required-section and exact-title checks: scheduled before commit.
- Whitepaper validator and quality rubric: scheduled before commit.
- Public-safe path, source-file, secret, and timestamp scan: scheduled before commit.
- Git allowlist and staged-diff review: scheduled before commit.
- Experiment reproduction: not performed and not claimed.

## Next-Reviewer Questions

1. Do the RLMF gains persist when intrinsic confidence is estimated with a different judge, semantic entropy, or model logits rather than Qwen3-32B consistency alone?
2. How much of the reported improvement survives five or more training seeds with checkpoint selection moved to a separate validation split?
3. Does contextual hedge rewriting improve calibrated human reliance without changing factual claims or making uncertain answers more persuasive?

## Next-Pass Challenges

1. Reproduce a small open-model configuration with strict train/validation/test separation and seed-level aggregate reporting.
2. Build a cross-proxy matrix that trains on one confidence estimator and evaluates faithful calibration against at least two independent estimators plus correctness.
3. Add an automated and human semantic-preservation audit for Stage 2 rewriting, including seeded entity, value, negation, and scope mutations.

## Source References

- https://arxiv.org/abs/2606.32032
- https://arxiv.org/html/2606.32032
- https://arxiv.org/pdf/2606.32032
- https://arxiv.org/e-print/2606.32032
- https://doi.org/10.48550/arXiv.2606.32032
- https://github.com/yale-nlp/RLMF
- https://aclanthology.org/2025.emnlp-main.1505/
- https://arxiv.org/abs/2409.12180
