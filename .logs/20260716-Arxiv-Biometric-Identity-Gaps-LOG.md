# Arxiv DEP Job Log: Biometric Identity Gaps

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2605.18238v1, *Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning*
- Selection result: accepted on the first uniform draw
- Source-integrity result: initial `partial`, repaired to verified `complete`
- Source-file policy: PDF, official full-paper HTML, metadata HTML, TeX/source, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- PDF count: 75,777
- Unique parent-paper units: 75,776
- Sampling method: PowerShell `Get-Random` over the complete sorted unique parent-unit list
- Zero-based selected index: 28,438
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, companion-repository DEP, or same-paper marker from the preceding 24 hours was found. Exact-title and identifier searches of the related public repository found no research deposit. The first draw was accepted.

## Source Integrity and Cache

- Existing PDF: 8,894,821 bytes, 25 pages, `%PDF-` header and trailing `%%EOF` present
- Initial full-paper HTML: missing
- Repair: official arXiv full-paper HTML, metadata HTML, and TeX/source archive completed with bounded requests
- Verified HTML: 658,614 bytes, 109,692 body characters, 49 headings, six structure terms, and a document marker
- Metadata HTML: 44,131 bytes; abstract/metadata only
- Source archive: 8,262,552 bytes, 24 entries
- Remaining partial files: 0
- Cache: 1.4-second missing-only backfill via `pypdf`, `html-regex`, and `tarfile`
- Cache outputs: PDF text 84,547 bytes; HTML text 112,658 bytes; source text 152,886 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - connects forensic detection, fixed-denominator evaluation, calibration, hybrid evidence, and human review.
2. `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` - connects inherited bias, representation diversity, minority-group evaluation, and deployment monitoring.
3. `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md` - connects runtime monitoring, independent safety queries, fallback/revocation policy, and offline falsification.

## Output Paths

- Job log: `.logs/20260716-Arxiv-Biometric-Identity-Gaps-LOG.md`
- Phase log: `.logs/20260716-Arxiv-Biometric-Identity-Gaps-PHASE-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-Biometric-Identity-Gaps-20260716/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260716-Biometric Identity Gaps/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260716-Biometric Identity Gaps/biometric_identity_gaps_manuscript.md`
- Publication index: `.lake-data/DEP-E/.index/pubs-index.md`
- Dedup pointer: `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How do gallery collision, image-level identity fidelity, and revocation rates change across independent encoders, sites, demographics, capture conditions, and longitudinal enrollment drift?
2. Can the capacity and open-world claims be reproduced with audited identity-disjoint datasets, dependence-aware uncertainty, exact nearest-neighbor checks, and preregistered thresholds?
3. What governance prevents provisioned faces from enabling Sybil identities, KYC evasion, anthropomorphic deception, surveillance expansion, or unconsented resemblance outside the finite gallery and chosen encoder?

## Challenges

1. The paper uses “non-colliding” for both hard-checked embeddings and generated images even though the 1M image results report 98.07% non-collision and 78.36% inter-class separation.
2. A text claim of 100%/100% at 10M and the table caption conflict with the displayed 100.00%/99.98% result at the primary threshold and perturbation setting.
3. The guarantee is gallery-, encoder-, threshold-, and time-relative, while the proposed use concerns persistent identities in an open world with sensitive biometric and misuse risks.

## Known Shortfalls

- No official code, project page, dataset release, model weights, or executable environment was identified in the paper or the authors' lab metadata; no experiment was rerun.
- The spherical submanifold capacity calculation is an acknowledged headroom approximation, not a rigorous capacity bound for the empirical face manifold.
- Open-world testing uses one held-out source and does not establish demographic, site, device, attack, or longitudinal robustness.
- Deepfake-detector accuracy and an in-family detector do not establish universal detectability, fairness, or resistance to adaptive evasion.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/50e88f2c5a4338e5aae1c9d55d71a728be55b813
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784205075516389
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source or biometric artifacts
- Submission status: direct default-branch push succeeded; Slack notice delivered
