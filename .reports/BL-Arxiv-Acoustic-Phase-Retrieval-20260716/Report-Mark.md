# Report-Mark: Acoustic Phase Retrieval

Public run date: 2026-07-16

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Retrieval of acoustic sources from multi-frequency phaseless data* |
| Authors | Deyue Zhang; Yukun Guo; Jingzhi Li; Hongyu Liu |
| Stable identifiers | arXiv:1803.11323v1; DOI:10.1088/1361-6420/aaccda |
| Publication context | Submitted to arXiv on 2018-03-30; published in *Inverse Problems* 34(9), article 094001, on 2018-06-29 |
| Subject | Two-dimensional Helmholtz inverse-source reconstruction from multifrequency phaseless near-field data |
| Source state | Verified complete local PDF and full-paper HTML; metadata HTML and TeX/source package also retained locally |
| Distribution | Generated Markdown only; all original and extracted source files withheld locally |

## Concise Research Notes

- **Problem:** Intensity-only measurements lose the complex phase of an acoustic radiated field. Even the sign pair `S` and `-S` produces the same modulus, so the source is not identifiable from the stated phaseless observations without more information.
- **Method:** The acquisition circle is divided into sectors. For every sector and frequency, two known reference point sources are added in separate measurements. Subtracting the original squared magnitude from each reference-augmented squared magnitude yields a two-by-two linear system for the real and imaginary parts of the field. A prescribed source geometry gives positive determinant lower bounds, after which a non-iterative multifrequency Fourier method estimates the source coefficients.
- **Evidence and results:** The paper proves determinant lower bounds of `(1 - 7/(20 tau))/(kR)` for ordinary admissible frequencies and `4/9` for the small auxiliary frequency, then bounds relative phase-recovery error by `epsilon C_epsilon`. Synthetic finite-element experiments report final source-reconstruction relative L2 errors of 4.60%, 5.82%, and 8.39% for 1%, 2%, and 5% multiplicative phaseless noise. At 5% noise, phase-recovery error is much larger at several frequencies, while Fourier integration partly filters that error.
- **Limitations:** Evidence is synthetic, two-dimensional, scalar, single-medium, and tied to a centered support box, circular acquisition curve, frequency-independent source, prescribed point-source locations, and repeated reference measurements. The paper reports no hardware experiment, code release, runtime ledger, repeated-seed uncertainty, reference-source calibration error, background mismatch, or ablation over geometry. The Fourier stage relies on earlier theory rather than rederiving all end-to-end guarantees here.
- **Implementation relevance:** The durable pattern is measurement intervention plus a conditioning certificate: add known probes that transform an unidentifiable modulus-only problem into a small auditable linear solve, gate the solve on determinant/condition margin, and then apply a physics-aligned reconstruction. This is more transferable than the exact acoustic geometry.
- **Reviewer interpretation:** The paper supports feasibility and analytic stability under its model. It does not establish field robustness. The claim that only “a few extra data” are needed should be translated into a physical measurement ledger because two reference-source measurements per sector and frequency may be operationally substantial.

## Evidence and Attribution

| ID | Evidence inspected | Supports | Assessment |
|---|---|---|---|
| E1 | Complete 27-page PDF, full-paper HTML, and extracted source text | Problem statement, equations, algorithms, theorems, numerical tables, conclusion | High confidence for faithful source reporting; equations were not independently rederived |
| E2 | arXiv metadata record | Title, authors, v1 date, categories, public source locators | High |
| E3 | Institutional publication record and DOI | Journal, volume, issue, article number, publication date | High for bibliography; publisher full text was not separately inspected |
| E4 | Local integrity and extraction records | PDF/HTML completeness and cache status | High; private paths and source bytes are not published |
| E5 | Three inspected related DEP manuscripts and their primary-source references | Cross-domain synthesis | Medium; conceptual context does not validate this paper |

Author claims are labeled as such. Numerical values above are transcribed from the primary paper, not reproduced measurements. Synthesis and product ideas below are reviewer interpretations.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md` — selected because accelerated MRI is another physics-grounded inverse reconstruction problem; its FastMRI evidence and Kronecker parameterization expose the tension between reconstruction quality, representation, and deployment constraints. Source basis: arXiv:2503.05063.
2. `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md` — selected because it co-designs a nonlinear measurement preprocessor and iterative decoder under noise, closely paralleling reference-source intervention followed by structured inversion. Source basis: arXiv:2106.01573 and DOI:10.1109/ITW48936.2021.9611458.
3. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` — selected because it treats excitation, initialization, conditioning, and heterogeneous calibration as prerequisites for recovering latent physical parameters from sensor measurements. Source basis: arXiv:2407.11420 and DOI:10.1109/TRO.2025.3532506.

## Synthesis Note

### Concept Bridge

The four artifacts describe one systems pattern at different layers. Acoustic phase retrieval makes the latent field identifiable by introducing known point-source probes. Irregular clipping modifies the transmitted measurements so the decoder sees a more useful distortion/noise tradeoff. iKalibr makes latent spatial and temporal parameters observable by requiring adequate motion excitation and fitting multiple calibrated residual families. Hypercomplex MRI then demonstrates that reconstruction quality also depends on how coupled physical channels are represented inside the estimator. Together they suggest a pipeline with four explicit contracts: intervention design, calibration/observability, conditioned inversion, and representation-aware reconstruction. A gain at one layer is not credible unless the downstream error ledger shows where uncertainty moved.

### Potential Implementations

1. **Condition-certified acoustic mapper:** Drive two calibrated reference emitters per acquisition sector, recover complex fields only when determinant and calibration margins pass, reconstruct a source map, and publish residual/conditioning overlays beside the image.
2. **Adaptive probe planner:** Select reference amplitudes, positions, and frequencies using a bounded optimizer that minimizes predicted condition number while respecting placement and power constraints; freeze the plan before measurement and compare it with the paper's analytic geometry.
3. **Cross-domain inverse-problem harness:** Express acoustic, clipped-channel, calibration, and MRI cases through a shared interface for known intervention, latent state, forward operator, conditioning gate, reconstruction, and uncertainty report.

### Deeper Relationship Observations

1. Known interventions do more than add data: they choose a coordinate system in which hidden variables become solvable. Reference sources expose complex phase, clipping mixtures reshape decoder state evolution, and calibration excitation exposes spatiotemporal offsets.
2. Conditioning is an end-to-end property. A well-conditioned two-by-two phase solve can still feed a poor Fourier reconstruction, just as precise calibration can feed a brittle world model or a compact MRI network can erase clinically relevant structure.
3. Integration can suppress some upstream noise while hiding failure. The paper's Fourier coefficient integrals reduce reconstruction error relative to noisy phase recovery, but that filtering benefit needs residual maps so systematic probe or model bias is not mistaken for robustness.

### Conceptual Similarities

1. Each entry uses domain structure to constrain an otherwise ambiguous or inefficient estimation problem.
2. Each entry separates an upstream transformation or calibration stage from a downstream estimator, creating a natural validation boundary.
3. Each entry needs mismatch tests beyond source-reported averages: geometry drift, clipping-distribution shift, sensor degeneracy, and anatomy/pathology shift are different forms of the same boundary problem.

### MVP Implementations with Code Mock-Ups

1. **Auditable two-probe phase solver:** accept already computed linear-system coefficients and reject an ill-conditioned solve.

```python
def recover_field(a, rhs, min_margin=0.01):
    (a00, a01), (a10, a11) = a
    r0, r1 = rhs
    determinant = a00 * a11 - a01 * a10
    scale = max(abs(a00), abs(a01), abs(a10), abs(a11), 1e-12)
    margin = abs(determinant) / (scale * scale)
    if margin < min_margin:
        raise ValueError("reference geometry is not observable enough")
    real = (r0 * a11 - a01 * r1) / determinant
    imag = (a00 * r1 - r0 * a10) / determinant
    return complex(real, imag), {"normalized_determinant": margin}
```

2. **Calibration and intervention gate:** combine iKalibr-style excitation/calibration checks with a phase-retrieval determinant margin before collecting a batch.

```python
def approve_batch(excitation, time_offset_ms, det_margin):
    checks = {
        "excitation": excitation >= 0.8,
        "time_alignment": abs(time_offset_ms) <= 1.0,
        "phase_geometry": det_margin >= 0.05,
    }
    return {"approved": all(checks.values()), "checks": checks}
```

3. **Reconstruction evidence ledger:** compare intervention settings and carry upstream conditioning into the final error report.

```python
def evidence_row(probe_plan, condition, residual, reconstruction_error):
    return {
        "probe_plan": probe_plan,
        "condition": round(float(condition), 4),
        "measurement_residual": round(float(residual), 6),
        "reconstruction_error": round(float(reconstruction_error), 6),
        "status": "review" if condition > 50 or residual > 0.05 else "pass",
    }
```

### Developer Challenges

1. Build a simulator that perturbs reference location, amplitude, phase, clock alignment, and background sound speed independently, then identify which perturbation first invalidates the determinant gate.
2. Implement matched baselines for no probe, one probe, two analytic probes, and two optimized probes with identical frequency and measurement budgets.
3. Carry calibration, conditioning, phase-recovery, and source-reconstruction uncertainty through one versioned evidence record without logging raw sensitive measurements.

### Author Challenges

1. Replace the synthetic-only demonstration with calibrated acoustic hardware and publish the complete extra-measurement, runtime, and positioning-error budget.
2. Extend the stability analysis to uncertain point-source positions/amplitudes and a mismatched or heterogeneous background medium.
3. Test whether jointly optimized probe placement and Fourier truncation improves end-to-end reconstruction without sacrificing the analytic conditioning certificate.

## Validation Notes

- Random selection used uniform `Get-Random` over 75,776 unique PDF-parent paper units derived from 75,777 `rg` PDF candidates; zero-based index 16,432 was selected.
- Dedup scans covered Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data for the arXiv ID, DOI, title, and slug. Exclusions: 0; reselections: 0; public-safe 24-hour cutoff date marker: 2026-07-15.
- The selected archive unit was initially partial. The valid 622,169-byte PDF was preserved. Repaired full-paper HTML was 2,289,055 bytes with 132,609 body characters, 40 heading/section markers, five structure terms, a valid document marker, and no partial files.
- PDF, HTML, and TeX/source extraction completed locally. No PDF, HTML, TeX/source archive, extracted text, cache, or local path is included in this report or authorized for repository upload.
- The three code blocks are the three required MVP mock-ups; each uses synthetic scalar inputs and requires engineering hardening.

## Attribution Block

- Source URL: https://arxiv.org/abs/1803.11323
  - Applies to: source identity, abstract, authors, submission history, and public source locators.
  - Notes: Canonical arXiv metadata record.
- Source URL: https://arxiv.org/pdf/1803.11323
  - Applies to: the full-paper review, equations, algorithms, theorems, tables, figures, and conclusion.
  - Notes: Public equivalent of the verified local PDF; the PDF was not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/1803.11323
  - Applies to: full-paper HTML review and integrity verification.
  - Notes: Approved full-paper fallback because official arXiv HTML was unavailable; this is not the abstract page.
- Source URL: https://arxiv.org/e-print/1803.11323
  - Applies to: source-text cross-checks of formulas, tables, and section structure.
  - Notes: Source package retained and inspected locally only.
- Source URL: https://doi.org/10.1088/1361-6420/aaccda
  - Applies to: journal identity and related DOI.
  - Notes: Persistent publisher identifier.
- Source URL: https://scholars.hkbu.edu.hk/en/publications/retrieval-of-acoustic-sources-from-multi-frequency-phaseless-data/
  - Applies to: journal, volume, issue, article number, publication date, and DOI metadata.
  - Notes: Official author-institution publication record.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: artifact layout, logs, reports, DEP contents, source withholding, and commit rules.
  - Notes: Live repository authority fetched before writing.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E container path and publications-index update.
  - Notes: Live DEP filing authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion-repository layout used during deduplication.
  - Notes: Live companion repository authority.
- Repository file: `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md
  - Source basis: https://arxiv.org/abs/2503.05063
  - Notes: Related DEP on physics-grounded MRI reconstruction and parameter-efficient representation.
- Repository file: `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Irregular%20Clipped%20SR/irregular_clipped_sr_manuscript.md
  - Source basis: https://arxiv.org/abs/2106.01573 and https://doi.org/10.1109/ITW48936.2021.9611458
  - Notes: Related DEP on nonlinear measurement preprocessing and structured decoding.
- Repository file: `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Source basis: https://arxiv.org/abs/2407.11420 and https://doi.org/10.1109/TRO.2025.3532506
  - Notes: Related DEP on sensor excitation, observability, calibration, and factor-graph refinement.
