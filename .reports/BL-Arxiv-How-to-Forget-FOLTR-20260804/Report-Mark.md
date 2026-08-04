---
title: "Report-Mark - FOLTR Unlearning"
artifact_type: "Black-Lake Arxiv research report"
primary_subject: "How to Forget Clients in Federated Online Learning to Rank?"
source_id: "arXiv:2401.13410v1"
public_date: "2026-08-04"
source_status: "complete local PDF and full-paper HTML verified; source files withheld locally"
---

# Report-Mark - FOLTR Unlearning

## Source Metadata

| Field | Value |
|---|---|
| Title | *How to Forget Clients in Federated Online Learning to Rank?* |
| Authors | Shuyi Wang; Bing Liu; Guido Zuccon |
| arXiv | [arXiv:2401.13410v1](https://arxiv.org/abs/2401.13410) |
| arXiv DOI | [10.48550/arXiv.2401.13410](https://doi.org/10.48550/arXiv.2401.13410) |
| Published venue | ECIR 2024, LNCS 14610, pages 105–121 |
| Publisher DOI | [10.1007/978-3-031-56063-7_7](https://doi.org/10.1007/978-3-031-56063-7_7) |
| Official results repository | [ielab/2024-ECIR-foltr-unlearning](https://github.com/ielab/2024-ECIR-foltr-unlearning) |
| Source integrity | PDF and full-paper HTML passed the local verification gate after one bounded repair; exact local paths are withheld. |
| Redistribution | Source PDF, HTML, metadata, extracted text, and provenance records remain local and were not uploaded. |

## Research Notes

The paper addresses the right to be forgotten in Federated Online Learning to Rank (FOLTR). Clients train locally on queries, documents, and implicit interactions; only model updates are aggregated into a global ranker. The authors propose removing a departing client's historical contribution without retraining the entire global model from scratch.

The method stores periodic local updates. When client `c*` leaves, the remaining clients reduce their local update counts, and stored updates are used to calibrate the new updates by norm scaling before a bounded unlearning run. The paper's main trade-off is explicit: more retained history and more local work can improve the approximation to retraining, while less retained history lowers storage and communication cost.

Verification is performed by asking the target client to introduce a synthetic noisy update and comparing the resulting model impact before and after unlearning. The intended signal is that the target contribution becomes less influential. This is a paper-described verification setup; the public artifact does not reproduce or operationalize an attack.

The empirical study uses four learning-to-rank datasets—MQ2007, MSLR-WEB10k, Yahoo, and Istella-S—with simulated clients and click behavior. The primary metric is offline nDCG@10. Across the displayed settings, unlearning generally approaches the no-target retraining baseline, with effectiveness affected by retained-update interval and the number of local updates retained during unlearning. The evidence is promising but bounded by simulation, an offline metric, a linear ranker, and the paper's distinguishability assumption for the verification client.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Confidence and boundary |
|---|---|---|---|
| E1 | [arXiv abstract and metadata](https://arxiv.org/abs/2401.13410) | Identity, authors, dates, GDPR/FOLTR motivation, unlearning objective, four-dataset study, and ECIR acceptance context | High for identity and abstract-level claims; abstract is not a substitute for full-text evidence |
| E2 | Verified full-paper HTML at [arxiv.org/html/2401.13410](https://arxiv.org/html/2401.13410) | Federated update flow, historical-update storage, norm calibration, unlearning schedule, verification design, experiments, limitations, and conclusion | High for inspected sections; numerical tables were transcribed from the paper and not independently reproduced |
| E3 | Local verified PDF of arXiv:2401.13410 | Page count, layout-sensitive tables, methods/results cross-check, and readable text extraction | High for source-integrity and cross-checking; source file is withheld from this public artifact |
| E4 | [Official results repository README](https://github.com/ielab/2024-ECIR-foltr-unlearning) | Public code/results location and stated release context | Medium; README was inspected but no runnable implementation was verified |
| E5 | [ECIR accepted-papers record](https://www.ecir2024.org/accepted-papers/) and [Springer record](https://doi.org/10.1007/978-3-031-56063-7_7) | Venue and publication context | High for venue metadata |

The distinction between author claims and reviewer synthesis is maintained throughout. The claim that unlearning trends toward retraining is attributed to E2. The recommendation to expose retained-update cost and deletion evidence as first-class audit records is reviewer synthesis grounded in E2 and the related DEP entries below.

## Related DEP Entries

Exactly three existing DEP-E entries were selected for concrete overlap:

| DEP entry | Public path | Relevance reason | Source basis |
|---|---|---|---|
| Agent State Review | [DEP-E-20260708-Agent State Review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md) | Connects unlearning to parameter-level localization and the broader requirement that persistent state be structured and auditable. | Its evidence ledger discusses LACUNA's parameter-localization testbed and separates behavioral success from unresolved state. |
| SMES Expert Sparsity | [DEP-E-20260713-SMES Expert Sparsity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-SMES%20Expert%20Sparsity/smes_expert_sparsity_manuscript.md) | Provides a direct online ranking and serving-cost comparison, including sparse execution, load balancing, and production-evidence limits. | Its detailed summary covers multi-task ranking, routing, latency, offline GAUC, and unverified online causal detail. |
| RPDG Incremental Grad | [DEP-E-20260804-RPDG Incremental Grad](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260804-RPDG%20Incremental%20Grad/rpdg_incremental_gradient_manuscript.md) | Makes cached per-component state and complete cost accounting explicit, which is directly relevant to stored client updates and unlearning overhead. | Its methods and observations distinguish initialization, cached state, update calls, prox work, memory, and privacy exposure. |

## Synthesis Note

### Concept Bridge

The paper's core bridge is between privacy-driven deletion and stateful optimization. FOLTR avoids raw client-data centralization, but the global model still contains accumulated client influence and the unlearning process requires retained update history. The useful DEP-level abstraction is therefore not “delete a record” alone; it is “identify, transform, and verify a bounded state contribution while accounting for the retained state needed to do so.” Agent State Review supplies the auditability lens, SMES supplies the online ranking/runtime lens, and RPDG supplies the cached-state cost lens.

### Potential Implementations

1. **Unlearning ledger:** maintain a signed, privacy-minimized ledger of client update epochs, aggregation membership, retention interval, unlearning request state, and verification outcomes without retaining raw interactions.
2. **Replayable synthetic benchmark:** implement the paper's update schedule on public or synthetic ranking data, with fixed seeds, explicit client partitions, and separate counters for retained-update storage, local steps, communications, and nDCG.
3. **Deletion evidence service:** expose a review-only report that compares the post-unlearning model with a no-target retraining reference and records confidence intervals, version hashes, and known verification assumptions.

### Deeper Relationship Observations

1. The retained-history interval `Δt` is both a statistical approximation knob and a privacy/storage governance decision; it should be treated as a policy variable, not only a hyperparameter.
2. The verification signal is a behavioral proxy for contribution removal, while Agent State Review's parameter-localization thread suggests that future evaluation should combine output behavior with state-local evidence.
3. The paper's reduction in retraining work resembles RPDG's shift from repeated full work to cached incremental updates, but both need a full accounting of initialization, memory, communication, and stale-state risks.

### Conceptual Similarities

1. All four artifacts treat persistent intermediate state as a first-class object: client updates in the paper, agent/parameter state in Agent State Review, routing/runtime state in SMES, and component caches in RPDG.
2. Each uses a compact proxy to control a larger system: calibrated updates for unlearning, structured state traces for review, bounded expert unions for serving, and cached component gradients for optimization.
3. Each separates a headline metric from implementation boundaries: nDCG from deletion assurance, behavior from parameter state, GAUC/latency from fairness and telemetry, and gradient calls from total runtime and memory.

### MVP Implementations with Code Mock-ups

1. **Synthetic contribution ledger**

   ```python
   from dataclasses import dataclass

   @dataclass(frozen=True)
   class UpdateRecord:
       client: str
       round_id: int
       norm: float
       model_hash: str

   def active_records(records, departing_client):
       return [r for r in records if r.client != departing_client]
   ```

   This mock-up only models synthetic metadata. It does not store client examples or implement a deletion guarantee.

2. **Cost-aware unlearning loop**

   ```python
   def run_synthetic_unlearning(rounds, stored, departing, local_steps):
       counters = {"local_steps": 0, "stored_updates": len(stored), "communications": 0}
       for round_id in range(rounds):
           active = [u for u in stored if u["client"] != departing]
           counters["local_steps"] += len(active) * local_steps
           counters["communications"] += len(active)
       return counters
   ```

   The intended test is accounting completeness on synthetic deltas, not deployment.

3. **Benign verification harness**

   ```python
   def compare_reference(unlearned_score, no_target_score, tolerance=0.01):
       gap = abs(unlearned_score - no_target_score)
       return {"gap": gap, "within_tolerance": gap <= tolerance}
   ```

   A real evaluation should use public data, fixed seeds, confidence intervals, and a non-adversarial synthetic perturbation signal.

### Developer Challenges

1. Preserve client-level deletion provenance while minimizing stored state and preventing update-history leakage.
2. Build a reproducible benchmark that counts retained history, local computation, communication, model comparisons, and verification separately.
3. Define safe failure behavior when history is stale, incomplete, compressed, or inconsistent with the model version under review.

### Author Challenges

1. Clarify how the verification protocol generalizes when the departing client is not distinguishable from other clients.
2. Report uncertainty, storage/communication overhead, and wall-clock cost alongside nDCG convergence.
3. Release a pinned, runnable implementation and public reproduction manifest so the method can be independently tested.

## Validation Notes

- Required manuscript-generation skill and its artifact schema were applied before drafting the DEP manuscript.
- Initial source state was partial; the local repair completed the PDF/full-HTML pair before any research synthesis.
- PDF validation: at least 10 KB, `%PDF-` header, trailing `%%EOF`, and readable page/text extraction passed.
- Full-paper HTML validation: at least 5 KB, at least 2,000 post-script/style body characters, article/main/LaTeXML marker, at least two headings, and at least two paper-structure terms passed.
- Duplicate validation: no matching arXiv ID, DOI, normalized title, slug, or recent same-paper marker was found in owning public artifact trees or automation memory.
- Public-output validation: no `.source` directory is created; no source PDF, HTML, archive, cache, extracted source text, local path, or exact local execution timestamp is included.
- The official repository was inspected for context, but no code was executed and no claim of independent reproduction is made.

## Attribution Block

Primary source: Shuyi Wang, Bing Liu, and Guido Zuccon, “How to Forget Clients in Federated Online Learning to Rank?”, arXiv:2401.13410v1, published in ECIR 2024, DOI [10.1007/978-3-031-56063-7_7](https://doi.org/10.1007/978-3-031-56063-7_7). Public source pages: [arXiv abstract](https://arxiv.org/abs/2401.13410), [full-paper HTML](https://arxiv.org/html/2401.13410), [PDF](https://arxiv.org/pdf/2401.13410), and [official results repository](https://github.com/ielab/2024-ECIR-foltr-unlearning). Related DEP paths are linked above. Source files were withheld locally; no source files were uploaded to Black-Lake or Slack.
