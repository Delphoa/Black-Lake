# 2026-08-01 - Arxiv PTransIPs Protein PLM

- Actor/tool: Codex recurring research automation.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260801-PTransIPs Protein PLM/`.
- Action: Random paper selection, cross-repository deduplication, local source-integrity repair, source-first review, implementation inspection, related-DEP synthesis, manuscript/report generation, validation, and submission preparation.
- Paper: *PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings*.
- Authors: Ziyang Xu, Haitian Zhong, Bingrui He, Xueying Wang, and Tianchi Lu.
- arXiv ID: `2308.05115v3`.
- arXiv DOI: https://doi.org/10.48550/arXiv.2308.05115
- Published DOI: https://doi.org/10.1109/JBHI.2024.3377362
- Result: Eligible, source-complete after repair, reviewed, and prepared for DEP-E deposition.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumerated local PDF candidates; paths were collapsed to unique parent-directory paper units; arXiv identifiers were resolved from PDF filenames, parent folder names, and nearby README metadata; globally used IDs and identifier-incomplete units were excluded; PowerShell `Get-Random` selected one zero-based index uniformly from the eligible array, with rejection reserved for exact duplicate or recent same-unit markers.
- PDF candidates: `75,960`.
- Unique PDF-parent units: `75,957`.
- Used arXiv base IDs observed: `1,742`.
- Units excluded by used ID: `502`.
- Identifier-incomplete units withheld from the draw: `185`.
- Eligible units before recent-marker rejection: `75,270`.
- Selected zero-based eligible index: `63,747`.
- Selected paper: arXiv `2308.05115`, *PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings*.
- Duplicate rejections/reselections: `0`.
- Recent-marker rejections/reselections: `0`.

## Deduplication and Reselection Validation

- Dedup scan locations: live Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; this automation's private memory; and fetched Black-Lake-Data `.logs`, `.reports`, `.lake-data`, and `.staging` records.
- Match keys: arXiv base/version ID, arXiv DOI, published DOI, canonical title, normalized title, `PTransIPs` token, and planned slugs.
- Exact acceptance check: no prior Arxiv DEP log, report, DEP-E manuscript, correction marker, or automation-memory record matched the paper ID, DOI values, canonical title, token, or planned slug.
- Public-safe 24-hour cutoff date: `2026-07-31`.
- Recent same-paper/archive-unit markers: none before the accepted draw.
- Reselection was not required.

## Local Source Integrity

- Initial state: `partial`.
- Initial evidence: a plausible full PDF and short metadata README were present, but verified full-paper HTML was absent.
- Repair: review paused; the valid PDF was preserved; the pinned publisher-broker workflow fetched official metadata HTML and official full-paper HTML and made one bounded source-package attempt.
- PDF verification: `1,469,516` bytes, `%PDF-` header present, trailing `%%EOF` present, ten unencrypted pages.
- Full-paper HTML verification: `473,588` bytes, `67,023` stripped body characters, a document marker, `52` heading markers, and seven paper-structure terms.
- Metadata HTML: `44,718` bytes.
- Source package: unavailable after the bounded broker attempt; not required for the complete-paper gate.
- Unexpected partial files: `0`.
- Final source state: `complete`.
- Local companion records updated: README, provenance record, machine-readable summary, immutable acquisition receipt, and verification report.
- Source locality: PDF, full-paper HTML, metadata HTML, receipt, verification records, and private renders were withheld locally.

## Review Evidence

- Inspected: the complete ten-page PDF, verified official full-paper HTML, canonical arXiv v3 record, IEEE/PubMed bibliographic record, both DOI locators, and the official implementation repository.
- Visual verification: architecture, embedding/loss ablations, UMAP views, benchmark tables, cross-bioactivity results, discussion, and conclusion were visually checked on rendered PDF pages.
- Implementation status: the official repository was inspected at main commit `60eb4aa4072857c12f7a64739940f73ea60fac77`; README, requirements, model, and training code were reviewed. Code and experiments were not run, no tagged paper release was established, and no top-level license was visible.
- Main evidence boundary: results are author-reported point estimates. The Y independent test has only 21 positive and 21 negative examples; no confidence intervals or external validation are reported.
- Source inconsistency: the abstract and conclusion report Y-site AUC `0.9660`, whereas Tables II-IV and the plotted curve report `0.9683` for PTransIPs. Table IV also reports DE-MHAIPs Y-site AUC `0.9778`, higher than PTransIPs, although PTransIPs leads four of five listed Y metrics.
- Code-paper divergence: the pinned training code computes `CE + H(Y) - H(Y|X)` while Equation 7 specifies `CE - H(Y) + H(Y|X)`; it uses `StratifiedShuffleSplit` rather than disjoint five-fold cross-validation; and the model loop does not visibly feed one custom Transformer layer's output into the next. These are reproducibility findings about the inspected repository state, not proof of the exact code used for reported experiments.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/fgbench_chemistry_manuscript.md` - connects molecular representation design to dependency-aware benchmarks, explicit structural features, and strict limits on downstream biological or chemical inference.
2. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` - connects representation geometry to task-grounded semantic validation and warns that embedding proximity or separation alone is not sufficient evidence of domain meaning.
3. `.lake-data/DEP-E/DEP-E-20260715-MSAIC ECG/msaic_ecg_manuscript.md` - connects multimodule biomedical classification on imbalanced data to patient/sample lineage, uncertainty, ablation discipline, and non-deployment boundaries.

## Generated Public Artifacts

- `.logs/20260801-Arxiv-PTransIPs-Protein-PLM-LOG.md`
- `.reports/BL-Arxiv-PTransIPs-Protein-PLM-20260801/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260801-PTransIPs Protein PLM/README.md`
- `.lake-data/DEP-E/DEP-E-20260801-PTransIPs Protein PLM/ptransips_protein_plm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Verification

- Required manuscript headings, matching YAML/H1 title, evidence ledger, exactly three exercise paths, and MVP fields must pass.
- Required Report-Mark headings, exactly three related DEP entries, exact-three Synthesis Note lists, and three Python mock-ups must pass.
- DEP README inventory, summary, insights, public-safe context, source-withholding statement, and final Attribution Block must pass.
- Public-output leak, encoding, URL-attribution, staged allowlist, and no-source-upload checks are required before commit.
- No `.source/` directory was created.
- No PDF, HTML, metadata page, source archive, cache, extracted text, receipt, render, or verification file was copied into the repository.

## Attribution Block

- Source URL: https://arxiv.org/abs/2308.05115
  - Applies to: paper identity, authors, version history, subjects, abstract context, source locators, and DOI metadata.
  - Notes: Metadata page only; not used as the full paper.
- Source URL: https://arxiv.org/pdf/2308.05115
  - Applies to: complete-paper review and visual verification.
  - Notes: Source file inspected locally and withheld.
- Source URL: https://arxiv.org/html/2308.05115
  - Applies to: verified searchable full-paper review.
  - Notes: Official full-paper HTML; local copy withheld.
- Source URL: https://arxiv.org/e-print/2308.05115
  - Applies to: bounded source-package availability check.
  - Notes: Source package was unavailable and no source file was uploaded.
- Source URL: https://doi.org/10.48550/arXiv.2308.05115
  - Applies to: persistent arXiv identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://doi.org/10.1109/JBHI.2024.3377362
  - Applies to: IEEE Journal of Biomedical and Health Informatics publication identity.
  - Notes: Published DOI.
- Source URL: https://pubmed.ncbi.nlm.nih.gov/38483806/
  - Applies to: journal, issue, pagination, publication date, PMID, and DOI cross-check.
  - Notes: Near-primary bibliographic record.
- Source URL: https://github.com/StatXzy7/PTransIPs
  - Applies to: official code/data/model availability and documented workflow.
  - Notes: Repository inspected but not executed or redistributed.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/src/PTransIPs_model.py
  - Applies to: model architecture conformance review.
  - Notes: Pinned code inspection only.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/src/train.py
  - Applies to: loss and validation-split conformance review.
  - Notes: Pinned code inspection only.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/requirements.txt
  - Applies to: dependency and environment reproducibility review.
  - Notes: Pinned dependency inventory only.
