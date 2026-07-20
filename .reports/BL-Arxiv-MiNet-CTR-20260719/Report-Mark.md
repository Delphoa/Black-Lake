# Report-Mark: MiNet CTR Transfer

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P07`
- Review date: 2026-07-19
- Review type: source-first cross-domain recommendation and deployment synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *MiNet: Mixed Interest Network for Cross-Domain Click-Through Rate Prediction* |
| Authors | Wentao Ouyang; Xiuwu Zhang; Lei Zhao; Jinmei Luo; Yu Zhang; Heng Zou; Zhaojie Liu; Yanlong Du |
| Stable identifier | arXiv:2008.02974v1 |
| Submission history | Submitted 2020-08-07 |
| DOI | https://doi.org/10.48550/arXiv.2008.02974 |
| Primary record | https://arxiv.org/abs/2008.02974 |
| Full-paper fallback | https://ar5iv.labs.arxiv.org/html/2008.02974 |
| PDF | https://arxiv.org/pdf/2008.02974 |
| Source state | Verified complete after one bounded repair; source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P07` |

## Concise Research Notes

### Problem

Advertising CTR models usually focus on target-domain behavior even when a colocated content service contains abundant signals about the same user's interests. MiNet transfers news-domain evidence to ad CTR prediction while distinguishing persistent and recent behavior.

### Method

MiNet represents long-term cross-domain interest with shared user features, short-term source interest with attention over clicked news, and short-term target interest with attention over clicked ads. Item-level attention selects history relevant to the candidate ad; interest-level attention dynamically scales the three representations. Joint source/target training shares user embeddings and optimizes domain-specific prediction heads.

### Evidence

The private company dataset contains tens of millions of news/ad instances across chronological train, validation, and test days; the Amazon Books-Movies benchmark retains 20,479 shared users. Across company and Amazon tests, MiNet reports the best Table 3 AUC/logloss: 0.7326/0.4784 and 0.7855/0.4254, each marked significant against the best baseline at p<=0.01. Ablations report gains from both attention levels and from combining all three interest types. A two-week production A/B test reports 4.12% relative online CTR improvement over DSTN.

### Limits

Production data are private, the paper predates several modern recommender baselines, online experimental allocation and uncertainty details are sparse, and CTR does not measure user welfare, advertiser value, calibration, privacy, or long-term effects. Attention weights are not causal explanations. The company and Amazon domains behave differently, demonstrating that the usefulness of interest components is context-dependent.

## Evidence and Attribution

| Claim | Source basis | Reviewer qualification |
|---|---|---|
| Three interest representations and two attention levels define MiNet. | Sections 2.2-2.8. | Direct architecture transcription. |
| MiNet reports best AUC/logloss on both datasets. | Table 3. | Source-reported five-run averages; private dataset not independently auditable. |
| Both attention levels outperform either alone. | Section 3.6 and Figure 3. | Ablation supports the combined mechanism inside this setup. |
| Component value differs between company and Amazon data. | Section 3.8 and Figure 5. | Strong warning against universal routing assumptions. |
| Online CTR rises 4.12% versus DSTN. | Section 3.9. | Relative source-reported result; allocation, CI, and downstream outcomes are not detailed. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - preference feedback can improve behavior while requiring balanced quality and drift checks.
2. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - conditional signals need route stability and real-runtime evaluation.
3. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md` - behavioral traces remain privacy-sensitive even when direct content is hidden.

## Synthesis Note

### Concept Bridge

MiNet is a multi-timescale, multi-domain router: it decides how much the candidate ad should rely on profile features, recent news, and recent ads. OViP adds a feedback-loop perspective: model errors and preference signals can shift over time, so the evidence pipeline must be balanced and auditable. DMNN shows why input-dependent routing requires route-stability and latency measurements. XPRINT supplies the privacy boundary: event timing and sequences can reveal behavior even without raw content. The combined engineering target is an offline, privacy-minimized evaluator that tests whether transfer improves calibrated ranking without exposing or overusing behavioral histories.

### Potential Implementations

1. Build a cross-domain ablation harness that compares long-term, source-short-term, target-short-term, and fused models on frozen chronological splits.
2. Add per-domain calibration, route-weight drift, and cold-start dashboards before any production experiment.
3. Create a privacy budget layer that bounds history length, feature retention, identity linkage, and analyst-visible telemetry.

### Deeper Relationship Observations

1. Interest-level attention is conditional computation over behavioral evidence, making routing diagnostics as important as aggregate AUC.
2. Cross-domain transfer can improve sparse target predictions while also expanding the surface for unintended inference and feedback loops.
3. Chronological evaluation is necessary but insufficient; policy, product, and population shifts can alter both relevance and acceptable data use.

### Conceptual Similarities

1. MiNet and OViP both learn from behavior-dependent signals whose distribution changes with the deployed model.
2. MiNet interest weighting and DMNN path selection both assign input-specific importance to alternative representations.
3. MiNet histories and XPRINT traces both show that behavioral sequences can encode sensitive information.

### MVP Implementations with Code Mock-Ups

1. Frozen interest-component ablation:

```python
def variants(profile, source_recent, target_recent):
    return {"long": [profile], "source": [profile, source_recent],
            "target": [profile, target_recent],
            "all": [profile, source_recent, target_recent]}
```

2. Route-drift metric:

```python
def route_drift(reference, current):
    keys = sorted(reference)
    return sum(abs(reference[k] - current[k]) for k in keys) / len(keys)
```

3. Privacy-minimized history window:

```python
def bounded_history(events, allowed_domains, limit=25):
    safe = [e for e in events if e["domain"] in allowed_domains
            and not e.get("direct_identifier")]
    return safe[-limit:]
```

### Developer Challenges

1. Shared identities, feature dictionaries, and timestamps must align across domains without leaking raw identifiers.
2. Offline gains can disappear through training-serving skew, delayed labels, feedback loops, or poorly calibrated scores.
3. Attention telemetry can become sensitive behavioral data and must be aggregated, access-controlled, and retention-bounded.

### Author Challenges

1. Release enough anonymized evidence or synthetic benchmarks to support independent replication.
2. Report online allocation, uncertainty, guardrails, calibration, and longer-term outcomes beyond CTR.
3. Compare against newer sequence, transfer, and multi-domain recommendation methods under equal budgets.

## Validation Notes

- Selection: first draw at 64,910 was source-gate rejected; replacement index 42,352 of 75,777 units accepted. Duplicate exclusions 0; source rejections 1; reselections 1.
- Integrity: valid PDF plus approved ar5iv full-paper fallback; one bounded repair; cache `cached`; no partials.
- Structure: all mandated sections and exactly three items per synthesis category; three syntax-checked Python mock-ups.
- Safety: implementation ideas are offline, privacy-minimized, and non-targeting; no operational ad manipulation is proposed.
- Public-safety: local paths, exact timestamps, timezone labels, user/machine context, and source documents withheld.

## Attribution Block

- https://arxiv.org/abs/2008.02974 - canonical metadata, authorship, abstract, and identifier.
- https://ar5iv.labs.arxiv.org/html/2008.02974 - approved full-paper HTML fallback used for method, results, and references.
- https://arxiv.org/pdf/2008.02974 - validated complete PDF; withheld locally.
- https://doi.org/10.48550/arXiv.2008.02974 - persistent identifier.
- `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - related preference evidence.
- `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - related routing evidence.
- `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md` - related privacy evidence.
- PDF, fallback HTML, metadata, extracted text, and cache files were withheld locally; zero source uploads.
