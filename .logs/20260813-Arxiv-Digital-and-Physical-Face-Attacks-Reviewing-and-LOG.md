# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260813-F994AA5E`
- Deployment item ID: `BLAD-2200-20260813-F994AA5E-P03`
- Public-safe date: 2026-08-13
- Paper: *Digital and Physical Face Attacks: Reviewing and One Step Further*
- Identifier: `arXiv:2209.14692`; DOI: `10.48550/arXiv.2209.14692`
- URL: https://arxiv.org/abs/2209.14692

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 28,387 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Digital-and-Physical-Face-Attacks-Reviewing-and` slug; the 24-hour marker cutoff was 2026-08-12.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 5,650,940 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 19; sampled text inspection: true.
- Full-paper HTML: 370,179 bytes, 123,301 body characters, 64 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260813-Arxiv-Digital-and-Physical-Face-Attacks-Reviewing-and-LOG.md`
- `.reports/BL-Arxiv-Digital-and-Physical-Face-Attacks-Reviewing-and-20260813/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260813-Digital and Physical Face/README.md`
- `.lake-data/DEP-E/DEP-E-20260813-Digital and Physical Face/digital_and_physical_face_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Stealthy Jailbreak/stealthy_jailbreak_manuscript.md` - Stealthy Jailbreak - DEP-E; overlap: attacks, face, one.
2. `.lake-data/DEP-E/DEP-E-20260731-GADT Enhancing/gadt_enhancing_manuscript.md` - GADT Enhancing - DEP-E; overlap: attacks, one.
3. `.lake-data/DEP-E/DEP-E-20260720-APB2Face Safety/apb2face_safety_manuscript.md` - APB2Face Safety Review - DEP-E; overlap: face, digital.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
