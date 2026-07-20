# DEP-E-20260720-Cued Speech MLLM

#accessibility #cued-speech #multimodal-learning #lip-reading #hand-modeling #hearing-impaired #responsible-ai

Public-safe context: job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P06`, uniformly selected `arXiv:2503.21785v1`. The PDF-only unit was repaired to verified complete with official full-paper HTML before review. Local paths, exact execution times, and source documents are withheld.

## Contents

- `README.md` - deposit context, inventory, responsible-use boundary, synthesis, and attribution.
- `cued_speech_mllm_manuscript.md` - schema-complete review of STF-ACSR, MHI-MCCSD, evidence, limitations, accessibility governance, and related DEP synthesis.

No `.source/` exists. No participant video, hand/lip image, dataset record, PDF, HTML, code, checkpoint, cache, or extracted source text is deposited.

## Summary of Items

STF-ACSR prompts a hosted MLLM to classify hand shapes/positions and fuses outputs with a pretrained lip-reading model. The added dataset contains 5,272 sentences from eight hearing-impaired Mandarin cuers. The paper reports greater than 68% error-rate reduction against EcoCued across tested settings, up to 84.37% CER improvement, and strong prompt/support-set ablations.

The manuscript preserves important limits: only eight hearing-impaired participants; no clearly participant-disjoint split; Mandarin-specific rules; hosted-model version/cost/privacy dependencies; and no inspected consent, IRB, licensing, retention, or community-governance protocol.

## Insights and Relevance

The useful derivative is a participant-centered offline evidence gate with per-cuer CER/WER, modality ablations, missing-modality tests, hosted-model version pinning, privacy receipts, and abstention. AV Emotion Fusion, CorrKD Missing Modal, and VLM Probing contribute complementary assurance patterns.

## Attribution Block

- https://arxiv.org/abs/2503.21785 - metadata and public source locators.
- https://arxiv.org/html/2503.21785 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2503.21785 - verified PDF; local copy withheld.
- https://github.com/DennisHgj/STF_ACSR - paper-declared implementation/checkpoint locator; not executed or redistributed.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion - related fusion evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-CorrKD%20Missing%20Modal - related missing-modality evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing - related representation evidence.
- Source files: verified PDF, full-paper HTML, metadata HTML, and integrity records; all withheld locally with zero source-document uploads.
