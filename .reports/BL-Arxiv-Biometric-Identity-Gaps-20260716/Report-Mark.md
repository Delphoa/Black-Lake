# Report-Mark: Biometric Identity Gaps

## Review Status

- Deposit date: 2026-07-16
- Primary work: arXiv:2605.18238v1
- Review mode: source-first, full-paper, public-safe
- Local integrity: initial `partial`; repaired and verified `complete`
- Cache: initial miss; missing-only backfill completed with status `cached`
- Reproduction: allocation, generation, capacity calculations, detectors, and benchmarks were not independently rerun
- Source handling: every source document, image, embedding, model, cache, and extraction remains local; no source file is deposited

## Source Metadata

| Field | Value |
|---|---|
| Title | *Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning* |
| Authors | Yuyang Ji; Yixuan Shen; Anil Jain; Xiaoming Liu; Feng Liu |
| Identifier | arXiv:2605.18238v1 |
| DOI | 10.48550/arXiv.2605.18238 |
| Submitted | 2026-05-18 |
| Subject | Computer Vision and Pattern Recognition (`cs.CV`) |
| Canonical record | https://arxiv.org/abs/2605.18238v1 |
| Full paper | https://arxiv.org/pdf/2605.18238 |
| Official HTML | https://arxiv.org/html/2605.18238 |
| Source package | https://arxiv.org/e-print/2605.18238 |
| Official availability record | https://github.com/VILab-Drexel/VILab.github.io/blob/271cb74f57f5e26e74f0bd62398742a0b4d46487/info.json |

The source unit passed the mandatory complete-paper gate after official arXiv repair. The existing 25-page PDF was preserved; official HTML, metadata HTML, and TeX/source were verified before review. The authors' lab metadata listed empty code and project fields for the paper. No official public dataset, model, code, or executable manifest was identified.

## Concise Research Notes

### Problem

Biometric Identity Provisioning (BIP) asks whether a digital entity can receive a synthetic face identity that a chosen face-recognition system will not match to any enrolled real identity, while remaining distinct from all other provisioned identities and renderable as high-quality face images.

### Formalization

A fixed encoder maps faces to normalized embeddings. Real identities are centroid vectors in gallery `R`. A virtual set `V` is accepted when every virtual-to-real and virtual-to-virtual cosine similarity is below threshold `tau`. These are hard, gallery-relative constraints. New enrollments can invalidate a prior identity, requiring reassessment and revocation.

### Allocation

The proposal starts from a real reference, moves against a weighted centroid of nearby real identities, adds PCA-scaled Gaussian noise, and normalizes. Perturbation `alpha` trades real-gallery distance against face-generation fidelity. Every candidate is checked against the real gallery and accepted virtual set. The hard checks provide the property; the repulsion/PCA mechanism proposes candidates efficiently.

### Geometry and Capacity

With ArcFace ResNet-100 and 360,232 Glint360K identity centroids, the paper reports 95% of PCA variance in 269 of 512 components and effective rank 238.4. A spherical-cap Gilbert-Varshamov calculation at `tau = 0.391` gives an ambient reference near `7.41e10` for the 269-dimensional approximation.

The appendix explicitly warns that this is a capacity-scale approximation, not a rigorous lower bound on the empirical face manifold. A 67-degree cap is not locally small, real identities are demographically clustered, and collision events are dependent. Safety buffers reduce the reference sharply: `tau_safe = 0.360` gives about `1.81e9`, while `0.319` gives about `2.38e7`.

### GapGen

GapGen adapts InstantID/SDXL components using real FFHQ steps and unpaired virtual steps. A frozen ArcFace encoder supplies target embeddings and a round-trip cosine loss. The same encoder therefore defines allocation, trains identity fidelity, and evaluates success. This makes the pipeline internally coherent but model-specific.

### Key Results and Reconciliation

At the primary threshold `tau = 0.391`, Table 1 reports hard-checked embedding results up to 10M. For `alpha = 4`, the 10M cell is 100.00% non-collision and 99.98% inter-class separation. The caption and adjacent prose say 100%/100%, which rounds away a small failure rate in a paper centered on exact non-collision.

Generated-image results are materially different. At 1M BIP+GapGen images, Table 2 reports 98.07% non-collision, 78.36% inter-class separation, FID 56.47, and 88.75% round-trip pass rate. The paper acknowledges this realization gap. Public descriptions must not transfer the embedding hard-check property to every rendered image.

The open-world test compares 1M virtual embeddings with up to 180K held-out WebFace4M identities and reports a stable near-zero collision rate at the default setting. v-LFW mirrors 5,749 LFW identities and 13,233 images; BIP+IAPCT reports R-R accuracy 99.80%, V-V 99.18%, R-V FAR 0.01%, detection AUC 98.13%, and unified accuracy 99.20%. Five detectors report 87.76%-99.57% accuracy on BIP images.

### Evidence Boundaries

- “Zero observed collision” applies to specified vectors, galleries, thresholds, and comparisons; it is not zero possible collision.
- The held-out gallery is useful but does not cover all demographics, sites, devices, ages, future enrollments, model updates, or attacks.
- FID is not evidence of consent, uniqueness, likeness rights, demographic fairness, or identity stability.
- Deepfake detection results do not establish universal detectability or adaptive-attack resistance.
- A finite gallery and one encoder cannot prove that a generated face resembles no real person.
- The authors' statement that gallery access mitigates misuse underestimates partial-gallery, query, weak-matcher, KYC, Sybil, and enrollment-abuse scenarios.

### Governance Assessment

The necessity question comes first. Digital entities can use cryptographic credentials, signed display badges, explicit machine marks, and non-human avatars without entering human biometric identity space. A realistic human face can cause anthropomorphic deception and increase surveillance or identity-fraud surface.

If a justified study proceeds, the visual identity should be treated as a revocable, versioned credential. The policy bundle must include encoder, alignment, gallery, threshold, generator, detector, exact-check logic, disclosure, rights basis, expiry, incident response, and human approval. A change to any component invalidates prior assurance.

## Evidence and Attribution

| Evidence | Source basis | Use | Qualification |
|---|---|---|---|
| BIP definition and hard checks | PDF/HTML/TeX Sections 3.1-3.2 | Method reconstruction | Fixed encoder/gallery/threshold only |
| PCA and capacity | Main geometry section and Appendix C | Headroom analysis | Spherical submanifold approximation, not empirical-manifold proof |
| GapGen curriculum | Section 3.3 and Appendix D | Realization mechanism | No code/weights/run |
| 10M embeddings and 1M images | Tables 1-2 | Scale and realization assessment | Source-reported; table/text discrepancy retained |
| Open-world test | Figure 5 and Appendix C.7 | Held-out collision evidence | One held-out source and model pipeline |
| v-LFW and detectors | Table 3 and Appendix E | Recognition/detection assessment | Generator/protocol specificity; no adaptive test |
| Ethics and limitations | Conclusion and Appendix A | Governance review | Reviewer adds threats not fully addressed by authors |
| Availability | Pinned author-lab metadata | Reproducibility status | Time-bounded absence of links |
| Selection/integrity/cache | Public-safe process records | Provenance | Local paths and source bytes withheld |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md`
   - Relevance: forensic scores require fixed denominators, parser/failure accounting, calibration, aggregation analysis, and human review.
   - Source basis: its Evidence Ledger, error/calibration analysis, omitted-output warning, and hybrid forensic-semantic recommendation.
2. `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
   - Relevance: representation diversity can hide minority failures, and inherited data imbalance requires explicit evaluation and live monitoring.
   - Source basis: its diversity regularizer, imbalanced-MNLI result, limitations, and adapter bias review guidance.
3. `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`
   - Relevance: runtime state, independent safety queries, fallback, and falsification map naturally to gallery updates, collision reassessment, revocation, and red teaming.
   - Source basis: its MDP monitor, controller switching, global/local falsification, and weak-fallback limitation.

## Synthesis Note

### Concept Bridge

BIP turns identity assignment into an explicit state-and-threshold problem. Document Fraud LLM shows that detection evidence fails when denominators, missing outputs, calibration, or aggregation are ambiguous. BA-LoRA shows that aggregate diversity and accuracy can conceal inherited imbalance and minority collapse. Mosaic shows how model state can drive an independent query, a fallback decision, and offline counterexample search.

The combined lifecycle is:

`necessity -> rights/data -> allocation -> realization -> exact audit -> disclosure -> monitoring -> revocation -> falsification`.

The lifecycle fails closed. A face is not generated merely because embedding capacity exists. A generated image is not assigned merely because its target vector passed. A detector score is not a safety certificate. A prior pass expires when gallery, threshold, encoder, generator, or policy changes.

### Potential Implementations

1. Build a synthetic-only collision and revocation simulator that compares exact and approximate search, preserves every failure in the denominator, and measures workload as galleries and thresholds change.
2. Build a public-safe identity lifecycle ledger containing version hashes, disclosure, rights review, audit results, expiry, revocation, and human approval without storing faces or biometric embeddings.
3. Build a biometric necessity and misuse gate that compares non-biometric alternatives and blocks work lacking consent, subgroup, resemblance, Sybil/KYC, detector, red-team, incident, and deletion evidence.

### Deeper Relationship Observations

1. BIP's image-level realization gap resembles Document Fraud LLM's patch-to-image aggregation gap: a locally successful representation can fail after the downstream transformation that actually reaches deployment.
2. PCA-aligned diversity resembles BA-LoRA's representation-diversity objective, but neither aggregate spread guarantees minority coverage; demographic density must be measured explicitly.
3. Gallery-relative identity is a Mosaic-style monitored state, not a permanent object: new enrollments change the query result and can trigger a fallback/revocation path whose quality must itself be audited.

### Conceptual Similarities

1. All four artifacts turn hidden model behavior into explicit evidence fields: similarities, detector scores, representation statistics, or abstract safety state.
2. All four require fixed denominators and visible failure states; dropping failed generations, parser errors, minority cases, or weak fallbacks inflates assurance.
3. All four separate a model's primary function from an independent review layer, while warning that the review layer inherits its own data and model limitations.

### MVP Implementations with Code Mock-ups

1. **Fixed-denominator audit record**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class AuditCounts:
    submitted: int
    passed: int
    failed: int
    unresolved: int

def validate_counts(counts):
    total = counts.passed + counts.failed + counts.unresolved
    return {
        "passed": total == counts.submitted and counts.unresolved == 0,
        "accounted": total,
        "submitted": counts.submitted,
    }
```

This defensive primitive prevents “successful outputs only” reporting. It stores counts, not biometric content.

2. **Version invalidation gate**

```python
POLICY_FIELDS = (
    "encoder",
    "alignment",
    "gallery",
    "threshold",
    "generator",
    "detector",
)

def requires_reaudit(previous, current):
    changed = [key for key in POLICY_FIELDS if previous.get(key) != current.get(key)]
    return {"requires_reaudit": bool(changed), "changed_fields": changed}
```

Any material policy change invalidates the prior result instead of silently inheriting it.

3. **Necessity evidence gate**

```python
REQUIRED = {
    "authorized_purpose",
    "non_biometric_alternatives",
    "rights_review",
    "subgroup_plan",
    "misuse_review",
    "revocation_plan",
    "human_approval",
}

def necessity_gate(evidence):
    missing = sorted(REQUIRED.difference(evidence))
    return {"passed": not missing, "missing": missing}
```

This gate does not generate or compare identities; it blocks progression when governance evidence is incomplete.

### Developer Challenges

1. Preserve exact denominators and version lineage across allocation, rendering, re-encoding, detector, gallery-update, and revocation stages without storing sensitive biometric material in public logs.
2. Validate approximate-neighbor search against exact synthetic ground truth and make every missed candidate a hard failure, not a performance tradeoff hidden in aggregate metrics.
3. Build disclosure, expiry, revocation, appeal, and deletion workflows that remain usable when encoders, thresholds, generators, or organizational owners change.

### Author Challenges

1. Release a licensed implementation, synthetic fixtures, manifests, seeds, model cards, and commands that reproduce every table while correcting the 10M 100%/99.98% text inconsistency.
2. Evaluate allocation and realized images across independent encoders, identity-disjoint datasets, demographics, sites, devices, time, approximate-index recall, and adaptive attacks with exact failure counts.
3. Expand the ethics analysis through independent biometric-rights, consent, likeness, anthropomorphic-deception, surveillance, Sybil/KYC, child-safety, accessibility, and non-biometric-alternative review.

## Validation Notes

- Manuscript contract: required YAML, H1, metadata, ledger, summaries, claims, methodology, scope, observations, considerations, strengths, weaknesses, improvements, implementations, exercises, MVP, reading, references, and appendix are present.
- Title contract: YAML title and manuscript H1 are identical and contain no more than 40 characters.
- Selection contract: 75,777 PDFs, 75,776 units, uniform index 28,438, first draw, zero exclusions, zero reselections.
- Integrity contract: valid PDF, official full-paper HTML, metadata, source package, zero partials, final `complete`.
- Cache contract: preflight and missing-only extraction recorded; miss became `cached`.
- Dedup contract: ID, DOI, normalized title, slug, artifacts, memory, companion repository, and recent markers checked.
- Related-entry contract: exactly three related DEP entries inspected and attributed.
- Synthesis contract: exactly three potential implementations, deeper observations, conceptual similarities, MVP mock-ups, developer challenges, and author challenges.
- Code validation: all three Python mock-ups are standard-library/pure-data governance examples with no biometric, model, network, or filesystem operations.
- Safety contract: no face generation, embedding allocation, identity-evasion procedure, gallery, model weight, or source file is deposited.
- Public-safety contract: no local path, drive, username, host, local timezone, or exact execution timestamp appears.

## Attribution Block

- Primary metadata: https://arxiv.org/abs/2605.18238v1
- Primary full-paper PDF, inspected locally and withheld: https://arxiv.org/pdf/2605.18238
- Official full-paper HTML, inspected locally and withheld: https://arxiv.org/html/2605.18238
- Primary TeX/source package, inspected locally and withheld: https://arxiv.org/e-print/2605.18238
- Canonical DOI: https://doi.org/10.48550/arXiv.2605.18238
- Authors' lab availability metadata: https://github.com/VILab-Drexel/VILab.github.io/blob/271cb74f57f5e26e74f0bd62398742a0b4d46487/info.json
- Related Document Fraud LLM DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md
- Related BA-LoRA Bias DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-BA-LoRA%20Bias/ba-lora-bias-manuscript.md
- Related Mosaic Safety DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Mosaic%20Safety/mosaic_safety_manuscript.md
- Source-file statement: PDF, HTML, metadata, TeX/source, figures, faces, embeddings, galleries, models, code, cache, and extracted text were withheld locally; none were uploaded.
