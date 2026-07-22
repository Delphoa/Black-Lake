# Report-Mark: FAVLA Fast-Slow

- Public run marker: 2026-07-22 (date only)
- Review type: Source-first paper review, critique, implementation translation, and DEP-E synthesis
- Source policy: Complete source inspected locally; all source documents and private execution records withheld

## Source Metadata

| Field | Value |
|---|---|
| Title | *FAVLA: A Force-Adaptive Fast-Slow VLA model for Contact-Rich Robotic Manipulation* |
| Authors | Yao Li; Peiyuan Tang; Wuyang Zhang; Chengyang Zhu; Yifan Duan; Weikai Shi; Xiaodong Zhang; Zijiang Yang; Jianmin Ji; Yanyong Zhang |
| arXiv | arXiv:2602.23648v1; submitted 2026-02-27 |
| DOI | https://doi.org/10.48550/arXiv.2602.23648 |
| Source platform | arXiv preprint in `cs.RO`; ICML 2026 preprint styling does not establish acceptance |
| Primary record | https://arxiv.org/abs/2602.23648 |
| Full-paper HTML | https://arxiv.org/html/2602.23648 |
| Source package | https://arxiv.org/e-print/2602.23648 |
| License | CC BY 4.0, linked by the canonical arXiv record |
| Official code | Not available from inspected sources; no author-verified repository was found |
| Access date | 2026-07-22 |

## Selection and Deduplication

`rg --files -g "*.pdf"` found 75,780 PDFs representing 75,777 unique parent-directory paper units. The units were sorted, then PowerShell `Get-Random` selected zero-based index 47,262 uniformly from `[0, 75,777)`. The first draw was accepted with zero duplicate exclusions, zero other exclusions, and zero reselections.

Dedup scanned live Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; relevant Black-Lake-Data entries; and prior-24-hour same-paper markers. Keys included arXiv ID `2602.23648`, arXiv DOI, normalized title, and `FAVLA-Fast-Slow` slug variants. The only match was one metadata-only author-inventory row. It is not a prior Arxiv DEP log, report, or DEP-E manuscript and therefore did not trigger exclusion.

## Local Source Integrity

The unit was initially partial. Its existing 22,218,424-byte PDF passed the 10 KB threshold, began with `%PDF-`, contained trailing `%%EOF`, and was preserved byte-for-byte, but full-paper HTML and the companion verification bundle were missing. Review paused while one bounded direct-HTTPS repair collected official metadata HTML, official full-paper HTML, and the arXiv source archive. The transfer used a 200 MB target ceiling, a 50 MB partial ceiling, a 500 MB free-space floor, no credentials, and a bounded source-candidate sequence.

Final classification is complete. Full-paper HTML is 212,377 bytes with 56,054 body characters, a full-document marker, 54 section/heading markers, seven paper-structure term classes, no abstract-only/error/conversion marker, and zero partial files. Metadata HTML is 43,391 bytes and was retained as metadata only. The local README, attribution/provenance, machine-readable summary, preflight manifest, and verification report were updated before substantive review.

All 16 PDF pages were rendered and inspected inside the private archive. Architecture diagrams, success-rate and frequency charts, force and ablation tables, dataset and model tables, qualitative sequences, and failure panels were legible. Temporary renderings were removed after inspection. No source file, extracted material, render, verification record, or private archive locator is included in the repository; no `.source/` directory was created.

## Research Notes

### Problem and Method

FAVLA targets a mismatch between semantic planning and contact response. Cameras and a large VLM update relatively slowly, while force sensing and action correction may need higher-rate feedback. Instead of concatenating every modality into one unified-frequency prefix, the system caches semantic context from a slow PaliGemma-based VLM and runs a smaller action expert more frequently.

The slow VLM consumes two RGB views, language, and historical six-axis force/torque tokens. The fast action expert consumes current seven-dimensional end-effector/gripper state, cached VLM context, noisy action tokens, and the latest force sequence. A TCN produces four force tokens. Layerwise cross-attention injects these tokens directly into action representations, and conditional flow matching emits 32-step, seven-dimensional delta-pose/gripper chunks.

A 1.6M-parameter auxiliary head predicts an EMA-smoothed, weighted variance of future force/torque. Its normalized output controls how many times the action expert runs inside a slow cycle. The system fixes the sampled flow noise across repeated calls and temporally ensembles overlapping chunks to limit jerk and inconsistency. The auxiliary loss weight is 0.1.

### Data and Training

The real-robot platform uses dual 7-DoF arms, wrist and external cameras, and wrist force/torque sensors. Four task-specific datasets cover USB Insertion, Gear Assembly, Box Flipping, and Board Wiping. They total 260 demonstrations, 198,250 frames, and about 1.84 hours. USB and Gear contain 80 trajectories each; Box and Wiping contain 50 each.

Force/torque and end-effector state are recorded at 200 Hz, while cameras run at 30 Hz. The appendix states that every stream is synchronized and downsampled to 30 Hz for training. This is a material tension with the paper's high-frequency-force motivation: the architecture may query force more often during execution, but the source does not fully specify the native force sampling retained per action-expert call, actual control rates, queueing, or sensor-to-action latency.

The VLM has 2.6B parameters, the action expert 300M, the TCN force encoder 25.2M, and the variance predictor 1.6M. The VLM and action expert initialize from `pi_0` and use LoRA. Each task model trains for 30,000 iterations with batch size 8, AdamW, and cosine decay from `2.5e-5` to `1e-6`; the appendix reports about six hours per task on one A100 80GB GPU.

### Results and Attribution

Evaluation uses 25 USB, 30 Gear, 20 Box, and 10 Wiping trials per method. FAVLA reports 80.0%, 93.3%, 80.0%, and 70.0%, for an unweighted task mean of 80.8%. The strongest baseline mean is ForceVLA at 67.0%, so the reported improvement is 13.8 percentage points. Vision-only `pi_0` averages 42.8%, yielding the paper's 38.0-point comparison.

The chart requires two qualifications. First, FAVLA is not uniquely best on Box Flipping: FAVLA, TA-VLA, and ForceVLA all report 80%. Second, unequal task denominators mean the 80.8% unweighted mean differs from the approximately 83.5% pooled-trial rate implied by 71 successes among 85 trials. The source uses task-balanced averaging; a production evidence card should report both.

Average peak contact force is 7.7 N on Gear and 9.9 N on Box, compared with 12.0 N and 12.2 N for vision-only `pi_0`. The next-best listed force values are 10.9 N on Gear and 10.0 N on Box, making the Box margin over the strongest comparator only 0.1 N. No force distribution, interval, impulse, duration, safety-stop rate, damage rate, or sensor calibration uncertainty is reported.

The cumulative component ablation moves Box/Wiping success from 50%/10% to 65%/60% with the force-injected action expert, 70%/60% after variance prediction, and 80%/70% after adaptive inference. This supports the assembled system but is not a full factorial isolation. The frequency chart reports USB/Gear success at 52%/70% for `n=1`, 52%/77% for `n=2`, 60%/90% for `n=4`, and 80%/93% for adaptive scheduling. Average calls, latency, and energy are absent, so the chart does not prove a better matched-compute frontier.

### Failure Cases and Reviewer Assessment

The authors show four failure classes: force ambiguity can cause premature USB release; gear misalignment can still cause a force-limit stop; low box force can cause slipping; and an incorrect wiping trajectory leaves residue. These examples directly limit any interpretation that lower average peak force equals robust or safe contact understanding.

The paper provides a compelling architecture hypothesis and unusually useful visual/task evidence for a recent preprint. Confidence is high that the source reports the described mechanism and numbers, medium that the full design causes the measured gains, and low that it generalizes to new robots, sensors, objects, or industrial safety regimes. The absent code/data/timing surface, 30 Hz training data, small trial counts, missing uncertainty, cumulative ablations, and under-specified control timing are the main blockers to stronger conclusions.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitation |
|---|---|---|---|---|---|
| E1 | arXiv metadata and DOI | Identity, authors, version, submission date, category, license link | Source attribution | High | Metadata only |
| E2 | Complete PDF, HTML, and TeX; sections 1-3 | Architecture, force adapter, variance target, loss, scheduler, noise reuse, temporal ensemble | Method reconstruction | High for transcription | No code or independent implementation |
| E3 | Complete PDF, HTML, and TeX; section 4 | Baselines, trials, task rates, force table, cumulative and frequency ablations | Empirical assessment | High for transcription | Small source-reported study; no intervals |
| E4 | Appendix and Figures 9-14 | Sensor rates, downsampling, dataset size, model/training settings, qualitative results, failure cases | Reproducibility and limits | High | Dataset and logs unavailable |
| E5 | Local integrity verification summarized publicly | PDF/HTML gate, repair status, visual review, zero partials, source locality | Complete-source validation | High | Private evidence withheld |
| E6 | Exactly three related DEP manuscripts | Action routing, calibration, and constraint/fallback relationships | Cross-DEP synthesis | Medium | Related work does not validate FAVLA |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-Semantic%20Skill%20MoE/semantic_skill_moe_manuscript.md
   - Relevance: Both separate semantic context from action generation and try to keep action chunks internally consistent. The related DEP adds skill-conditioned routing, route stability, rare-skill coverage, and independent action admissibility.
   - Source basis: Its reviewed primary paper, *Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation*, including offline skill labels, chunk-consistent routing, physical-task results, and routing limitations.
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
   - Relevance: FAVLA assumes coherent camera, proprioception, and force timing. The related DEP provides spatiotemporal calibration, excitation, drift, residual, versioning, and downstream evidence concepts needed to make multi-rate fusion auditable.
   - Source basis: Its reviewed iKalibr paper, official implementation, sensor-suite experiments, timing-offset estimates, limitations, and calibration-evidence proposal.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
   - Relevance: FAVLA proposes learned action chunks, while RRT-CBF distinguishes high task performance from admissible motion through explicit barrier constraints, state/solver checks, tracking, and fallback.
   - Source basis: Its reviewed primary motion-planning paper, CBF-QP formulation, MPC tracking, manipulator examples, and explicit simulation-to-deployment limits.

## Synthesis Note

### Concept Bridge

Together, the four artifacts describe a layered contact-control stack. FAVLA allocates semantic and force-reactive computation across timescales. Semantic Skill MoE shows how action routing can be made interpretable and chunk-consistent. iKalibr establishes that asynchronous sensor streams require explicit spatial/temporal provenance before fusion. RRT-CBF supplies an independent admissibility and fallback layer. The resulting design principle is that a learned fast path should be both evidence-aware and subordinate to calibration, freshness, constraints, and deterministic fallback; success rate or lower average force alone is not a safety argument.

### Potential Implementations

1. **Multi-rate trace auditor:** Reconstruct sensor age, slow/fast cycles, scheduler decisions, action changes, force events, and deadline misses from authorized offline traces; export a public-safe evidence card.
2. **Matched-compute scheduler lab:** Compare adaptive, static, random, threshold, and oracle schedules in simulation with equal average and maximum action-expert calls, then measure success, force, latency, and failure recovery.
3. **Calibrated constraint wrapper:** Place mocked learned proposals behind calibration freshness, timestamp, force, velocity, workspace, solver, and fallback gates; require every missing or invalid signal to fail closed.

### Deeper Relationship Observations

1. FAVLA and Semantic Skill MoE both reuse a slower semantic representation while a smaller action mechanism determines local execution; the former conditions on force and time, while the latter conditions on semantic skill and route identity.
2. FAVLA's scheduler can only be as meaningful as its sensor alignment: iKalibr's timing-offset and observability concerns turn “fresh force” from an architectural label into a measurable systems property.
3. FAVLA reduces average peak force but still exhibits force-limit and ambiguity failures; RRT-CBF explains why learned proposal quality and independent admissibility must remain separate evidence layers.

### Conceptual Similarities

1. Each work decomposes a complex pipeline into a slow/global representation layer and a faster/local decision or verification layer.
2. Each relies on a compact intermediate signal—force variance, skill embedding, calibration state, or barrier margin—to govern downstream behavior.
3. Each requires explicit boundary evidence: routing stability, timing/calibration validity, constraint feasibility, or contact safety cannot be inferred from aggregate task success.

### MVP Implementations with Code Mock-ups

#### 1. Fresh-Force Gate

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Sample:
    captured_ms: int
    value_n: float


def require_fresh(sample: Sample, decision_ms: int, max_age_ms: int) -> float:
    age = decision_ms - sample.captured_ms
    if age < 0 or age > max_age_ms:
        raise ValueError(f"stale or invalid force sample: age={age}ms")
    return sample.value_n


print(require_fresh(Sample(captured_ms=980, value_n=7.7), 1000, 25))
```

This dependency-free gate makes sample age explicit. A real implementation also needs clock-domain reconciliation, calibration versioning, units, saturation checks, and safe fallback.

#### 2. Matched-Compute Comparison

```python
from statistics import mean


def summarize(name: str, trials: list[dict]) -> dict:
    calls = sum(row["ae_calls"] for row in trials)
    return {
        "name": name,
        "mean_success": mean(row["success"] for row in trials),
        "mean_peak_force": mean(row["peak_force_n"] for row in trials),
        "total_calls": calls,
    }


static = [{"success": 1, "peak_force_n": 10.0, "ae_calls": 4}]
adaptive = [{"success": 1, "peak_force_n": 9.9, "ae_calls": 4}]
assert summarize("static", static)["total_calls"] == summarize("adaptive", adaptive)["total_calls"]
```

The mock-up refuses to compare policies with different total calls. A study needs multiple tasks, seeds, latency, call distributions, and confidence intervals.

#### 3. Independent Action Gate

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class GateState:
    calibration_fresh: bool
    sample_fresh: bool
    force_n: float
    solver_ok: bool
    fallback_ready: bool


def decide(state: GateState, force_limit_n: float) -> str:
    valid = state.calibration_fresh and state.sample_fresh and state.solver_ok
    if valid and state.force_n <= force_limit_n:
        return "allow_mock_proposal"
    if state.fallback_ready:
        return "safe_fallback"
    return "stop"


print(decide(GateState(True, True, 7.7, True, True), 8.0))
```

This is a simulation policy, not a hardware controller. Platform-specific dynamics, verified limits, real-time guarantees, and independent safety review remain mandatory.

### Developer Challenges

1. Reconstruct the absent multi-rate runtime contract: sensor sampling, clock synchronization, buffer windows, VLM/AE cadence, actuation timing, queueing, cache age, and fixed-noise reuse must be observable and testable.
2. Build fair baseline and scheduler infrastructure that pins data, weights, LoRA placement, seeds, compute budgets, timing, calibration, and success/force definitions across all methods.
3. Integrate learned proposals with a separately testable calibration/freshness/constraint/fallback interface that cannot be bypassed by model confidence or missing telemetry.

### Author Challenges

1. Release code, data schema, checkpoints, evaluation scripts, calibration records, and complete timing traces sufficient to reproduce every paper table and chart.
2. Resolve the 200 Hz-to-30 Hz ambiguity by reporting native-rate and downsampled ablations, exact inference sampling, sensor-to-action latency, and matched-compute static controls.
3. Expand physical evaluation with repeated seeds/trials, uncertainty intervals, new platforms/objects, force impulse/duration and safety events, sensor faults, calibration drift, and recovery behavior.

## Validation Notes

- Complete-source integrity passed before review; metadata-only HTML was never counted as the paper.
- The valid PDF was preserved during one bounded repair; official full-paper HTML, metadata HTML, and source package completed the local companion bundle.
- All 16 PDF pages, HTML sections, TeX equations/tables, appendix, and failure figures were inspected; no experiment was rerun.
- Related synthesis contains exactly three DEP entries with repository-relative paths, public URLs, relevance, and source basis.
- The Synthesis Note contains exactly three potential implementations, deeper relationship observations, conceptual similarities, MVP code mock-ups, developer challenges, and author challenges.
- The three Python mock-ups use only the standard library and were prepared for syntax validation.
- Public-safety review targets private paths, usernames, machine names, local timezone labels, and exact execution timestamps.
- No source file was uploaded; repository scope is generated Markdown only.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.23648
  - Applies to: title, authors, identifier, version, submission date, abstract, DOI, license, and public source links.
- Source URL: https://arxiv.org/pdf/2602.23648
  - Applies to: complete method, diagrams, tables, experiments, results, appendix, and failure cases; inspected locally and withheld.
- Source URL: https://arxiv.org/html/2602.23648
  - Applies to: verified full-paper cross-check; inspected locally and withheld.
- Source URL: https://arxiv.org/e-print/2602.23648
  - Applies to: equations, exact tables, captions, training/data details, and appendix; source archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.2602.23648
  - Applies to: persistent paper identification.
- Source URL: https://creativecommons.org/licenses/by/4.0/
  - Applies to: license identified through the canonical arXiv record.
- Source files: Withheld locally; none were uploaded, staged, copied, or attached.
