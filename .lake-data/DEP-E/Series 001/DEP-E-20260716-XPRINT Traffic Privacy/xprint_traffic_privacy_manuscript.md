---
title: "XPRINT Traffic Privacy - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Defensive source-grounded review of cross-platform encrypted-traffic behavior fingerprinting and privacy leakage."
source_status: "verified complete PDF and official full-paper HTML inspected; source and traffic files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:2509.00706v1 and bounded public code/data availability checks inspected through 2026-07-16"
primary_url: "https://arxiv.org/abs/2509.00706v1"
stable_identifier: "arXiv:2509.00706v1; DOI 10.48550/arXiv.2509.00706"
confidence_summary: "High for method and table transcription; medium for tested generalization; low for deployment-wide open-world conclusions."
safety_scope: "defensive privacy evaluation, countermeasure research, and authorized local auditing only"
distribution_notes: "Original documents, packet/URI traces, models, cache records, extracted text, and archive records remain local and are not redistributed."
---

# XPRINT Traffic Privacy - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | Usage Notes | Status |
|---|---|---|---|---|---|---|---|
| S1 | X-PRINT: Platform-Agnostic and Scalable Fine-Grained Encrypted Traffic Fingerprinting | Primary metadata | arXiv record | 2509.00706v1; DOI 10.48550/arXiv.2509.00706 | https://arxiv.org/abs/2509.00706v1 | Identity, authors, date, subject, license | Inspected |
| S2 | Complete paper | Primary artifact | PDF and official full-paper HTML | v1, 2025-08-31 | https://arxiv.org/pdf/2509.00706; https://arxiv.org/html/2509.00706v1 | Verified local copies withheld | Inspected in full |
| S3 | Telecom AI Roadmap | Related DEP | Manuscript | DEP-E-20260711 | `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` | Network governance context | Inspected |
| S4 | Agent Memory Forensics | Related DEP | Manuscript | DEP-E-20260711 | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` | Channel-specific forensic calibration | Inspected |
| S5 | Control Surfaces | Related DEP | Manuscript | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md` | Purpose-bound privacy and telemetry controls | Inspected |
| S6 | Black Lake and Black Lake Data READMEs | Repository authority | Markdown | live default branches | https://github.com/Delphoa/Black-Lake; https://github.com/Delphoa-Labs/Black-Lake-Data | Filing and source-locality contracts | Inspected |

The authors are YuKun Zhu, ManYuan Hua, Hai Huang, YongZhao Zhang, Jie Yang, FengHua Xu, RuiDong Chen, XiaoSong Zhang, JiGuo Yu, and Yong Ma. The record lists Cryptography and Security and a CC BY-NC-ND 4.0 license. No publisher venue, non-arXiv DOI, official code repository, traffic corpus, trained model, URI-map release, or collection-script release was identified.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|
| E1 | S1-S2 | Metadata, threat model, complete design, Tables 1-11, appendices, discussion | Identity, mechanism, author-reported results | High for transcription | No reproduction |
| E2 | S2, Sections 3-5 | Controlled URI labeling, shared/private analysis, four-model cascade, URI maps | System reconstruction | High | Privileged training environment; implementation unavailable |
| E3 | S2, Table 4 | Cross-platform app and behavior precision/recall/F1 | Main comparative claim | High for reporting | Custom data/splits; baseline adaptation fairness |
| E4 | S2, Tables 5-6 | Burst threshold and URI-map ablation | Component behavior | High for reporting | Selected apps/categories |
| E5 | S2, Tables 7-9 | Unseen platform/application/version tests | Generalization claim | High for transcription | Narrow target sets; tuned thresholds; coarse-filter scope |
| E6 | S2, Table 11 | Automated-to-human transfer | Collection realism claim | High for reporting | Five volunteers; same platforms/environment; prose/table tension |
| E7 | S2, Discussion | Padding, delay, transformation; Tor and pinning limits | Countermeasures and scope | High | No measured defense trade-off |
| E8 | S3-S5 | Telecom governance, forensic calibration, purpose-bound privacy | Cross-DEP synthesis | Medium | Conceptual; not validation evidence |
| E9 | Process records | Random selection, dedup, repair, cache, no-source gate | Workflow validity | High | Operational evidence only |

## Executive Summary

X-PRINT is a traffic-analysis attack framework showing that encrypted payloads can still reveal application behaviors through packet size, direction, and timing. Its central hypothesis is that backend URI invocation patterns are more stable across Android, iOS, desktop, new platforms, and app versions than client-side UI or instrumentation features.

The system learns URI labels in a controlled environment where researchers can associate decrypted requests with encrypted-flow side channels. It then uses only encrypted metadata at inference. A coarse stage filters irrelevant applications; application-specific models classify bursts into likely URI labels; temporally structured canonical URI maps combine URI confidence and ordering to identify behavior. For flagged unseen cases, the method removes platform/application-specific private URIs and matches on shared URIs.

Table 4 reports cross-platform behavior precision/recall/F1 of 0.970/0.970/0.965 for X-PRINT versus 0.794/0.436/0.515 for FOAP. Table 6 reports average behavior FNR/FPR of 0.037/0.012 with URI maps versus 0.172/0.072 for an unordered URI-set baseline. Unseen targets remain harder: full X-PRINT F1 is about 0.747/0.744 for SmartTV/iOS17, 0.736 across unseen applications, and 0.717 across version shifts.

The privacy implication is stronger than the product implication: transport encryption alone does not guarantee behavior confidentiality. The defensible use is to evaluate countermeasures and minimize leakage. The evidence does not support user monitoring. Dataset and code are unavailable; URI labels require privileged interception during training; threshold selection and open-world filtering narrow the setting; network and population diversity are limited; and defenses are not benchmarked.

## Detailed Summary

### Threat and Observation Model

The real-world observer is assumed to see encrypted packet metadata—size, direction, timing, and flow grouping—but not plaintext URIs. The model is trained in a controlled environment where URI labels can be associated with traffic. X-PRINT focuses on application and fine-grained behavior inference, such as distinguishing actions within an application.

This distinction matters. The deployed inference does not require plaintext access, but building the labeled training set does. The authors use controlled interception and certificate-validation bypass where necessary. Such collection should occur only on owned or explicitly authorized devices/accounts under applicable law and institutional review.

### URI Invariance Study

The paper separates URIs into shared paths observed across platforms and private paths specific to one platform/application variant. Shared-URI packet proportions range from about 30% to 89% in the studied applications. Shared URI traffic is more similar across platform pairs than private URI traffic. Canonical URI sequences also repeat with substantial frequency while preserving behavior-specific anchors.

The mechanism is plausible because multiple clients call common backend services. It may weaken when platforms use distinct providers, endpoints are highly personalized, clients aggressively multiplex traffic, or backend deployments change. The paper's examples do not establish a universal invariant.

### Coarse and Fine Pipeline

X-PRINT first extracts flow-level metadata and learns a similarity/filtering model to remove traffic judged irrelevant. It does not claim this stage fully identifies every application; it narrows candidate space. Fine processing splits flows into bursts using temporal gaps and predicts a URI label/confidence for each burst with application-specific classifiers.

Predicted URI sequences are grouped by domain and compared with behavior-specific canonical URI maps. Matching uses temporal order, confidence gating, coverage, and a penalty for expected URIs not observed. This is more expressive than simple set overlap because it retains sequence structure and confidence.

For unseen cases, X-PRINT uses a similarity threshold and suppresses private URIs. The refinement assumes shared URIs are reliable anchors and unseen private URIs are noise. It is useful when an unseen target shares a backend/function with training applications; it cannot infer unrelated applications with no meaningful overlap.

### Dataset Construction

The authors report downloading 500 popular applications from each mobile store and collecting corresponding desktop/native versions where available, spanning 29 categories. Applications requiring credit-card information at registration were excluded. Airtest performs 1,000 random clicks per application across 50 traffic instances, with 20 clicks per instance. Android devices/emulation, two iPhones, and desktop virtual machines share one network.

Actions are associated manually with decrypted URI timestamps in the controlled environment. Four model families are built: flow-level similarity, logistic flow filtering, burst-level URI classification, and canonical URI maps. The paper says no public dataset was available, but it does not release the new dataset inspected here.

### Cross-Platform Evidence

Instances are split 40/10 for train/test. Test traffic probabilistically merges two random instances with 0-5-second delay to emulate concurrent users. X-PRINT app F1 is 0.977 and behavior F1 0.965. FOAP behavior F1 is 0.515; an extended FOAP using URI-level data reaches 0.877. This shows both the URI labels and the X-PRINT temporal design contribute.

Recall variance for X-PRINT app recognition is large (0.940 plus/minus 0.142), which deserves per-application analysis. Baseline extension uses the authors' URI dataset, so fairness depends on equivalent tuning and access that independent reviewers cannot verify.

### Burst and URI-Map Evidence

For URI classification, a 500 ms inter-burst threshold gives the best reported F1 of 0.848. Shorter gaps fragment requests; larger gaps mix URIs. This threshold is network- and workload-sensitive and should not be treated as universal.

URI maps reduce selected-category average FNR from 0.172 to 0.037 and FPR from 0.072 to 0.012 relative to unordered URI matching. Music is hardest for the baseline. The ablation supports temporal/confidence structure, though category and application sampling are narrow.

### Open-World Evidence

Thresholds are chosen using a grid search over 20 known and 20 unseen applications, with coverage penalty at most one and unseen threshold 0.3. Unseen-platform tests train on Android, iOS15, and Windows and target SmartTV or iOS17 for 20 aligned apps. Full X-PRINT reports F1 0.747 and 0.744, compared with FOAP 0.501 and 0.517.

For 10 known/10 unseen applications in each of Video, Social, and Music, full X-PRINT averages precision/recall/F1 0.792/0.718/0.736. Across an 11-month application-version gap, averages are 0.825/0.679/0.717. These results are useful but materially below closed cross-platform F1 0.965.

The “open world” excludes unrelated applications through coarse filtering and evaluates targets intentionally sharing functions/backends. This is a bounded open set, not arbitrary internet traffic. The filter's own false negatives and false positives need end-to-end denominators.

### Human-Operation Transfer and Countermeasures

Appendix C adds five volunteers, 100 applications, and 500 traffic instances. Table 11 reports automated-to-automated and automated-to-human F1 both 0.927, while training with four volunteers and testing the held-out volunteer reports F1 0.950. The prose later says the final setting attains perfect metrics, which conflicts with the table; the table is treated as the stronger structured evidence.

The paper names packet padding, randomized delays, and traffic transformation as countermeasures, with overhead trade-offs. It does not test them. Tor-like fixed-cell multiplexing prevents the modeled semantic separation, and certificate pinning complicates label collection. These limits reinforce the defensive conclusion: reducing side-channel structure can protect privacy.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| Backend URI patterns can provide cross-platform behavior anchors. | Author empirical/mechanistic | E2-E5 | Supported for studied shared-backend applications. | Medium-high |
| X-PRINT improves cross-platform behavior F1 by about 0.45 over FOAP. | Author empirical | E3 | 0.965 minus 0.515 equals 0.450. | High for reporting |
| URI maps improve FNR/FPR over unordered URI matching. | Author empirical | E4 | Supported in three selected categories. | Medium-high |
| Private-URI removal improves unseen-case inference. | Author empirical | E5 | Full method exceeds no-refinement in tested shifts. | Medium |
| X-PRINT is scalable and robust in open-world settings. | Author interpretation | E5-E6 | Evidence covers bounded related unseen targets; universal wording is too broad. | Medium-low |
| Airtest data reproduces human behavior well. | Author empirical | E6 | Similar F1 in one same-environment study; five volunteers and prose/table discrepancy limit generality. | Medium-low |
| Encryption prevents behavior inference. | Common assumption challenged | E1-E5 | Contradicted in the tested metadata threat model. | Medium-high |

## Methodology

Candidate enumeration used `rg --files -g "*.pdf"` over the local archive and treated each PDF parent as one unit. A uniform PowerShell `Get-Random` draw selected zero-based index 44,195 from 75,776 units (75,777 PDFs). The first draw was eligible; exclusions and reselections were zero.

Dedup validation covered arXiv ID, DOI, normalized title, slug, public pointer, logs, reports, DEP-E manuscripts, automation memory, companion repository, and same-paper markers within 24 hours. No prior substantive artifact was found.

The source began `partial`: the 1,824,393-byte PDF passed header and EOF checks, but full-paper HTML was absent. One official arXiv HTML request and one metadata request succeeded. Full HTML passed at 312,956 bytes, 89,178 body characters, two document markers, 84 headings/sections, and seven structure terms. Local provenance records were updated; zero partials remained.

The document extractor ran `missing-only` against the paper unit and central cache. The initial miss became `cached` in 0.849 seconds using `pypdf` and `html-regex`, producing 92,377 and 88,946 bytes of text. No source package was collected. Review inspected the full threat model, design, Tables 1-11, appendices, discussion, countermeasures, and limitations. No packet capture, interception, behavior inference, model execution, or dataset collection occurred.

## Scope, Constraints, and Assumptions

- Scope is defensive privacy analysis, evidence quality, countermeasure translation, and three related Black Lake entries.
- Author-reported values were transcribed but not reproduced.
- The controlled labeling procedure is evidence, not an instruction; operational interception is out of scope.
- Open-world claims are interpreted within the paper's coarse-filtered, related-application target universe.
- URI paths and traffic features can be sensitive even without payload content; none are redistributed.
- Code/data absence is based on the inspected paper and bounded public searches at the cutoff.
- Legal and ethical requirements vary by jurisdiction; this artifact is not legal advice.

## Observations

- Server-side invariants can outlast client UI/platform changes, but common backend ownership is a hidden dependency.
- The large gap between FOAP and extended FOAP shows that labeling granularity contributes substantially, not only the matching algorithm.
- Closed cross-platform F1 0.965 falls to roughly 0.72-0.75 for unseen cases, clarifying the real generalization cost.
- Coarse filtering removes unrelated traffic from the evaluated open world, so end-to-end filter errors matter.
- The 500 ms burst threshold is a learned environmental parameter, not a protocol constant.
- URI maps improve both average error and variance in selected categories.
- Unreleased data prevents auditing application overlap, account effects, sensitive parameters, and split leakage.
- Metadata can be identifying and behavioral even when content is encrypted.
- The table/prose discrepancy in the human-transfer appendix should be corrected before reuse.

## Considerations

### Defensive Countermeasure Evaluation

Evaluate padding, batching, delays, multiplexing, cover traffic, and transformation under the strongest authorized classifier. Report behavior leakage alongside bandwidth, latency, energy, reliability, and accessibility costs. Prefer provider-side or client-side protections that do not require retaining user-level trace archives.

### Privacy and Authorization

URI labels can reveal searches, media, health, finance, communication, and account actions. Collection needs informed authorization, purpose limitation, data minimization, short retention, access logging, parameter redaction, and breach planning. Researchers should not weaken certificate validation on devices or accounts they do not control.

### Evaluation Integrity

Use nested threshold selection, application/provider-disjoint splits, independent networks, and fixed end-to-end denominators including coarse-filter misses. Publish category, application, account, device, network, and time-shift performance with calibrated uncertainty.

### Abuse Boundary

Fine-grained fingerprinting can support surveillance, censorship, stalking, advertising, or employee monitoring. Implementations should be restricted to authorized privacy testing and countermeasure validation, with no identity linkage or real-user monitoring.

## Strengths

- The server-centric hypothesis directly addresses platform-dependent client instrumentation.
- The pipeline separates coarse filtering, URI classification, temporal behavior matching, and unseen refinement.
- Evaluation includes Android, iOS, Windows, SmartTV, version shifts, applications, interleaved traffic, and human transfer.
- Tables report precision, recall, F1, variability, FNR, and FPR rather than accuracy alone.
- URI-map and private-URI ablations support the proposed structure.
- The paper states Tor/certificate-pinning limits and names countermeasure families.

## Weaknesses

- Dataset, code, URI maps, scripts, labels, and model artifacts are unavailable.
- Privileged MitM labeling complicates ethics, legality, reproducibility, and platform coverage.
- Device/network/geographic/account diversity is narrow and traffic shares one collection network.
- Coarse filtering narrows open-world scope, but its complete end-to-end errors are not foregrounded.
- Thresholds are tuned on in-domain data without a fully independent nested protocol.
- Baseline extension fairness and optimization budgets are not independently auditable.
- Countermeasures are not experimentally evaluated.
- Human transfer has five volunteers and a table/prose discrepancy.
- Sensitive URI parameters, consent, retention, and annotator governance are underdocumented.

## Potential Improvements

1. Release a privacy-reviewed, redacted benchmark with scripts, hashes, splits, labels, code, and licenses.
2. Separate provider/app/account/device/network/time domains and prevent shared-backend leakage across train/test.
3. Use nested validation for burst, coverage, confidence, and unseen thresholds.
4. Report end-to-end filter, classification, matching, abstention, and unrelated-traffic denominators.
5. Benchmark countermeasures under matched privacy/utility budgets.
6. Add cross-network, cross-region, accessibility, background-load, QUIC/TLS, VPN, and multiplexing tests.
7. Expand human-operated evaluation with consented participants and subgroup/privacy governance.
8. Correct the Table 11/prose discrepancy and publish raw aggregate run results.
9. Calibrate confidence and expose abstention rather than forced behavior labels.
10. Add an explicit ethics/misuse section and data-retention threat model.

## Potential Implementations

### Local Leakage Auditor

An offline defensive harness that runs only on owned traffic fixtures, measures whether behaviors remain distinguishable, and emits aggregate risk/overhead metrics without exporting packet traces or URI paths.

### Countermeasure Pareto Bench

A provider/client testbed comparing padding, delay, batching, multiplexing, and transformation across leakage F1, bandwidth, latency, energy, and failure rates. Results must use nested threshold selection and independent domains.

### Telemetry Minimization Gate

A schema/policy validator that rejects raw URI parameters, identity/account fields, payloads, and long-lived trace identifiers; permits only bounded aggregate metrics with retention and access metadata.

## Three Ways to Exercise This Research

1. **Synthetic side-channel fixture** - Objective: verify evaluation plumbing without real-user data; inputs: generated packet-size/direction/timing sequences and synthetic behavior labels; method: train a toy classifier and compare transformations; output: fixed-denominator leakage/utility report; success: deterministic metrics and no sensitive fields; stop: halt if fixtures contain captured traffic.
2. **Authorized countermeasure replay** - Objective: measure privacy protection; inputs: consented local application sessions and declared defenses; method: nested train/test across networks and time; output: F1/FPR/FNR, abstention, bandwidth, and latency; success: leakage falls under a predeclared utility budget; stop: halt on missing authorization or raw-data export.
3. **Governance audit** - Objective: test data minimization; inputs: collection schema, retention policy, consent record, and aggregate results; method: inspect purpose, fields, access, deletion, and public-output gates; output: pass/fail evidence card; success: necessary-only telemetry and verifiable deletion; stop: halt on identity linkage or unrestricted retention.

## Example MVP Product

### Encrypted-Traffic Privacy Card

- **User**: application/network privacy engineers and independent auditors.
- **Problem**: encryption claims rarely quantify metadata-level behavior leakage.
- **Input**: locally generated authorized fixtures plus countermeasure configuration.
- **Flow**: validate authorization and schema; run a bounded local classifier adapter; compute nested holdout leakage; compare defenses; delete raw fixtures according to policy; render aggregates.
- **Output**: Markdown/JSON card with threat model, domains, F1/FPR/FNR, abstention, bandwidth/latency overhead, retention proof, and limitations.
- **Architecture**: local-only adapters, schema gate, split validator, metric engine, countermeasure runner, deletion ledger, and public-safe renderer.
- **Safety boundary**: no real-user monitoring, identity linkage, payload/URI export, or interception guidance.
- **Success**: reproducible aggregates, independent splits, explicit denominators, and clean no-source/no-traffic gate.
- **Non-goals**: behavioral surveillance, censorship, employee monitoring, advertising profiling, or deanonymization.

```python
SENSITIVE = {"payload", "uri", "uri_parameters", "account_id", "user_id", "ip_address"}

def validate_public_record(record: dict) -> None:
    leaked = SENSITIVE.intersection(record)
    if leaked:
        raise ValueError(f"sensitive fields forbidden: {sorted(leaked)}")
    required = {"attempts", "f1", "false_positive_rate", "false_negative_rate"}
    missing = required.difference(record)
    if missing:
        raise ValueError(f"missing aggregate fields: {sorted(missing)}")
```

## Related Research and Reading

| Entry | Relationship | Source Basis | Boundary |
|---|---|---|---|
| Telecom AI Roadmap | Network AI needs privacy, security, task-specific evaluation, staged gates, and local/edge handling of sensitive telemetry. | `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` | Broad roadmap; does not validate X-PRINT. |
| Agent Memory Forensics | Both identify channel-specific operational signatures and require true-benign calibration plus minimized sensitive telemetry. | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` | Agent-memory events differ from packets/URIs. |
| Control Surfaces | Purpose-bound privacy and instrumenting the mechanism of disclosure apply directly to traffic collection and retained logs. | `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md` | Tool-agent benchmark does not measure network fingerprinting. |

## Source References

1. Zhu, YuKun; Hua, ManYuan; Huang, Hai; Zhang, YongZhao; Yang, Jie; Xu, FengHua; Chen, RuiDong; Zhang, XiaoSong; Yu, JiGuo; Ma, Yong. “X-PRINT: Platform-Agnostic and Scalable Fine-Grained Encrypted Traffic Fingerprinting.” arXiv:2509.00706v1, 2025. https://arxiv.org/abs/2509.00706v1
2. Full-paper HTML: https://arxiv.org/html/2509.00706v1
3. PDF: https://arxiv.org/pdf/2509.00706
4. DOI: https://doi.org/10.48550/arXiv.2509.00706
5. Related DEP: `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md`
6. Related DEP: `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md`
7. Related DEP: `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md`

## Appendix

### Workflow Provenance

- Candidate set: 75,777 PDFs / 75,776 unique parent units.
- Uniform draw: index 44,195; first draw; zero exclusions/reselections.
- Dedup: no substantive match by ID, DOI, title, slug, artifacts, memory, companion, or recent marker.
- Initial source: `partial`; valid PDF, missing full-paper HTML.
- Repair: official full-paper and metadata HTML fetched once; final source verified `complete`; zero partials.
- Cache: miss to `cached`, `missing-only`, 0.849 seconds, `pypdf`/`html-regex`.
- Redistribution: no PDF, HTML, metadata, packet/URI trace, source archive, model, cache, or extracted text deposited.

### Selected Result Matrix

| Setting | Comparator | X-PRINT | Interpretation |
|---|---:|---:|---|
| Cross-platform behavior F1 | FOAP 0.515 | 0.965 | Closed studied applications/platforms with interleaving |
| URI-map average FNR | URI set 0.172 | 0.037 | Three selected categories |
| URI-map average FPR | URI set 0.072 | 0.012 | Three selected categories |
| Unseen SmartTV/iOS17 F1 | FOAP 0.501/0.517 | 0.747/0.744 | Twenty aligned applications |
| Unseen applications F1 | FOAP 0.444 | 0.736 | Related functional categories |
| Unseen versions F1 | FOAP 0.300 | 0.717 | Eleven-month gap |

Values are author-reported means from the inspected paper and were not reproduced.
