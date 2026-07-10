---
title: "Physical Data - DEP-E"
generated_at: "2026-07-10 (date-only public marker; exact local timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of arXiv:2407.14504, Physical Data Embedding for Memory Efficient AI."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-10"
temporal_cutoff: "arXiv v3 revised 2025-04-18; public sources inspected on the date-only run marker."
primary_url: "https://arxiv.org/abs/2407.14504"
stable_identifier: "arXiv:2407.14504v3"
confidence_summary: "Medium-high for source identity and source-reported method/results; lower for reproducibility because code, data, and experiments were not rerun."
safety_scope: "non-sensitive, evaluation-oriented, public research review"
distribution_notes: "Repository-relative paths and public URLs only; local execution context withheld."
---

# Physical Data - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract page | Primary metadata | HTML | arXiv:2407.14504v3 | https://arxiv.org/abs/2407.14504 | Public arXiv page; source files not redistributed. | 2026-07-10 | Inspected |
| S2 | arXiv PDF | Primary paper | PDF | arXiv:2407.14504v3 | https://arxiv.org/pdf/2407.14504 | Public PDF inspected for review; not copied into this DEP. | 2026-07-10 | Inspected |
| S3 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2407.14504 | https://doi.org/10.48550/arXiv.2407.14504 | Public DOI reference. | 2026-07-10 | Recorded |
| S4 | Local arXiv archive metadata | Selection provenance | Readme/PDF presence | arXiv:2407.14504 | Local path withheld | Local archive unit confirmed selected paper; no local file redistributed. | 2026-07-10 | Observed |
| S5 | Black-Lake README | Repository authority | Markdown | origin/main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository standard. | 2026-07-10 | Fetched/read |
| S6 | Black-Lake-Data README | Related repository authority | Markdown | origin/main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository standard. | 2026-07-10 | Fetched/read |
| S7 | Tech Intel 2338 DEP-E | Related DEP | Markdown | DEP-E-20260709-Tech Intel 2338 | Black-Lake/.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md | Repository-relative related artifact. | 2026-07-10 | Inspected |
| S8 | Local AI Stack DEP-E | Related DEP | Markdown | DEP-E-20260709-Local AI Stack | Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md | Repository-relative related artifact. | 2026-07-10 | Inspected |
| S9 | Tech Intel 0103 source DEP | Related DEP | Markdown | DEP-20260710-Tech Intel 0103 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260710-Tech Intel 0103/daily_research_findings_2026-07-10_0103.md | Repository-relative related artifact. | 2026-07-10 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | arXiv metadata | Title, authors, arXiv ID/version, DOI, category, abstract, submission/revision dates, PDF/source links. | Source identity and high-level contribution. | High | Abstract-level evidence only. |
| E2 | S2 | Primary paper PDF | Method description, NSN architecture, trainable coefficients, datasets, Table 1 accuracy/parameter results, Table 2/3 ablations, analog-computing discussion, limitations. | Main technical review. | High for source-reported claims | No experiment reproduction; equations/figures not independently rederived. |
| E3 | S4 | Local archive metadata | Local readme and PDF presence for arXiv:2407.14504. | Random selection provenance. | Medium | Local path withheld; no local source file redistributed. |
| E4 | S5, S6 | Repository README files | DEP-E naming, required README contents, attribution block, source-side DEP layout. | Output structure and process compliance. | High | Process evidence only. |
| E5 | S7 | Related DEP-E manuscript | UltraQuant, UFP4, low-precision systems, cache residency, and hardware constraints. | Related synthesis around memory/precision efficiency. | Medium | Related artifact is not validation evidence for Physical Data. |
| E6 | S8 | Related DEP-E manuscript | Local inference stack, KV-cache offload, runtime packaging, edge hardware, power/throughput constraints. | Related synthesis around deployment constraints. | Medium | Related artifact is not validation evidence for Physical Data. |
| E7 | S9 | Related source DEP | Analog computing, GaN nonvolatile memory, practical AI-for-science efficiency, pruning/compression signals. | Related synthesis around physical/hardware substrate choices. | Medium | Related artifact is a source package summary; primary papers not deeply reviewed here. |

## Executive Summary

"Physical Data Embedding for Memory Efficient AI" proposes a representation-learning alternative in which trainable physical equations replace conventional neural feature-extraction layers. The reviewed paper demonstrates this idea with the Nonlinear Schrodinger Network (NSN), which treats the Nonlinear Schrodinger Equation as a differentiable trainable model. Each NSN layer adds only three physical coefficients: attenuation, dispersion, and nonlinearity.

The paper's strongest empirical evidence is a set of time-series classification experiments. In the reported six-layer NSN configuration, the embedding block adds 18 trainable parameters beyond the linear classifier. The source reports 92.1% accuracy on Starlight, 86.2% on Ford Engine, and 70.1% on Spoken Digits, averaged over 10 random seeds. These results are competitive with the paper's CNN/LSTM/MLP baselines while using far fewer embedding parameters.

The paper's strongest mechanistic evidence is its ablation study. Dispersion-only layers outperform the baseline, nonlinearity-only layers barely improve it, and the full dispersion-plus-nonlinearity configuration performs best on Ford Engine and Spoken Digits. The reviewer interpretation is that the paper is most convincing when framed as a structured, physics-prior feature transform for domains with compatible dynamics, not as a general replacement for deep representation learning.

The main limitation is generality. The authors explicitly note that NSN may be less flexible than traditional DNNs for data that does not match NLSE or broader PDE assumptions. No official code repository was found from inspected arXiv page context or title/code searches, and no experiments were reproduced in this run.

## Detailed Summary

### Problem

The paper starts from two pressure points in modern AI: large memory/computation footprints and limited interpretability. The authors argue that very large neural networks distribute representations across many opaque trainable parameters, while physical laws often describe complex dynamics with compact, meaningful coefficients. The proposed physical embedding approach tries to exploit that asymmetry by replacing learned feature layers with trainable equations.

### Method

The demonstration model is the Nonlinear Schrodinger Network. Inputs are treated as wave-like signals propagating through a virtual medium. Each layer applies a linear operation parameterized by attenuation and dispersion, followed by a nonlinear operation parameterized by nonlinearity. The model is differentiable, so the coefficients can be optimized with backpropagation and gradient descent. A final dense linear classifier maps the transformed representation to labels.

### Data and Experiments

The paper evaluates on three time-series classification datasets: Ford Engine, Starlight Curve, and Spoken Digits. It compares a baseline linear classifier, MLP, 1D CNN, LSTM with attention, and the NSN. All reported accuracies in Table 1 are averaged over 10 random seeds with standard deviations in parentheses.

Key source-reported Table 1 values:

| Model | Starlight Acc. | Ford Engine Acc. | Spoken Digits Acc. | Embedding / classifier parameter note |
|---|---:|---:|---:|---|
| Baseline | 84.6 | 49.1 | 15.6 | Linear classifier only |
| CNN | 92.0 | 89.5 | 61.9 | Much larger embedding blocks than NSN |
| LSTM+Attention | 86.7 | 90.9 | 54.4 | Larger recurrent embedding block |
| NSN | 92.1 | 86.2 | 70.1 | 18 embedding parameters plus the linear classifier |

### Ablations

The ablation study isolates the role of the NSN's linear/dispersive and nonlinear components. On Ford Engine, the baseline is 49.1%, nonlinearity-only is 51.7%, dispersion-only is 79.5%, and full dispersion plus nonlinearity is 86.2%. On Spoken Digits, the baseline is 15.6%, nonlinearity-only is 19.9%, dispersion-only is 60.3%, and full dispersion plus nonlinearity is 70.1%. The paper attributes the weak nonlinearity-only case to amplitude behavior: self-phase modulation alone does not alter the amplitude passed to the classifier.

### Extension

The authors extend the concept to the Gross-Pitaevskii Equation by adding a potential term. In a Ford Engine ablation, the source reports 49.1% baseline accuracy, 52.1% for nonlinearity plus potential, 85.0% for dispersion plus potential, and 86.0% for the full configuration. This supports the author's claim that physical embedding can be adapted to related PDEs, though only within the paper's tested scope.

### Discussion and Limits

The paper argues that NSN can be parameter-efficient and interpretable because its trainable values have physical meaning. It also discusses analog optical computing as a possible future implementation route, citing nonlinear optical kernels and spectral-phase modulation as adjacent approaches. However, the authors also state that NSN may generalize less well than traditional DNNs when data does not conform to NLSE or PDE assumptions. The reviewer assessment is that future work needs broader benchmarks, reproducible code, stronger hardware evidence, and clearer domain-fit criteria.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Physical embedding treats master equations as trainable models instead of using neural networks as equation surrogates. | Author conceptual claim | E1, E2 | Supported by abstract and method sections. | High |
| C2 | NSN layers add only three trainable physical coefficients per layer. | Author method claim | E2 | Supported by the architecture description and parameter discussion. | High |
| C3 | The six-layer NSN adds 18 embedding parameters and reports competitive time-series classification accuracy. | Author empirical claim | E2 | Supported by Table 1; not independently reproduced. | High for source report, medium for external validity |
| C4 | Dispersion contributes more than nonlinearity alone in the reported ablations, while the combined model performs best. | Author empirical/mechanistic claim | E2 | Supported by Table 2 and accompanying explanation. | High for source report |
| C5 | The framework can extend to related PDEs such as the Gross-Pitaevskii Equation. | Author extension claim | E2 | Supported by a Ford Engine ablation, but broader generality remains unproven. | Medium |
| C6 | NSN's practical value depends on domain fit and may be less general than ordinary DNNs. | Author limitation and reviewer interpretation | E2 | Directly aligned with the limitations section. | High |
| C7 | Related DEP entries show that memory-efficient AI is also a systems/hardware problem, not only a model-architecture problem. | Reviewer interpretation | E5, E6, E7 | Supported as cross-DEP synthesis, not as selected-paper evidence. | Medium |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv archive paper, review it source-first, and deposit a public-safe Black-Lake log, Report-Mark, and DEP-E manuscript.
- `Sources inspected`: Local archive readme/PDF presence, arXiv abstract page, arXiv PDF, arXiv DOI, live Black-Lake README, live Black-Lake-Data README, and exactly three related DEP entries.
- `Discovery strategy`: Enumerated local archive PDFs with `rg --files -g "*.pdf"`, grouped candidates by PDF parent directory, selected a uniform random index with PowerShell `Get-Random`, derived arXiv ID/title from filename and local readme metadata, searched Black-Lake artifacts, automation memory, and Black-Lake-Data context for duplicate markers, then inspected public arXiv and related DEP sources.
- `Inclusion criteria`: Included sources that identify the selected paper, support method/result/limitation claims, define repository deposition rules, or provide concrete conceptual overlap around memory efficiency, hardware substrate, low-precision systems, edge/local inference, analog computing, or model compression.
- `Exclusion criteria`: No source files were redistributed; code, datasets, external repositories, and experiments were not collected or reproduced. Generic recommendation widgets on arXiv were not treated as evidence.
- `Analytical approach`: Mixed empirical, conceptual, implementation, product research, and replication-oriented review.
- `Evidence handling`: Author claims are tied to evidence IDs. Reviewer interpretations and related-entry synthesis are labeled separately. Quantitative claims are preserved as source-reported unless reproduced, which did not occur.
- `Uncertainty handling`: Missing code, missing reproduction, limited benchmark scope, and analog-hardware uncertainty are preserved explicitly rather than smoothed over.
- `Random selection`: Candidate PDF count and paper-unit count were both 75,438. Selected zero-based index was 73,008. Duplicate reselections were 0.
- `Deduplication and reselection validation`: The run scanned Black-Lake `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data `.lake-data`/`.reports` for arXiv ID, DOI, normalized title, and slug markers. Used arXiv ID count was 291; candidate units excluded by used ID were 52; no same-paper marker was found for arXiv:2407.14504.

## Scope, Constraints, and Assumptions

- `Scope`: This artifact reviews arXiv:2407.14504 and connects it to three related DEP entries about memory-efficient systems, local/edge inference, analog computing, and compression.
- `Temporal boundary`: Sources were accessed on the date-only public run marker; the selected paper version is arXiv v3 revised 2025-04-18.
- `Evidence limits`: No experiments were reproduced; no official code was found; datasets and preprocessing were not independently inspected; arXiv PDF equations/figures were reviewed at paper-text level rather than rederived.
- `Assumptions`: The arXiv PDF corresponds to the selected local archive unit and the local readme correctly identifies the selected paper.
- `Constraints`: Public output must avoid local absolute paths, usernames, machine identifiers, local timezone labels, and exact local execution timestamps.
- `Out of scope`: Production implementation of NSN, analog optical hardware design, dataset reproduction, and hardware benchmarking.
- `Intended use`: DEP deposition, research triage, implementation planning, and future reproducibility review.
- `Audience`: Research reviewers, ML systems engineers, and product/implementation planners evaluating memory-efficient AI ideas.
- `Reproducibility boundary`: A reviewer can follow the public arXiv sources and repository-relative related paths, but cannot reproduce results from this artifact alone.
- `Data sensitivity`: Public research sources and repository artifacts only.

## Observations

- `Observed pattern`: The selected paper reframes memory efficiency as representation substrate choice, not just post-training compression.
- `Technical implication`: The value of physical embedding depends on matching the equation family to the data domain and reporting both accuracy and resource metrics.
- `Evidence-quality implication`: Parameter counts are clear in the source, but reproducibility requires code, preprocessing, seeds, hyperparameters, and dataset handling.
- `Hardware implication`: Analog optical computing is a plausible future direction discussed by the authors, but it is not validated by the digital NSN experiments alone.
- `Reviewer hypothesis`: Physical embedding may be most useful as a targeted module for time-series, signal-processing, sensing, or scientific data domains with known dynamical structure.

## Considerations

Adoption would require a benchmark harness that reports accuracy, trainable parameters, inference latency, memory footprint, numerical stability, and domain fit. A compact PDE layer that performs well on one family of time-series tasks could fail on image, tabular, or high-dimensional multimodal data. Product teams should avoid treating "physically interpretable" as a synonym for "validated" unless each coefficient's behavior is audited against task outcomes.

Analog implementation also changes the review burden. Hardware latency and energy claims require device-level evidence, calibration procedures, environmental stability notes, and failure-mode testing. The digital model is a strong conceptual prototype, but an analog product would need a separate engineering evidence ledger.

## Strengths

- The paper presents a clear conceptual distinction from physics-informed neural networks and neural PDE surrogates: it trains the physical equation itself as the representation layer.
- The NSN parameter-count story is concrete and easy to audit from the paper: six layers add 18 embedding parameters.
- The ablation study helps explain why the combination of dispersive and nonlinear terms matters.
- The use of physically meaningful coefficients provides a more interpretable parameter surface than generic neural feature layers.
- The GPE extension gives a first example of how the framework may move beyond one equation family.

## Weaknesses

- The benchmark scope is narrow: three time-series datasets and limited comparison depth are not enough to establish broad generality.
- No official code repository was found in inspected sources, which limits immediate reproducibility.
- The paper does not prove that physical embedding will help data without compatible dynamical structure.
- Analog optical implementation remains future-facing and requires hardware evidence separate from digital simulation.
- The reported results are source claims; this run did not rerun experiments or verify preprocessing.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release reproducible code and configs | Reproducibility | Parameter-efficiency claims need runnable baselines and seeds. | Easier independent validation. | Requires cleanup and maintenance. | Reproduce Table 1/2/3 with fixed scripts. |
| Expand benchmarks | Generality | Current evidence is strongest for selected time-series tasks. | Clearer domain-fit boundary. | More compute and dataset handling. | Add image, tabular, sensor, and scientific dynamics datasets. |
| Report latency/memory directly | Systems evidence | Parameter count is not the full deployment cost. | Better comparison to compression and edge-inference work. | Requires hardware-specific tests. | Measure CPU/GPU latency, memory, and energy per sample. |
| Add failure-case taxonomy | Evaluation | PDE-aligned models may fail in predictable domain-mismatch cases. | Better deployment guardrails. | Needs targeted data curation. | Label failures by signal structure, noise, scale, and nonstationarity. |
| Separate analog evidence | Hardware transfer | Digital experiments do not validate analog implementation. | Prevents overclaiming hardware benefits. | Requires device collaborators. | Maintain a separate analog-readiness evidence ledger. |

## Potential Implementations

1. `Physical Embedding Benchmark CLI`
   - `User`: ML systems researcher.
   - `Goal`: Compare PDE-shaped layers against compact neural baselines on public time-series data.
   - `Core mechanism`: Run standardized splits, train linear/CNN/MLP/NSN variants, and emit accuracy, parameter, latency, and memory tables.
   - `Required inputs`: Public datasets, model configs, seed list, hardware profile.
   - `Outputs`: Markdown report, CSV metrics, failure-case notes.
   - `Risk controls`: Public datasets only, reproducible configs, no deployment claims without reproduction.
   - `Evaluation`: Recreate source tables within tolerance and add extra baselines.

2. `Substrate-Aware DEP Tagger`
   - `User`: Black-Lake reviewer.
   - `Goal`: Classify research artifacts by representation substrate and resource bottleneck.
   - `Core mechanism`: Parse DEP manuscripts and tag claims as equation-based, cache-based, quantization-based, pruning-based, analog, or hardware-bound.
   - `Required inputs`: DEP Markdown files, source references, evidence ledger IDs.
   - `Outputs`: Related-entry graph and substrate taxonomy.
   - `Risk controls`: Tags are review aids, not validation claims.
   - `Evaluation`: Compare automatic tags with manual related-entry selections.

3. `Analog Readiness Scorecard`
   - `User`: Hardware/ML product planner.
   - `Goal`: Decide whether a digital physical-embedding method is ready for analog exploration.
   - `Core mechanism`: Score evidence for device model, calibration, input encoding, noise tolerance, latency, energy, reproducibility, and domain fit.
   - `Required inputs`: Paper evidence, hardware papers, prototype specs, test data.
   - `Outputs`: Go/no-go checklist and evidence gaps.
   - `Risk controls`: No medical, safety-critical, or production claims without domain validation.
   - `Evaluation`: Apply scorecard to historical analog-computing papers and check whether known blockers are surfaced.

## Three Ways to Exercise This Research

1. `Rebuild the paper tables`: Objective: reproduce Table 1 and ablation tables from public datasets once code/configs are available or independently reimplemented. Inputs: public time-series datasets, baseline implementations, fixed seeds. Method: train baseline, CNN, LSTM, and NSN-style models; record parameter counts and accuracies. Output: reproduction table. Success criterion: source-reported trends are confirmed, corrected, or marked unreproducible. Safety boundary: public non-sensitive datasets only.
2. `Domain-fit stress test`: Objective: test whether PDE-shaped layers degrade gracefully outside wave-like time-series data. Inputs: synthetic signals with known dynamics, random/noisy time series, tabular controls. Method: compare NSN-style transforms to linear and small neural baselines. Output: domain-fit map and failure taxonomy. Success criterion: each dataset has a clear hypothesis for why physical embedding helps or fails. Safety boundary: synthetic/public data only.
3. `Related-entry concept map`: Objective: connect Physical Data to Black-Lake systems and hardware-efficiency entries. Inputs: this DEP, Tech Intel 2338, Local AI Stack, and Tech Intel 0103. Method: map each source to bottleneck, substrate, evidence type, and implementation risk. Output: substrate-efficiency matrix. Success criterion: every relationship cites a source path or public URL. Safety boundary: related entries are synthesis anchors, not proof of selected-paper claims.

## Example MVP Product

- `Product name`: PhysEmbed Review Bench
- `Target user`: ML systems researchers evaluating compact, interpretable representation layers.
- `Problem`: Physical embedding claims are difficult to compare with ordinary neural, quantized, pruned, and edge-deployed models unless accuracy and resource evidence are normalized.
- `Core workflow`: Import a paper config, select public datasets, run baseline and physical-layer variants, compute parameter/latency/memory metrics, record ablations, and emit a DEP-ready evidence ledger.
- `Data requirements`: Public time-series datasets, model configs, seed lists, hardware profile, source-paper metadata, related DEP references.
- `Architecture`: Local Python training harness, dataset adapters, model registry, metrics logger, Markdown/CSV report generator, sanitization gate, and optional graph export for related DEP mapping.
- `Success metrics`: Reproduced source table trends, percentage of claims with evidence IDs, parameter/accuracy Pareto frontier, latency/memory measurement completeness, and no local-context leaks in public reports.
- `Risk controls`: Public data only, no sensitive deployment claims, no hidden benchmark changes, date-only public run markers, and clear separation of source claims from reproduced results.
- `Limitations`: MVP cannot validate analog optical hardware, prove broad generality, or replace full peer review.
- `MVP boundary`: Reproduction and review aid, not production model serving.
- `Deployment model`: Local CLI or notebook.
- `Evaluation plan`: Run on source-paper datasets, then add unseen public time-series datasets and compare with compact baselines.
- `Failure modes`: Misconfigured baselines, hidden preprocessing differences, overclaiming parameter counts as full memory savings, and mistaking physical interpretability for validated causal explanation.
- `Maintenance plan`: Track dataset versions, dependency versions, model configs, and source-paper revisions.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Physical Data Embedding for Memory Efficient AI | Primary paper | Reviewed work on physical embedding and NSN. | https://arxiv.org/abs/2407.14504 |
| Nonlinear Schrodinger kernel for hardware acceleration | Paper referenced by selected work | Related analog optical kernel and hardware-acceleration context. | Journal of Lightwave Technology 40(5), 1308-1319 (2022) |
| Physics-informed neural networks | Methodological neighbor | Contrasts with using neural networks as PDE solvers rather than training PDE coefficients as feature layers. | Journal of Computational Physics 378, 686-707 (2019) |
| Fourier Neural Operator | Methodological neighbor | Learns mappings across PDE families; useful contrast for physical embedding. | arXiv:2010.08895 |
| Tech Intel 2338 DEP-E | Related Black-Lake DEP | Low-precision, KV-cache, and hardware systems constraints. | Black-Lake/.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md |
| Local AI Stack DEP-E | Related Black-Lake DEP | Local/edge inference stack, memory-tiered serving, and hardware constraints. | Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md |
| Tech Intel 0103 DEP | Related Black-Lake-Data DEP | Analog computing, hardware efficiency, and pruning/compression findings. | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260710-Tech Intel 0103/daily_research_findings_2026-07-10_0103.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2407.14504 | Selected paper metadata, abstract, authors, version, DOI, and subjects. | 2026-07-10 | Primary arXiv page inspected. |
| R2 | https://arxiv.org/pdf/2407.14504 | Selected paper method, datasets, result tables, ablations, discussion, limitations, references. | 2026-07-10 | Public PDF inspected; no source file redistributed. |
| R3 | https://doi.org/10.48550/arXiv.2407.14504 | Persistent DOI reference. | 2026-07-10 | DOI recorded from arXiv metadata. |
| R4 | Local arXiv archive readme and PDF presence, path withheld | Random selection provenance and local paper-unit confirmation. | 2026-07-10 | No local paths or files redistributed. |
| R5 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Output DEP-E placement, README, attribution, log, and commit-message standards. | 2026-07-10 | Live README fetched/read. |
| R6 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository DEP layout and attribution expectations. | 2026-07-10 | Live README fetched/read. |
| R7 | Black-Lake/.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md | Related memory/precision and systems constraints. | 2026-07-10 | Related artifact inspected. |
| R8 | Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md | Related local inference, edge hardware, runtime, and memory-tiered serving context. | 2026-07-10 | Related artifact inspected. |
| R9 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260710-Tech Intel 0103/daily_research_findings_2026-07-10_0103.md | Related analog computing, hardware efficiency, and compression context. | 2026-07-10 | Related source DEP inspected. |

## Appendix

### Random Selection and Deduplication Record

- Automation name: Black Lake Arxiv DEP 0900.
- Candidate enumeration command class: `rg --files -g "*.pdf"` over the local arXiv source archive.
- Candidate PDF count: 75,438.
- Candidate paper-unit count: 75,438.
- Candidate unit definition: each PDF parent directory.
- Random method: PowerShell `Get-Random` uniform draw over candidate paper units with duplicate rejection.
- Selected zero-based index: 73,008.
- Selected arXiv ID: 2407.14504.
- Selected title: Physical Data Embedding for Memory Efficient AI.
- Dedup scan locations: Black-Lake `.logs`, `.reports`, `.lake-data`; automation memory; Black-Lake-Data `.lake-data`, `.reports`.
- Used arXiv IDs observed in scanned artifact index: 291.
- Candidate units excluded by used ID markers: 52.
- Duplicate reselections: 0.
- Recent marker cutoff: date markers from 2026-07-09 through 2026-07-10 were treated as the 24-hour duplicate window.
- Source files collected: none. Public URLs and repository-relative references are used instead.

### Validation Checklist

- Required manuscript headings are present.
- YAML `title` and H1 are identical and under 40 characters.
- Evidence ledger maps sources to claims.
- Author claims and reviewer interpretations are separated.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- DEP README ends with an attribution block.
- Public artifacts avoid local absolute paths, user home names, local timezone labels, machine identifiers, and exact local execution timestamps.
