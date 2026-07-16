# Arxiv DEP Job Log: Multi-Point ISAC

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2208.07592v2, *Multi-Point Integrated Sensing and Communication: Fusion Model and Functionality Selection*
- Selection result: accepted on the first uniform draw
- Source-integrity result: initial `partial`, repaired to verified `complete`
- Source-file policy: all PDF, HTML, metadata, TeX/source, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- PDF count: 75,777
- Unique parent-paper units: 75,776
- Sampling method: PowerShell `Get-Random` over the complete sorted unique parent-unit list
- Zero-based selected index: 53,616
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, normalized title, slug, DOI, prior Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, or recent active-worktree marker was found. One author-inventory row was metadata only and did not count as a research deposit. A targeted Black-Lake-Data code search returned no matching DEP artifact.

## Source Integrity and Cache

- Existing PDF: 1,345,194 bytes, `%PDF-` header present, trailing `%%EOF` present
- Initial full-paper HTML: missing
- Repair: official arXiv HTML returned no full paper; approved ar5iv full-paper fallback, metadata HTML, and TeX/source archive succeeded within bounded requests
- Verified HTML: 954,733 bytes, 71,826 body characters, 32 heading markers, seven structure terms, and a document marker
- Source archive: 6,933,844 bytes, nine listed entries
- Remaining partial files: 0
- Extractors: `pypdf`, `html-regex`, `tarfile`
- Cache outputs: PDF text 31,902 bytes; HTML text 58,990 bytes; source text 41,816 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` - jointly allocates sensing and communication/computation resources under coupled freshness and energy objectives.
2. `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` - preserves wireless-domain structure in a learned receiver and supplies a complementary view of sensing-quality estimation.
3. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` - frames telecom optimization as a guarded, evidence-bearing control-plane function rather than unconstrained automation.

## Output Paths

- Job log: `.logs/20260716-Arxiv-Multi-Point-ISAC-LOG.md`
- Phase log: `.logs/20260716-Arxiv-Multi-Point-ISAC-PHASE-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-Multi-Point-ISAC-20260716/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
- Publication index: `.lake-data/DEP-E/.index/pubs-index.md`
- Dedup pointer: `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How does correlated error across nearby sensing devices change the optimal voting threshold and claimed fusion gain?
2. Does the HMO selector remain stable under channel-estimation error, mobility, device failure, and rapidly changing sensing targets?
3. How large is the optimality gap when zero-forcing, the averaged-error surrogate, and local neighborhood search are tested independently?

## Challenges

1. The selected unit lacked full-paper HTML, so synthesis paused for an approved fallback repair and independent integrity verification.
2. The optimization combines binary mode choices, beamforming, power allocation, a surrogate voting model, and a weighted Pareto objective.
3. The evidence is figure-based simulation without an identified official code repository or independently rerun experiment.

## Known Shortfalls

- The ray-tracing simulator, CNN detector, CVXPY optimization, and HMO experiments were not rerun.
- Figure values were interpreted from source text and captions rather than digitized into a new dataset.
- The independence assumption across sensing views and the averaged-error approximation were not stress-tested.
- No official implementation repository was identified in the inspected primary sources.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/d7b708a76a0872c0014fec4f828bbde0263cc6a0
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784200999325719
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source files
- Submission status: direct default-branch push succeeded after preserving one concurrent publication-index entry; Slack notice delivered
