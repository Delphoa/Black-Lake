# Report-Mark: VG Navigable Space

- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P08`
- Review date: 2026-07-20

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Visual-Geometry GP-based Navigable Space for Autonomous Navigation* |
| Authors | Mahmoud Ali; Durgkant Pushp; Zheng Chen; Lantao Liu |
| Identifier | arXiv:2407.06545v1; DOI:10.48550/arXiv.2407.06545 |
| Submitted | 2024-07-09 |
| Record | https://arxiv.org/abs/2407.06545 |
| Full paper | https://arxiv.org/html/2407.06545 |
| PDF | https://arxiv.org/pdf/2407.06545 |
| Source state | Verified complete after one bounded official-source repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260720-8636EDC7`; `BLAD-2200-20260720-8636EDC7-P08` |

## Concise Research Notes

VG-Nav combines two sparse Gaussian-process models. G-SGP models geometric occupancy and removes infeasible local navigation points; V-SGP uses semantic segmentation and manually assigned terrain traversability to score the remaining points. Their joint cost selects local actions toward a goal while representing predictive uncertainty.

In 15 simulation trials, VG-Nav reports a 29.21 +/- 0.46 m path and 1.03 +/- 0.06 m/s average achieved maximum velocity while avoiding both mud and high-slope ground in 100% of trials. Geometry-only was shorter (22.54 m) but avoided mud 0%; visual-only flat-start paths averaged 33.01 m/0.30 m/s and did not handle steep geometry. Three real-world trials per approach in selected scenarios qualitatively reproduce terrain, slope, and limited-field-of-view failure differences. Average per-observation compute is reported as 81 ms for VG-Nav, 43 ms for G-Nav, and 9 ms for V-Nav.

Evidence remains preliminary: small scenario/trial counts, manual terrain costs, segmentation class confusion, no standardized benchmark, no collision/near-miss denominator across broad environments, and no formal safety guarantee. The paper's modular uncertainty is valuable, but a separate verified safety controller is still required.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Section II | G-SGP/V-SGP/LNP method and uncertainty | Not executed or formally verified |
| Table I / simulation | 15 trials, path/velocity and avoidance percentages | Narrow constructed scenario |
| Section III-C | Three real-world scenarios, three trials per approach | Mostly qualitative; small denominator |
| Compute analysis | 81/43/9 ms per observation | Hardware/workload transfer unclear |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - barrier-constrained motion planning and fallback control.
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - spatial/temporal integrity for camera and range sensing.
3. `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` - interpretable geometry/temporal perception with recovery and runtime questions.

## Synthesis Note

### Concept Bridge

VG-Nav supplies interpretable visual/geometric traversability; iKalibr anchors sensor geometry and time, Stereo Lane Detection supplies temporal-reset audit patterns, and RRT-CBF adds an independent constraint layer between local costs and executed motion.

### Potential Implementations

1. Build an offline scenario evaluator with fixed collision, intervention, path, clearance, and latency denominators.
2. Add calibration/segmentation perturbations and explicit uncertainty-triggered abstention.
3. Wrap VG-Nav proposals in a barrier-certified or emergency-stop controller.

### Deeper Relationship Observations

1. Visual semantics can reject traversable geometry, while geometry can rescue field-of-view local minima.
2. Calibration error couples both models and may make agreement falsely reassuring.
3. Predictive GP variance is useful only when mapped to conservative action and fallback policies.

### Conceptual Similarities

1. All four artifacts separate perception/estimation from control decisions.
2. Each exposes uncertainty or constraints as an auditable interface.
3. Each requires recovery tests under temporal, spatial, or semantic degradation.

### MVP Implementations with Code Mock-Ups

1. Safety wrapper: `action = cbf_filter(vg_proposal, obstacles, dynamics)`.
2. Uncertainty gate: `return stop() if max(gp_variance(path)) > limit else action`.
3. Perturbation suite: `audit(run(calib_shift, dropped_frames, label_noise))`.

### Developer Challenges

1. Maintaining calibrated geometry and segmentation across lighting, terrain, and sensor motion.
2. Keeping sparse-GP updates bounded without hiding latency tails.
3. Integrating independent safety constraints without causing deadlock or oscillation.

### Author Challenges

1. Scaling beyond small, hand-designed scenarios and manual terrain costs.
2. Reporting collision, near-miss, intervention, recovery, and worst-case latency denominators.
3. Demonstrating cross-robot, cross-sensor, weather, and dynamic-obstacle transfer.

## Validation Notes

- First uniform draw at index 26,345 of 75,776; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with verified PDF and official full-paper HTML.
- Source claims and reviewer safety interpretation are separated.
- Exactly three related entries and three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2407.06545 - metadata, authors, date, DOI, abstract, and locators.
- https://arxiv.org/html/2407.06545 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2407.06545 - verified primary PDF; local copy withheld.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion - related safe motion planning.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration - related calibration integrity.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection - related interpretable perception.
- Source files: PDF, full-paper HTML, metadata HTML, and integrity records; all withheld locally.
