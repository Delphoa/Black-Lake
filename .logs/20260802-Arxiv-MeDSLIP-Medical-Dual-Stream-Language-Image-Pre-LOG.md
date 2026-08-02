# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260802-0D11B2FA`
- Deployment item ID: `BLAD-2200-20260802-0D11B2FA-P10`
- Public-safe date: 2026-08-02
- Paper: *MeDSLIP: Medical Dual-Stream Language-Image Pre-training with Pathology-Anatomy Semantic Alignment*
- Identifier: `arXiv:2403.10635`; DOI: `10.48550/arXiv.2403.10635`
- URL: https://arxiv.org/abs/2403.10635

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 55,507 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `MeDSLIP-Medical-Dual-Stream-Language-Image-Pre` slug; the 24-hour marker cutoff was 2026-08-01.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 26,646,462 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 450,402 bytes, 71,866 body characters, 67 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260802-Arxiv-MeDSLIP-Medical-Dual-Stream-Language-Image-Pre-LOG.md`
- `.reports/BL-Arxiv-MeDSLIP-Medical-Dual-Stream-Language-Image-Pre-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/medslip_medical_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: tomography, cbct, scatter, attenuation, mri.
2. `.lake-data/DEP-E/DEP-E-20260802-Boundary and/boundary_and_manuscript.md` - Boundary and - DEP-E; overlap: pediatric, pet, tomography, cbct, scatter.
3. `.lake-data/DEP-E/DEP-E-20260731-Generalizable CT-Free PET/generalizable_ct_free_pet_manuscript.md` - Generalizable CT-Free PET - DEP-E; overlap: pediatric, pet, tomography, patients, scatter.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
