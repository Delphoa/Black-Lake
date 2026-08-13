# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260809-2E4CB30E`
- Deployment item ID: `BLAD-2200-20260809-2E4CB30E-P09`
- Public-safe date: 2026-08-09
- Paper: *On $[[n,n-4,3]]_{q}$ Quantum MDS Codes for odd prime power $q$*
- Identifier: `arXiv:0906.2509`; DOI: `10.1103/PhysRevA.82.052316`
- URL: https://arxiv.org/abs/0906.2509

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 16,323 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `On-n-n-4-3-q-Quantum` slug; the 24-hour marker cutoff was 2026-08-08.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 124,774 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 7; sampled text inspection: true.
- Full-paper HTML: 1,110,427 bytes, 47,761 body characters, 19 headings, and 5 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260809-Arxiv-On-n-n-4-3-q-Quantum-LOG.md`
- `.reports/BL-Arxiv-On-n-n-4-3-q-Quantum-20260809/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260809-On n n-4 3 q Quantum MDS/README.md`
- `.lake-data/DEP-E/DEP-E-20260809-On n n-4 3 q Quantum MDS/on_n_n_4_3_q_quantum_mds_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md` - Irregular Clipped SR - DEP-E; overlap: quantum, codes, power.
2. `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading/quantum_quant_trading_manuscript.md` - Quantum Quant Trading - DEP-E; overlap: quantum, power.
3. `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md` - SIM MARL Power - DEP-E; overlap: codes, power.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
