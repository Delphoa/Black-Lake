# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260727-ADBD50D5`
- Deployment item ID: `BLAD-2200-20260727-ADBD50D5-P07`
- Public-safe date: 2026-07-27
- Paper: *The Case of FBA as a DEX Processing Model*
- Identifier: `arXiv:2302.01177`; DOI: `10.48550/arXiv.2302.01177`
- URL: https://arxiv.org/abs/2302.01177

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 59,181 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `The-Case-of-FBA-as-a-DEX` slug; the 24-hour marker cutoff was 2026-07-26.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 11,094,410 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 1,323,656 bytes, 140,607 body characters, 97 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260727-Arxiv-The-Case-of-FBA-as-a-DEX-LOG.md`
- `.reports/BL-Arxiv-The-Case-of-FBA-as-a-DEX-20260727/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260727-The Case of FBA as a DEX/README.md`
- `.lake-data/DEP-E/DEP-E-20260727-The Case of FBA as a DEX/the_case_of_fba_as_a_dex_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-MA-VLM PNU Moderation/ma_vlm_pnu_moderation_manuscript.md` - MA-VLM Moderation - DEP-E; overlap: loss.
2. `.lake-data/DEP-E/DEP-E-20260722-Weak Diffusion Priors/weak_diffusion_priors_manuscript.md` - Weak Diffusion Priors - DEP-E; overlap: when.
3. `.lake-data/DEP-E/DEP-E-20260720-Decentralized SSL/decentralized_ssl_manuscript.md` - Decentralized SSL Review - DEP-E; overlap: decentralized.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
