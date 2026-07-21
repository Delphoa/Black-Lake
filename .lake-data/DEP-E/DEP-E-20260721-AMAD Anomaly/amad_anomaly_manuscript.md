---
title: "AMAD Anomaly Detection - DEP-E"
generated_at: "2026-07-21 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of AMAD for multiscale anomaly detection over high-dimensional, time-evolving categorical data."
source_status: "complete private source bundle inspected; public URLs only; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-21"
temporal_cutoff: "arXiv v1, published 2019 paper, and public implementation state inspected through 2026-07-21"
primary_url: "https://arxiv.org/abs/1907.06582"
stable_identifier: "arXiv:1907.06582v1; DOI:10.1145/3326937.3341256"
confidence_summary: "High for source identity and table transcription; medium for mechanism interpretation; low for independent reproducibility or deployment generalization."
safety_scope: "research review, synthetic evaluation, and non-enforcement monitoring prototypes"
distribution_notes: "Public URLs and repository-relative paths only; private source locations and exact execution details withheld; no source files redistributed."
---

# AMAD Anomaly Detection - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | AMAD arXiv record | Primary metadata | HTML | arXiv `1907.06582v1`; arXiv DOI `10.48550/arXiv.1907.06582` | https://arxiv.org/abs/1907.06582 | arXiv metadata; evidence use only | 2026-07-21 | Inspected |
| S2 | AMAD full paper | Primary artifact | PDF, full-paper HTML, TeX/source | v1 | https://arxiv.org/pdf/1907.06582; https://ar5iv.labs.arxiv.org/html/1907.06582; https://arxiv.org/e-print/1907.06582 | Private copies inspected and withheld; ar5iv used as the approved full-paper HTML fallback | 2026-07-21 | Complete and integrity-verified |
| S3 | ACM published record | Publisher identity | DOI | `10.1145/3326937.3341256` | https://doi.org/10.1145/3326937.3341256 | Publisher metadata and DOI exposed by the paper | 2026-07-21 | Identified |
| S4 | DLP-KDD 2019 record | Venue corroboration | Accepted-paper page and workshop PDF | DLP-KDD'19, August 5, 2019 | https://dlp-kdd.github.io/dlp-kdd2019/accept.html; https://dlp-kdd.github.io/dlp-kdd2019/assets/pdf/a7-gao.pdf | Workshop-hosted public records | 2026-07-21 | Inspected |
| S5 | AMAD implementation | Official author-attributed code | Git repository | commit `0391c97dba2823608006180957f9330c5ec06791` | https://github.com/pkumc/AMAD; https://github.com/pkumc/AMAD/commit/0391c97dba2823608006180957f9330c5ec06791 | README states GNU license without a version; no standalone license file was established | 2026-07-21 | README, `model.py`, and `run.sh` inspected; code not run |
| S6 | AMAD anomaly dataset record | Dataset locator | Web record | Tianchi dataset `27665` | https://tianchi.aliyun.com/dataset/27665 | Public record located; contents and license not independently reviewed | 2026-07-21 | Title page inspected; data not collected |
| S7 | CausalTAD Trajectory DEP | Related Black Lake artifact | Markdown | DEP-E-20260711 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md | Contextual synthesis only | 2026-07-21 | Inspected |
| S8 | HSD FTI-FDet DEP | Related Black Lake artifact | Markdown | DEP-E-20260712 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md | Contextual synthesis only | 2026-07-21 | Inspected |
| S9 | Tech Intel 1103 | Related Black-Lake-Data artifact | Markdown | DEP-20260627-Tech Intel 1103, finding 10 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260627-Tech%20Intel%201103/daily_research_findings_2026-06-27_1103.md | Contextual synthesis only | 2026-07-21 | Inspected from fetched default-branch state |
| S10 | Black Lake rules | Repository authority | Markdown | live `main` | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Filing, attribution, source-withholding, and publication-index authority | 2026-07-21 | Fetched and read |
| S11 | Black-Lake-Data rules | Related repository authority | Markdown | live `main` | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Read before relying on the related repository layout | 2026-07-21 | Fetched and read |

Paper/work metadata:

- `Full title`: *AMAD: Adversarial Multiscale Anomaly Detection on High-Dimensional and Time-Evolving Categorical Data*.
- `Authors`: Zheng Gao, Lin Guo, Chi Ma, Xiao Ma, Kai Sun, Hang Xiang, Xiaoqiang Zhu, Hongsong Li, Xiaozhong Liu.
- `Affiliations in the paper`: Indiana University Bloomington and Alibaba Group.
- `Submitted`: 2019-07-12; one arXiv version was exposed in the inspected record.
- `Publication`: *Proceedings of the 1st International Workshop on Deep Learning Practice for High-Dimensional Sparse Data* (DLP-KDD'19), Anchorage, Alaska, August 5, 2019, eight pages.
- `Published DOI`: `10.1145/3326937.3341256`.
- `Subjects`: Machine Learning (`cs.LG`, `stat.ML`).
- `Source files deposited`: none; no `.source/` directory exists.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S3, S4 | Primary metadata and venue records | Title, authors, dates, venue, arXiv ID, DOI, workshop listing. | Bibliographic identity and publication context. | High | Metadata does not establish technical validity. |
| E2 | S2, Sections 1-3 and Figure 2 | Primary full paper and source | Four-level hierarchy; feature/attribute attention; self and relative instance representations; RNN block representation; autoencoder and block generators; discriminators. | Mechanism and architectural claims. | High for source reporting | Equations were inspected but not independently rederived or implemented. |
| E3 | S2, Section 3.4 | Primary full paper and source | Alternating generator/discriminator training; instance and block compound anomaly scores; `beta` and `gamma` weighting. | Training and inference formulation. | High for paper formulation | Adversarial convergence and score calibration were not independently tested. |
| E4 | S2, Tables 1-4 and Appendix | Primary PDF/source tables | Dataset sizes, train/test construction, seven baselines, metrics, ten-run means, instance and block results, `p < 0.01` markers. | Main empirical claims. | High for transcription; low for reproduction | All anomalies are constructed; industrial data were not independently inspected. |
| E5 | S2, Tables 5-6 and Figure 3 | Primary ablations and sensitivity figure | Noise, relative representation, block-loss ablations; block-size behavior; non-sequential Connect-4 behavior. | Component and scale-sensitivity claims. | High for reporting | Ablation uncertainty and full per-run distributions are not exposed. |
| E6 | S5 | Official implementation | TensorFlow 1 APIs, model graph, optimizers, final score expressions, README, hard-coded run paths, and commit history. | Implementation availability and reproducibility audit. | High for inspected code state | Code was not executed; one observed commit may not reproduce the paper. |
| E7 | S6 | Dataset locator | Public title record for AMAD anomaly-detection data. | Evidence that a dataset record exists. | Medium | Contents, version, license, and correspondence to Table 1 were not verified. |
| E8 | S7-S9 | Related DEP artifacts | Online/OOD anomaly scoring, industrial field fault detection, and few-shot nonstationary fault diagnosis. | Cross-DEP synthesis. | Medium | Contextual evidence does not validate AMAD. |
| E9 | Private integrity record, path withheld | Processing evidence | PDF/HTML/source validation, source repair, render review, zero partial files. | Completeness of the reviewed source basis. | High | Private processing evidence is not deposited. |
| E10 | Selection and dedup record | Process evidence | Uniform eligible-unit draw, live repository scans, exact key searches, 24-hour check. | Random selection and non-duplication. | High | Coverage depends on the current archive and fetched repository state. |

## Executive Summary

AMAD addresses a useful anomaly-detection pattern: events arrive over time, each event contains several sets of high-cardinality categorical IDs, labels for true anomalies are scarce, and an operator needs both point-level and collective alerts. The paper builds a hierarchy from feature IDs to attributes, instances, and blocks. Attention summarizes variable-length categorical sets, a second attention path relates each instance to block context, an RNN represents temporal blocks, and adversarial reconstruction losses become anomaly scores at instance and block resolutions.

The paper reports that AMAD outperforms seven baselines on synthetic, Connect-4, and industrial recommendation datasets. Instance AUROC is reported as `0.717`, `0.730`, and `0.691`; block AUROC as `0.745`, `0.746`, and `0.674`. All nine instance metrics and all nine block metrics are marked as significantly above the best baseline with `p < 0.01`. Ablations report that injected autoencoder noise, relative representation, and explicit block loss contribute, with the largest drops appearing for sequential block detection.

These results support AMAD as a plausible multiresolution design, not as a deployment-ready anomaly detector. All evaluation anomalies are constructed; the test sets are balanced 50:50; accuracy and F1 appear to use an optimal threshold selected from the test scores; the industrial baselines receive Doc2Vec inputs while AMAD uses its native categorical hierarchy; and no contaminated-normal training study is reported. The official code improves inspectability but weakens exact reproducibility: it is a single TensorFlow-1-era commit, lacks an environment lock and tests, contains author-local paths, and visibly differs from the paper in optimization, representation combination, example block size, and anomaly-loss construction.

Reviewer confidence is high that the paper, source package, and tables were correctly inspected; medium that the mechanism is promising under its assumptions; and low that the published numbers can be reproduced or transferred to a live, drifting, low-prevalence environment without substantial new work.

## Detailed Summary

### Problem and Context

The paper identifies four challenges: changing event distributions, scarce labeled anomalies, extremely high-dimensional categorical input, and the need to detect irregularity at more than one temporal resolution. A recommendation event illustrates the representation: clicked-item IDs, favorite-brand IDs, and purchase-category IDs form set-valued attributes inside one time-ordered instance. A single corrupted event is an instance anomaly; a locally coherent but collectively irregular run is a block anomaly.

The model assumes training data are normal, or at least mostly normal. It learns the normal data distribution and treats higher reconstruction/discrimination loss as stronger abnormality. This is operationally closer to one-class learning than to fully label-free discovery: deployment still needs a trusted or contamination-tolerant training window.

### Hierarchical Representation

Each categorical ID receives a learned dense embedding. Feature-level attention aggregates the IDs belonging to one attribute. Attribute-level attention then forms a self representation of the whole instance. A second relative representation compares the instance's attributes with a memory vector derived from the preceding block. The paper concatenates the self and relative vectors and applies batch normalization to produce the instance representation.

An RNN processes the ordered instance representations inside a block. Its final hidden state represents the block and also supplies memory to the next block. This creates two coupled views: local structure inside an event and collective structure across a time window. Figure 2 makes this flow visually explicit, although the recurrence and training state-management details remain underspecified for a production stream.

### Adversarial Reconstruction and Scoring

An autoencoder reconstructs each instance representation after Gaussian noise is injected into the encode-decode path. A second RNN transforms reconstructed instances into a reconstructed block representation. Instance- and block-level discriminators distinguish real from reconstructed vectors. Training alternates generator and discriminator optimization because the authors note that adversarial objectives are difficult to converge jointly.

The paper defines the instance score as instance generator loss plus `beta` times instance discriminator loss. The block score adds block generator loss, `beta` times block discriminator loss, and `gamma` times the average instance score within the block. The reported configuration uses `beta = 0.3`, `gamma = 0.05`, RMSProp with learning rate `0.01`, and block size `100`.

### Datasets and Evaluation Design

| Dataset | Distinct categorical dimensions | Attributes | Normal instances | Constructed anomaly instances | Key role |
|---|---:|---:|---:|---:|---|
| Synthetic | 30 | 3 | 10,000 | 1,000 | Controlled sequential pattern |
| Connect-4 public data | 192 | 64 | 44,000 | 4,000 labeled-loss instances used as anomalies | Non-sequential categorical control |
| Industrial recommendation data | 440,512 | 8 | 783,000 | 25,000 injected anomalies | High-cardinality time-evolving case |

The synthetic sequence repeats a noisy categorical zigzag. The first 9,000 normal instances train the model; the remaining 2,000 form a test set in which 1,000 positions are replaced by randomly generated or copied anomalies. For Connect-4, 40,000 `win` instances train the model, while 4,000 other `win` instances and 4,000 `loss` instances form the test set. For the industrial data, the first 758,000 normal events train the model; 50,000 later events form the test window, and 25,000 are replaced by anomalies created by deleting one selected attribute's records or substituting random IDs.

All test sets are therefore balanced between normal and anomaly examples. A block is labeled anomalous when more than half its instances are anomalous. Seven baselines are compared: OCSVM, isolation forest, RDA, OCNN, ALAD, GANomaly, and ALOCC. Because those methods do not natively accept the industrial categorical hierarchy, their inputs are pre-embedded with Doc2Vec. AMAD is run ten times and average metrics are reported. AUROC uses all thresholds; the paper then selects an optimal threshold to compute accuracy and F1.

### Main Results

| Resolution | Dataset | AMAD Accuracy | AMAD F1-macro | AMAD AUROC | Best baseline AUROC |
|---|---|---:|---:|---:|---:|
| Instance | Synthetic | 0.680 | 0.681 | 0.717 | 0.705 |
| Instance | Public | 0.700 | 0.689 | 0.730 | 0.709 |
| Instance | Industrial | 0.644 | 0.643 | 0.691 | 0.661 |
| Block | Synthetic | 0.764 | 0.767 | 0.745 | 0.680 |
| Block | Public | 0.660 | 0.659 | 0.746 | 0.683 |
| Block | Industrial | 0.655 | 0.655 | 0.674 | 0.648 |

The tables mark every AMAD metric as significantly above the best baseline with a one-sample test of run-wise differences and `p < 0.01`. The larger block-level margins fit the method's main hypothesis: direct collective scoring adds information beyond averaging point scores. The result is strongest on the controlled synthetic block task, where AMAD accuracy is `0.764` versus the strongest listed baseline accuracy of `0.672`.

### Ablations and Scale Sensitivity

Removing Gaussian noise lowers all reported metrics. Removing relative representation causes the largest sequential penalties: for synthetic block detection, accuracy and F1 fall by `0.142` and `0.148`, while AUROC falls by `0.026`. Removing explicit block loss lowers synthetic block accuracy/F1/AUROC by `0.100`, `0.111`, and `0.074`, and industrial block accuracy/F1/AUROC by `0.062`, `0.053`, and `0.044`.

On non-sequential Connect-4, relative representation and block loss have much smaller effects, which is consistent with the proposed temporal mechanism. Figure 3 reports that public-data AUROC remains broadly flat over block sizes from 1 to 200, while synthetic and industrial performance falls once test blocks exceed the training size of 100. At block size 1, block scores approach instance-level results.

### Implementation Evidence

The public `pkumc/AMAD` repository contains the AMAD model and seven baseline folders at one observed commit dated 2019-11-19. Its README describes categorical input format and says the code is released under a GNU license, but does not identify the license version. `model.py` uses TensorFlow 1 APIs including `tensorflow.contrib`; `run.sh` embeds author-machine paths. No environment lock, test suite, release, or table-reproduction script was established.

Several code-to-paper differences are visible without executing the repository. The paper reports RMSProp, while `model.py` constructs Adam optimizers. The paper concatenates self and relative instance vectors, while the inspected code adds them. The sample run uses block size 20 instead of 100. The final instance/block score expressions in the inspected code comment out discriminator-loss terms that the paper includes. These may reflect a later or incomplete implementation, but they prevent treating the public repository as a verified reproduction package.

### Conclusion

AMAD is best understood as an early, concrete architecture for multiresolution anomaly scoring over set-valued categorical event streams. Its hierarchy, block context, and explicit point/collective losses remain useful design ideas. Its evidence does not settle the harder deployment questions: contamination, low base rates, adaptive drift, calibration, delayed labels, operational cost, reproducibility, privacy, or adversarial manipulation.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | AMAD unifies hierarchical categorical representation, temporal block modeling, and adversarial anomaly scoring at instance and block levels. | Author method claim | E2, E3 | Directly supported by the paper's equations and architecture figure. | High for formulation |
| C2 | AMAD outperforms seven baselines across all reported instance metrics. | Author empirical claim | E4 | Tables report nine leading values, all marked `p < 0.01`; not reproduced. | High for transcription; low for reproduction |
| C3 | AMAD has larger advantages for block anomaly detection. | Author empirical claim | E4 | Block tables show larger margins in several settings, especially synthetic and public AUROC. | Medium-high |
| C4 | Noise injection, relative representation, and explicit block loss contribute to performance. | Author ablation claim | E5 | Removing each component lowers most or all relevant metrics; sequential tasks show the largest scale-specific losses. | High for reported ablations |
| C5 | The approach handles time-evolving behavior robustly. | Author implication | E4, E5 | Only partly supported; there is no abrupt-drift, contaminated-training, or long-running recalibration experiment. | Low-medium |
| C6 | AMAD is unsupervised. | Author framing | E2-E4 | It does not use anomaly labels for fitting, but it assumes a normal training period and uses anomaly labels for evaluation and threshold choice. | Medium with qualification |
| C7 | The public code is sufficient for exact reproduction. | Reviewer test of reproducibility | E6 | Not supported by the inspected state because of missing environment/data workflow and multiple paper-code differences. | High |
| C8 | The result demonstrates production anomaly detection. | Reviewer boundary claim | E4-E7 | Not supported: anomalies are constructed, prevalence is balanced, and operational thresholding and costs are not evaluated. | High |
| C9 | AMAD's multiresolution pattern connects meaningfully to three existing DEP records. | Reviewer synthesis | E8 | Strong conceptual overlap exists in online/OOD scoring, industrial field monitoring, and nonstationary few-shot diagnosis. | Medium |
| C10 | The paper was randomly selected without a prior or 24-hour duplicate marker. | Process claim | E10 | Exact identifier, title, DOI, and slug scans returned no match; zero reselections. | High |

## Methodology

- `Research objective`: Preserve a source-grounded, schema-complete review of AMAD and translate its multiresolution anomaly-detection mechanism into auditable implementation and replication paths.
- `Sources inspected`: verified private PDF, approved full-paper HTML fallback, metadata HTML, TeX/source package, arXiv record, workshop page and PDF, DOI, official implementation repository, public dataset record, live repository rules, and exactly three related DEP artifacts.
- `Discovery strategy`: enumerate local PDFs using `rg --files -g "*.pdf"`, group by parent directory, derive identifiers from PDF filenames and nearby metadata, exclude used IDs, perform a uniform `Get-Random` draw, then resolve public primary sources and code.
- `Inclusion criteria`: primary or official sources supporting identity, method, experiments, limitations, implementation, dataset availability, or concrete cross-DEP overlap.
- `Exclusion criteria`: duplicate paper units, same-paper markers within 24 hours, abstract-only evidence for technical claims, secondary summaries where primary sources were available, and unrelated DEP entries.
- `Analytical approach`: empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication.
- `Evidence handling`: evidence IDs distinguish source claims, code observations, processing evidence, related-DEP context, and reviewer inference.
- `Uncertainty handling`: all paper metrics remain author-reported; unavailable data checks, code-paper mismatches, possible threshold leakage, and missing deployment evidence remain explicit.
- `Extraction process`: local integrity classification; bounded one-paper source repair; PDF metadata and text extraction; eight-page visual rendering; TeX file and table inspection; targeted repository-file inspection; and live repository-content review.
- `Version control`: paper pinned to arXiv v1; official implementation pinned to commit `0391c97dba2823608006180957f9330c5ec06791`.
- `Cross-checking`: abstract claims were checked against method, result, ablation, figure, and appendix sections; PDF tables were checked against TeX source; paper settings were compared with public code.
- `Reviewer stance`: critical paper report, DEP-ready preservation, product translation, and replication planning.
- `Random selection`: 75,779 PDFs grouped into 75,776 parent units; 1,055 used base IDs observed; 248 units excluded; 185 identifier-incomplete units withheld; uniform zero-based index 34,605 drawn from 75,343 eligible units; zero reselections.
- `Dedup validation`: scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and fetched Black-Lake-Data `.logs`, `.reports`, `.lake-data`, `.staging`; exact ID/title/slug searches found no match and no same-paper marker on or after 2026-07-20.

## Scope, Constraints, and Assumptions

- `Scope`: source identity, AMAD architecture, datasets, result tables, ablations, scale sensitivity, implementation evidence, limitations, exactly three DEP bridges, and bounded implementation ideas.
- `Temporal boundary`: paper v1 and publication from 2019; code and repository state inspected through 2026-07-21.
- `Evidence limits`: experiments were not rerun; dataset contents, per-run values, hyperparameter search space, hardware, and repository executability were not independently verified.
- `Assumptions`: the arXiv source package corresponds to the inspected v1 PDF; table values reflect the authors' stated setup; the code repository is author-controlled because it identifies the paper and contributor Zheng Gao.
- `Constraints`: public-safe output, no private paths or exact execution timestamps, no original-source redistribution, no operational surveillance or enforcement advice, and no production claim from unreplicated results.
- `Out of scope`: legal or privacy approval for recommendation logs, real fraud response, incident adjudication, production threshold policy, dataset redistribution, and safety certification.
- `Intended use`: research review, DEP deposition, replication planning, anomaly-monitoring design, and evaluation backlog creation.
- `Audience`: anomaly-detection researchers, ML engineers, platform reliability teams, data-governance reviewers, and Black Lake maintainers.
- `Reproducibility boundary`: readers can reconstruct the paper's mechanism and evaluation questions, but cannot reproduce the headline metrics from this artifact alone.
- `Operational boundary`: implementation examples are synthetic, local, and decision-support-only; anomaly scores must not trigger punitive or irreversible action without independent evidence and human review.
- `Data sensitivity`: the paper's industrial domain involves behavioral event logs that may contain personal, commercial, or security-sensitive information; real use requires minimization, access control, retention limits, and purpose limitation.

## Observations

1. `Observed pattern`: The largest reported advantage appears at block resolution, which fits the architecture's strongest differentiator rather than suggesting a generic optimizer effect alone.
2. `Technical implication`: Treating instance and block scores as separate evidence channels is preferable to collapsing them into one alert because it exposes whether abnormality is local, collective, or both.
3. `Evaluation tension`: The paper targets rare anomalies but evaluates balanced test sets and optimal thresholds, so accuracy and F1 do not represent live prevalence or alert burden.
4. `Fairness tension`: Industrial baselines receive Doc2Vec vectors while AMAD receives the native categorical hierarchy; this compares end-to-end systems rather than isolating only the detector.
5. `Reproducibility tension`: The paper and public code disagree in several material details, so the repository establishes implementation intent but not exact table provenance.
6. `Open question`: How well does the hierarchy behave when the normal training window is contaminated, schema cardinalities shift, categorical IDs are unseen, or block boundaries are misaligned with incidents?

## Considerations

- **Prevalence and alert load:** calibrate precision, recall, false alerts per million events, time-to-detection, and analyst minutes at realistic base rates.
- **Threshold governance:** choose thresholds on a separate validation period, preserve calibration provenance, and prohibit silent tuning on evaluation labels.
- **Drift:** monitor ID vocabulary growth, attention distributions, reconstruction residuals, prevalence, score quantiles, and delayed-label performance by time and segment.
- **Privacy:** minimize raw behavioral identifiers, hash or tokenize with governed dictionaries, restrict joins, and avoid logging reconstructable user histories.
- **Security:** treat categorical IDs and upstream fields as untrusted; validate schemas, rate-limit score requests, and test poisoning and evasion scenarios.
- **Human impact:** anomaly evidence is probabilistic. Require corroboration, appeal, and reviewer-visible uncertainty before acting on users, employees, customers, or devices.
- **Operations:** separate instance alerts from block incidents; suppress correlated alert floods; define ownership, escalation, rollback, and model-free fallback rules.
- **Maintenance:** pin environments, version feature dictionaries and block definitions, publish evaluation splits, and continuously compare with simple baselines.

## Strengths

- Directly models variable-length sets of high-cardinality categorical IDs.
- Couples local event representation with temporal block context.
- Produces instance- and block-level scores in one architecture.
- Includes seven baseline families rather than only adversarial methods.
- Uses three datasets that probe controlled sequence, non-sequential categorical data, and high-cardinality industrial events.
- Reports ten-run averages and significance markers for the main comparisons.
- Provides ablations for noise, relative representation, and block loss.
- Tests block-size sensitivity and includes a non-sequential control.
- Releases code and a public dataset locator, improving traceability even though reproduction remains incomplete.

## Weaknesses

- All anomalies are synthetic, relabeled, or constructed rather than verified production incidents.
- The 50:50 test prevalence is far from most anomaly-monitoring environments.
- Accuracy and F1 appear to use an optimal threshold derived from the test scores without a separate validation split.
- The normal-only training assumption is not stress-tested under contamination.
- The industrial data and exact splits were not independently inspectable in this review.
- Baselines and AMAD do not share the same representation path on industrial data.
- Hyperparameter search space, per-run distributions, confidence intervals, and multiple-comparison controls are not sufficiently exposed.
- Drift, unseen-ID behavior, latency, throughput, memory, alert costs, privacy, and adversarial robustness are not evaluated.
- The public code lacks a pinned environment, tests, packaged data workflow, and table reproduction command.
- Material paper-code differences prevent treating the repository as a faithful executable specification.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Use chronological train/validation/test windows | Evaluation | Avoid threshold tuning and temporal leakage | More realistic performance estimates | Lower headline metrics | Freeze threshold on validation; report future-window results |
| Evaluate realistic prevalence | Calibration | Balanced tests hide alert burden | Deployment-relevant precision and workload | Requires large negative sets | Report precision-recall curves and alerts per million events |
| Add contamination sweeps | Robustness | Training-normality assumption is fragile | Quantifies tolerance to mislabeled normals | More compute and failure modes | Inject 0.1%-10% diverse anomalies into training |
| Compare shared input encoders | Baseline fairness | Doc2Vec versus native hierarchy confounds method comparison | Clearer attribution of gains | Engineering seven pipelines | Run native, shared-encoder, and end-to-end comparisons |
| Publish exact environment and scripts | Reproducibility | Current code does not match paper settings | Executable table provenance | Maintenance burden | Containerized one-command reproduction with checksums |
| Add adaptive block and multiscale windows | Method | Fixed block 100 degrades when test scale changes | Better incident-duration coverage | Higher compute and alert complexity | Sweep learned and overlapping windows under drift |
| Calibrate uncertainty and explanations | Human review | Scores alone do not show supporting evidence | Better triage and trust calibration | Risk of misleading explanations | Log component scores, attention stability, and counterfactual tests |
| Add privacy and attack evaluation | Governance | Behavioral IDs can be sensitive and manipulable | Safer deployment boundary | Requires threat modeling | Membership, poisoning, evasion, and data-minimization audits |

## Potential Implementations

1. **Event-stream reliability monitor**
   - `User`: platform reliability engineer.
   - `Goal`: detect malformed individual events and correlated upstream pipeline faults.
   - `Core mechanism`: hierarchical set encoder plus separate instance and overlapping-window scores.
   - `Required inputs`: governed categorical telemetry, schema version, block definition, delayed incident labels.
   - `Outputs`: ranked evidence receipts, local/collective score decomposition, alert group.
   - `Risk controls`: synthetic development data, redaction, rate limits, no automated punitive action.
   - `Evaluation`: realistic prevalence, future-window holdout, analyst workload, time-to-detection.

2. **Categorical drift sentinel**
   - `User`: data-quality and ML-platform teams.
   - `Goal`: identify schema/cardinality shifts before downstream models silently degrade.
   - `Core mechanism`: track reconstruction residuals, unseen-ID rates, attention entropy, and block-level change scores.
   - `Required inputs`: versioned dictionaries and privacy-safe aggregates.
   - `Outputs`: drift report, affected attributes, rollback recommendation.
   - `Risk controls`: aggregate-only dashboards, minimum cohort sizes, approval-gated dictionary changes.
   - `Evaluation`: controlled schema migrations, unseen-ID injections, false-positive budget.

3. **Industrial fault triage assistant**
   - `User`: maintenance analyst.
   - `Goal`: combine point anomalies with persistent episode evidence from equipment telemetry.
   - `Core mechanism`: AMAD-style multiresolution scoring fused with a state-estimation or supervised fault channel.
   - `Required inputs`: authorized sensor/event data, maintenance outcomes, operating-state metadata.
   - `Outputs`: non-binding incident queue with uncertainty and corroborating channels.
   - `Risk controls`: human confirmation, fail-safe operating rules outside the model, no score-only shutdown.
   - `Evaluation`: rare-event recall, false alarms per operating hour, lead time, cost-weighted utility.

4. **Anomaly-research comparison bench**
   - `User`: ML researcher.
   - `Goal`: isolate the value of hierarchy, context, adversarial loss, and threshold policy.
   - `Core mechanism`: shared encoder and evaluation harness across AMAD, one-class, VAE, causal, and few-shot baselines.
   - `Required inputs`: public or synthetic datasets with versioned generators.
   - `Outputs`: reproducible tables, calibration plots, contamination curves, resource metrics.
   - `Risk controls`: no restricted data, fixed seeds, immutable splits, transparent negative results.
   - `Evaluation`: exact environment checks and cross-seed confidence intervals.

## Three Ways to Exercise This Research

1. **Recreate the hierarchical representation on synthetic data.** Objective: test whether feature-set attention plus temporal block context separates point and collective corruption. Inputs: generated categorical sequences with known normal rules. Method: implement a non-adversarial encoder first, add point and block scores, and sweep block sizes. Output: AUROC/PR-AUC, calibration, and score decomposition. Success criterion: block context improves collective anomalies without materially harming point detection. Stop condition: terminate if the model only memorizes IDs or results collapse under unseen IDs.
2. **Audit the released implementation against the paper.** Objective: produce an executable discrepancy ledger rather than assume the code reproduces the tables. Inputs: the pinned commit, a containerized legacy TensorFlow environment, and synthetic data only. Method: map equations to code, restore paper settings one change at a time, and run smoke tests. Output: paper-code matrix, passing unit tests, and reproducible toy curves. Success criterion: every material setting and loss term is either matched or explicitly documented. Stop condition: do not use the Tianchi data until license, privacy, schema, and checksum review pass.
3. **Run a realistic-prevalence shadow evaluation.** Objective: measure alert burden under low anomaly rates and chronological shift. Inputs: privacy-approved aggregate or synthetic event streams, frozen validation thresholds, and delayed labels. Method: compare instance-only, averaged-block, explicit-block, and causal/state-estimation variants. Output: precision-recall, alerts per million events, lead time, analyst workload, and subgroup/drift slices. Success criterion: a method improves cost-weighted utility within a fixed alert budget. Stop condition: suppress deployment if calibration, privacy, or reviewer workload gates fail.

## Example MVP Product

### Product name

**ScaleWatch Lab**

### Target user

ML reliability engineers and data-quality analysts evaluating categorical event pipelines in a governed internal environment.

### Problem

Conventional row-level validation catches malformed events but misses collective faults that become visible only across a sequence or operational window. A single anomaly score also makes it difficult to distinguish point corruption, episode-level drift, and upstream schema change.

### Core workflow

1. Ingest synthetic or privacy-approved categorical events through a strict schema and dictionary version.
2. Encode each set-valued attribute and produce an instance representation.
3. Score instance reconstruction and maintain overlapping block summaries.
4. Produce separate point, collective, and drift indicators.
5. Calibrate thresholds on a historical validation window under a fixed alert budget.
6. Group correlated alerts into one incident and display a public-safe evidence receipt.
7. Let analysts confirm, reject, or label incidents; no automated enforcement occurs.

### Data requirements

- Synthetic data by default; governed event aggregates for later shadow tests.
- Versioned categorical dictionaries and schema-change ledger.
- Chronological train, validation, and test windows.
- Delayed incident labels or proxy maintenance/data-quality outcomes.
- Cohort sizes sufficient for privacy-safe monitoring.

### Architecture

- **Schema gate:** validates field types, cardinality ceilings, missingness, and dictionary versions.
- **Set encoder:** embeds categorical IDs and aggregates within attributes.
- **Instance scorer:** produces point anomaly evidence.
- **Window scorer:** evaluates overlapping short and long blocks.
- **Drift monitor:** tracks score distributions, unseen IDs, attention entropy, and calibration.
- **Policy layer:** applies validation-frozen thresholds, alert budgets, and human-review routing.
- **Evidence ledger:** stores model/data versions, component scores, window definitions, and reviewer disposition.

### Success metrics

- PR-AUC and precision at the fixed alert budget.
- False alerts per million events and per analyst hour.
- Median and p95 detection lead time.
- Recall by anomaly duration, affected attribute, and drift regime.
- Calibration error and threshold stability across future windows.
- Reviewer agreement and confirmed-incident yield.
- Runtime, memory, and cost per million events.

### Risk controls

- Synthetic inputs for development and demonstrations.
- Data minimization, tokenization, access control, retention limits, and audit logging.
- Independent validation thresholds; no test-label tuning.
- Alert aggregation, rate limits, and rollback to deterministic schema checks.
- Human review and corroboration before operational action.
- Red-team tests for poisoning, evasion, unseen IDs, and schema abuse.
- Explicit model-card language that scores are evidence signals, not proof of fraud or fault.

### Limitations

The MVP cannot establish causality, guarantee detection of novel incidents, or safely adjudicate users or equipment. Its value depends on representative future-window evaluation, stable feature governance, and meaningful delayed labels. A successful synthetic benchmark does not establish production readiness.

### MVP boundary

No raw personal data, no online learning, no automated enforcement, no source-data export, and no deployment to safety-critical control loops.

### Deployment model

Local batch or shadow-stream evaluation inside an authorized environment.

### Evaluation plan

Run deterministic smoke tests; fixed-seed synthetic benchmarks; contamination, prevalence, drift, and block-boundary sweeps; privacy review; and an analyst shadow study with a predeclared alert budget.

### Failure modes

Unseen IDs may inflate scores; block boundaries may dilute incidents; adversarial optimization may destabilize; balanced development data may overstate precision; and attention weights may be mistaken for explanations.

### Maintenance plan

Version dictionaries, generators, thresholds, dependencies, and model artifacts; refresh calibration on a governed schedule; and require regression approval for every schema or window-policy change.

## Related Research and Reading

### Exactly three related DEP entries

| Entry | Concrete overlap | Source basis |
|---|---|---|
| [CausalTAD Trajectory - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md) | Both score evolving sequences with generative models, confront OOD behavior, and rely on constructed anomalies. CausalTAD adds an explicit bias/confounding perspective that AMAD lacks. | Inspected DEP manuscript grounded in arXiv `2412.18820`. |
| [HSD FTI-FDet - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md) | Both target industrial fault monitoring and must translate benchmark results into constrained field systems. HSD emphasizes resource, lighting, and safety-critical false-negative limits that AMAD does not measure. | Inspected DEP manuscript grounded in arXiv `2307.00701`. |
| [Tech Intel 1103](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260627-Tech%20Intel%201103/daily_research_findings_2026-06-27_1103.md) | Finding 10 covers Kalman prototypical networks for few-shot gas-turbine fault detection, connecting AMAD's scarce-label and nonstationary framing to state estimation and rare infrastructure faults. | Inspected fetched DEP entry; primary source listed as arXiv `2606.26710`. |

These are the only related DEP entries selected for this deposit.

### Primary implementation resources

| Resource | Type | Relevance |
|---|---|---|
| [AMAD official repository](https://github.com/pkumc/AMAD) | Author-attributed code | Establishes implementation intent and exposes the reproducibility gaps that a replication must resolve. |
| [AMAD dataset record](https://tianchi.aliyun.com/dataset/27665) | Dataset locator | Potential path to the industrial data; license, content, and correspondence require review before use. |
| [DLP-KDD accepted-paper record](https://dlp-kdd.github.io/dlp-kdd2019/accept.html) | Venue record | Corroborates the workshop publication and author list. |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1907.06582 | Canonical metadata, authors, date, abstract, version | 2026-07-21 | Primary metadata |
| R2 | https://arxiv.org/pdf/1907.06582 | Full paper, figures, tables, equations, appendix | 2026-07-21 | Private copy inspected; withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/1907.06582 | Verified full-paper HTML fallback | 2026-07-21 | Approved fallback; private copy withheld |
| R4 | https://arxiv.org/e-print/1907.06582 | TeX source and table-level cross-checking | 2026-07-21 | Private source package inspected; withheld |
| R5 | https://doi.org/10.48550/arXiv.1907.06582 | arXiv-issued DOI | 2026-07-21 | Stable identifier |
| R6 | https://doi.org/10.1145/3326937.3341256 | Published ACM identity | 2026-07-21 | Publisher DOI exposed by paper |
| R7 | https://dlp-kdd.github.io/dlp-kdd2019/accept.html | Workshop acceptance and authorship | 2026-07-21 | Official workshop page |
| R8 | https://dlp-kdd.github.io/dlp-kdd2019/assets/pdf/a7-gao.pdf | Public workshop-hosted paper corroboration | 2026-07-21 | Primary paper copy |
| R9 | https://github.com/pkumc/AMAD | README and implementation availability | 2026-07-21 | Inspected; not run |
| R10 | https://github.com/pkumc/AMAD/commit/0391c97dba2823608006180957f9330c5ec06791 | Implementation version pin | 2026-07-21 | Sole observed commit |
| R11 | https://tianchi.aliyun.com/dataset/27665 | Dataset existence locator | 2026-07-21 | Contents/license not reviewed |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md | Related online/OOD anomaly synthesis | 2026-07-21 | Contextual only |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md | Related industrial fault/deployment synthesis | 2026-07-21 | Contextual only |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260627-Tech%20Intel%201103/daily_research_findings_2026-06-27_1103.md | Related few-shot nonstationary fault finding | 2026-07-21 | Contextual only |
| R15 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository submission authority | 2026-07-21 | Process source |
| R16 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP filing and index authority | 2026-07-21 | Process source |
| R17 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout authority | 2026-07-21 | Process source |
| R18 | Private integrity, attribution, summary, and verification records; paths withheld | Source-completeness and repair evidence | 2026-07-21 | No original source file uploaded |

## Appendix

### Integrity receipt

| Artifact | Final verification | Distribution |
|---|---|---|
| PDF | 715,086 bytes; `%PDF-` header; trailing `%%EOF`; eight pages visually inspected | Private archive only |
| Full-paper HTML | 437,327 bytes; 47,873 body characters; document marker; 71 headings; seven structure terms | Private archive only |
| Metadata HTML | 43,293 bytes; retained as metadata only | Private archive only |
| Source package | 305,433 bytes; 14 archive entries | Private archive only |
| Partial files | Zero after bounded repair | None distributed |

### Replication checklist

- Pin the paper/source version and code commit.
- Establish the intended GNU license version and dataset terms.
- Replace author-local paths with configuration.
- Build a container compatible with the TensorFlow 1 APIs or port with equivalence tests.
- Reconcile RMSProp versus Adam, concatenation versus addition, block size 100 versus 20, and discriminator-loss terms.
- Recreate synthetic data from the appendix with fixed seeds and checksums.
- Freeze chronological train/validation/test splits and thresholds.
- Report per-seed results, confidence intervals, prevalence-aware metrics, and resource use.
- Run contamination, unseen-ID, drift, and block-boundary sweeps.
- Keep all original source files and restricted data outside the public repository.

### Decision boundary

This artifact supports continued research and a controlled synthetic MVP. It does not support production fraud adjudication, safety shutdown, employee monitoring, or claims that the published AMAD metrics have been independently reproduced.
