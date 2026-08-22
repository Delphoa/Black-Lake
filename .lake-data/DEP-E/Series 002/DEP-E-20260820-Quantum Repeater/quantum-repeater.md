---
title: "Quantum Repeater - DEP-E"
generated_at: "2026-08-19T15:04:34Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of a single-NV-center absorption-emission quantum repeater node."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "2026-08-20"
primary_url: "https://arxiv.org/abs/2608.17470"
stable_identifier: "arXiv:2608.17470v1"
confidence_summary: "Medium-high for the reported single-node experiment; low for scale-up and network-level performance because those were not demonstrated here."
safety_scope: "non-sensitive research review"
distribution_notes: "Derived review only; no source paper files, datasets, credentials, or private material are redistributed."
public_run_date: "2026-08-20"
---

# Quantum Repeater - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository-relative path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Absorption-emission quantum repeater using diamond quantum memories | Primary artifact | arXiv HTML and record | arXiv:2608.17470v1; submitted 2026-08-18 | https://arxiv.org/abs/2608.17470; https://arxiv.org/html/2608.17470 | arXiv access and source-paper terms apply; no paper file was collected | 2026-08-20 | Full experimental HTML and abstract inspected |
| S2 | Selected source DEP manifest | Source inventory | Markdown | Blob `acad8f9309bdebce03614dc4043b21c5c6e3333e` | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Tech%20Intel%202124%20D0155/README.md | Repository content; inspected by URL and not re-deposited | 2026-08-20 | Inspected |
| S3 | Selected source DEP finding | Source artifact | Markdown | Blob `548e5f59ae2fe692ab61d00793dfae6feba15588` | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Tech%20Intel%202124%20D0155/dep0155_research_findings_2026-08-19_2124.md | Repository content; concise prior finding, not treated as sufficient evidence by itself | 2026-08-20 | Inspected |
| S4 | Quantum repeaters: From quantum networks to the quantum internet | Near-primary review | Journal article | Rev. Mod. Phys. 95, 045006 (2023) | https://doi.org/10.1103/RevModPhys.95.045006 | Publisher terms apply; abstract inspected | 2026-08-20 | Related context inspected |
| S5 | Experimental demonstration of memory-enhanced quantum communication | Independent experimental context | Journal article | Nature 580, 60-64 (2020) | https://doi.org/10.1038/s41586-020-2103-5 | Publisher terms apply; public abstract and metadata inspected | 2026-08-20 | Related context inspected |
| S6 | Quantum teleportation of a photon via absorption and emission for quantum repeater nodes | Related primary work listed by S1 | Journal article | DOI `10.1038/s41534-025-01169-9` | https://doi.org/10.1038/s41534-025-01169-9 | Listed in S1; publisher page was not independently inspected in this pass | 2026-08-20 | Context-only locator |
| S7 | Robust transfer of a quantum state from an absorbed photon into a diamond spin | Related primary work listed by S1 | Journal article | DOI `10.1364/OL.567933` | https://doi.org/10.1364/OL.567933 | Listed in S1; publisher page was not independently inspected in this pass | 2026-08-20 | Context-only locator |

The selected source DEP contains one generated finding and no collected source files. Its source finding identifies the primary preprint but is abstract-level and explicitly says the result was not independently validated there. This artifact therefore treats S1 as the evidentiary anchor and S2-S3 as provenance and selection context.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, arXiv record and abstract | Primary preprint | Authors, title, v1 date, problem framing, complete-node claim, and reported 78% process fidelity | C1, C2 | High | Author-reported preprint; no independent reproduction |
| E2 | S1, Introduction and Principle of Operation | Primary preprint | NV-center absorption, spin-memory transfer, RUS emission, local Bell-state measurement, and multi-node conceptual extension | C2, C3 | High | Conceptual extension is not a network demonstration |
| E3 | S1, Experiments and Results | Primary preprint | 93% photon-to-nuclear-spin fidelity, 87% nuclear-memory fidelity after ten attempts, 83% nuclear-spin-to-photon fidelity, 3.2 microsecond repetition period, and ten-attempt limit | C2, C4 | High | Values are experiment-specific and conditioned on heralding or measurement events |
| E4 | S1, complete-node result and process-tomography supplement | Primary preprint | Six input polarization states, conditional Bell-measurement statistics, physical process constraints, post-processing correction, and 78% identity-process fidelity | C1, C4 | High | Counts, uncertainty intervals, and raw data are not presented in the inspected HTML excerpt |
| E5 | S1, Methods and Data Availability | Primary preprint | Single NV center, 5.5 K operation, optical and spin-control setup, FPGA/AWG conditional control, and data available from the corresponding author on reasonable request | C3, C5 | High | No public dataset or code package was identified in the inspected source |
| E6 | S4, review abstract | Independent review | Repeater architectures, rate limits, and quantum-internet context | C3, C5 | Medium | Abstract-level inspection only; full review figures and text were not used |
| E7 | S5, article abstract and metadata | Independent experiment | Memory-enhanced communication using a solid-state spin memory and asynchronous Bell-state measurements | C3, C5 | Medium-high | Different platform and protocol; comparison is contextual rather than a matched benchmark |
| E8 | S2-S3, selected source DEP | Source-repository evidence | Original item inventory, primary URL, and prior finding's explicit validation boundary | C1, C5 | Medium | Source DEP is a generated recap, not the primary paper |

## Executive Summary

The reviewed preprint reports a complete single-node absorption-emission quantum repeater operation using one nitrogen-vacancy (NV) center in diamond. The node combines heralded absorption of a polarization-encoded input photon, storage of the input state in a nitrogen nuclear-spin memory, memory-preserving repeat-until-success (RUS) emission of an entangled photon, and a local Bell-state measurement that transfers the state to the output photon [E1-E4]. The authors report a 78% process fidelity relative to the identity channel for the end-to-end photon-to-photon operation [E1, E4].

The strongest evidence is that the authors executed the full conditional sequence and characterized it as a quantum channel, rather than showing only a single state-transfer step. Supporting measurements include 93% photon-to-memory state fidelity, 87% memory fidelity after ten RUS attempts, and 83% memory-to-photon state-transfer fidelity [E3]. The paper also reports a calibrated 3.2 microsecond excitation repetition period and identifies residual dephasing from timing jitter and hyperfine dynamics as the main limitation [E3-E5].

Reviewer interpretation: this is a credible laboratory demonstration of a repeater-node primitive, not evidence that a multi-node network, long-distance link, or practical deployment has been achieved. The most important follow-up question is whether the process fidelity and conditional success probabilities remain useful after coupling, loss, synchronization, deterministic measurement, and scaling costs are included. Confidence is medium-high for the reported single-node result and low-to-medium for the paper's broader scalability implications.

## Detailed Summary

### Problem and background

Long-distance quantum communication is limited by photon loss, which causes direct entanglement-generation rates to degrade rapidly with distance. Quantum repeaters address this by combining flying photonic qubits with intermediate memories and conditional operations [E2, E6]. The reviewed approach uses absorption and emission at a local diamond NV center so that the state is transferred through a stationary memory rather than through interference between remote photons.

### Method and mechanism

The experiment prepares an entangled state between an NV electron spin and a nitrogen nuclear spin. Detection of an absorption event projects the input photon's polarization and the electron spin into a Bell-like state, allowing the input state to be teleported into the nuclear-spin memory. The electron spin is then optically excited to produce a zero-phonon-line photon entangled with the electron spin. Because the nuclear memory is not directly involved in the emission event, the excitation can be repeated until a photon is detected. A local Bell-state measurement between the electron and nuclear spins completes the state transfer to the emitted photon [E2].

The conceptual multi-node extension concatenates absorption-emission operations and local Bell-state measurements so that intermediate nodes can support entanglement swapping. This is a design argument, not a measured multi-node chain [E2, E4].

### Experimental setup

The reported device uses a naturally occurring NV center in electronic-grade diamond, a 2 micrometer solid-immersion lens, a 118 nanometer silicon-dioxide antireflection coating, and operation at 5.5 K with residual static fields compensated to zero [E5]. The input optical pulse is polarization encoded; the paper reports a 12 ns pulse, mean photon number 400 at the sample, and an absorption efficiency of approximately 10^-3, with absorption events treated as dominated by single-photon absorption [E5].

The RUS controller is implemented with a home-built FPGA that branches on photon-detection signals, while an arbitrary waveform generator changes spin-control sequences. The paper reports 3 ns pi pulses at 1.2 microwatts for the entangled-emission excitation and a 637 nm zero-phonon-line filter with 5 nm full width at half maximum [E5]. These details make the claimed conditional control concrete, but they also show that the result depends on specialized cryogenic optics, timing, and control hardware.

### Experiments and results

The paper uses six polarization states spanning the Pauli eigenstate bases for tomography. The reported measurements are:

| Stage | Reported result | Interpretation |
|---|---:|---|
| Photon to nitrogen nuclear-spin transfer | 93% average state fidelity | Heralded input storage in the memory |
| Memory preservation after RUS emission | 87% average fidelity after ten attempts | The memory remains usable while emission is retried |
| Nuclear spin to emitted photon | 83% average state fidelity | Conditional output transfer after emission and Bell measurement |
| Complete absorption-to-emission channel | 78% process fidelity to identity | End-to-end characterization of the repeater-node operation |

The authors choose ten as the maximum number of excitation attempts after observing a trade-off between photon collection efficiency and memory fidelity. The main reported degradation mechanism is residual dephasing from stochastic excited-state relaxation timing and the associated hyperfine interaction. A supplementary analysis estimates a memory-retention factor of 0.961 per excitation event and identifies a 1.6 ns timing offset for the 3.2 microsecond repetition period [E3-E5].

### Process characterization

The complete channel is reconstructed from conditional output-photon statistics. The supplementary method combines measured detection rates with Bell-measurement success rates, normalizes paired polarization outcomes, reconstructs output density matrices, and fits a process matrix subject to positivity and trace-preservation constraints [E4]. Known unitary rotations associated with Bell-measurement outcomes are compensated in post-processing; the paper argues that these corrections can be implemented by classical feedforward in a practical system [E4].

### Conclusion and boundary

The source supports the narrower conclusion that a single NV center can perform the essential conditional steps of an absorption-emission repeater node and that the resulting channel can be measured as non-classical with 78% process fidelity. It does not establish a long-distance network, a repeater-chain rate, deterministic Bell measurement in the demonstrated sequence, or production-ready hardware. The authors identify dephasing suppression, photonic integration, fiber coupling, and moderate Purcell enhancement as routes for improvement [E5].

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The experiment demonstrates a complete absorption-emission repeater-node operation with 78% process fidelity relative to identity. | Author claim supported by measured process tomography | E1, E4 | Supported for the single-node, conditional laboratory sequence. "Scalable" remains a forward-looking architectural claim. | High for the local result; low for scale-up |
| C2 | The nuclear-spin memory enables RUS emission without immediately discarding the stored input state. | Author claim supported by tomography | E2, E3 | Supported by the reported 87% memory fidelity after ten attempts, with dephasing as a visible trade-off. | High |
| C3 | The architecture relaxes dependence on remote-photon interference and strong cavity coupling. | Author claim and reviewer interpretation | E2, E5, E6 | Plausible for the local interface, but the claim does not remove the need for precise local optics, timing, collection, and memory control. | Medium-high |
| C4 | RUS creates a useful rate advantage over direct transmission in some parameter regimes. | Author claim based on supplementary analysis | E3-E5 | Partially supported as a conditional regime statement; no end-to-end network rate is measured here. | Medium |
| C5 | The result is a foundation for practical long-distance quantum networks. | Author interpretation / forward-looking implication | E1, E5-E7 | Reasonable as a research direction, not established as deployment readiness. Independent scaling and systems evaluation are still required. | Low-medium |

## Methodology

- `Research objective`: Preserve and critically review the selected DEP's primary quantum-repeater finding, identify what was actually demonstrated, and translate the evidence into bounded follow-up and implementation questions.
- `Sources inspected`: The selected DEP README and finding; the primary arXiv record and full experimental HTML for arXiv:2608.17470v1; the abstract and metadata for the 2023 quantum-repeater review; and the abstract and metadata for the 2020 memory-enhanced communication experiment.
- `Discovery strategy`: Repository inspection of the canonical source DEP, direct access to the cited arXiv record and HTML, inspection of the primary paper's methods and supplementary notes, and citation-following to two near-primary comparison sources. Two additional DOI locators were retained because the primary paper cites them, but their publisher pages were not independently inspected.
- `Inclusion criteria`: Primary evidence for the mechanism, experimental setup, measured fidelities, process tomography, limitations, data availability, and source provenance; near-primary context that helps distinguish a node primitive from network-level claims.
- `Exclusion criteria`: No unsupported claims from news or summaries; no uncollected paper files; no claims about code, datasets, error bars, network throughput, or replication when the inspected sources did not provide them.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication planning.
- `Evidence handling`: Evidence IDs link claims to inspected source sections. Author claims, reviewer interpretations, and forward-looking inferences are labeled separately.
- `Uncertainty handling`: Conditional results, source availability, uninspected related papers, and the gap between a single-node demonstration and a multi-node network are stated explicitly.
- `Extraction process`: HTML headings, methods, reported metrics, supplementary process-tomography equations, data-availability notes, and citation metadata were inspected directly. No PDF, source archive, dataset, or code package was collected.
- `Version control`: The primary work is pinned to arXiv:2608.17470v1; source-DEP Markdown files are identified by their public blob SHAs in S2-S3.
- `Claim selection`: Priority was given to the complete-node sequence, measured fidelity values, conditional control, limiting mechanism, and evidence needed for scale-up.
- `Cross-checking`: The primary abstract, introduction, results, discussion, methods, and supplementary notes were cross-checked against one another; comparison context was checked against the inspected abstracts of S4-S5.
- `Safety handling`: The artifact is non-sensitive quantum-network research. Implementation suggestions remain simulation, characterization, or authorized laboratory planning; they do not provide operational access instructions or unsafe procedures.
- `Reviewer stance`: Source-first DEP-ready manuscript, critical review, implementation brief, and replication plan.

## Scope, Constraints, and Assumptions

- `Scope`: The single-node absorption-emission protocol, its measured state-transfer and process fidelities, experimental control path, limitations, related quantum-repeater context, and bounded follow-up options.
- `Temporal boundary`: Sources accessed on 2026-08-20; primary paper version v1 submitted 2026-08-18.
- `Evidence limits`: The primary work is a preprint. Raw data are stated to be available from the corresponding author on reasonable request, but no data package was inspected. No public code, configuration, hardware design, or independent reproduction was identified in the inspected sources.
- `Assumptions`: "Complete repeater-node operation" is interpreted as the demonstrated absorption, RUS emission, local Bell measurement, and process-tomography sequence, not as a deployed multi-node repeater chain.
- `Constraints`: Do not redistribute paper files or restricted data; preserve public URLs and repository-relative provenance; avoid presenting laboratory parameters as a turnkey build recipe.
- `Out of scope`: Independent experimental replication, device fabrication, cryogenic laboratory work, full network-rate optimization, security-proof verification, and certification of a quantum internet deployment.
- `Intended use`: DEP deposition, source-preserving review, follow-on research planning, and evaluation design.
- `Audience`: Quantum-information researchers, systems engineers, research reviewers, and artifact-maintenance agents.
- `Depth target`: Full manuscript research artifact with implementation and replication guidance.
- `Reproducibility boundary`: A reader can identify the protocol and reported metrics, but cannot reproduce the experiment from this artifact alone because raw data, full hardware details, and an executable analysis package were not available.
- `Operational boundary`: Discuss the protocol at research and architecture level; do not treat the document as a laboratory operating procedure.
- `Data sensitivity`: Public research metadata and public paper content; no personal, proprietary, or restricted dataset was collected.

## Observations

- `Observed pattern`: The paper's central advance is architectural completeness at the node level. The 78% process fidelity matters because it follows the full conditional sequence rather than a single transfer stage [E1-E4].
- `Observed pattern`: The measured fidelities form a visible error budget: photon-to-memory transfer is highest, repeated-memory preservation is lower, spin-to-photon transfer is lower again, and the end-to-end channel is lowest [E3].
- `Technical implication`: RUS is not a free efficiency multiplier. It trades additional emission opportunities against memory dephasing, so any scale-up must optimize a joint fidelity-success-rate objective rather than maximize attempt count [E3-E5].
- `Technical implication`: The architecture shifts difficulty from remote interference toward local selection rules, timing, cryogenic optics, collection, charge-state preparation, and memory control. That is a meaningful systems trade, not an elimination of engineering complexity [E2, E5].
- `Contradiction or tension`: The source presents a scalable architectural primitive while the demonstrated system remains a single-node, conditionally post-selected experiment. The word "scalable" should therefore be read as a design direction, not a measured property [E2, E5].
- `Open question`: Whether the reported 78% process fidelity and conditional success probabilities yield a useful repeater rate after realistic coupling, detector, feedforward, and memory-lifetime costs remains unresolved.
- `Reviewer hypothesis`: A next-generation evaluation should report a Pareto frontier over process fidelity, heralded success probability, mean attempt count, memory survival, and latency. A single fidelity number hides the most important repeater trade-offs.

## Considerations

The practical value of the node depends on more than process fidelity. A network designer would need absorption probability, collection and coupling efficiency, detector efficiency, Bell-measurement success, feedforward latency, memory lifetime, clock rate, and loss per segment in one comparable model. The primary paper provides several ingredients but not a full end-to-end network-rate table [E3-E5].

The experiment uses probabilistic charge-state initialization and a probabilistic Bell-state projection in the demonstrated sequence. Those choices are reasonable for a proof-of-principle fidelity measurement, but they complicate comparisons with deterministic or multiplexed repeater proposals. They also make conditioning and post-selection boundaries important to report in later work.

The source's data-availability statement places the raw data behind reasonable-request access. That limits independent validation and means that any future artifact should preserve the distinction between "reported by the authors" and "recomputed by an independent reviewer." The comparison with the 2020 memory-enhanced experiment is useful but not a matched benchmark because the platforms and protocols differ [E5, E7].

Safety and governance considerations are modest but nonzero: quantum-network claims can affect research funding, procurement, and strategic technology decisions. Public summaries should keep experimental evidence, architecture proposals, and deployment predictions separate, and should not convert specialized parameters into an unreviewed laboratory recipe.

## Strengths

- The paper integrates absorption, memory storage, RUS emission, Bell measurement, and process characterization in one source, making the node-level claim auditable [E1-E4].
- It reports a coherent set of intermediate and end-to-end fidelity values rather than only a headline result [E3].
- The supplementary process-tomography description exposes how conditional probabilities are normalized and constrained, which improves interpretability [E4].
- The discussion identifies a specific limiting mechanism - timing-jitter-driven dephasing - and connects it to a concrete RUS-attempt limit [E3-E5].
- The methods section reports enough platform and control context to distinguish a real laboratory sequence from a purely conceptual proposal [E5].

## Weaknesses

- The result is a v1 preprint and has no independent reproduction in the inspected evidence set.
- The demonstration is single-node and does not measure a multi-node chain, long-distance transmission, or a system-level repeater rate.
- The headline process fidelity is conditional on successful measurement events and post-processing corrections; the full unconditional success budget is not summarized in one comparable table [E3-E4].
- Data are available from the corresponding author on reasonable request, but no public data or executable analysis package was inspected [E5].
- The comparison to direct transmission and future scalability is parameter-regime dependent; the paper does not establish that the demonstrated hardware already wins at network scale.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish raw count data, uncertainty estimates, and analysis scripts | Reproducibility | Fidelity values and conditional normalization should be independently recomputable | Higher auditability and error-budget clarity | Data curation and licensing effort | Recompute state/process tomography from released counts |
| Report a complete success-and-latency budget | Systems evaluation | Process fidelity alone does not predict repeater rate | Comparable network-level decision support | Requires calibrated hardware and timing measurements | Compare predicted and measured heralded rates across attempt limits |
| Sweep RUS attempt limits and timing schedules | Protocol optimization | The current ten-attempt cap reflects a fidelity-efficiency trade-off | Identify a Pareto frontier instead of one operating point | More experiment time and possible memory damage | Repeated tomography under pre-registered schedules |
| Replace probabilistic Bell projection or quantify its full overhead | Measurement | Deterministic or higher-success measurement changes the usable rate | Better comparison with repeater architectures | Hardware and control complexity | Measure conditional and unconditional channel metrics |
| Test fiber coupling and photonic integration in the same error budget | Device scale-up | The paper names coupling and Purcell engineering as improvement routes | Translate local fidelity into deployable link metrics | Fabrication and integration risk | End-to-end link test with calibrated loss and collection |
| Add independent validation of the process reconstruction | Analysis | Conditional tomography and post-processing can hide normalization mistakes | Stronger confidence in the 78% figure | Requires shared data and analysis review | Independent implementation and blind comparison |

## Potential Implementations

### 1. Repeater-node performance simulator

- `User`: Quantum-network researchers and systems architects.
- `Goal`: Explore how fidelity, attempt count, memory dephasing, collection efficiency, and link loss interact.
- `Core mechanism`: A transparent simulator models the absorption-to-memory step, RUS attempts, Bell-measurement success, and feedforward as a parameterized channel.
- `Required inputs`: Publicly reported fidelity values, synthetic success probabilities, configurable memory-retention factors, and link-loss assumptions.
- `Outputs`: Pareto plots, expected heralded throughput, end-to-end fidelity estimates, and sensitivity tables.
- `Risk controls`: Synthetic defaults, explicit conditional/unconditional labels, no claims of hardware equivalence, and provenance for every parameter.
- `Evaluation`: Unit tests against the paper's reported intermediate values and hand-checked limiting cases.

### 2. Evidence ledger and tomography audit notebook

- `User`: Experimental reviewers and replication teams.
- `Goal`: Recompute conditional probability normalization and process-matrix constraints from a released or synthetic count table.
- `Core mechanism`: A notebook implements the six-state tomography pipeline, normalization, physicality checks, and fidelity calculation.
- `Required inputs`: Released experimental counts or synthetic counts with documented assumptions.
- `Outputs`: Reconstructed density matrices, process matrix, fidelity, uncertainty estimates, and an auditable evidence map.
- `Risk controls`: Synthetic data until authorized data access is granted; no raw personal data; no unreviewed experimental control commands.
- `Evaluation`: Compare independent implementations and verify positivity, trace preservation, and known-channel test fixtures.

### 3. Research-grade RUS schedule optimizer

- `User`: Authorized quantum-control researchers.
- `Goal`: Search for excitation schedules that preserve nuclear-spin coherence while retaining useful emission probability.
- `Core mechanism`: Optimize a bounded schedule against a calibrated memory-retention model and measured photon-detection likelihood.
- `Required inputs`: Synthetic or authorized calibration data, timing jitter model, attempt limit, and safety envelope.
- `Outputs`: Candidate schedules, predicted fidelity-success trade-offs, and a validation plan.
- `Risk controls`: Simulation-first, hard attempt limits, human review before laboratory use, and no autonomous hardware actuation.
- `Evaluation`: Hold-out calibration tests, randomized schedule baselines, and laboratory confirmation only under approved procedures.

## Three Ways to Exercise This Research

1. `Synthetic channel reconstruction`: Objective - understand the reported process-fidelity pipeline. Inputs - six synthetic Pauli-eigenstate inputs and a known identity-plus-dephasing channel. Method - reconstruct conditional output states, enforce physical process constraints, and compare the recovered fidelity with the known value. Output - a small audit report. Success criterion - the recovered process is physical and agrees with the known channel within tolerance. Stop condition - stop if the implementation requires unverified experimental counts or undocumented conventions.
2. `RUS trade-off simulation`: Objective - test how repeated emission changes useful throughput. Inputs - the reported 87% ten-attempt memory fidelity, a synthetic per-attempt retention factor, and configurable detection probabilities. Method - sweep attempt limits and plot fidelity versus success and latency. Output - a Pareto frontier with clearly labeled assumptions. Success criterion - the trade-off is monotonic or its deviations are explained by the model. Stop condition - stop before treating simulated rates as measured network performance.
3. `Evidence-to-architecture review`: Objective - translate the node claim into a scale-up checklist. Inputs - the primary paper, the 2023 repeater review, and the 2020 memory-enhanced experiment. Method - map each required component to evidence, missing measurement, and a proposed validation test. Output - a two-column evidence-gap register. Success criterion - every architecture claim has either direct evidence or an explicit unresolved gap. Stop condition - stop if a source is inaccessible or a deployment conclusion would rely on an unverified citation.

## Example MVP Product

- `Product name`: Repeater Evidence Ledger
- `Target user`: Quantum-network research groups, reviewers, and technology-assessment teams.
- `Problem`: Experimental repeater papers often report fidelity, success, and scalability evidence in different places, making architecture-level comparison difficult.
- `Core workflow`: Ingest public paper metadata and reviewer-entered measurements; map each claim to a source and evidence ID; compute clearly labeled conditional metrics; render a fidelity-success-latency trade-off view; export a provenance-preserving review record.
- `Data requirements`: Public paper URLs, manually curated tables, synthetic defaults, source version identifiers, and optional authorized experimental counts.
- `Architecture`: Local-first Markdown/YAML evidence store, deterministic validation layer, notebook or CLI for derived metrics, and a static report renderer. No raw sensitive data is sent to a hosted service by default.
- `Success metrics`: 100% of displayed claims have evidence IDs; zero broken source links in a smoke test; independent reviewers agree on conditional/unconditional labels; synthetic reconstruction passes known-channel tests.
- `Risk controls`: No automatic claims of scalability, no hidden imputation of missing metrics, visible source status, source-version pinning, and human approval for any laboratory or procurement decision.
- `Limitations`: It cannot replace experimental validation, recover unavailable data, or compare unlike platforms without expert judgment.
- `MVP boundary`: Public-paper evidence and synthetic calculations only; no hardware control, no private data ingestion, and no autonomous literature claims.
- `Deployment model`: Local CLI plus static Markdown/HTML output.
- `Evaluation plan`: Schema validation, link checks, known-channel tests, reviewer spot checks, and a comparison against a hand-built evidence table.
- `Failure modes`: Conditional metrics may be mistaken for unconditional rates; source revisions may change numbers; model assumptions may dominate outputs; and a clean ledger may still encode a weak experiment.
- `Maintenance plan`: Recheck source versions, preserve correction notes, version parameter assumptions, and require a reviewer for changed headline metrics.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Azuma et al., *Quantum repeaters: From quantum networks to the quantum internet* | Near-primary review | Provides the broader repeater architecture, rate-limit, and quantum-internet context used to bound the single-node claim. Abstract and metadata inspected. | https://doi.org/10.1103/RevModPhys.95.045006 |
| Bhaskar et al., *Experimental demonstration of memory-enhanced quantum communication* | Independent experiment | Shows a different memory-assisted diamond platform and asynchronous Bell-state measurement, useful for comparison without treating it as a matched benchmark. Abstract and metadata inspected. | https://doi.org/10.1038/s41586-020-2103-5 |
| Reyes et al., *Quantum teleportation of a photon via absorption and emission for quantum repeater nodes* | Related primary work | Directly cited by the reviewed preprint as prior absorption-emission state-transfer work; publisher page was not independently inspected in this pass. | https://doi.org/10.1038/s41534-025-01169-9 |
| Ito et al., *Robust transfer of a quantum state from an absorbed photon into a diamond spin* | Related primary work | Cited by the reviewed preprint for photon-to-diamond-spin transfer; retained as a near-primary follow-up locator, not as independently verified evidence here. | https://doi.org/10.1364/OL.567933 |
| Kalb et al., *Dephasing mechanisms of diamond-based nuclear-spin memories for quantum networks* | Technical neighbor | Cited by the reviewed preprint for memory dephasing context and relevant to the RUS fidelity trade-off; not independently inspected in this pass. | https://doi.org/10.1103/PhysRevA.97.062330 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2608.17470 | Canonical title, authors, v1 date, abstract, DOI, and source status | 2026-08-20 | Primary arXiv record; v1 submitted 2026-08-18 |
| R2 | https://arxiv.org/html/2608.17470 | Introduction, protocol, results, methods, supplementary tomography, limitations, and data availability | 2026-08-20 | Full experimental HTML inspected |
| R3 | https://doi.org/10.48550/arXiv.2608.17470 | Stable DOI locator for the primary preprint | 2026-08-20 | arXiv-issued DOI shown on the canonical record |
| R4 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Tech%20Intel%202124%20D0155/README.md | Selected DEP inventory, provenance, and source-availability note | 2026-08-20 | Source DEP file inspected by URL; blob `acad8f9309bdebce03614dc4043b21c5c6e3333e`; not collected |
| R5 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Tech%20Intel%202124%20D0155/dep0155_research_findings_2026-08-19_2124.md | Prior generated finding and explicit non-validation boundary | 2026-08-20 | Source DEP file inspected by URL; blob `548e5f59ae2fe692ab61d00793dfae6feba15588`; not collected |
| R6 | https://doi.org/10.1103/RevModPhys.95.045006 | Repeater architecture and quantum-internet context | 2026-08-20 | Abstract and metadata inspected; full text not used |
| R7 | https://doi.org/10.1038/s41586-020-2103-5 | Memory-enhanced quantum communication comparison | 2026-08-20 | Abstract and metadata inspected; different platform and protocol |
| R8 | https://doi.org/10.1038/s41534-025-01169-9 | Related absorption-emission work listed by the primary paper | 2026-08-20 | Context-only locator; publisher page not independently inspected |
| R9 | https://doi.org/10.1364/OL.567933 | Related absorbed-photon-to-diamond-spin work listed by the primary paper | 2026-08-20 | Context-only locator; publisher page not independently inspected |
| R10 | https://doi.org/10.1103/PhysRevA.97.062330 | Related nuclear-spin dephasing work listed by the primary paper | 2026-08-20 | Context-only locator; publisher page not independently inspected |

## Appendix

### Replication checklist

- [ ] Obtain the primary paper's raw count data or an authorized synthetic equivalent.
- [ ] Confirm the six input-state and six output-measurement conventions.
- [ ] Recompute conditional probabilities using the supplementary normalization procedure.
- [ ] Reconstruct physical output states and a positive, trace-preserving process matrix.
- [ ] Reproduce the reported intermediate fidelities before attempting the end-to-end channel.
- [ ] Sweep RUS attempt count and timing schedule while recording memory fidelity, success probability, and latency.
- [ ] Report conditional and unconditional quantities separately.
- [ ] Compare the resulting parameter set with a transparent direct-transmission baseline.

### Provenance and selection note

This artifact was generated from the randomly selected source path `Black-Lake-Data/.lake-data/DEP-20260819-Tech Intel 2124 D0155`. The selection snapshot contained 984 canonical DEP directories, 52 excluded families with same-automation markers within the 24-hour window, and 932 eligible candidates. The cryptographic draw was `3125368765`, accepted on attempt 1 under rejection limit `4294967288`, yielding zero-based eligible index `897`. No prior Report-Mark, source report, or Black-Lake DEP Class artifact was found for this selected DEP at the recheck, so no iterative supporting-document draw was required.

### Missing evidence

No external PDFs, source archives, datasets, code repositories, models, benchmark payloads, or experimental traces were collected. The primary paper's raw data are described as available from the corresponding author on reasonable request. The two additional DOI entries in related reading are preserved as cited context, not as independently inspected evidence.

