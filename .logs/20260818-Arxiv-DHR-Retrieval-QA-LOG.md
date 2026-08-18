# Arxiv DEP Log: DHR Retrieval QA

- Run date: 2026-08-18
- Selected paper: *Dense Hierarchical Retrieval for Open-Domain Question Answering*
- Stable identifier: arXiv:2110.15439v1; DOI:10.48550/arXiv.2110.15439; ACL DOI:10.18653/v1/2021.findings-emnlp.19
- Source state: initially partial because the local PDF existed without verified full-paper HTML; one bounded brokered single-paper repair completed the local source pair before review.
- Public source policy: PDF, full-paper HTML, metadata HTML, provenance, verification, receipts, and source-package failure evidence remain local. No source file or `.source/` directory was uploaded.

## Selection and Deduplication

- Enumeration: `rg --files -g "*.pdf"` against the local arXiv archive found 75,967 PDFs across 75,964 unique PDF-parent paper units.
- Identifier normalization: 75,782 units had a normalized arXiv identifier from the PDF filename, nearby metadata, or the parent folder; 185 identifier-incomplete units were withheld from the frozen pool.
- Prior scan: `.logs`, `.reports`, `.lake-data`, automation memory, and relevant `Delphoa-Labs/Black-Lake-Data` searches were checked for arXiv IDs, DOI, title, and slug. The local scan contained 1,881 unique prior arXiv IDs; 729 candidate units matched a prior identifier and were excluded.
- Frozen eligible pool: 75,053 units.
- Random method: parent units were sorted by repository-independent path order, then sampled uniformly with PowerShell `Get-Random` using zero-based index 74,067.
- Reselection validation: duplicate exclusions 0; same-paper markers in the preceding 24-hour window 0; post-draw exact arXiv ID, DOI, normalized title, and slug scan 0; reselections 0.

## Source Integrity Gate

- Initial classification: partial, because the valid PDF was present but full-paper HTML was missing.
- Repair: one bounded archive-collector repair fetched official metadata and full-paper HTML through the broker; the existing valid PDF was preserved. The optional TeX/source package was unavailable and was not required for the source gate.
- Final verification: complete. The PDF was 1,164,987 bytes, began with `%PDF-`, and contained trailing `%%EOF`. The full-paper HTML was 213,659 bytes with 57,325 visible body characters, article/main/LaTeXML markers, 62 heading markers, and six paper-structure terms. No partial files remained.

## Generated Public Artifacts

- `.logs/20260818-Arxiv-DHR-Retrieval-QA-LOG.md`
- `.reports/BL-Arxiv-DHR-Retrieval-QA-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-DHR Retrieval/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-DHR Retrieval/dhr_retrieval_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Does DHR retain its retrieval and end-to-end QA gains when the Wikipedia snapshot, encoder revision, and corpus scale are updated together?
2. How much of the gain comes from hierarchy-aware passage construction versus document gating, title augmentation, hard negatives, or score reranking?
3. Do index-search-only speedups survive full request accounting, including document and passage encoding, memory movement, reader latency, and tail behavior?

## Challenges

1. Reproducing the 2018 Wikipedia preprocessing, title tree, positive-context matching, and four dataset splits without silent version drift.
2. Separating the causal value of DHR’s hierarchy from the substantial changes to passage splitting and negative-sampling policy.
3. Preserving provenance and answer-evidence boundaries when adapting hierarchical retrieval to private or access-controlled corpora.

## Attribution Block

- Public paper record: https://arxiv.org/abs/2110.15439
  - Applies to: selection, source identity, and public paper locator.
- Publication record: https://aclanthology.org/2021.findings-emnlp.19/
  - Applies to: venue, pages, publication DOI, and bibliographic confirmation.
- Source files: local-only verified PDF, full-paper HTML, metadata HTML, and integrity companions.
  - Applies to: source-first review evidence; withheld from the public repository and Slack.
