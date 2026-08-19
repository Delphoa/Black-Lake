# Report-Mark: MoCom MAV Visual Comms

## Source Metadata

| Field | Value |
|---|---|
| Paper | *MoCom: Motion-based Inter-MAV Visual Communication Using Event Vision and Spiking Neural Networks* |
| Authors | Nengbo Zhang; Hann Woei Ho; Ye Zhou |
| arXiv | `2510.14770v1`; submitted 2025-10-16; Computer Vision and Pattern Recognition (`cs.CV`) |
| arXiv DOI | `10.48550/arXiv.2510.14770` |
| Published record | *IEEE Transactions on Robotics*, volume 42 (2026), pages 1680-1694 |
| Published DOI | `10.1109/TRO.2026.3677077` |
| Primary sources | https://arxiv.org/abs/2510.14770 ; https://arxiv.org/html/2510.14770 ; https://arxiv.org/pdf/2510.14770 |
| Source integrity | Verified complete PDF and official full-paper HTML; metadata HTML retained as metadata only; source package unavailable under the bounded broker policy |
| Implementation status | The paper links generic SpikeJelly and says data/code will be public upon publication, but this review did not establish a MoCom-specific code or dataset repository |
| Review date | 2026-08-19 |

## Concise Research Notes

MoCom treats deliberate vehicle motion as a communication channel. Four flight patterns encode `start`, `end`, `1`, and `0`; an event camera converts the continuous motion stream into sparse positive/negative events. A statistical segmenter detects motion intervals, EventMAVNet classifies each interval, and the Integrated MAV Segmentation and Recognition algorithm assembles a bounded message carrying direction, heading, and distance.

EventMAVNet is a shallow spiking network over `128 x 128` two-polarity event frames and 16 timesteps. Two convolutional spiking stages feed a compact encoder and a 50-neuron voting layer for five classes, including background. The paper reports 96.51%, 95.37%, and 94.98% mean recognition accuracy at 0.9 m, 1.2 m, and 1.5 m, respectively, plus 1.26 ms per batch of 10 samples on an RTX 4090 averaged over 100 runs.

The evidence is promising but narrow. Dataset cardinality and identity are not stated, the 3:1 split is not tied to subject/session separation, segmentation is tested on three nine-action streams, and the three flight demonstrations use only three predefined 8-bit codes. The segmenter misses one of nine actions at a 2.5-second pause. Table I and the polarity ablation also disagree on short/long accuracies for the apparent full model, without explaining whether the values are means or different runs.

End-to-end communication efficiency is not established by classifier speed. Symbols last roughly three seconds, decoding waits for sufficient temporal context, pause length materially affects segmentation, and deliberate flight consumes time, energy, airspace, and visual observability. The reported `Energy(mJ)` values in ablation tables lack an explicit physical measurement or estimation protocol in the inspected paper, so they should not be read as system-level power evidence.

## Evidence and Attribution

| ID | Evidence | Supports | Reviewer qualification |
|---|---|---|---|
| E1 | arXiv metadata and v1 record | Identity, three-author byline, submission date, abstract, public URLs | Metadata supports identity, not empirical claims. |
| E2 | Complete 13-page PDF and official full-paper HTML | Motion alphabet, segmentation equations, EventMAVNet, IMSR algorithm, experiments, tables, figures, conclusion | Complete primary evidence; experiments were not independently reproduced. |
| E3 | Table I and Figure 6 | Three-distance recognition accuracy and 1.26 ms batch inference on RTX 4090 | Author-reported; no dataset size, confidence protocol, or edge-device end-to-end latency is provided. |
| E4 | Figures 8-11 and segmentation prose | Three streams with nine actions/eight pauses; sensitivity to 2.5, 3.0, and 3.5 second gaps | Small controlled evidence; 2.5-second sequence has one merged/missed action. |
| E5 | Tables II-IV | Resolution, timestep, polarity, operations, parameters, and energy tradeoffs | Useful ablations; energy derivation is not stated and Table I/Table IV full-model accuracies conflict. |
| E6 | Figures 12-13 and Tables V-VI | Three decoded 8-bit codes and target-reaching flight trajectories | Feasibility demonstration only; no repeated trial count, error rate, adverse condition, or autonomous radio-free control path is established. |
| E7 | Crossref and author-controlled institutional record | IEEE journal DOI, volume, year, pages, and published identity | Bibliographic evidence; it does not validate code release or paper claims. |
| E8 | Exactly three inspected Black Lake DEP manuscripts | Event/SNN efficiency, constrained swarm coding, and calibrated event-sensor simulation bridges | Reviewer synthesis; related entries do not independently validate MoCom. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md`
   - Relevance: both systems preserve event sparsity through spiking computation and aggregate temporal evidence before making a structured prediction. The related artifact's distinction between modeled operation energy and physical device energy directly qualifies MoCom's energy claims.
   - Source basis: inspected manuscript source metadata, executive summary, architecture, empirical tables, failure modes, claims, and review constraints.
2. `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md`
   - Relevance: both use a compact control alphabet under a constrained shared channel. The related artifact shows that a code or primitive may simplify command selection while increasing physical execution time, swept volume, and safety burden.
   - Source basis: inspected manuscript source metadata, controllability construction, coding/group allocation, planner/runtime tables, inconsistencies, and deployment boundary.
3. `.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md`
   - Relevance: MoCom depends on event polarity and event-count statistics whose distributions change with illumination, thresholds, layout, and noise. HESIM supplies the calibration/provenance layer needed to test whether a learned motion channel transfers across sensor regimes.
   - Source basis: inspected manuscript source metadata, unified APS/EVS signal model, calibration protocol, sim-to-real results, limitations, and claims map.

## Synthesis Note

### Concept Bridge

MoCom is best understood as a protocol stack rather than a classifier: a sender compiles bits into collision-bounded motion primitives; a calibrated event sensor observes them; a temporal front end segments them; a spiking recognizer estimates symbols; a decoder validates framing and semantics; and a controller decides whether the decoded command is safe to execute. Spiking Pose Tracking strengthens the observation layer, HESIM strengthens sensor-regime fidelity, and Group-Control Swarms exposes the cost of turning compact logical commands into physical trajectories.

### Potential Implementations

1. **Event-motion channel emulator:** generate synthetic motion symbols under calibrated sensor noise, occlusion, distance, lighting, and timing jitter; report symbol error, message completion, latency, and abstention rather than accuracy alone.
2. **Protocol-aware flight compiler:** convert a short command into `start/payload/end` motion primitives subject to geofence, clearance, visibility, acceleration, and energy budgets; reject commands whose safe execution window is unavailable.
3. **Dual-channel fallback monitor:** treat motion communication as a degraded-mode or side channel, compare it with a conventional telemetry path, and require message agreement or human authorization before consequential actuation.

### Deeper Relationship Observations

1. Event sparsity is useful only when the protocol creates observable changes. A sender that minimizes motion energy too aggressively may reduce event density below the segmenter's reliable regime; transmitter planning and receiver calibration are therefore coupled.
2. Compact alphabets move complexity into time and motion. Group-Control Swarms makes the same trade: fewer command distinctions can require longer composite trajectories. MoCom's multi-second symbols and pauses similarly dominate throughput even when neural inference is fast.
3. Sensor-specific event statistics can masquerade as semantic evidence. HESIM implies that threshold, brightness, fixed-pattern noise, and polarity imbalance must travel with every MoCom benchmark manifest, or the classifier may learn a device signature rather than a motion code.

### Conceptual Similarities

1. MoCom and Spiking Pose Tracking both convert sparse asynchronous event streams into temporally integrated structured predictions while relying on reported operation-level efficiency as a proxy for deployment efficiency.
2. MoCom and Group-Control Swarms both use physical motion primitives as an instruction set whose logical compactness does not guarantee short, safe, or energy-efficient execution.
3. MoCom and HESIM both depend on positive/negative event statistics, making sensor regime, calibration, and illumination part of the effective model input even when not represented in the learned label space.

### MVP Implementations with Code Mock-Ups

1. **Motion-code contract checker:** validate a synthetic codebook before simulation.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Symbol:
    name: str
    duration_s: float
    clearance_m: float


def validate_codebook(symbols: list[Symbol]) -> None:
    names = [symbol.name for symbol in symbols]
    required = {"start", "end", "0", "1"}
    if set(names) != required or len(names) != len(set(names)):
        raise ValueError("codebook must contain four unique framing/data symbols")
    if any(symbol.duration_s <= 0 or symbol.clearance_m <= 0 for symbol in symbols):
        raise ValueError("duration and clearance must be positive")


validate_codebook([
    Symbol("start", 3.0, 0.5),
    Symbol("end", 3.0, 0.5),
    Symbol("0", 3.0, 0.5),
    Symbol("1", 3.0, 0.5),
])
```

2. **Pause-robustness gate:** reject timing schedules outside a tested separation envelope.

```python
def timing_gate(intervals: list[tuple[float, float]], min_pause_s: float = 3.0) -> bool:
    ordered = sorted(intervals)
    if any(start >= end for start, end in ordered):
        return False
    pauses = [next_start - end for (_, end), (next_start, _) in zip(ordered, ordered[1:])]
    return all(pause >= min_pause_s for pause in pauses)


synthetic_symbols = [(0.0, 3.0), (6.1, 9.1), (12.2, 15.2)]
assert timing_gate(synthetic_symbols)
assert not timing_gate([(0.0, 3.0), (5.5, 8.5)])
```

3. **Public-safe experiment receipt:** require the evidence fields needed to interpret an accuracy result.

```python
REQUIRED = {
    "dataset_manifest",
    "split_policy",
    "sensor_profile",
    "distance_m",
    "pause_s",
    "seed",
    "symbol_errors",
    "message_trials",
}


def validate_receipt(receipt: dict[str, object]) -> None:
    missing = REQUIRED - receipt.keys()
    if missing:
        raise ValueError(f"missing evidence fields: {sorted(missing)}")
    if int(receipt["message_trials"]) <= 0:
        raise ValueError("message_trials must be positive")


validate_receipt({
    "dataset_manifest": "synthetic-v1",
    "split_policy": "flight-session-disjoint",
    "sensor_profile": "calibrated-profile-a",
    "distance_m": 1.2,
    "pause_s": 3.0,
    "seed": 7,
    "symbol_errors": 1,
    "message_trials": 50,
})
```

### Developer Challenges

1. **Clock and frame semantics:** asynchronous events, 30 fps segmentation windows, vehicle controllers, localization, and message timeouts need one versioned timing model; otherwise apparent symbol boundaries can shift across components.
2. **Safety-aware protocol compilation:** the codebook must produce visually separable motion while respecting acceleration, battery, clearance, geofence, occlusion, and bystander constraints under uncertainty.
3. **Evidence-complete evaluation:** dataset identities, session-disjoint splits, sensor calibration, repeated seeds, trial denominators, symbol/message errors, energy boundaries, and controller interventions must remain traceable through every benchmark run.

### Author Challenges

1. **Resolve empirical ambiguities:** publish dataset cardinalities and identities, split construction, repeated-run protocol, and an explanation for the Table I versus Table IV accuracy mismatch.
2. **Establish end-to-end communication evidence:** measure symbol rate, useful bitrate, complete-message error, recovery/abstention, sender flight energy, sensing/inference energy, and latency under lighting, distance, occlusion, motion, and interference sweeps.
3. **Complete the reproducibility surface:** provide the promised paper-specific code, data, sensor configuration, preprocessing, weights, controller scripts, flight-test repetitions, supplementary video locator, and a versioned license/manifest.

## Validation Notes

- Required PDF enumeration used `rg --files -g "*.pdf"`; 75,967 PDFs collapsed to 75,964 parent units.
- The used-paper index contained 2,871 arXiv base IDs; 903 used-ID units and 185 identifier-incomplete units were withheld before the uniform draw.
- The accepted zero-based eligible index was 71,005 of 74,876. Duplicate rejections and reselections were both zero.
- Exact arXiv ID, arXiv DOI, published DOI, normalized title, and slug checks found no prior same-paper deposit; the public-safe cutoff date was 2026-08-18.
- The source gate passed only after the 7,531,759-byte PDF and 257,858-byte official full-paper HTML independently validated; zero partials remained.
- All 13 PDF pages were rendered and visually inspected. The official HTML supplied searchable methods, equations, tables, figure captions, and references.
- Quantitative results are author-reported. Code, dataset payloads, supplementary video, and experiments were not inspected or executed.
- Original source files and private verification material remain local; no `.source/` directory was created and no source file is authorized for repository or Slack upload.

## Attribution Block

- Source URL: https://arxiv.org/abs/2510.14770
  - Applies to: paper identity, authors, v1 date, abstract, subjects, and source locators.
- Source URL: https://arxiv.org/html/2510.14770
  - Applies to: methods, equations, experiment design, tables, figures, limitations, conclusion, and references.
- Source URL: https://arxiv.org/pdf/2510.14770
  - Applies to: full-paper layout and visual checks across all 13 pages.
- Source URL: https://doi.org/10.48550/arXiv.2510.14770
  - Applies to: persistent arXiv identity.
- Source URL: https://doi.org/10.1109/TRO.2026.3677077
  - Applies to: published IEEE Transactions on Robotics identity.
- Source URL: https://api.crossref.org/works/10.1109/TRO.2026.3677077
  - Applies to: journal title, publisher, year, authors, and published DOI cross-check.
- Source URL: https://aerospace.eng.usm.my/index.php?id=563&option=com_content&view=article
  - Applies to: author-controlled journal volume and page-range listing.
- Source URL: https://github.com/fangwei123456/spikingjelly
  - Applies to: generic framework dependency linked by the paper; not evidence of a MoCom-specific release.
- Source file: `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md`
  - Applies to: spiking event-perception and efficiency relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md`
  - Applies to: compact swarm coding and physical planning/execution relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md`
  - Applies to: event-sensor calibration and sim-to-real relationship.
- Source-handling note: original source documents, metadata, caches, renderings, receipts, and verification records were withheld locally and were not uploaded.
