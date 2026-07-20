# Arxiv DEP Log: DUET Set-Wise CTR

- Deployment job: `BLAD-2200-20260719-7D93E819`
- Deployment item: `BLAD-2200-20260719-7D93E819-P10`
- Selected paper: *DUET: Dual Model Co-Training for Entire Space CTR Prediction*
- Identifier: arXiv:2510.24369v1; DOI:10.48550/arXiv.2510.24369
- Random method: a uniform random index was drawn from 75,776 unique PDF-parent paper units among 75,779 enumerated PDFs; index 49,531 was selected on the first draw.
- Dedup validation: `.logs`, `.reports`, `.lake-data`, the job-scoped selected-paper set, the automation ledger, and relevant Black-Lake-Data records were scanned by arXiv ID, DOI, normalized title, and slug. Zero draws were excluded for this slot; no duplicate or current-job match was found. The 24-hour cutoff began 2026-07-18.
- Source integrity: the initial unit was partial because it had a valid PDF but lacked full-paper HTML. One bounded repair retrieved official arXiv HTML and metadata. The final PDF was 2,899,255 bytes with valid header and EOF; the HTML was 208,862 bytes with 72,900 body characters, 27 heading markers, a document marker, and five paper-structure terms.
- Review basis: verified PDF, official full-paper HTML, canonical metadata, and exactly three verified related DEP entries.
- Related entries: `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/`, `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/`, and `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/`.
- Public outputs: `.reports/BL-Arxiv-DUET-Setwise-CTR-20260719/` and `.lake-data/DEP-E/DEP-E-20260719-DUET Setwise CTR/`.
- Locality: PDF, HTML, metadata, extracted text, and caches were withheld locally. No source document or `.source/` directory was uploaded.

Source URLs: https://arxiv.org/abs/2510.24369, https://arxiv.org/html/2510.24369, https://arxiv.org/pdf/2510.24369, https://doi.org/10.48550/arXiv.2510.24369
