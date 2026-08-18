# Report-Mark: HESIM Hybrid Sensors

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Hybrid Event Frame Sensors: Modeling, Calibration, and Simulation* |
| Authors | Yunfan Lu; Nico Messikommer; Xiaogang Xu; Liming Chen; Yuhan Chen; Nikola Zubić; Davide Scaramuzza; Hui Xiong |
| arXiv | [2511.18037v2](https://arxiv.org/abs/2511.18037) |
| arXiv DOI | [10.48550/arXiv.2511.18037](https://doi.org/10.48550/arXiv.2511.18037) |
| Version/date | v1 submitted 2025-11-22; v2 revised 2026-06-23; arXiv page comments identify ECCV 2026 |
| Primary sources | [PDF](https://arxiv.org/pdf/2511.18037), [full-paper HTML](https://arxiv.org/html/2511.18037), and [author project page](https://yunfanlu.github.io/HESIM/) |
| Source state | Complete after one bounded brokered repair; original files withheld locally |
| Source-package state | Unavailable through the permitted redirect policy |
| Review scope | Full-paper noise model, calibration, H-ESIM, tables, downstream tasks, limitations, implementation translation, and three related DEP bridges |

## Concise Research Notes

Hybrid event-frame sensors place APS intensity pixels and EVS event pixels on one chip. The paper's central move is to model both modalities from a shared latent electrical signal while retaining their different sampling behavior: APS integrates intensity over exposure, whereas EVS emits thresholded events from log-intensity differences. The unified model includes photon shot noise, dark-current noise, fixed-pattern noise, and quantization noise; EVS event probabilities are linked to illumination and dark current through a Gaussian Q-function formulation.

The calibration pipeline uses controlled dark captures and static multi-brightness scenes over multiple exposure times. APS calibration estimates dark-current, fixed-pattern, read, shot, and quantization components. EVS calibration uses the APS-derived intensity reference to fit brightness-dependent event-noise parameters. H-ESIM then converts 3,200-fps RGB input through an inverse sRGB-to-RAW pipeline, injects calibrated APS noise, maps intensity to EVS voltage, and samples events from calibrated threshold/noise probabilities.

The source evaluates two industrial hybrid sensors, GEN2 and Eiger. On the paper's one-frame-skipping VFI protocol, H-ESIM fine-tuning raises Eiger HR-INR PSNR from 32.4129 to 35.2425 and lowers LPIPS from 0.1979 to 0.0787; on GEN2, the corresponding PSNR changes from 34.2631 to 35.5198 and LPIPS from 0.0726 to 0.0419. For Eiger deblurring, EFNet fine-tuning changes CLIP-IQA from 0.2208 to 0.4248. These are author-reported results, and the reference limitations matter: rolling-shutter distortion affects VFI references, sharp ground truth is unavailable for deblurring, and extreme illumination, temperature, and bandwidth regimes are not modeled.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Attribution and use |
|---|---|---|
| E1 | Official arXiv metadata and abstract | Establishes title, complete author list, subject, v1/v2 chronology, ECCV 2026 comment, DOI, and public locators. |
| E2 | Verified full-paper PDF and full-paper HTML | Supports the unified model, calibration protocol, H-ESIM architecture, sensor resolutions, experiments, metrics, conclusion, and limitations. |
| E3 | Sections 3–5 and Figures 1–5 | Supports the shared latent signal, APS/EVS equations, Q-function event probabilities, controlled calibration captures, and simulation pipeline. |
| E4 | Sections 6, Tables 1–2, Figures 4–7 | Supports the two-sensor setup, 200-run parameter stability result, VFI metrics, deblurring metrics, and qualitative failure conditions. |
| E5 | Author-controlled HESIM project page | Cross-checks the public method overview, calibration narrative, H-ESIM inputs/outputs, downstream task framing, and author attribution. |
| E6 | Exactly three related Black Lake DEP manuscripts | Supports concrete bridges to multi-sensor calibration, physically modeled imaging, and task-preserving simulation-to-real transfer; it does not validate the paper's numerical claims. |
| E7 | Live Black Lake and Black-Lake-Data READMEs plus private process records | Supports DEP-E filing, public attribution, source withholding, selection, deduplication, and complete-source gate compliance. |

The source gate was applied before review. The selected local unit initially contained a valid PDF but lacked metadata/full-paper HTML. One approved brokered repair preserved the PDF and produced qualifying companions. The PDF passed the 10 KB, `%PDF-`, and trailing `%%EOF` checks. The full-paper HTML passed the 5 KB, body-character, document-marker, heading-marker, and paper-structure checks. Local README, provenance, machine-readable summary, verification report, and acquisition receipt were updated. No source file, cache, extracted text, rendering, provenance record, verification record, or source package was copied into this repository or attached to Slack.

## Related DEP Entries

Exactly three related entries were selected for concrete conceptual overlap:

1. [DEP-E-20260714-iKalibr Calibration](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md) - targetless continuous-time calibration for heterogeneous sensors; it supplies the strongest bridge for calibration provenance, temporal offsets, uncertainty, and drift gates around H-ESIM.
2. [DEP-E-20260730-Off-Aperture RGBD](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260730-Off-Aperture%20RGBD/off_aperture_rgbd_manuscript.md) - physically modeled computational imaging with learned reconstruction and depth; it connects sensor/optics modeling, calibration artifacts, prototype mismatch, and sim-to-real evaluation.
3. [DEP-E-20260805-RetinaGAN Transfer](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260805-RetinaGAN%20Sim-to-Real/retinagan_sim_to_real_manuscript.md) - task-preserving simulation-to-real transfer with downstream physical trials; it provides a complementary warning that image-level or sensor-level invariants must be audited for blind spots before deployment.

## Synthesis Note

### Concept Bridge

H-ESIM makes a useful Black Lake bridge by treating a simulator as a calibrated evidence transformer rather than a generic data augmenter. The source model begins with one latent signal, branches into APS and EVS observation processes, and keeps calibration parameters visible as the bridge from real hardware to synthetic training data. The related DEP pattern is a three-layer chain: iKalibr-like records establish when and how sensors agree, physically modeled imaging records expose optical and reconstruction mismatch, and RetinaGAN-like downstream checks ask whether the translated data preserves task-relevant structure. A public-safe derivative should preserve these layers separately, with calibration manifests, noise-fit diagnostics, simulator versioning, and real-data holdouts attached to every downstream result.

### Potential Implementations

1. **Calibrated hybrid-sensor twin**: Build an offline, authorized sensor-twin service that ingests dark/illuminated calibration summaries, produces synthetic RAW/event pairs from public or synthetic high-speed video, and emits a versioned parameter manifest plus fit diagnostics. Risk controls are local processing, no raw sensor upload, parameter-range validation, and automatic fallback when fit residuals exceed thresholds.
2. **Noise-aware VFI/deblurring training harness**: Use H-ESIM-style outputs to pretrain or fine-tune a downstream model, then compare against generic event simulators under matched data, compute, sensor, and seed conditions. The harness should report both reference-based and no-reference metrics, and stop short of claiming deployment readiness.
3. **Sensor drift and sim-to-real gate**: Periodically compare real sensor noise summaries with simulator-generated summaries by layout, brightness, exposure, event polarity, and spatial position. Route a model to retraining or a conservative baseline when the calibrated distribution is stale or the task's reference quality is unavailable.

### Deeper Relationship Observations

1. **Calibration is a contract boundary**: The paper's shared latent signal is a contract between two modalities, while iKalibr's shared trajectory is a contract across sensor clocks and frames. Both suggest that downstream systems need explicit evidence that the contract remains observable and valid, not just a one-time parameter file.
2. **Simulation fidelity is task-conditional**: H-ESIM's improvements appear after fine-tuning downstream models and are larger for some sensor/task pairs than others. This matches RetinaGAN's lesson that a visual or semantic invariant can preserve one task while missing another; fidelity should therefore be measured at the task boundary.
3. **Noise maps can become governance metadata**: The paper models brightness-, exposure-, position-, and layout-dependent effects. That structure can be carried into a data card or model card so each result states which physical regimes were calibrated, which were extrapolated, and when fallback is required.

### Conceptual Similarities

1. **Physics-informed intermediate state**: H-ESIM's shared electrical signal, iKalibr's continuous-time trajectory, and Off-Aperture RGBD's optical propagation each make an intermediate physical state explicit before learning consumes the data.
2. **Calibration before optimization**: All three primary research patterns treat calibration or system identification as a prerequisite for trustworthy downstream optimization, while RetinaGAN adds a task-preservation check after transformation.
3. **Domain-gap evidence rather than realism alone**: The paper uses real-sensor downstream tests, Off-Aperture RGBD compares physical measurements with modeled PSFs, and RetinaGAN uses physical robot trials. The shared idea is that plausible synthetic output is insufficient without an evaluation target in the real system.

### MVP Implementations with Code Mock-ups

1. **Shared-signal noise sampler** - bounded synthetic example of one latent intensity driving frame noise and event probability. It is not a sensor driver and does not accept private data.

```python
from math import erfc, sqrt
from random import Random

def sample_pair(intensity, shot_scale, event_threshold, rng):
    if not 0.0 <= intensity <= 1.0:
        raise ValueError("intensity must be bounded")
    frame = intensity + rng.gauss(0.0, sqrt(max(intensity * shot_scale, 0.0)))
    q = 0.5 * erfc(event_threshold / max(sqrt(shot_scale), 1e-6) / sqrt(2.0))
    event = 1 if rng.random() < min(max(q, 0.0), 1.0) else 0
    return frame, event

print(sample_pair(0.4, 0.02, 0.1, Random(7)))
```

2. **Calibration fit ledger** - record bounded brightness/noise observations and a simple linear fit for a synthetic smoke test. A real implementation would need the paper's per-pixel, exposure, dark-current, and fixed-pattern terms.

```python
from statistics import mean

def fit_noise_curve(brightness, variance):
    if len(brightness) != len(variance) or len(brightness) < 2:
        raise ValueError("paired observations required")
    if any(x < 0 or y < 0 for x, y in zip(brightness, variance)):
        raise ValueError("nonnegative observations required")
    xbar, ybar = mean(brightness), mean(variance)
    denom = sum((x - xbar) ** 2 for x in brightness)
    slope = sum((x - xbar) * (y - ybar) for x, y in zip(brightness, variance)) / denom
    intercept = ybar - slope * xbar
    return {"slope": slope, "intercept": intercept}

print(fit_noise_curve([0.1, 0.4, 0.8], [0.02, 0.06, 0.12]))
```

3. **Distribution drift gate** - compare compact synthetic summaries and require fallback when the calibrated regime no longer matches. This is an audit primitive, not a deployment decision by itself.

```python
def drift_gate(reference, observed, max_relative_error=0.2):
    if set(reference) != set(observed):
        return {"status": "fallback", "reason": "summary keys differ"}
    errors = {}
    for key in reference:
        base = max(abs(reference[key]), 1e-6)
        errors[key] = abs(observed[key] - reference[key]) / base
    worst = max(errors.values(), default=0.0)
    return {
        "status": "pass" if worst <= max_relative_error else "fallback",
        "worst_relative_error": worst,
        "errors": errors,
    }

print(drift_gate({"mean": 0.10, "variance": 0.03},
                 {"mean": 0.11, "variance": 0.035}))
```

### Developer Challenges

1. **Faithful sensor modeling**: Implement shared-signal, APS, EVS, layout, polarity, exposure, and fixed-pattern behavior without silently collapsing the model to generic Gaussian noise.
2. **Evaluation discipline**: Reproduce tables with matched sensor splits, seeds, compute, references, and no-reference caveats while separating calibration fit from downstream task gains.
3. **Operational provenance**: Version calibration captures, parameter manifests, simulator code, input video, sensor layout, and fallback decisions so a synthetic result can be traced back to a physical regime.

### Author Challenges

1. **Independent reproducibility**: Release the full implementation, calibration data schema, parameter files, deterministic scripts, and expected outputs needed to test the paper's claimed open/reproducible implementation.
2. **Boundary expansion**: Evaluate low illumination, temperature variation, bandwidth limits, additional layouts, and cross-device transfer where the Gaussian assumptions may break.
3. **Ground-truth strengthening**: Add distortion-free temporal references, sharp deblurring targets, repeated seeds, confidence intervals, and matched comparisons to establish how much improvement is caused by H-ESIM rather than data or model changes.

## Validation Notes

- Manuscript contract: YAML front matter present; YAML `title` and H1 match and are under 40 characters; all required schema headings are present; `## Evidence Ledger` is included; `## Three Ways to Exercise This Research` contains exactly three entries; MVP fields are complete.
- Source review: PDF and full-paper HTML were both available and passed the integrity gate before synthesis; `/abs/` metadata was not used as a paper substitute.
- Evidence review: public arXiv HTML and the author project page were inspected; source-reported metrics are labeled as such; no standalone official code repository was located in this run.
- Exact-count contract: the Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- Safety review: no local absolute path, home directory, username, Windows drive path, machine name, timezone label, exact execution timestamp, source file, cache, extracted text, local provenance path, or private repository context appears in this public artifact.
- Submission allowlist: only generated `.logs`, `.reports`, `.lake-data` Markdown/README artifacts, and the required DEP-E publication-index row are intended for staging; no `.source/` directory is created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2511.18037
  - Applies to: this Report-Mark and the deposited manuscript.
  - Notes: Official metadata, abstract, authors, version history, comments, and identifiers.
- Source URL: https://arxiv.org/pdf/2511.18037
  - Applies to: method, equations, calibration protocol, tables, figures, experiments, and conclusion.
  - Notes: Primary paper reviewed from a verified private copy; the PDF is withheld.
- Source URL: https://arxiv.org/html/2511.18037
  - Applies to: full-paper structural cross-check and public paper text.
  - Notes: Full-paper HTML route; the local HTML is withheld.
- Source URL: https://doi.org/10.48550/arXiv.2511.18037
  - Applies to: persistent arXiv identity.
  - Notes: arXiv DOI.
- Source URL: https://yunfanlu.github.io/HESIM/
  - Applies to: author-controlled project context and public method overview.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: related-entry bridge on multi-sensor calibration and temporal/spatial validity.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260730-Off-Aperture%20RGBD/off_aperture_rgbd_manuscript.md
  - Applies to: related-entry bridge on physical imaging models and calibration-to-reconstruction transfer.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260805-RetinaGAN%20Sim-to-Real/retinagan_sim_to_real_manuscript.md
  - Applies to: related-entry bridge on task-preserving sim-to-real transfer and physical evidence.
- Source files: withheld locally; no original PDF, HTML, metadata page, source package, cache, extracted text, rendering, provenance record, or verification report is redistributed.
  - Applies to: this Report-Mark and the deposited manuscript.
