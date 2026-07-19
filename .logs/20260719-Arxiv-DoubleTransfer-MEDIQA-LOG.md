# Arxiv DEP Phase Log

- Run date: 2026-07-19
- Actor/tool: Codex scheduled Arxiv DEP workflow
- Selected paper: *DoubleTransfer at MEDIQA 2019: Multi-Source Transfer Learning for Natural Language Understanding in the Medical Domain*
- Authors: Yichong Xu; Xiaodong Liu; Chunyuan Li; Hoifung Poon; Jianfeng Gao
- Stable identifiers: arXiv:1906.04382v1; arXiv DOI 10.48550/arXiv.1906.04382; ACL DOI 10.18653/v1/W19-5042
- Canonical record: https://arxiv.org/abs/1906.04382v1
- Outcome: complete
- Blockers: none

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"` against the local arXiv archive.
- Paper unit: one unique PDF parent directory, with adjacent metadata and source companions treated as one unit.
- Method: uniformly select one zero-based index from the sorted unique parent-directory set with PowerShell `Get-Random`.
- PDF candidates: 75,778.
- Unique paper units: 75,776.
- Selected zero-based index: 34,844.
- Duplicate exclusions: 0.
- Other exclusions: 0.
- Reselections: 0; the first draw was accepted.

## Deduplication

The arXiv ID, arXiv DOI, ACL DOI, normalized title, and `DoubleTransfer-MEDIQA` slug family were checked against Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and relevant Black-Lake-Data artifact scopes. No existing Arxiv DEP log, report, DEP-E deposit, or same-paper marker within 24 hours was found. Black-Lake-Data contained one metadata-only author-inventory pointer to the paper; it was not a processed research artifact and did not trigger exclusion.

## Source-Integrity Gate

- Initial state: partial. A 631,721-byte PDF and minimal metadata README were present, but full-paper HTML and companion provenance/verification records were absent.
- Preserved artifact: the existing PDF passed the 10 KB minimum, `%PDF-` header, and trailing `%%EOF` checks.
- Repair: collected arXiv metadata HTML and a 271,345-byte arXiv source package. The official arXiv full-paper HTML endpoint returned 404 after three bounded attempts, so the approved ar5iv fallback was collected.
- Full-paper HTML verification: 214,879 bytes; 31,992 body characters after script/style/tag removal; document marker present; 30 section/heading markers; five paper-structure term classes; no error, conversion, or abstract-only notice.
- Final state: complete. README, attribution record, machine-readable summary, and verification report were updated locally; no partial transfer files remain.
- Local review evidence: the complete 7-page v1 PDF, full-paper HTML, metadata HTML, TeX source, Algorithm 1, Figure 1, and all five tables were inspected.
- Source locality: all PDF, HTML, metadata, source-package, extraction, verification, and render files remain local. No source file is included in this repository change.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` - tests whether heterogeneous audio/video fusion adds value, and preserves negative evidence when fusion helps one label setting but hurts another.
2. `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/pixel_point_transfer_manuscript.md` - studies teacher-to-student representation transfer across modalities and makes domain-shift and transferred-bias checks explicit.
3. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` - supplies a medical question-answering evidence and governance boundary, including dataset lineage, leakage risk, calibration, and non-diagnostic use.

## Outputs

- `.logs/20260719-Arxiv-DoubleTransfer-MEDIQA-LOG.md`
- `.reports/BL-Arxiv-DoubleTransfer-MEDIQA-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-DoubleTransfer MEDIQA/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-DoubleTransfer MEDIQA/doubletransfer_mediqa_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Does the reported multi-source ensemble advantage persist across repeated seeds, matched ensemble sizes, calibration metrics, and an untouched validation protocol?
2. Which part of DoubleTransfer contributes most: SciBERT initialization, MT-DNN task knowledge, MNLI mixture-ratio training, task-specific fine-tuning, or heterogeneous voting?
3. How well do the learned representations and confidence estimates transfer to newer medical NLU datasets, institutions, specialties, and language distributions without protected-data leakage?

## Challenges

1. The selected unit required bounded source repair because official arXiv full-paper HTML was unavailable for this identifier.
2. The paper reports a large competition ensemble and development/test distribution interventions but no repeated-seed uncertainty, calibration, or matched-compute ablation.
3. Underlying MT-DNN and SciBERT repositories are public, but no paper-specific DoubleTransfer training package, split manifest, checkpoint set, or one-command reproduction was identified.
