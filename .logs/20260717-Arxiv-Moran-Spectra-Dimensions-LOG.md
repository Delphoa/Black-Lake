# Arxiv DEP Log - Moran Spectra Dimensions

- Deposit date: 2026-07-17
- Actor: Codex scheduled research workflow
- Selected paper: *On the intermediate value property of spectra for a class of Moran spectral measures*
- Authors: Jinjun Li and Zhiyi Wu
- Stable identifiers: arXiv:2302.05868v1; arXiv DOI 10.48550/arXiv.2302.05868; journal DOI 10.1016/j.acha.2023.101606
- Selection method: `rg --files -g "*.pdf"` enumerated 75,777 PDFs. Their parent directories were normalized into 75,776 paper units, sorted, and sampled uniformly with PowerShell `Get-Random`. The accepted zero-based index was 17,600.
- Candidate and exclusion counts: 75,776 paper units; 0 duplicate exclusions; 0 other exclusions; 0 reselections. The first draw was accepted.
- Dedup validation: no match for the arXiv ID, either DOI, normalized title, or slug family was found in Black-Lake `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, relevant Black-Lake-Data code search, or same-paper worktree markers from the preceding 24 hours. Metadata-only author inventories were not treated as substantive deposits.

## Source Integrity

- Initial classification: `partial`. A 243,499-byte PDF existed and passed the minimum-size, `%PDF-` header, and trailing `%%EOF` checks, but full-paper HTML and companion integrity records were absent, so review paused.
- Repair: the valid PDF was preserved. Official arXiv metadata and the e-print payload were fetched through bounded first-attempt HTTPS transfers. The official arXiv full-paper HTML endpoint returned HTTP 404, so the approved ar5iv full-paper fallback was used. The archive README, attribution record, machine-readable summary, and verification report were updated locally before synthesis.
- Final classification: `complete`. The full-paper HTML is 2,453,288 bytes with 142,726 body characters, a document marker, 45 heading/section markers, and five paper-structure terms. Metadata HTML is 40,030 bytes. The 17,636-byte e-print is a validated gzip-compressed single TeX source with 60,687 decompressed bytes. Partial files: 0.
- Extraction: missing-only cache generation succeeded with `pypdf` and `html-regex`, producing 44,524 bytes of PDF text and 110,876 bytes of HTML text. `pdftotext` was unavailable. The generic `tarfile` source extractor did not recognize the single-file gzip payload, so source-text cache output is absent even though the package was independently decompressed and validated as TeX.
- Source locality: the PDF, full-paper HTML, metadata HTML, TeX source, extracted text, cache, hashes, and integrity records remain local. No source document or `.source/` directory was copied, staged, attached, committed, or uploaded.

## Research Outcome

- Main interval theorem: for the paper's one-dimensional consecutive-digit Moran measures with integer ratios `r_n = b_n/q_n >= 2` and bounded `b_n`, every `t` from 0 through the upper entropy dimension is the Beurling dimension of some spectrum.
- Multiplicity theorem: for every such `t`, the set of spectra having Beurling dimension `t` has cardinality continuum.
- Mechanism: the authors compute the measure's upper entropy dimension, use a tree-mapping spectrality criterion, realize the upper endpoint with the canonical spectrum and the zero endpoint with a lacunary spectrum, then tune intermediate dimensions by replacing selected digit counts with smaller values. A zero-dimensional irregular correction preserves spectral completeness without changing the target dimension.
- Boundary: this is a theorem/proof contribution, not an empirical study or a complete classification of all spectra. The run checked statements, constructions, proof dependencies, and formulas against the full paper but did not formally certify the proofs.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md` - multiscale harmonic analysis, frequency-system decompositions, and assumption-sensitive dimension/exponent thresholds.
2. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - Fourier/exponential measurements, reconstruction, and the boundary between analytic guarantees and implemented evidence.
3. `.lake-data/DEP-E/DEP-E-20260716-FGLE Midpoint Scheme/fgle_midpoint_scheme_manuscript.md` - scale-dependent nonlocal analysis, constructive discretization, convergence conditions, and theorem-dependency auditing.

## Output Paths

- `.logs/20260717-Arxiv-Moran-Spectra-Dimensions-LOG.md`
- `.logs/20260717-Arxiv-Moran-Spectra-Dimensions-PHASE-LOG.md`
- `.reports/BL-Arxiv-Moran-Spectra-Dimensions-20260717/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260717-Moran Spectra/README.md`
- `.lake-data/DEP-E/DEP-E-20260717-Moran Spectra/moran_spectra_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Which parts of the intermediate-dimension construction can be formalized independently of the imported maximal-tree spectrality criterion, and which require the full prior theorem?
2. Does an analogous full interval and continuum-cardinality result hold after removing boundedness of `b_n`, replacing consecutive digits, or moving to higher-dimensional Moran measures?
3. Can finite truncations provide reliable numerical diagnostics for the asymptotic Beurling dimension without confusing long transients with the limsup defining the theorem?

## Challenges

1. Official arXiv full-paper HTML was unavailable, so the source gate required an approved ar5iv fallback and local structure verification before review.
2. The e-print is a valid gzip-compressed single TeX source rather than a tar archive; generic cache extraction failed for that format and required an independent format-aware integrity check.
3. Dense asymptotic and tree-mapping arguments depend on prior results and contain several long estimates, so source-first review cannot be represented as formal mathematical certification.

## Outcome

All required public artifacts were generated from a verified complete local source bundle. Public records use date-only markers, public URLs, and repository-relative paths, and explicitly state that source files were withheld locally.

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/cc8dbaeab8f86b0d77f9e3655e95dfcfb2682b94
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784270121320319
- Submission result: direct push to the default branch succeeded; the staged public-output allowlist contained only the seven declared Markdown/JSON artifacts and no source files.
