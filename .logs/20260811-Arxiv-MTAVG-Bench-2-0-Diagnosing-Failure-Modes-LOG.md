# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260811-BB3E2A1B`
- Deployment item ID: `BLAD-2200-20260811-BB3E2A1B-P01`
- Public-safe date: 2026-08-11
- Paper: *MTAVG-Bench 2.0: Diagnosing Failure Modes of Cinematic Expressiveness in Multi-Talker Audio-Video Generation*
- Identifier: `arXiv:2605.28035`; DOI: `10.48550/arXiv.2605.28035`
- URL: https://arxiv.org/abs/2605.28035

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 35,520 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `MTAVG-Bench-2-0-Diagnosing-Failure-Modes` slug; the 24-hour marker cutoff was 2026-08-10.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 33,148,164 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 24; sampled text inspection: true.
- Full-paper HTML: 303,614 bytes, 76,732 body characters, 142 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260811-Arxiv-MTAVG-Bench-2-0-Diagnosing-Failure-Modes-LOG.md`
- `.reports/BL-Arxiv-MTAVG-Bench-2-0-Diagnosing-Failure-Modes-20260811/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260811-MTAVG-Bench 2 0/README.md`
- `.lake-data/DEP-E/DEP-E-20260811-MTAVG-Bench 2 0/mtavg_bench_2_0_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-UnityShots Memory-Driven/unityshots_memory_driven_manuscript.md` - UnityShots Memory-Driven Multi-S - DEP-E; overlap: audio-video, generation, modes, failure.
2. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` - AV Emotion Fusion - DEP-E; overlap: audio-video, diagnosing, generation, modes, failure.
3. `.lake-data/DEP-E/DEP-E-20260809-Voice Evaluation of/voice_evaluation_of_manuscript.md` - Voice Evaluation of - DEP-E; overlap: diagnosing, modes, failure.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
