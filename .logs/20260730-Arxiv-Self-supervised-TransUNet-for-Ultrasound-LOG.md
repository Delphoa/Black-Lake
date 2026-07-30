# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260730-2FDDC232`
- Deployment item ID: `BLAD-2200-20260730-2FDDC232-P04`
- Public-safe date: 2026-07-30
- Paper: *Self-supervised TransUNet for Ultrasound regional segmentation of the distal radius in children*
- Identifier: `arXiv:2309.09490`; DOI: `10.48550/arXiv.2309.09490`
- URL: https://arxiv.org/abs/2309.09490

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 23,304 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Self-supervised-TransUNet-for-Ultrasound` slug; the 24-hour marker cutoff was 2026-07-29.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,318,849 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 4; sampled text inspection: true.
- Full-paper HTML: 59,870 bytes, 22,193 body characters, 37 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260730-Arxiv-Self-supervised-TransUNet-for-Ultrasound-LOG.md`
- `.reports/BL-Arxiv-Self-supervised-TransUNet-for-Ultrasound-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-Self-supervised TransUNet/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-Self-supervised TransUNet/self_supervised_transunet_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/decentralized_attention_manuscript.md` - Decentralized Attention - DEP-E; overlap: attention, medical.
2. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - LA-Pose Latent Action - DEP-E; overlap: self-supervised.
3. `.lake-data/DEP-E/DEP-E-20260720-Decentralized SSL/decentralized_ssl_manuscript.md` - Decentralized SSL Review - DEP-E; overlap: ssl.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
