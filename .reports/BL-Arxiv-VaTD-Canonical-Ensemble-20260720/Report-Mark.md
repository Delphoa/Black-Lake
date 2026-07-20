# Report-Mark: VaTD Canonical Ensemble

## Report Context

This source-first review examines the paper "Deep generative modelling of canonical ensemble with differentiable thermal properties" and its official implementation. Claims below distinguish mathematical derivations, source-reported measurements, author estimates, repository observations, and reviewer synthesis.

## Selection and Deduplication

The local archive contained 75,778 PDF candidates representing 75,776 unique PDF-parent paper units. A uniform random draw over the sorted unique unit list selected zero-based index 20,958. The selected paper was identified as arXiv:2404.18404.

Before acceptance, the Black Lake logs, reports, DEP-E deposits, staging records, automation memory, and relevant Black-Lake-Data records were scanned for the arXiv ID, arXiv DOI, publisher DOI, normalized title, and slug. No prior matching Arxiv DEP artifact or same-paper marker within 24 hours was found. The first draw was accepted: zero duplicate exclusions, zero other exclusions, and zero reselections.

## Local Source-Integrity Result

Initial classification: **partial**. The archive unit contained a valid full PDF but no full-paper HTML. Review and synthesis paused while the archive was repaired from official public endpoints using bounded retries and preservation checks.

Final classification: **complete and verified**. The preserved PDF was 3,010,534 bytes, began with `%PDF-`, and contained trailing `%%EOF`. The repaired full-paper HTML was 318,497 bytes and yielded 71,959 body characters after script/style removal, a valid document marker, 47 section/heading markers, seven paper-structure terms, and no abstract-only, error, or conversion-notice marker. The archive README, attribution/provenance record, machine-readable summary, and verification report were updated before review began.

Original source files remain local. No PDF, HTML, source archive, extracted source text, cache, or other source file was copied into this deposit or prepared for upload.

## Source Metadata

| Field | Value |
|---|---|
| Title | Deep generative modelling of canonical ensemble with differentiable thermal properties |
| Authors | Shuo-Hui Li; Yao-Wen Zhang; Ding Pan |
| arXiv | [2404.18404v2](https://arxiv.org/abs/2404.18404) |
| arXiv DOI | [10.48550/arXiv.2404.18404](https://doi.org/10.48550/arXiv.2404.18404) |
| Publisher DOI | [10.1103/8wx7-kyx8](https://doi.org/10.1103/8wx7-kyx8) |
| Version dates | v1: 2024-04-29; v2: 2025-12-09 |
| Publication | Physical Review Letters 135, 027301 (2025); issue record dated 2025-07-08 |
| Official code | [li012589/vatd](https://github.com/li012589/vatd), inspected at commit `d8fd69c243951769e1e083f8451339522873af8f` |
| Evidence inspected | Verified PDF; verified full-paper HTML; TeX source; public arXiv record; APS issue record; official code repository |

## Research Notes

### Problem

Canonical-ensemble calculations often require separate Monte Carlo runs at many temperatures. This makes dense temperature sweeps expensive, and finite-difference estimates of energy derivatives can be noisy near phase transitions.

### Mechanism

VaTD defines a normalized, temperature-conditioned density `q_theta(s; beta)` and minimizes the interval-averaged objective `E_q[log q_theta + beta E]`. The exact variational optimum is the Boltzmann density. Because the model density is tractable, the authors estimate `log Z(beta)` from the free-energy bound and differentiate the learned response with respect to inverse temperature for energy and heat capacity.

That identity establishes the target of the variational problem; it does not prove that a finite neural model reaches the optimum or covers every thermodynamic mode. Density evaluation, symmetry handling, mode coverage, and derivative validation therefore remain empirical requirements.

### Main Results

- On a 16 by 16 Ising model, a beta-conditioned PixelCNN fixes the first spin and compares learned free energy, energy, and heat capacity against exact finite-lattice values over beta from 0.05 to 1.2.
- On a 16 by 16 XY model, a normalizing flow with a von Mises prior pins the first spin and compares VaTD observables with MCMC across beta from 0.4 to 2.0.
- Source Table S1 reports convergence-time comparisons on an RTX 4090. At beta 0.65, HMC versus VaTD times are 497.46 versus 7.03 seconds for energy and 3164.93 versus 35.98 seconds for heat capacity. At beta 0.90, they are 526.67 versus 38.94 and 21863.21 versus 256.01 seconds. At beta 0.95, they are 435.43 versus 23.61 and 19654.64 versus 206.86 seconds. At beta 1.25, they are 568.46 versus 6.39 and 4883.55 versus 142.83 seconds.
- The authors summarize these selected measurements as roughly 10 to 90 times faster for the benchmark. This is source-reported, hardware- and threshold-specific evidence, not a universal speed guarantee.
- A training-overhead crossover near 18 requested temperatures is an author estimate; an RMHMC curve suggests a delay of roughly 50 more points, but that extension is not a direct measurement.
- XY scaling is plotted through 258 by 258. Systems above 32 by 32 use checkpointing and reduced batch sizes under a 24 GB RTX 4090 constraint, so the large-size result is plot-level scaling evidence rather than a complete end-to-end timing table.

### Evidence and Limits

The paper's strongest evidence is the exact Ising comparison, the physically structured XY benchmark, and tabulated convergence-time measurements at four beta values. Limits include exact-reference use during Ising model selection, single-run presentation for major results, sparse timing points, model-dependent reverse-KL coverage risk, and limited reporting of uncertainty and baseline tuning.

The official code is compact and pinned to six principal Python package dependencies, but it provides no frozen release, pretrained checkpoints, exact environment lock, or seed-level replication bundle. A material discrepancy also needs resolution: the inspected XY training script uses `K=25` interpolation bins and one hidden fully connected layer, whereas the v2 supplement reports 45 interpolation points and two fully connected layers.

### Implementation Relevance

The most reusable idea is not a claim of universal sampler replacement. It is a validation-gated response-surface pattern: condition a tractable density on a physical control parameter, learn across an interval, differentiate only after density and mode-coverage checks pass, and compare total time-to-accuracy against matched baselines. This pattern could support local benchmark tools, surrogate thermodynamic sweeps, or experiment-design systems.

## Evidence and Attribution

| Statement type | Basis | Treatment |
|---|---|---|
| Variational optimum equals the Boltzmann density | Paper derivation | Reported as a formal identity under stated conditions |
| Ising and XY results | Paper figures, tables, and supplement | Reported as source evidence for the studied systems |
| Four timing comparisons | Supplement Table S1 | Reported with exact source values and hardware context |
| Crossover near 18 points and RMHMC extension | Paper discussion and plotted estimate | Labeled as author estimates, not measurements |
| Large-system XY scaling | Source figures and configuration notes | Labeled as plot-only evidence with memory adaptations |
| Code/configuration discrepancy | Official code versus v2 supplement | Repository observation requiring author clarification |
| Product and implementation proposals | Reviewer synthesis | Not attributed to the paper authors |

## Related DEP Entries

1. [Physical Data AI](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md) - concrete overlap: differentiable physical equations are embedded in trainable models to obtain compact, interpretable representations. Source basis: inspected sections on analytic equations, differentiable computation, and residual learning.
2. [Surface SQD Study](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Surface%20SQD%20Study/surface-sqd-study.md) - concrete overlap: both estimate many-body energy behavior from samples and require physical-sector validation, classical comparators, and scaling discipline. Source basis: inspected evidence ledger, constraint checks, energy estimation, and scaling cautions.
3. [Transport Convexity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Transport%20Convexity/transport_convexity_manuscript.md) - concrete overlap: both use distribution-transform geometry to make a difficult physical inference tractable while depending on explicit regularity assumptions. Source basis: inspected transport formulation, convexity assumptions, and implementation discussion.

## Synthesis Note

### Concept Bridge

VaTD connects the three related deposits through a shared design principle: place known physical or geometric structure inside a learnable transformation, then make validity tests part of the output contract. Physical Data AI contributes the differentiable-equation viewpoint; Surface SQD contributes sampled-state and comparator discipline; Transport Convexity contributes transform geometry and assumption tracking. Together they suggest a scientific-ML stack in which a conditional density is useful only when its physical constraints, coverage, derivatives, and computational advantage are measured explicitly.

### Potential Implementations

1. **Thermodynamic response-surface service:** train a local, density-evaluable model across an authorized beta interval and expose validated estimates of free energy, energy, heat capacity, samples, and uncertainty.
2. **Amortization benchmark harness:** compare VaTD, HMC, RMHMC, and exact baselines under matched convergence criteria while accounting separately for training, tuning, burn-in, sampling, evaluation, and memory.
3. **Phase-transition experiment planner:** use derivative and coverage diagnostics to propose additional beta points, but require an independent sampler or exact reference before elevating a detected feature into a scientific claim.

### Deeper Relationship Observations

1. **Differentiability is an evidence amplifier, not evidence itself.** The same end-to-end gradients that connect Physical Data AI to VaTD can produce precise derivatives of a biased density; derivative access raises the value of coverage gates rather than replacing them.
2. **Physical-sector checks generalize beyond quantum sampling.** Surface SQD's emphasis on valid sampled sectors maps directly to fixed-spin, rotational-symmetry, and rare-mode checks in canonical-ensemble generators.
3. **Transform assumptions define the trustworthy domain.** Transport Convexity makes regularity assumptions explicit; VaTD likewise needs support, normalization, capacity, and beta-range assumptions surfaced before interpolation or differentiation is trusted.

### Conceptual Similarities

1. Each approach uses known structure to reduce a difficult high-dimensional inference problem to a more tractable learned representation.
2. Each separates an attractive mathematical mechanism from empirical claims that still require comparators, scaling evidence, and failure analysis.
3. Each can support a compact MVP only if source provenance, assumption boundaries, validation metrics, and stop conditions are preserved with the model output.

### MVP Implementations

#### 1. Validated beta-grid builder

This mock-up creates an explicit in-range evaluation grid and rejects underspecified or nonphysical intervals.

```python
def temperature_grid(
    beta_min: float,
    beta_max: float,
    points: int,
) -> list[float]:
    if points < 2:
        raise ValueError("points must be at least 2")
    if beta_min <= 0 or beta_max <= beta_min:
        raise ValueError("require 0 < beta_min < beta_max")
    step = (beta_max - beta_min) / (points - 1)
    return [beta_min + index * step for index in range(points)]
```

#### 2. Derivative sanity checker

This mock-up computes centered observables only on an evenly spaced beta grid and fails closed when the inputs are unsuitable.

```python
def finite_difference_observables(
    beta: list[float],
    log_z: list[float],
) -> list[dict[str, float]]:
    if len(beta) != len(log_z) or len(beta) < 3:
        raise ValueError("matching arrays with at least 3 points required")
    if any(right <= left for left, right in zip(beta, beta[1:])):
        raise ValueError("beta must be strictly increasing")

    results: list[dict[str, float]] = []
    for index in range(1, len(beta) - 1):
        left_step = beta[index] - beta[index - 1]
        right_step = beta[index + 1] - beta[index]
        tolerance = 1e-9 * max(1.0, abs(left_step), abs(right_step))
        if abs(left_step - right_step) > tolerance:
            raise ValueError("centered check requires an even grid")
        energy = -(
            log_z[index + 1] - log_z[index - 1]
        ) / (2.0 * left_step)
        curvature = (
            log_z[index + 1]
            - 2.0 * log_z[index]
            + log_z[index - 1]
        ) / (left_step**2)
        results.append(
            {
                "beta": beta[index],
                "energy": energy,
                "heat_capacity": beta[index] ** 2 * curvature,
            }
        )
    return results
```

#### 3. Measured crossover calculator

This mock-up prevents a speed claim until the full fixed cost and per-query costs produce a measured crossover.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class CostModel:
    learned_fixed_seconds: float
    learned_per_query_seconds: float
    baseline_per_query_seconds: float


def first_crossover(
    model: CostModel,
    max_points: int = 1000,
) -> int | None:
    if min(
        model.learned_fixed_seconds,
        model.learned_per_query_seconds,
        model.baseline_per_query_seconds,
    ) < 0:
        raise ValueError("costs must be nonnegative")
    for points in range(1, max_points + 1):
        learned = (
            model.learned_fixed_seconds
            + points * model.learned_per_query_seconds
        )
        baseline = points * model.baseline_per_query_seconds
        if learned <= baseline:
            return points
    return None
```

### Developer Challenges

1. **Density and support correctness:** implement a normalized conditional density whose support, symmetry treatment, Jacobians, and temperature conditioning remain correct across the full declared beta interval.
2. **Derivative stability:** preserve useful gradients through stochastic estimates and automatic differentiation without hiding bias, numerical instability, or rare-mode failure.
3. **Reproducible benchmarking:** freeze configurations, environments, seeds, hardware accounting, convergence rules, and competitor tuning so the amortization claim can be audited.

### Author Challenges

1. Reconcile the official XY script's 25 interpolation bins and one hidden fully connected layer with the v2 supplement's 45 interpolation points and two fully connected layers.
2. Publish a frozen release with exact configurations, checkpoints or deterministic training recipes, seeds, environment lock, raw benchmark traces, and uncertainty across repeated runs.
3. Expand evaluation to independent held-out beta points, rare-mode and symmetry diagnostics, matched baseline tuning, measured crossover curves, and systems beyond the reported lattice benchmarks.

## Validation Notes

- The manuscript title and H1 were matched and kept within the 40-character limit.
- The local source gate passed before synthesis; the repaired unit includes a valid PDF and structurally complete full-paper HTML.
- Paper, supplement, code, public metadata, and exactly three related DEP artifacts were inspected and attributed.
- Mathematical identities, source measurements, author estimates, repository observations, and reviewer proposals are labeled separately.
- The three Python mock-ups use the standard library only and are intended for syntax validation, not as production scientific software.
- Public-path and timestamp sanitation, Markdown-only allowlisting, forbidden-source extension checks, staged-diff review, and `git diff --check` are required before submission.
- No `.source/` directory is included. All original source files remain withheld locally.

## Attribution Block

- **Primary source:** Shuo-Hui Li, Yao-Wen Zhang, and Ding Pan, "Deep generative modelling of canonical ensemble with differentiable thermal properties," arXiv:2404.18404v2. [arXiv](https://arxiv.org/abs/2404.18404) - [arXiv DOI](https://doi.org/10.48550/arXiv.2404.18404) - [publisher DOI](https://doi.org/10.1103/8wx7-kyx8).
- **Official implementation:** [li012589/vatd](https://github.com/li012589/vatd), inspected at commit `d8fd69c243951769e1e083f8451339522873af8f`.
- **Publication record:** [Physical Review Letters, volume 135, issue 2](https://journals.aps.org/prl/issues/135/2).
- **Related DEP entries:** [Physical Data AI](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md); [Surface SQD Study](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Surface%20SQD%20Study/surface-sqd-study.md); [Transport Convexity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Transport%20Convexity/transport_convexity_manuscript.md).
- **Review date:** 2026-07-20.
- **Source locality:** source PDF, full-paper HTML, metadata, TeX/source archive, extracted text, and caches were retained in the local archive and were not uploaded.
- **Artifact status:** source-first derived research review for Delphoa/Black-Lake; no source files included.
