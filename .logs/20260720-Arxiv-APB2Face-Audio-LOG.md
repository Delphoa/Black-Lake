# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P03`
- Public-safe run date: 2026-07-20
- Outcome: defensively reviewed, validated, and prepared for submission
- Selected paper: *APB2Face: Audio-guided face reenactment with auxiliary pose and blink signals*
- Stable identifier: `arXiv:2004.14569v1`
- Canonical URL: https://arxiv.org/abs/2004.14569

## Random Selection

- Method: `rg --files -g "*.pdf"`, unique PDF-parent units, uniform PowerShell `Get-Random` index.
- PDF candidates: 75,779; candidate paper units: 75,776.
- Selected one-based index: 65,096.
- Random selection succeeded on the first draw without a machine-, user-, path-, timezone-, or timestamp-derived seed.

## Deduplication and Reselection

- Scanned Black Lake artifacts/indexes, this automation memory, relevant Black-Lake-Data records, and the current-job selected set.
- Keys: arXiv ID, DOI, normalized title, `APB2Face-Audio` slug, artifact markers, and markers on or after the public-safe cutoff date 2026-07-19.
- Metadata-only author inventory rows were not treated as prior reviews.
- Duplicate exclusions: 0; reselections: 0.

## Source Integrity

- Initial classification: partial; valid PDF present, full-paper HTML absent.
- Repair: official HTML returned HTTP 404; one approved ar5iv fallback retrieved full-paper HTML, with arXiv metadata retained separately.
- PDF: 4,277,655 bytes; `%PDF-` and trailing `%%EOF` passed.
- Full-paper HTML: 206,725 bytes; 25,459 body characters; 17 document markers; 17 headings; 37 paper-structure terms.
- Final state: complete. All source files and verification records remain local.

## Safety Scope

- Review is limited to evidence, evaluation, consent/provenance gaps, defensive detection, disclosure, and governance.
- No face-generation code, identity assets, dataset media, models, operational reenactment procedure, or evasion guidance is published.

## Public Outputs

- `.logs/20260720-Arxiv-APB2Face-Audio-LOG.md`
- `.reports/BL-Arxiv-APB2Face-Audio-20260720/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260720-APB2Face Safety/README.md`
- `.lake-data/DEP-E/DEP-E-20260720-APB2Face Safety/apb2face_safety_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - manipulated-media detection, calibration, and human review.
2. `.lake-data/DEP-E/DEP-E-20260716-Biometric Identity Gaps/biometric_identity_gaps_manuscript.md` - synthetic identity, consent, biometric lifecycle, resemblance, and revocation risks.
3. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` - motion-controllable generation, evaluator dependence, provenance, and synthetic-media governance.

## Submission Gate

- Allowlist: generated Markdown plus required publication-index Markdown and dedup JSON.
- `.source/`: absent; source-document upload: none.
- Public sanitization withholds local paths, exact execution timestamps, and user/machine context.
