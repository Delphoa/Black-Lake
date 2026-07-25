# Arxiv DEP Log: Dental-Lung Cancer MR

- Date: 2026-07-25
- Actor: Codex
- Action: Randomly select one eligible locally archived arXiv paper, enforce a complete-source gate, create a source-grounded review, and deposit a DEP-E research package.
- Selected paper: *Dissecting the Dental Lung Cancer Axis via Mendelian Randomization and Mediation Analysis*
- Canonical record: [arXiv:2507.18287v1](https://arxiv.org/abs/2507.18287v1)
- Result: Complete; the public repository submission contains generated Markdown only.
- Affected DEP: `.lake-data/DEP-E/DEP-E-20260725-Dental Lung MR/`
- Blockers: None.

## Random Selection and Deduplication

- Candidate discovery used `rg --files -g "*.pdf"` over the private archive, with each PDF parent directory treated as one paper unit.
- The enumeration produced 75,780 PDFs in 75,777 candidate units.
- A used-paper index was assembled from Delphoa/Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and the corresponding fetched `origin/main` surfaces in Delphoa-Labs/Black-Lake-Data.
- The index contained 1,362 used arXiv base identifiers. It excluded 352 candidate units as already used; another 185 units were withheld because a canonical identifier could not be established reliably. Total unavailable to the draw: 537 units.
- The remaining eligible pool contained 75,240 units. PowerShell `Get-Random` selected uniform zero-based eligible index 70,409.
- The accepted identifier was arXiv:2507.18287, *Dissecting the Dental Lung Cancer Axis via Mendelian Randomization and Mediation Analysis*.
- Duplicate rejections and reselections: 0.
- The 24-hour marker cutoff was 2026-07-24. The accepted paper had no matching recent marker.
- A final exact-match check covered arXiv ID `2507.18287`, arXiv DOI `10.48550/arXiv.2507.18287`, IEEE DOI `10.1109/BIBM66473.2025.11357049`, hyphenated and unhyphenated title forms, normalized title, and the planned public slugs. No prior Black Lake Arxiv DEP artifact was found.

## Source Integrity Gate

- Initial state: partial. A valid full PDF was present, but verified full-paper HTML was absent.
- Repair preflight: one ID-scoped paper bundle, a private staging target, no credentials, one brokered acquisition strategy, finite retries, no restart automation, and explicit separation of complete artifacts from partial bytes.
- The first ID-search request failed closed because arXiv redirected the search surface to an abstract page. It produced no partial files. One final exact-title search reused the same publisher-control strategy and acquired the paper successfully.
- The existing PDF was preserved because it was byte-identical to the broker-acquired PDF.
- Final PDF verification: 3,192,319 bytes; `%PDF-` header present; trailing `%%EOF` present; eight pages; unencrypted; SHA-256 `007BC2DD4B8CD88C822F0F8A7E78A40B5BD43803F79AE6457ADF766C6486FE1A`.
- Final official full-paper HTML verification: 187,338 bytes; 53,098 script/style-stripped body characters; a full-document marker; 48 heading markers; and six paper-structure terms.
- Supporting verification: one retained search-provenance snapshot and immutable collector receipt; one valid machine-readable unit summary; zero partial files.
- Extraction cache: complete PDF and HTML text cached locally with `pypdf` and HTML extraction; no TeX/source package was collected.
- Final classification: complete and verified.
- Source-file policy: all PDF, HTML, search-provenance, render, cache, receipt, and verification materials were withheld in the private archive. No source file was copied into, staged for, or uploaded to the public repository.

## Review Boundary

- The paper was inspected from its complete PDF and official full-paper HTML; all eight PDF pages, four tables, three figures, methods, results, discussion, conclusion, and references were reviewed.
- The authors report dental-caries associations with overall lung cancer and three subtypes using two-sample Mendelian randomization, plus small mediation proportions through FVC and FEV1.
- Reviewer cautions include significant heterogeneity, directional-pleiotropy signals in parts of the lung-function chain, European-only summary data, survival-selection and smoking-confounding limits, no described multiple-testing correction, an abstract-versus-Table-I exposure-sample discrepancy, and no independent reproduction.
- The result is research evidence, not clinical guidance. Mendelian-randomization estimates do not by themselves establish that dental treatment prevents lung cancer or that screening criteria should change.
- The arXiv record is v1 in `cs.CV`; later public bibliographic evidence identifies an IEEE BIBM 2025 proceedings version. A bounded exact-name search did not establish an official public code repository.

## Public Artifacts

- `.logs/20260725-Arxiv-Dental-Lung-Cancer-MR-LOG.md`
- `.reports/BL-Arxiv-Dental-Lung-Cancer-MR-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-Dental Lung MR/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-Dental Lung MR/dental_lung_mr_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication-index update

## Related DEP Basis

1. `.lake-data/DEP-E/DEP-E-20260722-Causal DP Workloads/causal-dp-workloads.md` - causal-estimand preservation, uncertainty calibration, and the distinction between point accuracy and valid inference.
2. `.lake-data/DEP-E/DEP-E-20260720-Agent Systems Map/agent-systems-map.md` - the NAIS governed biomedical workflow, a 286,422-person hypertension GWAS, aggregate-only execution, and human phenotype reconciliation.
3. `.lake-data/DEP-A/DEP-A-20260717-ClinRAG Graph/2607.00798-whitepaper-review.md` - multi-center clinical prediction, domain-shift controls, evidence-grounded inference, external testing, and deployment-governance boundaries.

## Public Sources

- [Canonical arXiv record](https://arxiv.org/abs/2507.18287v1)
- [Official full-paper HTML](https://arxiv.org/html/2507.18287v1)
- [arXiv PDF](https://arxiv.org/pdf/2507.18287v1)
- [arXiv DOI](https://doi.org/10.48550/arXiv.2507.18287)
- [IEEE BIBM DOI](https://doi.org/10.1109/BIBM66473.2025.11357049)
- [DBLP BIBM record](https://dblp.org/rec/conf/bibm/ZhangLWNWY25)
