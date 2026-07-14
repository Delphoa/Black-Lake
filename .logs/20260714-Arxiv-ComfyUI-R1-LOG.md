# Arxiv DEP Log - ComfyUI-R1

- Date: 2026-07-14
- Actor: Codex automation
- Selected paper: *ComfyUI-R1: Exploring Reasoning Models for Workflow Generation*
- Stable identifiers: arXiv:2506.09790v1; arXiv DOI: 10.48550/arXiv.2506.09790; later ACL Anthology record: 2026.findings-acl.146
- Selection method: `rg --files -g "*.pdf"` enumerated PDF candidates; parent directories were deduplicated into 75,774 paper units; PowerShell `Get-Random` selected zero-based index 62,885 uniformly.
- Duplicate exclusions: 0
- Reselections: 0; the first draw was accepted.
- Dedup validation: No arXiv ID, DOI, normalized title, slug, or same-paper marker was found in Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, or relevant Black-Lake-Data search results.
- Initial source state: partial. The full PDF passed integrity checks, but full-paper HTML was missing.
- Repair: Preserved the valid PDF and collected official full-paper HTML, abstract/metadata HTML, and the TeX/source package under a bounded local repair. The archive README, provenance record, CSV summary, and verification reports were updated.
- Integrity result: complete. The PDF is 4,571,802 bytes with a `%PDF-` header and trailing `%%EOF`. Full-paper HTML is 302,705 bytes with 72,241 body characters, a document marker, 59 heading/section markers, and seven paper-structure terms. No partial transfer files remain.
- Public source policy: All original source files remain in the private local archive. No PDF, HTML, TeX/source package, extracted source text, or cache was copied into this repository.
- Outcome: source-first review completed and public-safe artifacts prepared.

## Output Paths

- `.logs/20260714-Arxiv-ComfyUI-R1-LOG.md`
- `.reports/BL-Arxiv-ComfyUI-R1-20260714/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260714-ComfyUI R1/README.md`
- `.lake-data/DEP-E/DEP-E-20260714-ComfyUI R1/comfyui_r1_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Does the later ACL Findings version materially change the data construction, generalization tests, or limitations relative to arXiv v1?
2. Can the reported 67% ComfyBench pass rate be reproduced with pinned ComfyUI, node, model, retrieval, and execution environments?
3. How does the hybrid reward behave when multiple valid workflows satisfy the same instruction but differ substantially from the single reference graph?

## Challenges

1. The selected unit required local archive repair before any synthesis because full-paper HTML was initially absent.
2. The main in-domain test supplies candidate nodes, so retrieval quality is separated from most reported generation metrics.
3. The current ComfyUI-Copilot repository documents service changes and does not expose a clearly pinned ComfyUI-R1 model or training package in the inspected surface.
