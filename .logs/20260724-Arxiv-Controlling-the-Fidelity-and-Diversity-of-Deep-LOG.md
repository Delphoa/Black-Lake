# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260724-CF53BCCB`
- Deployment item ID: `BLAD-2200-20260724-CF53BCCB-P08`
- Public-safe date: 2026-07-24
- Paper: *Controlling the Fidelity and Diversity of Deep Generative Models via Pseudo Density*
- Identifier: `arXiv:2407.08659`; DOI: `10.48550/arXiv.2407.08659`
- URL: https://arxiv.org/abs/2407.08659

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 33,224 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Controlling-the-Fidelity-and-Diversity-of-Deep` slug; the 24-hour marker cutoff was 2026-07-23.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 26,365,540 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 25; sampled text inspection: true.
- Full-paper HTML: 516,651 bytes, 76,764 body characters, 43 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260724-Arxiv-Controlling-the-Fidelity-and-Diversity-of-Deep-LOG.md`
- `.reports/BL-Arxiv-Controlling-the-Fidelity-and-Diversity-of-Deep-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-Controlling the Fidelity/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-Controlling the Fidelity/controlling_the_fidelity_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Controlling Latent/controlling_latent_manuscript.md` - Controlling Latent Review - DEP-E; overlap: controlling, generative, diffusion.
2. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` - Adversarial Label Noise - DEP-E; overlap: distribution, training.
3. `.lake-data/DEP-E/DEP-E-20260710-Deep ESN Memory/deep_esn_memory_manuscript.md` - Deep ESN - DEP-E; overlap: deep.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
