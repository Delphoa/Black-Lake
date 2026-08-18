# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P28`
- Public-safe date: 2026-08-18
- Paper: *Shadow Generation with Decomposed Mask Prediction and Attentive Shadow Filling*
- Identifier: `arXiv:2306.17358`; DOI: `10.48550/arXiv.2306.17358`
- URL: https://arxiv.org/abs/2306.17358

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 37,923 on draw 1.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Shadow-Generation-with-Decomposed-Mask` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 23,012,155 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 0; sampled text inspection: true.
- Full-paper HTML: 166,576 bytes, 43,331 body characters, 51 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Shadow-Generation-with-Decomposed-Mask-LOG.md`
- `.reports/BL-Arxiv-Shadow-Generation-with-Decomposed-Mask-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Shadow Generation with/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Shadow Generation with/shadow_generation_with_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Controlling Latent/controlling_latent_manuscript.md` - Controlling Latent Review - DEP-E; overlap: shadow, generation.
2. `.lake-data/DEP-E/DEP-E-20260818-Mask Proposal Voting/mask_proposal_voting_manuscript.md` - Mask Proposal Voting - DEP-E; overlap: mask.
3. `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md` - Mixed-Interest CTR Transfer; overlap: prediction, shadow.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
