# Report-Mark: Hallo4 Portrait Motion

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization* |
| Authors | Jiahao Cui; Yan Chen; Mingwang Xu; Hanlin Shang; Yuxuan Chen; Yun Zhan; Zilong Dong; Yao Yao; Jingdong Wang; Siyu Zhu |
| Stable identity | arXiv:2505.23525v4; DOI:10.48550/arXiv.2505.23525 |
| First submission / reviewed revision | 2025-05-29 / 2025-11-30 |
| Subject | Computer Vision and Pattern Recognition |
| Primary records | https://arxiv.org/abs/2505.23525; https://arxiv.org/html/2505.23525; https://arxiv.org/pdf/2505.23525; https://arxiv.org/e-print/2505.23525 |
| Official implementation | https://github.com/fudan-generative-vision/hallo4 at `d8274e5e809ea1cd94279063b2a835b23832e466` |
| Venue evidence | The official repository labels the work SIGGRAPH Asia 2025; no paper-specific publisher record or publisher DOI was established. |
| Source policy | Complete local sources were inspected and withheld; public artifact contains URLs and derived analysis only. |

The canonical paper and TeX source name Yan Chen. The official repository README names Baoyou Chen in the corresponding author position. The discrepancy is unresolved and is recorded as a provenance issue rather than normalized by inference.

## Selection, Dedup, Integrity, and Cache

- Candidate enumeration used `rg --files -g "*.pdf"`: 75,779 PDFs collapsed to 75,776 unique parent-paper units.
- PowerShell `Get-Random` uniformly selected zero-based index 11,355.
- First draw accepted; duplicate exclusions 0; reselections 0.
- ID, DOI, normalized title, slug, artifact paths, memory, relevant Black-Lake-Data entries, and active-worktree markers were checked. Two author-inventory rows were metadata only; no research deposit or preceding-24-hour marker existed.
- Initial source state was partial: the 10,418,972-byte PDF passed header/EOF checks, but full-paper HTML was absent.
- Bounded repair added official full-paper HTML, metadata HTML, and a valid 19-entry source archive. Final HTML passed at 151,929 bytes, 46,119 body characters, 39 headings/sections, seven structure terms, and a document marker. Zero partials remained.
- Cache lookup was a miss. Local `missing-only` extraction ended `cached`: `pypdf` 53,699 bytes, `html-regex` 46,819 bytes, and `tarfile` 193,139 bytes. `pypdf` was the successful fallback because `pdftotext` was unavailable.

## Concise Research Notes

### Problem and Method

Hallo4 addresses two failure modes in audio- and skeleton-driven portrait animation. First, conventional objectives do not directly capture human preferences for lip/body synchronization and natural expression. Second, DiT video latents compress time by roughly 4x, and direct motion-signal downsampling can erase fast articulation or gestures.

The preference dataset generates five candidate videos per audio clip using GAN, UNet-diffusion, and DiT-diffusion systems. Annotators score motion-video alignment and portrait fidelity on five-point scales. The highest and lowest composite scores form a best-vs-worst DPO pair, while low-margin cases are excluded. The reported dataset has 220,000 source videos/220 hours and 20,000 curated pairs.

Temporal motion modulation groups four audio or skeleton time steps and redistributes them into a proportionally 4x wider channel representation before projection and cross-attention. The UNet experiment extends Hallo with DPO. The DiT system uses Wan2.1, phased audio/skeleton cross-attention training, flow matching, and final DPO.

### Evidence and Results

| Evidence | Reported result | Reviewer note |
|---|---|---|
| HDTF, Ours DiT | Sync-C 9.161; Sync-D 6.987; E-FID 7.645 | Best displayed model values. Real video Sync-D is lower/better at 6.359, contradicting prose that both synchronization values surpass real video. |
| Celeb-V, Ours DiT | Sync-C 5.689; E-FID 18.998 | Best displayed alignment/expression values, but FID 58.815 and FVD 538.396 are not best. |
| EMTD, Ours DiT | Sync-C 6.764; HKV 35.736; HKC 0.886; PSNR 22.221; SSIM 0.808 | Leads these metrics; EchoMimic-v2 has better FID/FVD 38.461/301.347 versus 44.422/381.752. |
| Temporal audio ablation | Sync-C 2.769 -> 4.244 -> 5.689 for no, partial, and full expansion | Supports the selected reshape within the tested configuration. |
| Temporal skeleton ablation | HKV 31.096 -> 33.567 -> 35.736; HKC 0.850 -> 0.873 -> 0.886 | Supports motion-diversity/articulation gains; does not prove lossless information preservation. |
| DPO versus SFT | DPO Sync-C/E-FID 5.689/18.998; SFT 5.387/21.432; baseline 5.326/21.065 | DPO leads. The paper incorrectly describes SFT E-FID 21.432 as an improvement over 21.065 despite lower being better. |
| User study | 200 generated samples; Hallo4 scores 4.60/4.48/4.43/4.23 | Participant count, assignments, randomization, agreement, uncertainty, and tests are absent. |

The metric vector matters. Motion-plus-fidelity preference improves Sync-C, Sync-D, and E-FID relative to motion-only preference while worsening FID/FVD. Best-vs-worst pairs lead selected alignment metrics, but another pair strategy has lower FVD. Hallo4 therefore demonstrates targeted improvements rather than uniform quality dominance.

### Implementation and Reproducibility Boundary

The paper reports eight A100 GPUs, 10,000 temporal-module iterations at `1e-5`, 12,000 DPO iterations at `1e-8`, 2,000/2,500 warm-up steps, beta 2500, and batch size 8. It omits training time, energy, peak memory, repeated seeds, uncertainty, and a complete configuration manifest.

The official repository exposes inference source, an inference shell command, requirements, and model-download/layout instructions. It also documents Ubuntu/CUDA/H100 expectations and English-only audio. Reproduction remains unverified because:

- one requirement points to an absolute machine-local `flash_attn` wheel;
- README documents `model_weight.pth`, while the inference launcher requests `model_weight.ckpt`;
- no root repository license was visible, although the README says WAN license terms govern the derivative model;
- visible root material does not establish training, preference-data construction, benchmark recreation, or user-study pipelines;
- the paper/repository author-name mismatch is unresolved.

### Limitations and Safety

The authors disclose precise audio-visual alignment dependence, additional compute from channel expansion, and upper-body-only scope. Further reviewer limitations are missing data provenance/consent detail, missing annotation protocol, point-estimate evaluation, English-only released inference, and no long-duration or subgroup analysis.

Portrait animation can facilitate impersonation, non-consensual sexual or deceptive media, harassment, fraud, and biometric privacy harm. Safe implementation needs affirmative consent, provenance, revocation, retention limits, watermarking/content credentials, blocked high-risk identities, abuse reporting, and human approval before export. These controls are product requirements, not consequences of better synchronization metrics.

## Evidence and Attribution Notes

- Technical claims derive from the complete PDF, official HTML, TeX/source archive, and official repository.
- Numerical values were cross-checked against Tables 1-9 and selected rendered PDF pages.
- Still-image visual review verified table layout and qualitative figure contents, but cannot prove temporal coherence.
- The official repository is supporting evidence for public implementation state, not proof of reproducibility or safety.
- Related DEP entries supply conceptual bridges only and do not validate Hallo4's experiments.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
   - Relevance: both use preference optimization to shape generative behavior and depend on how preferred/dispreferred evidence is constructed.
   - Source basis: inspected OViP manuscript sections on online negatives, judges, synthetic data, efficiency, and behavior-preservation tradeoffs.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
   - Relevance: both reshape auxiliary information into a video diffusion latent process and require structural/temporal metrics beyond appearance.
   - Source basis: inspected VideoWeave manuscript sections on geometry adapters, joint latent denoising, distillation, multi-metric evaluation, and dataset constraints.
3. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md`
   - Relevance: both optimize controllable motion video and expose conflicts among control, appearance, temporal stability, latency, and safety.
   - Source basis: inspected AR-Drag manuscript sections on Self-Rollout, GRPO, motion rewards, point-estimate limitations, interactive state, and synthetic-media governance.

## Synthesis Note

### Concept Bridge

Together, Hallo4, OViP, VideoWeave, and AR-Drag show a common systems pattern: a generative model becomes more useful when it receives an auxiliary signal that is closer to the desired behavior than generic reconstruction loss. Hallo4 uses human rankings and high-rate motion; OViP uses model-specific failure-driven preferences; VideoWeave uses implicit geometry latents; AR-Drag uses trajectory rewards and inference-aligned history. The shared risk is proxy capture. Better scores can reflect the annotation scheme, geometry encoder, tracker, or benchmark rather than broad human utility. The practical bridge is an evidence-gated optimization loop: define the proxy, preserve its provenance, test independent metrics, measure regressions, and block release when safety or reproducibility evidence is missing.

### Potential Implementations (Exactly 3)

1. **Preference-and-proxy registry** - record who or what produced each preference/reward, what alternatives were sampled, which groups were represented, and which metrics regressed after optimization.
2. **Temporal conditioning laboratory** - compare subsampling, temporal-to-channel reshaping, latent geometry, and finite-history motion control on known synthetic signals with shared frequency, phase, and stability metrics.
3. **Consent-aware media release gate** - require identity/voice consent, provenance, watermarking, license clarity, reproducible environment metadata, and independent quality/safety review before portrait-animation export.

### Deeper Relationship Observations (Exactly 3)

1. Preference data and motion features are both bottlenecks: once candidate diversity or temporal detail is discarded, downstream optimization cannot recover evidence that never reached the model.
2. Each related system improves one proxy while creating a new dependency: OViP depends on judge/diffusion services, VideoWeave on geometry features, AR-Drag on tracker/reward state, and Hallo4 on annotator/composite-score design.
3. Metric conflicts are not noise but architectural evidence: Hallo4's synchronization/FID tradeoff, VideoWeave's appearance/geometry split, and AR-Drag's latency/teacher-quality tradeoff all favor Pareto reporting over single-rank claims.

### Conceptual Similarities (Exactly 3)

1. All four systems post-train a powerful pretrained generative backbone rather than learning the entire capability from scratch.
2. All introduce an auxiliary representation or preference channel intended to preserve behavior that the base objective underweights.
3. All require an independent validation layer because the optimized signal can be biased, incomplete, or coupled to the evaluation metric.

### MVP Implementations with Code Mock-Ups (Exactly 3)

#### 1. Metric-Direction Claim Checker

```python
DIRECTION = {"sync_c": "max", "sync_d": "min", "e_fid": "min", "fid": "min", "fvd": "min"}

def compare(candidate, reference):
    return {
        key: (candidate[key] >= reference[key] if mode == "max" else candidate[key] <= reference[key])
        for key, mode in DIRECTION.items()
    }

real = {"sync_c": 8.976, "sync_d": 6.359, "e_fid": 0.0, "fid": 0.0, "fvd": 0.0}
hallo4 = {"sync_c": 9.161, "sync_d": 6.987, "e_fid": 7.645, "fid": 0.0, "fvd": 0.0}
print(compare(hallo4, real)["sync_c"], compare(hallo4, real)["sync_d"])
```

Purpose: catch prose that reverses lower-is-better metrics. Boundary: values must come from comparable evaluation sets; the mock-up does not establish statistical significance.

#### 2. Synthetic Temporal-to-Channel Probe

```python
def pack_four(frames):
    if len(frames) % 4:
        raise ValueError("frame count must be divisible by four")
    return [sum((list(frame) for frame in frames[i:i + 4]), []) for i in range(0, len(frames), 4)]

def unpack_four(packed, width):
    return [chunk[i:i + width] for chunk in packed for i in range(0, len(chunk), width)]

toy = [[0.0], [1.0], [0.0], [-1.0]] * 2
assert unpack_four(pack_four(toy), 1) == toy
```

Purpose: test the indexing invariant before learning/projection. Boundary: exact packing does not prove a trained network preserves semantics; frequency sweeps and downstream probes remain necessary.

#### 3. Consent and Provenance Gate

```python
REQUIRED = {"subject_consent", "voice_consent", "purpose", "expires_on", "source_license", "watermark"}

def release_allowed(record):
    missing = sorted(REQUIRED - set(record))
    if missing:
        return False, {"missing": missing}
    if record["purpose"] not in {"research", "authorized_preview"}:
        return False, {"reason": "purpose not allowlisted"}
    return True, {"reason": "human review still required"}

ok, evidence = release_allowed({"subject_consent": True})
assert not ok and "missing" in evidence
```

Purpose: fail closed when consent/provenance evidence is incomplete. Boundary: a boolean record cannot replace identity verification, revocation handling, legal review, access control, or abuse response.

### Developer Challenges (Exactly 3)

1. Build a portable, licensed environment from a repository containing a machine-local wheel reference and inconsistent checkpoint names without silently substituting unverified dependencies.
2. Reproduce temporal and human-preference gains while separating DPO, candidate-method diversity, temporal reshaping, backbone, and dataset effects under multiple seeds.
3. Implement consent, provenance, watermarking, audit, revocation, and retention controls without retaining unnecessary biometric media or exposing a high-risk public generation endpoint.

### Author Challenges (Exactly 3)

1. Publish complete preference/user-study protocols: annotator and participant counts, assignments, demographics, training, agreement, randomization, blinding, exclusions, compensation, uncertainty, and significance tests.
2. Reconcile every provenance and reproduction inconsistency: Yan/Baoyou Chen, `.pth`/`.ckpt`, code/model/data licenses, dependency source, training/evaluation scripts, and expected outputs.
3. Reframe aggregate superiority claims around a Pareto analysis that explicitly reports FID/FVD regressions, real-video Sync-D counterevidence, multilingual/full-body boundaries, and safety subgroup tests.

## Validation Notes

- Complete-source gate passed before synthesis; abstract-only evidence was not used as the paper.
- Required random selection, dedup, cache, and reselection methods are recorded.
- Exactly three related DEP entries were inspected and cited.
- Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVPs with code mock-ups, three developer challenges, and three author challenges.
- All code examples use synthetic metadata/signals and are non-operational for portrait generation.
- No local absolute path, username, machine name, timezone label, exact execution timestamp, source file, cache, or extracted text is included.
- No `.source/` directory was created and no source file was uploaded.

## Attribution Block

- Source URL: https://arxiv.org/abs/2505.23525
  - Applies to: source identity, authors, dates, version, abstract, and public artifact links.
  - Notes: Canonical metadata; abstract alone was not used for synthesis.
- Source URL: https://arxiv.org/html/2505.23525
  - Applies to: method, experiments, results, user study, limitations, and references.
  - Notes: Official full-paper HTML inspected after integrity repair.
- Source URL: https://arxiv.org/pdf/2505.23525
  - Applies to: full-paper and selected visual table/figure review.
  - Notes: Local PDF was verified and withheld; no PDF was uploaded.
- Source URL: https://arxiv.org/e-print/2505.23525
  - Applies to: formulas, tables, captions, author block, and cross-format verification.
  - Notes: Valid local source archive was inspected and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2505.23525
  - Applies to: persistent source identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/fudan-generative-vision/hallo4
  - Applies to: implementation availability, dependency/weight instructions, safety note, and reproducibility boundary.
  - Notes: Inspected at commit `d8274e5e809ea1cd94279063b2a835b23832e466`; code and weights were not executed or downloaded.
