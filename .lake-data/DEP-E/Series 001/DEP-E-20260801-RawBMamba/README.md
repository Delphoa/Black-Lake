# DEP-E-20260801-RawBMamba

#audio-deepfake-detection #speech-processing #raw-waveform #state-space-models #Mamba #audio-forensics #calibration #provenance #responsible-ai #arxiv

Public-safe context: this DEP-E records a source-first review of arXiv:2406.06086v2, *RawBMamba: End-to-End Bidirectional State Space Model for Audio Deepfake Detection*. The selected local archive unit was initially partial and was repaired to a verified PDF plus full-paper HTML before review. Source files, local paths, exact execution details, caches, and private verification records remain withheld.

## Contents

- README.md - DEP inventory, public-safe context, item summaries, relevance notes, and source attribution.
- rawbmamba_manuscript.md - schema-complete manuscript review of the paper's short/long-range raw-audio architecture, evidence, limitations, implementation implications, three bounded exercises, and related DEP synthesis.

No .source/ directory was created. No PDF, full-paper HTML, metadata HTML, TeX/source archive, cache, extracted text, audio, checkpoint, or model artifact is included.

## Summary of Items

- README.md makes the deposit auditable by stating the classification, inventory, source boundary, and canonical public locators.
- rawbmamba_manuscript.md reconstructs the sinc/convolutional front end, bidirectional Mamba paths, fusion ablation, ASVspoof evaluation, reported results, implementation availability, evidence limits, and safe downstream uses.
- The manuscript records the uniform random selection and repository-wide deduplication checks, the repaired local source-integrity gate, and the fact that no source files were uploaded.

## Insights and Relevance

RawBMamba is useful as a testable representation hypothesis: local acoustic artifacts and longer contextual patterns may require different feature paths, but the gain must be separated from crop choice, seed variance, baseline naming, and benchmark shift. The three related entries extend the review in complementary directions. AV Emotion Fusion supplies matched fusion and negative-result discipline; Lattice Spoken LM supplies uncertainty-preserving speech representation context; APB2Face Safety supplies consent, provenance, and synthetic-media governance boundaries. The combined downstream recommendation is a calibrated, abstention-capable research queue that exposes evidence channels and shift state instead of treating a detector score as an identity or legal decision.

## Attribution Block

- Source URL: https://arxiv.org/abs/2406.06086
  - Applies to: rawbmamba_manuscript.md and this README.
  - Notes: Canonical paper identity, authors, abstract, dates, version, subjects, and arXiv DOI.
- Source URL: https://arxiv.org/html/2406.06086
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Official full-paper source for methods, tables, results, and conclusion; inspected locally and withheld.
- Source URL: https://arxiv.org/pdf/2406.06086
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Primary PDF source and integrity reference; inspected locally and withheld.
- Source URL: https://www.isca-archive.org/interspeech_2024/chen24k_interspeech.html
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Official Interspeech record, publication pages, DOI, and code locator.
- Source URL: https://doi.org/10.21437/Interspeech.2024-698
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Publisher DOI.
- Source URL: https://github.com/cyjie429/RawBMamba
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Official implementation README, evaluation commands, and README-reported result context; not executed.
- Source URL: https://zenodo.org/records/12743966
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Attributed code-archive availability and license context; not deposited.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Related audio representation and fusion synthesis; no claims transferred.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260731-Lattice%20Spoken%20LM/lattice_spoken_lm_manuscript.md
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Related speech representation and uncertainty synthesis; no claims transferred.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-APB2Face%20Safety/apb2face_safety_manuscript.md
  - Applies to: rawbmamba_manuscript.md.
  - Notes: Related synthetic-media safety and provenance synthesis; no claims transferred.
