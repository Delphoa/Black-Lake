---
title: "MoCom MAV Comms - DEP-E"
generated_at: "2026-08-19 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of motion-encoded inter-MAV visual communication using event vision and a spiking neural network."
source_status: "verified complete local PDF and full-paper HTML inspected and withheld; public URLs cited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-19"
temporal_cutoff: "arXiv v1 and current published bibliographic context inspected through 2026-08-19"
primary_url: "https://arxiv.org/abs/2510.14770"
stable_identifier: "arXiv:2510.14770v1; DOI:10.48550/arXiv.2510.14770; DOI:10.1109/TRO.2026.3677077"
confidence_summary: "High for source identity, method reconstruction, printed tables, and visible figures; medium for interpretation; low for deployment generalization because code, data, and experiments were not reproduced."
safety_scope: "offline simulation, protocol analysis, synthetic event data, and supervised non-actuating implementation planning"
distribution_notes: "No PDF, HTML, metadata page, cache, rendering, receipt, verification record, extracted source text, or private path is redistributed."
---

# MoCom MAV Comms - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv metadata record | Canonical preprint metadata | HTML | arXiv:2510.14770v1 | https://arxiv.org/abs/2510.14770 | Public scholarly record; arXiv terms apply. | 2026-08-19 | Inspected |
| S2 | Complete primary paper | Primary artifact | PDF and official full-paper HTML | arXiv:2510.14770v1 | https://arxiv.org/pdf/2510.14770 ; https://arxiv.org/html/2510.14770 | Verified local copies inspected and withheld; no source document redistributed. | 2026-08-19 | Complete-source gate passed; all 13 PDF pages inspected |
| S3 | arXiv DOI | Persistent identity | DOI | 10.48550/arXiv.2510.14770 | https://doi.org/10.48550/arXiv.2510.14770 | Persistent preprint identity. | 2026-08-19 | Verified |
| S4 | IEEE journal record | Published identity | DOI / registry metadata | 10.1109/TRO.2026.3677077 | https://doi.org/10.1109/TRO.2026.3677077 ; https://api.crossref.org/works/10.1109/TRO.2026.3677077 | Crossref identifies IEEE Transactions on Robotics, 2026; the inspected arXiv full text remains v1. | 2026-08-19 | Bibliographic metadata inspected |
| S5 | USM Aerospace author page | Author-controlled context | Institutional web page | Publication listing | https://aerospace.eng.usm.my/index.php?id=563&option=com_content&view=article | Lists the paper in volume 42, pages 1680-1694. | 2026-08-19 | Inspected |
| S6 | SpikeJelly | Generic implementation dependency | GitHub repository | Public repository | https://github.com/fangwei123456/spikingjelly | Linked from the paper for SNN implementation; not a MoCom-specific release. | 2026-08-19 | Locator inspected; code not run |
| S7 | Spiking Pose Tracking DEP-E | Related processed artifact | Markdown | DEP-E-20260724-Spiking Pose Tracking | `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` | Public-safe Black Lake review; underlying sources remain separately attributed. | 2026-08-19 | Inspected |
| S8 | Group-Control Swarms DEP-E | Related processed artifact | Markdown | DEP-E-20260729-Group Control Swarms | `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md` | Public-safe Black Lake review; underlying sources remain separately attributed. | 2026-08-19 | Inspected |
| S9 | HESIM Hybrid DEP-E | Related processed artifact | Markdown | DEP-E-20260818-Hybrid Sensor HESIM | `.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md` | Public-safe Black Lake review; underlying sources remain separately attributed. | 2026-08-19 | Inspected |
| S10 | Private integrity and process records | Selection, deduplication, and verification evidence | Local records | arXiv:2510.14770 | Local paths withheld | Used only to validate randomness, repair, completeness, and the no-source-upload gate. | 2026-08-19 | Inspected; not a public locator |

The primary preprint lists Nengbo Zhang, Hann Woei Ho, and Ye Zhou; arXiv v1 was submitted on 2025-10-16 under `cs.CV`. Crossref now identifies a 2026 journal article in *IEEE Transactions on Robotics* with DOI `10.1109/TRO.2026.3677077`, and an author-controlled institutional page lists volume 42, pages 1680-1694. The reviewed full text is still the arXiv v1 artifact, whose running header says “submitted”; the later journal record is bibliographic context rather than proof that every page is identical to the version of record.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S3 | Canonical metadata / DOI | Title, authors, version, submission date, subject, abstract, and source locators. | Source identity and chronology. | High | Metadata does not validate methods or results. |
| E2 | S2 | Complete primary paper | Introduction, related work, equations 1-9, Algorithm 1, all experiment sections, Tables I-VI, Figures 1-13, conclusion, and references. | Channel design, segmentation, EventMAVNet, IMSR, experiments, claims, and stated future work. | High for reporting | Author-reported evidence; no experiment reproduced. |
| E3 | S2 visual pages | Rendered PDF figures and tables | All 13 pages, including codebook, pipeline, segmentation figures, recognition tables, flight encoding, and trajectories. | Cross-check of layout, metrics, and qualitative results. | High for transcription | Static pages cannot establish live reliability or supplementary-video behavior. |
| E4 | S4, S5 | Registry and institutional records | Journal, publisher, year, DOI, volume, and page range. | Published bibliographic identity. | High | Does not establish implementation release or empirical validity. |
| E5 | S6 | Generic repository | SpikeJelly framework locator linked by the paper. | Dependency context. | Medium | No MoCom-specific code, weights, data, controller, or manifest was established. |
| E6 | S7 | Related DEP manuscript | Event-only spiking perception, temporal evidence, modeled energy, and failure boundaries. | Sparse-perception and efficiency concept bridge. | Medium-high | Human pose tracking is not a communication protocol. |
| E7 | S8 | Related DEP manuscript | Compact group coding, globally constrained swarm control, and planner/execution tradeoffs. | Command-alphabet and physical-execution concept bridge. | Medium-high | Microrobot group control differs from event-observed MAV signaling. |
| E8 | S9 | Related DEP manuscript | Hybrid event-sensor noise, calibration, simulator provenance, and sim-to-real evaluation. | Sensor-regime and synthetic-evaluation concept bridge. | Medium-high | HESIM does not evaluate MoCom or its sensor. |
| E9 | S10 | Private process evidence | Required PDF enumeration, uniform random draw, all-history dedup scan, bounded repair receipt, integrity metrics, and zero-partial/source-upload checks. | Eligibility and complete-source gate. | High | Private paths and exact execution timestamps are intentionally excluded. |

## Executive Summary

MoCom proposes a visual side channel for micro air vehicles: a sender encodes information into deliberate flight motions; an event camera passively observes the motions; a temporal segmenter finds candidate actions; EventMAVNet classifies each action with a shallow spiking neural network; and an Integrated MAV Segmentation and Recognition decoder reconstructs a framed message. Four physical symbols represent `start`, `end`, `1`, and `0`, allowing the example protocol to encode direction, heading, and distance.

The strongest reported recognition result is the three-distance comparison. MoCom reports 96.51% ± 0.61%, 95.37% ± 1.01%, and 94.98% ± 1.17% accuracy at 0.9 m, 1.2 m, and 1.5 m. The paper also reports 1.26 ms per 10 test samples on an RTX 4090 over 100 runs. In three indoor flight demonstrations, three predefined 8-bit codes were decoded and used to send an executor MAV to three target positions.

These results establish a small controlled feasibility demonstration, not a general radio replacement. Dataset cardinalities and split identities are absent; the 3:1 split is not documented as flight-, session-, or vehicle-disjoint; segmentation uses three streams with nine actions each; a 2.5-second pause leads to one missed/merged action; the flight test has three messages with no repeated-trial error rate; and paper-specific code/data were not established. The receiver's model inference is fast, but the multi-second symbols and pauses dominate end-to-end throughput.

Reviewer confidence is high that the source identity, mechanism, printed tables, and visible figures are represented faithfully. Confidence is medium that the protocol can serve as a degraded-mode signaling channel in a controlled line-of-sight setting. Confidence is low for claims about contested-environment robustness, physical energy efficiency, dense-swarm scaling, or deployment safety because those boundaries were not directly tested.

## Detailed Summary

### Problem Context and Channel Model

Radio links in MAV swarms can face congestion, jamming, obstruction, and coordination overhead. MoCom takes inspiration from honeybee waggle dances and asks whether an agent's physical action can also be a message. This changes the communication substrate: the sender expends flight motion, the environment is part of the optical channel, and a receiver needs line-of-sight perception rather than an RF demodulator.

The paper defines four visually distinct motion primitives for `start`, `end`, binary `1`, and binary `0`. An event camera records changes rather than full RGB frames, producing tuples with spatial coordinates, timestamp, and polarity. A complete message becomes a sequence of valid motions separated by “empty” intervals so the temporal segmenter can isolate symbols.

The codebook is conceptually small and interpretable. It also couples semantic rate to vehicle dynamics. A symbol must last long enough to create sufficient events, differ from ordinary navigation, stay inside a safe volume, and remain visible at the intended distance and angle.

### Motion Segmentation

The segmentation path converts event streams into event frames and then into one-dimensional temporal features. For each frame it computes total event count, positive-event ratio, and a sliding-window event-count variance. Positive ratio captures polarity balance; variance is intended to distinguish motion from static periods.

The paper smooths features and applies thresholds, including a ratio threshold of 0.5 and a variance threshold derived from the sequence. Boundary differences locate candidate motion intervals. Heuristic refinement removes very short detections, merges segments separated by gaps of at most 10 frames, and ultimately discards motion shorter than 91 frames, approximately three seconds under the paper's timing assumptions.

The Integrated MAV Segmentation and Recognition algorithm buffers filtered events, waits until event-frame context exceeds a threshold such as 100 frames, segments the stream, classifies actions, discards background, and decodes only a framed sequence. The decoder requires the `start` symbol and extracts direction, three heading bits, and two distance bits before accepting an `end` signal.

This is a pragmatic pipeline, but its constants are tightly connected to symbol duration, camera rate, event density, and the controlled environment. The paper does not report a cross-sensor or cross-frame-rate threshold sweep.

### EventMAVNet

EventMAVNet consumes `128 x 128` two-channel positive/negative event frames over 16 timesteps. Two spiking convolutional stages use `3 x 3` kernels and 128 output channels, with batch normalization, Leaky Integrate-and-Fire neurons, and `4 x 4` max pooling. Spatial resolution falls to `32 x 32` and then `8 x 8`.

The resulting `128 x 8 x 8` feature is flattened, regularized with dropout, compressed to 128 dimensions, and projected to 50 spiking outputs. Ten output neurons vote for each of five categories: the four symbols plus background/noise. Temporal average scores are trained against one-hot labels using mean-squared error.

The architecture is small relative to several compared models and naturally matches sparse event data. The paper's efficiency evidence remains bounded to operation counts, an `Energy(mJ)` column, and GPU batch latency. It does not report end-to-end latency from the first physical motion through safe decoded execution on an onboard platform.

### Experimental Setup

Data were collected indoors with Crazyflie vehicles, a DVS Micro Explore event camera, a Lighthouse positioning system, and a PC with an RTX 4090 running Ubuntu. Sensor distances were 0.9 m, 1.2 m, and 1.5 m, labeled short, medium, and long. Each distance contains five classes: `0`, `1`, `start`, `end`, and background.

The paper states a 3:1 training-to-testing ratio and shows 40 training epochs, but it does not give sample counts, message counts, flight/session identities, random seeds, subject/vehicle separation, or an explicit validation split. The recognition comparisons use spike-CNN, spike-ResNet, and DVS-Gesture baselines. The segmenter is compared with a hidden Markov model and change-point detection.

### Recognition and Efficiency Results

Table I reports:

| Model | Short 0.9 m | Medium 1.2 m | Long 1.5 m |
|---|---:|---:|---:|
| spike-C | 94.63% ± 1.82% | 93.00% ± 1.64% | 91.49% ± 8.2% |
| spike-R | 96.49% ± 0.47% | 94.54% ± 0.24% | 92.35% ± 1.23% |
| DVS-G | 95.36% ± 1.4% | 94.12% ± 0.6% | 91.82% ± 1.56% |
| MoCom / EventMAVNet | 96.51% ± 0.61% | 95.37% ± 1.01% | 94.98% ± 1.17% |

Figure 6 reports 1.26 ms for 10 samples, averaged over 100 RTX 4090 runs, compared with 4.22 ms for DVS-Gesture, 18.9 ms for spike-CNN, and 33.07 ms for spike-ResNet. This supports low model inference latency in the measured batch configuration. It does not establish onboard latency, sender motion time, segment accumulation, message framing, controller delay, or network-independent operation.

### Segmentation Results

The segmentation comparison uses three streams, each with nine valid actions and eight empty signals. Pause durations are 2.5, 3.0, and 3.5 seconds. Figures report center error, duration error, and interval IoU against HMM and change-point detection baselines.

MoCom is generally strongest on center and IoU plots and gains a duration-error advantage as pauses reach 3.0 and 3.5 seconds. At 2.5 seconds, however, it incorrectly segments nine valid actions into eight. This is direct source evidence that the protocol has a minimum practical separation regime in the tested setup.

### Ablations and Internal Tensions

The resolution ablation reports 95.37% accuracy at `128 x 128`, 92.28% at `64 x 64`, and 81.79% at `32 x 32`. Reported energy falls from 2.567 mJ to 0.432 mJ and 0.108 mJ. The timestep ablation reports 95.37% at `F=16`, 91.98% at `F=8`, and 83.95% at `F=4`, with energy values of 2.567, 0.875, and 0.438 mJ. These support an accuracy/compute tradeoff, but the paper does not state how the energy values were measured or estimated.

The polarity ablation favors using both event polarities. E-BiPolNet reports 96.85%, 95.37%, and 94.24% across short, medium, and long distances. Those short/long figures do not match Table I's apparent full-model values of 96.51% and 94.98%, and the text does not explain whether Table IV is a single run, another seed, or a different configuration.

### Flight Demonstration and Protocol Semantics

The flight demonstration uses two vehicles: a performer MAV transmits by motion, and an executor MAV receives a decoded control command. The example 8-bit format includes framing plus one direction bit, three heading bits, and two distance bits. Three predefined codes correspond to three target positions; the paper shows the executor reaching all three.

The setup still includes a conventional control path from the decoded output to the executor and Lighthouse localization. The evidence therefore demonstrates visual message recognition inside a larger controlled system, not a completely radio-free autonomous swarm protocol. No repeated-trial denominator, bit-error rate, complete-message error rate, false-command rate, recovery policy, collision test, occlusion test, lighting sweep, wind test, or multi-sender contention test is reported.

### Publication and Reproducibility Surface

The arXiv paper says data and code will be made public upon publication and links the generic SpikeJelly framework. A bounded public search confirmed the later journal DOI and author-controlled publication listing but did not establish a MoCom-specific repository, dataset, weights, preprocessing manifest, controller package, or supplementary-video locator. This is a reproducibility gap, not proof that no artifact exists outside the inspected surface.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Deliberate MAV motions can form a visual communication alphabet decoded from event streams. | Author mechanism claim | E2, E3 | The mechanism is clearly specified and demonstrated for four symbols in a controlled setup. | High for mechanism |
| C2 | EventMAVNet improves recognition accuracy across three tested distances. | Author empirical claim | E2, E3 | Table I supports the comparison; absent dataset cardinality/split identities limit generalization. | High for reporting, medium for inference |
| C3 | EventMAVNet has the lowest reported inference latency among compared models. | Author empirical claim | E2, E3 | Supported for a batch of 10 on RTX 4090 over 100 runs; not end-to-end or onboard latency. | High for measured setting |
| C4 | The segmentation model is robust to varying empty intervals. | Author empirical claim | E2, E3 | Qualified: it performs well at 3.0/3.5 seconds but merges or misses one action at 2.5 seconds. | Medium |
| C5 | MoCom is energy efficient. | Author system implication | E2 | Tables report energy values, but the accounting method and sender/system energy are not established. | Low for system claim |
| C6 | MoCom can serve as an alternative to radio communication in constrained environments. | Author deployment implication | E2 | The evidence supports a small visual side-channel demonstration, not a general replacement under jamming, occlusion, density, or adverse conditions. | Low-medium |
| C7 | The published work is reproducible from its public implementation surface. | Potential overclaim | E4, E5 | Not established; publication metadata is available but MoCom-specific code/data were not located. | High that evidence is insufficient |
| C8 | A safe implementation should co-design motion, sensing, decoding, and command execution around one evidence manifest. | Reviewer synthesis | E2, E6-E8 | Strong cross-source design inference; not directly tested by the paper. | Medium-high |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv paper unit, require complete source integrity, review MoCom source-first, and create a public-safe Black Lake log, Report-Mark, DEP-E manuscript, README, and publication-index row.
- `Sources inspected`: Verified complete PDF and official full-paper HTML, arXiv metadata and DOI, Crossref journal metadata, an author-controlled institutional publication page, the generic SpikeJelly repository locator, live repository READMEs, private integrity/process records, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, grouped unique parent directories into paper units, built a used-ID index from live Black Lake, live Black-Lake-Data, and automation memory, withheld identifier-incomplete units, then drew one uniform PowerShell `Get-Random` index from the eligible list.
- `Inclusion criteria`: Evidence had to establish source identity, directly support methods/results/limitations, define implementation availability, prove selection/integrity, or provide concrete overlap with event/SNN perception, swarm command execution, or sensor calibration.
- `Exclusion criteria`: Abstract-only synthesis, duplicate paper markers, source files as public output, private machine context, unverified implementation claims, unrelated keyword hits, and background sources not used analytically were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication-boundary analysis.
- `Evidence handling`: Author claims and printed metrics are labeled as such. Reviewer interpretations are separate. Searchable HTML was cross-checked against every rendered PDF page, with special attention to Tables I-VI, Figures 2-13, equations, and Algorithm 1.
- `Uncertainty handling`: Missing sample counts, split identities, seeds, energy derivation, repeated flight trials, adverse-condition tests, code/data release, and end-to-end measurements remain explicit rather than inferred.
- `Extraction process`: Official HTML supplied searchable paragraphs, equations, table cells, captions, and references; all 13 PDF pages supplied layout and visual cross-checks. No extracted source text or rendering is redistributed.
- `Version control`: The reviewed paper is arXiv v1. The 2026 journal DOI is treated as current bibliographic context, not as evidence that the inspected v1 and final version are byte-identical.
- `Random selection methodology`: 75,967 PDFs collapsed to 75,964 unique parent units. The used-paper index contained 2,871 arXiv base IDs. After withholding 903 used-ID units and 185 identifier-incomplete units, one uniform draw selected zero-based eligible index 71,005 of 74,876 and arXiv `2510.14770`.
- `Dedup/reselection validation`: Live Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and live Black-Lake-Data `.lake-data`/`.reports` were searched for arXiv ID, both DOI values, normalized title, and slug. Exact/recent matches, duplicate rejections, and reselections were all zero. The public-safe cutoff date was 2026-08-18.
- `Source-integrity methodology`: The initial valid PDF lacked full-paper HTML. One bounded broker-controlled repair preserved the PDF and obtained official full-paper HTML plus metadata HTML. PDF size/header/EOF and HTML size/body/marker/heading/structure checks passed; zero partials remained before synthesis.
- `Reviewer stance`: Skeptical paper report, DEP-ready preservation, protocol/safety translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: MoCom's motion alphabet, event segmentation, EventMAVNet architecture, IMSR decoder, controlled recognition/segmentation/flight experiments, current publication metadata, reproducibility surface, and synthesis with exactly three related DEP entries.
- `Temporal boundary`: arXiv v1 submitted 2025-10-16 and public bibliographic context inspected through 2026-08-19.
- `Evidence limits`: No code, dataset, weights, supplementary video, event recording, simulator, controller, or experiment was executed. Dataset size, session identity, and energy methodology are unavailable in the inspected paper.
- `Assumptions`: The verified PDF and official HTML represent the same arXiv v1 work; printed tables and figures accurately report the authors' experiments; the Crossref DOI and author page identify the later journal publication.
- `Constraints`: Source files remain local. Public output omits private paths, user/machine names, timezone labels, and exact execution timestamps. Implementation examples remain synthetic and non-actuating.
- `Out of scope`: Operating a MAV, producing autonomous control code, testing jamming or stealth, reproducing the model, auditing unpublished data, proving novelty exhaustively, or certifying a communication system.
- `Intended use`: Research review, DEP deposition, simulator design, protocol evaluation planning, and safe product ideation.
- `Audience`: Event-vision researchers, robotics communication teams, SNN engineers, flight-safety reviewers, simulator developers, and research auditors.
- `Reproducibility boundary`: The paper supports conceptual reconstruction and metric transcription but not exact reproduction without the promised code/data and full experiment manifests.
- `Operational boundary`: Any physical actuation requires separate authorization, validated hardware, geofencing, collision protection, emergency stop, and human oversight.
- `Data sensitivity`: Flight logs and event recordings can reveal locations, people, infrastructure, vehicle identifiers, and operational behavior; they require minimization and controlled retention.

## Observations

- `Observed pattern`: MoCom's fast classifier sits inside a slow physical protocol. Symbol and pause durations, not neural inference, are likely the dominant communication-latency terms.
- `Technical implication`: Event counts are both the perceptual input and a protocol resource. Lower-motion-energy symbols may become less observable, so transmitter energy and receiver confidence cannot be optimized independently.
- `Observed pattern`: Background is an explicit fifth class, and framing symbols are explicit. These are valuable protocol choices because they create rejection opportunities rather than forcing every event interval into `0` or `1`.
- `Contradiction or tension`: Table I's full-model short/long values differ from Table IV's E-BiPolNet values, while the medium value matches exactly. The source gives no run/configuration explanation.
- `Evidence tension`: The paper claims low power but does not connect ablation `Energy(mJ)` values to a stated device, equation, measurement procedure, or whole-system boundary.
- `Boundary observation`: The 2.5-second pause failure shows that the empty interval is part of the channel code, not merely preprocessing convenience.
- `Cross-DEP observation`: Spiking Pose Tracking, Group-Control Swarms, and HESIM jointly imply an evidence chain from calibrated sensor events through sparse temporal inference to safety-bounded physical command compilation.
- `Reviewer hypothesis`: An error-detecting code with confidence-based abstention and re-transmission could improve safety more than adding recognition capacity alone.

## Considerations

**Communication semantics:** A motion alphabet must be disjoint from ordinary navigation, recovery maneuvers, collision avoidance, and gust response. Otherwise the receiver can interpret safety behavior as data or data as safety behavior.

**Throughput and energy:** End-to-end accounting should include performer flight energy, receiver sensing, buffering, inference, framing, re-transmission, and executor control. Classifier `Energy(mJ)` and GPU batch latency are incomplete system proxies.

**Safety:** Deliberate arcs and translations consume swept volume. A protocol compiler needs conservative clearance, geofencing, acceleration bounds, line-of-sight checks, and a fail-closed rule when either motion or decoding confidence leaves the verified envelope.

**Security:** An optical channel may reduce RF dependence but introduces spoofing, replay, mimicry, occlusion, and observation risks. Authentication cannot be inferred from a visible motion pattern. Consequential commands require cryptographic or independently trusted authorization where feasible.

**Privacy and operational security:** Event data are sparse, but motion patterns, environments, and trajectories can still identify infrastructure and behavior. Raw streams should be minimized, access-controlled, and deleted under a declared retention policy.

**Evaluation:** Session-disjoint splits, vehicle-disjoint tests, calibrated sensor profiles, repeated seeds, matched baseline tuning, trial denominators, adverse-condition sweeps, and message-level metrics are needed before deployment claims.

**Fallback posture:** The present evidence best supports a simulator-first degraded-mode side channel. A fielded system should retain a safe fallback and should not silently route decoded messages into actuation.

## Strengths

- The paper connects a physical alphabet, event sensing, temporal segmentation, spiking recognition, framed decoding, and flight semantics in one intelligible pipeline.
- The four-symbol codebook and explicit background class make the communication contract reviewable and create natural rejection points.
- The paper evaluates three observation distances and reports uncertainties for the main recognition comparison.
- The segmentation study exposes timing sensitivity rather than showing only a favorable stream.
- Resolution, timestep, and polarity ablations reveal useful accuracy/compute tradeoffs.
- The three flight trajectories show that decoded visual messages can reach a control layer in a controlled setup.
- Official full-paper HTML and the PDF make equations, algorithm flow, tables, and figures inspectable.
- The later journal DOI supplies durable bibliographic identity beyond the preprint.

## Weaknesses

- Dataset cardinalities, sample identities, capture-session counts, and class balance are not reported.
- The 3:1 split is not documented as session-, message-, environment-, or vehicle-disjoint, leaving leakage risk unresolved.
- The segmentation comparison uses three streams with nine actions each and no repeated-seed uncertainty.
- The system misses one action at the shortest tested pause, showing a material temporal-boundary failure.
- The flight demonstration has only three predefined messages and no repeated-trial success/error denominator.
- Table I and Table IV disagree on apparent full-model accuracies without explaining run or configuration differences.
- The paper's energy values lack an explicit measurement/estimation method and exclude performer flight and whole-system energy.
- RTX 4090 batch inference does not establish onboard, streaming, or end-to-end communication latency.
- Lighting, occlusion, viewpoint, multiple simultaneous senders, wind, navigation-motion confusion, and adversarial spoofing are not systematically tested.
- The paper says code/data will be public after publication, but a paper-specific public release was not established in this review.
- The controlled system still relies on Lighthouse positioning and a separate executor-control path, limiting claims of a self-contained radio alternative.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish immutable dataset manifests | Reproducibility | Cardinalities and split identities are missing. | Auditable leakage-free comparisons. | Storage and maintenance. | Hash every recording and publish session/vehicle/message-disjoint folds. |
| Reconcile Tables I and IV | Evidence integrity | Apparent full-model accuracies conflict. | Reliable downstream interpretation. | Low editorial cost. | Release run-level values, seeds, configs, and a correction note. |
| Define an end-to-end energy model | Systems evidence | Current energy boundary is unclear. | Honest comparison with RF/VLC alternatives. | Hardware instrumentation. | Measure performer, sensor, compute, controller, and recovery energy per useful bit/message. |
| Report channel metrics | Communication evaluation | Class accuracy is not message reliability. | Protocol-level comparability. | More trials and tooling. | Measure symbol error, bit error, packet completion, false command, abstention, and retry rate. |
| Add session/vehicle/environment holdouts | Generalization | Random sample splits may leak capture conditions. | More credible transfer evidence. | Reduced training data. | Pre-register folds and test unseen vehicles, sessions, rooms, backgrounds, and trajectories. |
| Sweep the optical channel | Robustness | Lighting/viewpoint/occlusion remain open. | Verified operating envelope. | Large capture matrix. | Factorial tests over illumination, distance, angle, speed, clutter, motion, and sensor settings. |
| Calibrate sensor noise | Sim-to-real | Event statistics are device/regime dependent. | Better synthetic testing and transfer. | Calibration data and modeling. | Use HESIM-style profiles and real-data holdouts across sensors. |
| Add error detection and abstention | Protocol safety | A valid-looking wrong message can actuate a vehicle. | Fail-closed behavior. | Lower throughput. | Inject symbol errors, measure detection, and verify no unsafe command passes. |
| Compile safe motion primitives | Physical safety | Code motions consume flight volume and can conflict with navigation. | Deployable protocol boundary. | Planner complexity. | Verify swept volume, clearance, energy, observability, and stop conditions in simulation. |
| Release code/data/supplement | Reproducibility | The promised surface was not located. | Independent reproduction and extension. | Documentation and licensing. | One pinned command recreates tables, figures, and synthetic/flight evaluation receipts. |

## Potential Implementations

### Calibrated event-motion channel emulator

- `User`: Event-vision and aerial-robotics researchers.
- `Goal`: Test a MoCom-like protocol without live actuation.
- `Core mechanism`: Render safe synthetic motion primitives, apply HESIM-style sensor profiles, run segmentation/classification adapters, and compute symbol/message metrics.
- `Required inputs`: Synthetic trajectories, codebook, camera model, calibrated noise profiles, timing jitter, occlusion masks, and decoder rules.
- `Outputs`: Event streams, decoded symbols, message receipts, error curves, confidence traces, and operating-envelope report.
- `Risk controls`: Synthetic-only; no vehicle driver; no private captures; fail closed outside calibrated sensor regimes.
- `Evaluation`: Known-message tests over distance, lighting, angle, pause, noise, and occlusion sweeps.

### Safety-bounded motion protocol compiler

- `User`: Flight-control and protocol engineers.
- `Goal`: Convert a short command into observable yet safe physical symbols.
- `Core mechanism`: Choose a codeword, compile symbols into trajectories, and reject any plan that violates clearance, acceleration, battery, visibility, timing, or geofence constraints.
- `Required inputs`: Vehicle model, state uncertainty, obstacle map, observer geometry, codebook, energy budget, and safety envelope.
- `Outputs`: Timestamped symbol plan, expected observability, swept-volume certificate, and reject reason.
- `Risk controls`: Simulation gate; human approval; independent emergency stop; no hardware export from the MVP.
- `Evaluation`: Property tests, reachability/clearance checks, perturbation sweeps, and false-symbol analysis.

### Evidence-first degraded-mode receiver

- `User`: Safety and resilience teams.
- `Goal`: Treat motion signaling as a bounded side channel rather than an unquestioned command bus.
- `Core mechanism`: Segment events, calibrate symbol confidence, validate framing/checksum, compare with an independent state/authorization channel, and abstain on disagreement.
- `Required inputs`: Event stream, sensor profile, model/version, codebook, command policy, state estimate, and authorization evidence.
- `Outputs`: Accept/reject/abstain decision, decoded payload, confidence, provenance, and audit receipt.
- `Risk controls`: No direct actuation; minimum-confidence and agreement rules; rate limiting; replay detection; human review for consequential commands.
- `Evaluation`: Synthetic faults, replay/mimic tests, session holdouts, and zero-unsafe-acceptance acceptance criteria.

## Three Ways to Exercise This Research

1. `Protocol arithmetic audit`: Define four synthetic symbols and one eight-bit format; compute symbol duration, required pauses, total message time, useful bitrate, and a conservative retry budget. Success means every timing assumption is explicit; stop if any rate claim omits physical motion or segmentation delay.
2. `Sensor-regime robustness lab`: Generate a toy event-count sequence for known symbols, inject brightness-dependent polarity imbalance, missed events, and timing jitter, then compare fixed thresholds with calibrated profiles. Success means error and abstention are reported by regime; stop before using real or private flight data.
3. `Simulation-only safety gate`: Compile a synthetic message into planar trajectories, inflate obstacles by state uncertainty, and reject any symbol whose swept path violates clearance or observer visibility. Success means every accepted motion has a replayable certificate; stop before connecting the prototype to flight hardware.

## Example MVP Product

- `Product name`: MotionLink Lab
- `Target user`: Event-camera researchers, MAV communication engineers, and flight-safety reviewers.
- `Problem`: Classifier accuracy alone cannot show whether a motion-coded message is observable, timely, energy-bounded, and safe to execute.
- `Core workflow`: Define a codebook and vehicle envelope; generate synthetic trajectories; simulate calibrated event streams; run pluggable segmentation/recognition; decode framed messages; evaluate symbol/message errors, latency, energy proxies, visibility, clearance, and abstention; export an evidence receipt.
- `Data requirements`: Synthetic trajectories and backgrounds by default; optional authorized event captures with sensor calibration, session IDs, retention policy, and redistribution status.
- `Architecture`: Local CLI/notebook; versioned codebook registry; trajectory generator; HESIM-style sensor-profile adapter; segmentation/recognition interface; decoder; safety checker; metrics engine; immutable receipt writer.
- `Success metrics`: Reproducible known-message tests; zero unsafe command acceptance in the MVP suite; calibrated abstention; disclosed symbol/bit/message error; complete latency and energy boundaries; no private-path or source-file leakage.
- `Risk controls`: Local-only processing, synthetic-first defaults, no hardware driver, no direct actuation, explicit authorization evidence, geofence/clearance checks, rate limiting, and human review.
- `Limitations`: A simulator cannot prove real-flight reliability; sensor models can be wrong; physical energy and aerodynamic effects need hardware measurement; the MVP does not authenticate visible motion by itself.
- `MVP boundary`: No live vehicle control, no autonomous command execution, no RF-jamming experiment, no surveillance deployment, and no claim of certified communication.
- `Deployment model`: Offline local notebook and command-line tool.
- `Evaluation plan`: Unit tests for code/framing, synthetic sensor sweeps, session-disjoint replay tests, perturbation tests, safety-property checks, and blinded reviewer inspection of receipts.
- `Failure modes`: Threshold overfit, device-profile mismatch, motion/navigation confusion, occlusion, unsafe trajectory compilation, replay/mimicry, and misleading energy accounting.
- `Maintenance plan`: Version codebooks, sensor profiles, model weights, metric definitions, safety envelopes, datasets, and revocation notes; rerun the evidence suite after any change.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| MoCom | Primary paper | Motion-coded MAV communication, event segmentation, EventMAVNet, IMSR, and flight demonstrations. | https://arxiv.org/abs/2510.14770 |
| MoCom journal record | Published identity | Durable IEEE Transactions on Robotics citation. | https://doi.org/10.1109/TRO.2026.3677077 |
| SpikeJelly | Generic implementation framework | SNN framework explicitly linked in the paper; not a MoCom release. | https://github.com/fangwei123456/spikingjelly |
| Spiking Pose Tracking - DEP-E | Related Black Lake review | Event-only spiking temporal perception, accuracy/efficiency tradeoffs, and deployment energy boundary. | `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` |
| Group-Control Swarms - DEP-E | Related Black Lake review | Compact group coding and the distinction between planning simplicity and physical execution burden. | `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md` |
| HESIM Hybrid - DEP-E | Related Black Lake review | Calibrated event-sensor noise, simulator provenance, and sim-to-real validation. | `.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2510.14770 | Identity, authors, date, abstract, version, subjects, and public locators. | 2026-08-19 | Primary metadata. |
| R2 | https://arxiv.org/html/2510.14770 | Complete searchable paper: methods, equations, algorithm, experiments, tables, figures, conclusion, references. | 2026-08-19 | Primary full text. |
| R3 | https://arxiv.org/pdf/2510.14770 | Full paper layout and all 13 rendered-page cross-checks. | 2026-08-19 | Primary PDF; source file withheld locally. |
| R4 | https://doi.org/10.48550/arXiv.2510.14770 | Persistent arXiv identity. | 2026-08-19 | Primary identifier. |
| R5 | https://doi.org/10.1109/TRO.2026.3677077 | Published IEEE journal identity. | 2026-08-19 | Version-of-record locator. |
| R6 | https://api.crossref.org/works/10.1109/TRO.2026.3677077 | Published title, authors, publisher, journal, year, and DOI metadata. | 2026-08-19 | Registry metadata. |
| R7 | https://aerospace.eng.usm.my/index.php?id=563&option=com_content&view=article | Author-controlled listing of volume and page range. | 2026-08-19 | Institutional context. |
| R8 | https://github.com/fangwei123456/spikingjelly | Generic SNN framework dependency. | 2026-08-19 | Not evidence of MoCom-specific code/data. |
| R9 | `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` | Spiking event perception and efficiency bridge. | 2026-08-19 | Inspected related DEP. |
| R10 | `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md` | Swarm coding and execution bridge. | 2026-08-19 | Inspected related DEP. |
| R11 | `.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md` | Sensor calibration and sim-to-real bridge. | 2026-08-19 | Inspected related DEP. |
| R12 | Private integrity/process evidence | Random selection, deduplication, source repair, verification, and no-source-upload gate. | 2026-08-19 | Withheld local context; no private path or source bytes published. |

## Appendix

### Source-Integrity Summary

- Initial state: partial because verified full-paper HTML was missing.
- Repair: one broker-controlled single-paper acquisition; no strategy switch and no blind retry.
- PDF: 7,531,759 bytes; `%PDF-` header; trailing `%%EOF`; 13 pages; not encrypted.
- Official full-paper HTML: 257,858 bytes; 71,273 body characters; document marker; 55 headings; six structure terms.
- Metadata HTML: 41,816 bytes; treated only as metadata.
- TeX/source package: unavailable after the permitted route redirected outside the broker's exact-surface policy.
- Remaining partials: zero.
- Public source deposition: none; source documents, caches, renderings, receipts, and verification files remain local.

### Selection and Deduplication Summary

- Required enumeration: 75,967 PDFs and 75,964 unique parent units.
- Used-paper index: 2,871 arXiv base IDs.
- Withheld before draw: 903 used-ID units and 185 identifier-incomplete units.
- Eligible units: 74,876.
- Uniform selected zero-based index: 71,005.
- Accepted paper: arXiv `2510.14770`.
- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; Black-Lake-Data `.lake-data` and `.reports`.
- Identity checks: arXiv ID, arXiv DOI, published DOI, normalized title, and slug.
- Exact/recent matches: zero; duplicate rejections: zero; reselections: zero.
- Public-safe 24-hour cutoff date: 2026-08-18.

### Replication Checklist

- [ ] Obtain the promised MoCom-specific code, weights, data, controller, and license from an author-controlled source.
- [ ] Publish exact recording counts, class balance, session/vehicle/environment identifiers, and checksums.
- [ ] Use session-, vehicle-, trajectory-, and environment-disjoint splits with a declared validation set.
- [ ] Pin Python, PyTorch, SpikeJelly, CUDA, preprocessing, random seeds, and baseline configurations.
- [ ] Reproduce Tables I-IV with run-level values and reconcile the full-model accuracy mismatch.
- [ ] Define the `Energy(mJ)` equation, device constants, measurement boundary, and uncertainty.
- [ ] Measure streaming and end-to-end latency, not only batch inference.
- [ ] Report symbol error, bit error, complete-message error, false-command rate, abstention, and retries.
- [ ] Repeat flight messages across lighting, distance, angle, clutter, occlusion, wind, vehicle, and sensor regimes.
- [ ] Add calibrated event-noise profiles and a real-data holdout.
- [ ] Evaluate multi-sender contention, navigation-motion confusion, replay/mimicry, and safe fallback.
- [ ] Keep all raw flight/event sources local or access-controlled unless redistribution is separately authorized.
