# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-50A35360`
- Deployment item ID: `BLAD-2200-20260818-50A35360-P07`
- Public-safe date: 2026-08-18
- Paper: *Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models*
- Identifier: `arXiv:2403.03003`; DOI: `10.48550/arXiv.2403.03003`
- URL: https://arxiv.org/abs/2403.03003

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 24,650 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Feast-Your-Eyes-Mixture-of-Resolution-Adaptation` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,078,938 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 223,401 bytes, 48,327 body characters, 48 headings, and 5 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Feast-Your-Eyes-Mixture-of-Resolution-Adaptation-LOG.md`
- `.reports/BL-Arxiv-Feast-Your-Eyes-Mixture-of-Resolution-Adaptation-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Feast Your Eyes/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Feast Your Eyes/feast_your_eyes_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260816-Get Your Embedding Space/get_your_embedding_space_manuscript.md` - Get Your Embedding Space - DEP-E; overlap: your, adaptation.
2. `.lake-data/DEP-E/DEP-E-20260730-Drag Your GAN Interactive/drag_your_gan_interactive_manuscript.md` - Drag Your GAN Interactive - DEP-E; overlap: your.
3. `.lake-data/DEP-E/DEP-E-20260813-Adapt as You Say Online/adapt_as_you_say_online_manuscript.md` - Adapt as You Say Online - DEP-E; overlap: adaptation, language.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
