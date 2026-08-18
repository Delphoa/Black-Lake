# Arxiv DEP Log: AKB-48 Articulation

- Date: 2026-08-18
- Actor: Codex automation `Black Lake Arxiv DEP 0900`
- Outcome: completed review package; repository submission is represented by the enclosing commit
- Selected paper: *AKB-48: A Real-World Articulated Object Knowledge Base*
- arXiv ID: `2202.08432v1`
- arXiv DOI: `10.48550/arXiv.2202.08432`
- CVPR DOI: `10.1109/CVPR52688.2022.01439`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"` over the private arXiv archive.
- PDF candidates: 75,967.
- Unique PDF-parent paper units: 75,964.
- Identifier-complete units: 75,777.
- Identifier-incomplete units withheld from selection: 187.
- Used-paper index: 2,519 arXiv base IDs.
- Units excluded by used arXiv ID: 745.
- Eligible units: 75,032.
- Selection method: one uniform PowerShell `Get-Random` index over the eligible-unit list.
- Selected zero-based eligible index: 58,660.
- Duplicate rejections after the accepted draw: 0.
- Reselections: 0.

## Deduplication and Recent-Marker Validation

- Scanned `Delphoa/Black-Lake` `.logs`, `.reports`, `.lake-data`, and `.staging` on live `main`.
- Scanned the automation memory for all prior scheduled selections.
- Scanned `Delphoa-Labs/Black-Lake-Data` `.lake-data` and `.reports` on live `main` after reading its README.
- Compared arXiv ID, arXiv DOI, CVPR DOI, canonical and normalized title, and planned slug.
- Exact prior-paper matches: 0.
- Same-unit markers within the 24-hour window: 0.
- Public-safe 24-hour cutoff date: 2026-08-17.

## Source Integrity

- Initial state: partial; a valid PDF and metadata README existed, but no full-paper HTML was present.
- Repair: bounded one-paper companion acquisition collected official full-paper HTML, abstract metadata HTML, and the TeX/source package.
- Existing PDF: preserved after its SHA-256 matched the repair copy byte-for-byte.
- PDF verification: 2,327,224 bytes, `%PDF-` header present, trailing `%%EOF` present, 10 pages reported by the public arXiv PDF view.
- Full-paper HTML verification: 168,613 bytes, 44,824 stripped body characters, document marker present, 56 heading markers, and seven paper-structure terms.
- Metadata HTML: 41,584 bytes; treated as metadata only.
- Source archive: 1,739,558 bytes with 12 readable entries.
- Partial files remaining: 0.
- Local archive companions updated: README, attribution, machine-readable summary, provenance JSON, and verification report.
- Gate result: pass. Review began only after this result.

## Evidence Reviewed

- Complete arXiv v1 PDF, official full-paper HTML, metadata, and TeX source.
- Official CVPR 2022 record and supplemental-material locator.
- Paper-linked AKB-48 project and download pages.
- Paper-linked GitHub project-site repository at observed commit `a351b79874385fddfedff59951507fe2ab81bfb1`.
- Three Black Lake related research entries.
- Code, models, dataset files, and experiments were not downloaded or executed.

## Generated Public Artifacts

- `.logs/20260818-Arxiv-AKB-48-Articulation-LOG.md`
- `.reports/BL-Arxiv-AKB-48-Articulation-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-AKB-48 Articulation/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-AKB-48 Articulation/akb48_articulation_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication-index update

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260806-MemPose Geometry/2607.04930-whitepaper-review.md` - category-level object pose and size estimation from geometric memory.
2. `.lake-data/DEP-A/DEP-A-20260727-ManipulationNet An Intake/whitepaper-intake-review.md` - physical robot-skill benchmarking and cross-site evaluation infrastructure.
3. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md` - contact-rich manipulation with force-aware fast/slow control and explicit failure modes.

## Submission Guard

- Public artifacts use repository-relative paths and public URLs only.
- Source files are withheld locally; no public `.source/` directory is created.
- The staged allowlist must contain only the five Markdown artifacts named above.
- PDF, HTML, TeX/source archives, cache files, extracted source text, repair records, and local archive material must not be staged or uploaded.
