---
title: "AKB-48 Articulation - DEP-E"
generated_at: 2026-08-18
artifact_type: research_manuscript
primary_subject: "articulated-object knowledge bases and perception-to-manipulation evaluation"
source_status: verified-complete
reviewer: "Codex automated research review"
schema_version: "2026-07-07-expanded"
source_access_date: 2026-08-18
temporal_cutoff: 2026-08-18
primary_url: "https://arxiv.org/abs/2202.08432"
stable_identifier: "arXiv:2202.08432v1"
confidence_summary: "High confidence in the paper's reported design and tabulated results; moderate confidence in external release completeness and benchmark generalization."
safety_scope: "Research synthesis only; no robotic control system was executed or validated."
distribution_notes: "Public-safe derived analysis only. Original PDF, HTML, metadata, TeX/source, caches, and verification files remain withheld locally."
---

# AKB-48 Articulation - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Work | *AKB-48: A Real-World Articulated Object Knowledge Base* |
| arXiv record | `2202.08432v1`, submitted 2022-02-17 |
| arXiv authors | Liu Liu; Wenqiang Xu; Haoyuan Fu; Sucheng Qian; Yang Han; Cewu Lu |
| Published authors | Liu Liu; Wenqiang Xu; Haoyuan Fu; Sucheng Qian; Qiaojun Yu; Yang Han; Cewu Lu |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022 |
| Persistent identifiers | `10.48550/arXiv.2202.08432`; `10.1109/CVPR52688.2022.01439` |
| Primary public record | https://arxiv.org/abs/2202.08432 |
| Complete public text | https://arxiv.org/html/2202.08432 |
| Publisher record | https://openaccess.thecvf.com/content/CVPR2022/html/Liu_AKB-48_A_Real-World_Articulated_Object_Knowledge_Base_CVPR_2022_paper.html |
| Official project | https://liuliu66.github.io/AKB-48/ |
| Review state | Source-first review of a verified complete PDF and full-paper HTML, with metadata and TeX/source cross-checks |

The arXiv v1 record has six authors, while the CVPR record adds Qiaojun Yu. Both bylines are retained. Page ranges are deliberately omitted because currently indexed publisher and proceedings records disagree.

## Evidence Ledger

| ID | Evidence | Source basis | Confidence | Qualification |
|---|---|---|---|---|
| E1 | AKB-48 contains 2,037 articulated-object models spanning 48 categories. | arXiv abstract; full paper, Sections 1 and 3 | High | This is the authors' dataset count; the archived dataset itself was not downloaded or independently recounted. |
| E2 | ArtiKG describes appearance, structure, semantics, and physics. | Full paper, Sections 3.1-3.2 and Figure 2 | High | Some physical properties are measured, while inertia and friction include approximations or reference-table values. |
| E3 | FArM targets roughly five minutes of scanning and 10-15 minutes of annotation per object. | Full paper, Section 3.3 and Table 1 | High | The cost comparison includes assumptions about common inexpensive objects and outsourced CAD estimates. |
| E4 | AKBNet maps one RGB-D observation and an object box through pose, articulation, shape, and manipulation stages. | Full paper, Section 4 and Figure 4 | High | It is a cascaded reference pipeline, not proof that every stage generalizes independently. |
| E5 | Pose and reconstruction training uses 100,000 synthetic images and 10,000 real images split into 5,000 fine-tuning and 5,000 test images. | Full paper, Section 5.1 | High | The text does not clearly establish object-identity independence for the real-image split. |
| E6 | AKBNet reports 9.8-degree rotation error, 0.021 m translation error, 53.6 3D IoU, 8.1-degree joint-axis error, 0.019 m joint-location error, and 94.6% joint-type accuracy. | Full paper, Table 3 | High | These are source-reported benchmark values; no independent reproduction was performed. |
| E7 | Shape Chamfer-L1 is 4.2 with ground-truth joints and 7.5 with predicted joints. | Full paper, Table 4 | High | The gap indicates sensitivity to upstream joint estimation. |
| E8 | TQC+HER reports 72.5% opening and 95.5% pulling success with ground-truth state, dropping to 40.2% and 44.6% with predicted state. | Full paper, Table 5; TeX table cross-check | High | The nearby prose says 98.7% for TQC pulling, but Table 5 assigns 98.7% to SAC+HER; this manuscript preserves the table and flags the conflict. |
| E9 | The project page exposes dataset browsing and a dataset download locator. | Official project page and download page | Medium | Availability was inspected at the page level; the external dataset payload was not downloaded or audited. |
| E10 | A bounded inspection of the official public repository found a project-site tree, but did not establish a maintained AKBNet code/model release. | Official GitHub repository, observed default `gh-pages` tree | Medium | Absence in the observed tree is not proof that no release exists elsewhere or later. |

## Executive Summary

AKB-48 is best understood as a data-modeling proposal with an end-to-end stress test. Its durable contribution is ArtiKG: a representation that treats an articulated object as more than geometry by joining appearance, part hierarchy, joint semantics, and physical attributes. The companion FArM workflow aims to make that representation economical enough to populate a category-scale bank from physical objects.

The paper's AKBNet experiment demonstrates why this representation matters and where a practical system can fail. Perception errors propagate into reconstruction and then into manipulation: Table 5 shows the strongest reported ground-truth-state manipulation scores falling sharply when predicted state is substituted. This makes the paper especially useful as a blueprint for interface contracts and error-budget accounting, even where its benchmark evidence is not yet sufficient for deployment claims.

The central recommendation is to treat AKB-48 as a typed prior and benchmark substrate, not an oracle. A modern implementation should validate provenance, joint constraints, units, uncertainty, identity-disjoint splits, and real-robot transfer before using the knowledge base to drive hardware.

## Detailed Summary

### Problem and representation

The paper argues that articulated-object research is fragmented across CAD geometry, visual perception, and robot manipulation. Synthetic CAD datasets often provide clean mesh and joint annotations but omit mass, material, friction, or physical acquisition provenance. AKB-48 responds with 2,037 models in 48 categories and an Articulation Knowledge Graph (ArtiKG) for each object.

ArtiKG groups object knowledge into four modalities. Appearance covers mesh and texture; structure captures parts, hierarchy, joint types, axes, and limits; semantics assigns category and part meaning; physics records mass, inertia, material, and friction. The paper reports average mesh complexity near 63,000 vertices and 126,000 triangles per object.

### Acquisition and annotation

FArM combines physical scanning, alignment to a canonical coordinate frame, manual part segmentation, kinematic-tree annotation, and physical-property entry. The source reports approximately five minutes for scanning and 10-15 minutes for annotation. Table 1 compares about 20 minutes and roughly USD 3 for the real-world workflow with more than 120 minutes and USD 100 for outsourced CAD modeling. This is an operational estimate, not a randomized or controlled cost evaluation.

The collection is not uniform. For expensive or hard-to-scan categories, the authors describe using existing models and measuring basic information, marking this subset `ArtiKG-sim`. Physics also mixes measurement and estimation: inertia is approximated from primitive shapes, and friction/material values are drawn from a machinery handbook rather than direct per-object friction experiments.

### AKBNet benchmark pipeline

AKBNet receives a single RGB-D image and an object bounding box. A pose stage predicts part segmentation and normalized object coordinate space values, then estimates per-part 6D pose and joint type/properties. A reconstruction stage predicts canonical part shapes and transforms them using estimated pose. A manipulation stage trains reinforcement-learning agents against the resulting state.

For pose and shape experiments, the paper reports 100,000 rendered synthetic RGB-D images plus 10,000 real images, split into 5,000 fine-tuning and 5,000 test images. The described split does not make object-instance independence explicit. The manipulation split is also described ambiguously: 68 and 32 instances are associated with agent training/testing and with opening/pulling in the same sentence, so the allocation cannot be reconstructed confidently from the main text alone.

### Results and error propagation

Table 3 reports 9.8 degrees of rotation error, 0.021 m translation error, 53.6 3D IoU, 8.1 degrees of joint-axis error, 0.019 m joint-location error, and 94.6% joint-type accuracy for AKBNet. Table 4 reports Chamfer-L1 of 4.2 using ground-truth joints and 7.5 using predicted joints, directly exposing upstream sensitivity.

Table 5 makes the same point at the control boundary. SAC+HER reports 57.1% opening and 98.7% pulling with ground-truth state, versus 32.3% and 36.5% with predicted state. TQC+HER reports 72.5% and 95.5% with ground-truth state, versus 40.2% and 44.6% with predicted state. The prose instead pairs TQC+HER with 98.7% pulling; because the table and TeX source agree on 95.5%, this review preserves 95.5% and records the discrepancy.

## Key Claims and Evidence

1. **Claim: a multi-modal object representation is necessary for articulated perception and manipulation.** ArtiKG's four modalities substantiate a useful system schema. This is a design claim supported by coverage, not a proof that all fields are equally accurate.
2. **Claim: AKB-48 materially expands real-world articulated-object coverage.** The paper reports 2,037 models and 48 categories. Independent verification requires the released payload, category manifest, and duplicate audit, none of which were performed here.
3. **Claim: FArM makes acquisition substantially cheaper and faster.** The paper reports 5x time and 33x monetary savings. Those ratios follow its Table 1 assumptions; they should not be generalized to expensive objects, scanner amortization, annotation quality control, or labor markets without a new study.
4. **Claim: one knowledge base can support pose, reconstruction, and manipulation.** AKBNet exercises all three stages. The strongest evidence is architectural integration and tabulated benchmark performance; the largest caveat is error propagation from predicted state.
5. **Claim: the benchmark supports category-level generalization.** Category diversity supports the intent, but the paper's split language is not detailed enough to rule out every form of object-identity or scene leakage.

## Methodology

This deposit used a source-first review process:

1. Enumerate local PDF candidates and treat each parent folder as one archive unit.
2. Build a cross-repository used-paper index from prior logs, reports, DEP manuscripts, relevant context deposits, and automation memory.
3. Uniformly select one eligible unit, then verify canonical identity by arXiv ID, title, and slug.
4. Classify local source integrity before synthesis. Preserve a valid PDF, repair the missing full-paper HTML, and validate both complete-document forms before review.
5. Inspect the arXiv record, full-paper HTML, PDF layout, TeX/source tables, CVPR record, official project site, and bounded public repository tree.
6. Separate paper claims, externally observed release state, and reviewer interpretation in the evidence ledger.
7. Connect exactly three repository deposits using concrete interface overlap rather than title similarity.

Selection used one uniform PowerShell `Get-Random` index over 75,032 eligible units. The chosen zero-based eligible index was 58,660. No duplicate was drawn after prior-use filtering, so the reselection count was zero. Full counts and the 24-hour marker cutoff appear in the Appendix.

## Scope, Constraints, and Assumptions

- The complete local paper corresponds to arXiv v1. The published CVPR record has an expanded byline.
- The dataset payload and external Google Drive folder were not downloaded or independently audited.
- The CVPR supplemental locator was verified, but supplemental experiments were not treated as primary evidence in this review.
- Public repository inspection was bounded to the observed default project-site tree; it does not prove universal absence of code or models.
- No robot, simulator, dataset loader, training job, or benchmark script was run.
- Manipulation results are treated as simulated unless the source explicitly establishes physical-robot execution.
- Local source paths, machine context, timestamps, and original source documents are intentionally withheld.

## Observations

- ArtiKG is more valuable as a contract between perception and control than as a static catalog. It identifies the state fields that downstream consumers need.
- The performance gap between ground-truth and predicted state is a first-class research result. It quantifies how representation quality becomes control risk.
- Mixed measurement methods create field-specific uncertainty. Mass may be directly measured while inertia and friction may be estimated; a single object-level confidence score would hide this distinction.
- The `ArtiKG-sim` subset complicates a blanket “real-world” label, but also offers an opportunity for explicit domain-stratified evaluation.
- The Table 5 prose/table mismatch is small in location but important in meaning, because it changes which algorithm owns the best reported pulling result.

## Considerations

- Add per-field provenance, units, acquisition method, and uncertainty before integrating ArtiKG into a robot stack.
- Enforce kinematic invariants: normalized joint axes, valid limits, connected part trees, nonnegative masses, symmetric positive inertia tensors, and consistent coordinate frames.
- Use identity-disjoint, category-held-out, and acquisition-domain-held-out splits. Publish stable manifests and hashes.
- Report repeated seeds, trial counts, confidence intervals, and failure categories for manipulation.
- Separate perception benchmarking from controller benchmarking with frozen state interfaces and counterfactual perturbation tests.
- Add real-robot calibration and safety interlocks before hardware execution; simulated success is not a deployment certificate.

## Strengths

- A coherent schema spans geometry, kinematics, semantics, and physics.
- The dataset scale and category breadth are substantial for articulated objects.
- FArM makes collection cost and time explicit instead of treating asset creation as invisible labor.
- AKBNet exercises the representation across perception, shape reconstruction, and manipulation.
- Ground-truth versus predicted-state comparisons reveal downstream error amplification.
- The authors expose enough tabular detail to identify an internal narrative/table inconsistency.

## Weaknesses

- Physical fields mix direct measurement, approximation, and handbook lookup without a strong per-field uncertainty model.
- The use of existing models for some costly categories makes the “real-world” characterization heterogeneous.
- Dataset split descriptions do not fully establish object-identity independence.
- Manipulation trial counts, confidence intervals, seed sensitivity, and real-hardware evidence are insufficiently reported in the main paper.
- The Table 5 prose conflicts with its table for TQC+HER pulling.
- The bounded official repository inspection did not establish a maintained end-to-end code/model release.

## Potential Improvements

1. Publish a versioned machine-readable manifest with object hashes, acquisition domain, field-level provenance, units, uncertainty, and licensing.
2. Release identity-disjoint split manifests and leakage tests for synthetic rendering, real-image fine-tuning, and manipulation instances.
3. Add a conformance suite for ArtiKG graphs and explicit migration rules between schema versions.
4. Repeat manipulation evaluation over multiple seeds and report denominators, intervals, failure taxonomy, and both simulated and real-robot outcomes.
5. Calibrate uncertainty across pose, joints, shape, and physical parameters, then propagate it into the control policy.
6. Resolve the Table 5 narrative discrepancy and publish an erratum or machine-readable results file.

## Potential Implementations

1. **ArtiKG validator:** a typed schema and constraint checker that rejects invalid joint trees, units, inertia, and provenance before ingestion.
2. **Perception-to-control error budget:** a replay system that perturbs pose, joint, and shape estimates independently to measure downstream success degradation.
3. **Benchmark manifest service:** a versioned registry for object identities, train/test membership, acquisition domain, and artifact hashes.
4. **Retrieval prior for unseen objects:** a service that retrieves structurally similar ArtiKG objects and returns calibrated priors for joints, geometry, and physics.
5. **Failure-receipt recorder:** a standardized trial artifact containing model version, object identity, state source, seed, calibration, action trace, and outcome.

## Three Ways to Exercise This Research

1. **Schema exercise:** encode five articulated household objects from independent sources, run graph conformance checks, and compare annotation disagreements by field.
2. **Error-propagation exercise:** replay one manipulation policy with ground-truth state and controlled perturbations to pose, joint axis, limits, and shape; plot success degradation against each error source.
3. **Domain exercise:** evaluate identical perception and control components across directly scanned objects, `ArtiKG-sim` objects, and unseen physical objects using identity-disjoint manifests.

## Example MVP Product

**Name:** Articulation Contract Bench

**User:** A robotics or embodied-AI team integrating perception outputs with manipulation policies.

**Problem:** The team cannot tell whether a manipulation failure came from invalid object metadata, perception error, controller behavior, or benchmark leakage.

**Input:** An ArtiKG-like object record, RGB-D observation, predicted articulated state, optional ground-truth state, controller version, and trial outcome.

**Core workflow:** Validate the object record; normalize frames and units; compare predicted and ground-truth state; replay bounded perturbations; generate a signed trial receipt and error-budget report.

**Output:** A conformance report, per-field uncertainty map, state-delta summary, manipulation outcome ledger, and prioritized failure attribution.

**Success criteria:** Every trial is reproducible from frozen identifiers; invalid graphs are rejected before control; benchmark splits are identity-disjoint; and the system quantifies which state errors cause the largest success loss.

**Safety boundary:** The MVP operates offline against recorded data or a sandboxed simulator. Hardware control requires a separate approval layer, collision limits, emergency-stop integration, and site-specific calibration.

**Minimal architecture:** A schema validator, manifest registry, replay/perturbation worker, metrics store, and report UI connected through immutable artifact IDs.

## Related Research and Reading

1. `.lake-data/DEP-A/DEP-A-20260806-MemPose Geometry/2607.04930-whitepaper-review.md` — MemPose addresses category-level 9-DoF pose and size estimation with geometric memory. It is a direct upstream neighbor to AKBNet's state-estimation stage and suggests a retrieval-backed prior that can be evaluated through the same error budget.
2. `.lake-data/DEP-A/DEP-A-20260727-ManipulationNet An Intake/whitepaper-intake-review.md` — ManipulationNet focuses on persistent, standardized real-world robot-skill evaluation. It supplies the physical trial discipline, calibration accounting, and cross-site evidence missing from a simulation-heavy manipulation benchmark.
3. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md` — FAVLA contributes force-aware fast/slow control for contact-rich tasks. It complements AKB-48's articulated state with feedback needed when nominal geometry and physics do not predict contact accurately.

Together these deposits form a useful pipeline: retrieve and estimate articulated state, validate it against a knowledge contract, exercise it in repeatable physical trials, and close the loop with contact-aware control.

## Source References

- Liu, L., Xu, W., Fu, H., Qian, S., Han, Y., and Lu, C. *AKB-48: A Real-World Articulated Object Knowledge Base*. arXiv:2202.08432v1. https://arxiv.org/abs/2202.08432
- Complete arXiv HTML: https://arxiv.org/html/2202.08432
- Public arXiv PDF: https://arxiv.org/pdf/2202.08432
- Public arXiv TeX/source endpoint: https://arxiv.org/e-print/2202.08432
- arXiv DOI: https://doi.org/10.48550/arXiv.2202.08432
- CVPR publisher record: https://openaccess.thecvf.com/content/CVPR2022/html/Liu_AKB-48_A_Real-World_Articulated_Object_Knowledge_Base_CVPR_2022_paper.html
- CVPR paper PDF: https://openaccess.thecvf.com/content/CVPR2022/papers/Liu_AKB-48_A_Real-World_Articulated_Object_Knowledge_Base_CVPR_2022_paper.pdf
- CVPR supplemental locator: https://openaccess.thecvf.com/content/CVPR2022/supplemental/Liu_AKB-48_A_Real-World_CVPR_2022_supplemental.pdf
- CVPR DOI: https://doi.org/10.1109/CVPR52688.2022.01439
- Official project page: https://liuliu66.github.io/AKB-48/
- Official project repository: https://github.com/liuliu66/AKB-48/tree/gh-pages
- Official dataset download page: https://liuliu66.github.io/AKB-48/download.html

## Appendix

### Random selection record

- PDF candidates enumerated: 75,967.
- Unique parent-directory paper units: 75,964.
- Units with an identified canonical paper ID: 75,777.
- Units withheld because no canonical ID could be resolved: 187.
- Units excluded by the prior-use index: 745.
- Eligible units: 75,032.
- Method: one uniform PowerShell `Get-Random` index over the eligible units.
- Selected zero-based eligible index: 58,660.
- Selected canonical ID: `2202.08432`.
- Duplicate rejections after filtering: 0.

### Deduplication and reselection validation

The used-paper index scanned repository logs, reports, DEP manuscripts, staging records, automation memory, and relevant context-repository deposits using arXiv ID, DOI, normalized title, and slug. No prior artifact matched `2202.08432`, its normalized title, or its slug. Same-unit markers were also checked against a 24-hour cutoff of 2026-08-17. Because the draw came from the already filtered population and produced no remaining match, reselection was not required.

### Source-integrity gate

The selected unit initially contained a valid full PDF but lacked full-paper HTML, so it was classified as partial and review stopped. A bounded repair fetched the arXiv full-paper HTML, metadata page, and TeX/source package while preserving the valid PDF. Verification then confirmed a PDF larger than 10 KB with `%PDF-` header and trailing `%%EOF`, and HTML larger than 5 KB with more than 2,000 body characters, document markers, multiple headings, and multiple paper-structure terms. No partial artifact remained. The unit was reclassified as complete before synthesis began.

All original source artifacts, metadata, caches, checksums, and verification records remain local. No PDF, HTML, TeX/source archive, extracted source text, or `.source/` directory is included in this deposit.
