# Black Lake Arxiv DEP Log: Spectrum Occupancy ML

## Selection and Source Gate

- Review date: 2026-08-20. Exact local execution time and local environment details are withheld.
- Selection method: enumerate PDFs with `rg --files -g "*.pdf"`, collapse each PDF parent directory to one paper unit, sort units, and draw one uniform zero-based index with PowerShell `Get-Random`.
- Candidate counts: 75,967 PDFs and 75,964 unique parent-directory paper units.
- Draw: zero-based index 10,451; selected arXiv:1503.07104, *Analysis of Spectrum Occupancy Using Machine Learning Algorithms*.
- Dedup validation: arXiv ID, DOI, normalized title, slug, prior Arxiv DEP artifacts, automation memory, and same-paper-within-24-hours markers were checked across the public artifact areas and related inventory. No match was found.
- Exclusion counts: 0 duplicate exclusions, 0 other exclusions, 0 same-paper-within-24-hours markers, and 0 reselections.
- Initial source state: partial. The PDF was present and passed the basic header/EOF check, but full-paper HTML was missing.
- Repair: one bounded brokered single-paper repair preserved the valid PDF and added metadata HTML plus full-paper HTML. The local archive unit's README, provenance record, machine-readable summary, acquisition receipt, and verification report were updated.
- Final source state: complete. PDF and full-paper HTML passed the mandatory integrity gate; no partial files remained. The optional TeX/source package was unavailable through the brokered redirect policy.
- Source policy: the PDF, full-paper HTML, metadata HTML, acquisition records, extracted evidence, and any source package remain local and were not uploaded, staged, committed, copied, or attached. No public `.source/` directory was created.

## Public Outputs

- `.logs/20260820-Arxiv-Spectrum-Occupancy-ML-LOG.md` - this operational record.
- `.reports/BL-Arxiv-Spectrum-Occupancy-ML-20260820/Report-Mark.md` - detailed review and synthesis note.
- `.lake-data/DEP-E/DEP-E-20260820-Spectrum Occupancy/README.md` - public-safe DEP inventory and attribution.
- `.lake-data/DEP-E/DEP-E-20260820-Spectrum Occupancy/spectrum_occupancy_ml_manuscript.md` - schema-complete manuscript research artifact.
- `.lake-data/DEP-E/.index/pubs-index.md` - publication-index row for the substantively reviewed paper.

## Next Review Questions

1. Does the reported SVM+FFA advantage persist across independent locations, seasons, bands, and receiver hardware?
2. How do calibrated probabilities, class imbalance, and asymmetric PU-protection costs change the classifier ranking?
3. Can a reproducible public benchmark reproduce the outage estimates without exposing sensitive spectrum traces?

## Challenges

1. The source reports strong comparative numbers but does not provide raw measurements, code, repeated-seed uncertainty, or hardware-independent runtime detail.
2. Thresholds, temporal splits, and band-specific occupancy rules are scenario-sensitive, so headline accuracy is not a deployment guarantee.
3. A live spectrum product must protect licensed users and avoid turning a research classifier into unauthorized radio-control authority.

## Attribution Block

- Primary paper: https://arxiv.org/abs/1503.07104
- Full-paper HTML: https://arxiv.org/html/1503.07104
- arXiv-issued DOI: https://doi.org/10.48550/arXiv.1503.07104
- Journal record: https://doi.org/10.1109/TVT.2015.2487047
- Source files were withheld locally; only generated Markdown artifacts and public URLs are deposited.
