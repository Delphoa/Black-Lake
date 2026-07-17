# Arxiv DEP Job Log: Integrals and Rigidity

## Public-Safe Run Summary

- Deposit date: 2026-07-17
- Selected paper: *Integrals and Rigidity on Manifolds with Nonnegative Ricci Curvature*
- Authors: Zixuan Chen; Guoyi Xu; Shuai Zhang
- arXiv: https://arxiv.org/abs/2602.10393
- arXiv DOI: https://doi.org/10.48550/arXiv.2602.10393
- Source state: initially `partial`; repaired and verified `complete` before review
- Source policy: the PDF, full-paper HTML, metadata HTML, TeX/source archive, verification records, and extraction inputs were retained locally; no source file was copied into the repository or attached to Slack
- Result: public-safe artifacts generated and ready for validated repository submission

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- Paper unit: each unique PDF parent directory
- PDF candidates enumerated: 75,777
- Eligible paper-unit candidates: 75,776
- Random method: uniform PowerShell `Get-Random` index over the complete paper-unit array
- Selected zero-based index: 67,845
- Selected one-based position: 67,846
- Exclusions before acceptance: 0
- Duplicate reselections: 0
- Same-paper markers within the preceding 24 hours: 0

## Dedup Validation

The arXiv ID, arXiv DOI, normalized title, and `integrals-rigidity` slug were checked against Black Lake `.logs`, `.reports`, `.lake-data`, the public dedup staging index, automation memory, relevant Black-Lake-Data search results, and the active worktree. No prior Arxiv DEP log, report, DEP-E deposit, or same-paper marker was found. The first random draw was therefore accepted.

## Source Integrity and Repair

- Initial classification: `partial`, because a valid PDF existed but full-paper HTML was absent
- Repair strategy: one bounded direct-arXiv companion-bundle attempt in a fresh staging target; no credentials; no strategy switch; no retry
- Existing PDF: 308,002 bytes; `%PDF-` header; trailing `%%EOF`; preserved after its hash matched the staged copy
- Full-paper HTML: 952,870 bytes; 137,716 body characters after script/style removal; document marker present; 63 heading/section markers; five paper-structure terms
- Metadata HTML: 39,280 bytes; retained as metadata only and never counted as the paper
- TeX/source archive: 27,139 bytes; retained locally
- Partial files after repair: 0
- Verification result: `complete`; independent integrity gate passed before review

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Hyperbolic Catenaries/hyperbolic_catenaries_manuscript.md` - direct differential-geometric overlap through curvature, rigidity, variational structure, and explicit manifold models.
2. `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md` - methodological overlap through geometry-adapted harmonic analysis, anisotropic scaling, and sharp integral estimates.
3. `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` - analytic overlap through Green functions, divergence identities, geometry-sensitive estimates, and careful boundary/topology handling.

## Output Paths

- `.logs/20260717-Arxiv-integrals-rigidity-LOG.md`
- `.reports/BL-Arxiv-integrals-rigidity-20260717/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260717-Integrals and Rigidity/README.md`
- `.lake-data/DEP-E/DEP-E-20260717-Integrals and Rigidity/integrals_and_rigidity_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Can the exact scalar-curvature integral formula be extended from maximal volume growth to the broader non-parabolic three-manifold setting identified by the authors?
2. Is there a quantitative almost-rigidity theorem converting near-equality in the sharp mean value inequality into measured closeness to a Euclidean ball?
3. Can the level-set topology and weighted-curvature limits be independently reconstructed in a symbolic or formal proof environment with explicit dependency traces?

## Challenges

1. The selected unit initially lacked full-paper HTML, so review had to stop for bounded repair and independent complete-source verification.
2. The paper is proof-dense and its HTML math rendering suppresses notation in plain-text views, requiring formula-aware inspection of the verified local document.
3. The headline Hamilton-pinching application is conditional on dimension three and maximal volume growth; preserving that boundary is essential to avoid overstating the result.

## Known Shortfalls

- The differential-geometric proofs were reconstructed from the complete paper but not formally certified.
- No independent computation or proof-assistant implementation was identified or executed.
- The work is an arXiv v1 preprint; no publisher version or official code repository was identified in focused searches.

## Submission Record

- Repository submission: pending
- Slack notification: pending
- Source-upload gate: to be enforced against the staged file list before commit
- Source files uploaded: none
