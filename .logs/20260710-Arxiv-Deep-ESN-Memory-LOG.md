# Arxiv DEP Log: Deep ESN Memory

- Automation: Black Lake Arxiv DEP 1100
- Public run date: 2026-07-10
- Actor: Codex
- Selected paper: `Analysis of Memory Capacity for Deep Echo State Networks`
- Selected identifier: `arXiv:1908.07063`
- Paper URL: https://arxiv.org/abs/1908.07063
- Output class: `DEP-E`

## Selection Method

- Candidate enumeration used `rg --files -g "*.pdf"` over the local arXiv source archive.
- Candidate unit rule: each PDF parent directory was treated as one paper unit, with adjacent metadata files inspected after selection.
- Random method: uniform zero-based random index using PowerShell `Get-Random`.
- Candidate count: 75,438 PDF candidates.
- Selected zero-based index: 35,572.
- Selected unit metadata exposed `arXiv:1908.07063` and title `Analysis of Memory Capacity for Deep Echo State Networks`.

## Deduplication and Exclusion Counts

- Duplicate marker scan targets: `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, automation memory, and `Black-Lake-Data/.lake-data` plus `.reports`.
- Markers searched: arXiv ID `1908.07063`, normalized title, slug `Deep-ESN-Memory`, and phrase markers `Deep Echo State` / `Memory Capacity`.
- Duplicate markers found: 0.
- Same-paper 24-hour markers found: 0.
- Candidate units excluded in this run: 0.
- Reselections required: 0.

## Sources Inspected

- arXiv abstract page for `1908.07063`.
- arXiv PDF for `1908.07063`.
- Local archive readme/PDF presence for the selected paper unit, with local path withheld.
- Live `Delphoa/Black-Lake` README from the fetched default branch.
- Live `Delphoa-Labs/Black-Lake-Data` README from a temporary repository read.
- Related Black-Lake and Black-Lake-Data DEP entries listed below.

## Output Paths

- `.logs/20260710-Arxiv-Deep-ESN-Memory-LOG.md`
- `.reports/BL-Arxiv-Deep-ESN-Memory-20260710/Report-Mark.md`
- `.lake-data/DEP-E-20260710-Deep ESN Memory/README.md`
- `.lake-data/DEP-E-20260710-Deep ESN Memory/deep_esn_memory_manuscript.md`

## Related DEP Entries

1. `.lake-data/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
   - Relevance: direct reservoir-computing overlap; the OTFS review studies reservoir computing for online wireless symbol detection, while the selected paper analyzes memory capacity and deep ESN architectures.
2. `.lake-data/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`
   - Relevance: shared time-series and compact model-design concern; both artifacts ask how structured dynamics can improve learning with fewer or better-targeted trainable degrees of freedom.
3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260707-Tech Intel 1103/daily_research_findings_2026-07-07_1103.md`
   - Relevance: memory as a measurable system resource; the entry includes agent-memory and cache-state findings that help contrast ESN short-term memory capacity with operational AI memory workloads.

## Next-Review Questions

1. Can the NARMA experiments be reproduced with a small, version-pinned ESN harness and published seeds?
2. Does the paper's parallel ESN improvement persist when total reservoir parameters are equalized against a larger shallow ESN?
3. What practical workload best exposes the tradeoff between memory capacity and feature extraction in series ESNs?

## Challenges

1. The paper leaves the full theoretical memory-capacity derivation for series ESNs to future work.
2. The reported results are simulation-only in this review, with no official code found in inspected sources.
3. The PDF text extraction flattens equations and figures, so formula-level validation should use source or manual equation review.

## Outcome

The paper was accepted for this run. Artifacts were generated as public-safe repository records with no source files collected or redistributed.
