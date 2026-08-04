# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260804-92EFB161`
- Deployment item ID: `BLAD-2200-20260804-92EFB161-P04`
- Public-safe date: 2026-08-04
- Paper: *Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring*
- Identifier: `arXiv:2410.21083`; DOI: `10.48550/arXiv.2410.21083`
- URL: https://arxiv.org/abs/2410.21083

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 49,891 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Stealthy-Jailbreak-Attacks-on-Large-Language` slug; the 24-hour marker cutoff was 2026-08-03.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 927,662 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 16; sampled text inspection: true.
- Full-paper HTML: 419,615 bytes, 78,145 body characters, 109 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260804-Arxiv-Stealthy-Jailbreak-Attacks-on-Large-Language-LOG.md`
- `.reports/BL-Arxiv-Stealthy-Jailbreak-Attacks-on-Large-Language-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-Stealthy Jailbreak/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-Stealthy Jailbreak/stealthy_jailbreak_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/stealth_memory_trust_manuscript.md` - Stealth Memory Trust - DEP-E; overlap: stealthy, benign, attacks.
2. `.lake-data/DEP-E/DEP-E-20260716-PIArena Evaluation/piarena_evaluation_manuscript.md` - PIArena Evaluation - DEP-E; overlap: benign, attacks, language.
3. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` - ViT Semantic Robustness - DEP-E; overlap: benign, attacks.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
