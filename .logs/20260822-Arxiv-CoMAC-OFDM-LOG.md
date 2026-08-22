# Arxiv DEP Log: CoMAC OFDM

- Run class: Arxiv DEP / DEP-E research.
- Selected paper: *Computation over Wide-Band MAC: Improved Achievable Rate through Sub-Function Allocation*.
- Authors: Fangzhou Wu, Li Chen, Nan Zhao, Yunfei Chen, F. Richard Yu, and Guo Wei.
- Identity: arXiv:1806.08632v1; arXiv DOI 10.48550/arXiv.1806.08632; related IEEE DOI 10.1109/TWC.2019.2918145.
- Selection status: one identity atomically reserved by the arXiv selection family; source body was opened only after reservation.

## Selection and Deduplication

- Enumeration method: `rg --files -g "*.pdf"` against the local arXiv archive, with each PDF parent directory treated as one paper unit.
- Archive counts: 75,967 PDFs; 75,964 unique parent units; 67,990 unique canonical arXiv identities in the immutable candidate index.
- Eligible set: 59,867 identities after exclusions.
- Random method: `secrets_system_random_from_locked_eligible_set` applied by the family reservation helper; selected identity `arxiv:1806.08632`.
- Exclusion evidence: 6,801 duplicate-identity archive groups; 1,611 existing public identity matches; 1,425 DOI matches; 1,387 same-paper markers within 24 hours. Counts overlap and are not additive.
- Reselection validation: no reselection was needed after the reservation; the selected identity had no intersection with the checked artifact/memory set.
- Dedup surfaces: public `.logs`, `.reports`, `.lake-data`, automation memory, arXiv ID/DOI/title/slug matches, and recent-paper markers.

## Source Integrity and Review

- Initial state: partial. The valid PDF existed, but full-paper HTML was absent.
- Repair: one bounded publisher-brokered single-paper repair fetched the official metadata page and full-paper HTML while preserving the valid PDF.
- Final gate: PDF 848,218 bytes with valid PDF header and EOF marker; full-paper HTML 404,242 bytes with 73,784 body characters, 71 heading markers, 7 paper-structure term classes, and no partial files.
- Source package: unavailable through the archive redirect policy; this did not affect the complete-paper gate.
- Review: full-paper HTML and the local PDF were inspected through the abstract, introduction, model, main results, sub-function allocation, power allocation, simulation, conclusion, and references.

## Generated Public Outputs

- `.logs/20260822-Arxiv-CoMAC-OFDM-LOG.md`
- `.reports/BL-Arxiv-CoMAC-OFDM-20260822/Report-Mark.md`
- `.lake-data/DEP-E/Series 002/DEP-E-20260822-CoMAC OFDM/README.md`
- `.lake-data/DEP-E/Series 002/DEP-E-20260822-CoMAC OFDM/comac_ofdm_manuscript.md`

## Next-review Questions

1. Can the CoMAC-OFDM rate curves and the sponge-squeezing solution be reproduced from a public, version-pinned simulation with the paper's channel and power assumptions?
2. How does the sub-function allocation behave under correlated sub-carrier fading, imperfect CSI, finite blocklength, and unequal node power budgets?
3. What latency, energy, privacy, and robustness tradeoffs appear when the scheme is evaluated on hardware-in-the-loop or authorized radio traces?

## Challenges

1. The source gives theoretical and simulation evidence but no inspected official implementation, seeds, or reproducible experiment bundle.
2. The min-channel-gain bottleneck, integer partitioning, and CSI assumptions complicate fair comparisons with modern AirComp and OFDM baselines.
3. Translating an information-theoretic rate gain into a deployable system requires synchronization, channel estimation, scheduling, and safety controls that the paper does not validate.

## Public-Safety Confirmation

Only generated Markdown artifacts and public source URLs are intended for submission. PDFs, full-paper HTML, metadata HTML, source archives, extracted text, caches, verification receipts, and local archive paths remain withheld locally. No source file is uploaded, staged, committed, attached, or copied into the public repository or Slack.

## Attribution Block

- Source URL: https://arxiv.org/abs/1806.08632
  - Applies to: selection identity, authors, date, abstract, and public metadata.
- Source URL: https://arxiv.org/html/1806.08632
  - Applies to: full-paper method, evidence, simulations, limitations, and references.
- Source URL: https://arxiv.org/pdf/1806.08632
  - Applies to: primary-paper integrity cross-check.
- Source URL: https://doi.org/10.1109/TWC.2019.2918145
  - Applies to: related published-version identifier.
