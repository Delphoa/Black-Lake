---
title: "2D-RC OTFS - DEP-E"
generated_at: "2026-07-09"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of arXiv:2311.08543, a two-dimensional reservoir-computing method for OTFS symbol detection."
source_status: "URLs only with local archive metadata observed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-09"
temporal_cutoff: "Sources inspected through 2026-07-09."
primary_url: "https://arxiv.org/abs/2311.08543"
stable_identifier: "arXiv:2311.08543"
confidence_summary: "Medium-high for paper metadata and source claims from arXiv HTML; lower for reproducibility because code, datasets, source package, and PDF figures were not independently audited."
safety_scope: "research review, wireless systems analysis, privacy-aware implementation planning, non-sensitive synthetic examples"
distribution_notes: "No source PDF, TeX source, or local archive file is redistributed; local paths and execution context are withheld."
---

# 2D-RC OTFS - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | 2D-RC arXiv abstract page | Primary paper metadata | HTML | arXiv:2311.08543 | https://arxiv.org/abs/2311.08543 | arXiv metadata; DOI and license link visible. | 2026-07-09 | Inspected |
| S2 | 2D-RC arXiv HTML | Primary paper full text | HTML | arXiv:2311.08543v2 | https://arxiv.org/html/2311.08543 | arXiv HTML reports CC BY 4.0; formulas may render incompletely in text extraction. | 2026-07-09 | Inspected |
| S3 | 2D-RC DOI | Persistent identifier | DOI | 10.48550/arXiv.2311.08543 | https://doi.org/10.48550/arXiv.2311.08543 | arXiv-issued DOI. | 2026-07-09 | Referenced |
| S4 | Local arXiv archive metadata | Selection provenance | Local readme/PDF presence | arXiv:2311.08543 | Local path withheld | Local readme and PDF presence observed; no local source file redistributed. | 2026-07-09 | Observed |
| S5 | Black-Lake README | Repository standard | Markdown | origin/main at review time | Black-Lake/README.md | Repository authority for DEP, log, report, attribution, and commit-message rules. | 2026-07-09 | Inspected after fetch |
| S6 | Black-Lake-Data README | Related repository standard | Markdown | origin/main at review time | Black-Lake-Data/README.md | Repository authority for related DEP layout and attribution expectations. | 2026-07-09 | Inspected after fetch |
| S7 | Agent State Review | Related DEP artifact | Markdown | DEP-E-20260708-Agent State Review | Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md | Related Black-Lake artifact; generated synthesis treated as related context, not primary evidence for 2D-RC. | 2026-07-09 | Inspected |
| S8 | Tech Intel 0103 | Related DEP entry | Markdown | Black-Lake-Data DEP-20260626-Tech Intel 0103 | Black-Lake-Data/.lake-data/DEP-20260626-Tech Intel 0103/daily_research_findings_2026-06-26_0103.md | Related source-first findings artifact; no files copied. | 2026-07-09 | Inspected |
| S9 | Wi-Fi privacy paper | Related primary source basis | arXiv abstract page | arXiv:2606.25788 | https://arxiv.org/abs/2606.25788 | Referenced by related DEP entry. | 2026-07-09 | Referenced through related entry |
| S10 | Tech Intel 0103 | Related DEP entry | Markdown | Black-Lake-Data DEP-20260701-Tech Intel 0103 | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md | Related source-first findings artifact; no files copied. | 2026-07-09 | Inspected |
| S11 | MESA paper | Related primary source basis | arXiv abstract page | arXiv:2606.30602 | https://arxiv.org/abs/2606.30602 | Referenced by related DEP entry. | 2026-07-09 | Referenced through related entry |
| S12 | Quantum-network authentication review | Related primary source basis | arXiv abstract page | arXiv:2606.30636 | https://arxiv.org/abs/2606.30636 | Referenced by related DEP entry. | 2026-07-09 | Referenced through related entry |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary arXiv metadata | Title, authors, subjects, submitted/revised dates, DOI, comments, and abstract. | Source identity, metadata, and high-level contribution. | High | Abstract alone is not enough for empirical validation. |
| E2 | S2 | Primary arXiv HTML full text | Introduction, OTFS problem formulation, 2D-RC method, experiments, complexity analysis, conclusion, and appendices. | Method, reported results, limitations, and implementation interpretation. | High for source claims; low for reproduction | HTML formula text is incomplete in places; experiments were not reproduced. |
| E3 | S4 | Local archive metadata | Randomly selected archive unit had a readme and PDF for arXiv:2311.08543. | Selection provenance and local archive availability. | Medium | Local path withheld; local PDF was not redistributed or independently text-extracted. |
| E4 | S5 | Repository standard | DEP-E naming, short-description limit, README requirements, `.logs`, `.reports`, `.lake-data`, and attribution rules. | File placement and DEP README structure. | High | Repository policy source, not research evidence. |
| E5 | S6 | Related repository standard | Raw DEP naming, README, `.source`, and attribution expectations. | Related DEP context handling. | High | Repository policy source, not research evidence. |
| E6 | S7 | Related DEP artifact | State, evidence replay, runtime monitoring, and structured state synthesis. | Related-entry bridge from OTFS online state to Black-Lake state-control themes. | Medium | Generated artifact; does not validate 2D-RC claims. |
| E7 | S8, S9 | Related DEP entry and source basis | Wi-Fi privacy and ML fingerprinting over wireless-side metadata. | Wireless ML/privacy bridge. | Medium | Related entry inspected; full related paper not deeply reviewed here. |
| E8 | S10, S11, S12 | Related DEP entry and source bases | MESA communication-channel security and quantum-network authentication. | Communication-channel trust and authentication bridge. | Medium | Related entry inspected; full related papers not deeply reviewed here. |

## Executive Summary

`2D-RC: Two-Dimensional Neural Network Approach for OTFS Symbol Detection` proposes a learning-based receiver for OTFS modulation in high-mobility wireless channels. The paper's central claim is that prior reservoir-computing symbol detection underuses OTFS domain structure: it works in the time domain and needs multiple RCs to track channel variation. 2D-RC instead operates in the delay-Doppler domain and embeds the 2D circular channel interaction through 2D circular padding and filtering.

The inspected arXiv HTML reports experiments across RCP-OTFS and CP-OTFS variants, QPSK and 16 QAM modulation, mobility changes, LDPC coding, and complexity comparisons. The authors report that a single 2D-RC neural network outperforms prior 1D-RC and model-based estimated-CSI detectors, including LMMSE, MPA, and LSMR. They also report about 2 dB to 3 dB gain over conventional estimated-CSI model-based approaches in the coded CP-OTFS BLER scenario discussed in the paper.

Reviewer confidence is medium-high for metadata, method summary, and reporting of source claims because arXiv abstract and HTML full text were inspected. Confidence is lower for reproducibility: no official code was found in inspected sources, experiments were not reproduced, local PDF text extraction tooling was unavailable, and HTML formula rendering omitted some symbols. The reusable Black-Lake insight is that online learning improves when the learner's state geometry matches the underlying communication process.

## Detailed Summary

### Problem

OTFS modulation places information symbols in the delay-Doppler domain and is motivated by high-mobility scenarios where OFDM can suffer from inter-carrier interference under high Doppler spread. Symbol detection in OTFS is difficult because the receiver must handle channel variation, pilot overhead, and imperfect channel state information.

The paper positions existing approaches in two groups. Model-based detectors can exploit channel structure, but often depend on explicit system modeling and accurate CSI. Offline learning detectors can require large training datasets and may generalize poorly when online channel conditions differ from training. The prior online RC detector can learn from limited over-the-air pilots, but it operates in the time domain and uses multiple RCs to track channel changes.

### Method

2D-RC keeps the online subframe-based training advantage of reservoir computing while moving the representation into the OTFS delay-Doppler domain. The paper's key physical-domain premise is that channel interaction in the DD domain is a 2D circular operation. The method encodes this premise through:

- Phase compensation before windowing.
- 2D windowing over delay and Doppler neighborhoods.
- 2D circular padding to preserve circular boundary structure.
- A 2D filtering reservoir structure with row, column, and diagonal state propagation.
- Output-weight learning from pilot symbols within each subframe.

The authors emphasize that 2D-RC uses one neural network for DD-domain detection, rather than multiple time-domain RCs.

### Experiments and Results

The inspected paper compares 2D-RC with a 1D-RC baseline, MPA with estimated CSI, LSMR with estimated CSI, LMMSE with estimated CSI, and an OFDM LMMSE reference. Reported evaluations include RCP-OTFS, CP-OTFS, QPSK, 16 QAM, varying mobility, LDPC coding, and computational-complexity estimates.

The authors report better BER for 2D-RC than 1D-RC under QPSK and 16 QAM, especially in higher SNR regimes. They attribute this to the 2D method's use of OTFS domain structure and reduced mismatch between pilot and data regions. They also report that 2D-RC outperforms the selected model-based methods when those methods depend on estimated CSI. For the LDPC-coded CP-OTFS scenario, the paper reports around 2 dB to 3 dB BLER gain over conventional model-based estimated-CSI approaches at the target BLER discussed by the authors.

The complexity discussion reports that 2D-RC has lower computational complexity than MPA and LSMR when training/channel-estimation plus testing/detection are counted for one OTFS subframe. It also reports that 2D-RC has higher complexity than 1D-RC but stronger performance.

### Limitations and Review Boundary

The authors' results are numerical experiments, not reproduced in this run. The HTML source does not expose all formulas cleanly as text. No official implementation, dataset, or simulation scripts were found in inspected sources. This artifact therefore preserves source claims and reviewer interpretation, not independent validation.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | 2D-RC embeds OTFS DD-domain 2D circular channel interaction through 2D circular padding and 2D filtering. | Author claim supported by method sections | E2 | Directly supported by inspected arXiv HTML sections on the introduced approach. | High |
| C2 | 2D-RC performs online subframe-based symbol detection using limited pilot symbols and a single neural network. | Author claim supported by method/conclusion | E2 | Directly supported by method and conclusion text. | High |
| C3 | The paper reports better BER/BLER performance than 1D-RC and estimated-CSI model-based detectors across tested OTFS variants and modulations. | Author empirical result | E2 | Supported by source text around numerical experiments; not independently reproduced. | High for reporting; low for reproduced validity |
| C4 | The reported LDPC-coded case gives about 2 dB to 3 dB gain over conventional estimated-CSI model-based approaches. | Author empirical result | E2 | Directly reported in the inspected arXiv HTML; exact target BLER symbol is not available from text extraction. | Medium |
| C5 | A broader implementation lesson is to encode known channel/state geometry into online learners rather than relying on generic temporal recurrence. | Reviewer interpretation | E2, E6-E8 | Reasonable synthesis from the paper and related DEP entries; not an author-stated claim across all sources. | Medium |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv archive paper, review it source-first, and deposit a Black-Lake log, Report-Mark, and DEP-E manuscript that connects the paper to three related DEP entries.
- `Sources inspected`: Selected local archive readme/PDF presence, arXiv abstract page, arXiv HTML full text, arXiv DOI, Black-Lake README, Black-Lake-Data README, three related DEP entries, and related primary arXiv source bases referenced by those entries.
- `Discovery strategy`: Enumerated local archive PDFs with `rg --files -g "*.pdf"`, selected a uniform random index with PowerShell `Get-Random`, derived canonical identifier `arXiv:2311.08543`, scanned Black-Lake artifacts and automation memory for duplicate markers, then inspected public arXiv and related DEP sources.
- `Inclusion criteria`: Sources were included when they identified the selected paper, supported method/results/limitations, defined repository deposition rules, or supplied concrete related DEP overlap.
- `Exclusion criteria`: Local PDF redistribution, TeX source collection, code execution, external dataset collection, and experiment reproduction were excluded. Related source PDFs were not deeply reviewed beyond inspected DEP context.
- `Analytical approach`: Mixed empirical, conceptual, comparative, implementation, product research, privacy/safety, and DEP-ready provenance analysis.
- `Evidence handling`: Author claims are tied to arXiv evidence IDs. Reviewer interpretations are labeled as such. Related DEP entries are synthesis anchors, not validation sources for 2D-RC.
- `Uncertainty handling`: Missing code, unextracted local PDF text, unreproduced experiments, incomplete HTML formula rendering, and related-entry limits are recorded explicitly.
- `Extraction process`: Markdown readmes and DEP artifacts were inspected locally; public arXiv pages were inspected as HTML; local archive file paths are withheld.
- `Version control`: arXiv v2 and public run date are preserved; repository outputs use date-only public-safe names.
- `Reviewer stance`: DEP-ready paper report, implementation brief, and synthesis bridge.

## Scope, Constraints, and Assumptions

- `Scope`: This artifact reviews arXiv:2311.08543 and bridges it with three related DEP entries around state, wireless ML privacy, communication channels, and authentication.
- `Temporal boundary`: Sources were accessed on 2026-07-09. The paper version inspected is arXiv v2 revised 2024-01-25.
- `Evidence limits`: No experiments were reproduced; no official code was found; local PDF text extraction tooling was unavailable; arXiv HTML formulas may omit symbols; related DEP source papers were not deeply reviewed.
- `Assumptions`: The arXiv HTML corresponds to the selected local PDF/readme unit. The related DEP entries are suitable for conceptual synthesis when clearly labeled as related context.
- `Constraints`: Public artifacts omit local absolute paths, home directory names, usernames, machine names, local timezone labels, and exact local execution timestamps. Source files are not redistributed.
- `Out of scope`: Claiming implementation readiness, reproducing BER/BLER curves, validating pilot parameters, collecting copyrighted PDFs, or operationalizing privacy attacks.
- `Intended use`: Black-Lake DEP deposition, reviewer handoff, future wireless/agent-state synthesis, and safe implementation ideation.
- `Audience`: Black-Lake reviewers, wireless ML researchers, agent infrastructure researchers, and implementation planners.
- `Reproducibility boundary`: A future reviewer can follow the cited arXiv sources and repository-relative DEP paths, but cannot reproduce the reported experiments from this artifact alone.
- `Data sensitivity`: Public research metadata and repository-relative artifacts only; local archive context withheld.

## Observations

- `Observed pattern`: The paper's strongest design pattern is geometry-aware online learning: model architecture is shaped by the communication channel's circular delay-Doppler structure.
- `Technical implication`: For wireless or agent systems, scarce observations become more useful when the learner tracks the right state axes rather than flattening everything into generic sequence history.
- `Privacy implication`: If a detector learns highly specific channel features, future implementations should test whether device, user, or environment fingerprints leak through side tasks.
- `Communication-security implication`: Physical-layer detection and logical communication security both require explicit assumptions about channel state, trust, and authentication.
- `Open question`: Can a reproducible, synthetic OTFS harness validate 2D-RC behavior while producing reviewable evidence ledgers for each pilot, prediction, and failure case?

## Considerations

2D-RC should be treated as a research method, not a deployment-ready receiver. Any implementation would need reproducible simulation code, parameter traces, sensitivity analysis, and hardware/runtime assessment. The method may be attractive for practical systems because it avoids reliance on estimated CSI, but the source claims remain numerical and unreproduced here.

Wireless ML systems can create privacy and security side effects. A detector optimized for robust symbol recovery may also learn persistent signatures of devices, channels, or environments. Future work should separate detection performance from identity leakage and include synthetic privacy probes before using real device traces.

The related DEP bridge should stay modest. Agent state ledgers, Wi-Fi ML fingerprinting, MESA communication edges, and quantum-network authentication are not evidence for 2D-RC results. They are useful because they expose shared design questions: what state is observed, how it is encoded, which channel assumptions are trusted, and what evidence remains for later review.

## Strengths

- The paper aligns architecture with OTFS domain structure rather than treating symbol detection as generic sequence learning.
- The method keeps an online subframe-based training story with limited pilots, which is closer to practical adaptation than offline-only learning.
- The evaluation spans multiple OTFS variants, modulation orders, mobility conditions, coding, and complexity comparison.
- The single-network DD-domain framing is simpler operationally than configuring multiple time-domain RCs.
- The paper states a clear advantage over estimated-CSI model-based methods in settings where accurate CSI is difficult.

## Weaknesses

- Experiments were not reproduced and no official implementation was found in inspected sources.
- HTML extraction does not preserve all equations and symbols, limiting formula-level review.
- The paper's empirical support appears simulation-based in the inspected source; real-world OTA measurements were not identified in this run.
- The privacy and robustness implications of learning channel-specific structure are not deeply explored in the inspected paper.
- Related DEP synthesis is conceptual and should not be mistaken for independent validation of wireless detection claims.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish reproducible simulation scripts | Reproducibility | BER/BLER and complexity claims need runnable traces. | Higher reviewer confidence and easier comparison. | Requires code cleanup and parameter documentation. | Recreate figures and compare against paper curves. |
| Add privacy leakage tests | Privacy | Channel-sensitive models may learn device or environment fingerprints. | Safer wireless ML deployment. | Requires careful synthetic and authorized data design. | Test identity prediction from intermediate features under controlled synthetic traces. |
| Report ablations for each structure component | Method clarity | Phase compensation, padding, and filtering should be separable. | Clearer causal understanding of gains. | Extra experiments and paper space. | Remove one component at a time and report BER/BLER deltas. |
| Add real-world or hardware-in-loop checks | Deployment relevance | Simulation may miss radio hardware impairments. | Better external validity. | Hardware access and calibration burden. | Compare synthetic, emulator, and OTA traces under matched pilot overhead. |
| Create evidence-ledger outputs | Auditability | Online detectors are hard to review after failures. | Easier debugging and DEP-style preservation. | More logging and storage. | Store pilot maps, confidence, decisions, and failure cases for sampled subframes. |

## Potential Implementations

1. `OTFS Detector Audit Harness`
   - `User`: Wireless ML researcher.
   - `Goal`: Run toy OTFS detection experiments while preserving pilot maps, detector choices, and confidence traces.
   - `Core mechanism`: Generate synthetic OTFS frames, apply a 2D-RC-like detector, and export per-subframe evidence ledgers.
   - `Required inputs`: Synthetic channel parameters, pilot positions, modulation order, detector configuration, and evaluation metrics.
   - `Outputs`: BER/BLER table, complexity estimates, evidence ledger, and failure case samples.
   - `Risk controls`: Synthetic data by default; no device identity traces; clear simulation disclaimers.
   - `Evaluation`: Match known baseline behavior on a small reproducible scenario.

2. `Wireless Privacy Feature Probe`
   - `User`: Privacy reviewer for wireless ML systems.
   - `Goal`: Test whether model features reveal device or channel identity beyond the intended detection target.
   - `Core mechanism`: Train auxiliary classifiers on synthetic intermediate features and check identity leakage under controlled labels.
   - `Required inputs`: Synthetic device/channel labels, detector features, and privacy thresholds.
   - `Outputs`: Leakage report, risky feature list, and mitigation suggestions.
   - `Risk controls`: No real device tracking; authorized datasets only; aggregate reporting.
   - `Evaluation`: A privacy probe should stay near chance when identity features are not intentionally present.

3. `Communication State Mapper`
   - `User`: Agent or network-system reviewer.
   - `Goal`: Compare physical communication state, multi-agent channel state, and authentication state under one review vocabulary.
   - `Core mechanism`: Represent observed state, trusted state, inferred state, and retained evidence as separate fields.
   - `Required inputs`: Source references, channel graph, authentication assumptions, and state evidence.
   - `Outputs`: Review table, relationship graph, and next-source queue.
   - `Risk controls`: Treat source texts as evidence only; avoid operational attack detail; preserve uncertainty.
   - `Evaluation`: Every relationship edge must cite a source or evidence ledger item.

## Three Ways to Exercise This Research

1. `Build a toy ledger`: Objective: create a synthetic OTFS-like grid and record pilot positions, predicted symbols, confidence scores, and failure notes. Inputs: synthetic frames and toy channel parameters. Method: implement data structures first, then plug in simple baseline detectors. Output: evidence ledger and error table. Success criterion: every error can be traced to an input region and detector decision. Safety boundary: synthetic data only.
2. `Ablate structure`: Objective: test the importance of 2D circular padding and 2D filtering in a small synthetic detector. Inputs: toy delay-Doppler grids and controlled noise. Method: compare full, no-padding, and flattened baselines. Output: ablation table. Success criterion: differences are measurable and tied to a known structural change. Safety boundary: no claims about real radios without real validation.
3. `Probe privacy`: Objective: check whether intermediate detector features encode unintended identity labels. Inputs: synthetic channel/device labels and detector states. Method: train a simple auxiliary classifier on held-out synthetic traces. Output: leakage score and mitigation note. Success criterion: leakage is either near chance or clearly explained. Safety boundary: no real device fingerprinting or unauthorized wireless capture.

## Example MVP Product

- `Product name`: Delay-Doppler Review Bench
- `Target user`: Wireless ML researchers and Black-Lake reviewers.
- `Problem`: OTFS detection papers report performance curves, but reviewers need reproducible evidence traces, privacy checks, and source-grounded comparisons.
- `Core workflow`: Select a public OTFS paper, enter simulation parameters, run or import synthetic detector outputs, generate an evidence ledger, and export a DEP-ready review packet.
- `Data requirements`: Public paper metadata, synthetic frame configurations, pilot maps, detector outputs, confidence scores, baseline metrics, and source references.
- `Architecture`: Local CLI with paper metadata parser, synthetic OTFS scenario generator, detector adapter interface, evidence-ledger writer, privacy probe, and Markdown artifact exporter.
- `Success metrics`: Reproduced baseline sanity checks, percentage of claims with source traces, number of failure cases with evidence records, and zero local-path leaks in exported artifacts.
- `Risk controls`: Synthetic data by default, no unauthorized radio capture, no device tracking, source-file redistribution checks, and sanitization gate before export.
- `Limitations`: MVP would not reproduce the full paper without official parameters and code; it would provide a review scaffold and small-scale validation path.
- `MVP boundary`: Local-only research tool; not a deployed receiver or privacy audit for real devices.
- `Evaluation plan`: Smoke tests on synthetic grids, schema validation for manuscripts, sanitization scans, and reviewer assessment of evidence trace usefulness.
- `Failure modes`: Incorrect simulation assumptions, missing formula details, overgeneralized results, and privacy probe false negatives.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| 2D-RC | Primary paper | Reviewed work on 2D reservoir computing for OTFS symbol detection. | https://arxiv.org/abs/2311.08543 |
| Agent State Review | Related Black-Lake DEP | State, evidence replay, and runtime monitoring concepts useful for detector evidence ledgers. | Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md |
| Black-Lake-Data DEP-20260626-Tech Intel 0103 | Related DEP entry | Contains Wi-Fi privacy/ML fingerprinting source connecting wireless signals and ML privacy risk. | Black-Lake-Data/.lake-data/DEP-20260626-Tech Intel 0103/daily_research_findings_2026-06-26_0103.md |
| Can Machine Learning Break Wi-Fi Privacy? | Related primary source basis | Wireless ML/privacy neighbor referenced by the related DEP. | https://arxiv.org/abs/2606.25788 |
| Black-Lake-Data DEP-20260701-Tech Intel 0103 | Related DEP entry | Contains communication-channel security and quantum-network authentication source bases. | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md |
| MESA | Related primary source basis | Communication-channel risk ranking for multi-agent systems. | https://arxiv.org/abs/2606.30602 |
| Authentication in Quantum Networks | Related primary source basis | Communication authentication assumptions and deployment constraints. | https://arxiv.org/abs/2606.30636 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2311.08543 | Selected paper metadata, abstract, authors, version dates, DOI, and subjects. | 2026-07-09 | Primary arXiv metadata page inspected. |
| R2 | https://arxiv.org/html/2311.08543 | Selected paper method, experiments, complexity discussion, conclusion, and appendix context. | 2026-07-09 | arXiv HTML full text inspected; formulas may be incomplete as text. |
| R3 | https://doi.org/10.48550/arXiv.2311.08543 | Persistent DOI reference. | 2026-07-09 | DOI recorded from arXiv metadata. |
| R4 | Local arXiv archive readme.md, path withheld | Selection provenance and local PDF/readme presence. | 2026-07-09 | Local path withheld; no source file redistributed. |
| R5 | Black-Lake/README.md | DEP class, README, log, report, attribution, and commit-message standards. | 2026-07-09 | Live README inspected after fetch. |
| R6 | Black-Lake-Data/README.md | Related repository DEP layout and attribution expectations. | 2026-07-09 | Live README inspected after fetch. |
| R7 | Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md | Related state/evidence-control synthesis. | 2026-07-09 | Related DEP artifact inspected. |
| R8 | Black-Lake-Data/.lake-data/DEP-20260626-Tech Intel 0103/daily_research_findings_2026-06-26_0103.md | Related wireless privacy and ML fingerprinting context. | 2026-07-09 | Related DEP entry inspected. |
| R9 | https://arxiv.org/abs/2606.25788 | Primary source basis for Wi-Fi privacy finding referenced by related DEP. | 2026-07-09 | Referenced through related entry. |
| R10 | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md | Related communication-channel security and authentication context. | 2026-07-09 | Related DEP entry inspected. |
| R11 | https://arxiv.org/abs/2606.30602 | Primary source basis for MESA referenced by related DEP. | 2026-07-09 | Referenced through related entry. |
| R12 | https://arxiv.org/abs/2606.30636 | Primary source basis for quantum-network authentication referenced by related DEP. | 2026-07-09 | Referenced through related entry. |

## Appendix

### Random Selection and Eligibility Record

- Automation name: Black Lake Arxiv DEP.
- Public run date: 2026-07-09.
- PDF candidate enumeration: `rg --files -g "*.pdf"` over the local arXiv archive.
- Candidate count: 64,657 PDFs.
- Random method: uniform random index with PowerShell `Get-Random`.
- Selected index: 43,290.
- Selected identifier: `arXiv:2311.08543`.
- Selected title: `2D-RC: Two-Dimensional Neural Network Approach for OTFS Symbol Detection`.
- Dedup scan locations: `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, automation memory, and related Black-Lake-Data context.
- Duplicate/reselection count: 0.
- 24-hour cutoff: 2026-07-08 date boundary.
- Source files collected into this DEP: none.

### Validation Checklist

- Required manuscript headings are present.
- YAML `title` and H1 are identical and under 40 characters.
- Evidence ledger exists and maps claims to inspected sources.
- Author claims and reviewer interpretations are separated.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- `## Example MVP Product` includes required MVP fields.
- Related research includes exactly three related DEP entries used for synthesis plus their source bases.
- Public artifacts avoid local absolute paths, local usernames, machine identifiers, local timezone labels, and exact local execution timestamps.
