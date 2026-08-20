# Geometry-Matched Online Detection in Delay-Doppler Space

## A detailed review and independent re-conceptualization of “2D-RC: Two-Dimensional Neural Network Approach for OTFS Symbol Detection”

**Source paper:** Jiarui Xu, Karim Said, Lizhong Zheng, and Lingjia Liu, arXiv:2311.08543v2, revised 25 January 2024.[^paper]
**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS`[^source-dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-1D87E17B`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E review plus complete canonical article reconstruction, including appendices, figures, tables, equations, and reported experiments
**Reproduction boundary:** paper and source record inspected; no code was executed, no simulation was rerun, and no result was independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; files copied: no; new derived DEP-A data generated: yes

---

## Executive assessment

### The paper in one sentence

The paper replaces a time-sequence reservoir detector for orthogonal time frequency space modulation with one two-dimensional reservoir whose circular padding and row-column recurrence mirror the channel interaction in delay-Doppler space.

### The deeper idea

The contribution is a form of inductive-bias accounting. Reservoir computing economizes training by freezing the recurrent weights and fitting only a linear readout. That economy is valuable when pilots are scarce, but it also leaves architecture responsible for arranging information into a learnable state. The paper's 2D construction makes the arrangement match the physical domain: observations are windowed in delay and Doppler, boundaries wrap circularly, and state travels across both axes. The least-squares readout can then exploit a representation in which pilots and data experience more similar transformations.

### Bottom-line judgment

The technical story is coherent and unusually traceable. The complete paper defines the system variants, derives preprocessing and state updates, supplies complexity expressions, and evaluates QPSK, 16-QAM, mobility, coding, pilot patterns, and model-based baselines. Reported evidence supports “better under the tested simulations,” particularly against the earlier 1D reservoir and estimated-CSI detectors. It does not establish hardware readiness, universal complexity superiority, or robustness to real radio impairments. No official runnable artifact was validated in this review.

### Principal strengths

- Architecture is tied to a specific channel symmetry rather than generic deep-learning capacity.
- Training remains closed-form for the readout and uses only pilots within the current subframe.
- The evaluation spans two OTFS variants, modulation orders, mobility, channel coding, and complexity.
- The paper includes fractional delay/Doppler derivations and a pilot-pattern appendix.

### Principal qualifications

1. Evidence is simulation-based and was not independently rerun.
2. Complexity comparisons depend on counted operations, dimensions, and whether estimation/training costs are included.
3. Some equation symbols are imperfect in arXiv HTML; the structural reading is stronger than a character-perfect formula transcription.

## 1. The problem the paper is actually solving

OTFS transmits symbols on a two-dimensional delay-Doppler grid and transforms them into the time-frequency and then time domains. In high-mobility settings, Doppler spread can make conventional OFDM detection difficult. OTFS is attractive because a delay-Doppler symbol experiences the full time-frequency channel, but detection still requires coping with interference, channel variation, pilots, and imperfect channel state information.

Model-based equalizers exploit analytical channel structure but depend on a sufficiently accurate model and CSI estimate. Message passing, LMMSE, and iterative LSMR variants trade accuracy and complexity differently. Offline neural detectors can learn mappings without explicit CSI, yet require large training sets and may fail when deployment conditions differ. The paper's prior 1D reservoir approach trains online from a small pilot allocation, but flattens the problem into time and deploys multiple reservoirs to track change.

The research question is therefore specific: can one online learner retain the small-data, cheap-training benefits of reservoir computing while using the circular two-axis structure that defines the OTFS interaction? The paper's answer is 2D-RC.

## 2. Formal and technical reconstruction

### 2.1 Signal model and assumptions

An OTFS subframe contains a grid with delay and Doppler dimensions. Modulated QAM symbols undergo an inverse symplectic finite Fourier transform into the time-frequency domain, then a Heisenberg transform into time samples. At the receiver, the Wigner transform and symplectic Fourier transform reverse those stages. The paper assumes practical rectangular pulse shaping and considers a multipath time-varying channel whose paths have gains, delays, and Doppler shifts.

Two framing variants matter. RCP-OTFS attaches one cyclic prefix to the whole subframe and offers higher spectral efficiency. CP-OTFS places a cyclic prefix on every OFDM symbol and is easier to overlay on existing OFDM structures. The paper gives integer-delay/integer-Doppler input-output forms in the main text and fractional forms in Appendix A. Those derivations are part of the guarantee boundary: the network is not claimed to make the physics unnecessary; it is designed around the physics.

### 2.2 From 1D reservoir to 2D reservoir

In a conventional reservoir, fixed random input and recurrent matrices transform a sequence into internal states. The spectral radius is chosen below one to reduce sensitivity to initialization. Only an output matrix is learned, normally through least squares. Windowing supplies short-term context, and padding plus a searched forget length discards transient states.

The 2D version operates on the delay-Doppler grid. First, phase compensation removes a system-dependent phase term so a common circular representation can serve RCP and CP variants. Second, a rectangular neighborhood is collected around each grid location. Third, circular padding wraps that neighborhood across both axes. Unlike zero padding, the wrap respects how delay-Doppler interaction crosses boundaries.

The reservoir then updates a state at each grid coordinate from the local input and neighboring state flows. Separate fixed matrices propagate information along row, column, and diagonal directions. Their combined effect is a two-dimensional filter over the grid rather than recurrence along one flattened sequence. An extended state concatenates the learned representation and the input features; the trainable output matrix maps that state to symbol estimates.

### 2.3 Training objective

Known pilot positions define a mask. For candidate delay and Doppler forget lengths, the state tensor is truncated, pilot-masked, and vectorized. The output weights have a closed-form least-squares solution using a pseudoinverse. The algorithm searches for forget lengths that minimize pilot loss, with a staged Doppler-then-delay search to avoid exhaustively evaluating every pair.[^method]

This is important for claim calibration. “Online learning” here does not mean gradient-based continual training of the recurrent dynamics. The fixed reservoir is sampled once; the per-subframe work estimates a linear readout and transient lengths from current pilots. The adaptation capacity is consequently bounded and interpretable.

### 2.4 Inference

After selecting the forget lengths and fitting the readout, the same preprocessing and reservoir state construction are applied across the received grid. The trained output matrix produces symbol estimates at data positions. The method uses one 2D reservoir for the subframe rather than partitioning the time-domain signal across multiple 1D reservoirs.

### 2.5 Notation and implementation audit

The canonical HTML exposes the equation sequence and structural definitions, but reports known conversion limits for an unsupported math package. Several symbols appear blank in extracted text. That prevents a trustworthy character-for-character restatement of dimensions and indices here. The relation among prose, algorithm, and equations is nevertheless consistent: window and forget lengths are two-dimensional, states depend on fixed directional matrices, pilot masking selects training targets, and the readout is least-squares. A reproduction should use PDF or TeX source to avoid HTML symbol loss.

## 3. Architecture and information flow

The data flow is: receive time samples; transform to delay-Doppler space; compensate phase; form two-dimensional windows; circularly pad; compute fixed reservoir states across both axes; concatenate extended states; mask pilot positions; solve the readout; choose forget lengths; and predict data symbols. For CP-OTFS, the paper includes variant-specific preprocessing but retains the common detector.

Information is allocated spatially rather than by a deep trainable hierarchy. Memory is implicit in directional recurrence and window size. Compute is spent on state construction and a pseudoinverse rather than iterative backpropagation. The approach assumes that a random feature map aligned with channel geometry exposes a sufficiently linear relation to transmitted symbols.

The method does not certify correct symbols. It outputs estimates whose quality is measured statistically. Any deployed receiver would still need conventional error detection, channel coding, signal-quality monitoring, and fallbacks.

## 4. Experimental design and evidence reconstructed

### 4.1 Data generation and channel

The evaluation uses numerical OTFS simulations and a 3GPP 5G NR clustered delay line channel with the CDL-C profile. The paper specifies carrier, subcarrier spacing, delay spread, mobility, and grid configuration, though some symbols are lost in the HTML conversion. Pilot overhead is held equal across compared approaches; the text states that 48 delay grids are occupied for both blockwise and spike patterns in the default configuration.[^experiments]

This is synthetic channel evidence, not over-the-air data. The channel model gives reproducible structure if all parameters and random seeds are preserved, but does not cover oscillator drift, nonlinear front ends, synchronization errors, quantization, antenna effects, or real scheduling interactions unless explicitly simulated.

### 4.2 Baselines

The major comparisons are the earlier multi-reservoir 1D-RC; LMMSE with estimated CSI; message passing with estimated CSI; iterative LSMR with estimated CSI; and an OFDM reference. The framing is partly asymmetrical: 2D-RC learns from pilots without explicit CSI, while model-based baselines receive an estimated channel produced from pilots. That is a legitimate systems comparison when pilot budgets are equal, but it does not isolate detector quality from channel-estimation quality.

The paper also varies the number of 1D reservoirs. Because 2D-RC uses one network, its operational simplicity is real, but “one network” does not by itself imply less compute: the 2D state is larger and the paper reports higher complexity than 1D-RC.

### 4.3 Metrics

Training and testing normalized mean square error guide hyperparameter analysis. Bit error rate and block error rate assess detection. Complexity is expressed in complex multiplications for training/channel estimation plus testing/detection over one subframe. These metrics answer different questions. NMSE on pilot reconstruction is not a substitute for BER. BER is per bit, while BLER measures whether an encoded block contains an error. Complexity counts do not equal measured latency or energy.

### 4.4 Configurations

The paper covers RCP-OTFS and CP-OTFS, QPSK and 16-QAM, different velocities, pilot structures, network/window sizes, and LDPC coding at a stated rate of 0.3125. Hyperparameter plots show a training-testing tradeoff: increasing reservoir capacity and window size can lower training error while testing error eventually reflects overfitting or unnecessary complexity.

Hardware runtime is not the primary evidence. Operation counts are useful for scale comparison but omit memory traffic, parallelism, numerical libraries, and implementation quality.

## 5. Results: what is reported and what it means

Across the plotted simulations, the paper reports that 2D-RC improves BER over 1D-RC for both QPSK and 16-QAM and that the advantage grows at higher mobility. Its proposed explanation is reduced train-test mismatch: in the delay-Doppler grid, pilot and data regions experience similar structural impairments, whereas a time-domain partition can see different channel conditions as speed rises.

Against model-based baselines using estimated CSI, 2D-RC is reported to outperform LMMSE, MPA, and LSMR under the tested OTFS variants. This supports a narrower claim: joint pilot-to-symbol mapping can be more robust than a pipeline whose channel estimate is imperfect. It does not show that the learned detector beats a model-based method with oracle CSI, nor that it transfers beyond the simulated distribution.

For coded CP-OTFS with QPSK and LDPC, the paper reports roughly a 2–3 dB gain over conventional estimated-CSI approaches at its target BLER.[^coded] The target symbol is lost in HTML extraction, so this review preserves the magnitude but does not invent the missing threshold. The complexity section reports lower counts than MPA and LSMR even after including online training, higher counts than 1D-RC, and better detection than 1D-RC.

The bottom line is “supported under tested simulation conditions.” The evidence is broad within the chosen simulator, but not statistically characterized with independent training seeds, confidence intervals, or hardware measurements in the inspected text.

## 6. Ablations and causal evidence

The paper provides sensitivity and comparison evidence, but not a perfectly isolated component ablation. It varies neuron count and window size, showing that capacity affects pilot fit and test error. It compares one 2D reservoir with multiple 1D reservoirs and examines mobility, supporting the proposed train-test mismatch mechanism. It also compares variants and pilot patterns.

The key missing causal tests would remove phase compensation, replace circular padding with zero padding, flatten the 2D state while holding parameter and compute budgets fixed, and separately remove row, column, and diagonal recurrence. Such ablations would determine which structure produces the gain. The current evidence strongly associates the whole geometry-matched package with performance; it is less precise about individual components.

Random initialization is another underdeveloped causal factor. Reservoir matrices are random, but the paper evidence visible in this review does not establish how many reservoir seeds were used or report intervals over them. A result can be stable across channel noise seeds yet sensitive to the frozen reservoir draw.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| 2D-RC embeds circular delay-Doppler structure. | Method equations, preprocessing, and architecture figures. | Strongly supported. | Exact symbol transcription requires PDF/TeX because HTML drops notation. |
| It trains online from limited pilots. | Pilot mask and least-squares readout procedure. | Strongly supported. | Only the readout and forget lengths adapt online. |
| One 2D reservoir outperforms multiple 1D reservoirs. | Simulation curves across variants and modulation. | Supported under tested conditions. | Budget matching and random reservoir variance deserve more detail. |
| It outperforms model-based detectors. | BER/BLER comparisons with estimated-CSI LMMSE, MPA, and LSMR. | Supported in the simulator. | Does not isolate detector from channel estimator or compare oracle CSI. |
| It has lower complexity than MPA and LSMR. | Complex-multiplication analysis. | Supported for the paper's dimensions and accounting. | Not a measured latency, memory, or energy result. |
| It generalizes better. | Cross-variant, modulation, and mobility plots. | Promising but limited. | All tests remain within related synthetic channel families. |
| It is ready for practical receivers. | No direct deployment evidence. | Not established. | Requires code, OTA data, timing, calibration, and safety fallback. |

## 8. External primary-source context

The arXiv record identifies version 2, four authors, the signal-processing category, and a CC BY 4.0 license. The complete HTML article contains introduction, reservoir preliminaries, OTFS system model, introduced method, complexity, numerical experiments, conclusion, fractional delay/Doppler derivation, and pilot appendix.[^paper] The DOI provides a stable identifier.[^doi]

The paper's related-work context situates 2D-RC among analytical equalizers, message passing, iterative cross-domain detectors, offline neural detectors, and earlier online RC. This supports a measured novelty statement: the work is not the first OTFS detector or first online reservoir detector; its contribution is the two-dimensional, circular, delay-Doppler-specific reservoir construction.

No official code link was established in the directly reviewed canonical article. Therefore artifact status is “paper available and inspectable,” not “runnable” or “reproduced.”

## 9. Independent re-conceptualization: coordinate-aligned random features

Strip away the wireless terminology and the method is coordinate-aligned random feature regression. A physical process has two coupled periodic axes. Fixed random operators propagate context along those axes, while a small supervised sample fits a linear output. The architecture succeeds if its coordinates make local training evidence representative of unobserved locations.

This view explains the reported mobility advantage. More speed increases interference, but the pilot and data points remain embedded in the same delay-Doppler interaction. The 1D time partition changes what each reservoir sees, increasing mismatch. The 2D design pays more compute to reduce representational mismatch.

**Boundary of the analogy:** the reservoir is recurrent rather than a generic static random-feature map; OTFS transforms and phase compensation are domain-specific; and circularity may be approximate under practical impairments. The analogy predicts that gains should shrink when the assumed wrap symmetry is broken or when pilots are placed in a way that fails to cover the relevant interference neighborhood.

The transferable design principle is to spend fixed capacity on the coordinate system that preserves the process invariances before increasing trainable depth.

## 10. Research notes and critical considerations

Pilot fairness is necessary but not sufficient. An estimated-CSI baseline allocates pilot information to estimation and then detection; 2D-RC allocates it directly to a discriminative map. A stronger comparison would include joint model-based inference and an oracle-CSI ceiling.

The word “generalization” should be bounded. The paper varies system settings, but online retraining occurs every subframe. This is rapid adaptation within a family, not evidence of a frozen model generalizing to arbitrary radios.

Operation counts omit numerical stability. Pseudoinverses can become ill-conditioned with correlated states or too few pilots. Regularization, precision, and conditioning diagnostics should be reported.

Reservoir randomness matters. A chosen spectral radius and sparse matrices may interact with grid dimensions. Multiple draws, checkpointing of matrices, and sensitivity intervals are needed for exact reproducibility.

The paper gives a compelling mechanism for simulated channels, yet deployment could violate circular assumptions through synchronization errors, guard intervals, nonlinear amplification, or fractional effects outside the modeled range. Appendix A improves fidelity by treating fractional delay and Doppler; it does not exhaust hardware effects.

## 11. Implications

Scientifically, the work demonstrates that inductive bias can improve small-sample online learning without training a large network. For systems design, it suggests separating expensive representational structure from cheap online calibration. For deployment, it suggests a receiver that can adapt per subframe, but only if state construction, pseudoinverse stability, and timing fit the radio budget.

Governance is not materially a social-policy issue for the core algorithm, but operational safeguards are material. Appropriate use requires deterministic channel-coding validation, measured signal quality, conservative fallbacks, per-subframe condition numbers, reservoir seed provenance, and out-of-distribution monitoring. Poor-fit conditions include pilot corruption, unmodeled interference, severe synchronization error, and hardware unable to meet latency.

## 12. New hypotheses derived from the paper

These are reviewer hypotheses, not established findings.

### Hypothesis 1: symmetry violation predicts the 2D advantage

**Proposition:** the performance margin over 1D-RC is governed by how closely the effective channel preserves circular delay-Doppler locality.
**Predicted observation:** controlled boundary distortions reduce the margin monotonically.
**Falsifier:** 2D-RC retains the same advantage when circular structure is destroyed but all other factors are fixed.
**Minimum test:** simulate increasing boundary and synchronization perturbations with matched pilots and reservoir seeds.

### Hypothesis 2: conditioning is the hidden capacity limit

**Proposition:** increasing windows or neurons eventually harms test performance because the pilot-masked state matrix becomes poorly conditioned relative to the sample count.
**Predicted observation:** condition number predicts error better than raw state dimension.
**Falsifier:** condition number and test error remain unrelated across pilot budgets.
**Minimum test:** log singular spectra, readout norm, and BER over capacity sweeps.

### Hypothesis 3: direct learning wins mainly when CSI estimation is the bottleneck

**Proposition:** 2D-RC's advantage over model-based pipelines grows with channel-estimation error and shrinks toward an oracle-CSI detector.
**Minimum test:** sweep estimator quality while holding data, compute, and detector configuration fixed.
**Falsifier:** the advantage is unchanged between poor and oracle CSI.

## 13. Replication and falsification agenda

First, recover the PDF or source equations and build a configuration ledger containing every grid dimension, channel parameter, pilot pattern, reservoir distribution, spectral radius, seed, forget-length set, and baseline setting. Archive frozen reservoir matrices because they are part of the model.

Second, reproduce one uncoded CP-OTFS QPSK curve. Verify the input-output transformation and pilot mask independently before comparing BER. Success requires agreement within a preregistered tolerance across multiple channel and reservoir seeds.

Third, reproduce the coded BLER experiment and record the missing target threshold from the primary PDF. Count decoder cost consistently. Compare estimated CSI, oracle CSI, and direct learning.

Fourth, run component ablations: no phase compensation, zero rather than circular padding, flattened state, and removal of each directional transition. Match state size and operation budget where possible.

Fifth, build hardware-in-loop or OTA tests with synchronization and front-end impairment sweeps. Measure end-to-end latency, memory, energy, and failure recovery—not only multiplication counts. Archive error cases with pilot locations and state conditioning.

## 14. Durable restatement

> 2D-RC is a per-subframe linear-readout learner whose fixed recurrent representation is organized around circular delay-Doppler geometry. In the paper's simulations, this alignment uses pilots more effectively than a time-flattened reservoir and outperforms several estimated-CSI detectors, at a complexity above 1D-RC but below selected iterative baselines.

The result should be remembered as evidence for geometry-matched online representation, not as universal proof that learning replaces channel models.

## Appendix A. Complete table and figure coverage ledger

### Tables

1. **Table I, 2D-RC notation:** defines two-axis windows, forget lengths, state and weight objects; HTML symbol loss requires PDF confirmation.
2. **Complexity tables:** compare complex multiplications for training/estimation and testing/detection; interpreted as operation counts, not wall-clock latency.
3. **Configuration/parameter material:** establishes common pilot overhead and simulation settings.

### Figures

1. **Figures 1–2:** prior 1D reservoir and its windowing; establish the baseline representation.
2. **Figures 3–5:** OTFS pipeline, system variants, and pilot patterns; define the physical and supervision layout.
3. **Figures 6–7:** 2D windowing/padding and reservoir structure; carry the central architectural claim.
4. **Figures 8–9:** train/test NMSE versus capacity; show fit-generalization tradeoff.
5. **Figures 10–14:** BER across reservoirs, variants, modulation, mobility, and detectors; support the empirical claim under simulation.
6. **Figure 15:** coded BLER; supports the reported 2–3 dB comparison at the paper's target.
7. **Appendix figures/material:** fractional-delay/Doppler relationships and OFDM pilot pattern; account for boundary cases used by the main formulation.

### Equations and algorithms

- Equations 1–7 reconstruct prior 1D reservoir state, readout, loss, and inference.
- Equations 8–16 define OTFS transformations and system variants.
- Equations 17–28 define 2D preprocessing, directional state, output, masked least squares, forget search, and testing.
- Complexity expressions and Equations 29–41 cover operation accounting and fractional channel derivation.
- Every central equation family was inspected for role and direction; exact missing glyphs were not guessed.

## Appendix B. Source and evidence notes

### Primary reviewed artifact

The complete two-file DEP-E record was read. The canonical arXiv HTML version 2 contains 496 extracted lines, all main sections, references, Appendix A, and Appendix B. Its license is CC BY 4.0. The article ends cleanly and identifies the four authors and version.

### External primary sources

- https://arxiv.org/abs/2311.08543
- https://arxiv.org/html/2311.08543
- https://doi.org/10.48550/arXiv.2311.08543

### Evidence boundary

Paper reports are labeled as such. Direct inspection covered the full article structure, method, experiments, figures/tables, conclusion, and appendices. Reviewer inference is confined to mechanism, failure modes, and hypotheses. No code was found or run; no data were regenerated; no BER or BLER result was independently reproduced.

## Footnotes

[^paper]: Canonical paper and complete HTML: https://arxiv.org/abs/2311.08543 and https://arxiv.org/html/2311.08543
[^method]: Training and 2D state construction are described in the introduced-approach section of https://arxiv.org/html/2311.08543
[^experiments]: Numerical-experiment settings and pilot accounting: https://arxiv.org/html/2311.08543
[^coded]: The coded CP-OTFS result is reported around Figure 15 in https://arxiv.org/html/2311.08543
[^doi]: Persistent identifier: https://doi.org/10.48550/arXiv.2311.08543
[^source-dep]: Immutable reviewed repository record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS
