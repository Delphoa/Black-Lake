---
title: "Fast ML Science - DEP-E"
generated_at: "2026-08-19 (date-only; exact time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of fast machine learning for scientific applications, instrumentation, and deployment."
source_status: "Mixed: complete local source pair inspected and withheld; public URLs cited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-19"
temporal_cutoff: "Sources inspected through 2026-08-19"
primary_url: "https://arxiv.org/abs/2110.13041"
stable_identifier: "arXiv:2110.13041v1; DOI:10.48550/arXiv.2110.13041; journal DOI:10.3389/fdata.2022.787421"
confidence_summary: "High for the paper's taxonomy and reported scope; medium for transferable implementation implications; low for any unreplicated deployment claim."
safety_scope: "Public-safe research review, synthetic evaluation planning, and authorized shadow-mode design"
distribution_notes: "Only derived Markdown and public URLs are deposited; original paper sources remain local and are withheld."
---

# Fast ML Science - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Applications and Techniques for Fast Machine Learning in Science | Primary paper | PDF and full-paper HTML | arXiv:2110.13041v1 | https://arxiv.org/abs/2110.13041 | Public source locator; local copies withheld | 2026-08-19 | Complete PDF and full-paper HTML verified locally |
| S2 | arXiv metadata record | Primary metadata | HTML | Submitted 2021-10-25; v1 | https://arxiv.org/abs/2110.13041 | Metadata page is not treated as the paper document | 2026-08-19 | Inspected |
| S3 | Frontiers publication | Near-primary publication record | Journal HTML | *Frontiers in Big Data* 5:787421, 2022 | https://doi.org/10.3389/fdata.2022.787421 | Publisher terms apply; public record cited | 2026-08-19 | Inspected |
| S4 | fastml-science | Official community implementation context | GitHub repository | Current public repository | https://github.com/fastmachinelearning/fastml-science | Repository license and contents govern reuse | 2026-08-19 | README inspected |
| S5 | hls4ml and FastML Foundation | Official community implementation context | GitHub and web | Current public project context | https://github.com/fastmachinelearning/hls4ml | Repository license and project terms govern reuse | 2026-08-19 | README and foundation page inspected |
| S6 | SpOctA Accelerator DEP | Related Black Lake artifact | Markdown | DEP-E-20260718 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-SpOctA%20Accelerator/spocta_accelerator_manuscript.md | Derived public-safe context only | 2026-08-19 | Inspected |
| S7 | ELiTeFormer FPGA DEP | Related Black Lake artifact | Markdown | DEP-A-20260809 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20002/DEP-A-20260809-ELiTeFormer%20FPGA/2607.03652-whitepaper-review.md | Derived public-safe context only | 2026-08-19 | Inspected |
| S8 | Local AI Stack DEP | Related Black Lake artifact | Markdown | DEP-E-20260709 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md | Derived public-safe context only | 2026-08-19 | Inspected |
| S9 | Black Lake repository rules | Repository authority | README and DEP rules | Main branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public filing and source-locality rules | 2026-08-19 | Inspected before writing |
| S10 | Black-Lake-Data repository rules | Related repository authority | README | Main branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public source-deposition rules | 2026-08-19 | Inspected before writing |

Local source inventory: one complete PDF, one complete full-paper HTML document, and one metadata HTML document were inspected in the private archive unit. Their absolute paths and contents are intentionally not disclosed here. No source file, extracted text, cache, or source package is deposited.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary paper | Introduction, domain applications, data representations, system constraints, Tables 2-3, technology state-of-the-art, outlook, figures, and references | Problem, method of review, taxonomy, implementation implications, and limitations | High | Author/community review; no independent reproduction |
| E2 | S2 | Primary metadata | Title, author list, date, version, subjects, report number, page/figure/table counts, journal reference, and DOI links | Identity and publication metadata | High | Metadata alone does not support detailed method or results claims |
| E3 | S3 | Published article | Abstract, article outline, publication date, journal volume/article number, and publisher context | Published status and cross-format scope check | High | It remains the same review, not independent validation |
| E4 | S4-S5 | Official community repositories | Float/quantized benchmark README, hls4ml low-latency FPGA scope, community resource context | Current implementation and benchmark context | Medium | Companion ecosystem evidence, not evidence that the review's claims were reproduced |
| E5 | S6-S8 | Related Black Lake artifacts | Sparse accelerator, FPGA low-precision, and edge/runtime deployment analyses | Concrete conceptual bridge and implementation cautions | Medium | Derived related records; not primary evidence for the selected paper |
| E6 | S9-S10 | Repository authority | Filing, attribution, source-locality, and no-source-upload rules | Artifact compliance | High | Process evidence only |

## Executive Summary

The paper is a broad community review of fast machine learning for science. It argues that scientific ML becomes materially useful when it is integrated into the experimental data path, where data rates, latency, bandwidth, memory, energy, and deployment hardware are part of the design problem. Its scope spans particle physics, nuclear and plasma physics, astronomy, material science, biomedical engineering, communications, and related scientific workflows. [E1][E2][E3]

The review organizes the subject into domain applications, recurring data representations and system constraints, and techniques for efficient training and deployment. It distinguishes real-time data reduction, real-time analysis, and closed-loop control, then connects those task modes to software-programmable processors, GPUs/TPUs, FPGAs, ASICs, and emerging hardware. It presents quantization, pruning/sparse inference, efficient architectures, knowledge distillation, and model/hardware co-design as recurring tools. [E1]

Reviewer assessment: the paper's strongest durable contribution is a design vocabulary and a cross-domain systems framing, not a unified benchmark result. Confidence is high for the taxonomy and reported review scope, medium for transfer to a new instrument, and low for any claim that a particular deployment is reproducible or safe without matched end-to-end measurements.

## Detailed Summary

### Problem Context

Scientific instruments increasingly observe finer spatial and temporal scales, producing data volumes that challenge storage, communication, and offline analysis. Fast ML is framed as a way to move useful inference closer to sensors or into high-throughput pipelines, reducing data before storage, extracting features in real time, or supporting feedback. The relevant problem is therefore not simply model accuracy; it is whether the entire system can meet the instrument's operating envelope. [E1]

### Review Method and Scope

The authors describe a community report built from two Fast ML for Science workshops. It is intentionally broad: domain experts contribute examples, while ML and computer-architecture discussions supply shared implementation vocabulary. The article is a taxonomy and pointer-rich review, not a new data collection study or one controlled benchmark across all domains. [E1][E2]

### Domain Applications

The review surveys fast-ML examples in LHC event reconstruction and triggering, nuclear and neutrino physics, dark-matter experiments, astronomy and cosmology, material synthesis and microscopy, biomedical sensing, gravitational waves, communications, accelerator control, and plasma physics. The examples differ in data form and operating envelope, but share pressure to reduce latency or data movement while retaining scientifically relevant information. [E1]

### Data Representations

The paper groups recurring representations into raw versus reconstructed data, temporal data, frame-based images, point clouds, multispectral or hyperspectral data, and spatio-temporal forms. This is more than a descriptive taxonomy: the representation influences the model family, memory layout, sparsity opportunity, communication cost, and hardware architecture. For example, point clouds may require irregular neighborhood operations, while temporal signals make data movement and state update cadence central concerns. [E1]

### System Constraints and Task Modes

Table 2 pairs domains with indicative event rates, latency scales, software-versus-custom systems, and energy constraints. Table 3 distinguishes real-time data reduction, real-time analysis, and closed-loop control. The distinction changes the validation contract: a reduction system must quantify retained signal and false drops, an analysis system must characterize decision latency and quality, and a control system must additionally prove bounded response, fallback, and intervention behavior. [E1]

### Efficient Model and Deployment Techniques

The technology section groups efficient deployment methods into efficient neural-network architectures, model/hardware co-design, quantization, pruning and sparse inference, and knowledge distillation. It also surveys software-programmable processors, conventional CMOS architectures, FPGA hardware/software co-design, and beyond-CMOS approaches. The article repeatedly emphasizes that model design and hardware choice should be considered together because memory footprint, data movement, precision, parallelism, and programmability determine end-to-end performance. [E1]

### Evidence and Reproducibility

The review's evidence consists primarily of selected domain examples and pointers to prior work. It reports no single shared dataset, protocol, or independent reproduction that would make all cross-domain numbers directly comparable. The official FastML ecosystem provides companion benchmarks and software such as fastml-science and hls4ml, but those repositories are implementation context rather than proof of the selected review's aggregate claims. [E4]

### Conclusion and Boundaries

The outlook argues that fast ML is promising but rapidly changing, and that the central future need is continued co-design across applications, models, hardware platforms, and tool flows. The authors also acknowledge that the broad report cannot be comprehensive and that the state-of-the-art discussion can become outdated. A downstream reviewer should therefore treat the article as a map and vocabulary, then pin current versions, benchmarks, hardware, and failure evidence before making a deployment decision. [E1][E3]

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Fast ML for science means integrating ML into experimental data-processing infrastructure to reduce time to science. | Author definition | E1, E2, E3 | Directly stated and consistent across primary and published records. | High |
| C2 | Scientific domains share recurring constraints involving data representation, event rate, latency, bandwidth, memory, energy, and hardware choice. | Author synthesis | E1 | Supported by the taxonomy and Tables 2-3; the exact envelope remains domain-specific. | High |
| C3 | Real-time reduction, analysis, and closed-loop control require distinct system and validation choices. | Author taxonomy and reviewer interpretation | E1 | Table 3 supports the distinction; the stronger governance implications are reviewer interpretation. | High for distinction; medium for governance extension |
| C4 | Efficient architectures, co-design, quantization, pruning/sparse inference, and distillation are reusable technique families. | Author survey claim | E1 | Directly supported by the technology section; relative benefit depends on workload and device. | High |
| C5 | A fast-ML claim should be evaluated end-to-end rather than by model latency alone. | Reviewer interpretation | E1, E5 | Strongly implied by data movement, memory, and system-constraint discussion; not a single measured result in the paper. | Medium-high |
| C6 | The paper is a useful design map but not a unified benchmark or independent deployment validation. | Reviewer assessment | E1-E4 | Supported by the paper's review format, breadth, and stated non-comprehensive scope. | High |

## Methodology

- `Research objective`: Preserve a source-grounded, public-safe DEP research artifact about the paper's fast-ML taxonomy and implementation relevance.
- `Sources inspected`: Complete local PDF and full-paper HTML, metadata HTML, arXiv record, Frontiers/PMC publication record, official FastML repositories, live Black Lake and Black-Lake-Data READMEs, and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, grouped by PDF parent, derived identifiers from filenames/folders/nearby metadata, reconciled ownership identifiers and artifact records, selected uniformly with PowerShell `Get-Random`, repaired the selected incomplete source unit through the bounded arXiv archive process, then searched public arXiv, DOI, publisher, official-repository, and related-DEP surfaces.
- `Inclusion criteria`: Full-paper sections, tables, figures, metadata, publication records, official implementation context, and related DEPs were included when they supported identity, mechanism, evidence, limitations, implementation relevance, or provenance.
- `Exclusion criteria`: Abstract-only pages were excluded from method/result claims. No source file, extracted source text, cache, dataset, model, or executable artifact was uploaded. Unverified code, unreviewed citations, and keyword-only related entries were excluded from synthesis.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, and safety/ethics.
- `Evidence handling`: Evidence IDs distinguish primary source reporting, metadata, official implementation context, related DEP context, and reviewer interpretation. Author claims remain labeled as author claims.
- `Uncertainty handling`: Missing paper-specific code, cross-domain normalization, rapidly changing technology, simulated or source-reported results, and closed-loop safety gaps are stated rather than smoothed over.
- `Random selection`: Uniform sorted eligible-parent pool; PowerShell `Get-Random`; 75,967 PDFs, 75,964 parent units, 185 incomplete-ID units withheld, 891 prior-ownership exclusions, 74,888 eligible units, selected zero-based index 11,772, zero reselections.
- `Dedup/reselection validation`: Exact arXiv ID, DOI, normalized title, slug, local `.logs`, `.reports`, `.lake-data`, automation memory, related-repository tree identifiers, and preceding-24-hour markers were scanned. No selected-paper match was found.
- `Source-integrity process`: The initial unit was partial because full-paper HTML was missing. One bounded official arXiv repair preserved the valid PDF and produced a verified full-paper HTML pair. The private README, provenance record, machine summary, and verification report were updated. The source package was unavailable and was not required after the complete-source gate passed.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's definitions, domain/application taxonomy, data representations, system constraints, efficient deployment methods, hardware/software co-design framing, evidence boundary, and bounded implementation implications.
- `Temporal boundary`: Public and repository sources inspected through 2026-08-19; the primary preprint is v1 from 2021-10-25 and the journal record is from 2022-04-12.
- `Evidence limits`: The paper is a broad review, not a unified benchmark. Cross-domain results are not directly comparable without source-level reconstruction. No paper-specific code or dataset was independently executed.
- `Assumptions`: The public arXiv and Frontiers records identify the same work; related Black Lake artifacts are used only for conceptual synthesis, not as validation of the primary paper.
- `Constraints`: Original source files remain private; public output contains only derived Markdown and public URLs. MVP examples are synthetic, local, shadow-mode, or authorized-use oriented and do not actuate instruments.
- `Out of scope`: Certification, clinical or safety approval, live instrument control, deployment of hardware, downloading datasets or model weights, and independent reproduction of every cited study.
- `Intended use`: Research review, DEP deposition, implementation planning, benchmark design, and follow-on source collection.
- `Audience`: Scientific ML researchers, instrument and accelerator engineers, benchmark designers, and reviewers assessing deployment readiness.
- `Reproducibility boundary`: The review's source claims are inspectable from the cited public paper records; the current artifact does not reproduce the underlying cited experiments or establish hardware performance.
- `Data sensitivity`: Public research sources; local source files are withheld for provenance and distribution safety.

## Observations

- `Observed pattern`: The paper treats representation choice as the first systems decision because it affects model structure, memory, sparsity, communication, and hardware.
- `Technical implication`: A benchmark should report data movement, preprocessing, postprocessing, fallback, and device conditions beside inference latency.
- `Contradiction or tension`: The review advocates cross-domain commonality while also showing that event rates, latency, energy, and control consequences differ enough to block naive score aggregation.
- `Reviewer hypothesis`: A typed requirements ledger could make the paper's taxonomy operational by forcing each deployment claim to name its data form, task mode, resource denominator, and failure boundary.
- `Open question`: How much of an efficiency gain survives when a model is moved across compiler, runtime, accelerator, sensor, and calibration versions?

## Considerations

Fast ML deployments can reduce storage and decision latency, but they can also move errors earlier in the scientific process. A data-reduction model may discard rare events; a real-time analysis model may create false triggers; a control model may alter the experiment. The system should therefore keep a conservative or offline path during validation, log model/data/device versions, and report tail failures rather than only averages.

The paper's hardware discussion also implies an operational cost: custom systems can meet constraints that software-programmable devices cannot, but they raise development, verification, maintenance, and portability burdens. Low precision or sparsity can create real gains only when the compiler, memory hierarchy, and target device exploit them. The related SpOctA, ELiTeFormer, and Local AI Stack records reinforce this boundary. [E5]

## Strengths

- It unifies scientific applications, data representations, model efficiency, and hardware/software deployment in one navigable framework.
- It makes system constraints explicit through event-rate, latency, systems, energy, and task-mode tables.
- It gives non-specialists a useful entry point while pointing to primary technical literature and community resources.
- It recognizes its own breadth and time-sensitivity rather than presenting the review as exhaustive or final.

## Weaknesses

- The review is not a common benchmark; its domain examples use different datasets, metrics, hardware, and denominators.
- Many technique summaries are necessarily high-level, so a reader still needs current primary papers, code, tool versions, and device measurements.
- The public artifact ecosystem surrounding the review is broader than one paper-specific codebase, which limits direct reproduction of the review's narrative.
- Closed-loop control is identified as a task mode, but the review does not supply one uniform safety or fallback protocol across domains.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a versioned cross-domain benchmark schema | Evidence comparability | Shared fields for input rate, data form, latency boundary, quality, power, and data movement would reduce denominator ambiguity | Better comparison and auditability | Community coordination and schema adoption | Re-run representative tasks with matched reporting fields |
| Add end-to-end cost-quality frontiers | Systems evidence | Model latency alone misses sensor, transfer, preprocessing, and fallback cost | More realistic deployment decisions | Higher measurement burden | Report percentile latency, energy, memory, quality, and failure slices |
| Add control-mode safety templates | Closed-loop use | Reduction, analysis, and control require different stop and fallback rules | Safer transfer to instruments | Domain-specific review effort | Shadow-mode trials with conservative comparison and failure injection |
| Maintain living tool and hardware pins | Review currency | The article's state-of-the-art section can age quickly | Easier follow-up review and reproduction | Maintenance overhead | Scheduled source refresh with immutable version history |

## Potential Implementations

1. **Fast-ML requirements ledger**: A researcher records data representation, event rate, latency target, energy limit, task mode, hardware candidates, quality metric, fallback, and source version. The output is a reviewable deployment envelope; risk control is mandatory human/domain review before control-mode use.
2. **Public cost-quality benchmark**: A local runner compares float, quantized, pruned, and distilled variants on public or synthetic data and reports task quality, percentile latency, throughput, memory, energy, preprocessing, transfer, and fallback separately. The runner must refuse to compare results with missing denominators.
3. **Shadow-mode scientific gateway**: A stream adapter mirrors an existing analysis path, produces a reduction or analysis suggestion, and keeps the conservative path authoritative. Control actions are out of scope for the MVP; any later authorization requires domain safety review and bounded fallback tests.

## Three Ways to Exercise This Research

1. **Taxonomy exercise**: Classify a public scientific dataset as raw/reconstructed, temporal, image, point cloud, multispectral, or spatio-temporal; choose reduction, analysis, or control mode; and write the expected rate, latency, memory, and energy boundaries. Success means a second reviewer can reproduce the classification and identify missing fields. Stop if the task mode or quality target is ambiguous.
2. **Synthetic precision sweep**: Train or load a small public model, then compare float and quantized variants on synthetic or authorized data under a fixed metric and fixed input pipeline. Record quality, percentile latency, memory, and energy proxy separately. Success means the complete ledger contains both gains and regressions. Stop before using restricted data or claiming hardware equivalence.
3. **Shadow-mode replay**: Replay a public or synthetic stream through a baseline and a fast-ML candidate without actuating an instrument. Compare retained events, false drops, decision latency, tail failures, and fallback behavior. Success means the candidate has a bounded abstention path and the baseline remains available. Stop if any step would change a live experiment.

## Example MVP Product

- `Product name`: FastML Design Ledger
- `Target user`: Scientific ML researcher, instrument engineer, or accelerator reviewer.
- `Problem`: Fast-ML proposals often report model speed without a common record of representation, data movement, device, energy, quality, and task mode.
- `Core workflow`: Import a public paper or synthetic benchmark description; fill the typed requirements record; attach model, runtime, and hardware versions; compare candidate variants; generate a cost-quality report; route control-mode proposals to human review.
- `Data requirements`: Public or synthetic traces, model metadata, data representation, event-rate estimates, latency/power/memory measurements, quality labels, fallback outcomes, and source URLs. Restricted scientific data stays local.
- `Architecture`: Local-first Markdown/JSON ledger, deterministic validation rules, optional benchmark adapters, and a report generator. No remote upload is required for the MVP.
- `Success metrics`: 100% of completed records name the end-to-end boundary, at least three resource dimensions, task mode, quality metric, source versions, and fallback; reviewers can reproduce the comparison from the ledger.
- `Risk controls`: No live actuation, no credential storage, no raw sensitive-data logging, explicit source-locality, schema validation, baseline comparison, uncertainty labels, and mandatory human review for control mode.
- `Limitations`: It cannot establish hardware performance without measurements, cannot replace domain safety review, and cannot make incomparable benchmarks comparable merely by formatting them.
- `MVP boundary`: Public/synthetic replay and review only; no hardware synthesis, live instrument connection, clinical action, or closed-loop control.
- `Deployment model`: Local CLI or notebook with Markdown/JSON output.
- `Evaluation plan`: Schema tests, golden synthetic traces, matched baseline comparisons, failure injection, and reviewer agreement checks.
- `Failure modes`: Missing denominators, optimistic averages, stale device/runtime pins, hidden preprocessing cost, confidence drift, false drops, and fallback misconfiguration.
- `Maintenance plan`: Versioned schema, source refresh dates, device/runtime records, and append-only correction notes.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| FastML Science Benchmarks | Official community benchmark repository | Float and quantized reference models for fast scientific ML evaluation | https://github.com/fastmachinelearning/fastml-science |
| hls4ml | Official community software | Low-latency ML inference on FPGAs and hardware/software co-design | https://github.com/fastmachinelearning/hls4ml |
| FastML Foundation | Official community | Current community projects, applications, and resources | https://fastmachinelearning.org/ |
| SpOctA Accelerator | Related Black Lake DEP | Sparse representation, map search, memory skew, and accelerator co-design | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-SpOctA%20Accelerator/spocta_accelerator_manuscript.md |
| ELiTeFormer FPGA | Related Black Lake DEP | Low-precision FPGA deployment and resource accounting | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20002/DEP-A-20260809-ELiTeFormer%20FPGA/2607.03652-whitepaper-review.md |
| Local AI Stack | Related Black Lake DEP | Runtime, accelerator, quantization, edge-power, and governance boundary | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md |
| Journal publication | Near-primary publication | Published version and article context | https://doi.org/10.3389/fdata.2022.787421 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2110.13041 | Identity, abstract, authors, date, version, subjects, and public source links | 2026-08-19 | Primary metadata; abstract not used alone for detailed claims |
| R2 | https://arxiv.org/html/2110.13041 | Full-paper sections, figures, tables, technology survey, and outlook | 2026-08-19 | Complete full-paper rendering inspected locally and withheld |
| R3 | https://arxiv.org/pdf/2110.13041 | PDF text and visual cross-check of Tables 2-3 and selected pages | 2026-08-19 | Complete PDF inspected locally and withheld |
| R4 | https://doi.org/10.3389/fdata.2022.787421 | Journal identity and publication context | 2026-08-19 | Frontiers record |
| R5 | https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2022.787421/full | Publisher abstract, outline, and article framing | 2026-08-19 | Near-primary publication record |
| R6 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9041419/ | Open full-text publication cross-check | 2026-08-19 | Same published work; not independent validation |
| R7 | https://github.com/fastmachinelearning/fastml-science | Official float/quantized benchmark context | 2026-08-19 | Companion implementation context |
| R8 | https://github.com/fastmachinelearning/hls4ml | Official low-latency FPGA inference context | 2026-08-19 | Community software context |
| R9 | https://fastmachinelearning.org/ | Current FastML Foundation context | 2026-08-19 | Community resource context |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-SpOctA%20Accelerator/spocta_accelerator_manuscript.md | Related DEP 1 | 2026-08-19 | Derived artifact; not primary validation |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20002/DEP-A-20260809-ELiTeFormer%20FPGA/2607.03652-whitepaper-review.md | Related DEP 2 | 2026-08-19 | Derived artifact; not primary validation |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md | Related DEP 3 | 2026-08-19 | Derived artifact; not primary validation |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository layout, source locality, and attribution | 2026-08-19 | Repository authority |
| R14 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index requirements | 2026-08-19 | Repository authority |
| R15 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related raw repository source-deposition rules | 2026-08-19 | Repository authority |

## Appendix

### Source Integrity and Selection Record

- Candidate method: `rg --files -g "*.pdf"` against the local arXiv archive; each PDF parent was treated as one paper unit.
- Candidate counts: 75,967 PDFs; 75,964 parent units; 185 incomplete-ID units withheld; 891 prior-ownership exclusions; 74,888 eligible units.
- Random draw: sorted eligible pool and uniform PowerShell `Get-Random`, zero-based index 11,772; selected arXiv:2110.13041; zero reselections.
- Dedup validation: exact ID, DOI, normalized title, normalized slug, local artifact collections, automation memory, related-repository identifiers, and preceding-24-hour markers were checked with no selected-paper match.
- Initial source state: partial because full-paper HTML was absent.
- Repair outcome: one bounded brokered official arXiv repair; valid PDF preserved; complete full-paper HTML acquired; private README, provenance, machine summary, and verification report updated.
- Final source state: complete PDF plus complete full-paper HTML; metadata HTML present; no partial files; source package unavailable; no source files uploaded.

### Public Safety Boundary

This manuscript contains no local absolute paths, usernames, machine names, local timezone labels, exact local execution timestamps, credentials, private data, source archives, PDFs, HTML files, extracted source text, caches, or `.source/` directory. The original paper is attributed through public URLs only.

## Attribution Block

- Source boundary: complete local source documents, provenance records, and verification records were inspected and retained locally; no source files were staged, committed, uploaded, or attached to Slack.
