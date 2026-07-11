# Arxiv DEP Log: Self-Learned IDC

## Public-Safe Run Summary

- Deposit date: 2026-07-10
- Automation: Black Lake Arxiv DEP 1500
- Selected paper: Self-learned Intelligence for Integrated Decision and Control of Automated Vehicles at Signalized Intersections
- arXiv ID: 2110.12359
- DOI: 10.48550/arXiv.2110.12359
- Authors: Yangang Ren; Jianhua Jiang; Dongjie Yu; Shengbo Eben Li; Jingliang Duan; Chen Chen; Keqiang Li
- Source URLs: https://arxiv.org/abs/2110.12359 ; https://arxiv.org/pdf/2110.12359 ; https://arxiv.org/e-print/2110.12359 ; https://doi.org/10.48550/arXiv.2110.12359
- Source-file policy: no `.source/` files deposited; public URLs and cache-derived review notes only.

## Random Selection Method

- Candidate enumeration command class: `rg --files -g "*.pdf"` against the local arXiv source archive.
- Paper unit rule: each PDF parent directory counted as one paper unit.
- Candidate PDF count: 75,438.
- Candidate paper-unit count: 75,438.
- Random method: PowerShell `Get-Random` selected zero-based paper-unit index 22,294.
- Reselection count: 0.
- Exclusion counts during acceptance: no arXiv ID, 0; prior Black-Lake artifact hit, 0; Black-Lake-Data ID/title hit, 0.

## Deduplication Validation

- `.staging/arxiv-dep-dedup-index.json`: not present before this run in the checked upstream state.
- Black-Lake scans: `.logs`, `.reports`, `.lake-data`, and `.staging` were scanned for `2110.12359` before acceptance; no hit found.
- Automation memory: memory file was absent before this run.
- Black-Lake-Data checks: authenticated repository search found no match for `2110.12359` and no match for the exact selected title.
- Same-paper 24-hour markers: no repository marker found for the selected arXiv ID, DOI, title, or slug.

## Extraction Cache Summary

- Initial cache state: miss.
- Local `missing-only` extraction: metadata-only; local PDF was found, local HTML/source package was not found, and PDF text extraction failed because available local extractors were unavailable.
- Network backfill: allowed because reviewable text was missing; public arXiv HTML and source package were fetched through the extraction script.
- Final cache status: cached.
- Final text outputs: HTML text present; source text present; PDF text absent.
- Extractor status: HTML `html-regex` ok; source `tarfile` ok; PDF extractor failed.

## Output Paths

- Log: `.logs/20260710-Arxiv-Self-Learned-IDC-LOG.md`
- Phase log: `.logs/20260710-Arxiv-Self-Learned-IDC-PHASE-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-Self-Learned-IDC-20260710/Report-Mark.md`
- DEP README: `.lake-data/DEP-E-20260710-Self Learned IDC/README.md`
- DEP manuscript: `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`
- Dedup index: `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md` - selected for overlap with state as a first-class control and safety review object.
2. `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - selected for overlap with spatial/world-model consistency and embodied simulation evaluation.
3. `.lake-data/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - selected for overlap with physical-system learning, compact structured representations, and domain-aligned model substrates.

## Next-Review Questions

1. Can the dynamic permutation encoding be reproduced from released code or reconstructed from the paper's source with a small SUMO scenario?
2. How sensitive are the reported collision and compliance counts to traffic density, sensor noise, and left-turn scenario randomization?
3. Can the same set-encoding/control pattern be generalized into an agent-state ledger or simulation-evidence card for Black-Lake reviews?

## Challenges

1. PDF text extraction was unavailable in the local extractor environment, so the review relied on arXiv HTML and fetched TeX source after approved network backfill.
2. No official code repository was found from inspected arXiv, web, or GitHub title/ID searches.
3. The reported driving metrics were source-reported only; no SUMO simulation, controller training, or MPC comparison was reproduced.
