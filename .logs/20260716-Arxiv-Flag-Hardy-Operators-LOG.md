# Arxiv DEP Log - Flag Hardy Operators

- Deposit date: 2026-07-16
- Actor: Codex scheduled research workflow
- Selected paper: *Boundedness of singular integrals on the flag Hardy spaces on Heisenberg group*
- Authors: Guorong Hu and Ji Li
- Stable identifiers: arXiv:1702.07201v1; arXiv DOI 10.48550/arXiv.1702.07201; journal DOI 10.1016/j.jmaa.2017.11.054
- Selection method: `rg --files -g "*.pdf"` enumerated 75,777 PDFs. Their parent directories were normalized into 75,776 paper units, sorted, and sampled uniformly with PowerShell `Get-Random`. The accepted zero-based index was 16,565.
- Candidate and exclusion counts: 75,776 paper units; 0 duplicate exclusions; 0 other exclusions; 0 reselections. The first draw was accepted.
- Dedup validation: no match for arXiv ID, DOI, normalized title, or slug family was found in Black-Lake `.logs`, `.reports`, `.lake-data`, the automation memory, the relevant Black-Lake-Data code search, or same-paper markers from the preceding 24 hours.

## Source Integrity

- Initial classification: `partial`. A valid full PDF existed, but full-paper HTML and companion provenance records were absent, so review paused.
- Repair: preserved the existing PDF; fetched official arXiv metadata and e-print payload with bounded direct-HTTPS requests. The official arXiv full-paper HTML endpoint returned HTTP 404, so the approved ar5iv full-paper fallback was used. The archive README, attribution record, machine-readable summary, verification report, and extraction cache were updated locally.
- Final classification: `complete`. The PDF is 211,007 bytes, begins with `%PDF-`, and contains a trailing `%%EOF`. Full-paper HTML is 3,093,841 bytes with 112,378 body characters, a document marker, 24 heading/section markers, and four paper-structure term classes. Independent skill validation also passed. Partial files: 0.
- Extraction: PDF extraction succeeded with `pypdf`; HTML extraction succeeded. The e-print is a valid gzip-wrapped single TeX file with 71,045 decompressed bytes; the generic tar extractor reported that its single-file gzip format is not a tar archive.
- Source locality: PDF, full-paper HTML, metadata HTML, TeX source, extracted text, caches, and integrity records remain local. No source file was copied, staged, attached, committed, or uploaded.

## Research Outcome

- Main theorem reviewed: a classical Calderón-Zygmund convolution operator whose kernel satisfies the stated first-order regularity and cancellation conditions is bounded on the flag Hardy space `H^p_flag(H^n)` for `4n/(4n+1) < p <= 1`.
- Corollary reviewed: duality yields boundedness on `BMO_flag(H^n)`.
- Proof mechanism reviewed: discrete flag Littlewood-Paley analysis, almost-orthogonality estimates, a new discrete Calderón reproducing formula, molecular-space control, and Hardy-Littlewood/strong maximal plus Fefferman-Stein vector-valued estimates.
- Evidence limit: the paper is a theorem/proof contribution with no empirical benchmark. Several proof details are cited, outlined, or left to the reader; this run did not formally verify the mathematics.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` - Calderón-type commutator estimates, function-space control, and explicit theorem thresholds.
2. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - Fourier reconstruction, operator conditioning, and the distinction between analytic guarantees and implemented validation.
3. `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` - structured two-dimensional convolution, geometry-aware representation, and separate scale regimes.

## Output Paths

- `.logs/20260716-Arxiv-Flag-Hardy-Operators-LOG.md`
- `.reports/BL-Arxiv-Flag-Hardy-Operators-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Can the lower endpoint `4n/(4n+1)` be derived mechanically from the exact maximal-function exponent constraints, and how does it change under higher kernel regularity and cancellation?
2. Which omitted or imported steps in Lemma 2.1, Proposition 2.5, and the final square-function estimates carry the greatest formal-verification risk?
3. How far does the proof architecture extend beyond classical convolution kernels on the Heisenberg group to non-convolution operators or other flag geometries?

## Challenges

1. The selected unit required a full-paper HTML repair before synthesis, and the official endpoint needed an approved ar5iv fallback.
2. PDF extraction introduced glyph corruption in dense formulas, requiring cross-checks against full-paper HTML and TeX source.
3. The argument depends heavily on prior flag-Hardy theory and omits several routine or analogous derivations, so source review cannot be presented as proof certification.

## Outcome

All required public artifacts were generated from verified complete sources. Public records use date-only markers, public URLs, and repository-relative paths, and explicitly state that source files were withheld locally.
