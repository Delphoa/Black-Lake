# 2026-07-24 - Black Lake Arxiv DEP: MOCS Flexible Lengths

- Actor/tool: Codex automation `Black Lake Arxiv DEP 1300`
- Action: Randomly selected, integrity-verified, reviewed, and synthesized one arXiv archive paper.
- Selected paper: *How to Construct Mutually Orthogonal Complementary Sets with Non-Power-of-Two Lengths?* (`arXiv:2003.06991v1`)
- Source provenance: Public arXiv PDF, approved full-paper HTML fallback, metadata page, arXiv-issued DOI, IEEE DOI, and institutional publication metadata. All source files were withheld locally.
- Random method: `rg --files -g "*.pdf"` produced 75,780 PDF candidates, collapsed to 75,777 unique PDF-parent paper units, then PowerShell `Get-Random` selected zero-based index 42,505 uniformly.
- Eligibility: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and relevant Black-Lake-Data material were scanned for arXiv ID, DOI, normalized title, and slug markers. The only related-repository hit was a metadata-only inventory row, not a processed DEP. Duplicate exclusions: 0. Other exclusions: 0. Reselections: 0.
- Source-integrity result: Initial state `partial`; the existing 233,143-byte PDF passed size, `%PDF-`, trailing `%%EOF`, and SHA-256 checks, but full-paper HTML was absent. A bounded v4 publisher-brokered repair collected metadata HTML and a 2,302,873-byte approved ar5iv full-paper rendering. Final state `complete`: the HTML had 99,316 body characters, three document markers, 51 heading/section markers, seven paper-structure term classes, no error or abstract-only marker, and zero partials. The source-package redirect was rejected by the strict broker policy and was not required for the complete-paper gate.
- Related DEP entries:
  1. `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md`
  2. `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
  3. `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
- Outputs:
  - Report-Mark: `.reports/BL-Arxiv-MOCS-Flexible-Lengths-20260724/Report-Mark.md`
  - DEP: `.lake-data/DEP-E/DEP-E-20260724-MOCS Flexible Lengths`
  - Manuscript: `.lake-data/DEP-E/DEP-E-20260724-MOCS Flexible Lengths/mocs_flexible_lengths_manuscript.md`
  - Publication index: `.lake-data/DEP-E/.index/pubs-index.md`
  - Dedup pointer: `.staging/arxiv-dep-dedup-index.json`
- Validation target: Full manuscript schema, matching compact title, exact-three sections, DEP inventory, publication index, dedup pointer, Markdown hygiene, public-safety scan, staged allowlist, and no-source-upload gate.
- Source upload status: No PDF, HTML, metadata page, source archive, extracted text, cache, render, verification record, or `.source/` directory is included.

## Questions for the Next Reviewer

1. Does Corollary 5's `M/N = 1/2` ratio remain the best attainable value for this GBF length family, or can a different algebraic construction approach a complete complementary code with `M/N = 1`?
2. Can the theorem examples be reproduced by a small reference generator whose exhaustive correlation checks match every reported `(M,N,L)` tuple?
3. How do the flexible-length families affect system metrics such as PAPR, BER, radar ambiguity, storage, and generation latency under matched OFDM, OTFS, or ISAC conditions?

## Challenges for the Next Review Pass

1. Mechanize one theorem and Corollary 5 in a proof assistant or exact symbolic checker, including the binary-index and truncation conventions.
2. Reproduce Examples 1-4 and Tables I-II with an independently written generator, then publish discrepancy tests for the `r = N/M` notation and the length-18 table statement.
3. Benchmark the generated sequences in a pinned multicarrier or radar simulator against power-of-two CCCs and paraunitary constructions using matched resources.
