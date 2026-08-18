# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P40`
- Public-safe date: 2026-08-18
- Paper: *RANP: Resource Aware Neuron Pruning at Initialization for 3D CNNs*
- Identifier: `arXiv:2010.02488`; DOI: `10.48550/arXiv.2010.02488`
- URL: https://arxiv.org/abs/2010.02488

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 42,144 on draw 1.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RANP-Resource-Aware-Neuron-Pruning-at` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,240,359 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 16; sampled text inspection: true.
- Full-paper HTML: 458,241 bytes, 80,021 body characters, 61 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-RANP-Resource-Aware-Neuron-Pruning-at-LOG.md`
- `.reports/BL-Arxiv-RANP-Resource-Aware-Neuron-Pruning-at-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-RANP Resource Aware/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-RANP Resource Aware/ranp_resource_aware_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-Can Attention Enable MLPs/can_attention_enable_mlps_manuscript.md` - Can Attention Enable MLPs - DEP-E; overlap: cnns.
2. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: initialization, resource.
3. `.lake-data/DEP-E/DEP-E-20260731-Structured Directional/structured_directional_manuscript.md` - Structured Directional - DEP-E; overlap: pruning.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
