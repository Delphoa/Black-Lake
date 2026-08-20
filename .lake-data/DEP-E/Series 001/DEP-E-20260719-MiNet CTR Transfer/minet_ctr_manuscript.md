---
title: "Mixed-Interest CTR Transfer"
generated_at: "2026-07-19 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of cross-domain CTR prediction using long- and short-term interest attention."
source_status: "verified complete local PDF, approved ar5iv full-paper HTML, and official metadata inspected; all sources withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/2008.02974"
stable_identifier: "arXiv:2008.02974v1; DOI:10.48550/arXiv.2008.02974"
deployment_job_id: "BLAD-2200-20260719-7D93E819"
deployment_item_id: "BLAD-2200-20260719-7D93E819-P07"
confidence_summary: "High for identity, architecture, table transcription, and stated deployment result; medium for transferability; low for causal, privacy, and long-term claims."
safety_scope: "offline recommender evaluation, privacy minimization, calibration, route-drift review, and human-governed experiments"
distribution_notes: "No PDF, HTML, metadata, extracted text, behavioral data, cache, local path, or source document is redistributed."
---

# Mixed-Interest CTR Transfer

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2008.02974v1 | https://arxiv.org/abs/2008.02974 | Metadata only. | 2026-07-19 | Inspected. |
| S2 | Approved ar5iv rendering | Primary paper | HTML | arXiv:2008.02974v1 | https://ar5iv.labs.arxiv.org/html/2008.02974 | Verified fallback copy withheld. | 2026-07-19 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2008.02974v1 | https://arxiv.org/pdf/2008.02974 | Verified local copy withheld. | 2026-07-19 | Inspected through extraction. |
| S4 | arXiv-issued DOI | Identity | DOI | 10.48550/arXiv.2008.02974 | https://doi.org/10.48550/arXiv.2008.02974 | Persistent locator. | 2026-07-19 | Resolved. |
| S5 | OViP Preference DEP | Related | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S6 | DMNN Conditional Paths DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S7 | XPRINT Traffic Privacy DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S8 | Selection, rejection, repair, and cache | Process evidence | Private records | `BLAD-2200-20260719-7D93E819-P07` | Local paths withheld | Integrity, dedup, and locality only. | 2026-07-19 | Verified. |

Authors: Wentao Ouyang, Xiuwu Zhang, Lei Zhao, Jinmei Luo, Yu Zhang, Heng Zou, Zhaojie Liu, and Yanlong Du. Submitted 2020-08-07. Deployment job `BLAD-2200-20260719-7D93E819`; item `BLAD-2200-20260719-7D93E819-P07`.

## Evidence Ledger

| Evidence ID | Source | Claim or observation | Type | Confidence | Limits |
|---|---|---|---|---|---|
| E1 | S2, section 2 | MiNet models three interest types with item- and interest-level attention. | Direct method. | High | No independent reproduction. |
| E2 | S2, Table 2 | Company and Amazon datasets use chronological splits and distinct domains. | Dataset design. | High transcription. | Company data private; Amazon labels derive from ratings. |
| E3 | S2, Table 3 | MiNet reports company AUC/logloss 0.7326/0.4784 and Amazon 0.7855/0.4254. | Comparative result. | High transcription; medium generalization. | Source-reported five-run averages. |
| E4 | S2, sections 3.6-3.8 | Both attention levels and all three interest types report best results; component importance differs by dataset. | Ablation. | Medium-high. | Figures lack full uncertainty reporting. |
| E5 | S2, section 3.9 | Two-week A/B test reports 4.12% relative CTR lift versus DSTN. | Production result. | Medium. | Sparse allocation, CI, guardrail, and long-term detail. |
| E6 | S5-S7 | Feedback, conditional routing, and behavioral privacy extend the deployment analysis. | Reviewer synthesis. | Medium | Cross-paper bridge. |

## Executive Summary

MiNet transfers behavioral evidence from a news domain into ad CTR prediction by modeling long-term cross-domain interest, recent source-domain clicks, and recent target-domain clicks. Candidate-conditioned item attention filters histories, and a second attention layer weights the three interest representations. The paper reports the strongest AUC/logloss among listed baselines on private company and Amazon benchmarks plus a 4.12% relative CTR lift in a production A/B test. These results support the architecture's relevance but do not close calibration, welfare, privacy, reproducibility, or long-term feedback questions.

## Detailed Summary

The shared long-term representation concatenates user feature embeddings learned jointly from source and target tasks. Source short-term interest aggregates clicked news after projecting target-ad information across feature spaces; target short-term interest aggregates clicked ads directly. Both item attentions depend on history item, target ad, user, and pairwise interaction. Interest-level attention then scales long-term, source-short-term, and target-short-term vectors before target prediction.

The company experiment uses six consecutive days for initial training, the next for validation, and the following day for testing; Amazon holds out each user's last and second-last target ratings for test and validation. Models run five times. Table 3 reports significant improvements over the best baseline at p<=0.01. Attention/component ablations show that source-versus-target usefulness changes materially between advertising and e-commerce.

The production section describes a two-week test against DSTN and a 4.12% relative CTR increase. It does not provide a full experiment card, confidence interval, sample allocation, novelty effects, revenue/user-welfare guardrails, or long-term retention outcomes. Reviewer interpretation therefore treats it as encouraging operational evidence rather than a portable effect size.

## Key Claims and Evidence

1. **Cross-domain mixture:** Sections 2.2-2.9 directly support the three-component architecture.
2. **Offline ranking gain:** Table 3 supports best listed AUC/logloss on both datasets within the paper's setup.
3. **Hierarchical attention contribution:** Section 3.6 reports the combined attention configuration as best.
4. **Context-dependent interest:** Section 3.8 shows short-term signals dominate company data while long-term interest is stronger on Amazon.
5. **Online lift:** Section 3.9 reports 4.12% relative CTR improvement; missing experimental detail limits causal portability.

## Methodology

The paper defines source and target CTR losses with shared user embeddings, candidate-aware history attention, interest-level scaling, and jointly weighted domain objectives. Evaluation uses AUC, relative AUC improvement, and logloss on chronological splits, five repeated runs, baseline comparison, mechanism ablations, attention inspection, and a production A/B test.

The review inspected canonical metadata, validated PDF, complete fallback HTML, tables, formulas, deployment section, and exactly three related DEP entries. The first randomly drawn unit failed the complete-source gate and was privately rejected; the replacement passed. Repository, memory, companion-repository, ID, DOI, title, slug, 24-hour, and current-job dedup checks found no accepted-paper collision.

## Scope, Constraints, and Assumptions

- CTR is a ranking/engagement proxy, not a welfare or causal-value measure.
- Company data and production details are not independently accessible.
- Amazon ratings are transformed into click-like labels and differ from advertising clicks.
- Attention weights are diagnostic signals, not causal explanations of preference.
- Cross-domain identity linkage requires lawful purpose, consent, minimization, and governance.
- Related DEP connections are reviewer synthesis.

## Observations

- Candidate-conditioned history filtering is more defensible than undifferentiated sequence pooling.
- Exponential interest weights may compensate for representation dimension differences but can amplify instability.
- The dataset-dependent ablation is more informative than a single aggregate leaderboard.
- Chronological splits reduce one leakage mode while leaving policy and population shift open.
- Production telemetry should minimize identities and event sequences.

## Considerations

- Measure calibration and ranking by domain, cohort, history length, and cold-start status.
- Bound identity linkage, feature use, retention, and analyst access.
- Monitor route weights and component contribution under shift.
- Pair CTR with user-experience, advertiser-value, fairness, and safety guardrails.
- Require a preregistered experiment card before production promotion.

## Strengths

- Clear decomposition of long- and short-term signals.
- Candidate-aware attention at two levels.
- Chronological evaluation on private and public-style domains.
- Useful mechanism ablations and online evidence.
- Explicit demonstration that component importance changes by domain.

## Weaknesses

- Private primary dataset and sparse reproducibility detail.
- Older baseline set.
- No comprehensive calibration, fairness, privacy, or welfare analysis.
- Limited statistical details for figures and A/B test.
- CTR-only online outcome.

## Potential Improvements

- Publish an anonymized/synthetic cross-domain benchmark and experiment card.
- Add calibration, uncertainty, fairness, privacy, and long-term metrics.
- Compare against newer sequential and multi-domain recommenders.
- Measure route stability and attention saturation.
- Evaluate consent- and purpose-limited feature subsets.
- Report A/B allocation, intervals, guardrails, and follow-up duration.

## Potential Implementations

Begin with a non-serving ablation harness on consented, de-identified data. Freeze chronological splits, compare each interest component, evaluate calibration and cold start, and retain only aggregate route diagnostics. No production targeting should occur until privacy, security, experiment, fairness, and product reviews approve a bounded shadow test.

## Three Ways to Exercise This Research

1. **Component replay:** Compare four interest variants on frozen chronological splits and report AUC, logloss, calibration, and subgroup slices.
2. **Shift stress:** Change source activity, history length, and domain mix; measure route-weight drift and target calibration.
3. **Privacy minimization:** Remove identifiers and shorten histories incrementally; chart utility versus privacy exposure.

## Example MVP Product

**InterestMix Audit** is an offline evaluation console. It accepts de-identified feature fixtures and frozen predictions, compares component ablations, tracks calibration and route drift, and exports an aggregate evidence manifest. It stores no raw content, direct identifiers, or individual browsing sequences and cannot serve ads.

## Related Research and Reading

1. **OViP Preference:** behavior-dependent feedback needs balanced quality and drift evidence.
2. **DMNN Conditional Paths:** input-dependent routing should be evaluated for stability and real runtime.
3. **XPRINT Traffic Privacy:** event sequences and timing can remain sensitive even without content.

## Source References

1. Wentao Ouyang et al., *MiNet: Mixed Interest Network for Cross-Domain Click-Through Rate Prediction*, https://arxiv.org/abs/2008.02974
2. Approved full-paper fallback, https://ar5iv.labs.arxiv.org/html/2008.02974
3. Official PDF, https://arxiv.org/pdf/2008.02974
4. Persistent DOI, https://doi.org/10.48550/arXiv.2008.02974
5. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
6. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md`
7. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md`

## Appendix

- Title and H1 are identical and within 40 characters.
- Required manuscript sections are present.
- First-draw rejection and replacement outcomes are recorded.
- Source-integrity thresholds passed before review.
- Exactly three related DEP entries are used.
- Zero source files, private paths, exact timestamps, or timezone labels are published.
