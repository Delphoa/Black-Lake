# Arxiv DEP Log: MCPWorld

- Paper: *MCPWorld: A Unified Benchmarking Testbed for API, GUI, and Hybrid Computer Use Agents*
- Stable identifiers: arXiv:2506.07672; DOI: [10.48550/arXiv.2506.07672](https://doi.org/10.48550/arXiv.2506.07672)
- Status: deposited research review; public artifacts contain derived analysis and public URLs only.

## Selection and Deduplication

- Enumeration method: `rg --files -g "*.pdf"` produced 75,959 PDF files in 75,956 unique PDF-parent paper units.
- Selection method: uniform PowerShell `Get-Random` draw over the sorted parent-unit list; zero-based index `50,457` selected the MCPWorld unit.
- Exclusion counts: 0 pre-draw exclusions; 0 post-draw duplicate exclusions; 0 source-gate exclusions after repair; 0 reselections.
- Dedup validation: searches of `Black-Lake/.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data material found no owning Arxiv DEP log, Report-Mark, or DEP-E entry for the arXiv ID, DOI, normalized title, or `mcpworld` slug. Black-Lake-Data contained metadata-only inventory references, not a deposited review.
- Recent-marker validation: no same-paper marker was found in the reviewed artifact locations; the selected paper was not an accepted duplicate within the preceding 24-hour review window.

## Source Integrity

- Initial classification: partial. The selected archive unit contained a valid PDF but no full-paper HTML.
- Repair: a bounded brokered single-paper repair retained the valid PDF and collected the official arXiv metadata page and official full-paper HTML. The archive README, provenance record, machine-readable summary, verification report, and acquisition receipt were refreshed locally.
- Verification: complete. The PDF is 1,442,366 bytes, begins with `%PDF-`, and has a trailing `%%EOF`. The full-paper HTML is 774,129 bytes with 123,748 body characters after markup removal, a document marker, 91 heading/section markers, and all seven checked paper-structure terms. No partial files remain.
- Source package: unavailable through the bounded source request; this does not affect the complete PDF-plus-full-HTML gate.
- Source policy: PDF, HTML, metadata, provenance, receipt, and all other source files remain withheld locally. No source file or `.source/` directory was created for public submission.

## Outputs

- `.logs/20260730-Arxiv-MCPWorld-LOG.md`
- `.reports/BL-Arxiv-MCPWorld-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-MCPWorld Benchmark/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-MCPWorld Benchmark/mcpworld_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Can independently authored agents reproduce the reported hybrid advantage under pinned task, MCP-server, and model versions?
2. How often do internal hooks yield false positives or false negatives when application implementations evolve?
3. Does a capability-complete MCP surface close the MCP-only gap without making tool descriptions too long for reliable planning?

## Challenges

1. The paper evaluates one dated agent/model configuration, so its modality ranking is not a current general leaderboard.
2. White-box instrumentation improves observability but depends on application-source access and maintenance work.
3. The official repository README advertises approximately 170 tasks while the paper reports 201, creating a version-alignment question.

## Public Sources

- [arXiv record](https://arxiv.org/abs/2506.07672)
- [Full-paper HTML](https://arxiv.org/html/2506.07672)
- [Official MCPWorld repository](https://github.com/SAAgent/MCPWorld)
