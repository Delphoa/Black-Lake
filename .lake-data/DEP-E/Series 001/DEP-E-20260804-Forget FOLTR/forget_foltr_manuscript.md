---
title: "FOLTR Unlearning - DEP-E"
generated_at: "2026-08-04 (public date only)"
artifact_type: "DEP-E schema-complete research manuscript"
primary_subject: "How to Forget Clients in Federated Online Learning to Rank?"
source_id: "arXiv:2401.13410v1"
source_status: "complete local PDF and full-paper HTML verified; source files withheld locally"
selection_method: "Uniform draw from eligible local PDF parent units after ownership-tree deduplication"
deduplication_status: "No prior ID, DOI, title, slug, or recent same-paper marker; one partial-source repair; zero reselections after corrected freeze"
---

# FOLTR Unlearning - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Title | *How to Forget Clients in Federated Online Learning to Rank?* |
| Authors | Shuyi Wang; Bing Liu; Guido Zuccon |
| arXiv identifier | [2401.13410v1](https://arxiv.org/abs/2401.13410) |
| DOI | [10.48550/arXiv.2401.13410](https://doi.org/10.48550/arXiv.2401.13410) |
| Published record | ECIR 2024, LNCS 14610, pages 105–121; [publisher DOI](https://doi.org/10.1007/978-3-031-56063-7_7) |
| Official code/results context | [ielab/2024-ECIR-foltr-unlearning](https://github.com/ielab/2024-ECIR-foltr-unlearning) |
| Public source access | [Abstract](https://arxiv.org/abs/2401.13410), [full-paper HTML](https://arxiv.org/html/2401.13410), and [PDF](https://arxiv.org/pdf/2401.13410) |
| Local integrity result | Complete after repair: PDF and full-paper HTML both passed the required checks. |
| Local source policy | PDF, HTML, metadata, extracted text, provenance, and caches are retained locally only; no source files are in this DEP. |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| S1 | [arXiv abstract](https://arxiv.org/abs/2401.13410) | Primary metadata and abstract | Title, authors, date, GDPR/FOLTR motivation, unlearning objective, four-dataset study, and ECIR context | Paper identity and high-level contribution | High | Abstract-level evidence does not establish all method or result details |
| S2 | [Full-paper HTML](https://arxiv.org/html/2401.13410) | Primary full text | FOLTR update flow, stored updates, norm calibration, unlearning schedule, verification setup, datasets, metrics, results, and limitations | Method and evidence claims | High for inspected sections | Tables were read but not independently reproduced |
| S3 | Local verified PDF, source withheld | Primary full text | Layout-sensitive cross-check, 17 pages, readable text extraction, and table verification | Source integrity and cross-checking | High | The source file is intentionally not redistributed |
| S4 | [Official results repository](https://github.com/ielab/2024-ECIR-foltr-unlearning) | Public code/results context | README-level availability and stated release context | Reproducibility context | Medium | No runnable implementation was verified or executed |
| S5 | [ECIR accepted-papers record](https://www.ecir2024.org/accepted-papers/) and [publisher record](https://doi.org/10.1007/978-3-031-56063-7_7) | Venue metadata | Acceptance and published-record context | Publication attribution | High | Venue pages are not evidence for the method itself |
| S6 | [Agent State Review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md), [SMES Expert Sparsity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-SMES%20Expert%20Sparsity/smes_expert_sparsity_manuscript.md), and [RPDG Incremental Grad](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260804-RPDG%20Incremental%20Grad/rpdg_incremental_gradient_manuscript.md) | Related DEP artifacts | State auditability, online ranking/runtime, and cached update/cost-accounting overlap | Cross-DEP synthesis | Medium | Related entries are evidence about their own deposits, not primary evidence for the selected paper |

## Executive Summary

The paper studies how a federated online learning-to-rank system can remove one client's contribution after a right-to-be-forgotten request. In FOLTR, clients keep queries, documents, and implicit interactions locally while contributing model updates to a global ranker. The proposed approach retains periodic local updates, recalibrates updates from the remaining clients, and performs a shorter unlearning run rather than retraining from scratch.

The experiments on MQ2007, MSLR-WEB10k, Yahoo, and Istella-S report that unlearning generally moves effectiveness toward a no-target retraining baseline under the tested simulated-client setup. The central research value is the state transition: stored update history makes deletion cheaper, but also creates a privacy, storage, staleness, and provenance surface that must be measured. The verification procedure is a useful signal for contribution removal, not a universal proof of secure deletion.

## Detailed Summary

### Problem and setting

The paper places the GDPR right to be forgotten inside FOLTR. A central service receives model updates rather than raw client interactions, but the aggregated model still contains the effects of client participation. Removing one client while preserving ranker quality is difficult because the federation learns online and the full update history is not normally replayed from scratch.

### Method

The global ranker is trained through repeated federated aggregation. At a chosen interval `Δt`, clients store local updates. If target client `c*` departs, the remaining clients use fewer local updates during unlearning. Historical updates calibrate current updates through a norm-based rescaling, after which a bounded number of global rounds approximates the model that would have been learned without `c*`. The method trades retained state and extra bookkeeping for reduced retraining work.

### Verification and experiments

The paper tests forgetting by adding a synthetic noisy signal to the target client's local update and comparing the target-influenced model with the post-unlearning behavior. It reports results for ten simulated clients with one target, linear ranking, FPDGD, `T=10,000` global rounds, five local updates in the original setup, stored-update interval values of 5, 10, and 20, and unlearning local-update counts from 1 through 4. The main effectiveness metric is offline nDCG@10 across four datasets and several click-model settings.

Across the reported tables, larger retained unlearning local-update counts generally improve alignment with the no-target retraining baseline, while larger storage intervals reduce retained-update frequency but can weaken the match. For example, in the displayed `Δt=10`, four-local-update setting, the reported MQ2007 scores are 0.513, 0.507, and 0.502 across the three click modes, compared with the no-target baseline values 0.513, 0.516, and 0.515. These numbers show the pattern without implying exact equality or independent reproduction.

### Limitations

The evidence is offline and simulation-based. It uses a linear ranker, one target client, public benchmark datasets, and modeled click behavior rather than a live federated deployment. The verification protocol assumes a target-client perturbation that may be distinguishable from ordinary behavior; the authors qualify whether the same signal generalizes to a normal departing client. The paper does not establish cryptographic erasure, parameter-localization, secure deletion of historical updates, or a universal privacy guarantee. The official public repository was inspected at README level, but a runnable implementation was not verified.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment |
|---|---|---|---|
| A client contribution can be approximately removed from FOLTR without full retraining. | Author method claim | S1, S2 | Supported within the tested simulation and parameter settings; not a universal deletion guarantee. |
| Periodic historical updates can support a shorter unlearning run. | Author method claim | S2 | Directly described in the method; storage and leakage costs require separate accounting. |
| Unlearning effectiveness generally approaches no-target retraining across four datasets. | Author empirical claim | S2, S3 | Supported as a reported paper result; no independent reproduction was performed. |
| A noisy target-client update can provide a behavioral verification signal. | Author evaluation claim | S2 | Useful as a proxy under the paper's assumptions; does not prove parameter-level erasure. |
| Deletion workflows should expose update-history provenance, cost, and residual-state evidence. | Reviewer synthesis | S2, S6 | A reasoned implementation implication, not a direct claim that the authors tested. |

## Methodology

- **Selection:** Enumerated PDFs with `rg --files -g "*.pdf"`, treated each PDF parent directory as one paper unit, sorted units, and sampled uniformly with PowerShell `Get-Random`.
- **Pool:** 75,960 PDFs, 75,957 unique parent units, 3,314 owning artifact/memory files scanned, 1,414 prior unique identifiers, 545 prior-ID exclusions, and 75,412 eligible units.
- **Deduplication:** Scanned owning `.logs`, `.reports`, `.lake-data`, `.staging`, and automation memory for arXiv ID, DOI, normalized title, slug, and recent same-paper markers. The `.lists` mirror was excluded because it is metadata-only and does not establish ownership.
- **Draw:** Corrected frozen-pool zero-based draw index 52,166 selected arXiv:2401.13410; there were zero reselections after the corrected freeze.
- **Source gate:** The selected unit began as partial because the PDF existed while verified full-paper HTML was missing. A bounded local repair completed the pair before review. No abstract-only synthesis was performed.
- **Review:** Read the local verified PDF and full-paper HTML, public arXiv metadata, the official results repository README, ECIR venue records, and exactly three related Black-Lake DEP-E artifacts.
- **Evidence handling:** Primary paper claims are tied to S1–S5. Cross-DEP observations use S6 and are labeled synthesis. Unverified code, unavailable source packages, and production claims are not presented as reproduced evidence.
- **Public-safety handling:** Source files and local provenance remain local. Public artifacts contain only generated Markdown and public URLs.

## Scope, Constraints, and Assumptions

- Scope is the selected arXiv v1 paper and its ECIR publication context.
- The selected paper's reported results are treated as author-reported evidence, not independently reproduced results.
- “Unlearning” is used in the paper's approximate contribution-removal sense; it is not upgraded here to cryptographic deletion or formal privacy certification.
- Offline nDCG@10 and simulated click behavior are not substitutes for live user outcomes, fairness analysis, or legal compliance review.
- The public repository intentionally omits PDF, HTML, source archive, extracted text, caches, local paths, and exact local execution times.
- The optional arXiv source package was unavailable through the bounded brokered request; the complete PDF/full-paper HTML pair was sufficient for this review.

## Observations

- The method's central resource is retained update history, which simultaneously reduces retraining work and enlarges the state that must be governed.
- The storage interval `Δt` should be reported as a joint quality, cost, and retention-policy parameter.
- The paper evaluates contribution removal through model behavior; related DEP evidence suggests complementing this with parameter/state localization and explicit provenance records.
- The unlearning loop is close in spirit to incremental optimization methods that replace repeated full work with cached state, but the cost boundary differs and must be measured directly.

## Considerations

- A production workflow should minimize retained update detail, separate access-controlled provenance from model-serving state, and record versioned deletion outcomes.
- Verification should report confidence intervals, reference-model gaps, and failure states when the target client cannot be distinguished by a benign signal.
- A privacy review must examine whether historical updates can reveal client behavior even when raw interactions never leave the client.
- Ranking quality should be evaluated alongside calibration, subgroup/tail behavior, delayed feedback, and rollback readiness before deployment.

## Strengths

- Addresses a concrete privacy and maintenance problem in a federated online setting.
- Provides a method-level state transition rather than only a conceptual deletion request.
- Evaluates multiple datasets and click-model settings with an explicit retraining reference.
- Makes the trade-off between retained updates, local work, and effectiveness visible.

## Weaknesses

- The evidence is offline and based on simulated clients and click behavior.
- The verification setup may rely on a target-client distinction that does not hold in ordinary use.
- Storage, communication, wall-clock, and residual-state costs are not reported as a complete operational ledger.
- No independently runnable implementation was verified from the public repository context.

## Potential Improvements

- Release a pinned implementation, configuration manifest, seeds, and public reproduction scripts.
- Report confidence intervals, wall-clock time, memory, communication volume, and update-history retention cost.
- Add benign verification tests that do not rely on a uniquely identifiable departing client.
- Evaluate parameter-level localization, update leakage, compression, missing history, and non-IID client behavior.

## Potential Implementations

1. **Synthetic FOLTR replay harness:** public ranking data, fixed client partitions, deterministic seeds, and a complete ledger for local updates, stored history, communication, nDCG, and reference-model gaps.
2. **Deletion provenance service:** versioned request records, model/update membership hashes, access-controlled history metadata, and explicit “verified / inconclusive / blocked” outcomes.
3. **State-aware evaluation dashboard:** a reviewer-facing view combining quality drift, retained-state volume, storage interval, residual contribution proxies, and deletion workflow failures.

## Three Ways to Exercise This Research

1. **Reproduction exercise:** implement the smallest synthetic federated ranker, compare full retraining with the paper's approximate unlearning schedule, and publish a versioned work ledger.
2. **Robustness exercise:** vary client heterogeneity, departing-client indistinguishability, missing historical updates, and retention interval while preserving a benign synthetic verification signal.
3. **Governance exercise:** model the unlearning request as a state machine and test whether each transition has sufficient provenance, access control, cost accounting, and an auditable terminal outcome.

## Example MVP Product

- **Product name:** Forgettable Ranker Lab.
- **Target user:** privacy and ML-systems researchers evaluating federated ranking maintenance.
- **Problem:** compare approximate client unlearning with no-target retraining while keeping cost and evidence visible.
- **Core workflow:** ingest public ranking data; create synthetic clients; train a reference model; request removal; run an unlearning variant; compare quality and benign verification metrics; emit a Markdown/JSON review record.
- **Data requirements:** public query-document features, synthetic implicit interactions, model/update hashes, seeds, and experiment configuration. No private user data.
- **Architecture:** local-only experiment runner, immutable run manifest, synthetic update ledger, reference/unlearned model comparator, and report generator.
- **Success metrics:** nDCG gap to no-target retraining, total local updates, communication count, retained-state bytes, wall-clock time, verification confidence, and zero missing ledger fields.
- **Risk controls:** synthetic data only; no real-client attack testing; bounded runs; explicit incomplete-history outcomes; no public source uploads; review of leakage from stored updates.
- **Limitations:** a benchmark cannot certify legal compliance, cryptographic erasure, or production behavior.

## Related Research and Reading

Exactly three related Black-Lake DEP-E entries were selected:

1. [Agent State Review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md) — parameter-level localization and auditable persistent state.
2. [SMES Expert Sparsity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-SMES%20Expert%20Sparsity/smes_expert_sparsity_manuscript.md) — online ranking, sparse routing, runtime cost, and production evidence boundaries.
3. [RPDG Incremental Grad](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260804-RPDG%20Incremental%20Grad/rpdg_incremental_gradient_manuscript.md) — cached state, incremental updates, and complete cost accounting.

The primary paper's surrounding reading should begin with the [arXiv record](https://arxiv.org/abs/2401.13410), [ECIR accepted-paper listing](https://www.ecir2024.org/accepted-papers/), [Springer publication record](https://doi.org/10.1007/978-3-031-56063-7_7), and [official results repository](https://github.com/ielab/2024-ECIR-foltr-unlearning).

## Source References

1. Wang, Shuyi; Liu, Bing; Zuccon, Guido. *How to Forget Clients in Federated Online Learning to Rank?* [arXiv:2401.13410v1](https://arxiv.org/abs/2401.13410), [full-paper HTML](https://arxiv.org/html/2401.13410), [PDF](https://arxiv.org/pdf/2401.13410), [arXiv DOI](https://doi.org/10.48550/arXiv.2401.13410).
2. Wang, Shuyi; Liu, Bing; Zuccon, Guido. ECIR 2024 publication record, [publisher DOI](https://doi.org/10.1007/978-3-031-56063-7_7).
3. [ECIR 2024 accepted-papers record](https://www.ecir2024.org/accepted-papers/).
4. [Official results repository](https://github.com/ielab/2024-ECIR-foltr-unlearning), README context inspected; no runnable implementation was verified.

## Appendix

### Selection and Deduplication Record

| Item | Result |
|---|---|
| Candidate enumeration | 75,960 PDFs; 75,957 unique parent units |
| Uniform draw | Corrected eligible index 52,166; arXiv:2401.13410v1 |
| Ownership scan | 3,314 files; 1,414 prior unique identifiers; 545 prior-ID unit exclusions |
| Final eligible pool | 75,412 units; 0 incomplete-ID units |
| Reselection validation | 0 reselections after corrected freeze; 0 recent same-paper markers |
| Source state | Initial partial; repaired to complete before review |
| Public source handling | No PDF, HTML, source archive, extracted text, cache, or local path uploaded |

### Source-Integrity Validation

- PDF: 2,375,508 bytes, `%PDF-` header, trailing `%%EOF`, 17 pages.
- Full-paper HTML: 503,162 bytes, 71,491 post-script/style body characters, 37 headings, an article/main/LaTeXML marker, and required structural terms.
- Optional source package: unavailable through the brokered request; no source upload was attempted.

## Attribution Block

This manuscript is a public-safe research synthesis of Shuyi Wang, Bing Liu, and Guido Zuccon, “How to Forget Clients in Federated Online Learning to Rank?”, [arXiv:2401.13410v1](https://arxiv.org/abs/2401.13410), published in ECIR 2024, [DOI 10.1007/978-3-031-56063-7_7](https://doi.org/10.1007/978-3-031-56063-7_7). Source files were withheld locally; no source files were uploaded to Black-Lake or Slack.
