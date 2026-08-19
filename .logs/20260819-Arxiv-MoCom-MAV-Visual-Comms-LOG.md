# Arxiv DEP Log: MoCom MAV Visual Comms

- Date: 2026-08-19
- Actor: Codex automation `Black Lake Arxiv DEP 0900`
- Outcome: completed review package; repository submission is represented by the enclosing commit
- Selected paper: *MoCom: Motion-based Inter-MAV Visual Communication Using Event Vision and Spiking Neural Networks*
- Authors: Nengbo Zhang; Hann Woei Ho; Ye Zhou
- arXiv ID: `2510.14770v1`
- arXiv DOI: `10.48550/arXiv.2510.14770`
- Published DOI: `10.1109/TRO.2026.3677077`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"` over the private arXiv archive.
- PDF candidates: 75,967.
- Unique PDF-parent paper units: 75,964.
- Identifier-incomplete units withheld from selection: 185.
- Used-paper index: 2,871 arXiv base IDs.
- Units excluded by used arXiv ID: 903.
- Eligible units: 74,876.
- Selection method: one uniform PowerShell `Get-Random` index over the eligible-unit list after used-ID exclusion.
- Selected zero-based eligible index: 71,005.
- Duplicate rejections after the accepted draw: 0.
- Reselections: 0.

## Deduplication and Recent-Marker Validation

- Scanned `Delphoa/Black-Lake` `.logs`, `.reports`, `.lake-data`, and `.staging` on live `main`.
- Scanned the automation memory for prior scheduled selections.
- Scanned `Delphoa-Labs/Black-Lake-Data` `.lake-data` and `.reports` on live `main` after reading its README.
- Compared arXiv ID, arXiv DOI, published DOI, canonical and normalized title, and planned slug.
- Exact prior-paper matches: 0.
- Same-unit markers within the 24-hour window: 0.
- Public-safe 24-hour cutoff date: 2026-08-18.

## Source Integrity

- Initial state: partial; a valid full PDF existed, but verified full-paper HTML was absent.
- Repair: one broker-controlled, bounded single-paper acquisition preserved the existing PDF and collected official full-paper HTML plus abstract metadata HTML.
- PDF verification: 7,531,759 bytes, `%PDF-` header present, trailing `%%EOF` present, 13 pages, and no encryption.
- Full-paper HTML verification: 257,858 bytes, 71,273 stripped body characters, document marker present, 55 heading markers, and six paper-structure terms.
- Metadata HTML: 41,816 bytes; treated as metadata only.
- TeX/source package: unavailable because the source endpoint redirected outside the broker's permitted exact surface; no blind retry or strategy switch was attempted.
- Partial files remaining: 0.
- Local archive companions updated: README, provenance record, machine-readable summary, verification report, and immutable acquisition receipt.
- Gate result: pass. Review began only after the PDF and full-paper HTML both passed validation.

## Evidence Reviewed

- Complete arXiv v1 PDF and official full-paper HTML, including all 13 rendered pages, figures, tables, equations, and references.
- Official arXiv metadata and persistent arXiv DOI.
- Crossref metadata for the IEEE Transactions on Robotics publication and DOI.
- Author-controlled institutional publication listing.
- The paper's generic SpikeJelly implementation dependency; no paper-specific code or dataset repository was established in the bounded public search.
- Exactly three Black Lake related research entries.
- Code, data, supplementary video, and experiments were not downloaded or executed.

## Generated Public Artifacts

- `.logs/20260819-Arxiv-MoCom-MAV-Visual-Comms-LOG.md`
- `.reports/BL-Arxiv-MoCom-MAV-Visual-Comms-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-MoCom MAV Comms/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-MoCom MAV Comms/mocom_mav_comms_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication-index update

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` - event-only spiking perception, temporal evidence aggregation, modeled energy, and deployment-boundary analysis.
2. `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md` - globally constrained swarm coordination, compact group coding, motion primitives, and planning/execution tradeoffs.
3. `.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md` - calibrated event-sensor noise, synthetic event generation, and sensor-regime provenance.

## Submission Guard

- Public artifacts use repository-relative paths and public URLs only.
- Original PDF, HTML, metadata, caches, renderings, repair records, and extracted source material are withheld locally.
- No public `.source/` directory is created.
- The staged allowlist must contain only the five Markdown artifacts named above.
- Any PDF, HTML, TeX/source archive, cache, extracted source text, repair record, or local archive material must remain unstaged and must not be uploaded.
