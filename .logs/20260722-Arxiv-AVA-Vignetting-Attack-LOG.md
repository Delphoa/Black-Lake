# Arxiv DEP Job Log: AVA Vignetting Attack

## Job Summary

This source-first review deposited a public-safe analysis of *AVA: Adversarial Vignetting Attack against Visual Recognition* (arXiv:2105.05558; IJCAI 2021). The paper studies adversarial perturbations expressed as camera-vignetting transformations. Source documents and extraction caches were retained outside the public repository and were not copied into this deposit.

## Random Selection

- Method: enumerate PDF files, collapse them to unique parent paper units, then use a uniform random integer draw over the resulting list.
- PDF count observed: 75,780.
- Candidate paper-unit count: 75,777.
- Zero-based random index: 13,681.
- Selection outcome: first draw accepted.
- Duplicate exclusions: 0.
- Reselections: 0.

## Deduplication Validation

The public dedup index, existing Black Lake logs, reports, DEP-E deposits, automation memory, active recent worktrees, and relevant Black-Lake-Data records were checked for the arXiv identifier, publisher DOI, normalized title, and slug. No existing Arxiv DEP package or same-paper marker within 24 hours was found. The dedup pointer was reserved as part of this deposit.

## Source Integrity and Cache

- Initial archive state: partial; the PDF was valid but full-paper HTML was absent.
- Repair: the valid PDF was preserved, and a full-paper HTML rendering was acquired from the approved ar5iv fallback after the official arXiv HTML route did not yield a usable full paper. Metadata, provenance, machine-readable summary, and verification records were refreshed locally.
- Final source state: complete and verified.
- PDF validation: 5,822,468 bytes, `%PDF-` header present, trailing `%%EOF` present.
- Full-paper HTML validation: 474,183 bytes, 49,452 body characters after script/style removal, document marker present, 29 heading markers, and six paper-structure terms detected.
- Partial artifacts: none.
- Extractor preflight: `pypdf`, HTML, and source-package fallbacks available; `pdftotext` unavailable.
- Cache trajectory: miss -> backfilled -> cached.
- Extraction mode: `missing-only`; PDF, HTML, and source-package text were extracted from the verified local paper unit without a network fetch during extraction.
- Source policy: all PDFs, HTML, source archives, extracted text, caches, and inspection renders were withheld locally; no source files were uploaded.

## Evidence Reviewed

The review inspected the complete eight-page paper, its full-paper HTML and TeX/source representation, figures and tables, the arXiv abstract record, the official IJCAI proceedings record and BibTeX, and a focused implementation search. No official code repository was located. The paper's reported numbers were transcribed as claims, not reproduced experimentally.

## Output Paths

- `.logs/20260722-Arxiv-AVA-Vignetting-Attack-LOG.md`
- `.logs/20260722-Arxiv-AVA-Vignetting-Attack-PHASE-LOG.md`
- `.reports/BL-Arxiv-AVA-Vignetting-Attack-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-AVA Vignetting Attack/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-AVA Vignetting Attack/ava_vignetting_attack_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Feature Denoising/feature_denoising_manuscript.md` — a defense-side counterpart focused on representation-level denoising and matched adversarial evaluation.
2. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` — a direct bridge from small pixel-space changes to the need for semantic and perceptual validation.
3. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` — a complementary account of threat-model-specific robustness, calibration, and held-out attack evaluation.

## Exactly Three Next-Review Questions

1. Does RA-AVA remain effective under modern augmentations, restoration defenses, and adversarially trained vision backbones when evaluated with multiple seeds and confidence intervals?
2. Can a controlled camera-and-display experiment distinguish a realizable optical vignette from a purely digital perturbation while preserving the attack's reported success?
3. How do human perceptual judgments compare with BRISQUE and NIQE when the same images are assessed for visibility, naturalness, and semantic preservation?

## Exactly Three Challenges

1. The initial archive unit lacked full-paper HTML and had to pass a bounded repair-and-verification gate before review.
2. The prose discussion of one DEV transfer result conflicts materially with Table 2, so the deposit preserves both records and avoids choosing an unsupported value.
3. Reproducibility is constrained by the absence of an official implementation, execution environment, seeds, uncertainty estimates, and a demonstrated physical-camera evaluation.

## Submission Record

- Status: deposited to the default branch and remotely verified.
- Primary commit: [4000bc7283145a6a128ffe0c66ff63c8a2bd14b3](https://github.com/Delphoa/Black-Lake/commit/4000bc7283145a6a128ffe0c66ff63c8a2bd14b3).
- Slack notification: delivered to `#black-lake-artifacts`.
- Public-source policy: source files withheld locally; no source files uploaded.
