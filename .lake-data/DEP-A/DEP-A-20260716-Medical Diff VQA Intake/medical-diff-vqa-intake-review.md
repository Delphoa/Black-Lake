# Longitudinal Medical VQA as Alignment, Structured Change, and Calibrated Answering

## A whitepaper-grade archival intake review and independent re-conceptualization of the complete Medical Diff VQA DEP-E record

**Artifact prepared:** 2026-07-16

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA`

**Source commit:** `b5ad2459a6ee3d649feb8209d9390d86d475502c`

**Paired task indicator:** `BL-DEPPAIR-20260716-672AC475`

**Direction:** `DEP-E -> DEP-A`

**Source provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes

**Review scope:** complete two-file DEP-E repository record, canonical arXiv identity and abstract, dataset and model reconstruction, quantitative and ablation audit, clinical evidence boundary, independent re-conceptualization, and replication agenda

**Reproduction boundary:** the current intake did not independently re-read the external full paper, access MIMIC-CXR, download Medical-Diff-VQA, execute code, retrain detectors, or reproduce any metric. Detailed paper-level and repository-level content is attributed to the DEP-E report, which records complete source inspection.

---

## Executive assessment

The source record reviews a difference-aware medical visual question answering system and the Medical-Diff-VQA benchmark built from longitudinal chest radiographs.[^paper] Instead of asking only what is visible in one image, the task asks what changed between a prior and current examination. The reported dataset contains 700,703 question–answer pairs derived from 164,324 image pairs and spans seven question types. The model detects anatomical and disease concepts, constructs spatial, semantic, and implicit graphs for each examination, learns difference-aware representations, and combines them with the question to produce closed or open answers.

The principal reported result is improved aggregate and closed-question performance over comparison systems. The DEP-E records total accuracy of 60.2 versus 54.7 for MMQ and closed accuracy of 84.9 versus 74.2. Open accuracy is 36.6, below MMQ’s reported 40.5. For difference-answer generation, reported values include BLEU-4 .434, METEOR .339, ROUGE-L .577, and CIDEr 1.027. These numbers support a representation benefit on the benchmark, especially for constrained answers. They do not support a claim that the system is generally better on every task, and they do not establish clinical usefulness.

The source report handles internal tensions well. Human validation is reported as 1,657 correct items out of a 1,700-item sample. That fraction is approximately 97.47%, while the paper’s prose and table are represented as 97.33% and 97.4% in different places. The discrepancy is small but should be preserved. The full graph is not best in every ablation cell: individual semantic or implicit components lead some metrics. A question-only degradation suggests that images contribute information, but it does not eliminate language shortcuts or answer-prior exploitation.

Reviewer judgment: the record supports Medical-Diff-VQA as a valuable research benchmark and supports the claim that expert-structured graph relations can improve difference-aware answer prediction under its evaluation. The open-answer weakness and evidence design prevent stronger conclusions. The next conceptual step is to separate pair alignment, change-state estimation, uncertainty, and language rendering. A clinically meaningful system should first produce a calibrated structured change record with provenance, then answer questions from that record. Free-form text should not be the only observable intermediate.

## 1. Problem framing and research question

Longitudinal radiology reasoning is not equivalent to independently classifying two images and subtracting labels. The images can differ in projection, patient position, inspiration, exposure, support devices, crop, and acquisition interval. A true clinical change can be local or diffuse, newly present, resolved, worsened, improved, or stable. A useful system must align comparable anatomy, recognize findings, represent relations, and communicate the difference in the terms requested by a question.

The reviewed paper asks whether expert knowledge expressed as graphs can improve visual representation learning for this task. It also contributes a large automatically constructed QA dataset to make the problem trainable and measurable. The benchmark includes direct questions about one image and difference questions across image pairs. Answers can be closed categories or open text.

The task has two coupled uncertainties. First, the image evidence may be ambiguous or technically incomparable. Second, the automatically generated question and reference answer may not faithfully encode the source report or clinically salient change. A model can be penalized for a reasonable paraphrase, rewarded for a dataset prior, or evaluated on a question whose premise is incomplete.

The source positions graph structure as an inductive bias. Anatomical nodes provide a stable spatial frame; disease nodes encode findings; spatial edges describe geometry; semantic edges encode expert relationships; implicit edges are learned. Difference-aware graph comparison can then focus on changes instead of relearning all relations from pooled image features.

## 2. Formal and technical reconstruction

### 2.1 Dataset construction

The DEP-E reports that the dataset is derived from MIMIC-CXR, a large deidentified chest-radiograph collection with reports and longitudinal studies.[^physionet] Image pairs are formed for the same patient across examinations. Rules and templates transform report content and structured finding relationships into seven question families and reference answers. The resulting scale—700,703 QA pairs across 164,324 pairs—supports deep learning but also makes automated-generation assumptions central to validity.

Human validation samples 1,700 generated examples. The reported correct count of 1,657 indicates high surface-level correctness, but the sample design matters: how cases were selected, which question types were represented, who annotated them, what counted as correct, and whether ambiguity was allowed. The current intake relies on the DEP-E’s account and does not independently access patient-derived data.

### 2.2 Visual and graph representation

The model begins with Faster R-CNN-style detectors for anatomical regions and disease findings. Detector features become graph nodes. Spatial graphs encode position or relative anatomy. Semantic graphs encode known relations among anatomical structures and diseases. Implicit graphs learn relations not fixed by explicit knowledge.

For a prior/current pair, graph representations are compared through relation-aware attention or message passing. Difference features should emphasize nodes and edges whose state changes between studies while retaining stable context. The question representation conditions which changes matter. A question about pleural effusion should attend differently from one about support devices or anatomic location.

The DEP-E describes the model as expert knowledge-aware because semantic structure is not learned entirely from task labels. That label should be scoped: encoded relations are expert-inspired priors, not proof that every internal edge has clinical causal meaning. Detector errors can propagate into all three graphs, and learned implicit edges are not automatically interpretable.

### 2.3 Answer generation

Closed questions are treated as classification over a bounded answer vocabulary. Open questions require generation or prediction over a larger set of phrases. These regimes differ sharply. High closed accuracy can reflect both useful vision and strong answer priors. Open answers are sensitive to wording and require compositional detail.

The reported evaluation includes accuracy and common language-generation metrics. BLEU, METEOR, ROUGE, and CIDEr measure lexical overlap in different ways. In a medical setting, lexical overlap is not the same as factual or clinical correctness. “No new opacity” and “new opacity” differ by one token but reverse meaning. A robust evaluation needs entity, relation, temporality, negation, and severity scoring in addition to text similarity.

### 2.4 Difference representation as latent state transition

A useful formalization is to treat each examination as an uncertain structured state `S_t` over anatomy, finding, severity, location, and device variables. Pair alignment `A` maps comparable regions. The change record is not simple subtraction but a posterior `P(Delta S | I_prior, I_current, A)`. The question `q` selects a projection of this posterior, and the answer renderer converts that projection into a categorical or textual output.

This state-transition formulation is reviewer inference. It makes uncertainty explicit and separates clinical content from phrasing. The paper’s graph architecture approximates parts of this pipeline, but the reviewed benchmark evaluates final answers rather than a fully calibrated intermediate change record.

## 3. Evaluation design and evidence reconstructed

The paper’s empirical design, as reconstructed by the DEP-E, includes dataset validation, comparisons with VQA baselines, graph-component ablations, question-only or modality comparisons, and separate reporting for closed, open, direct, and difference questions. Tables 1–6 and architecture figures are materially covered in the source report.[^dep] The current intake read both tracked files fully but did not independently inspect original table pixels or run the repositories.

The canonical arXiv record confirms the title, nine authors, v2 revision, computer-vision classification, and abstract-level contribution of expert knowledge-aware image-difference graph representation learning for difference-aware medical VQA.[^arxiv] The DEP-E also records KDD publication, official PhysioNet data resources, and two public GitHub repositories. Those locators improve reproducibility in principle, but access to MIMIC-derived data is governed and was not attempted here.

The comparison design supports benchmark-level relative claims. It is less informative about clinical validity because all models are evaluated within the same generated dataset and source domain. There is no reported prospective reader study, external hospital evaluation, deployment workflow, calibration audit, fairness analysis, or outcome measurement.

Question-only performance is a useful negative control. A gap between question-only and full multimodal performance demonstrates that visual features add predictive information. It does not show that the system uses the correct radiographic evidence or that it is robust to counterfactual image changes. Causal faithfulness would require interventions: alter or mask the relevant region, swap prior/current order, or construct controlled pairs where only one finding changes.

## 4. Results and quantitative audit

The scale figures imply about 4.26 QA pairs per image pair on average (`700,703 / 164,324`), a reviewer calculation. This average hides variation across question types and patients. Dataset splits must be patient-disjoint to prevent leakage through repeated anatomy and report style; the DEP-E should be consulted for the paper’s exact split protocol, and this intake does not independently verify it.

The human-validation arithmetic is straightforward: `1,657 / 1,700 = 0.974705...`, or approximately 97.47%. The reported table value 97.4% is compatible with truncation or another aggregation; a prose value of 97.33% is not the direct rounded fraction. Possible explanations include a typo, a different denominator, or averaging by subgroup. The discrepancy is not large enough to invalidate the dataset, but it should be reconciled in future documentation.

The main comparison shows a 5.5-point absolute total-accuracy gain over MMQ and a 10.7-point closed-accuracy gain. Open accuracy is 3.9 points lower than MMQ. Thus the aggregate improvement is driven substantially by the closed regime. A weighted total can favor the model if closed questions are common. Without per-type support counts and confidence intervals, the stability and clinical significance of those differences cannot be judged.

Reported generation metrics—BLEU-4 .434, METEOR .339, ROUGE-L .577, and CIDEr 1.027—provide a multidimensional lexical view but no uncertainty estimates. The DEP-E also records an IDCPCL ROUGE value of .582 in comparison context. Small metric differences can be sensitive to tokenization and reference count. Reproduction must fix evaluation scripts and versions.

The source reports that the full graph does not dominate every ablation. This prevents a simplistic “every component always helps” conclusion. If the semantic-only or implicit-only configuration leads selected metrics, interactions may introduce optimization difficulty, redundancy, or noise. Statistical variation across runs is needed before interpreting one-cell reversals.

## 5. Ablations and missing discriminators

The reported ablations vary graph components and input modalities. They establish that structure matters under the chosen training and evaluation protocol, but several discriminators remain.

1. **Detector oracle versus predicted nodes:** substitute ground-truth anatomy/finding nodes where available to measure error propagation.
2. **Alignment ablation:** compare explicit registration, learned matching, and no alignment under controlled acquisition differences.
3. **Prior/current swap:** answers about improvement, worsening, new, and resolved findings should transform predictably.
4. **Counterfactual region edit:** change a relevant image region while holding language constant to test causal visual use.
5. **Question-template split:** hold out templates or paraphrase families to test generalization beyond wording.
6. **Patient and site shift:** evaluate on external data with different devices, protocols, demographics, and reporting styles.
7. **Graph-edge randomization:** preserve degree distributions while permuting semantic edges to test whether knowledge content, not graph capacity, drives gains.
8. **Uncertainty head:** require abstention when images are incomparable or evidence is ambiguous.

No ablation can by itself demonstrate clinical utility. The relevant outcome would be improved, calibrated clinician performance or safer workflow decisions under prospective conditions.

## 6. Claim-by-claim vetting

| Claim | Evidence | Assessment |
|---|---|---|
| Medical-Diff-VQA is a large longitudinal chest-radiograph QA dataset. | DEP-E-reported counts and official resource locators. | Supported; data were not independently accessed in this intake. |
| Generated QA pairs are approximately 97.4% correct in the validation sample. | 1,657 of 1,700 reported correct; table/prose discrepancy noted. | Broadly supported for the sample; exact percentage reporting needs reconciliation. |
| Expert graph structure improves total benchmark performance. | Main comparison and graph ablations reported in the DEP-E. | Supported under the evaluated protocol. |
| The full model is best on every metric. | Some component ablations lead individual cells; open accuracy trails MMQ. | Rejected. |
| Images contribute beyond question priors. | Question-only degradation reported. | Supported as an information-contribution claim; not proof of causal visual grounding. |
| Lexical metrics establish clinical correctness. | BLEU, METEOR, ROUGE, and CIDEr compare generated text. | Unsupported; factual, temporal, and negation errors need dedicated scoring. |
| Benchmark gains imply clinical utility. | No prospective clinical evaluation reported. | Unsupported. |
| Public code and data make results independently reproduced. | Repositories and PhysioNet records exist, but this run did not execute them and access may require governance. | Reproducibility resources exist; reproduction not demonstrated here. |

## 7. External primary-source context

The canonical arXiv record identifies the paper as “Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering,” submitted in 2023 and revised to v2 in 2024.[^arxiv] The KDD DOI retained by the source record supplies venue provenance.[^doi] The official PhysioNet page and public repositories provide dataset and implementation routes.[^data][^code]

MIMIC-CXR is a governed deidentified resource. A public URL does not mean unrestricted redistribution. This DEP-A contains no radiograph, report, patient-derived data, model weights, or cache. Reproduction should follow the applicable credentialing, data-use, privacy, and security rules.

The external context underscores why longitudinal evaluation is a separate problem from ordinary VQA. Clinical reports often compare with prior studies, and change direction is decision-relevant. However, report-derived QA generation inherits report omissions and practice patterns. The benchmark is therefore evidence about a particular research task, not a complete model of longitudinal diagnosis.

The current intake directly inspected only canonical paper metadata and abstract. Dataset, code, table, and clinical-detail claims remain attributed to the complete DEP-E report rather than presented as independently verified external facts.

## 8. Research notes, caveats, and code/reproducibility status

The source reports public code repositories and PhysioNet resources, but no code was executed in this run. There was no dependency audit, commit pinning, environment reconstruction, data checksum validation, training replay, or metric recomputation. Reproduction status is therefore “resources identified; results not reproduced.”

Dataset generation can introduce correlated errors at enormous scale. A 2.5% surface error rate across 700,703 items would still correspond to many thousands of examples, and clinically important error types may be nonuniform. Validation should stratify by question type, finding rarity, answer polarity, time interval, image quality, and patient subgroup.

Closed accuracy is particularly vulnerable to class imbalance. A per-class macro score, calibration plot, and prevalence-matched baseline would reveal whether performance reflects common answers. Open answers need semantic scoring that is robust to acceptable paraphrase yet sensitive to negation and temporal direction.

The detector layer creates a bottleneck. If anatomy or disease detection is wrong, graph reasoning can be internally consistent but clinically false. Visualizing attention or graph edges does not establish faithfulness. Intervention tests should measure whether the answer changes for the right visual reason.

Clinical deployment also requires abstention. Some pairs cannot be compared because projection or field of view differs. A forced answer can sound confident while the evidence is inadequate. The benchmark should include “not comparable” and “insufficient evidence” states when justified.

## 9. Independent re-conceptualization

The paper can be extended into a **provenance-aware change ledger**. For each anatomical region and finding, record:

- prior state and confidence;
- current state and confidence;
- alignment confidence;
- inferred change category: new, resolved, improved, worsened, stable, or indeterminate;
- supporting image regions and detector versions;
- acquisition comparability flags;
- source timestamps and study identifiers;
- uncertainty and abstention rationale.

The VQA answer becomes a query over this ledger rather than the only output. Closed questions retrieve a constrained field. Open questions render selected ledger entries into language. This design makes errors localizable: alignment, observation, transition inference, question parsing, or rendering.

Graph structure fits naturally. Anatomy nodes anchor the ledger; disease and device nodes carry states; semantic edges constrain plausible relations; implicit edges suggest candidates but should not be promoted to clinical facts without evidence. Temporal edges represent transitions explicitly rather than collapsing two graphs into one latent vector.

Evaluation should be hierarchical. First score alignment. Then score finding states and transition direction. Then score question selection. Finally score textual rendering. End-to-end answer metrics remain useful but no longer conceal where the system failed. This is a reviewer proposal, not a system evaluated in the source.

The architecture also supports governance. Each answer can cite the change-ledger fields and model versions used. A clinician can override an incorrect state, and the correction can be tracked without editing the original image. Calibration can be measured at the ledger level, and abstention can be tied to acquisition mismatch or uncertain findings.

## 10. Implications and failure modes

For research, the benchmark demonstrates that relational structure can help compare medical images at scale. For product design, it warns against treating final answer accuracy as the only observable. For governance, it highlights the need to separate patient-derived evidence, generated labels, learned representations, and human-facing output.

Failure modes include:

1. **Temporal inversion:** prior and current images are swapped, reversing “new” and “resolved.”
2. **Registration confounding:** projection or positioning differences are mistaken for pathology change.
3. **Detector cascade:** an upstream missed finding makes graph reasoning confidently wrong.
4. **Language shortcut:** question templates predict common answers without relevant visual evidence.
5. **Negation loss:** lexical similarity rewards a clinically opposite statement.
6. **Closed-class inflation:** high accuracy on common categorical answers dominates aggregate performance.
7. **Graph authority illusion:** expert-labeled edges are treated as patient-specific causal evidence.
8. **Domain shift:** external devices, sites, and reporting practices break learned relations.
9. **Uncalibrated certainty:** the model answers when pairs are incomparable.
10. **Privacy leakage:** patient-derived data or memorized text is exposed through training or outputs.

Mitigation requires patient-disjoint splits, external validation, intervention tests, calibrated abstention, semantic error taxonomies, security controls, and prospective human-factor studies.

## 11. Replication, falsification, and hypothesis agenda

The following are reviewer proposals.

**H1 — Structured transition supervision improves open answers.** Training an explicit change ledger before language generation will improve factual transition accuracy and reduce negation errors relative to end-to-end answer training. Falsification: no improvement on blinded clinician-labeled transitions and external data.

**H2 — Graph gains depend on relation semantics.** Semantically correct expert edges will outperform degree-matched randomized edges across repeated seeds. Falsification: randomized graphs perform equivalently, suggesting capacity rather than knowledge drives gains.

**H3 — Alignment confidence predicts error.** Answer error rates will rise monotonically as acquisition-comparability and region-alignment confidence fall. Falsification: no relationship after controlling for question type.

**H4 — Counterfactual visual edits expose shortcuts.** Models with genuine difference grounding will change answers predictably when a relevant finding is inserted or removed while remaining stable to irrelevant edits. Falsification: answers track question priors rather than controlled evidence.

**H5 — Abstention improves clinical utility.** A calibrated indeterminate option will reduce harmful false change claims at an acceptable coverage cost in a reader study. Falsification: abstention fails to improve risk-weighted clinician performance.

A replication should pin code commits, dependencies, random seeds, detector checkpoints, data version, patient split, and question-generation rules. It should reproduce all tables with confidence intervals over seeds, reconcile the 1,657/1,700 percentage, and verify evaluation scripts. Dataset auditing should sample every question type and rare answer class.

A clinical falsification program should use external-site pairs, expert annotations of change and comparability, prospective time-ordering, and predefined harm weights. Clinicians should evaluate both correctness and whether the answer helps or distracts. Privacy and access controls should be audited separately from model quality.

## 12. Durable restatement

The complete DEP-E record supports a bounded conclusion. Medical-Diff-VQA provides a large report-derived longitudinal chest-radiograph QA task. The reviewed expert-graph model uses anatomical, disease, spatial, semantic, and learned relations to represent image differences. It improves aggregate and closed-question performance under the reported benchmark, while open accuracy remains weaker than one comparison and individual graph ablations lead some metrics.

The evidence does not establish clinical utility, causal visual grounding, fairness, calibration, privacy safety, or external robustness. No result was reproduced in this intake.

The reviewer’s durable design recommendation is to make change representation an auditable intermediate object. Align the pair, estimate structured states and transitions with uncertainty, preserve provenance, and generate answers from that ledger. This turns final text from an opaque endpoint into one view of a testable longitudinal model.

## 13. Source and evidence notes

### Complete inventory and source integrity

| Item | Inspection | Role | Integrity assessment |
|---|---|---|---|
| Source `README.md` | Read end to end | Identity, inventory, resources, summary, associations, attribution | Complete public boundary and source routing. |
| `medical_diff_vqa_whitepaper.md` | Read end to end | Dataset, architecture, tables, ablations, limitations, reproduction status, coverage | Complete DEP report; reports full primary and public-resource inspection. |
| Canonical arXiv record | Directly inspected | Title, authors, v2, abstract, identifiers, access links | Primary metadata; body not independently re-read. |
| Generated review | New derived artifact | Intake, quantitative audit, re-conceptualization, hypotheses | Original prose; no data, code, or source copied. |

### Coverage ledger

| Source dimension | Coverage in this review | Boundary |
|---|---|---|
| Dataset construction and seven types | Framing and technical reconstruction | DEP-E-reported details. |
| Human validation | Results and claim table | Arithmetic recomputed; sampling not independently audited. |
| Detectors and graph components | Technical reconstruction | Architecture represented; code not executed. |
| Tables 1–6 and main metrics | Evaluation and quantitative audit | Values from DEP-E; original tables not re-opened. |
| Ablations and question-only control | Evaluation, ablations, claim table | Limits and missing controls explicit. |
| Figures | Technical reconstruction and coverage | Concepts represented; original graphics not inspected here. |
| Code and data resources | External context and research notes | URLs retained; no download or execution. |
| Clinical limitations | Executive, research notes, implications | No clinical-readiness claim. |
| Re-conceptualization | Section 9 | Reviewer proposal only. |
| References and provenance | Footnotes and README attribution | No patient-derived or source document uploaded. |

### Evidence boundary

The complete DEP-E report is the source for dataset, architecture, table, figure, code, and clinical-detail claims. Directly inspected primary evidence in this run is limited to canonical arXiv metadata and abstract. Reviewer inference includes the state-transition formalization, change ledger, proposed controls, and hypotheses. No data, model, code, detector, result, or clinical workflow was independently reproduced.

The paper reports the benchmark outcomes summarized here; the current intake attributes them to the DEP-E rather than claiming reproduction. The paired record preserves review-only provenance and no source-file transfer.[^provenance]

## 14. Footnotes

[^paper]: Xinyue Hu et al., “Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering,” arXiv:2307.11986v2, https://arxiv.org/abs/2307.11986v2.
[^dep]: Complete source record, https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA, inspected at commit `b5ad2459a6ee3d649feb8209d9390d86d475502c`.
[^arxiv]: Canonical arXiv metadata and abstract, https://arxiv.org/abs/2307.11986.
[^doi]: KDD publication DOI, https://doi.org/10.1145/3580305.3599819.
[^physionet]: MIMIC-CXR v2.1.0 resource, https://physionet.org/content/mimic-cxr/2.1.0/.
[^data]: Medical-Diff-VQA resource, https://physionet.org/content/medical-diff-vqa/1.0.1/.
[^code]: Public repositories reported by the DEP-E, https://github.com/Holipori/MIMIC-Diff-VQA and https://github.com/Holipori/Medical_Diff_VQA.
[^provenance]: Paired task `BL-DEPPAIR-20260716-672AC475` records review-only derivation; no DEP-E file was modified, moved, or copied.
