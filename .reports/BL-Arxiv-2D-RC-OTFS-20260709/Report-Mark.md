# Report-Mark: 2D-RC OTFS

Public run date: 2026-07-09

## Source Metadata

| Field | Value |
|---|---|
| Title | 2D-RC: Two-Dimensional Neural Network Approach for OTFS Symbol Detection |
| Authors | Jiarui Xu, Karim Said, Lizhong Zheng, Lingjia Liu |
| Identifier | arXiv:2311.08543 |
| DOI | https://doi.org/10.48550/arXiv.2311.08543 |
| Version inspected | v2, revised 2024-01-25 |
| Submitted | 2023-11-14 |
| Subjects | Signal Processing; Artificial Intelligence; Machine Learning |
| License observed | CC BY 4.0 on arXiv HTML |
| Primary sources inspected | https://arxiv.org/abs/2311.08543 ; https://arxiv.org/html/2311.08543 |
| Local archive status | Local readme and PDF presence observed; local path withheld; source files not redistributed. |

## Concise Research Notes

`2D-RC` addresses online symbol detection for orthogonal time frequency space (OTFS) systems in high-mobility wireless channels. The paper starts from a practical constraint: model-based OTFS detectors often rely on channel state information, while prior reservoir-computing detection used multiple time-domain RCs and did not encode OTFS-specific delay-Doppler structure.

The method introduces a two-dimensional reservoir-computing detector that operates in the delay-Doppler domain. Its main architectural move is to encode the two-dimensional circular channel interaction using phase compensation, 2D windowing, 2D circular padding, and a 2D filtering structure. The authors state that this lets a single neural network perform online subframe-based detection using limited over-the-air pilot symbols.

The inspected arXiv HTML reports numerical experiments across RCP-OTFS and CP-OTFS variants, QPSK and 16 QAM modulation, different mobility settings, and an LDPC-coded case. The paper reports that 2D-RC outperforms the prior 1D-RC baseline and model-based LMMSE, MPA, and LSMR detectors using estimated CSI. In the coded CP-OTFS scenario, the authors report about 2 dB to 3 dB BLER gain over conventional estimated-CSI model-based approaches at the target BLER discussed in the paper.

Limitations for this review: the PDF was not text-extracted locally, equations in the arXiv HTML are partially rendered without symbol text, no official implementation was found in the inspected sources, and experiments were not reproduced. Reviewer interpretation: the useful transferable idea is not only "use a neural detector"; it is "embed a known interaction geometry into an online learner so scarce pilots and shifting channel state become tractable."

Implementation relevance: 2D-RC is a candidate pattern for online, resource-aware inference in systems where structured state and local observations matter. For Black-Lake, it bridges physical-layer communication, online learning, state tracking, and structured evidence/control deposits.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Notes |
|---|---|---|---|---|
| E1 | arXiv abstract page for `2311.08543` | Title, authors, version dates, DOI, subjects, abstract, comments. | High | Primary metadata source. |
| E2 | arXiv HTML for `2311.08543v2` | Method, system model, experiments, complexity discussion, conclusion. | High for source claims; low for reproduced validity | HTML equations may omit symbols. |
| E3 | Local archive readme | Archive provenance and local PDF/readme presence. | Medium | Local path withheld; local PDF not redistributed. |
| E4 | Black-Lake README | DEP naming, README, log, report, attribution, and commit-message rules. | High | Repository policy source. |
| E5 | Black-Lake-Data README | Related DEP layout and attribution rules. | High | Repository policy source. |
| E6 | Three related DEP entries | Synthesis anchors for wireless/privacy, communication security, and state-control analogies. | Medium | Related entries are prior DEP artifacts and generated findings, not direct validation of 2D-RC. |

## Related DEP Entries

1. `Black-Lake/.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md`
   - Reason selected: 2D-RC depends on online state adaptation and evidence from limited pilots; this DEP frames state, evidence replay, and monitoring as review objects in agent systems.
   - Source basis: Agent State Review source metadata and synthesis sections on persistent state, evidence replay, and runtime monitoring.

2. `Black-Lake-Data/.lake-data/DEP-20260626-Tech Intel 0103/daily_research_findings_2026-06-26_0103.md`
   - Reason selected: Its Wi-Fi privacy finding is the closest inspected communications-adjacent source, connecting wireless physical signals, machine learning, and privacy-sensitive device behavior.
   - Source basis: Finding 9, "Can Machine Learning Break Wi-Fi Privacy?", with arXiv source `2606.25788`.

3. `Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md`
   - Reason selected: Its MESA and quantum-network authentication findings connect communication channels, graph security, authentication assumptions, and deployment constraints.
   - Source basis: Finding 2, MESA multi-agent communication-channel security, and Finding 10, Authentication in Quantum Networks.

## Synthesis Note

### Concept Bridge

2D-RC is about using domain structure to make online learning viable under scarce, noisy observations. The related DEP entries approach the same meta-problem from adjacent systems: Agent State Review asks how state and evidence should be captured for later audit; the Wi-Fi privacy entry asks what machine learning can infer from wireless-side metadata; and the communication-security entry asks how channels, edges, and authentication assumptions affect downstream trust. Together they point to a general design pattern: treat communication state as structured, observable, and reviewable, then choose learning and control mechanisms that respect the geometry and security assumptions of that state.

### Potential Implementations

1. `Delay-Doppler Evidence Ledger`: Capture OTFS pilot positions, observed delay-Doppler neighborhoods, model outputs, and detector confidence as a reviewable ledger for each subframe.
2. `Wireless Privacy Stress Harness`: Use synthetic Wi-Fi and OTFS-style feature traces to test whether learning pipelines leak device or channel identity beyond the intended detection task.
3. `Channel-Aware Agent Router`: Apply the 2D-RC principle to multi-agent communication graphs by embedding known channel topology into routing or monitoring decisions instead of treating messages as flat text.

### Deeper Relationship Observations

1. 2D-RC and the state-review DEP both distinguish raw history from structured state; the useful unit is not every received sample or every context token, but the state representation that preserves decision-relevant structure.
2. Wireless ML privacy and OTFS detection share a caution: learning systems can exploit subtle channel or device signatures, so performance gains and privacy leakage can arise from the same feature sensitivity.
3. MESA and quantum-network authentication show that communication reliability is not only about signal recovery; the trusted edge, principal, and authentication resource matter as much as the detector.

### Conceptual Similarities

1. All three bridges use structure to reduce ambiguity: delay-Doppler circularity, wireless fingerprint features, and communication graph edges.
2. All three involve partial observation, where the system must infer useful state from limited pilots, noisy probes, logs, or authentication assumptions.
3. All three benefit from explicit evidence records, because later reviewers need to know which observations justified a detection, routing, privacy, or authorization decision.

### MVP Implementations with Code Mock-Ups

1. `Pilot Evidence Ledger`

```python
def record_subframe(run_id, pilots, predictions, confidence):
    return {
        "run_id": run_id,
        "pilot_count": len(pilots),
        "observed_cells": [(p["delay"], p["doppler"]) for p in pilots],
        "detector": "2d_rc_like",
        "confidence": round(confidence, 4),
        "review_status": "needs_validation" if confidence < 0.8 else "accepted",
    }
```

2. `Wireless Feature Privacy Check`

```python
def privacy_probe(features, allowed_fields):
    unexpected = sorted(set(features) - set(allowed_fields))
    return {
        "unexpected_features": unexpected,
        "risk": "review" if unexpected else "low",
        "note": "Synthetic feature audit only; no device tracking.",
    }
```

3. `Structured Channel Monitor`

```python
def rank_channel_edges(edges, signal_quality, trust_score):
    ranked = []
    for edge in edges:
        risk = (1 - signal_quality[edge]) + (1 - trust_score[edge])
        ranked.append((edge, round(risk, 3)))
    return sorted(ranked, key=lambda item: item[1], reverse=True)
```

### Developer Challenges

1. Build an OTFS toy simulator that records every pilot, detector decision, and confidence score in a source-grounded review ledger.
2. Add privacy tests that check whether a detector learns device identity proxies or channel fingerprints unrelated to the intended symbol-detection task.
3. Design a communication-channel monitor that can handle both physical signal quality and logical trust assumptions without collapsing them into one score.

### Author Challenges

1. Release or document enough simulation code and parameter settings for independent reviewers to reproduce the BER, BLER, and complexity comparisons.
2. Add privacy and robustness analysis that tests whether 2D-RC encodes persistent device/channel signatures beyond the intended OTFS detection objective.
3. Extend the paper's domain-structure argument into a broader taxonomy of when reservoir computing should encode physical channel geometry versus learn it implicitly.

## Validation Notes

- Candidate selection used `rg --files -g "*.pdf"` over the local archive, counted 64,657 PDFs, and selected uniform random index 43,290.
- The accepted paper unit was `arXiv:2311.08543`; duplicate marker checks found no prior Black Lake Arxiv DEP artifacts for the identifier, normalized title, or slug.
- Duplicate/reselection count was 0.
- 24-hour cutoff was recorded at date boundary 2026-07-08.
- Repository scans covered `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, automation memory, and related Black-Lake-Data context.
- No source files were collected into this repository. The local archive readme and PDF presence were observed, but local paths and source files are withheld from public artifacts.
- Public-output sanitization was applied before staging; local absolute paths, user/machine identifiers, local timezone labels, and exact local execution timestamps are intentionally absent.

## Attribution Block

- Source URL: https://arxiv.org/abs/2311.08543
  - Applies to: selected paper metadata, abstract, version, DOI, subjects, and authors.
  - Notes: Primary arXiv abstract page inspected.
- Source URL: https://arxiv.org/html/2311.08543
  - Applies to: selected paper method, experiments, complexity discussion, and conclusion.
  - Notes: arXiv HTML full text inspected; formula extraction is incomplete where HTML omits symbols.
- Source URL: https://doi.org/10.48550/arXiv.2311.08543
  - Applies to: persistent identifier for selected paper.
  - Notes: DOI recorded from arXiv metadata.
- Source file: local arXiv archive readme.md, path withheld
  - Applies to: archive provenance and confirmation of local PDF/readme presence.
  - Notes: Local path and local execution context withheld by sanitization policy.
- Repository file: `Black-Lake/README.md`
  - Applies to: output repository DEP, report, log, attribution, and commit-message rules.
  - Notes: Live README read after fetch.
- Repository file: `Black-Lake-Data/README.md`
  - Applies to: related DEP repository layout and attribution expectations.
  - Notes: Live README read after fetch.
- Repository file: `Black-Lake/.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md`
  - Applies to: related state/evidence-control synthesis.
  - Notes: Related DEP entry inspected.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260626-Tech Intel 0103/daily_research_findings_2026-06-26_0103.md`
  - Applies to: related wireless ML privacy finding.
  - Notes: Related DEP entry inspected.
- Source URL: https://arxiv.org/abs/2606.25788
  - Applies to: Wi-Fi privacy and ML fingerprinting source basis referenced by related DEP.
  - Notes: Referenced through inspected related DEP entry.
- Repository file: `Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md`
  - Applies to: related communication-channel security and quantum-network authentication findings.
  - Notes: Related DEP entry inspected.
- Source URL: https://arxiv.org/abs/2606.30602
  - Applies to: MESA multi-agent communication-channel security source basis referenced by related DEP.
  - Notes: Referenced through inspected related DEP entry.
- Source URL: https://arxiv.org/abs/2606.30636
  - Applies to: quantum-network authentication source basis referenced by related DEP.
  - Notes: Referenced through inspected related DEP entry.
