# Report-Mark: AVA Vignetting Attack

## Source Metadata

- **Paper:** *AVA: Adversarial Vignetting Attack against Visual Recognition*
- **Authors:** Binyu Tian; Felix Juefei-Xu; Qing Guo; Xiaofei Xie; Xiaohong Li; Yang Liu
- **arXiv:** [2105.05558](https://arxiv.org/abs/2105.05558)
- **Venue:** IJCAI 2021 Main Track, pages 1046-1053
- **Publisher DOI:** [10.24963/ijcai.2021/145](https://doi.org/10.24963/ijcai.2021/145)
- **Submission date:** 2021-05-12
- **Subjects:** Image and Video Processing; Computer Vision and Pattern Recognition
- **Access date:** 2026-07-22
- **Source state:** complete local PDF and full-paper HTML verified before synthesis; source files withheld locally and not uploaded

## Selection, Deduplication, and Cache Record

A uniform random integer selected zero-based index 13,681 from 75,777 unique parent paper units derived from 75,780 PDFs. The first draw passed identifier, DOI, normalized-title, slug, 24-hour-marker, public-index, repository-artifact, automation-memory, worktree, and related-data checks. There were zero duplicate exclusions and zero reselections.

The initial source state was partial because full-paper HTML was absent. The valid PDF was preserved, an approved ar5iv full-paper fallback was acquired, and the local provenance and verification records were refreshed. The final gate passed with a 5,822,468-byte PDF carrying the required header and EOF marker and a 474,183-byte full-paper HTML document carrying 49,452 body characters, 29 heading markers, and six paper-structure terms. A `missing-only` extraction changed the cache state from miss to backfilled/cached; `pypdf`, HTML-regex, and source-package fallbacks succeeded. No source document or extracted text entered this repository.

## Concise Research Notes

### Problem

The paper asks whether image classifiers can be fooled by perturbations that resemble optical vignetting rather than conventional unconstrained pixel noise. Its motivating claim is that physically inspired spatial darkening may be both effective and visually natural.

### Method

The vignetting field is modeled as `V = A ⊙ G ⊙ T`: an off-axis illumination factor `A`, a geometric factor `G`, and a tilt factor `T`. RI-AVA optimizes four bounded physical parameters, while RA-AVA makes `G` elementwise tunable inside a learned closed curve. A level-set/Heaviside formulation and signed-gradient updates constrain this tunable region toward a physical reference field while optimizing the attack objective.

The experiments use 40 attack iterations and evaluate ResNet-50, EfficientNet-B0, DenseNet-121, and MobileNet-V2 on DEV, CIFAR-10, and Tiny ImageNet. Attack success rate is paired with the no-reference BRISQUE and NIQE quality metrics. Comparisons include MIFGSM, C&W L2, TIMIFGSM, Wasserstein perturbations, and cAdv.

### Evidence and Results

- In Table 1, RA-AVA reports 96.77%, 98.34%, 99.22%, and 99.18% white-box success on the four DEV models, while RI-AVA is substantially weaker. This supports the narrower claim that spatially tunable geometry is important within the authors' setup.
- RA-AVA is strongest in all 12 displayed CIFAR-10 transfer cells, but only 4 of 12 Tiny ImageNet transfer cells and none of the 12 DEV transfer cells. Across the 36 displayed transfer comparisons, it is highest in 16, so a general transfer-dominance claim would overstate the table.
- Table 3 reports that Zero-DCE improves Tiny ImageNet accuracy under RA-AVA by roughly 8.49 to 10.21 percentage points across the four models, but defended accuracy remains far below each clean baseline. This is evidence for partial mitigation, not recovery.
- The qualitative figures show smooth spatial darkening patterns and preserved scene recognizability to the reviewer. They do not substitute for a blinded human perceptual study or a physical-camera experiment.

### Internal Consistency Finding

The prose transfer discussion says that DEV adversarial examples crafted on ResNet-50 reach 37.21%, 40.75%, and 40.89% on the other three models with BRISQUE 11 and NIQE 37.04. Table 2 and the table source instead report 20.27%, 21.59%, and 23.97%, with BRISQUE 21.33 and NIQE 46.92. The source also retains commented draft values. This deposit treats the discrepancy as unresolved revision drift and preserves both records rather than silently selecting one.

### Limitations and Reproducibility

The paper provides no human perceptual study, physical optical realization, end-to-end camera test, official implementation, executable environment, trained weights, run-time or compute accounting, seed-level results, confidence intervals, or statistical tests. Dataset sample counts, splits, and training details are incomplete for reproduction. Evaluation is limited to four convolutional classifiers, three datasets, and one tested defense. “Imperceptible” and “physical” should therefore be read as hypotheses suggested by the parameterization and qualitative examples, not independently validated properties.

### Implementation Relevance and Safety Boundary

AVA is most useful here as a robustness-audit family: a structured photometric threat model can expose a blind spot that pixel-norm attacks miss. This report does not publish operational attack code. Its code mock-ups audit reported evidence, matrix coverage, and release readiness; they do not optimize adversarial images.

## Evidence and Attribution Notes

1. The complete PDF, full-paper HTML, and source representation support method, equation, table, and limitation claims.
2. The [official IJCAI proceedings page](https://www.ijcai.org/proceedings/2021/145) supports venue, pages, authors, and publisher DOI.
3. The [arXiv record](https://arxiv.org/abs/2105.05558) supports title, author list, submission date, subjects, and public source links.
4. [Papers with Code](https://paperswithcode.com/paper/ava-adversarial-vignetting-attack-against) was used only as a secondary negative implementation locator; it lists no implementation. Focused exact-title and identifier searches likewise found no official repository.
5. All numeric statements remain attributed to the paper unless explicitly described as reviewer arithmetic. No experimental reproduction was performed.

## Related DEP Entries

1. [Feature Denoising manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Feature%20Denoising/feature_denoising_manuscript.md) — **relevance:** a defense-side complement that places denoising blocks inside the representation pipeline and emphasizes matched adversarial training/evaluation. **Source basis:** its review of arXiv:1812.03411 and CVPR 2019 ablations.
2. [ViT Semantic Robustness manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md) — **relevance:** both studies use bounded image perturbations while raising a distinction between numerical smallness and semantic or perceptual stability. **Source basis:** its PRM-oriented medical-ViT evidence ledger and expert-validation recommendations.
3. [Adversarial Label Noise manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md) — **relevance:** it shows that robustness conclusions depend on threat-model, label, calibration, and held-out evaluation choices. **Source basis:** its synthesis of adversarial label mismatch and robust overfitting evidence.

## Synthesis Note

### Concept Bridge

AVA connects optical image formation, adversarial optimization, perceptual-quality assessment, and deployment assurance. The three related deposits supply missing controls: representation denoising for a defense comparison, semantic robustness for validating “imperceptibility,” and adversarial label-noise analysis for testing whether robustness survives changes in objective and evaluation protocol. Together they suggest treating optical perturbations as one axis in an evidence matrix rather than as a standalone benchmark.

### Potential Implementations (Exactly 3)

1. **Photometric robustness audit:** evaluate model accuracy and calibration over benign and adversarial vignette families, with matched clean controls and restoration baselines.
2. **Evidence consistency gate:** compare claims in prose, tables, and machine-readable results before approving a robustness report.
3. **Perceptual validation protocol:** pair BRISQUE/NIQE with blinded human ratings and, where relevant, a controlled camera/display acquisition study.

### Deeper Relationship Observations (Exactly 3)

1. RA-AVA's benefit over RI-AVA comes from increasing spatial degrees of freedom, which also weakens the inference that the resulting perturbation is physically realizable; effectiveness and physical plausibility move in tension.
2. Feature denoising and Zero-DCE intervene at different layers—representation versus input restoration—so a factorial comparison could distinguish whether failures arise from photometric preprocessing, feature extraction, or both.
3. Semantic-robustness and label-noise work imply that top-1 attack success alone can confound perceptual validity, semantic preservation, calibration, and objective mismatch; a strong audit must measure each separately.

### Conceptual Similarities (Exactly 3)

1. AVA and feature denoising both treat adversarial robustness as a structured signal-processing problem rather than only a generic norm ball.
2. AVA and ViT semantic robustness both motivate small or visually subtle input changes, while neither metric smallness nor qualitative inspection alone establishes semantic equivalence.
3. AVA and adversarial label-noise research both show that robustness is conditional on a chosen threat and training objective, making held-out evaluations necessary.

### MVP Implementations with Code Mock-Ups (Exactly 3)

1. **Prose/table consistency checker.** This bounded checker flags the published DEV transfer mismatch; it does not generate an attack.

   ```python
   table = {"transfer": [20.27, 21.59, 23.97], "brisque": 21.33, "niqe": 46.92}
   prose = {"transfer": [37.21, 40.75, 40.89], "brisque": 11.00, "niqe": 37.04}

   mismatches = {
       key: {"table": table[key], "prose": prose[key]}
       for key in table
       if table[key] != prose[key]
   }
   assert set(mismatches) == {"transfer", "brisque", "niqe"}
   ```

2. **Transfer-coverage counter.** The mock-up records which method leads each displayed transfer cell and prevents a local win from becoming an unsupported global claim.

   ```python
   leaders = {
       "DEV": ["cAdv"] * 12,
       "CIFAR-10": ["RA-AVA"] * 12,
       "Tiny-ImageNet": ["RA-AVA"] * 4 + ["cAdv"] * 8,
   }

   total = sum(len(values) for values in leaders.values())
   ra_ava_wins = sum(values.count("RA-AVA") for values in leaders.values())
   assert (ra_ava_wins, total) == (16, 36)
   ```

3. **Defensive release-readiness gate.** The gate refuses a broad physical-imperceptibility claim until independent evidence categories are present.

   ```python
   evidence = {
       "multi_seed_statistics": False,
       "human_perceptual_study": False,
       "physical_camera_test": False,
       "reproducible_environment": False,
       "adaptive_defense_evaluation": False,
   }

   missing = [name for name, present in evidence.items() if not present]
   decision = "hold broad claim" if missing else "eligible for independent review"
   assert decision == "hold broad claim"
   ```

### Developer Challenges (Exactly 3)

1. Reconstruct the paper's preprocessing, model checkpoints, and optimization details without an official implementation or environment record.
2. Implement differentiable photometric transformations while separating physically constrained parameters from RA-AVA's flexible spatial field.
3. Build a benchmark that preserves provenance, seed-level outputs, confidence intervals, calibration, perceptual ratings, and defense adaptations across datasets.

### Author Challenges (Exactly 3)

1. Reconcile the DEV transfer numbers in the prose with Table 2 and publish a machine-readable result table tied to the final manuscript version.
2. Support “imperceptible” with blinded human evaluation and “physical” with an end-to-end optical acquisition experiment.
3. Release code, environment, model/data recipes, seeds, compute costs, and uncertainty estimates sufficient for independent reproduction.

## Validation Notes

- The source-integrity gate passed before synthesis; the initial partial state was repaired and reverified.
- All eight PDF pages were visually inspected, including equations, figures, and the three result tables.
- Values were cross-checked between rendered tables, extracted text, and the source representation where available.
- The three Python mock-ups are non-operational defensive audit snippets and are subject to parser-based syntax validation before submission.
- No source file, cache, extracted source text, or local execution path is included in the public artifact set.
- No result was experimentally reproduced; confidence is high for bibliographic facts and transcription, moderate for broad generalization, and low for claims of physical realizability or human imperceptibility.

## Attribution Block

Primary research: Binyu Tian, Felix Juefei-Xu, Qing Guo, Xiaofei Xie, Xiaohong Li, and Yang Liu, *AVA: Adversarial Vignetting Attack against Visual Recognition*, IJCAI 2021, [arXiv:2105.05558](https://arxiv.org/abs/2105.05558), [DOI:10.24963/ijcai.2021/145](https://doi.org/10.24963/ijcai.2021/145). This public artifact is an independent source-grounded review. The paper's content remains the authors' work; reviewer arithmetic, comparisons, and proposed audit controls are clearly identified as derived analysis. Original source files were retained locally and were not uploaded.
