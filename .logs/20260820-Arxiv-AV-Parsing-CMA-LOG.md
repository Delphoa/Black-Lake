# Black Lake Arxiv DEP: AV Parsing CMA

Run date: 2026-08-20

`Black Lake Arxiv DEP` randomly selected and reviewed one eligible arXiv archive paper.

## Selection and eligibility

- Selected paper: **Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing** (`arXiv:2509.14097`, Yaru Chen, Ruohao Guo, Liting Gao, Yang Xiang, Qingyu Luo, Zhenbo Li, Wenwu Wang).
- Public provenance: [arXiv metadata](https://arxiv.org/abs/2509.14097), [full-paper HTML](https://arxiv.org/html/2509.14097), and [PDF](https://arxiv.org/pdf/2509.14097).
- Random method: `rg --files -g "*.pdf"` enumerated 75,967 PDF candidates; 75,964 unique parent-directory paper units were formed; uniform PowerShell `Get-Random` selected zero-based index 2,973. No manual substitution.
- Dedup scan: `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data search context were checked for the arXiv ID, title, DOI, normalized title, slug, Arxiv DEP markers, and date-only recent markers.
- Eligibility: duplicate exclusions 0; reselections 0; public 24-hour cutoff date 2026-08-19; selected unit initially partial because full-paper HTML and metadata HTML were absent.
- Source repair: one bounded brokered repair added verified full-paper HTML and metadata/provenance/verification companions. The PDF passed the size, `%PDF-`, and `%%EOF` checks; full-paper HTML passed size, body, article-marker, heading, and structure-term checks; source package was unavailable; no partial files remained.

## Related DEP entries

1. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` — direct audio-video fusion and modality-value evidence.
2. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` — teacher/student distillation and incomplete-modality robustness.
3. `.lake-data/DEP-A/DEP-A-20260721-Cued Speech MLLM Intake/cued-speech-mllm-intake-review.md` — multimodal cue fusion with confidence, availability, alignment, and provenance accountability.

## Outputs

- Log: `.logs/20260820-Arxiv-AV-Parsing-CMA-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-AV-Parsing-CMA-20260820/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260820-AV Parsing CMA/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260820-AV Parsing CMA/av_parsing_cma_manuscript.md`
- Publication index: `.lake-data/DEP-E/.index/pubs-index.md`

## Validation notes

- Manuscript schema, title identity/length, evidence ledger, required headings, and exactly three exercise paths were checked.
- Report-Mark synthesis sections contain exactly three implementations, observations, similarities, mock-ups, developer challenges, and author challenges.
- Public-output sanitization and staged allowlist checks are required before commit; no local paths, usernames, machine names, local timezone labels, exact local execution times, PDFs, HTML, source archives, caches, or extracted source files may be staged.
- Source files were withheld locally and were not uploaded, committed, pushed, or sent to Slack.

## Questions for the next reviewer

1. Do confidence-gated segment pairs remain calibrated when audio and video are asynchronous or corrupted?
2. Which teacher update and pseudo-mask policy is most stable across event-frequency shifts?
3. Does the reported gain survive speaker- or video-disjoint repeated evaluation with uncertainty intervals?

## Challenges for the next review pass

1. Reconstruct the full training and evaluation protocol without silently filling unspecified hyperparameters.
2. Separate the contribution of EMA, pseudo-mask selection, and CMA under matched compute and seed budgets.
3. Design a missing-modality and modality-conflict test that preserves privacy and does not redistribute source media.
