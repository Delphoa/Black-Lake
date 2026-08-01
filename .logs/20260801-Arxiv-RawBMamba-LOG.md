# Black Lake Arxiv DEP Log: RawBMamba

- Run date: 2026-08-01
- Selected paper: *RawBMamba: End-to-End Bidirectional State Space Model for Audio Deepfake Detection*
- Authors: Yujie Chen; Jiangyan Yi; Jun Xue; Xiaohui Zhang; Shunbo Dong; Siding Zeng; Jianhua Tao; Lv Zhao; Cunhang Fan
- arXiv: 2406.06086v2
- Public venue: Interspeech 2024, pages 2720-2724
- Public DOI: https://doi.org/10.21437/Interspeech.2024-698

## Selection and Deduplication

- Method: 'rg --files -g "*.pdf"' enumerated the local archive, PDF parent directories were reduced to unique paper units, the units were sorted, and a uniform PowerShell Get-Random draw selected one zero-based index.
- Candidate count: 75,960 PDF files and 75,957 unique parent-directory paper units.
- Draw: zero-based index 5,736.
- Acceptance: first draw accepted; duplicate exclusions 0, other exclusions 0, reselections 0.
- Dedup keys checked: arXiv ID, arXiv DOI, publisher DOI, normalized title, slug, prior .logs, .reports, .lake-data/DEP-E-* artifacts, staging markers, automation memory, and matching Black-Lake-Data search results.
- Recency check: no same-paper marker was found in the preceding 24-hour window.

## Source Integrity Gate

- Initial state: partial; the local unit contained a valid PDF but no metadata HTML or full-paper HTML.
- Repair: one bounded brokered single-paper acquisition preserved the PDF and collected metadata HTML plus full-paper HTML from the official arXiv route.
- Final PDF validation: 986,266 bytes, %PDF- header, trailing %%EOF.
- Final full-paper HTML validation: 266,444 bytes, 48,345 extracted body characters after script/style removal, 39 heading markers, a document marker, and 6 paper-structure term classes.
- Partial-file check: no .part files remained.
- Source package: unavailable through the broker redirect policy; this did not block the PDF plus full-paper HTML gate.
- Review status: complete. Source files remain local and were not copied to, staged for, or attached to public outputs.

## Generated Public Outputs

- .logs/20260801-Arxiv-RawBMamba-LOG.md
- .reports/BL-Arxiv-RawBMamba-20260801/Report-Mark.md
- .lake-data/DEP-E/DEP-E-20260801-RawBMamba/README.md
- .lake-data/DEP-E/DEP-E-20260801-RawBMamba/rawbmamba_manuscript.md
- .lake-data/DEP-E/.index/pubs-index.md

No public .source/ directory was created. The public artifacts cite canonical URLs and state that source files were withheld locally.

## Next-Review Questions

1. Does the 21LA gain survive repeated seeds, speaker-disjoint splits, and matched preprocessing against modern audio deepfake baselines?
2. How does bidirectional context behave under streaming latency constraints, variable-duration clips, codec changes, noise, and adversarial post-processing?
3. Can the official implementation reproduce the paper tables with pinned dependencies, released checkpoints, and a public evaluation manifest?

## Challenges

1. The headline 34.1% improvement depends on a baseline naming/table comparison that should be made explicit and independently recomputed.
2. The reported fixed four-second raw-waveform window may miss artifacts outside the crop and does not establish full-utterance robustness.
3. Deepfake detection is dual-use: public evaluation must protect speaker privacy, dataset rights, model-weight provenance, and misuse resistance.

## Attribution Block

- Source URL: https://arxiv.org/abs/2406.06086
  - Applies to: selection identity, authors, dates, abstract, and version record.
- Source URL: https://arxiv.org/html/2406.06086
  - Applies to: full-paper methods, tables, results, and conclusion; the source file was inspected locally and withheld.
- Source URL: https://doi.org/10.21437/Interspeech.2024-698
  - Applies to: venue and publication metadata.
- Source URL: https://github.com/cyjie429/RawBMamba
  - Applies to: official implementation availability and README-reported reproduction context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md
  - Applies to: related audio representation and fusion synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260731-Lattice%20Spoken%20LM/lattice_spoken_lm_manuscript.md
  - Applies to: related speech representation and uncertainty synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-APB2Face%20Safety/apb2face_safety_manuscript.md
  - Applies to: related synthetic-media safety and provenance synthesis.
