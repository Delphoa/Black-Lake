# Report-Mark: Off-Aperture RGBD

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Learned Off-aperture Encoding for Wide Field-of-view RGBD Imaging* |
| Authors | Haoyu Wei; Xin Liu; Yuhui Liu; Qiang Fu; Wolfgang Heidrich; Edmund Y. Lam; Yifan Peng |
| Identifier | arXiv:2507.22523; DOI:10.48550/arXiv.2507.22523 |
| Submitted | 2025-07-30 |
| Primary public records | https://arxiv.org/abs/2507.22523 and https://arxiv.org/html/2507.22523 |
| Source status | Complete: a valid PDF plus verified full-paper HTML were inspected. Metadata HTML is provenance only. |
| Source locality | PDF, HTML, metadata, repair receipts, and any source-package status records remain local and were not uploaded. |

## Research Notes

The paper treats the position of a diffractive optical element (DOE) as a design variable rather than fixing it at the aperture. Its proposed placement between the aperture and sensor aims to balance local wavefront control against the ability to redirect light, which matters for off-axis aberrations in wide-field-of-view (FoV) cameras.

The system combines differentiable ray tracing for refractive components with least-sampling angular spectrum propagation for diffraction. A shared ResNet-18 encoder feeds separate upsampling decoders for color and depth; the authors use image, depth, point-spread-function (PSF), and dynamically weighted multi-task losses. The simple-lens application targets about 45-degree FoV, while a Cooke-triplet RGBD prototype targets about 28-degree FoV.

The paper reports over 5 dB PSNR improvement for off-axis aberration correction in its simple-lens setting. In the compound RGBD comparison, the reported off-aperture multi-head row is 32.09 dB / 0.033 MAE on Sceneflow, 28.28 / 0.019 on Dualpixel, and 31.42 / 0.027 on Instereo2K; these are author-reported results, not a reproduction. Physical prototypes support feasibility but the paper also reports haze, halo artifacts, GPU-memory limits, separate refractive/DOE optimization, and imperfect semantic depth as constraints.

## Evidence and Attribution

| Evidence | Basis | Use | Qualification |
|---|---|---|---|
| E1 | arXiv metadata | Identity, authors, date, abstract, DOI, and stated publication intent | Metadata does not substantiate method or results. |
| E2 | Verified full PDF and full-paper HTML | Sections 1–8, Table I, figures, and limitations | Supports source reporting only; no experiment was rerun. |
| E3 | arXiv full-paper HTML | Hybrid propagation, multi-head decoder, datasets, experiments, and conclusion | Math rendering omits some symbols in browser text; claims were limited to readable prose/table values. |
| E4 | Related DEP manuscripts | Conceptual links to RGBD correspondence, depth robustness, and calibration | Related records do not independently validate this paper. |

Primary citations: [arXiv abstract](https://arxiv.org/abs/2507.22523), [arXiv full paper](https://arxiv.org/html/2507.22523), and [arXiv PDF](https://arxiv.org/pdf/2507.22523).

## Related DEP Entries

| Entry | Path | Relevance reason | Source basis |
|---|---|---|---|
| Pixel-Point Transfer | `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/pixel_point_transfer_manuscript.md` | Both works make RGBD geometry operational: this paper encodes depth optically, while Pixel-Point Transfer uses calibrated pixel-to-point correspondences. | [Repository manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md) |
| Stable Diffusion Depth | `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` | Both address depth recovery limits and the risk that visual appearance or proxy supervision can corrupt geometry conclusions. | [Repository manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Stable%20Diffusion%20Depth/stable_diffusion_depth_manuscript.md) |
| iKalibr Calibration | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` | Both depend on trustworthy camera geometry; iKalibr supplies a concrete spatial-temporal calibration and uncertainty perspective for future RGBD evaluations. | [Repository manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md) |

## Synthesis Note

### Concept Bridge

Off-aperture optical encoding changes what information reaches a sensor; downstream depth learning and RGBD fusion determine whether that information becomes reliable spatial evidence. The practical bridge is an evidence chain: calibrated optics and PSFs, validated reconstruction, geometry-aware depth checks, and calibration provenance.

### Potential Implementations

1. A PSF-position sweep harness that records FoV, PSF concentration, reconstruction quality, and mechanical tolerance for a synthetic optical layout.
2. A RGBD geometry evidence card that compares optically estimated depth against authorized active-depth references and flags halo-heavy regions.
3. A calibration-aware reconstruction evaluator that propagates bounded camera pose and timing perturbations through depth and downstream 3D metrics.

### Deeper Relationship Observations

1. DOE placement is analogous to a representation bottleneck: it governs which angle-dependent detail is preserved before learned decoding begins.
2. Optical and learned priors can fail together when calibration, fabrication, or training data inject correlated geometric error.
3. A sharp color reconstruction is not proof of metrically trustworthy depth, so image metrics and geometry metrics must remain separate.

### Conceptual Similarities

1. All three related DEP entries require explicit correspondence or coordinate-system assumptions.
2. Each benefits from a staged validation path rather than a single aggregate quality score.
3. Each exposes a boundary between source-reported performance and deployment readiness.

### MVP Implementations With Code Mock-ups

1. **Position sweep ledger**

```python
def rank_positions(rows):
    valid = [r for r in rows if r["psnr_db"] >= r["minimum_psnr_db"]]
    return sorted(valid, key=lambda r: (-r["psnr_db"], r["mounting_risk"]))
```

2. **Geometry acceptance gate**

```python
def accept_depth(sample, max_mae, max_halo_rate):
    return sample["mae"] <= max_mae and sample["halo_rate"] <= max_halo_rate
```

3. **Calibration perturbation check**

```python
def within_pose_budget(rotation_deg, translation_mm, limits):
    return rotation_deg <= limits["rotation_deg"] and translation_mm <= limits["translation_mm"]
```

### Developer Challenges

1. Reproducing ray-wave propagation requires careful unit conventions, sampling control, and validated optics libraries.
2. Benchmarking needs paired image/depth evidence, camera calibration, and a clear split between simulated and physical PSFs.
3. Hardware-in-the-loop work must make fabrication, illumination, and mechanical changes observable rather than treating them as noise.

### Author Challenges

1. Report repeated-run uncertainty and full denominator details for simulation and physical comparisons.
2. Release a reproducible configuration surface or explicitly document its absence.
3. Quantify geometry accuracy with active-depth reference data, including adverse illumination and artifact cases.

## Validation Notes

- The selected unit was initially partial: its existing PDF was valid but full-paper HTML was absent.
- A bounded brokered repair preserved the valid PDF and added metadata plus full-paper HTML. Final checks recorded a 44,284,252-byte PDF with `%PDF-` header and `%%EOF`, and a 209,952-byte HTML document with 77,538 body characters, three document markers, 61 heading markers, and six paper-structure terms.
- The source package was unavailable through the redirect policy, but PDF and full-paper HTML passed the mandatory gate. No `.source/` directory was created and no source file was staged or uploaded.
- Dedup checked the arXiv ID, DOI, title, and slug across Black-Lake, Black-Lake-Data, and automation history. The only Black-Lake-Data hit was a metadata-only inventory entry; no prior processed artifact or 24-hour marker matched.

## Attribution Block

- Source URL: https://arxiv.org/abs/2507.22523
  - Applies to: this Report-Mark and the DEP manuscript.
  - Notes: Canonical metadata, author list, submission date, and arXiv DOI.
- Source URL: https://arxiv.org/html/2507.22523
  - Applies to: this Report-Mark and the DEP manuscript.
  - Notes: Full-paper method, experiment, result, and limitation evidence.
- Source URL: https://arxiv.org/pdf/2507.22523
  - Applies to: this Report-Mark and the DEP manuscript.
  - Notes: Full PDF was inspected locally and withheld from the repository.
- Source files: withheld locally
  - Applies to: all public artifacts in this deposit.
  - Notes: No PDF, HTML, metadata, source archive, cache, extracted text, or repair record was uploaded.
