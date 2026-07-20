# Report-Mark: AR-Drag Motion Control

## Source Metadata

- `Title`: *Real-Time Motion-Controllable Autoregressive Video Diffusion*.
- `Authors`: Kesen Zhao; Jiaxin Shi; Beier Zhu; Junbao Zhou; Xiaolong Shen; Yuan Zhou; Qianru Sun; Hanwang Zhang.
- `arXiv`: `2510.08131v3`; submitted 2025-10-09; revised 2026-03-08.
- `DOI`: https://doi.org/10.48550/arXiv.2510.08131.
- `Subject`: Computer Vision and Pattern Recognition (`cs.CV`).
- `Venue`: ICLR 2026 Poster, https://iclr.cc/virtual/2026/poster/10011557.
- `OpenReview`: https://openreview.net/forum?id=4Q55RwYte9.
- `Project page`: https://kesenzhao.github.io/AR-Drag.github.io/.
- `Primary sources`: https://arxiv.org/abs/2510.08131, https://arxiv.org/pdf/2510.08131, https://arxiv.org/html/2510.08131, and https://arxiv.org/e-print/2510.08131.
- `License visibility`: the arXiv page links a CC BY-NC-ND 4.0 license; no source redistribution was performed.
- `Access date`: 2026-07-20.
- `Source state`: verified complete after bounded repair; the preserved PDF, official full-paper HTML, metadata HTML, TeX/source package, extracted text, and selected page renders remain local.
- `Public-source policy`: only generated Markdown and public locators are deposited; no source document or `.source/` directory is public.
- `Code/data status`: the paper says code, configuration, and reproduction instructions are in supplementary materials. The official project page was inspected, but no official public implementation repository or downloadable benchmark corpus was established; no experiment was run.

## Concise Research Notes

### Research Question

Can a compact few-step autoregressive image-to-video diffusion model accept frame-level trajectory updates with sub-second first-frame latency while preserving visual fidelity and motion alignment well enough to outperform slower bidirectional and chunk-wise baselines?

### Method

AR-Drag uses two training stages. First, a Wan2.1-1.3B-I2V model is fine-tuned on motion-conditioned real and synthetic videos, then distilled from a bidirectional teacher into a three-step frame-wise causal student. Self-Rollout denoises each training frame through the full remaining trajectory and updates a seven-frame KV cache with model-generated clean history, aligning training context with autoregressive inference.

Second, the paper formulates frame-by-frame denoising as an MDP and applies GRPO. One randomly selected denoising step uses an ODE-to-SDE update to supply exploration while other steps remain deterministic. The reward combines a LAION aesthetic predictor with a Co-Tracker-based trajectory-alignment term. Group-relative standardized advantages and a clipped policy-ratio objective optimize the model.

### Data and Evaluation

The authors report approximately 10,000 real and Wan2.1-14B-generated training videos, with automatically detected trajectories and manual filtering. A difficult subset of about 3,000 videos is fully human-annotated. The main benchmark contains 206 curated clips covering trajectory and scene variation. The model trains with AdamW at learning rate `1e-5` on eight NVIDIA H20 GPUs; first-frame latency is measured on one H20.

Evaluation uses FID, FVD, a 1-5 aesthetic score, Motion Smoothness, and a Motion Consistency score computed with the proposed tracking-based reward model. Baselines are DragNUWA, DragAnything, Tora, MagicMotion, and an adapted Self-Forcing model trained on the same data.

### Evidence and Results

- Table 1 reports AR-Drag at 0.44-second first-frame latency, FID 28.98, FVD 187.49, aesthetic quality 4.07, motion smoothness 0.9948, and motion consistency 4.37. It is the strongest displayed method in all six columns.
- Self-Forcing reports 0.95 seconds, FID 34.47, FVD 315.87, aesthetic 3.70, smoothness 0.9920, and consistency 4.06. The slowest baseline, MagicMotion, reports 1,426.37 seconds with a 5B model.
- The teacher model reports stronger FVD at 151.46 and aesthetic score 4.15, but 45.64-second latency. AR-Drag is therefore not uniformly superior to its teacher on every quality metric.
- Removing RL leaves latency unchanged but worsens FID from 28.98 to 31.65, FVD from 187.49 to 210.35, aesthetic from 4.07 to 3.92, and motion consistency from 4.37 to 4.12.
- Removing Self-Rollout leaves latency at 0.44 seconds but worsens FID to 38.13 and FVD to 353.75. The accompanying frames show visible artifacts, supporting a train-inference mismatch concern.
- A chunk-size-three variant improves FID to 27.47 and FVD to 179.23 but increases latency to 0.94 seconds. KV cache sizes 15 and 25 produce small reported metric changes relative to the seven-frame default.

All metrics above are author-reported point estimates. No confidence intervals, multi-seed aggregates, independent benchmark run, kernel profile, or user study was reproduced for this report.

### Reviewer Assessment

The paper's most transferable idea is not merely “use RL.” It is to restore the actual sequential transition process before applying an on-policy objective. Self-Rollout makes model-generated history part of training, while selective stochasticity limits how much variance is introduced into a very long frame-by-denoising-step chain. This is a coherent response to exposure bias and policy-gradient cost.

The result is promising but narrower than “real-time controllable video” can suggest. The latency number is first-frame latency on one H20, not end-to-end stream latency across commodity hardware, input preprocessing, trajectory updates, decoding, and display. The benchmark is author-curated and small. Motion Consistency reuses the proposed reward machinery, which raises evaluator dependence. Data provenance, exclusion criteria, consent/licensing, seeds, variance, and full reproduction artifacts are not sufficiently public for an independent audit.

The stated limitation is meaningful: exaggerated or physically impossible trajectories may be ignored because both training data and reward favor physical plausibility. Additional reviewer-identified risks include reward hacking, tracker failure under occlusion, identity drift beyond the tested horizon, bias from synthetic training videos, malicious/deceptive video use, and unsafe assumptions that “de-identified” fully resolves consent or licensing.

### Strengths

- Clear mechanism connecting inference-aligned history, an MDP formulation, and GRPO.
- Strong matched-data Self-Forcing comparison and component ablations.
- Multiple fidelity, temporal, motion, and latency measures rather than one headline score.
- Compact 1.3B backbone, three denoising steps, and explicit H20 training/inference settings.
- Appendix disclosure of data scale, resolutions, loss weights, algorithms, pseudocode, cache sensitivity, limitations, ethics, and reward curves.

### Limitations

- Point estimates without reported seed variance, confidence intervals, or significance testing.
- A 206-clip author-curated benchmark with no established public release in inspected sources.
- Reward/evaluator coupling for Motion Consistency and no independent blinded human-motion study.
- One first-frame hardware profile rather than end-to-end latency, throughput, memory, and energy across devices.
- Incomplete public provenance for the approximately 10,000-video mixture and manually annotated subset.
- No established public repository for full training, evaluation, and artifact reproduction.
- Physical-plausibility bias limits deliberately stylized or non-physical motion control.

## Evidence and Attribution

| Evidence ID | Evidence | Claim Support | Reviewer Handling |
|---|---|---|---|
| E1 | Complete v3 PDF, official full-paper HTML, metadata HTML, and TeX/source package | Method, equations, algorithms, pseudocode, tables, figures, appendix, limitations, ethics, reproducibility | Inspected after integrity gate; decisive pages rendered; no long quotation copied |
| E2 | https://arxiv.org/abs/2510.08131 | Identity, authors, version history, subject, DOI, license, official artifact links | Metadata only; not used alone for empirical claims |
| E3 | https://kesenzhao.github.io/AR-Drag.github.io/ | Official qualitative/project context and streaming-control framing | Author context; qualitative claims remain attributed |
| E4 | https://iclr.cc/virtual/2026/poster/10011557 and https://openreview.net/forum?id=4Q55RwYte9 | ICLR 2026 Poster and forum identity | Official venue context; OpenReview forum content was challenge-gated |
| E5 | Three Black Lake artifacts | Geometry-aware diffusion, bounded autoregressive KV state, and instance-specific context absorption | Related-entry synthesis only; their claims remain attributed |
| E6 | Live Black Lake and Black-Lake-Data READMEs | Layout, source locality, attribution, dedup scope, index maintenance | Repository authority, not research evidence |
| E7 | Local verification record | PDF/HTML/source integrity and zero partials | Public metrics only; paths and source files withheld |

### Random Selection and Dedup Evidence

- Method: `rg --files -g "*.pdf"`, unique PDF-parent units, normalized-ID exclusion, then one uniform PowerShell `Get-Random` draw over eligible units.
- Counts: 75,778 PDFs; 75,776 unique units; 1,007 observed used identifiers; 222 units excluded; 0 identifier-incomplete units; 75,554 eligible units.
- Selected zero-based eligible index: 14,671.
- Selected identity: `2510.08131v3`, *Real-Time Motion-Controllable Autoregressive Video Diffusion*.
- Exact base/versioned ID, DOI, normalized title, and `AR-Drag` slug scans found no prior owning artifact in Black Lake, automation memory, or relevant Black-Lake-Data records.
- Duplicate reselections: zero. Same-paper markers within the preceding 24 hours: zero.

### Source-Integrity Evidence

- Initial classification: `partial`; the 34,931,055-byte PDF passed the size, `%PDF-`, trailing `%%EOF`, and hash checks, while full-paper HTML was absent.
- Bounded repair preserved the PDF and collected 356,542-byte official full-paper HTML, 42,779-byte metadata HTML, and a 32,494,867-byte source package.
- Full-paper HTML contains 88,798 body characters, a document marker, 63 heading/section markers, and eight structure terms. The source archive has 34 readable entries. No partial files remain.
- The local README, attribution/provenance record, machine-readable summary, and verification report were updated before review began.
- Final classification: `complete`. No PDF, HTML, source archive, extracted text, render, cache, or verification file is uploaded.

## Related DEP Entries

Exactly three current repository entries were selected:

| Entry | Concrete Relevance | Source Basis |
|---|---|---|
| [VideoWeave Geometry](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md) | Both methods distill video diffusion into a few-step student and inject training-time structure that should survive at inference. VideoWeave targets geometry latents; AR-Drag targets sequential history and trajectories. | Review of [arXiv:2606.14162](https://arxiv.org/abs/2606.14162) and its official project context |
| [PackForcing Video](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-PackForcing%20Video/2603.25730-whitepaper-review.md) | Both govern autoregressive-video KV history and confront compounding long-horizon errors. PackForcing bounds and compresses history; AR-Drag uses generated history to align training with inference. | Review of [arXiv:2603.25730v1](https://arxiv.org/abs/2603.25730v1) and author-linked code context |
| [ISPA Video Memory](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ISPA%20Video%20Memory/2607.00712-whitepaper-review.md) | Both treat historical video context as a resource-constrained state. ISPA absorbs context into temporary parameters; AR-Drag retains a bounded generated-frame KV cache. | Review of [arXiv:2607.00712v1](https://arxiv.org/abs/2607.00712v1) |

## Synthesis Note

### Concept Bridge

AR-Drag, VideoWeave, PackForcing, and ISPA can be read as four interventions on the same causal chain: training constructs a state representation, autoregressive inference updates that state, resource limits determine how much history survives, and evaluation decides whether the surviving state still supports the intended motion and appearance. AR-Drag's distinctive intervention is before deployment: make generated history part of training and keep the RL exploration budget sparse. The related entries show that geometry, cache partitions, and temporary parameter absorption are complementary controls rather than substitutes.

### Potential Implementations

1. **Interactive trajectory preview service** - Generate a low-resolution, short-horizon preview after each drag update; expose first-frame, inter-frame, decode, and display latency separately; reject or soften physically implausible inputs; log no user images by default.
2. **Rollout-integrity training harness** - Instrument every generated-frame transition, KV-cache update, stochastic step, reward component, and fallback so Self-Rollout and Self-Forcing variants can be compared under matched seeds and data.
3. **Independent motion-control benchmark** - Evaluate released or internal models with held-out trajectories, independent trackers, blinded human raters, occlusion strata, long-stream drift, hardware profiles, and misuse/red-team scenarios.

### Deeper Relationship Observations

1. VideoWeave and AR-Drag both move an inference desideratum into a training-time latent process: geometry consistency for VideoWeave and inference-consistent generated history for AR-Drag. The common hypothesis is that the student can internalize structure that need not remain an expensive explicit inference dependency.
2. PackForcing exposes a tension hidden by AR-Drag's seven-frame cache: generated history improves policy validity, but history growth threatens memory and long-horizon stability. A combined system needs both inference-aligned training and an auditable retention policy.
3. ISPA shows that historical context can move between storage forms. For AR-Drag, this suggests evaluating explicit KV frames, compressed partitions, and temporary parameter absorption on one quality-latency-memory frontier rather than assuming a fixed cache is optimal.

### Conceptual Similarities

1. All four entries treat video generation as stateful sequential computation, not independent frame synthesis.
2. All four use a constrained representation or auxiliary mechanism to preserve an invariant under compute or memory pressure.
3. All four require boundary-focused evaluation because average visual quality can hide geometry drift, identity drift, motion misalignment, or latency regressions.

### MVP Implementations with Code Mock-ups

1. **Latency-quality release gate** - A deterministic policy rejects a candidate configuration unless latency, independent motion error, and quality all pass.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Result:
    first_frame_s: float
    motion_error_px: float
    fid: float

def release_ok(result: Result) -> bool:
    return (
        result.first_frame_s <= 0.50
        and result.motion_error_px <= 8.0
        and result.fid <= 32.0
    )
```

2. **Rollout transition auditor** - The toy audit fails when frame or cache order diverges, making the state-transition contract visible before expensive training.

```python
def audit_rollout(events: list[dict]) -> None:
    expected_frame = 0
    for event in events:
        if event["frame"] != expected_frame:
            raise ValueError("non-sequential frame transition")
        if event["cache_tail"] != event["frame"]:
            raise ValueError("cache not updated from generated frame")
        expected_frame += 1
```

3. **Reward-dependence check** - Compare group-relative advantages from a training reward with an independent evaluator and flag rank disagreement.

```python
def centered(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    return [value - mean for value in values]

def rank_disagreement(train: list[float], audit: list[float]) -> bool:
    train_order = sorted(range(len(train)), key=train.__getitem__)
    audit_order = sorted(range(len(audit)), key=audit.__getitem__)
    return train_order != audit_order
```

### Developer Challenges

1. Reproduce the 0.44-second claim with a timestamped end-to-end trace that separates control encoding, denoising, KV updates, VAE decode, transfer, and display.
2. Implement independent trajectory and perceptual evaluators without leaking training reward assumptions into acceptance tests.
3. Preserve cache isolation, deletion, provenance, and fallback behavior when interactive inputs contain faces, private scenes, copyrighted media, or adversarial trajectories.

### Author Challenges

1. Release version-pinned code, configurations, benchmark clips or legally redistributable equivalents, metric implementations, seeds, and expected outputs.
2. Report repeated runs, uncertainty, failure distributions, independent human evaluation, and reward-hacking tests across trackers and trajectory types.
3. Expand data provenance and consent/licensing disclosure, then test physical, stylized, impossible, occluded, abrupt, and long-horizon controls across multiple hardware classes.

## Validation Notes

- Complete-source gate passed before review; abstract-only evidence was never treated as the paper.
- Tables 1-3, Figures 1, 4, and 6, Algorithms 1-2, appendix data settings, and limitations were checked in rendered PDF pages and reconciled with extracted text/HTML.
- Reported metrics retain their evaluation context and are labeled as author reports; no independent reproduction is implied.
- Exactly three related DEP entries are present, each with a repository path, concrete relevance reason, and primary-source basis.
- The Synthesis Note contains one Concept Bridge, exactly three potential implementations, exactly three deeper relationship observations, exactly three conceptual similarities, exactly three MVP implementations with Python mock-ups, exactly three developer challenges, and exactly three author challenges.
- All three Python mock-ups are intended for syntax validation only; they do not train or execute a generative model.
- Public-safety scan must reject absolute paths, usernames, machine names, timezone labels, exact execution timestamps, local source-file paths, or source-byte content.
- Source documents were withheld locally; no `.source/` directory is created.

## Attribution Block

- Primary paper: https://arxiv.org/abs/2510.08131
- Full-paper HTML: https://arxiv.org/html/2510.08131
- Canonical PDF: https://arxiv.org/pdf/2510.08131
- TeX/source locator: https://arxiv.org/e-print/2510.08131
- arXiv-issued DOI: https://doi.org/10.48550/arXiv.2510.08131
- Official project page: https://kesenzhao.github.io/AR-Drag.github.io/
- ICLR 2026 poster record: https://iclr.cc/virtual/2026/poster/10011557
- OpenReview forum locator: https://openreview.net/forum?id=4Q55RwYte9
- Related DEP source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
- Related paper: https://arxiv.org/abs/2606.14162
- Related DEP source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-PackForcing%20Video/2603.25730-whitepaper-review.md
- Related paper: https://arxiv.org/abs/2603.25730v1
- Related DEP source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ISPA%20Video%20Memory/2607.00712-whitepaper-review.md
- Related paper: https://arxiv.org/abs/2607.00712v1
- Repository authority: https://github.com/Delphoa/Black-Lake/blob/main/README.md
- DEP filing authority: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
- Companion repository authority: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
- Source policy: all PDF, HTML, metadata, TeX/source, extracted content, renders, caches, and local verification records were withheld from Git, GitHub, PRs, and Slack.
