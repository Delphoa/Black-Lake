# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260815-A0637DE9`
- Deployment item ID: `BLAD-2200-20260815-A0637DE9-P03`
- Public-safe date: 2026-08-15
- Paper: *The Clock and the Pizza: Two Stories in Mechanistic Explanation of Neural Networks*
- Identifier: `arXiv:2306.17844`; DOI: `10.48550/arXiv.2306.17844`
- URL: https://arxiv.org/abs/2306.17844

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 34,293 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `The-Clock-and-the-Pizza-Two-Stories` slug; the 24-hour marker cutoff was 2026-08-14.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 10,491,957 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 28; sampled text inspection: true.
- Full-paper HTML: 391,998 bytes, 79,858 body characters, 128 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260815-Arxiv-The-Clock-and-the-Pizza-Two-Stories-LOG.md`
- `.reports/BL-Arxiv-The-Clock-and-the-Pizza-Two-Stories-20260815/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260815-The Clock and the Pizza/README.md`
- `.lake-data/DEP-E/DEP-E-20260815-The Clock and the Pizza/the_clock_and_the_pizza_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260727-A New System of Global/a_new_system_of_global_manuscript.md` - A New System of Global - DEP-E; overlap: neural, networks.
2. `.lake-data/DEP-E/DEP-E-20260713-Dynamical Dictionary/dynamical_dictionary_manuscript.md` - Dynamical Dictionary - DEP-E; overlap: networks, explanation, neural, two.
3. `.lake-data/DEP-E/DEP-E-20260731-Lattice Spoken LM/lattice_spoken_lm_manuscript.md` - Lattice Spoken LM - DEP-E; overlap: neural, networks, two.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
