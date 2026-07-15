# Making Acoustic Phase Observable by Designed Intervention

## A detailed review, technical reconstruction, and independent re-conceptualization of “Retrieval of acoustic sources from multi-frequency phaseless data”

**Source paper:** Deyue Zhang, Yukun Guo, Jingzhi Li, and Hongyu Liu, “Retrieval of acoustic sources from multi-frequency phaseless data,” *Inverse Problems* 34 (2018), arXiv:1803.11323v1, DOI 10.1088/1361-6420/aaccda.[^source-paper]

**Artifact prepared:** 2026-07-16

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval`

**Source commit:** `e149ddfa04aaff808e7d3602c5bf02691257a212`

**Paired task indicator:** `BL-DEPPAIR-20260716-E47CCF16`

**Direction:** `DEP-E -> DEP-A`

**Source provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes

**Primary source reviewed:** complete two-file DEP-E repository record and the complete authorized 27-page arXiv v1 paper

**Review scope:** full-record and full-paper reconstruction, claim vetting, quantitative audit, external primary-source context, re-conceptualization, implications, and replication agenda
**Reproduction boundary:** no code was available in the reviewed record, no implementation was inspected, and no equations, simulations, noise draws, figures, tables, or reconstruction results were independently rerun or reproduced

---

## Executive assessment

### The contribution in one sentence

The paper introduces two deliberately placed reference point sources per angular measurement sector and frequency so that magnitude-only acoustic measurements yield a well-conditioned linear system for the missing complex field, after which a standard multifrequency Fourier method reconstructs the unknown source.

### The deeper idea

The method does not infer phase from passive intensities by adding a clever estimator. It changes the experiment. A known coherent field is injected twice, producing two interference measurements whose algebra separates the real and imaginary parts of the unknown field. Geometry is not a presentation detail: the reference locations are chosen so that the Bessel-function coefficient matrix remains invertible, and the paper proves lower bounds on its determinant. The mechanism is therefore best described as **intervention-certified observability**. The experiment creates the information the downstream inverse method needs and certifies the conditioning of the transformation that recovers it.

### Bottom-line judgment

The complete paper supports a coherent three-part contribution: a reference-source measurement design, a solvability and perturbation analysis for its local phase-retrieval step, and a synthetic demonstration coupled to an established Fourier reconstruction. The mathematics is materially stronger than a purely empirical phase-recovery proposal: Theorem 3.1 gives determinant lower bounds under explicit geometry and frequency conditions, and Theorem 3.2 converts bounded relative magnitude perturbations into a relative complex-field error estimate. The numerical results are consistent with noise-sensitive but usable recovery in the chosen setting.

The evidence does not establish real-world readiness or broad model robustness. There is one synthetic source family, one displayed measurement sector, a simple independent bounded multiplicative-noise model, no repeated-seed statistics, no calibration-error study, no timing or hardware report, and no released implementation in the reviewed materials. Claims about three-dimensional acoustics, Maxwell systems, or practical instrumentation are prospective. The paper is convincing as an analytic mechanism under its assumptions and suggestive, not conclusive, as an engineering solution.

### Principal strengths

- Measurement design, algebra, and stability analysis align: the same determinant that enables phase recovery is explicitly bounded away from zero.
- The two-stage decomposition is modular. Once phase is recovered, a conventional phased inverse-source solver can be used.
- Numerical tables expose both relative L2 and relative infinity errors at four frequencies and four noise levels rather than relying only on images.
- The complete DEP-E record preserves the paper identity, technical reconstruction, limitations, quantitative results, related concepts, and attribution in a compact scholarly bundle.

### Principal qualifications

1. The theorem controls phase-retrieval error under a prescribed relative perturbation model; it does not cover reference-source misplacement, amplitude/phase calibration drift, boundary geometry error, heterogeneous media, reverberation, or sensor-response error.
2. The synthetic experiment does not separate errors from forward discretization, random noise, phase retrieval, Cauchy-data continuation, Fourier truncation, and spatial quadrature through a full component ablation.
3. “No regularization or iteration” describes the presented inversion pipeline, but the forward-data generation uses mesh refinement and the practical conditioning of the Fourier stage remains parameter dependent.

---

## 1. The problem the paper is actually solving

### 1.1 Formal problem and stakes

An unknown compactly supported source function \(S\) radiates a time-harmonic field \(u(x,k)\) governed in two dimensions by the Helmholtz equation

\[
\Delta u(x,k)+k^2u(x,k)=S(x),
\]

with the Sommerfeld radiation condition. The source is supported in a square domain \(V_0=[-a,a]^2\), while measurements are taken on a surrounding circle \(\Gamma_R\). At multiple wavenumbers \(k\), the desired input to a conventional inverse-source method is the complex field \(u\), but the assumed instrument reports only \(|u|\).

Magnitude removes the global and local phase information carried by the complex wave. The issue is not merely numerical inconvenience. Phase-less inverse problems commonly admit invariances and nonuniqueness that do not arise with complex observations. The practical stakes include acoustic source localization and imaging, but the paper itself studies a specific idealized scalar, two-dimensional, homogeneous-background model.

### 1.2 Prior method families

The paper situates itself among multifrequency inverse-source methods, phaseless inverse scattering, and reference-object techniques. Multifrequency phased data can support recursive, sampling, or Fourier reconstructions; the paper adopts the Fourier line developed for the Helmholtz inverse-source problem.[^fourier-predecessor] Phaseless methods often modify the illumination or introduce a known scatterer/reference object to break ambiguities. Here the reference is an actively added point source, and the output of the phase-retrieval stage is designed to plug into a phased solver rather than replace it.

### 1.3 The proposed gap

The authors argue that a direct, noniterative way to turn multifrequency phaseless boundary data into usable complex measurements is missing for their inverse-source setting. Their answer is a local linearization created by interference with known fields. The gap is narrow and precise: recover \(\operatorname{Re}u\) and \(\operatorname{Im}u\) on each measurement sector without solving a nonlinear global phase-retrieval optimization.

---

## 2. Formal and technical reconstruction

### 2.1 Definitions and assumptions

The measurement circle is divided into \(m\) angular arcs \(\Gamma_j\), with \(m\geq 10\). Each arc is paired with a sector \(B_j\) and two reference locations \(z_{j,1}\) and \(z_{j,2}\) outside the source support. The observation radius is set to \(R=\tau a\) with \(\tau\geq 6\). An admissible set of wavenumbers contains ordinary Fourier-linked frequencies and one specially chosen small auxiliary frequency \(k^*\).

For reference index \(\ell\in\{1,2\}\), the known point source produces a Green-function field proportional to the outgoing Hankel function \(H_0^{(1)}(k|x-z_{j,\ell}|)\). Its amplitude coefficient is scaled from the measured magnitude of \(u\) on the arc. The observed combined field is

\[
v_{j,\ell}(x,k)=u(x,k)-c_{j,\ell,k}\Phi_k(x,z_{j,\ell}),
\]

and the available data for phase retrieval are \(|u|\) and the two magnitudes \(|v_{j,1}|,|v_{j,2}|\).

The analysis assumes the forward model, wavenumbers, sensor geometry, reference locations, reference-field formula, and relative-noise envelope are known. The source is frequency independent in the presented formulation. The reference source is coherent with the unknown field so that cross terms retain relative phase.

### 2.2 Central equations

Squaring each combined-field magnitude and subtracting the known energy terms isolates an interference cross term. Because \(H_0^{(1)}=J_0+iY_0\), each reference produces one real linear equation in \(\operatorname{Re}u\) and \(\operatorname{Im}u\):

\[
Y_0(kr_{j,\ell})\operatorname{Re}u
-J_0(kr_{j,\ell})\operatorname{Im}u=f_{j,\ell,k},
\]

where \(r_{j,\ell}=|x-z_{j,\ell}|\) and \(f_{j,\ell,k}\) is computed from the three measured magnitudes and the known reference amplitude. Stacking \(\ell=1,2\) yields a two-by-two matrix \(A_{j,k}\). Its determinant is a cross-combination of \(J_0\) and \(Y_0\) evaluated at the two reference distances. If that determinant vanishes, the two interventions provide redundant projections and phase remains unobservable; if it is bounded away from zero, Cramer's rule recovers both quadratures.

The paper's parameter construction places the two references along rays tied to each sector. For ordinary frequencies, Theorem 3.1 proves

\[
|\det A_{j,k}|\geq \frac{1-7/(20\tau)}{kR},
\]

and for the small auxiliary frequency it proves \(|\det A_{j,k^*}|>4/9\). These lower bounds are the conditioning certificate. The proof uses asymptotic expansions and error bounds for Bessel functions at ordinary frequencies and series bounds for the small-frequency case.

Under the paper's relative perturbation model, Theorem 3.2 reports

\[
\|u^\epsilon_{j,k}-u_{j,k}\|_{j,\infty}
\leq \epsilon C_\epsilon\|u_{j,k}\|_{j,\infty},
\]

with

\[
C_\epsilon=\frac{2.5(2+\epsilon)^2(3+\epsilon)+15}{1-\epsilon}.
\]

This is a worst-case relative bound within the assumed noise envelope. It is not a tight prediction of the table values and becomes conservative as the algebra accumulates triangle-inequality bounds.

### 2.3 Algorithms and components

**Algorithm PR** is the phase-retrieval stage. It chooses \(R,m\), the frequency set, and the two reference geometries; collects \(|u|\) and two combined-field magnitudes per sector/frequency; computes the right-hand sides; and solves the two-by-two systems pointwise on each arc.

**Algorithm FM** is the source-reconstruction stage inherited from prior work. It chooses an auxiliary radius \(\rho\), a Fourier truncation \(N\), and an admissible frequency set; collects the recovered multifrequency complex data on \(\Gamma_R\); evaluates auxiliary Cauchy data on \(\Gamma_\rho\); estimates the Fourier coefficients of \(S\); and forms a truncated Fourier series \(S_N\).

There is no model training. “Inference” consists of experimental acquisition followed by direct algebra, Cauchy-data evaluation, integration, and truncated-series synthesis.

### 2.4 Notation and implementation audit

The complete paper and the DEP-E manuscript agree on the main geometry, determinant bounds, perturbation result, numerical parameters, table values, and final reconstruction errors. No material contradiction was found. The paper sometimes calls the method stable based on both a conservative theorem and a single synthetic noise study; readers should keep those evidentiary layers separate. No executable implementation was available to resolve numerical conventions that are abbreviated by the paper's reference to prior work for further Fourier-method details.

---

## 3. Architecture and information flow

### 3.1 Measurement representation

The native observation is a real nonnegative magnitude field indexed by boundary position and frequency. Two extra magnitude channels are generated by known reference interventions. The latent representation after Algorithm PR is a complex boundary field whose real and imaginary parts are explicit solutions of a local linear system. Algorithm FM then maps that complex boundary representation into Fourier coefficients of the spatial source.

### 3.2 Decision or action modules

There is no learned decision module. The operative choices are geometric: how to partition the boundary, where to place references, which ordinary wavenumbers to use, and how to define the special low frequency. These choices determine matrix conditioning. Reconstruction choices—\(\rho\), \(N\), measurement count, and quadrature—determine the resolution/noise tradeoff in the Fourier stage.

### 3.3 Dependencies and post-processing

The phase-retrieval algebra depends on a homogeneous two-dimensional Green function and coherent additive reference sources. The source reconstruction depends on the prior Fourier method, including auxiliary Cauchy-data continuation. The final spatial image is post-processed through Fourier truncation. The paper argues that the integration inherent in coefficient estimation filters some high-frequency noise, which plausibly explains why the 5% phase-field error does not translate one-for-one into final source error. That explanation is physically and numerically reasonable but is not isolated by an ablation.

---

## 4. The complete operational pipeline

### 4.1 End-to-end flow

1. Specify the support scale \(a\), measurement radius \(R=\tau a\), at least ten angular sectors, ordinary wavenumbers, and an auxiliary low wavenumber.
2. Measure the unknown-source magnitude \(|u|\) on the boundary.
3. For each sector and frequency, activate the first calibrated reference point source and measure \(|v_{j,1}|\); repeat for the second reference.
4. Convert the three magnitudes into two interference right-hand sides.
5. Solve the certified two-by-two Bessel system for the complex field on that sector.
6. Assemble the recovered phased boundary data over sectors and frequencies.
7. Evaluate auxiliary Cauchy data, integrate for Fourier coefficients, truncate, and synthesize the source estimate.

### 4.2 Resource allocation

The acquisition cost is at least three magnitude configurations per sector and frequency: unknown field alone plus two reference activations. With \(m\) sectors and \(|K_N|\) frequencies, the reference-stage experiment scales linearly in both. The paper does not report acquisition time, reference-switching overhead, solver runtime, memory, or numerical complexity. The numerical reconstruction uses 400 pseudo-uniform boundary measurements and an 800-by-800 evaluation grid. Fourier truncation follows \(N=2\lceil\epsilon^{-1/3}\rceil\) in the reported experiment.

### 4.3 Guarantee boundary

Exact algebra holds when the model and measurements are exact and \(A_{j,k}\) is nonsingular. Determinant lower bounds hold under the stipulated geometry, radius, sector count, and frequency construction. The perturbation guarantee applies to the paper's bounded relative magnitude errors. The Fourier method's theoretical basis is delegated to earlier work. The final source-image quality is empirical for one synthetic example. No guarantee is provided for reference calibration error, medium mismatch, finite sensor response, environmental noise correlation, three-dimensional propagation, or actual apparatus constraints.

---

## 5. Re-conceptualization

### 5.1 Intervention-certified observability

The paper can be abstracted as a four-step design pattern:

1. Identify the missing latent coordinate that prevents an established solver from operating.
2. Add known interventions that produce independent projections of that coordinate.
3. design the interventions so their observation matrix has a certified singular-value or determinant margin.
4. Hand the recovered coordinate to a mature downstream estimator.

This is more general than “use reference sources.” It is a blueprint for turning an under-observed passive measurement into a controlled active measurement. The theorem is not separate from the instrumentation: it certifies that the intervention geometry provides distinct information.

**Boundary of the analogy:** A determinant bound for a two-dimensional linear subproblem does not automatically imply global identifiability, robustness, or optimal experimental design in nonlinear, high-dimensional, or mismatched systems.

### 5.2 Phase recovery as local demodulation

The two references act like calibrated probes. Their interference with the unknown field encodes two quadratures into intensity differences, analogous in spirit to coherent demodulation. Unlike a purely signal-processing metaphor, however, the spatial Green function determines the mixing coefficients, and the reference geometry must be chosen with the Bessel structure in view.

**Boundary of the analogy:** The paper does not build or analyze a heterodyne receiver, and the noise model does not include oscillator phase drift or hardware coherence loss.

### 5.3 Transferable design principle

When a downstream solver expects information that a passive sensor discards, it may be more effective to redesign the measurement with certified probes than to compensate with a more complex inverse algorithm. The intervention should be evaluated by its information geometry and conditioning margin, not merely by downstream benchmark quality.

---

## 6. Experimental design reconstructed

### 6.1 Data and source

All data are synthetic. A smooth “mountain-shaped” source combines a localized Gaussian bump and a signed polynomial-times-Gaussian term over \([-0.3,0.3]^2\). The forward radiated fields are generated with a finite-element method on a truncated circular domain surrounded by a perfectly matched layer. The forward mesh is refined until successive measured data differ by less than 0.1%.

The phase-retrieval geometry uses \(a=0.3\), \(\tau=6\), \(R=1.8\), \(m=10\), and \(k^*=\pi/9\). Ordinary test wavenumbers are \(10\pi/3\), \(50\pi/3\), and \(100\pi/3\). The figures and tables display results on \(\Gamma_1\). For final source recovery, \(\rho=1.4\), 400 pseudo-uniform boundary measurements, and an 800-by-800 evaluation grid are used.

### 6.2 Noise, compute, and hardware

The paper multiplies exact magnitudes by \(1+\epsilon r\), where \(r\) is uniformly distributed on \([-1,1]\), at \(\epsilon=0\), 0.1%, 1%, and 5% for phase retrieval. Final source errors are reported at 1%, 2%, and 5%. The random draws, seeds, number of repetitions, variance across draws, software, libraries, floating-point precision, operating system, processor, accelerator, memory, and wall-clock time are not reported. The experiment therefore demonstrates one reported realization or unspecified aggregation, not a distribution of performance.

### 6.3 Baselines and ablations

There is no external baseline comparing alternative phaseless inverse-source methods, nonlinear optimization, more than two references, different reference amplitudes, or passive-only strategies. Exact complex data function implicitly as an oracle reference for phase-field error. The final Fourier reconstruction is not compared against another phased solver. There is no component ablation of the low auxiliary frequency, determinant-aware placement, number of sectors, measurement density, truncation schedule, or integration stage.

### 6.4 Metrics

Phase retrieval is evaluated with discrete relative L2 error and relative infinity error over boundary samples on \(\Gamma_1\). Final source recovery uses relative L2 error over the 800-by-800 grid in \(V_0\). These metrics are appropriate for global and worst-point field discrepancies, but they do not measure support localization, peak amplitude bias, structural similarity, spectral error, calibration sensitivity, or uncertainty. The denominators use the exact simulated field/source, which is unavailable in real deployment.

### 6.5 Runtime semantics

No runtime claim is quantitatively supported. The authors describe the reconstruction as noniterative and without regularization. Algebraically, Algorithm PR is pointwise and cheap, while Algorithm FM uses numerical continuation and integration. “Noniterative” should not be conflated with constant-time acquisition or negligible computational cost; the measurement count, forward calibration, boundary quadrature, and grid synthesis still scale with problem resolution.

---

## 7. Results: what is reported and what it means

### 7.1 Phase-retrieval accuracy

Table 1 reports relative L2 errors at \(k^*,10\pi/3,50\pi/3,100\pi/3\). With 1% magnitude noise, the errors are 2.95%, 1.22%, 2.16%, and 2.08%. With 5% noise, they rise to 15.5%, 5.12%, 10.6%, and 10.23%. At 0.1% noise, they remain between 0.13% and 0.28%; without added noise, the errors are at floating-point scale.

Table 2 reports relative infinity errors in the same order. At 1% noise the values are 4.60%, 1.42%, 3.32%, and 3.18%; at 5% they are 23.9%, 6.47%, 19.2%, and 18.97%. The low auxiliary frequency is consistently the least favorable in the noisy table even though its determinant has a separate constant lower bound.

**Interpretation:** The results support exact recovery in the noiseless numerical setting and roughly noise-proportional degradation over the tested range. They also show that worst-point error can materially exceed global L2 error.

**Qualification:** One source, sector, geometry, and unspecified random draw cannot establish general robustness. The table does not test the theoretical upper bound sharply, and no condition-number values are reported alongside error.

### 7.2 Final source reconstruction

The paper reports relative L2 source errors of 4.60%, 5.82%, and 8.39% for 1%, 2%, and 5% phaseless noise. Figure 4 shows the surface and contour reconstruction at 1% noise. The authors attribute the relatively moderate 5% source error to noise filtering by integration when estimating Fourier coefficients.

**Interpretation:** Within the chosen smooth synthetic example, error introduced during phase retrieval does not catastrophically compound through the Fourier stage. The source image remains recognizable, and final L2 error grows more slowly than the worst phase-field entries.

**Qualification:** The explanation is not tested by replacing integration, varying source spectrum, isolating Fourier truncation, or comparing recovered phase against exact phase in the final solver. A smooth source is especially favorable to low-order Fourier reconstruction.

### 7.3 Generalization and robustness

The complete primary evidence contains no real measurements, no nonsmooth or multi-component source family, no heterogeneous or lossy medium, no alternative aperture, no missing sensors, no reference misplacement, and no three-dimensional case. The paper notes that related Fourier methods extend to scalar 3D Helmholtz and Maxwell models and identifies those extensions as future work; this is context for feasibility, not evidence that the new phase-retrieval design already generalizes.

---

## 8. Ablations and causal evidence

### 8.1 Reference-source pair

The algebra establishes necessity of two independent equations for two real unknowns and shows how geometry avoids singularity. That is strong analytic causal evidence for the pair as a mechanism. But the experiment does not compare one, two, or more references, nor does it scan placement to connect empirical error to determinant or condition number.

### 8.2 Fourier integration

The authors propose integration as the reason final source error remains moderate at 5% noise. This is a plausible causal hypothesis, not an isolated empirical result. A proper ablation would feed exact phase, recovered phase, phase with matched synthetic error, and spectrally shaped errors into the same Fourier solver, then decompose coefficient and truncation error.

### 8.3 Randomness and statistical evidence

Uniform random multiplicative noise is the only stochastic element reported. There are no seed counts, confidence intervals, hypothesis tests, error bars, effect sizes across trials, or sensitivity distributions. Consequently, numerical entries should be treated as point outcomes. The monotonic trend with \(\epsilon\) is supportive but not a statistical characterization.

---

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| Two reference sources permit unique recovery of the complex boundary field. | Two independent interference equations form a two-by-two Bessel system; Theorem 3.1 bounds its determinant away from zero under explicit parameters. | Strongly supported within the exact model. | Requires coherent calibrated references and prescribed geometry/frequencies. |
| The phase-retrieval formula is stable to measurement perturbations. | Theorem 3.2 derives a relative infinity-norm bound; Tables 1 and 2 show monotone degradation with noise. | Supported for the stipulated bounded relative-noise model. | No calibration, model-mismatch, correlated, additive-floor, or real-sensor noise study. |
| The complete method is noniterative and uses no regularization. | Algorithms PR and FM are presented as direct algebra and Fourier reconstruction. | Accurate as a description of the inverse steps. | Forward FEM generation uses mesh refinement; parameter truncation still regularizes effective spatial bandwidth in a broad numerical sense. |
| Phase recovery enables successful source imaging. | Figure 4 and reported final L2 errors of 4.60%, 5.82%, and 8.39% at 1%, 2%, and 5% noise. | Supported as a proof of concept for one smooth synthetic source. | No baseline, repeated trials, real data, or source-family diversity. |
| Fourier integration is inherently tolerant to large noise. | Final source error at 5% is lower than several phase-field errors; the authors give an integration-filtering explanation. | Plausible but incompletely established. | “Large” is undefined; only one bounded multiplicative setting is shown and no causal ablation is provided. |
| The approach can extend to 3D acoustics and electromagnetics. | Related cited Fourier solvers cover those equations; the paper lists extension as future work. | A reasonable research direction, not a demonstrated result. | New reference geometry, Green functions, conditioning, vector coupling, and acquisition constraints require fresh analysis. |
| The DEP-E record faithfully represents the paper. | Both tracked DEP-E files were read completely and compared with the full arXiv paper's equations, algorithms, tables, figures, limitations, and citations. | No material mismatch found. | The DEP-E is a derived scholarly report and does not replace the canonical paper. |

---

## 10. External views and field context

### 10.1 Predecessor evidence

The Fourier reconstruction stage is not introduced from scratch. The paper explicitly delegates its theoretical justification and further implementation details to Zhang and Guo's 2015 multifrequency Helmholtz inverse-source method.[^fourier-predecessor] This matters for claim allocation: the new contribution is primarily the reference-source phase interface and its stability analysis, while the source inversion reuses an established phased-data pipeline.

### 10.2 Independent publication context

The canonical arXiv record identifies the March 2018 v1 manuscript, four authors, 27 pages, four figures, and the journal DOI.[^arxiv-record] The University of Hertfordshire research portal independently records the same title and authorship and identifies publication in *Inverse Problems*.[^institutional-record] These records corroborate identity and publication status; they do not independently replicate the numerical findings.

### 10.3 Contemporaneous alternatives

The paper's bibliography places the work alongside multifrequency inverse-source algorithms and phaseless inverse-scattering methods. Bao, Lu, Rundell, and Xu's recursive multifrequency method is a phased-data predecessor family, while earlier phaseless work often targets scattering obstacles or coefficients rather than the exact source problem here.[^recursive-context] A fair comparison would distinguish whether an alternative uses active references, assumes far-field versus near-field data, solves for a source versus a medium/obstacle, and has comparable measurement budgets.

### 10.4 Publication, code, and reproducibility status

The reviewed DEP-E includes the complete derived manuscript and attribution but no code repository, environment, meshes, noise seeds, or data files. The complete arXiv paper likewise gives algorithms and parameters but no implementation locator. The journal DOI resolves the publication identity.[^journal-doi] Reproducibility is therefore specification-level: an informed numerical inverse-problems researcher could implement the method, but exact numerical replication would require filling in details, especially those delegated to the prior Fourier paper.

---

## 11. Research notes and critical considerations

### 11.1 Internal consistency

The qualitative narrative, determinant theorems, perturbation analysis, tables, and conclusion are mutually consistent. No material arithmetic mismatch was found in the reported table entries as transcribed by the DEP-E. The distinction between low-frequency and ordinary-frequency determinant arguments is important and preserved. The paper's use of “stable” is mathematically grounded for its phase-retrieval subsystem, while broader full-pipeline robustness remains empirical.

### 11.2 Metric and baseline concerns

Relative L2 and infinity error are transparent but incomplete. Since the exact denominator can be small at some points or frequencies, per-point behavior and phase-angle error would add insight. A condition-number plot would connect geometry to observed noise gain. Baselines should include exact phased data into Algorithm FM, a passive phaseless solver if compatible, alternative reference placements at equal acquisition budget, and a nonlinear least-squares phase solution.

### 11.3 Unsupported or overbroad claims

The central unique-solvability and perturbation claims are properly scoped by assumptions. The weaker areas are rhetorical: “quite accurate,” “moderately small,” “satisfactory,” and “inherently tolerant to large noise” are not operationally defined. The 5% bounded synthetic noise setting is not enough to establish general large-noise tolerance. The proposed 3D and electromagnetic reach remains future work.

### 11.4 Alternative explanations

The final reconstruction's apparent robustness could arise from source smoothness and aggressive Fourier truncation rather than an intrinsically noise-tolerant integration mechanism. The ordinary frequencies' better phase errors could reflect signal amplitude, geometry, or discretization as well as determinant behavior. Results on one sector may be unusually favorable relative to other arcs. Without repeated noise draws, individual tables may partly reflect sample luck.

### 11.5 Failure modes

- Reference-source amplitude or position error makes the right-hand side and matrix inconsistent with the actual intervention.
- Loss of coherence destroys the cross terms that encode phase.
- A heterogeneous or reverberant medium invalidates the free-space Green-function coefficients.
- Geometric constraints may prevent placing reference sources at the prescribed locations.
- Small field magnitudes make relative noise and coefficient scaling unstable.
- Sensor saturation can occur when a reference is strong enough to aid conditioning.
- Fourier truncation may erase sharp source features or merge multiple nearby sources.
- Sparse or partial-aperture sampling may break the Cauchy-data/Fourier stage even if local phase is recovered.

### 11.6 Unresolved questions

- What determinant or singular-value margin minimizes total error when reference amplitude, coherence, and sensor dynamic range are modeled jointly?
- Does performance remain monotone with theoretical conditioning across all sectors, frequencies, and source shapes?
- How much of final robustness comes from integration, source smoothness, or truncation?
- Can a self-calibrating design estimate small reference-position and amplitude errors from redundant probes?
- What measurement budget is needed in three dimensions when reference placement and surface coverage are constrained?

---

## 12. Potential implications

### 12.1 Scientific implications

The work illustrates that inverse-problem identifiability can be improved by controlling the observation process rather than only changing the inverse solver. It also shows the value of aligning an instrumentation choice with an explicit conditioning theorem. Future theory should promote the determinant bound into a full experimental-design objective that accounts for model and calibration uncertainty.

### 12.2 System-design implications

A practical system should log every reference state, calibration coefficient, geometry estimate, field magnitude, matrix determinant or singular value, and reconstructed complex sample. These intermediate artifacts make failures diagnosable and allow the downstream solver to reject weakly conditioned data. Measurement planning should include dynamic-range and coherence constraints, not just mathematical nonsingularity.

### 12.3 Broader implications

The intervention-certified observability pattern transfers cautiously to optical intensity imaging, array processing, electromagnetic sensing, and other systems where a known probe can mix with an unknown complex signal. The portable lesson is methodological, not a claim that the exact Bessel construction transfers unchanged.

---

## 13. New hypotheses derived from the paper

These are reviewer inferences, not established findings.

### Hypothesis 1: Conditioning predicts realized phase-error amplification

**Proposition:** Across valid reference placements, the realized ratio of complex-field error to magnitude-noise level will track the inverse smallest singular value of the local two-by-two matrix more closely than frequency alone.

**Motivating evidence:** The determinant is central to both solvability and the perturbation proof, while table errors vary materially by frequency.

**Predicted observation:** A placement sweep will show monotone or rank-consistent growth in median and upper-quantile error as the smallest singular value decreases.

**Falsifying observation:** Error remains uncorrelated with conditioning after controlling for field magnitude, reference amplitude, and discretization.

**Minimum test:** Simulate at least 100 noise draws over a grid of valid placements and report condition numbers, error distributions, and partial correlations per sector and frequency.

### Hypothesis 2: Redundant references enable self-calibration

**Proposition:** Using three or more reference states will permit joint estimation of the complex field and small reference-amplitude or position biases, improving robustness under realistic calibration error despite increased acquisition cost.

**Motivating evidence:** Two references exactly determine two field quadratures and leave no redundancy for inconsistency detection.

**Predicted observation:** An overdetermined robust estimator will reduce worst-sector error under injected calibration drift while matching the two-reference method in the ideal setting.

**Falsifying observation:** Additional references do not identify calibration bias or worsen error after accounting for equal total measurement energy and time.

**Minimum test:** Compare two-, three-, and four-reference designs under controlled amplitude, position, and coherence perturbations with equalized acquisition budgets.

### Hypothesis 3: Smooth-source truncation explains much of the apparent large-noise tolerance

**Proposition:** The favorable 5% final reconstruction error depends substantially on the smooth, low-spatial-frequency source and the truncation schedule rather than on integration alone.

**Motivating evidence:** The test source is smooth and Algorithm FM explicitly truncates Fourier coefficients.

**Predicted observation:** Piecewise or sharply localized sources will show a larger increase in final error at the same phase-field error, especially near edges and high-frequency coefficients.

**Falsifying observation:** Matched-energy smooth and nonsmooth source families show similar source-error distributions and spectral error profiles.

**Minimum test:** Evaluate smooth Gaussian mixtures, discontinuous supports, multipoles, and clustered sources using matched noise draws and report coefficient-wise error.

---

## 14. Deployment and governance considerations

### 14.1 Appropriate use

The method is appropriate as a research design or controlled-laboratory prototype when coherent reference sources can be placed and calibrated, the propagation model is close to homogeneous 2D Helmholtz physics, and conditioning diagnostics are recorded. It may also serve as a benchmark mechanism for active phase recovery.

### 14.2 Poor fit and failure modes

It is a poor fit when sensors are passive-only, reference coherence cannot be maintained, geometry is uncertain, the medium is strongly heterogeneous, data are partial-aperture, or errors are dominated by systematic calibration rather than bounded magnitude noise. It should not be deployed on safety-critical localization based solely on the reported synthetic example.

### 14.3 Required safeguards

1. Calibrate reference amplitude, phase coherence, and position before each acquisition and archive uncertainty estimates.
2. Compute and threshold local matrix conditioning; preserve rejected sectors rather than silently interpolating them.
3. Validate on representative real or high-fidelity data with model mismatch, repeated trials, blinded sources, and predefined acceptance criteria.
4. Separate phase-retrieval, continuation, truncation, and spatial reconstruction errors in monitoring.
5. Version the forward model, numerical environment, meshes, quadrature, frequencies, and raw magnitude observations.

---

## 15. Replication and falsification agenda

### 15.1 Highest-priority unresolved result

The highest-priority test is whether the analytic conditioning certificate predicts robust performance under calibration and model mismatch. Pre-register reference placement sweeps, multiple source families, at least 100 independent noise draws, amplitude and position bias levels, and both relative field and source errors. Success requires the designed placement to outperform equal-budget alternatives in median and 95th-percentile error; failure is no advantage or reversed ranking once mismatch is introduced.

### 15.2 Reproduce the full pipeline

Archive the exact source formula, FEM mesh sequence, PML parameters, convergence traces, boundary points, noise seeds, reference geometry, combined magnitudes, per-sample matrices, determinants, recovered complex fields, Cauchy data, Fourier coefficients, truncation index, reconstructed grids, and metric scripts. First reproduce noiseless machine-precision phase retrieval, then Tables 1 and 2, then Figure 4 and the three final L2 errors.

### 15.3 Normalize evaluation

Use a common suite of smooth, nonsmooth, sparse, extended, and multi-component sources. Equalize measurement configurations, reference energy, sensor count, and frequency set across methods. Report L2, infinity, phase-angle, support, localization, coefficient-wise, and calibration errors with confidence intervals. Provide runtime and hardware separately for acquisition, phase retrieval, continuation, and reconstruction.

### 15.4 Test the proposed mechanism directly

Sweep reference placements through predicted determinant margins and measure the full singular-value spectrum. Compare empirical error amplification against theorem-derived and linearized predictions. Replace recovered phase with controlled synthetic phase errors to isolate downstream filtering. Test whether integration suppresses independent high-frequency error but fails for coherent low-frequency bias, as the mechanism would predict.

### 15.5 Test realistic shifts and alternatives

Add sensor floors, additive noise, correlated drift, saturation, missing samples, phase decoherence, location bias, amplitude bias, uncertain sound speed, weak heterogeneity, partial aperture, and boundary-shape error. Compare direct two-reference inversion, redundant least squares, robust regression, nonlinear joint calibration, and compatible passive phaseless baselines. Only after those tests should the design be extended to three-dimensional scalar and vector electromagnetic models.

---

## 16. Durable restatement

> The paper's lasting contribution is a way to manufacture the missing phase information required by an acoustic inverse-source solver: add two known coherent point sources, observe their interference with the unknown field, and choose their geometry so the resulting two-equation system is provably invertible. Under the stated two-dimensional Helmholtz model, this converts magnitude data into complex boundary data with an explicit perturbation bound; a prior multifrequency Fourier method then reconstructs the source. Synthetic results support feasibility but do not resolve calibration, model-mismatch, statistical, real-data, or three-dimensional questions.

What should be remembered is the coupling of intervention and certification. The references are not auxiliary decoration, and the determinant theorem is not an isolated mathematical appendix. Together they create an observable interface for an existing downstream method. The next scientific step is to test whether that interface stays reliable when the reference system and propagation model are imperfect.

---

## Appendix A. Complete table and figure coverage ledger

### Source DEP-E inventory

1. **`README.md`:** Read from beginning to end. Accounted for classification, context, two-file inventory, summary, insights, related DEP records, arXiv and DOI identity, repository provenance, and attribution. It is a repository intake wrapper, not primary experimental evidence.
2. **`acoustic_phase_retrieval_manuscript.md`:** Read from beginning to end. Accounted for bibliographic identity, executive summary, problem formulation, reference-source equations, parameter geometry, determinant and perturbation results, Algorithms PR and FM, numerical setup, both tables, all figures, limitations, future work, related concepts, and references.

### Paper sections and equations

1. **Introduction and problem formulation:** covered the Helmholtz model, compact source, radiation condition, phaseless measurement loss, prior-work positioning, and two-stage contribution.
2. **Reference-source phase retrieval:** covered sector partition, Green-function probes, interference equations, two-by-two recovery matrix, parameter rules, and Algorithm PR.
3. **Stability analysis:** covered Bessel asymptotics/series strategy, Theorem 3.1 ordinary- and low-frequency determinant bounds, perturbed right-hand sides, and Theorem 3.2 relative field-error estimate.
4. **Fourier method:** covered auxiliary Cauchy data, coefficient estimation, truncation, source synthesis, and Algorithm FM; deeper implementation details are explicitly delegated by the paper to prior work.
5. **Numerical examples, conclusion, acknowledgements, references:** covered forward FEM/PML generation, mesh convergence, noise rule, source, geometry, metrics, results, extension claims, funding, and cited predecessor context.

### Tables

1. **Table 1, relative L2 phase-retrieval errors:** all four frequencies and four noise levels were inspected. It demonstrates machine-precision noiseless recovery and increasing global error with noise; no repeated-trial uncertainty is supplied.
2. **Table 2, relative infinity phase-retrieval errors:** all four frequencies and four noise levels were inspected. It shows larger worst-point amplification, especially for the auxiliary frequency; no location-wise error plot or confidence interval is supplied.

### Figures

1. **Figure 1, geometry of the inverse-source and reference configuration:** establishes source support, measurement circle, sectorization, and reference placement; it is schematic rather than empirical evidence.
2. **Figure 2, exact mountain-shaped source:** supplies surface and contour views of the single synthetic ground truth; its smoothness limits generalization.
3. **Figure 3, reference geometry on the first sector:** contrasts an ordinary wavenumber and the auxiliary low-frequency placement; it visualizes the designed intervention but does not show conditioning values.
4. **Figure 4, source reconstruction at 1% noise:** provides surface and contour output for the final pipeline; only one noise level and source are visualized.

---

## Appendix B. Source and evidence notes

### Primary reviewed artifact

The primary repository object is `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval` at commit `e149ddfa04aaff808e7d3602c5bf02691257a212`. It contains exactly two tracked Markdown files, both read completely. The canonical arXiv v1 PDF was inspected as a complete 27-page paper, including every named section, equation sequence, both algorithms, both theorems, two tables, four figures, conclusion, acknowledgements, and bibliography.[^source-paper]

### External primary sources

- https://arxiv.org/abs/1803.11323v1 — canonical version metadata.
- https://arxiv.org/pdf/1803.11323v1 — complete authorized paper.
- https://doi.org/10.1088/1361-6420/aaccda — persistent journal record.
- https://researchprofiles.herts.ac.uk/en/publications/retrieval-of-acoustic-sources-from-multi-frequency-phaseless-data — institutional bibliographic record.
- https://doi.org/10.1088/0266-5611/31/3/035007 — DOI for the prior Fourier method used downstream.

### Evidence boundary

Statements labeled as paper reports or authors' arguments derive from the complete primary paper. Descriptions of the DEP-E record derive from both tracked repository files. Reviewer inference includes the “intervention-certified observability” framing, alternative explanations, failure modes, implications, and hypotheses. Proposed tests are agendas, not observed results. No source document was committed. No code was available or inspected. No calculation, theorem proof, finite-element simulation, noise draw, table, figure, or reconstruction was independently rerun or reproduced. The review checks internal coherence and evidentiary scope; it is not an independent verification of correctness.

---

## Footnotes

[^source-paper]: Deyue Zhang, Yukun Guo, Jingzhi Li, and Hongyu Liu, “Retrieval of acoustic sources from multi-frequency phaseless data,” arXiv:1803.11323v1, 27 pages, 4 figures, https://arxiv.org/abs/1803.11323v1 and https://arxiv.org/pdf/1803.11323v1.

[^fourier-predecessor]: Deyue Zhang and Yukun Guo, “Fourier method for solving the multi-frequency inverse source problem for the Helmholtz equation,” *Inverse Problems* 31, 035007 (2015), https://doi.org/10.1088/0266-5611/31/3/035007. The reviewed paper identifies this as the basis for Algorithm FM.

[^arxiv-record]: Canonical arXiv abstract and version record, https://arxiv.org/abs/1803.11323v1.

[^institutional-record]: University of Hertfordshire Research Profiles, publication record for the paper, https://researchprofiles.herts.ac.uk/en/publications/retrieval-of-acoustic-sources-from-multi-frequency-phaseless-data.

[^recursive-context]: Gang Bao, Songting Lu, William Rundell, and Boxi Xu, “A recursive algorithm for multi-frequency acoustic inverse source problems,” *SIAM Journal on Numerical Analysis* 53 (2015), 1608–1628, DOI record https://doi.org/10.1137/140975031. This is contextual predecessor evidence, not an evaluated baseline in the reviewed paper.

[^journal-doi]: Institute of Physics journal DOI for the reviewed paper, https://doi.org/10.1088/1361-6420/aaccda.
