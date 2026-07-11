---
title: "SSP Detection - DEP-E"
generated_at: "2026-07-11 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of semantic-decoupled spatial partitioning for point-supervised oriented object detection."
source_status: "local archive evidence plus public URLs and extraction cache; no source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-11"
temporal_cutoff: "arXiv v2 revised 2026-06-04; official code main pinned on 2026-07-11"
primary_url: "https://arxiv.org/abs/2506.10601"
stable_identifier: "arXiv:2506.10601v2; DOI 10.1016/j.patcog.2026.114079"
confidence_summary: "High for source identity and method description; medium for author-reported results; low for independent reproducibility because experiments were not run."
safety_scope: "public scholarly review and synthetic evaluation planning"
distribution_notes: "Public URLs and repository-relative paths only; local source locations and exact execution details withheld."
---

# SSP Detection - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Semantic-decoupled Spatial Partition Guided Point-supervised Oriented Object Detection | Primary paper metadata | arXiv HTML | arXiv:2506.10601v2 | https://arxiv.org/abs/2506.10601 | Public metadata page; no source file redistributed. | 2026-07-11 | Inspected |
| S2 | Paper HTML and TeX source | Primary full text | HTML and source package | arXiv:2506.10601v2 | https://arxiv.org/html/2506.10601; https://arxiv.org/e-print/2506.10601 | Manuscript footer states CC BY-NC-ND 4.0; text used as evidence only. | 2026-07-11 | Extracted and inspected |
| S3 | Pattern Recognition article page | Venue and DOI record | Publisher page | Volume 180, Part B, Article 114079 (2026) | https://doi.org/10.1016/j.patcog.2026.114079 | Publisher metadata and abstract context; no publisher file collected. | 2026-07-11 | Inspected as metadata |
| S4 | AntXinyuan/SSP | Official implementation | GitHub repository | main commit `1e42389c4770e835a55afb733f6d9079b3f9567a` | https://github.com/AntXinyuan/SSP | Apache-2.0 repository; README, commands, configs, model links, and reported metrics inspected. | 2026-07-11 | Inspected, not executed |
| S5 | Local arXiv archive paper unit | Selection provenance | README and PDF presence | arXiv:2506.10601 | Location withheld | Private archive evidence only; no source file deposited. | 2026-07-11 | Inspected |
| S6 | Extraction cache public summary | Processing evidence | JSON-derived public-safe record | schema 1.0 | Source URLs in S1-S2 | Cache status, extractor status, and output sizes only; private paths withheld. | 2026-07-11 | Inspected |
| S7 | CAR Avatar - DEP-E | Related DEP entry | Markdown | DEP-E-20260709-Clothed Avatar CAR | `.lake-data/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` | Processed Black Lake artifact. | 2026-07-11 | Inspected |
| S8 | VideoWeave - DEP-E | Related DEP entry | Markdown | DEP-E-20260709-VideoWeave Geometry | `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Processed Black Lake artifact. | 2026-07-11 | Inspected |
| S9 | RRT-CBF Motion - DEP-E | Related DEP entry | Markdown | DEP-E-20260711-RRT-CBF Motion | `.lake-data/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` | Processed Black Lake artifact. | 2026-07-11 | Inspected |
| S10 | Black Lake README | Repository authority | Markdown | origin/main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public DEP and artifact rules. | 2026-07-11 | Fetched and read |
| S11 | Black-Lake-Data README | Related repository authority | Markdown | main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public raw-data DEP rules used for cross-repository context. | 2026-07-11 | Fetched and read |

Paper/work metadata:

- `Full title`: Semantic-decoupled Spatial Partition Guided Point-supervised Oriented Object Detection.
- `Authors`: Xinyuan Liu, Hang Xu, Zirui Chen, Yike Ma, Chenggang Yan, Feng Dai.
- `Affiliations`: Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Hangzhou Dianzi University.
- `Publication`: Pattern Recognition, Volume 180, Part B, Article 114079 (2026).
- `Dates`: arXiv v1 submitted 2025-06-12; v2 revised 2026-06-04.
- `Identifiers`: arXiv:2506.10601; arXiv DOI 10.48550/arXiv.2506.10601; publisher DOI 10.1016/j.patcog.2026.114079.
- `Research domain`: point-supervised, weakly supervised, oriented object detection in remote-sensing imagery.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S3 | Primary metadata and publisher record | Title, authors, versions, publication, abstract, identifiers, code link. | Source identity and high-level contribution. | High | Abstract and metadata do not validate detailed results. |
| E2 | S2, method sections | Primary full text | Two-stage label-marker/detector pipeline; PSPSA, SSPBE, class decoupling, region growing, PCA-MinMax. | Mechanism and claimed novelty. | High for source reporting | Equations and implementation were not independently rederived. |
| E3 | S2, experiment tables | Primary full text | DOTA-v1.0/v1.5/v2.0 and RSAR settings, detector results, cost table, ablations, offset sensitivity. | Author-reported empirical results. | High for transcription; low for reproduction | Experiments were not rerun; some prose values conflict with tables. |
| E4 | S2, conclusion and bad-case discussion | Primary full text | Prior assumptions, bridge failures, overlap/background limitations, compatibility-pair dependence, noise and resolution sensitivity. | Boundary conditions and weaknesses. | High | Limited to disclosed and visible cases. |
| E5 | S4 | Official repository | Apache license, release dates, installation, scripts, configs, pseudo labels, checkpoints, and reported metrics. | Implementation availability and reproduction path. | Medium-high | Repository was not cloned or executed; dataset access and hardware compatibility remain unverified. |
| E6 | S5, S6 | Private selection and public-safe cache evidence | Uniform draw identity; initial miss; metadata-only local extraction; HTML/source backfill; PDF extractor failure. | Selection and cache methodology. | High | Private paths intentionally withheld. |
| E7 | S7-S9 | Related DEP artifacts | Sparse-evidence priors, latent geometry consistency, and boundary-constrained spatial search. | Cross-DEP synthesis. | Medium | Related artifacts contextualize rather than validate SSP. |
| E8 | S10, S11 | Repository standards | DEP naming, contents, attribution, stable deposition, and public-safe records. | Artifact compliance. | High | Process evidence only. |

## Executive Summary

SSP addresses point-supervised oriented object detection, where each training object is labeled only by a class and an approximate center point rather than a rotated bounding box. The method keeps the two-stage “simple model” pattern of PointOBB-v2: first generate pseudo rotated boxes with a lightweight label marker, then train a conventional oriented detector on those boxes. Its contribution is to make pseudo-label construction more structured. Pixel Spatial Partition-based Sample Assignment combines point-distance bounds, Voronoi-like spatial partitions, and region growing to produce denser positive and negative samples. Semantic Spatial Partition-based Box Extraction then decouples semantic maps by class, partitions compatible object groups, grows instance masks, and converts them to rotated boxes with a PCA-MinMax rule.

The paper reports that SSP with the FCOSR-style detector reaches 48.41 mAP on DOTA-v1.0 versus 41.68 for PointOBB-v2, a 6.73-point improvement. Stronger ORCNN and ReDet detectors are reported at 50.00 and 50.81 mAP. The training-cost table reports 1.91 hours and 5.34 GB on two RTX 3090 GPUs for the strongest SSP setting, compared with 1.43 hours and 5.99 GB for PointOBB-v2 and substantially larger costs for several teacher-student methods. Component ablations support the value of growing positive regions, partition boundaries, class-decoupled semantic maps, and spatial-partition box extraction.

Confidence is high that the source describes the method and these table values, but only medium that the comparisons generalize. The experiments were not independently reproduced, the design relies on limited intra-class overlap and distinguishable foreground/background appearance, and the paper contains numerical tensions: DOTA-v1.0 prose says 48.51 where the table and repository say 48.41; DOTA-v1.5/v2.0 prose values differ from the comparison table; and an offset paragraph mentions 36.05 while its table reports 38.79 at 30% offset. This artifact therefore privileges table/repository values and treats all results as author-reported.

## Detailed Summary

### Problem and Context

Oriented object detection predicts object class, center, width, height, and rotation. It is useful for aerial scenes where ships, vehicles, sports fields, bridges, and aircraft appear at arbitrary angles. Full rotated-box annotation is costly, especially in large, dense remote-sensing imagery. Point supervision reduces annotation effort but removes object scale, extent, and orientation, making pseudo-label generation the central inference problem.

The paper distinguishes teacher-student methods from simple-model methods. Teacher-student systems jointly optimize multiple detectors and gradually mine geometric consistency, often at higher training and memory cost. Simple-model methods first turn points into pseudo boxes with a small label marker, then train a normal detector. SSP inherits this decoupled pipeline and targets two weaknesses in PointOBB-v2: too many ignored pixels during label-marker training and unstable separation of instances when masks are converted to boxes.

### Stage 1: Pixel Spatial Partition Sample Assignment

The label marker is a ResNet-50/FPN encoder whose highest-resolution feature is projected through four 256-channel convolution layers into a class probability map. Training targets are dense pseudo masks built from point annotations and image content.

Dynamic radius assignment gives each annotated point a small positive disk with default lower threshold 5 pixels. The nearest neighboring point supplies an upper-radius estimate: pixels beyond it can be labeled background, while the uncertain interval remains ignored. This is conservative but wastes pixels.

Spatial partition assignment tightens the bounds anisotropically. A Voronoi-like partition assigns space to the nearest annotation point. Region growing expands positive regions from each point using low-level image information, while partition boundaries stop growth from swallowing adjacent instances. The dynamic-radius and partition-derived bounds are fused: lower bounds use the larger estimate, upper bounds use the smaller estimate, and abnormal grown regions can fall back to the fixed radius. The resulting pseudo masks supervise the label marker with focal loss.

### Stage 2: Semantic Spatial Partition Box Extraction

After the label marker predicts full-image semantic maps, SSP separates maps by class and normalizes them so one class’s confidence is not suppressed by competing classes. For each class, the method partitions its points together with points from explicitly compatible categories. Compatibility exceptions handle nested pairs such as ship/harbor, ground-track-field/soccer-ball-field, plane/airport, and helicopter/helipad. A default semantic threshold of 0.3 filters low-confidence regions before region growing.

Each grown instance mask becomes a rotated box. Instead of OpenCV’s minimum-area rectangle, SSP estimates the principal direction with PCA and takes symmetric min/max extents around the annotated center along the principal and orthogonal axes. The authors argue this aligns man-made objects more closely with their symmetry axes. The resulting boxes and classes supervise a standard oriented detector with classification and box losses.

### Data, Training, and Evaluation

The paper evaluates DOTA-v1.0, DOTA-v1.5, DOTA-v2.0, and RSAR. DOTA-v1.0 contains 2,806 images and 188,282 instances across 15 classes; v1.5 adds very small objects and a container-crane class; v2.0 expands to 11,268 images and 1,793,658 instances across 18 classes. RSAR contains 95,842 cropped SAR images across six classes.

Experiments use PyTorch 1.10.0 and MMRotate 0.3.4 on RTX 3090 GPUs. The detector uses ResNet50-FPN-FCOS with a 12-epoch schedule; the label marker uses a 6-epoch schedule. SGD starts at 0.01 for batch size 16 with 500 warm-up iterations and stepwise decay. Random flipping is the only augmentation, and evaluation avoids multi-scale testing.

### Main Results

On DOTA-v1.0, the main table reports PointOBB-v2 at 41.68 mAP, SSP(FCOSR) at 48.41, SSP(ORCNN) at 50.00, and SSP(ReDet) at 50.81. The 48.41 FCOSR result exceeds the other listed simple-model methods but remains below several fully supervised and stronger teacher-student systems. Class results show strong gains for some regular or densely arranged categories, while bridge AP is 0.0 or 0.3 in the listed SSP variants, exposing a severe failure mode.

The cross-dataset table reports the strongest SSP variant at 50.81 on DOTA-v1.0, 35.93 on DOTA-v1.5, 29.02 on DOTA-v2.0, and 31.16 on RSAR. Because nearby prose states different v1.5/v2.0 values, these numbers are recorded as table values rather than harmonized claims.

The cost table reports SSP at 1.91 hours, 5.34 GB, and 50.81 mAP on two RTX 3090 GPUs. PointOBB-v2 is listed at 1.43 hours, 5.99 GB, and 41.68 mAP. The strongest teacher-student comparators range from about 9 to 24 hours and roughly 9.64 to more than 24 GB in the same table, but exact fairness depends on implementation, detector, schedule, and accounting conventions.

### Ablations and Robustness

The sample-assignment ablation rises from 12.88 detector mAP with only a positive radius to 20.74 after adding negative-radius labels, 43.05 after adding grown positives, and 48.41 after adding partition-boundary negatives. The semantic-partition ablation rises from 37.57 using center positives to 45.43 with negative boundaries and 48.41 with semantic preassignment.

Using decoupled semantic maps produces 48.41 detector mAP, compared with 34.66 for raw-image masks and 30.81 for merged semantic maps. Spatial-partition box extraction reports 48.41 versus 42.80 for oriented search and 37.64 for simple binarization. Annotation offset reduces detector mAP from 48.41 at the nominal setting to 45.79 at 10%, 42.20 at 20%, and 38.79 at 30% according to the table.

### Limitations

The method depends on two priors: same-class instances usually do not overlap heavily, and foreground/background appearance is distinguishable. Dense overlap, bridge-like structures that blend into roads, extreme noise, and ultra-low resolution can violate these priors. Compatibility pairs are dataset-specific domain knowledge rather than learned relations. Point placement also matters; performance declines as points move away from object centers. Finally, pseudo-label quality and detector accuracy are imperfectly correlated, complicating model selection.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | SSP converts sparse point labels into pseudo rotated boxes through partition-guided sample assignment and class-decoupled instance extraction. | Author method claim | E2 | Directly supported by algorithms and method text. | High |
| C2 | SSP(FCOSR) improves DOTA-v1.0 mAP from 41.68 to 48.41 over PointOBB-v2. | Author empirical claim | E3, E5 | Table and official repository agree; not reproduced. | High for reporting; low for independent validity |
| C3 | Stronger SSP detector variants reach 50.00 and 50.81 mAP on DOTA-v1.0. | Author empirical claim | E3, E5 | Table and repository agree; detector-specific comparison limits attribution to SSP alone. | High for reporting |
| C4 | Partition boundaries, grown positives, semantic decoupling, and partition-based box extraction each contribute. | Author ablation claim | E3 | Reported ablations support component value, though interactions and repeated-seed uncertainty are not shown. | Medium-high |
| C5 | SSP keeps training near two hours and below 6 GB while improving accuracy. | Author efficiency claim | E3 | Supported by one cost table under two RTX 3090 GPUs; independent timing is absent. | Medium |
| C6 | SSP generalizes robustly across remote-sensing datasets. | Author claim | E3, E4 | Cross-dataset gains are reported, but conflicting prose/table values and dataset-specific compatibility priors weaken the claim. | Medium-low |
| C7 | Explicit spatial priors are a reusable pattern for learning from sparse evidence. | Reviewer interpretation | E2, E7 | Supported conceptually across SSP and the three related DEP entries, not established as a universal result. | Medium |

## Methodology

- `Research objective`: Randomly select one eligible archived arXiv paper, review it source-first, relate it to exactly three DEP entries, and preserve a public-safe research deposit.
- `Sources inspected`: Local archive README/PDF presence; arXiv metadata, HTML, and TeX source; publisher DOI metadata; official GitHub metadata and README at a pinned commit; repository README files; and three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated each PDF parent as a paper unit, selected a uniform zero-based random index with PowerShell `Get-Random`, derived the arXiv ID from filename and README, and searched identifiers, title phrases, DOI, and slug markers across both repositories and automation memory.
- `Inclusion criteria`: Included sources that identify the paper, expose methods/results/limitations, establish implementation availability, define deposition rules, or provide concrete conceptual overlap.
- `Exclusion criteria`: Excluded recommender pages, unverified secondary summaries, source redistribution, local paths, raw cache manifests, and claims not supported by inspected evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, safety/ethics, and provenance review.
- `Evidence handling`: Major claims map to evidence IDs. Author claims remain labeled; table values are preferred when prose conflicts; reviewer inferences are separated.
- `Uncertainty handling`: Numerical conflicts, failed PDF extraction, unexecuted code, missing repeated-seed statistics, dataset-specific priors, and reproduction gaps remain explicit.
- `Extraction process`: Preflight found no `pdftotext` or supported Python PDF extractor. Missing-only local extraction created metadata only in 0.11 seconds. An approved network fallback backfilled arXiv HTML and TeX-source text in 3.92 seconds. Final cache status was `cached`, with 5,342 bytes of HTML text and 123,813 bytes of source text; PDF text remained unavailable.
- `Version control`: Paper pinned to arXiv v2; code pinned to commit `1e42389c4770e835a55afb733f6d9079b3f9567a`.
- `Cross-checking`: Compared abstract, method algorithms, experiment tables, conclusion, repository README metrics, and paper prose; preserved discrepancies instead of silently reconciling them.
- `Random selection`: 75,438 PDF candidates and 75,438 paper units; zero-based selected index 29,914; one uniform draw; 0 duplicate exclusions and 0 reselections.
- `Deduplication and reselection validation`: Checked the public dedup index, Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data code search for arXiv ID, DOI, normalized title, and slug. No prior or same-paper 24-hour marker was found.
- `Reviewer stance`: Skeptical source review, DEP-ready preservation, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2506.10601v2, its official code repository, and exactly three related Black Lake DEP entries.
- `Temporal boundary`: Public sources inspected through 2026-07-11; code evidence pinned to the commit above.
- `Evidence limits`: Experiments and code were not run; datasets, pretrained checkpoints, and pseudo-label archives were not downloaded; PDF text extraction was unavailable; figures were reviewed through source captions and surrounding text rather than a visual replication pass.
- `Assumptions`: The local README/PDF identify the same arXiv work; extracted source corresponds to v2; repository README results refer to the stated configurations.
- `Constraints`: Public artifacts exclude local absolute paths, home directories, usernames, machine names, local workspace roots, timezone labels, and exact local execution timestamps. No source file is redistributed.
- `Out of scope`: Training SSP, benchmarking GPUs, downloading DOTA/RSAR, validating annotation cost, proving partition algorithms, or assessing production surveillance use.
- `Intended use`: DEP deposition, research review, replication planning, benchmark design, and bounded product ideation.
- `Audience`: Computer-vision researchers, remote-sensing engineers, ML evaluation teams, and Black Lake reviewers.
- `Depth target`: Full manuscript review with implementation and evidence-quality analysis.
- `Reproducibility boundary`: Public code and commands exist, but exact reproduction requires datasets, environment reconstruction, GPU resources, and validation of repository-to-paper configuration mapping.
- `Operational boundary`: Implementations remain offline evaluation and annotation-assistance tools, not autonomous operational surveillance systems.
- `Data sensitivity`: Public scholarly sources; any future imagery pipeline must separately address imagery rights, location sensitivity, and annotation governance.

## Observations

- `Observed pattern`: SSP succeeds by converting a weak label into several explicit constraints—center, nearest-neighbor scale, partition boundary, semantic compatibility, and principal orientation—rather than asking one model to infer every missing quantity implicitly.
- `Technical implication`: Pseudo-label systems should log which constraint contributed to each box so failures can be attributed to points, partitions, semantic confidence, region growth, or box conversion.
- `Evidence tension`: The strongest headline values are stable across tables and the repository, but several prose values conflict with nearby tables. This lowers confidence in unqualified cross-dataset claims.
- `Boundary condition`: Bridge failures are not incidental; they expose the method’s dependence on background contrast and regular extent.
- `Reviewer hypothesis`: Learning compatibility relations and uncertainty over partition boundaries could preserve SSP’s efficiency while reducing brittle dataset-specific rules.
- `Cross-DEP pattern`: CAR Avatar, VideoWeave, RRT-CBF Motion, and SSP all use explicit structural priors to constrain otherwise ambiguous prediction or search.

## Considerations

Reproduction should distinguish label-marker quality from downstream detector quality. The paper itself notes that pseudo-label mIoU/mAP do not perfectly predict detector mAP. A credible benchmark therefore needs both stages, multiple seeds, calibration of point offsets, and category-level failure reporting.

Operational remote-sensing systems can affect people, property, infrastructure, or sensitive locations. SSP’s paper evaluates object detection, not decision policy. Any deployment needs imagery-license review, location and retention controls, dataset shift monitoring, uncertainty display, human review, and prohibitions on unsupported downstream inference.

The official code improves reproducibility but does not eliminate environment risk. The paper names PyTorch 1.10.0/MMRotate 0.3.4, while the repository installation lists PyTorch 1.11.0, MMCV 1.7.0, and MMDetection 2.28.2. A reproduction ledger should pin the actual configuration used for each result and record deviations.

## Strengths

- The method targets a clear bottleneck—pseudo-label quality—without abandoning the efficient simple-model pipeline.
- PSPSA and SSPBE expose interpretable stages and assumptions rather than hiding all supervision recovery inside an opaque teacher-student loop.
- The ablations cover sample assignment, semantic partitioning, mask source, box extraction, and annotation offset.
- Evaluation spans multiple DOTA versions and SAR imagery, giving at least some evidence beyond one benchmark.
- The official repository provides code, scripts, configs, pseudo-label references, checkpoints, and an Apache-2.0 license.
- The paper openly documents important failure conditions and includes bridge bad-case analysis.

## Weaknesses

- Results were not reproduced here and the paper does not report repeated-seed uncertainty for key metrics.
- Several prose values conflict with the paper’s own tables, complicating exact claim extraction.
- Dataset-specific compatibility exceptions inject hand-authored domain knowledge and may limit transfer.
- Same-class overlap, low contrast, noise, low resolution, and point offset directly threaten the core priors.
- Bridge detection remains near zero AP in the listed DOTA-v1.0 SSP variants.
- Stronger-detector gains confound pseudo-label quality with detector architecture.
- Training cost is reported for one hardware setup and does not include all data preparation, pseudo-label storage, or reproducibility overhead.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Learn category compatibility | Generalization | Fixed exception pairs require dataset knowledge. | Better transfer to unseen categories and nested layouts. | Learned relations may overfit. | Hold out category pairs and datasets; compare fixed, learned, and no-compatibility variants. |
| Predict partition uncertainty | Pseudo labels | Hard boundaries hide ambiguity. | Calibrated boxes and safer filtering. | More model complexity. | Measure coverage-error curves and downstream mAP after uncertainty filtering. |
| Add low-contrast boundary cues | Failure cases | Bridges blend with roads. | Better performance on elongated, connected structures. | May increase false positives. | Category-specific bridge/road benchmark with boundary and topology metrics. |
| Reconcile result manifests | Evidence quality | Prose/table inconsistencies hinder auditing. | Exact table-to-config traceability. | Documentation burden. | Machine-readable result JSON checked against manuscript tables and README. |
| Run repeated seeds | Statistical validity | Single values hide variance. | More credible comparisons. | Additional GPU time. | At least three seeds with mean, standard deviation, and paired tests. |
| Jointly score label and detector stages | Model selection | Pseudo-label metrics imperfectly predict detector mAP. | Better checkpoint selection. | Requires end-to-end validation runs. | Fit and validate a stage-aware selection metric across datasets. |

## Potential Implementations

1. `Sparse-Label Geometry Auditor`
   - `User`: Computer-vision evaluation engineer.
   - `Goal`: Diagnose why a point-supervised pseudo box succeeded or failed.
   - `Core mechanism`: Replay partition, radius, region-growing, semantic, and PCA-MinMax stages and preserve intermediate overlays and scores.
   - `Required inputs`: Public or governed images, point labels, class map, model outputs, and configuration.
   - `Outputs`: Per-instance evidence cards, failure categories, and aggregate metric tables.
   - `Risk controls`: Local processing, redacted geospatial metadata, no identity inference, and explicit non-deployment labels.
   - `Evaluation`: Box IoU, orientation error, stage-attribution completeness, and reviewer agreement.
2. `Point-Offset Robustness Bench`
   - `User`: Dataset and annotation lead.
   - `Goal`: Determine acceptable annotation imprecision before commissioning a point-label campaign.
   - `Core mechanism`: Inject controlled point offsets and stratify performance by class, density, contrast, size, and overlap.
   - `Required inputs`: Licensed benchmark images, ground-truth boxes, synthetic offset generator, and model adapter.
   - `Outputs`: Accuracy-cost curves, per-class tolerance thresholds, and annotation guidance.
   - `Risk controls`: Use public/licensed datasets and aggregate location-free outputs.
   - `Evaluation`: mAP, pseudo-box IoU, annotation time, and worst-stratum degradation.
3. `Pseudo-Label Provenance Exporter`
   - `User`: Research lead or DEP reviewer.
   - `Goal`: Make pseudo-label claims traceable from source point to downstream detector result.
   - `Core mechanism`: Emit a versioned manifest linking data split, point source, partition configuration, code commit, checkpoint, pseudo box, and evaluation row.
   - `Required inputs`: Experiment manifests, hashes, configs, metrics, and source URLs.
   - `Outputs`: Markdown/JSON ledger and reproducibility checklist.
   - `Risk controls`: No raw sensitive imagery; schema validation; immutable hashes; access controls for restricted manifests.
   - `Evaluation`: Reproduction success, missing-field rate, and table-to-run consistency.

## Three Ways to Exercise This Research

1. `Toy partition replay`: Objective—verify the mechanism on synthetic rotated rectangles; inputs—generated images and center points; method—compare radius-only, partition, region-growing, and decoupled-map stages; output—overlays and IoU table; success—each added stage improves at least one targeted failure without hiding regressions; stop—halt on nondeterminism or invalid geometry.
2. `Offset and overlap stress test`: Objective—map boundary conditions; inputs—a small licensed benchmark subset; method—sweep point offsets, same-class overlap, noise, blur, and contrast; output—stratified degradation curves; success—identify stable and unstable operating regions; stop—do not generalize beyond the tested strata.
3. `Claim-to-run audit`: Objective—validate publication traceability; inputs—paper tables, official configs, repository logs, and checkpoints where permitted; method—map every reported value to a pinned run artifact; output—evidence ledger and discrepancy list; success—all headline values have a unique configuration and source; stop—mark unresolved rather than substituting inferred values.

## Example MVP Product

- `Product name`: SSP Evidence Lab.
- `Target user`: Point-supervised detection researchers and dataset teams.
- `Problem`: Sparse-label pipelines can improve headline mAP while hiding brittle priors, unclear stage failures, and table-to-code mismatches.
- `Core workflow`: Import a safe dataset manifest; generate or load point labels; run bounded pseudo-label stages; capture intermediate evidence; compute pseudo-box and detector metrics; stress point offsets and contrast; export a DEP-ready report.
- `Data requirements`: Licensed images, center points, optional ground-truth rotated boxes, class definitions, configuration files, code commit, and aggregate metrics.
- `Architecture`: Local CLI/notebook with synthetic fixture generator, stage adapters, geometry validator, metric engine, provenance store, and Markdown/JSON renderer.
- `Success metrics`: Deterministic replay, complete provenance, pseudo-box IoU/orientation coverage, detector mAP, worst-stratum reporting, and zero public path leaks.
- `Risk controls`: Local-only default, no identity or sensitive-location inference, metadata stripping, access-controlled datasets, aggregate exports, and explicit research-only labeling.
- `Limitations`: The MVP cannot establish real-world safety, annotation-cost savings, or broad transfer without external studies.
- `MVP boundary`: Synthetic and licensed benchmark evaluation only; no live sensing or operational alerting.
- `Deployment model`: Local CLI and notebook.
- `Evaluation plan`: Golden synthetic cases, malformed-manifest tests, offset sweeps, stage ablations, and one pinned public benchmark reproduction attempt.
- `Failure modes`: Incorrect coordinate transforms, data leakage, config drift, mismatched metric definitions, silently missing labels, and overclaiming from small strata.
- `Maintenance plan`: Version schemas, code commits, dataset manifests, metric definitions, and public-safe validation rules.

Illustrative bounded mock-up:

```python
def audit_instance(point, partition, semantic_mask, pseudo_box):
    """Return public-safe geometry diagnostics; no image content is logged."""
    return {
        "point_inside_partition": partition.contains(point),
        "point_inside_mask": semantic_mask.contains(point),
        "box_contains_point": pseudo_box.contains(point),
        "partition_area": round(partition.area, 2),
        "mask_area": round(semantic_mask.area, 2),
    }
```

Dependencies are an implementation-specific geometry library plus validated adapters for the chosen dataset format. Production use would require coordinate-system tests, privacy review, error handling, and authenticated access to restricted data.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| PointOBB-v2 | Direct baseline | Supplies the simple-model two-stage pipeline that SSP extends. | https://github.com/VisionXLab/PointOBB-v2 |
| DOTA | Dataset foundation | Main aerial oriented-object benchmark family used by SSP. | Xia et al., CVPR 2018 |
| MMRotate | Official toolkit dependency | Rotation-detection framework used in experiments and repository setup. | https://github.com/open-mmlab/mmrotate |
| CAR Avatar - DEP-E | Related Black Lake DEP | Uses explicit geometry and body priors to constrain an underdetermined single-image reconstruction problem. | `.lake-data/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` |
| VideoWeave - DEP-E | Related Black Lake DEP | Encodes geometry-aware structure to improve consistency without relying only on appearance. | `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |
| RRT-CBF Motion - DEP-E | Related Black Lake DEP | Uses geometric boundaries and constraint layers to control spatial search and prevent invalid expansion. | `.lake-data/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2506.10601 | Metadata, abstract, versions, journal reference, DOI, code link. | 2026-07-11 | Primary metadata. |
| R2 | https://arxiv.org/html/2506.10601 | Full-text method, experiments, tables, limitations. | 2026-07-11 | Primary full text. |
| R3 | https://arxiv.org/e-print/2506.10601 | TeX source used by extraction cache. | 2026-07-11 | Inspected, not redistributed. |
| R4 | https://doi.org/10.1016/j.patcog.2026.114079 | Publisher identity and venue record. | 2026-07-11 | Primary publisher reference. |
| R5 | https://github.com/AntXinyuan/SSP | Official code, scripts, configs, license, model/pseudo-label links, metrics. | 2026-07-11 | Pinned to commit in Source Metadata; not executed. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Black Lake artifact rules. | 2026-07-11 | Repository authority. |
| R7 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository context and dedup scope. | 2026-07-11 | Repository authority. |
| R8 | `.lake-data/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` | Sparse visual evidence and explicit-prior bridge. | 2026-07-11 | Related DEP artifact. |
| R9 | `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Geometry-consistency bridge. | 2026-07-11 | Related DEP artifact. |
| R10 | `.lake-data/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` | Boundary-constrained search bridge. | 2026-07-11 | Related DEP artifact. |

## Appendix

### Numerical Discrepancy Register

| Topic | Table / repository value | Conflicting prose value | Handling |
|---|---:|---:|---|
| DOTA-v1.0 SSP(FCOSR) | 48.41 mAP | 48.51 in one paragraph | Use 48.41; table and official repository agree. |
| DOTA-v1.5 strongest SSP | 35.93 AP50 | 33.52 in paragraph | Preserve 35.93 as table value; flag unresolved. |
| DOTA-v2.0 strongest SSP | 29.02 AP50 | 25.36 in paragraph | Preserve 29.02 as table value; flag unresolved. |
| 30% point offset | 38.79 detector mAP | 36.05 in paragraph | Preserve 38.79 as table value; flag unresolved. |

### Replication Checklist

- Pin paper version and code commit.
- Confirm environment mapping between paper and repository dependency versions.
- Record DOTA/RSAR dataset versions, licenses, splits, and preprocessing.
- Map every result row to config, pseudo-label set, checkpoint, and log.
- Run multiple seeds and report variance.
- Validate point-offset, overlap, contrast, noise, and low-resolution strata.
- Report pseudo-label and downstream detector metrics separately.
- Record bridge and other category failures, not only aggregate mAP.
- Preserve public-safe provenance without redistributing restricted data.

### Attribution Block

- Source URL: https://arxiv.org/abs/2506.10601
  - Applies to: this manuscript.
  - Notes: Primary paper metadata and abstract.
- Source URL: https://arxiv.org/html/2506.10601
  - Applies to: this manuscript.
  - Notes: Primary full-text evidence for method, results, and limitations.
- Source URL: https://github.com/AntXinyuan/SSP
  - Applies to: implementation and reproducibility analysis.
  - Notes: Official Apache-2.0 code repository, inspected but not executed.
- Source URL: https://doi.org/10.1016/j.patcog.2026.114079
  - Applies to: publication metadata.
  - Notes: Pattern Recognition article identifier.
