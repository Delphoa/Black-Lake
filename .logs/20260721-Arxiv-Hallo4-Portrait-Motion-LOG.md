# Arxiv DEP Job Log: Hallo4 Portrait Motion

## Public-Safe Run Summary

- Deposit date: 2026-07-21.
- Selected paper: *Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization*.
- Stable identity: arXiv:2505.23525v4; DOI:10.48550/arXiv.2505.23525.
- Selection method: `rg --files -g "*.pdf"` enumerated 75,779 PDF files, collapsed to 75,776 unique PDF-parent paper units, and PowerShell `Get-Random` selected zero-based index 11,355 uniformly.
- Draw outcome: first draw accepted; duplicate exclusions 0; reselections 0.
- Source state: initially partial because full-paper HTML was absent; repaired to verified complete before review.
- Cache state: initial miss; final `cached` after local `missing-only` extraction.
- Submission state: deposited; primary repository commit pushed and Slack notification delivered.

## Dedup and Eligibility Validation

The selected arXiv ID, arXiv DOI, normalized title, and `Hallo4-Portrait-Motion` slug were checked against the public dedup pointer, `.logs`, `.reports`, `.lake-data`, automation memory, relevant Black-Lake-Data content, and active Black Lake worktrees. No prior Arxiv DEP research deposit or same-paper marker within 24 hours was found. Two Black-Lake-Data author-inventory rows were metadata-only pointers and did not constitute research deposits.

## Source Integrity and Cache

- Existing PDF: 10,418,972 bytes; `%PDF-` header and trailing `%%EOF` verified.
- Repaired official full-paper HTML: 151,929 bytes; 46,119 body characters; 39 headings/section markers; seven paper-structure terms; article/LaTeXML document marker present.
- Metadata HTML: collected locally and classified as metadata only.
- Source archive: valid 19-entry archive retained locally.
- Unexpected partial files after repair: 0.
- Extraction: `pypdf` 53,699 bytes, `html-regex` 46,819 bytes, and `tarfile` 193,139 bytes.
- Extractor fallback: `pdftotext` unavailable; `pypdf` succeeded.
- Public-source policy: PDF, HTML, metadata, source archive, renders, cache, extracted text, hashes, and integrity records were withheld locally. No `.source/` directory was created.

## Evidence Reviewed

- Complete 16-page PDF, official full-paper HTML, TeX/source archive, and extraction-cache outputs.
- Tables 1-9, Figures 4-8, preference-data construction, DPO objective, temporal motion modulation, training settings, user study, limitations, and conclusion.
- Canonical arXiv metadata and arXiv-issued DOI.
- Official `fudan-generative-vision/hallo4` repository at commit `d8274e5e809ea1cd94279063b2a835b23832e466`, including README, inference launcher, dependency inventory, and visible source tree.
- Live Black Lake and Black-Lake-Data repository authorities.

## Generated Outputs

- `.logs/20260721-Arxiv-Hallo4-Portrait-Motion-LOG.md`
- `.logs/20260721-Arxiv-Hallo4-Portrait-Motion-PHASE-LOG.md`
- `.reports/BL-Arxiv-Hallo4-Portrait-Motion-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - connects online preference optimization, curated hard negatives, and the need to audit judge/data pipelines rather than treating DPO as an automatic quality guarantee.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - connects shared latent conditioning and video-diffusion evaluation beyond surface appearance, especially temporal and structural consistency.
3. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` - connects motion-conditioned video generation, inference-aligned training, motion metrics, streaming state, and synthetic-media safety controls.

## Exactly Three Next-Review Questions

1. How many annotators rated the preference pairs and user-study clips, what agreement statistics were observed, and how sensitive are results to annotator composition?
2. Do Hallo4's synchronization gains persist under multiple seeds, independent human raters, unseen languages, longer clips, and identity/consent-safe evaluation sets?
3. Can the released implementation be made reproducible with a portable environment, consistent checkpoint naming, a clear repository license, and scripts for training, metrics, and dataset provenance?

## Exactly Three Challenges

1. The method improves synchronization and expression metrics without uniformly improving FID/FVD, so a single state-of-the-art label would hide meaningful tradeoffs.
2. Preference-data and user-study protocols omit annotator counts, agreement, randomization, and uncertainty, limiting confidence in human-alignment claims.
3. The official repository exposes inference code and weights instructions, but a machine-local dependency URI, checkpoint-name mismatch, unclear repository license, and paper/README author-name mismatch obstruct a clean reproduction.

## Submission Record

- Primary commit: https://github.com/Delphoa/Black-Lake/commit/91d3203f8b6708be77fd6c5be451b434775463d8
- Final submission-record commit: recorded in repository history by the completion-record commit that updates this log.
- Slack notification: delivered to `#black-lake-artifacts`.
- Source files uploaded: no; all source and source-derived review files were withheld locally.
