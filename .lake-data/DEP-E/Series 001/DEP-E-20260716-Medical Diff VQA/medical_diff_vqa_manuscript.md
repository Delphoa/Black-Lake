---
title: "Medical Diff VQA - DEP-E"
generated_at: "2026-07-16 (public-safe date; exact execution timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of expert-knowledge graph learning for longitudinal chest-X-ray difference visual question answering."
source_status: "verified complete local PDF, full-paper HTML, metadata HTML, and TeX source; public URLs cited; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "Sources and repository context inspected through 2026-07-16."
primary_url: "https://arxiv.org/abs/2307.11986"
stable_identifier: "arXiv:2307.11986v2; DOI:10.1145/3580305.3599819"
confidence_summary: "High for identity, method, tables, dataset counts, and stated limits; medium for reviewer synthesis; low for independent reproducibility because code and experiments were not run."
safety_scope: "clinical decision-support research review; retrospective, evaluation-only, non-diagnostic implementation guidance"
distribution_notes: "No PDF, HTML, source archive, extracted text, cache, clinical record, image, model checkpoint, local path, or exact local execution detail is redistributed."
---

# Medical Diff VQA - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Canonical metadata | HTML | arXiv:2307.11986v2 | https://arxiv.org/abs/2307.11986 | Public metadata; arXiv distribution terms apply. | 2026-07-16 | Inspected. |
| S2 | arXiv full-paper HTML | Primary paper | HTML | arXiv:2307.11986v2 | https://arxiv.org/html/2307.11986 | Complete paper rendering; local copy withheld. | 2026-07-16 | Inspected in full. |
| S3 | arXiv PDF | Primary paper | PDF | arXiv:2307.11986v2 | https://arxiv.org/pdf/2307.11986 | Verified local copy withheld. | 2026-07-16 | Inspected. |
| S4 | arXiv source package | Primary source | TeX archive | arXiv:2307.11986v2 | https://arxiv.org/e-print/2307.11986 | Used locally to cross-check tables, equations, figures, and appendices; withheld. | 2026-07-16 | Inspected. |
| S5 | KDD publication DOI | Persistent publication record | DOI | 10.1145/3580305.3599819 | https://doi.org/10.1145/3580305.3599819 | KDD 2023 publication locator; publisher full text was not separately fetched. | 2026-07-16 | Metadata cross-checked through primary/official records. |
| S6 | Medical-Diff-VQA | Official dataset record | PhysioNet database | v1.0.1; DOI:10.13026/e6dd-cn74 | https://physionet.org/content/medical-diff-vqa/1.0.1/ | Credentialed access; derivative of MIMIC-CXR; data-use rules apply. | 2026-07-16 | Record inspected; dataset not downloaded. |
| S7 | MIMIC-CXR | Source dataset record | PhysioNet database | v2.1.0; DOI:10.13026/4jqj-jw95 | https://physionet.org/content/mimic-cxr/2.1.0/ | Credentialed access; DUA forbids sharing and re-identification attempts. | 2026-07-16 | Record inspected. |
| S8 | Medical-Diff-VQA repository | Official data-generation implementation | GitHub repository | main branch | https://github.com/Holipori/MIMIC-Diff-VQA | Regeneration instructions visible; no repository license was established in this review. | 2026-07-16 | README inspected; code not run. |
| S9 | EKAID repository | Official model implementation | GitHub repository | main at observed commit `1e5dd0de91554515d2acc83ad402e810ace0a5d7` | https://github.com/Holipori/EKAID | Feature extraction, training, testing, and UI instructions; no release or license was established. | 2026-07-16 | READMEs inspected; code not run. |
| S10 | VLM Probing DEP | Related research artifact | Markdown | DEP-E-20260712-VLM Probing | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Repository-generated review. | 2026-07-16 | Inspected. |
| S11 | OViP Preference DEP | Related research artifact | Markdown | DEP-E-20260714-OViP Preference | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Repository-generated review. | 2026-07-16 | Inspected. |
| S12 | VideoWeave Geometry DEP | Related research artifact | Markdown | DEP-E-20260709-VideoWeave Geometry | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Repository-generated review. | 2026-07-16 | Inspected. |
| S13 | Local archive integrity records | Private processing evidence | README/CSV/JSON | arXiv:2307.11986v2 | Local path withheld | Source documents and processing records remain local; no source upload authorized. | 2026-07-16 | Verified complete after repair. |

The canonical record lists Xinyue Hu, Lin Gu, Qiyuan An, Mengliang Zhang, Liangchen Liu, Kazuma Kobayashi, Tatsuya Harada, Ronald M. Summers, and Yingying Zhu. Version 1 was submitted on 2023-07-22 and version 2 on 2024-08-27. The published paper appears in KDD 2023, pages 4156-4165. The paper calls the dataset MIMIC-Diff-VQA; the current official PhysioNet record calls it Medical-Diff-VQA.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5, S6 | Canonical/official metadata | Title, authors, dates, venue, DOI, current dataset name/version, publication citation. | Source identity and publication context. | High | Metadata alone does not validate methods or results. |
| E2 | S2-S4 | Primary paper and source | Introduction, dataset construction, method, equations, Tables 1-6, appendices, conclusion. | Mechanism, counts, evaluation, numerical results, and source-disclosed limits. | High for faithful reporting | Experiments and calculations were not independently reproduced. |
| E3 | S6, S7 | Official dataset records | Category counts, credentialed access, source-dataset scale, de-identification, DUA, and ethics notes. | Dataset availability, governance, and provenance boundary. | High | Dataset contents were not downloaded or audited. |
| E4 | S8 | Official data code | README workflow for MIMIC mapping, report parsing, KeyInfo extraction, and QA generation. | Regeneration pathway and randomness caveat. | Medium-high | Code was not executed; environment and outputs were not verified. |
| E5 | S9 | Official model code | Python 3.6 requirement, feature-extraction prerequisites, graph training flags, checkpoint/testing instructions, server-client demo. | Implementation availability and burden. | Medium-high | Dependencies, checkpoints, license, and runtime were not independently validated. |
| E6 | S10-S12 | Related DEP artifacts | Multimodal probing, visual grounding/hallucination evaluation, paired-view geometry consistency. | Cross-DEP synthesis and implementation design. | Medium | Related artifacts do not validate this paper's results. |
| E7 | S13 | Private integrity/process evidence | PDF/HTML/source verification, repair status, random draw, and dedup checks. | Source completeness and selection eligibility. | High | Local paths and files are intentionally withheld. |

## Executive Summary

The paper introduces difference visual question answering for longitudinal chest X-rays: a model receives a present image, an earlier reference image from the same patient, and a question, then answers about current findings or change. The accompanying Medical-Diff-VQA dataset contains 700,703 QA pairs derived from 164,324 image pairs and seven question types. The paper also proposes an expert-knowledge graph model that aligns anatomy and disease features, builds spatial, semantic, and implicit relations for each image, learns relation-aware graph representations, computes change, and generates an answer.

The strongest reported evidence has three parts. First, 1,700 randomly sampled QA pairs were checked by three human verifiers, with 1,657 labeled correct (97.4% in the table; 97.33% in prose). Second, on six non-difference question types, the proposed generative model reports total exact-match accuracy of 60.2 versus 54.7 for MMQ, with stronger closed-question accuracy (84.9 versus 74.2) but weaker open-question accuracy (36.6 versus 40.5). Third, on difference questions, the proposed method reports stronger BLEU-1/2/3/4, METEOR, and CIDEr than MCCFormers and IDCPCL, while IDCPCL reports slightly higher ROUGE-L (0.582 versus 0.577).

The evidence supports a useful research task, a large derivative dataset, and a plausible structured baseline. It does not establish clinical safety, prospective benefit, causal explanation, subgroup fairness, patient-level leakage resistance, or generalization beyond the source institutions and data pipeline. The graph ablation is also mixed: the full graph leads or ties several BLEU metrics, but implicit-only or semantic-only settings are strongest on some BLEU-1, METEOR, ROUGE-L, and CIDEr values. Reviewer confidence is high for source reporting, medium for the broader design pattern, and low for clinical deployment or independent reproducibility.

## Detailed Summary

### Problem Context

Single-image labels, report generation, and conventional medical VQA can miss the comparative reasoning used in longitudinal radiology. Disease changes are often subtle, while acquisition pose, scale, projection, and nonrigid anatomy can vary more than pathology. Direct pixel- or patch-coordinate comparison can therefore confuse acquisition variation with clinical change. The paper reframes the task around questions that explicitly compare a current study with an earlier study from the same patient.

### Dataset Construction

Medical-Diff-VQA is derived from MIMIC-CXR. Patients with only one radiology visit are excluded. Earlier studies become references and later studies become main/current studies. The first six question types—abnormality, presence, view, location, type, and level—refer to the main image; the seventh type asks about differences across the pair. The released category counts sum to 700,703: abnormality 145,421; location 84,193; type 27,478; level 67,296; view 56,265; presence 155,726; and difference 164,324.

Construction follows an Extract-Check-Fix cycle. ScispaCy and manual review help build abnormality and attribute keyword libraries. Rules extract positive findings, attributes, and negations from reports into an intermediate KeyInfo representation. Automated and manual checks compare extraction with parts of speech, biomedical entities, and MIMIC-CXR-JPG labels; rules are refined before QA generation. The official repository warns that regeneration is stochastic and may not reproduce the provided dataset exactly.

### Dataset Validation

Three verifiers assessed 1,700 sampled QA pairs alongside reports: 475/500, 989/1,000, and 193/200 were marked correct. The total is 1,657/1,700, or 97.47% by direct division and 97.4% as rounded in the table; the prose reports 97.33%. The sample supports high rule-output correctness under the paper's review protocol, but the source does not provide confidence intervals, inter-rater overlap/agreement, stratification by question type, patient, or clinical severity, or an independent external audit.

### Feature Extraction and Graph Construction

For each image, a Faster R-CNN trained on Chest ImaGenome extracts 26 anatomical structures and region features. A second Faster R-CNN trained on VinDr-CXR supplies disease features from corresponding anatomical regions. Questions are tokenized with GloVe embeddings and encoded through a bidirectional GRU plus self-attention.

Each image becomes a graph with anatomical and disease nodes, each conditioned on the question. Three edge families encode different assumptions:

- Spatial edges describe overlap, containment, and directional relationships between region boxes, with 11 relation classes and a distance threshold.
- Semantic edges use an anatomical knowledge graph and a label co-occurrence graph to connect clinically related structures or findings.
- Implicit edges form a fully connected complement intended to learn relationships not captured explicitly.

Relation-aware graph attention produces a representation for each image. The architecture then forms an image-difference representation and passes it to an attention-equipped answer generator. The main conceptual bet is that anatomy supplies a more stable correspondence system than raw image coordinates.

### Experimental Setup

The paper reports PyTorch training with Adam at learning rate 0.0001 for 30,000 iterations, batch size 64, two RTX 3090 GPUs, and 3 hours 49 minutes of training. Bounding-box features are 1,024-dimensional. Word features are 600-dimensional and include 300-dimensional GloVe vectors. Generated text is evaluated with BLEU, METEOR, ROUGE-L, and CIDEr through the COCO caption evaluation toolkit. MMQ comparison uses exact-match accuracy on the six non-difference question types; difference questions use MCCFormers and IDCPCL baselines.

### Main Results

For non-difference questions, MMQ reports open 40.5, closed 74.2, and total 54.7 accuracy. The proposed model reports open 36.6, closed 84.9, and total 60.2. This is not a uniform win: the model improves closed and total scores but trails MMQ on open-ended questions.

For difference questions, the proposed model reports BLEU-1 0.628, BLEU-2 0.553, BLEU-3 0.491, BLEU-4 0.434, METEOR 0.339, ROUGE-L 0.577, and CIDEr 1.027. IDCPCL reports 0.614, 0.541, 0.474, 0.414, 0.303, 0.582, and 0.703. The proposed method leads every listed metric except ROUGE-L. MCCFormers is substantially lower on most metrics and has CIDEr 0 in the reported table.

The question-only control reports BLEU-4 0.12, ROUGE-L 0.340, and CIDEr 0, compared with 0.42, 0.645, and 1.893 for images plus questions. This is evidence that image input matters under the test, but it does not rule out report-template, answer-frequency, or region-detector shortcuts.

### Ablation Tension

The paper says the full spatial+semantic+implicit graph achieves the best performance across most metrics. The table is more nuanced. Full is strongest or tied on BLEU-2 (0.541), BLEU-3 (0.477 tie), and BLEU-4 (0.422). Implicit-only is higher on BLEU-1 (0.626 versus 0.624), ROUGE-L (0.649 versus 0.645), and CIDEr (1.911 versus 1.893). Semantic-only is higher on METEOR (0.340 versus 0.337). This does not negate the structured design, but it weakens a simple additive claim for all three graphs and motivates repeated-seed, per-question, and targeted relation ablations.

### Limitations and Error Types

The authors state that the KeyInfo representation handles at most two locations for the same disease and does not cover some combined abnormality terminology. They identify errors involving similar presentations, synonymous abnormality names, and inaccurate Faster R-CNN features. Reviewer-identified limits include rule-generated targets derived from the same reports used as evidence, uncertain patient-level leakage controls, no external-site evaluation, no calibration or abstention, no clinically weighted harm analysis, attention visualizations without causal intervention, and no prospective workflow study.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Medical difference VQA is a distinct task that better represents longitudinal comparison than single-image VQA. | Author conceptual claim | E2, task definition and motivation | The task distinction is clear; clinical fidelity remains a design hypothesis without prospective study. | Medium-high |
| C2 | Medical-Diff-VQA contains 700,703 QA pairs from 164,324 image pairs. | Author/release factual claim | E1-E3 | Paper and current official dataset record agree. | High |
| C3 | The Extract-Check-Fix process yields a low-error QA dataset. | Author empirical claim | E2, 1,700-sample validation | The sampled correctness is high, but the audit design and stratification are incomplete. | Medium-high |
| C4 | Anatomy-aware multi-relation graphs improve difference VQA. | Author mechanism/empirical claim | E2, baseline and ablation tables | Main comparison is favorable, but component ablation does not show the full graph dominating every metric. | Medium |
| C5 | The model uses visual evidence rather than only language priors. | Author empirical claim | E2, question-only control | Removing images degrades metrics strongly; other shortcut pathways remain untested. | Medium-high |
| C6 | Attention regions provide evidence and faithfulness. | Author interpretability claim | E2, visualizations and narrative | Saliency can support inspection, but attention is not a causal explanation or clinical validation. | Low-medium |
| C7 | The official code enables reproduction. | Reviewer assessment | E4, E5 | Code and instructions improve inspectability, but credentialed data, checkpoints, old dependencies, missing license evidence, and unexecuted workflows prevent a reproduction claim. | Medium-low |
| C8 | The paper was eligible for this automation run. | Process claim | E7 | No prior ID/title/slug marker was found; the source gate passed after repair. | High |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E manuscript for one randomly selected, non-duplicate arXiv paper; preserve its mechanism, evidence, limits, and safe implementation implications.
- `Sources inspected`: Verified complete local PDF, full-paper HTML, metadata HTML, and TeX source; arXiv record; KDD DOI metadata; PhysioNet dataset records; official dataset/model GitHub READMEs; live repository authorities; three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs using `rg --files -g "*.pdf"`, grouped parent directories as paper units, extracted canonical arXiv IDs, built a cross-repository used-paper index, made a uniform `Get-Random` draw over eligible units, repaired the selected archive unit, then inspected primary sources and related DEP artifacts.
- `Inclusion criteria`: Sources had to establish paper identity, expose full methods/results/limits, document dataset/code availability and governance, define repository rules, or provide concrete overlap in multimodal grounding, paired-view consistency, or interpretability.
- `Exclusion criteria`: Abstract-only evidence was excluded from synthesis. No source file, private path, unexecuted code result, inferred license, clinical deployment claim, or unrelated keyword hit was treated as evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety-and-ethics, product-research, and replication analysis.
- `Evidence handling`: Author claims and reviewer interpretations are labeled separately; quantitative claims are tied to source tables; current official records cross-check paper-era availability statements.
- `Uncertainty handling`: Non-reproduction, sampled validation limits, shortcut risk, graph-ablation tension, clinical uncertainty, and inaccessible publisher full text are explicit.
- `Extraction process`: Local HTML and TeX source were inspected for section structure, tables, equations, and limitations; PDF and public HTML supplied cross-format checks. No clinical data were downloaded.
- `Version control`: Paper pinned to arXiv:2307.11986v2; dataset record pinned to Medical-Diff-VQA v1.0.1; EKAID main observed at commit `1e5dd0de91554515d2acc83ad402e810ace0a5d7`.
- `Random selection`: 75,777 PDFs collapsed to 75,776 parent-directory units. After used-ID and identifier-completeness filtering, PowerShell `Get-Random` selected zero-based eligible index 32,396 of 75,537.
- `Deduplication`: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data `.lake-data`/`.reports` were scanned for ID, DOI, normalized title, and slug. The scan observed 446 used IDs, excluded 54 units by used ID, withheld 185 missing-ID units, and required zero reselections.
- `24-hour validation`: Public-safe cutoff date 2026-07-15; no same-paper or same-unit marker was found on or after it.
- `Source-integrity gate`: Initial state `partial` because full-paper HTML was missing. The valid PDF was preserved; official HTML, metadata HTML, and source archive were collected with bounded direct-HTTPS attempts. PDF, HTML, structural, and zero-partial checks passed before review.
- `Reviewer stance`: Critical paper review, DEP-ready preservation, safe implementation translation, and explicit clinical/reproducibility boundaries.

## Scope, Constraints, and Assumptions

- `Scope`: Task definition, dataset construction, graph method, reported experiments, limitations, official code/data records, and research-to-product implications.
- `Temporal boundary`: Sources inspected through 2026-07-16; paper version is v2 from 2024; official dataset record is v1.0.1 from 2025.
- `Evidence limits`: No dataset download, code execution, checkpoint inspection, repeated-seed analysis, external-site evaluation, prospective clinical study, or independent statistical review.
- `Assumptions`: The arXiv v2 PDF/HTML/source correspond; the official repositories are author-controlled implementations; current PhysioNet records describe the released derivative dataset accurately.
- `Constraints`: Credentialed clinical data and source documents may not be redistributed. No patient data, local identifiers, or source artifacts are included. Code reuse requires separate license review.
- `Out of scope`: Diagnostic use, treatment recommendation, clinical performance certification, formal privacy audit, dataset re-identification, or reproduction of the paper.
- `Intended use`: Research review, DEP deposition, replication planning, evaluation design, and safe prototype scoping.
- `Audience`: Medical-AI researchers, multimodal engineers, dataset stewards, clinical safety reviewers, and Black Lake reviewers.
- `Depth target`: Full schema-complete manuscript with quantitative preservation and a critical evidence boundary.
- `Reproducibility boundary`: A reviewer can locate source records and code, but cannot reproduce results from this Markdown artifact alone.
- `Operational boundary`: Any prototype must remain retrospective and non-diagnostic until governed clinical validation, privacy, and regulatory review exist.
- `Data sensitivity`: Credentialed, de-identified clinical imaging/report data; residual privacy and governance obligations remain.

## Observations

- `Observed pattern`: Anatomy functions as a correspondence layer between temporally separated images, reducing dependence on raw coordinate alignment.
- `Observed pattern`: Rule-generated QA creates scale and control, but also couples evaluation targets to the linguistic templates used during extraction.
- `Technical implication`: Difference VQA needs two validation axes—whether the answer is correct and whether the claimed change is visually/temporally grounded.
- `Contradiction or tension`: The full three-graph model is not numerically best on every ablation metric despite the broad headline claim.
- `Open question`: How much performance survives patient-level, report-template, institution, device, and projection shift?
- `Reviewer hypothesis`: A clinically useful successor should produce a structured change ledger with evidence regions, uncertainty, and abstention rather than only a generated phrase.
- `Cross-DEP pattern`: VLM Probing supplies tests for modality/relation use, OViP supplies precision-versus-coverage and hallucination controls, and VideoWeave supplies paired-view consistency checks beyond surface quality.

## Considerations

Clinical use magnifies ordinary VQA risks. An answer can be linguistically plausible while missing a newly visible abnormality, confusing synonymous terms, or attributing acquisition variation to disease progression. Closed-question accuracy can look strong while open-ended coverage remains weak. Metrics should therefore include clinically weighted omission and commission errors, calibration, abstention, temporal consistency, localization quality, subgroup performance, and human override behavior.

Data governance is central. MIMIC-CXR and Medical-Diff-VQA are credentialed resources with data-use agreements. Derived QA pairs may be de-identified, but public outputs must not expose underlying images, reports, patient/study identifiers, or reconstructable linkages. Dataset generation and split logic should be audited for patient-level isolation and report-template leakage.

The implementation surface is nontrivial: multiple detector checkpoints, credentialed datasets, feature extraction, legacy Python dependencies, graph training, evaluation files, and optional networked UI. The visible repositories improve transparency but do not establish maintenance, security hardening, licensing, or reproducibility. A networked demo that handles clinical images would require authentication, encryption, logging controls, least-privilege access, and explicit non-diagnostic labeling.

## Strengths

- Defines a clear longitudinal multimodal task grounded in an authentic radiology comparison workflow.
- Provides a large derivative dataset with seven interpretable question categories and an official governed release record.
- Uses anatomy as a stable unit of comparison rather than relying only on pixel- or patch-coordinate alignment.
- Separates spatial, domain-semantic, and implicit relations, making modeling assumptions visible and ablatable.
- Includes a human QA sample check, multiple baseline families, a question-only control, graph ablations, and error discussion.
- Provides official code for dataset generation, feature extraction, training, testing, and an interface.

## Weaknesses

- Dataset targets are generated from reports through rules, so answer quality and evaluation can inherit extraction, negation, synonym, and template biases.
- The 1,700-item validation lacks reported agreement statistics, uncertainty intervals, stratified errors, and independent external review.
- No prospective clinical workflow, external-institution, subgroup, calibration, abstention, or clinically weighted harm evaluation is reported.
- Exact-match and caption metrics can miss clinical equivalence, omission severity, and evidence-grounding failures.
- The full graph does not dominate every ablation metric, and no repeated-seed uncertainty is reported.
- Attention visualization is presented as evidence/faithfulness without causal intervention or clinician validation.
- Reproduction requires credentialed data, checkpoints, old dependencies, and substantial preprocessing; license visibility is incomplete.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Patient-level split and leakage audit | Dataset | Prevent identity/report-template overlap across splits | More credible generalization | May reduce effective sample size | Hash patient/study groups, audit templates, publish split checks |
| Stratified clinician review | Labels | Aggregate correctness hides category/severity errors | Clinically interpretable quality bounds | Requires expert time | Double-review balanced strata; report agreement and confidence intervals |
| Registration and acquisition perturbations | Robustness | Pose/projection variation is central to the task | Measures true change sensitivity | Perturbations may be unrealistic | Controlled alignment, crop, projection, and detector-error sweeps |
| Causal graph-edge tests | Mechanism | Attention and graph structure are not causal proof | Better understanding of relation use | Combinatorial experiments | Edge deletion/corruption, counterfactual relations, mediation tests |
| Clinical semantic evaluation | Metrics | Exact match and caption metrics underweight severity | Safer performance assessment | Requires ontology and experts | Concept matching, contradiction/omission severity, calibration, abstention |
| External-site and subgroup validation | Generalization | Single-source evidence may not transfer | Better deployment boundary | Access and governance burden | Locked protocol across sites/devices/subgroups |
| Reproducible environment and license manifest | Engineering | Current instructions depend on legacy tooling and opaque rights | Lower replication and compliance risk | Maintenance work | Containerized smoke test, dependency lock, artifact checksums, license inventory |

## Potential Implementations

1. **Retrospective change-audit workbench**
   - `User`: Medical-AI validation teams and radiologists reviewing research outputs.
   - `Goal`: Compare a current/reference pair and audit whether a proposed change label is supported.
   - `Core mechanism`: Anatomy-aligned regions, explicit relation graphs, structured change candidates, and a human confirmation queue.
   - `Required inputs`: Credentialed de-identified study pairs, approved question templates, detector outputs, and governance metadata.
   - `Outputs`: Change ledger, evidence regions, confidence, abstention reason, and reviewer decision.
   - `Risk controls`: Local/controlled processing, no autonomous diagnosis, no raw-image export, access logging, patient-level isolation.
   - `Evaluation`: Clinician agreement, omission/commission severity, calibration, subgroup performance, and review time.

2. **Difference-VQA dataset lint service**
   - `User`: Dataset maintainers.
   - `Goal`: Detect contradictory, templated, ungrounded, or leakage-prone QA pairs before training.
   - `Core mechanism`: Rule trace capture, negation/synonym normalization, patient/split checks, answer-frequency analysis, and stratified sampling.
   - `Required inputs`: QA metadata and rule provenance; raw clinical content only inside the governed environment.
   - `Outputs`: Issue ledger, sampled review batches, split warnings, and versioned quality report.
   - `Risk controls`: Minimum necessary data, no re-identification, export only aggregate findings.
   - `Evaluation`: Reviewer precision/recall on issue types and reduction in post-release corrections.

3. **Multimodal grounding probe suite**
   - `User`: Vision-language model researchers.
   - `Goal`: Test whether answers depend on current image, reference image, question, and graph relations.
   - `Core mechanism`: Image/question removal, reference swaps, region masking, edge corruption, and modality/layer probes inspired by VLM Probing.
   - `Required inputs`: Public or governed test pairs, model hooks, and synthetic controls.
   - `Outputs`: Grounding matrix, shortcut indicators, failure clusters, and reproducible test manifest.
   - `Risk controls`: Evaluation-only access, synthetic/public examples where possible, no clinical decisions.
   - `Evaluation`: Sensitivity to correct evidence and invariance to irrelevant perturbations.

4. **Longitudinal evidence card generator**
   - `User`: Model governance and research review teams.
   - `Goal`: Package paired-image model claims with provenance, uncertainty, and evaluation boundaries.
   - `Core mechanism`: Attach source version, pair lineage, relation inventory, metric suite, grounding checks, and review status to each experiment.
   - `Required inputs`: Experiment manifest, aggregate metrics, sample audit results, and source locators.
   - `Outputs`: DEP-ready Markdown evidence card.
   - `Risk controls`: No source image/report embedding, public-safe aggregation, explicit non-diagnostic labeling.
   - `Evaluation`: Completeness, traceability, and independent reviewer agreement.

## Three Ways to Exercise This Research

1. `Synthetic paired-image graph test`: Objective: verify the graph/difference mechanism without clinical data. Inputs: synthetic shapes with known spatial relations and controlled changes. Method: create paired scenes, build spatial/semantic toy graphs, corrupt one relation at a time, and compare answer accuracy. Output: relation-sensitivity report. Success criterion: known changes are detected while irrelevant pose changes are ignored. Stop condition: end if the task leaks answers through filenames or templates. Safety boundary: synthetic data only.
2. `Public artifact reproduction preflight`: Objective: determine whether the released code can support a lawful reproduction before downloading credentialed data. Inputs: public READMEs, dependency files, repository commit, checkpoint manifests, and DUA requirements. Method: inventory dependencies, licenses, expected artifacts, compute, and split logic; run only static and toy smoke checks. Output: reproducibility and rights matrix. Success criterion: every required artifact has an owner, locator, expected format, and permission state. Stop condition: do not fetch clinical data until credentialing and governance approval are complete. Safety boundary: no patient data.
3. `Grounding-and-coverage evaluation design`: Objective: extend caption metrics with evidence and omission checks. Inputs: a small governed or synthetic paired-image set, candidate answers, region annotations, and reviewer rubric. Method: score concept correctness, change direction, evidence region, coverage, contradiction, calibration, and abstention. Output: evaluation card and disagreement ledger. Success criterion: the rubric identifies at least one failure hidden by exact match or BLEU. Stop condition: halt clinical interpretation if reviewer qualifications or data authorization are unclear. Safety boundary: retrospective research only.

## Example MVP Product

- `Product name`: Longitudinal VQA Audit Card.
- `Target user`: Medical-AI evaluation teams and clinical research reviewers.
- `Problem`: Aggregate VQA metrics do not show whether a longitudinal answer is grounded, complete, calibrated, or safe to surface.
- `Core workflow`: Import an approved experiment manifest and aggregate predictions; validate pair/split provenance; run modality, reference-swap, and relation perturbation checks; sample high-risk errors for qualified review; export a public-safe evidence card.
- `Data requirements`: Synthetic/public pairs for development; credentialed de-identified clinical pairs only inside an approved governed environment; no raw source data in exported cards.
- `Architecture`: Local or controlled batch pipeline with manifest validator, perturbation runner, metric engine, reviewer queue, and Markdown exporter. No autonomous clinical action or external model call with clinical data.
- `Success metrics`: Evidence-card completeness, patient-split validation pass rate, reviewer agreement, shortcut detection yield, calibrated abstention, and zero source-data leakage.
- `Risk controls`: Role-based access, encryption, minimum necessary data, immutable audit log, export allowlist, no diagnosis/treatment text, explicit research-only status, and human review.
- `Limitations`: Does not prove clinical utility, cannot eliminate dataset bias, depends on detector/annotation quality, and does not replace prospective validation or regulatory review.
- `MVP boundary`: Aggregate/offline audit only; no bedside integration, report drafting, or real-time diagnosis.
- `Deployment model`: Local-only or approved institutional batch service.
- `Evaluation plan`: Synthetic unit tests, public toy benchmark, privacy review, clinician rubric pilot, and red-team export/leak checks.
- `Failure modes`: Wrong pair linkage, leakage across splits, plausible ungrounded answers, detector drift, overconfident coverage gaps, and accidental sensitive export.
- `Maintenance plan`: Pin source/data/code versions, refresh ontology mappings, rerun perturbation suites after model changes, and review governance quarterly.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Expert Knowledge-Aware Image Difference Graph Representation Learning | Primary paper | Task, dataset, graph method, and reported results reviewed here. | https://arxiv.org/abs/2307.11986 |
| Medical-Diff-VQA v1.0.1 | Official dataset | Current governed release record and category counts. | https://physionet.org/content/medical-diff-vqa/1.0.1/ |
| MIMIC-CXR v2.1.0 | Source dataset | Clinical image/report provenance, de-identification, and DUA boundary. | https://physionet.org/content/mimic-cxr/2.1.0/ |
| VLM Probing - DEP-E | Related DEP | Tests whether multimodal models encode/use visual relations and where probe leakage can mislead. | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` |
| OViP Preference - DEP-E | Related DEP | Frames visual grounding, hallucination, and precision-versus-coverage trade-offs. | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` |
| VideoWeave Geometry - DEP-E | Related DEP | Shows why paired visual outputs need geometric/temporal consistency evidence beyond appearance metrics. | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2307.11986 | Canonical metadata, abstract, version history, DOI, public locators | 2026-07-16 | Primary metadata. |
| R2 | https://arxiv.org/html/2307.11986 | Complete paper body, method, tables, experiments, limitations | 2026-07-16 | Official full-paper HTML; local file withheld. |
| R3 | https://arxiv.org/pdf/2307.11986 | Complete primary paper and figure/table cross-check | 2026-07-16 | Local verified PDF withheld. |
| R4 | https://arxiv.org/e-print/2307.11986 | TeX tables, equations, figures, appendices | 2026-07-16 | Local source package withheld. |
| R5 | https://doi.org/10.1145/3580305.3599819 | Persistent KDD publication identity | 2026-07-16 | Publisher full text not separately fetched. |
| R6 | https://physionet.org/content/medical-diff-vqa/1.0.1/ | Dataset version, counts, method, access, citation | 2026-07-16 | Official credentialed release record. |
| R7 | https://physionet.org/content/mimic-cxr/2.1.0/ | Source-dataset provenance, de-identification, DUA, ethics | 2026-07-16 | Official credentialed database record. |
| R8 | https://github.com/Holipori/MIMIC-Diff-VQA | Dataset-generation workflow | 2026-07-16 | README inspected; code not run. |
| R9 | https://github.com/Holipori/EKAID | Model/feature/training/testing implementation | 2026-07-16 | Main observed at `1e5dd0de91554515d2acc83ad402e810ace0a5d7`; code not run. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository deposition and source-withholding authority | 2026-07-16 | Live README inspected. |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index authority | 2026-07-16 | Live class guidance inspected. |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion-repository DEP context | 2026-07-16 | Live README inspected before dedup use. |
| R13 | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Related multimodal-probing synthesis | 2026-07-16 | Repository-generated artifact; source basis arXiv:2005.07310. |
| R14 | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Related grounding/hallucination synthesis | 2026-07-16 | Repository-generated artifact; source basis arXiv:2505.15963. |
| R15 | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Related paired-visual consistency synthesis | 2026-07-16 | Repository-generated artifact; source basis arXiv:2606.14162. |

## Appendix

### Preserved Quantitative Snapshot

| Evidence | Reported values | Reviewer note |
|---|---|---|
| QA sample validation | 1,657/1,700; table 97.4%; prose 97.33% | Direct division is about 97.47%; audit design details are limited. |
| Non-difference exact match | MMQ 40.5 open / 74.2 closed / 54.7 total; proposed 36.6 / 84.9 / 60.2 | Improvement is closed/total, not open-ended. |
| Difference generation | Proposed BLEU-4 0.434, METEOR 0.339, ROUGE-L 0.577, CIDEr 1.027 | IDCPCL ROUGE-L is slightly higher at 0.582. |
| Question-only control | BLEU-4 0.12, ROUGE-L 0.340, CIDEr 0 | Images+questions: 0.42, 0.645, 1.893. |
| Graph ablation | Full leads/ties BLEU-2/3/4; implicit leads BLEU-1/ROUGE-L/CIDEr; semantic leads METEOR | Full graph is not universally strongest. |

### Replication Checklist

- Pin paper v2, dataset v1.0.1, source-dataset version, repository commits, checkpoints, and dependency hashes.
- Verify credentialing, DUA, patient-level split isolation, and no raw-data export.
- Recreate the KeyInfo and QA generation trace; record randomness and deterministic seeds where possible.
- Validate anatomical/disease detectors separately before graph training.
- Reproduce all tables across repeated seeds with uncertainty intervals.
- Add open/closed/difference stratification, category balance, subgroup metrics, calibration, abstention, and clinically weighted errors.
- Run reference swaps, image removal, region masking, graph-edge corruption, registration perturbation, and report-template leakage tests.
- Require qualified clinical review before any claim beyond retrospective research performance.

Source files were withheld locally. No PDF, HTML, source archive, extracted text, cache, image, report, model, checkpoint, or patient-level record was uploaded with this DEP.
