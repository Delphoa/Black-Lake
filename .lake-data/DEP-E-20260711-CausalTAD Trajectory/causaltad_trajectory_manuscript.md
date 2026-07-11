---
title: "CausalTAD Trajectory - DEP-E"
generated_at: "2026-07-11 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of CausalTAD for debiased online trajectory anomaly detection under unseen source-destination pairs."
source_status: "URLs and local extraction cache used for review; no source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-11"
temporal_cutoff: "arXiv v1 and public repository state inspected on 2026-07-11"
primary_url: "https://arxiv.org/abs/2412.18820"
stable_identifier: "arXiv:2412.18820v1; DOI 10.48550/arXiv.2412.18820"
confidence_summary: "High for source identity, paper formulation, and transcription of reported tables; medium for causal interpretation and low for independent reproducibility."
safety_scope: "research review, synthetic evaluation, and decision-support prototyping only"
distribution_notes: "Public URLs and repository-relative paths only; no local execution context or source files redistributed."
---

# CausalTAD Trajectory - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | CausalTAD arXiv record | Primary metadata | HTML | arXiv:2412.18820v1; DOI 10.48550/arXiv.2412.18820 | https://arxiv.org/abs/2412.18820 | arXiv page links the non-exclusive distribution license | 2026-07-11 | Inspected |
| S2 | CausalTAD full text | Primary artifact | HTML and TeX source | v1 | https://arxiv.org/html/2412.18820 ; https://arxiv.org/e-print/2412.18820 | Reviewed for evidence; not redistributed | 2026-07-11 | Inspected through extraction cache |
| S3 | CausalTAD PDF | Primary artifact | PDF | v1 | https://arxiv.org/pdf/2412.18820 | Canonical reference; local PDF existed but PDF text extraction was unavailable | 2026-07-11 | Identified; not deposited |
| S4 | CausalTAD code repository | Official implementation | Git repository README | public `main` page | https://github.com/LwbXc/CausalTAD | No root license file was visible on the inspected page; reuse requires license review | 2026-07-11 | README inspected; code not executed |
| S5 | Self-Learned IDC DEP | Related Black-Lake artifact | Markdown | DEP-E-20260710 | `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` | Repository context only | 2026-07-11 | Inspected |
| S6 | BA-LoRA Bias DEP | Related Black-Lake artifact | Markdown | DEP-E-20260709 | `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Repository context only | 2026-07-11 | Inspected |
| S7 | Structure-aware split finding | Related Black-Lake-Data artifact | Markdown | DEP-20260707-Tech Intel 1103 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%201103/daily_research_findings_2026-07-07_1103.md | Repository context only | 2026-07-11 | Inspected |

Paper/work metadata:

- `Full title`: CausalTAD: Causal Implicit Generative Model for Debiased Online Trajectory Anomaly Detection.
- `Authors`: Wenbin Li, Di Yao, Chang Gong, Xiaokai Chu, Quanliang Jing, Xiaolei Zhou, Yuxuan Zhang, Yunxia Fan, Jingping Bi.
- `Affiliations`: Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; DiDi Global Inc.
- `Venue`: 40th IEEE International Conference on Data Engineering, ICDE 2024, Utrecht, pages 4477-4490.
- `arXiv history`: submitted 2024-12-25; one version exposed in the inspected metadata.
- `Subject`: Computer Science - Machine Learning.
- `Source files deposited`: none; no `.source/` folder.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, date, v1, DOI, subject, ICDE comment, abstract. | Bibliographic identity and high-level contribution. | High | Abstract alone cannot validate detailed method or results. |
| E2 | S2 | Primary TeX/HTML | Causal graph, road-preference confounder, backdoor adjustment, and `P(T|do(C))` definition. | Problem framing and causal criterion. | High for author formulation; medium for causal validity | The assumed graph and identifiability conditions were not independently established from interventions. |
| E3 | S2 | Primary TeX/HTML | TG-VAE and RP-VAE derivations, road-constrained decoding, segment factorization, anomaly-score equation. | Core mechanism. | High | Mathematical derivations were inspected but not independently rederived. |
| E4 | S2 | Primary TeX/HTML | Xi'an/Chengdu sampling, 100 candidate SD pairs, ID/OOD construction, detour/switch anomaly generation, metrics, baselines, hardware. | Experimental design. | High | Dataset release and exact split construction were not independently verified. |
| E5 | S2 | Primary TeX tables | In-distribution results: full model scores 0.9351-0.9788 and improvements 2.1%-5.7% across reported settings. | Reported ID performance. | High for transcription | Not reproduced; synthetic anomalies. |
| E6 | S2 | Primary TeX tables | OOD results: full model scores 0.7950-0.8844 and improvements 10.6%-32.7% across reported settings. | Reported OOD performance. | High for transcription | Not reproduced; split sensitivity unknown. |
| E7 | S2 | Primary TeX/HTML | Ablations, online observation curves, complexity claims, lambda analysis, static-road-preference limitation. | Component value, online behavior, and boundary conditions. | Medium-high | Figures and runtime were not independently benchmarked. |
| E8 | S4 | Official repository README | Code layout, dataset description, Xi'an command, ICDE citation. | Implementation availability and reproducibility review. | Medium-high | Paper datasets are Xi'an/Chengdu; README describes Xi'an/Porto; no execution or license confirmation. |
| E9 | S5-S7 | Related DEP artifacts | Road-system state/control, inherited bias, and structure-aware spatial split context. | Cross-DEP synthesis. | Medium | Contextual evidence does not validate CausalTAD's claims. |
| E10 | Selection/dedup record | Process evidence | Uniform draw index 68,925 of 75,438 paper units; marker scans across repositories and memory. | Random selection and non-duplication. | High | Search coverage depends on repository indexing plus current local checkout. |

## Executive Summary

CausalTAD reframes online trajectory anomaly detection as a causal-debiasing problem. Standard learning-based systems estimate `P(T|C)`, the likelihood of a trajectory conditioned on a source-destination pair. The authors argue that this score is confounded because road preference influences both which SD pairs occur and which routes are taken. A model trained on popular destinations can therefore label a normal route to an unseen destination as anomalous merely because it uses roads that were uncommon in the observational training data.

The proposed criterion is `P(T|do(C))`, intended to remove the backdoor path from road preference to SD-pair distribution. CausalTAD approximates the resulting anomaly score with two VAEs: TG-VAE estimates joint SD/trajectory likelihood; RP-VAE estimates a road-level scaling factor that compensates for unpopular segments. Factors can be precomputed, supporting constant-time updates per newly observed segment under the paper's assumptions.

The reported experiments on Xi'an and Chengdu taxi trajectories show 2.1%-5.7% improvement over the best baselines for observed SD pairs and 10.6%-32.7% for unseen SD pairs. Confidence is high that these numbers are faithfully transcribed from the paper, but low that they are independently reproduced. The main limits are synthetic anomaly labels, a static confounder assumption, untested causal-graph alternatives, and a public repository whose dataset description does not align exactly with the paper.

## Detailed Summary

### Problem and Context

Online trajectory anomaly detection aims to identify unusual ongoing trips early enough for a platform or safety operator to respond. Metric methods compare an incoming trajectory with historical routes sharing the same SD pair, while learning methods estimate a conditional generative likelihood. Both families struggle when the SD pair is new: metric systems lack references, and generative systems can over-penalize roads associated with less-popular destinations.

The paper represents three variables: `C` for SD-pair distribution, `T` for observed trajectories, and hidden road preference `E` for a mixture of urban layout, road level, speed limit, weather, congestion, buildings, and similar factors. Its causal graph contains `E -> C`, `E -> T`, and `C -> T`. Under that graph, conditioning on `C` retains the backdoor association `C <- E -> T`, while intervening on `C` cuts `E -> C`.

### Method

The authors first rewrite the interventional trajectory probability into a joint-likelihood term and a debiasing scaling factor. Because the hidden road-preference variable and the set of possible routes are intractable, the scaling factor is approximated at road-segment level.

TG-VAE encodes the source and destination into a latent route representation. Two decoders reconstruct the SD pair and generate the trajectory. The trajectory decoder is autoregressive and constrained to predict only road segments adjacent to the current segment, limiting impossible transitions and containing the influence of popular roads to local network neighborhoods.

RP-VAE learns a latent representation for road preference from individual road segments and estimates a per-segment likelihood-derived factor. CausalTAD combines the negative log joint likelihood from TG-VAE with the log scaling factors from RP-VAE, balanced by hyperparameter `lambda`. The paper reports that values near 0.1 work best across its tested settings because the approximation otherwise overestimates the scaling term.

### Data and Evaluation

The paper uses two public DiDi taxi-trajectory datasets, Xi'an and Chengdu. Trajectories are map matched, and sequences shorter than 30 are filtered. For each city, the authors sample 100 SD pairs with more than 100 trajectories, split their trajectories between training and ID testing, and sample OOD trajectories from the wider dataset so that their SD-pair distribution differs from training. The source states that each Xi'an dataset contains about 10,000 trajectories and each Chengdu dataset about 20,000.

With no labeled anomaly dataset, the authors generate two anomaly families. Detours replace a subpath with an alternative road-network path. Switch anomalies splice between low-similarity routes sharing an SD pair. Test sets balance anomalous and normal trajectories. ROC-AUC and PR-AUC are reported against iBOAT, VSAE, SAE, beta-VAE, FactorVAE, GM-VSAE, and DeepTEA. Learning models train for 200 epochs with hidden dimension 128 and initial learning rate 0.01 on one RTX 2080 Ti.

### Results

On ID tests, CausalTAD reports ROC-AUC/PR-AUC values from 0.9351 through 0.9788 and relative improvements from 2.1% through 5.7% over the best listed baseline. On OOD tests, it reports scores from 0.7950 through 0.8844 and improvements from 10.6% through 32.7%. The strongest relative gains occur on Chengdu OOD detour cases, where the table reports 32.7% ROC-AUC and 32.4% PR-AUC improvement.

The ablation table shows the full model outperforming TG-VAE alone and RP-VAE alone across all eight city/distribution/anomaly combinations. Online curves indicate performance improves as more of a trajectory is observed; at a 0.6 observation ratio the paper reports PR-AUC 0.9123 for an Xi'an ID switch setting and ROC-AUC 0.8030 for a Chengdu OOD switch setting. The authors also report linear training scaling and efficient inference, but exact figure values beyond the cited examples were not reproduced here.

### Limitations and Conclusion

The paper explicitly treats road preference as static, although congestion and related conditions change by hour and weekday. It proposes time-segment factorization as future work. Reviewer-identified limits include synthetic anomalies, lack of real incident labels, possible spatial leakage or route overlap, sensitivity to the assumed causal graph, and incomplete alignment between the paper and public code repository. The work is promising as a causal-regularization design, but deployment readiness is not established.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Road preference creates confounding bias between SD-pair distribution and observed trajectories. | Author causal claim | E2 | Coherent under the proposed graph, but the graph and hidden-variable interpretation need intervention or sensitivity evidence. | Medium |
| C2 | `P(T|do(C))` is a more appropriate anomaly criterion than `P(T|C)` under the proposed causal model. | Author theoretical claim | E2, E3 | Supported by the stated backdoor adjustment under the paper's assumptions. | Medium-high for formulation |
| C3 | TG-VAE plus RP-VAE yields a road-constrained likelihood and debiasing factor suitable for online updates. | Author method claim | E3, E7 | Directly supported by the architecture and complexity discussion. | High for design; medium for runtime generality |
| C4 | CausalTAD improves the best baseline by 2.1%-5.7% on ID tests. | Author empirical claim | E4, E5 | Faithfully reported from Table I; not reproduced. | High for reporting; low for reproduction |
| C5 | CausalTAD improves the best baseline by 10.6%-32.7% on OOD tests. | Author empirical claim | E4, E6 | Faithfully reported from Table II; split and label sensitivity remain open. | High for reporting; low for reproduction |
| C6 | Both TG-VAE and RP-VAE contribute to performance. | Author ablation claim | E7 | Full-model table values exceed either component alone across all reported settings. | High for reporting |
| C7 | Static road preference is a material limitation. | Author limitation and reviewer assessment | E7 | Directly disclosed and operationally important. | High |
| C8 | The public repository is not yet sufficient evidence for exact reproduction. | Reviewer implementation observation | E8 | Dataset descriptions differ and no run was attempted. | High |
| C9 | The selected paper was not already deposited as an Arxiv DEP. | Process claim | E10 | ID/title/slug checks found no duplicate or same-paper 24-hour marker. | High |

## Methodology

- `Research objective`: Preserve a source-grounded, schema-complete review of CausalTAD and translate its causal/OOD contribution into auditable implementation and replication paths.
- `Sources inspected`: arXiv metadata, public HTML, fetched TeX source including tables and limitations, public code repository README, live Black-Lake and Black-Lake-Data READMEs, automation memory, and exactly three related DEP artifacts.
- `Discovery strategy`: enumerate local PDFs with `rg --files -g "*.pdf"`, group by parent directory, draw a uniform random index with `Get-Random`, inspect nearby metadata, then backfill public arXiv HTML/source when local PDF extraction was unavailable.
- `Inclusion criteria`: primary or official sources supporting identity, method, results, limitations, implementation, or concrete related-DEP overlap.
- `Exclusion criteria`: duplicate papers, same-paper markers within 24 hours, secondary summaries where primary text was available, and unrelated DEP entries.
- `Analytical approach`: empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication.
- `Evidence handling`: evidence IDs distinguish primary paper claims, official repository observations, contextual DEP material, and process evidence.
- `Uncertainty handling`: unreproduced metrics remain author-reported; causal claims are conditional on the assumed graph; missing license and dataset alignment are explicit.
- `Extraction process`: document-source-processing preflight, public arXiv metadata/source fetch, HTML regex extraction, TeX archive extraction, targeted section/table inspection, and public-safe summary review.
- `Version control`: paper pinned to arXiv v1; repository inspected at its public main page without a commit-level execution pin.
- `Cross-checking`: abstract claims were checked against TeX tables; venue metadata was checked against the official repository citation block; dataset descriptions were compared between paper and repository README.
- `Reviewer stance`: critical paper report, DEP-ready preservation, product translation, and replication planning.
- `Random selection`: uniform zero-based index 68,925 from 75,438 unique PDF parent directories; zero reselections.
- `Dedup validation`: searched Black-Lake logs/reports/lake-data, automation memory, and connected Black-Lake-Data for arXiv ID, DOI, title, and slug; zero acceptance exclusions.

## Scope, Constraints, and Assumptions

- `Scope`: paper identity, causal formulation, model mechanism, experimental evidence, limitations, official repository context, and three related DEP bridges.
- `Temporal boundary`: sources inspected through 2026-07-11; paper analysis pinned to arXiv v1.
- `Evidence limits`: PDF text extraction unavailable; no model execution, dataset unpacking, checkpoint inspection, figure measurement, or result reproduction.
- `Assumptions`: fetched TeX source corresponds to arXiv v1 and reported table values accurately represent the conference work.
- `Constraints`: public-safe repository artifacts; no local paths or exact execution timestamps; no redistribution without clear permission; no real-trip deployment advice.
- `Out of scope`: validating passenger-safety operations, production thresholds, surveillance policy, causal identification from interventions, or legal/privacy compliance for ride-hailing telemetry.
- `Intended use`: DEP deposition, research triage, replication planning, evaluation design, and safe prototype ideation.
- `Audience`: ML researchers, spatial-AI engineers, anomaly-detection practitioners, safety reviewers, and Black-Lake maintainers.
- `Reproducibility boundary`: readers can inspect sources and reconstruct the review, but cannot reproduce metrics from this artifact alone.
- `Operational boundary`: code concepts use synthetic summaries only and must not control enforcement or passenger interventions.
- `Data sensitivity`: public paper metadata and repository context; real mobility traces would be sensitive and require governance.

## Observations

- `Observed pattern`: CausalTAD's largest reported gains occur under unseen SD pairs, matching its stated target rather than only improving the familiar ID benchmark.
- `Technical implication`: Separate likelihood and road-preference factors make anomaly evidence more inspectable than a single opaque score, provided both components are logged and calibrated.
- `Contradiction or tension`: The paper presents road preference as a causal confounder but approximates it with a learned latent factor from the same observational data; causal validity therefore relies heavily on structural assumptions.
- `Evidence-quality implication`: Generated detour and switch labels provide controlled evaluation but may not represent fraud, safety incidents, navigation errors, or benign unusual trips.
- `Reproducibility implication`: The Xi'an/Chengdu versus Xi'an/Porto description mismatch should be resolved before treating the public repository as a faithful table reproduction package.
- `Open question`: Do the gains persist with time-aware, geographically disjoint, or route-graph-disjoint splits and real incident review?

## Considerations

Mobility traces can expose sensitive location patterns. A practical implementation should minimize raw trajectory retention, separate research identifiers from user accounts, enforce access controls, aggregate segment statistics, and document retention/deletion rules. The paper does not establish a privacy or governance protocol.

An anomaly score is not a safety verdict. Unseen but legitimate destinations, road closures, emergencies, accessibility needs, and driver discretion can all produce unusual routes. Production systems need calibrated uncertainty, explanation, human review, contestability, and clear non-punitive defaults.

The road-preference factor must be versioned with the road graph and time window. Map changes, congestion regimes, seasonal travel, events, and policy changes can otherwise invalidate cached factors. Monitoring should track both performance and the distribution of false positives across geography and user groups.

## Strengths

- The paper identifies a concrete OOD failure mode tied to how SD-pair frequency and route popularity interact.
- The causal graph provides an explicit hypothesis that reviewers can test, dispute, or extend.
- TG-VAE and RP-VAE form a mechanism-aligned decomposition rather than an unexplained regularizer.
- Evaluation includes ID, OOD, online observation ratios, ablations, efficiency, stability, and hyperparameter analysis.
- Tables report multiple baselines and both ROC-AUC and PR-AUC across two cities and two anomaly generators.
- The paper discloses the static-road-preference limitation and proposes a clear temporal extension.
- Public code and datasets are at least partially exposed for follow-up inspection.

## Weaknesses

- The causal graph and hidden confounder are assumed rather than established through interventions or sensitivity analysis.
- Synthetic detour and switch anomalies may not match real safety or fraud incidents.
- Random or partially overlapping spatial sampling may overstate generalization if road segments or structural patterns leak across splits.
- The static preference variable omits time, weather, congestion, events, and road closures.
- Results were not independently reproduced, and the code README's dataset names do not align with the paper.
- The inspected repository page did not expose a root license file, limiting reuse confidence.
- The paper's relative improvement percentages can appear large when baselines are weak; absolute performance and calibration remain essential.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add time-indexed road preference | Causal model | Preference changes by hour, weekday, weather, congestion, and events. | Better temporal generalization and fewer stale factors. | More sparse strata and drift management. | Hold out time periods and measure calibration plus false-positive drift. |
| Use structure-aware geographic splits | Evaluation | Random sampling can leak road or neighborhood structure. | More credible OOD evidence. | Lower sample efficiency and harder comparisons. | Compare random, SD-disjoint, segment-disjoint, region-disjoint, and time-disjoint results. |
| Add real incident adjudication | Label validity | Synthetic anomalies may not capture operational cases. | Stronger external validity. | Privacy, consent, annotation, and class imbalance. | Blinded expert review with inter-rater agreement and privacy controls. |
| Release a reproduction manifest | Reproducibility | Paper and repository dataset descriptions differ. | Clear table-to-code traceability. | Documentation and storage burden. | Fresh-environment reproduction at a pinned commit. |
| Calibrate anomaly probabilities | Decision safety | AUC does not define usable thresholds. | Better human review and escalation. | Requires representative validation data. | Reliability diagrams, expected calibration error, and cost-sensitive threshold analysis. |
| Test causal-graph sensitivity | Causal validity | Alternative dependencies may fit the same observations. | More honest robustness bounds. | Additional models and assumptions. | Compare graphs, negative controls, and simulated interventions. |
| Report subgroup false positives | Fairness and geography | Rare regions or users may absorb errors. | Detects localized harm. | Requires governance-safe strata. | Region/time/road-class error tables with minimum sample thresholds. |

## Potential Implementations

1. `Trajectory Distribution-Shift Auditor`
   - `User`: ML evaluation engineer.
   - `Goal`: Determine whether an anomaly model generalizes beyond seen routes without spatial leakage.
   - `Core mechanism`: Build SD-, segment-, region-, and time-disjoint split manifests and compare metrics/calibration.
   - `Required inputs`: De-identified map-matched trajectories, road-graph version, labels or synthetic generator, model scores.
   - `Outputs`: Split manifest, metric table, leakage warnings, and failure strata.
   - `Risk controls`: Aggregate statistics, access control, retention limits, and no raw user identifiers.
   - `Evaluation`: Reproducible splits, zero overlap violations, and stable results across seeds.

2. `Temporal Road-Preference Monitor`
   - `User`: Mobility ML operations team.
   - `Goal`: Detect when cached debiasing factors are stale.
   - `Core mechanism`: Compare segment-frequency and factor distributions across rolling public-safe time buckets.
   - `Required inputs`: Aggregated segment counts, factor versions, map version, maintenance/event metadata.
   - `Outputs`: Drift score, affected regions, refresh recommendation, and evidence log.
   - `Risk controls`: Minimum aggregation thresholds, no individual trajectories, manual review before refresh.
   - `Evaluation`: Detect simulated regime changes without excessive false alarms.

3. `Anomaly Decision Evidence Card`
   - `User`: Safety, privacy, or model-risk reviewer.
   - `Goal`: Make each model release reviewable before operational use.
   - `Core mechanism`: Record causal assumptions, data provenance, split design, label source, calibration, subgroup errors, and escalation policy.
   - `Required inputs`: Model card, experiment outputs, data governance notes, source URLs, and limitations.
   - `Outputs`: Markdown/JSON card and approval checklist.
   - `Risk controls`: Public-safe metadata, no sensitive examples, explicit research/deployment status.
   - `Evaluation`: Schema completeness and reviewer ability to identify unsupported claims.

## Three Ways to Exercise This Research

1. `Synthetic SD split test`: Objective: verify ID/OOD bookkeeping. Inputs: toy trajectories with source, destination, and segment sequences. Method: hold out SD pairs, assert no overlap, score a simple frequency baseline. Output: split and metric report. Success criterion: deterministic split with zero SD leakage. Stop condition: any identifier or real mobility record enters the toy dataset.
2. `Road-frequency drift simulation`: Objective: explore the paper's scaling-factor intuition. Inputs: synthetic road counts for two time windows. Method: inject closures or popularity shifts and measure segment-distribution divergence. Output: ranked drift list. Success criterion: injected changes are detected without flagging unchanged segments. Stop condition: results are interpreted as a production causal estimate.
3. `Reproduction manifest audit`: Objective: assess whether public artifacts can reproduce one table. Inputs: paper, repository README, file inventory, and configs. Method: map every table field to dataset, script, seed, dependency, and checkpoint; mark gaps. Output: evidence matrix. Success criterion: all missing prerequisites are explicit. Stop condition: unlicensed or sensitive data would need redistribution.

## Example MVP Product

- `Product name`: RouteShift Evidence Lab.
- `Target user`: Spatial-ML researchers and safety reviewers evaluating trajectory anomaly models.
- `Problem`: Aggregate AUC on randomly sampled routes can hide spatial leakage, stale road preferences, and false positives on legitimate unseen destinations.
- `Core workflow`: import a public-safe experiment manifest; validate SD/segment/region/time split isolation; ingest model scores; compute ROC-AUC, PR-AUC, calibration, and subgroup errors; emit an evidence card with causal assumptions and gaps.
- `Data requirements`: synthetic or governed de-identified trajectory IDs, road-segment sequences, split labels, anomaly labels or generator metadata, and model scores.
- `Architecture`: local CLI/notebook with split validators, metric/calibration module, drift module, Markdown/JSON renderer, and immutable provenance ledger.
- `Success metrics`: zero split-overlap violations, deterministic reruns, calibrated metric coverage, subgroup reporting completeness, and reviewer time to locate unsupported claims.
- `Risk controls`: synthetic mode by default, no raw coordinates or user IDs, configurable aggregation thresholds, local-only execution, explicit research-only status, and human review.
- `Limitations`: The MVP would audit evaluation evidence; it would not reproduce CausalTAD training, infer causal effects, or make operational safety decisions.
- `MVP boundary`: No live ride-hailing integration, passenger surveillance, automated intervention, or punitive action.
- `Deployment model`: local CLI and notebook for research teams.
- `Evaluation plan`: unit tests for split overlap, synthetic drift fixtures, metric golden files, malformed-manifest tests, and privacy review.
- `Failure modes`: mislabeled splits, map-version mismatch, too-small subgroups, misleading synthetic anomalies, and causal claims inferred from correlational audits.
- `Maintenance plan`: version schemas, metric definitions, road-graph IDs, and synthetic fixtures; review dependencies quarterly.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Self-Learned IDC - DEP-E | Related Black-Lake DEP | Road-network online decision system, physical safety metrics, simulation limits, and state representation. | `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` |
| BA-LoRA Bias - DEP-E | Related Black-Lake DEP | Debiasing under inherited observational imbalance and caution about causal interpretation. | `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` |
| Structure-aware spatial split finding | Related Black-Lake-Data DEP | Spatial leakage, hidden stratification, and distributionally robust evaluation. | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%201103/daily_research_findings_2026-07-07_1103.md |
| CausalTAD code repository | Official implementation | Code/dataset/usage context and ICDE citation; requires dataset-alignment and license review. | https://github.com/LwbXc/CausalTAD |
| Causality | Foundational book cited by paper | Structural causal models, interventions, and backdoor adjustment. | Judea Pearl, Cambridge University Press, 2009 |
| DeepTEA | Direct baseline | Learning-based online trajectory anomaly detector included in comparisons. | Han et al., cited in the CausalTAD paper |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| S1 | https://arxiv.org/abs/2412.18820 | Metadata, abstract, DOI, version, subject, ICDE comment. | 2026-07-11 | Primary source. |
| S2 | https://arxiv.org/html/2412.18820 | Full-text method, experiments, discussion, limitations. | 2026-07-11 | Primary source; HTML rendering. |
| S3 | https://arxiv.org/e-print/2412.18820 | TeX sections, equations, tables, references. | 2026-07-11 | Primary source package; inspected through extraction cache, not redistributed. |
| S4 | https://arxiv.org/pdf/2412.18820 | Canonical paper reference. | 2026-07-11 | PDF text extraction unavailable; no file deposited. |
| S5 | https://doi.org/10.48550/arXiv.2412.18820 | Persistent identifier. | 2026-07-11 | arXiv-issued DOI. |
| S6 | https://github.com/LwbXc/CausalTAD | Official code, dataset, usage, and citation context. | 2026-07-11 | README inspected; no execution or redistribution. |
| S7 | `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` | Related road-system synthesis. | 2026-07-11 | Existing Black-Lake artifact. |
| S8 | `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Related bias and causal-evidence synthesis. | 2026-07-11 | Existing Black-Lake artifact. |
| S9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%201103/daily_research_findings_2026-07-07_1103.md | Related spatial split and distribution-shift synthesis. | 2026-07-11 | Existing Black-Lake-Data artifact. |
| S10 | Live `Delphoa/Black-Lake` README | DEP-E naming, contents, log/report roles, commit-message standard. | 2026-07-11 | Repository authority inspected through connected GitHub access. |
| S11 | Live `Delphoa-Labs/Black-Lake-Data` README | Related raw-data DEP context and attribution standard. | 2026-07-11 | Repository authority inspected through connected GitHub access. |
| S12 | `.logs/20260711-Arxiv-CausalTAD-Trajectory-LOG.md` | Random selection, deduplication, extraction, and output-path process evidence. | 2026-07-11 | Public-safe process record generated in this run. |

## Appendix

### Replication Checklist

- [ ] Pin the exact public code commit and record repository license status.
- [ ] Resolve Xi'an/Chengdu paper datasets versus Xi'an/Porto README datasets.
- [ ] Inventory raw datasets, map-matching pipeline, road-graph versions, and anomaly generators.
- [ ] Recreate the 100 SD-pair sampling and ID/OOD split with deterministic seeds.
- [ ] Verify detour and route-switch generation against the paper definitions.
- [ ] Pin Python, framework, CUDA, and hardware configuration.
- [ ] Reproduce Tables I-III before attempting figure curves.
- [ ] Compare random, SD-disjoint, segment-disjoint, region-disjoint, and time-disjoint splits.
- [ ] Add calibration and subgroup false-positive analysis.
- [ ] Document all divergences without overwriting source-reported results.

### Public-Safe Selection Record

- Candidate paper units: 75,438 unique PDF parent directories.
- Uniform random method: PowerShell `Get-Random`.
- Selected zero-based index: 68,925.
- Accepted paper: arXiv:2412.18820v1.
- Reselections: 0.
- Duplicate and same-paper acceptance exclusions: 0.
- Scanned markers: arXiv ID, DOI, normalized title, and slug across Black-Lake artifacts, automation memory, and connected Black-Lake-Data search.

### Source Inventory

- Public arXiv abstract/metadata URL.
- Public arXiv HTML URL.
- Public arXiv PDF URL.
- Public arXiv TeX source URL.
- Public author code repository URL.
- Two related Black-Lake DEP manuscripts.
- One related Black-Lake-Data DEP research finding.
- No files deposited under `.source/`.
