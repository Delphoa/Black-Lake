---
title: "Irregular Clipped SR - DEP-E"
generated_at: "2026-07-11"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of irregular clipping distributions for finite-length sparse regression codes decoded with OAMP."
source_status: "URLs only; local readme and PDF inspected but not redistributed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-11"
temporal_cutoff: "Sources inspected through 2026-07-11"
primary_url: "https://arxiv.org/abs/2106.01573"
stable_identifier: "arXiv:2106.01573; DOI:10.1109/ITW48936.2021.9611458"
confidence_summary: "High for source identity and reported method; medium for empirical generality because numerical experiments were not reproduced and official code was not found."
safety_scope: "non-sensitive communications research, synthetic evaluation, and bounded implementation planning"
distribution_notes: "No source files redistributed; public artifacts omit local execution context."
---

# Irregular Clipped SR - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Irregularly Clipped Sparse Regression Codes* | Primary research object | Local and public PDF | arXiv:2106.01573v1 | https://arxiv.org/pdf/2106.01573v1; local path withheld | Redistribution permission not established; local copy not deposited. | 2026-07-11 | Six-page full text inspected |
| S2 | arXiv metadata record | Primary metadata | Atom/HTML | arXiv:2106.01573v1 | https://arxiv.org/abs/2106.01573 | Public metadata; primary category cs.IT. | 2026-07-11 | Inspected |
| S3 | IEEE ITW publication record | Bibliographic metadata | DOI/Crossref | 10.1109/ITW48936.2021.9611458 | https://doi.org/10.1109/ITW48936.2021.9611458 | Bibliographic use; publisher terms apply. | 2026-07-11 | Crossref metadata inspected |
| S4 | Local archive readme | Selection provenance | Markdown | arXiv:2106.01573 | Path withheld | Not redistributed. | 2026-07-11 | Inspected |
| S5 | Black-Lake README | Repository authority | Markdown | default branch at access date | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository policy, not research evidence. | 2026-07-11 | Live file inspected |
| S6 | Black-Lake-Data README | Related repository authority | Markdown | default branch at access date | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Repository policy, not research evidence. | 2026-07-11 | Live file inspected |
| S7 | 2D-RC OTFS manuscript | Related DEP artifact | Markdown | DEP-E-20260709-2D-RC OTFS | `Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | Generated synthesis used as related context only. | 2026-07-11 | Inspected |
| S8 | Machine Learning Optimal QEC Thresholds finding | Related DEP entry | Markdown | DEP-20260625-Tech Intel 0102 | `Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 0102/daily_research_findings_2026-06-25_0102.md` | Generated findings artifact; primary source basis separately checked. | 2026-07-11 | Inspected |
| S9 | Directed Graph Topology Inference finding | Related DEP entry | Markdown | DEP-20260630-Tech Intel 0104 | `Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md` | Generated findings artifact; primary source basis separately checked. | 2026-07-11 | Inspected |

The paper is by Wencong Li, Lei Liu, and Brian M. Kurkoski. arXiv records publication on 2021-06-03 and labels it as six pages, four figures, submitted to IEEE ITW 2021. Crossref identifies the published venue as the 2021 IEEE Information Theory Workshop and supplies the DOI above with publication date 2021-10-17.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary paper | Abstract, introduction, code definition, clipping methods, OAMP equations, state-evolution optimization, figures, table, conclusion, and references. | Problem, mechanism, complexity, simulation settings, results, and limitations. | High for source reporting | Extraction introduced mathematical-glyph encoding noise; no reproduction was performed. |
| E2 | S2 | Primary arXiv metadata | Title, authors, version, dates, category, abstract, and submission comment. | Stable identity and high-level claim cross-check. | High | Abstract cannot independently support detailed empirical claims. |
| E3 | S3 | DOI/Crossref metadata | Exact title, authors, venue, DOI, and publication date. | Published-work identity. | High | Does not validate methods or results. |
| E4 | S4 | Local selection metadata | Public paper URL and presence of selected PDF. | Selection provenance. | Medium | Local path withheld and file not redistributed. |
| E5 | S5-S6 | Repository standards | DEP classes, naming, README inventory, attribution, logs, and reports. | Artifact structure and submission policy. | High | Policy evidence only. |
| E6 | S7 and arXiv:2311.08543 | Related DEP and primary metadata | Geometry-aware 2D reservoir-computing symbol detection for OTFS. | Structured-channel detection comparison. | Medium | Related work does not validate the selected paper. |
| E7 | S8 and arXiv:2606.22194 | Related DEP and primary metadata | Learned maximum-likelihood QEC decoding under multiple noise models and information-theoretic threshold framing. | Decoder-threshold and noisy-channel comparison. | Medium | Quantum setting differs materially from classical SR coding. |
| E8 | S9 and arXiv:2606.27455 | Related DEP and primary metadata | Graph-filter identification followed by sparse admissible shift recovery and alternating optimization. | Structured sparse-inference comparison. | Medium | Network inference is not a channel-coding benchmark. |
| E9 | Exact-title GitHub search | Discovery search | Returned third-party indexing or notes; no official implementation identified. | Code-availability limitation. | Medium | Search non-result is not proof of nonexistence. |

## Executive Summary

*Irregularly Clipped Sparse Regression Codes* replaces one global clipping threshold with a distribution over several thresholds in a sparse-regression-code transmitter. A partial discrete cosine transform encodes a block-sparse information vector. The output symbols are partitioned, clipped groupwise, normalized to preserve transmit power, sent through additive white Gaussian noise, and decoded with orthogonal approximate message passing (OAMP).

The mechanism is an explicit distortion tradeoff. Strong clipping increases nonlinear clipping distortion but permits greater normalization-based amplitude compensation; weak clipping preserves the transform output but accepts more channel-noise impact. A mixture of thresholds expands this tradeoff beyond any single threshold. The authors use OAMP state evolution to choose distribution weights over a fixed candidate threshold set.

The source reports about 0.4 dB SNR gain over an optimized regular clipper at code length 24,576 and section error rate near `10^-5`. It also reports waterfall behavior across rates 0.2 to 1.0 with separately optimized mixtures. Confidence is high that the paper states and numerically illustrates these results, but only medium that they generalize: experiments were not reproduced, no official code was found, mixtures are retuned per operating point, and hardware or mismatch evidence is absent.

The wider research value is the use of a tractable iterative-decoder state model to optimize a mixture of nonlinear preprocessors. That pattern may transfer to quantization, saturation, companding, or learned preprocessing, provided finite-length and mismatch tests accompany asymptotic analysis.

## Detailed Summary

### Problem and Background

Sparse regression codes represent information in a block-sparse vector with one nonzero entry per section. Multiplying that vector by a measurement matrix creates the channel codeword. In asymptotic settings, sparse superposition/regression codes decoded by approximate message passing can approach AWGN capacity, but the paper emphasizes a finite-length gap and practical competitiveness problems relative to established coding families.

Earlier regular clipping applies the same saturation threshold to every transform output, then rescales the clipped codeword to fixed transmit power. Rescaling can improve the effective balance between codeword amplitude and AWGN, but clipping introduces nonlinear distortion. This produces an optimal regular threshold rather than a monotonic benefit from stronger clipping.

### Code and Decoder

The source uses a partial DCT measurement matrix obtained by selecting rows from an `N x N` DCT matrix. This supports fast DCT/IDCT and fits OAMP's treatment of non-IID sensing matrices. The information vector has `L` sections of length `B`, one nonzero of amplitude `sqrt(B)` in each section, compression rate `delta=M/N`, and code rate `R=L log(B)/M` as stated by the paper.

OAMP alternates de-clipping, orthogonalization, inverse transform, sparse-section demodulation, another orthogonalization, and a forward transform. State evolution reduces iterative dynamics to scalar variance transfer curves under stated asymptotic assumptions. The paper uses locally simulated transfer functions rather than a fully analytic finite-length guarantee.

### Irregular Clipping

For `K` thresholds, the transform output is partitioned into `K` subvectors. Threshold `k` applies to a fraction `lambda_k` of symbols, with nonnegative weights summing to one. Each group is clipped and normalized using its own threshold-dependent factor. The de-clipping variance becomes a weighted sum of groupwise variances; the rest of OAMP remains structurally the same.

Given a threshold vector, the authors optimize weights to maximize the smallest gap between inverse demodulation and irregular de-clipping transfer curves over a target variance interval. They discretize the interval using 100 log-spaced points from `10^-6` to `1`. The paper characterizes the weight problem as concave with linear simplex constraints and says standard convex-optimization tools can solve it.

### Evidence and Results

The state-evolution charts compare regular and irregular clipping at rate 0.5. The text reports that the decoding tunnel opens at about 2.0 dB for regular clipping and about 1.3 dB for irregular clipping at the target variance, an approximate 0.7 dB analytical separation. This should not be conflated with the finite-length result.

The main simulation sets `B=64`, `L=2048`, `R=0.5`, `M=24,576`, and at most 120 iterations. Regular clipping uses an optimized clipping ratio of -13 dB. Irregular clipping considers 19 candidate ratios and reoptimizes the distribution for each simulated SNR. At SER near `10^-5`, the authors report about 0.4 dB gain over regular clipping and a larger advantage over no clipping.

The rate sweep uses rates 0.2, 0.4, 0.6, 0.8, and 1.0 with code lengths 61,440; 30,720; 20,480; 15,360; and 12,288, at `B=64`, `L=2048`, and at most 100 iterations. The paper reports waterfall behavior and provides representative optimized distributions near `10^-5` SER. Different points can use different thresholds and weights, demonstrating tuning flexibility but leaving open how one fixed design behaves across an operating range.

### Conclusion and Boundary

The paper concludes that irregular clipping improves the clipping-distortion/noise-distortion tradeoff at almost the same computational complexity order as regular clipping because DCT/IDCT dominates at `O(N log N)` per iteration. The evidence is numerical and model-specific. The paper does not provide an official reproducibility package, confidence intervals, real-radio measurements, quantized-hardware evaluation, or a direct practical-code comparison in the inspected text.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | A distribution over clipping thresholds expands the regular-clipping design space for finite-length SR codes. | Author method claim | E1 | Directly supported by the groupwise encoder and weighted state evolution. | High |
| C2 | Given fixed thresholds, the distribution can be optimized using sampled transfer-curve gaps under simplex constraints. | Author method claim | E1 | Formulation and discretization are explicit; solver implementation was not inspected. | High for description; medium for reproducibility |
| C3 | Decoder complexity remains nearly that of regular clipping, dominated by DCT/IDCT at `O(N log N)` per iteration. | Author complexity claim | E1 | Plausible from described operations; constants and design-time optimizer cost are not benchmarked. | Medium-high |
| C4 | The finite-length simulation reports about 0.4 dB gain over regular clipping at `M=24,576` and SER near `10^-5`. | Author empirical claim | E1-E2 | Supported by abstract, results discussion, and conclusion; not reproduced. | High for reporting; medium for generality |
| C5 | The method is robust across rates 0.2 to 1.0. | Author interpretation | E1 | Waterfall curves are shown, but operating points can be retuned and no mismatch intervals are reported. | Medium |
| C6 | Mixture preprocessing guided by iterative state models could generalize beyond clipping. | Reviewer inference | E1, E6-E8 | Reasonable bridge, not demonstrated by the paper or related DEP entries. | Medium-low |

## Methodology

- `Research objective`: Preserve a source-grounded, schema-complete DEP review of one randomly selected eligible arXiv paper and connect it to exactly three related DEP entries.
- `Sources inspected`: Local archive readme; all six pages of the local PDF through native extraction; arXiv metadata; Crossref metadata; live Black-Lake and Black-Lake-Data READMEs; three related DEP artifacts; and arXiv metadata for each related artifact's primary source basis.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, collapsed them to parent-directory paper units, selected a uniform PowerShell `Get-Random` index, derived the arXiv ID, and searched all required dedup surfaces before acceptance.
- `Inclusion criteria`: Primary evidence for identity, method, settings, results, and limitations; repository rules; and DEP entries with overlap in structured channels, learned decoding, or sparse inverse problems.
- `Exclusion criteria`: Third-party summaries as claim evidence, unverified implementation repositories, redistribution of local sources, and entries with only generic AI overlap.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, and DEP-ready provenance analysis.
- `Evidence handling`: Major claims map to ledger IDs; author claims, facts, reviewer interpretations, and non-results are labeled separately.
- `Uncertainty handling`: Unreproduced results, mathematical extraction artifacts, missing code, unknown redistribution permission, related-source depth, and operating-point retuning are explicit.
- `Extraction process`: Native extraction covered six pages with no OCR requirement; prose, captions, values, and equations were inspected while corrupted glyphs were interpreted only with context.
- `Version control`: Primary work pinned to arXiv v1 and DOI 10.1109/ITW48936.2021.9611458; repository rules identified by live default-branch files at access date.
- `Claim selection`: Priority went to mechanism, optimization, state-evolution evidence, exact settings, the 0.4 dB result, complexity, rate sweep, and missing reproducibility evidence.
- `Cross-checking`: The 0.4 dB result was checked across abstract, results discussion, and conclusion; identity was checked between arXiv and Crossref.
- `Safety handling`: Examples use synthetic communications data and avoid unauthorized radio operation or sensitive payload processing.
- `Reviewer stance`: Paper report, critique, replication brief, product translation, and archival deposition.

## Scope, Constraints, and Assumptions

- `Scope`: Review irregular clipping, OAMP/state-evolution optimization, reported finite-length results, related methods, limitations, and safe implementation paths.
- `Temporal boundary`: Sources and repository context inspected through 2026-07-11; no claim about later revisions or implementations.
- `Evidence limits`: No reproduction; no official code found; Crossref supplied metadata rather than publisher full text; formula extraction had encoding noise; related papers checked at metadata/abstract level.
- `Assumptions`: The local PDF corresponds to arXiv:2106.01573v1; prose and captions preserve settings despite glyph noise.
- `Constraints`: Public artifacts omit local paths, identifiers, local timezone labels, and exact execution timestamps. No local source is redistributed without established permission.
- `Out of scope`: Proving the optimization formulation, verifying capacity proximity, implementing a production modem, comparing every modern code, or conducting hardware experiments.
- `Intended use`: DEP deposition, communications review, replication planning, and bounded product ideation.
- `Audience`: Information-theory researchers, signal-processing engineers, iterative-inference researchers, and Black Lake reviewers.
- `Depth target`: Full manuscript report with implementation and replication context.
- `Reproducibility boundary`: Sources and a test plan are preserved, but curves cannot be reproduced from this artifact alone.
- `Operational boundary`: Synthetic and authorized research settings only.
- `Data sensitivity`: Public research metadata and synthetic inputs.

## Observations

- `Observed pattern`: The empirical 0.4 dB gain is smaller than the approximate 0.7 dB state-evolution tunnel difference, illustrating a finite-length gap between scalar trajectory design and realized decoding.
- `Observed pattern`: Irregularity is expressed through weights over fixed thresholds; threshold locations, assignments, and weights are not jointly learned in the described optimization.
- `Technical implication`: Unchanged asymptotic decoder order does not mean zero system cost; partitioning, per-group normalization, design-time optimization, signaling, and quantization still matter.
- `Comparative implication`: The selected paper and related OTFS work inject known structure before final decisions, while the graph-recovery neighbor learns structure as part of inversion.
- `Open question`: A slightly suboptimal fixed mixture may be operationally preferable if it stays calibrated across rates, mismatch, and hardware limits.
- `Reviewer hypothesis`: Joint threshold and weight optimization may help but may also overfit state-evolution approximations.

## Considerations

Deployment assessment should separate decoder iterations from design-time optimization and transmitter complexity. The `O(N log N)` statement covers DCT/IDCT dominance, not the lifecycle cost of generating transfer curves, solving per-SNR distributions, calibrating normalization, and communicating assignments.

Robustness requires mismatch sweeps. State evolution assumes a model family and asymptotic regime; finite-length behavior may change with structured interference, non-Gaussian noise, imperfect normalization, transform error, or amplifier interactions. A practical design needs a policy for choosing mixtures without exact SNR knowledge.

Evaluation should report uncertainty. SER near `10^-5` requires enough trials for stable comparisons, and a 0.4 dB horizontal difference can be sensitive to interpolation, stopping rules, and seeds. Error counts, intervals, and curve-fitting rules would improve decision usefulness.

No sensitive data is needed for replication. Synthetic sections, deterministic transform seeds, and simulated noise suffice. Hardware-in-loop work should remain authorized and retain only aggregate error statistics.

## Strengths

- Simple, interpretable extension of regular clipping rather than an opaque end-to-end model.
- Encoder design connects directly to an iterative decoder's state evolution.
- Partial DCT supports fast transforms and avoids an IID Gaussian implementation requirement.
- Analytical transfer-chart comparison is separated from finite-length simulations.
- Rate sweep covers more than one operating regime and publishes representative distributions.
- Proposed decoder complexity order remains aligned with the regular baseline.

## Weaknesses

- No official code, solver configuration, seeds, or reproducibility package found.
- Principal result is simulation-based, without hardware or independent reproduction.
- Threshold distributions are retuned across SNR and rate settings.
- Baselines do not establish superiority over contemporary practical channel codes.
- No confidence intervals or clear error-count budget near SER `10^-5` in extracted text.
- Quantized thresholds, saturation granularity, and amplifier efficiency are not evaluated.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release deterministic reproduction package | Reproducibility | Modest gain requires exact settings. | Independent verification. | Maintenance effort. | Recreate figures and Table I. |
| Jointly optimize thresholds and weights | Encoder design | Fixed locations constrain mixture. | Possibly better tradeoff. | Nonconvexity and overfit. | Nested search with held-out scenarios. |
| Evaluate fixed versus adaptive mixtures | Robustness | Per-point tuning may be impractical. | Clear deployment tradeoff. | Broader experiment matrix. | Worst-case and average SER over envelopes. |
| Add uncertainty estimates | Evidence quality | Rare errors need sufficient counts. | Credible effect sizes. | Longer runs. | Report trials, intervals, seeds, and interpolation. |
| Add hardware-aware clipping | Systems relevance | Ideal clipping differs from transmit chains. | Better external validity. | Modeling complexity. | Quantization and PA-nonlinearity sweeps. |
| Compare practical codes and latency | Comparative validity | Capacity context is not deployment evidence. | Better positioning. | Implementation parity burden. | Compare errors, throughput, iterations, energy, latency. |

## Potential Implementations

1. `Irregular Clipping Reproduction Bench`
   - `User`: Information-theory researcher.
   - `Goal`: Reproduce transfer curves and finite-length SER under fixed seeds.
   - `Core mechanism`: Generate sparse sections, apply partial DCT and clipping mixtures, run OAMP, and log states and errors.
   - `Required inputs`: `B`, `L`, `M`, rate, SNR grid, thresholds, weights, seeds, iteration limit, and stopping rule.
   - `Outputs`: Transfer charts, SER curves, uncertainty intervals, profile, and evidence ledger.
   - `Risk controls`: Synthetic data only; bounded resources; no payload logging.
   - `Evaluation`: Reproduce qualitative ordering and quantify deviation from the reported 0.4 dB gap.
2. `Robust Mixture Designer`
   - `User`: Communications-algorithm engineer.
   - `Goal`: Choose one mixture that remains useful across an operating envelope.
   - `Core mechanism`: Optimize worst-case or risk-weighted margin over SNR, rate, mismatch, and quantization scenarios.
   - `Required inputs`: Candidate thresholds, scenario family, deployment constraints, and evaluation budget.
   - `Outputs`: Weights, sensitivity report, regular fallback, and validation scenarios.
   - `Risk controls`: Held-out scenarios, explicit failure thresholds, and simulation-only labels.
   - `Evaluation`: Worst-case SER, calibration, latency, and sensitivity versus per-point tuning.
3. `Structured Decoder Comparison Ledger`
   - `User`: Black Lake reviewer or signal-processing team.
   - `Goal`: Compare inverse methods without collapsing assumptions.
   - `Core mechanism`: Normalize each experiment into forward model, prior, decoder, proxy, finite metric, mismatch set, and evidence status.
   - `Required inputs`: Paper metadata, synthetic runs, decoder traces, and DEP paths.
   - `Outputs`: Comparison table, provenance graph, and replication queue.
   - `Risk controls`: Separate source claims from reproduced findings and forbid untraceable numbers.
   - `Evaluation`: Claim coverage and matched-assumption comparison count.

## Three Ways to Exercise This Research

1. `Recreate the distortion tradeoff`: Objective: compare no clipping, one threshold, and a two-threshold mixture on Gaussian transform samples. Inputs: synthetic samples, thresholds, and fixed-power normalization. Method: clip, normalize, add Gaussian noise, and measure clipping and noise components. Output: distortion table. Success criterion: the mixture exposes a tradeoff not represented by one threshold. Stop condition: terminate if normalization fails a deterministic check.
2. `Trace a toy iterative decoder`: Objective: preserve variance and error proxies across iterations. Inputs: a small synthetic sparse-section problem and bounded OAMP-like adapter. Method: run fixed iterations, record proxies, compare regular and mixed clipping, and flag divergence. Output: trace ledger and convergence plot. Success criterion: every plot point maps to a stored record. Stop condition: halt on non-finite values or a preset variance bound.
3. `Stress a fixed mixture`: Objective: test one mixture under mismatch. Inputs: synthetic SNR, non-Gaussian-noise, quantization, and transform-perturbation scenarios. Method: choose weights on training scenarios, freeze them, evaluate held-out scenarios, and compare with regular clipping. Output: robustness matrix. Success criterion: improvement remains without violating latency or error budgets. Stop condition: reject when any error threshold is exceeded.

## Example MVP Product

- `Product name`: ClipMix Lab
- `Target user`: Researchers implementing iterative communications decoders.
- `Problem`: Published clipping gains are hard to reproduce and may rely on tuning that does not transfer.
- `Core workflow`: Define a synthetic scenario, select thresholds, optimize or import weights, run bounded OAMP experiments, inspect traces, and export a DEP-ready evidence packet.
- `Data requirements`: Synthetic sparse-section seeds, partial-DCT configuration, noise scenarios, threshold grids, weights, iteration traces, and aggregate error counts.
- `Architecture`: Local CLI with deterministic simulator, transform adapter, clipping module, optimizer adapter, trace ledger, validation suite, and Markdown exporter.
- `Success metrics`: Figure-order reproduction, interval width, held-out robustness, deterministic rerun equality, runtime budget, and evidence-to-claim coverage.
- `Risk controls`: Synthetic inputs, bounded budgets, no raw payloads, non-finite-value stops, source-claim labels, and sanitization.
- `Limitations`: Does not establish real-radio performance, capacity achievement, or superiority over production codes.
- `MVP boundary`: Research simulator and evidence generator, not a modem or live transmitter.
- `Deployment model`: Local-only CLI and static reports.
- `Evaluation plan`: Unit tests for clipping and normalization, seed-repeatability tests, curve sanity checks, matched-baseline review, and public-safe validation.
- `Failure modes`: Incorrect normalization, state-evolution mismatch, insufficient error counts, optimizer overfit, and misleading SER interpolation.
- `Maintenance plan`: Pin dependencies, retain manifests, version solver settings, and rerun smoke tests after changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Irregularly Clipped Sparse Regression Codes | Primary paper | Reviewed work on mixture clipping for OAMP-decoded SR codes. | https://arxiv.org/abs/2106.01573; DOI:10.1109/ITW48936.2021.9611458 |
| Clipping Can Improve the Performance of Spatially Coupled Sparse Superposition Codes | Direct baseline | Regular-clipping predecessor cited by the paper. | IEEE Communications Letters 21(12), 2017 |
| Orthogonal AMP | Decoder foundation | OAMP method cited by the paper. | arXiv:1602.06509; IEEE Access 5, 2017 |
| Vector Approximate Message Passing | State-evolution neighbor | Related rigorous iterative-inference framework. | IEEE Transactions on Information Theory 65(10), 2019 |
| 2D-RC OTFS | Related Black-Lake DEP | Geometry-aware symbol detection for wireless channels. | `Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`; arXiv:2311.08543 |
| Machine Learning Optimal QEC Thresholds | Related Black-Lake-Data DEP finding | Learned decoder tied to noisy-channel limits. | `Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 0102/daily_research_findings_2026-06-25_0102.md`; arXiv:2606.22194 |
| Directed Graph Topology Inference | Related Black-Lake-Data DEP finding | Sparse structural recovery after filter identification. | `Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md`; arXiv:2606.27455 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2106.01573 | Identity, abstract, authors, date, category, and submission comment. | 2026-07-11 | Primary metadata. |
| R2 | https://arxiv.org/pdf/2106.01573v1 | Full method, simulations, results, and references. | 2026-07-11 | Public URL corresponding to inspected local PDF. |
| R3 | https://doi.org/10.1109/ITW48936.2021.9611458 | IEEE ITW publication identity. | 2026-07-11 | Crossref-verified metadata. |
| R4 | Local archive readme and PDF, paths withheld | Selection provenance and full-text inspection. | 2026-07-11 | Not redistributed. |
| R5 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Output repository policy. | 2026-07-11 | Live file inspected. |
| R6 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository policy. | 2026-07-11 | Live file inspected. |
| R7 | `Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | Related structured-channel synthesis. | 2026-07-11 | Source basis: https://arxiv.org/abs/2311.08543. |
| R8 | `Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 0102/daily_research_findings_2026-06-25_0102.md` | Related learned-decoder synthesis. | 2026-07-11 | Source basis: https://arxiv.org/abs/2606.22194. |
| R9 | `Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md` | Related sparse-inference synthesis. | 2026-07-11 | Source basis: https://arxiv.org/abs/2606.27455. |
| R10 | Exact-title GitHub search | Code-availability check. | 2026-07-11 | No official implementation identified; non-result treated cautiously. |

## Appendix

### Random Selection and Dedup Record

- Enumeration: `rg --files -g "*.pdf"` over the local arXiv archive.
- PDF count: 75,438.
- Unique parent-directory paper units: 75,438.
- Uniform method: PowerShell `Get-Random` over unique units.
- Draw: index 27,136 zero-based, or 27,137 one-based.
- Selected unit: arXiv:2106.01573, *Irregularly Clipped Sparse Regression Codes*.
- Dedup fields: arXiv ID, DOI, normalized title, and `Irregular-Clipped-SR` slug.
- Dedup surfaces: Black-Lake logs, reports, lake-data, automation memory, and relevant Black-Lake-Data entries.
- Duplicate exclusions: 0.
- Same-paper markers in the preceding 24-hour window: 0.
- Reselections: 0.
- Source files collected into the DEP: none.

### Replication Checklist

- Reconstruct partial-DCT row selection and sparse-section generator.
- Confirm fixed-power normalization for regular and groupwise clipping.
- Reproduce OAMP de-clipping, orthogonalization, and section demodulation.
- Recreate 100-point log-domain state-evolution sampling from `10^-6` to `1`.
- Recover 19 threshold candidates and per-SNR weights.
- Fix seeds, iteration limits, and stopping rules.
- Report error counts, trials, intervals, and interpolation method.
- Compare analytical tunnel thresholds with finite-length curves.
- Add fixed-mixture, mismatch, and quantized-hardware tests.

### Validation Checklist

- YAML `title` and H1 are identical and no more than 40 characters.
- All required schema headings are present in required order.
- Evidence ledger and claim map distinguish source claims from reviewer inference.
- Every evidence source appears in Source References.
- Three Ways to Exercise This Research contains exactly three paths.
- Example MVP Product includes required fields and bounded controls.
- Exactly three related DEP entries are used for synthesis.
- Public text contains no local absolute paths, user or machine identifiers, local timezone labels, or exact execution timestamps.
