---
title: "SpOctA Accelerator - DEP-E"
generated_at: "2026-07-18 (date-only; exact time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of SpOctA, an accelerator for octree-indexed and sparsity-aware 3D sparse convolution."
source_status: "Complete local source bundle inspected; all source files withheld from public deposition"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-18"
temporal_cutoff: "Sources inspected through 2026-07-18"
primary_url: "https://arxiv.org/abs/2308.09249"
stable_identifier: "arXiv:2308.09249v1; DOI:10.1109/ICCAD57390.2023.10323728"
confidence_summary: "High for source reporting; medium for cross-platform generalization; low for independent reproducibility without released RTL and simulator assets."
safety_scope: "Research review and synthetic evaluation planning; no vehicle-control or safety-certification claims"
distribution_notes: "Public-safe derived Markdown only; PDF, HTML, TeX/source, extracted text, and caches remain local."
---

# SpOctA Accelerator - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | SpOctA arXiv record | Primary metadata | HTML | arXiv:2308.09249v1 | https://arxiv.org/abs/2308.09249 | arXiv license locator visible; evidence use only | 2026-07-18 | Inspected |
| S2 | SpOctA paper | Primary artifact | PDF | arXiv:2308.09249v1 | https://arxiv.org/pdf/2308.09249 | Complete local PDF inspected; file withheld | 2026-07-18 | Verified complete |
| S3 | SpOctA full-paper HTML | Primary artifact fallback | HTML | ar5iv rendering of 2308.09249 | https://ar5iv.labs.arxiv.org/html/2308.09249 | Used after official arXiv HTML was unavailable; file withheld | 2026-07-18 | Verified complete |
| S4 | SpOctA TeX source | Primary artifact | Source package | arXiv:2308.09249v1 | https://arxiv.org/e-print/2308.09249 | 21-entry source package inspected; file withheld | 2026-07-18 | Verified archive |
| S5 | IEEE publication | Near-primary publication record | DOI / publisher locator | DOI:10.1109/ICCAD57390.2023.10323728 | https://doi.org/10.1109/ICCAD57390.2023.10323728 | Publisher terms apply | 2026-07-18 | DOI and locator established; IEEE page body unavailable to browser |
| S6 | Dongxu Lyu publication page | Author context | Web page | ICCAD 2023 entry | https://lvdongxu.github.io/ | Author-maintained metadata | 2026-07-18 | Inspected |
| S7 | Efficient FM Survey - DEP-E | Related DEP | Markdown | DEP-E-20260718-Efficient FM Survey | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey/efficient_fm_survey_manuscript.md | Derived Black Lake artifact | 2026-07-18 | Inspected |
| S8 | Physical Data - DEP-E | Related DEP | Markdown | DEP-E-20260710-Physical Data AI | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md | Derived Black Lake artifact | 2026-07-18 | Inspected |
| S9 | HERMES World Model - DEP-E | Related DEP | Markdown | DEP-E-20260712-HERMES World Model | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md | Derived Black Lake artifact | 2026-07-18 | Inspected |
| S10 | Black Lake repository rules | Repository authority | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository policy | 2026-07-18 | Inspected |
| S11 | Black Lake DEP rules | Repository authority | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public repository policy | 2026-07-18 | Inspected |
| S12 | Black-Lake-Data rules | Related repository authority | Markdown | Live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository policy | 2026-07-18 | Inspected before using related-repository dedup context |

Primary work metadata:

- `Full title`: SpOctA: A 3D Sparse Convolution Accelerator with Octree-Encoding-Based Map Search and Inherent Sparsity-Aware Processing.
- `Authors`: Dongxu Lyu; Zhenyu Li; Yuzhou Chen; Jinming Zhang; Ningyi Xu; Guanghui He.
- `Version`: arXiv v1, submitted 2023-08-18.
- `Venue`: ICCAD 2023, pages 1-9.
- `Published DOI`: 10.1109/ICCAD57390.2023.10323728.
- `arXiv DOI`: 10.48550/arXiv.2308.09249.
- `Subject`: Computer Science - Hardware Architecture.
- `Code availability`: No official SpOctA repository was established through the arXiv record, author page, or exact-title GitHub search.
- `Local source policy`: The complete PDF, full-paper HTML, metadata HTML, TeX/source, extracted text, cache manifests, and integrity reports were inspected locally and withheld from publication.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, date, subject, acceptance note, abstract, version history | Identity and headline claims | High | Abstract alone does not support method or result details |
| E2 | S2, S4 | Primary paper and source | Introduction; sparse-convolution background; equations; OCTENT/SPAC design; evaluation; figures; conclusion | Problem, mechanism, setup, results, limitations | High for reporting | Author-reported; no independent execution |
| E3 | S3 | Primary full text | Full-paper section structure and narrative cross-check | Completeness and text extraction | High | ar5iv conversion may differ typographically from the source PDF |
| E4 | S2 | Primary visual evidence | Rendered pages 7-8: benchmark table, Figure 9, Figure 10, comparison values | Datasets, optimization effects, area/power/throughput/frame-rate values | High for transcription | Figures remain author-generated evidence |
| E5 | S5, S6 | Publication records | ICCAD listing, pages, published DOI, author context | Venue and publication metadata | Medium-high | IEEE page body was unavailable; DOI locator and author record agree |
| E6 | S7 | Related DEP synthesis | Resource definitions, sparse execution, operational-envelope cautions | Cross-DEP efficiency interpretation | Medium | Not empirical validation of SpOctA |
| E7 | S8 | Related DEP synthesis | Representation substrate, model/hardware boundary, evidence discipline | Cross-DEP representation and hardware interpretation | Medium | Different method and workload |
| E8 | S9 | Related DEP synthesis | BEV compression, point-cloud generation, autonomous-driving evaluation limits | Workload transfer and safety boundary | Medium | HERMES is a world model, not an accelerator benchmark |
| E9 | S10-S12 plus public dedup pointer and automation memory | Process evidence | Filing rules, source locality, random selection, dedup, cutoff, artifact scope | Methodological and repository compliance | High | Private paths and precise execution details intentionally withheld |

## Executive Summary

SpOctA is a specialized architecture for 3D sparse convolution, a core operation in voxelized point-cloud networks. The paper argues that sparse convolution is difficult on general hardware because the nonempty coordinates must first be mapped into valid input-output neighborhoods, activation sparsity is not automatically converted into fewer cycles, and 3D kernels create large weight traffic. SpOctA addresses these bottlenecks with OCTENT, an octree-encoding and table-aided map-search core, and SPAC, a sparsity-aware compute and memory core.

The source reports that OCTENT reduces map-search latency enough to produce an 8.8-21.2x search speedup. SPAC and fine-grained overlap save 44.4-79.1% processing latency. A non-uniform weight cache exploits the higher use frequency of center and middle vertical kernel planes and saves 57.6% external-memory access energy on average. A 40 nm synthesis and cycle-simulation study across MinkUNet/SECOND and four datasets reports 200 GOPS at 400 MHz, 83.7 mW, 1.06 square millimeters, and 2.39 TOPS/W, plus 1.1-6.9x speedup and 1.5-3.1x energy-efficiency gains over cited accelerator baselines.

Reviewer assessment: the paper provides a coherent algorithm-architecture co-design and useful breakdowns, but its evidence is simulated/synthesized rather than measured silicon. The absence of released RTL, simulator inputs, switching traces, synthesis constraints, accuracy-recovery results, and normalization scripts limits independent reproduction. The strongest transferable insight is a co-design pattern: turn irregular spatial representation into bank-safe parallel lookup, overlap lookup and compute, and allocate memory according to measured access skew.

## Detailed Summary

### Problem Context

Point clouds are spatially sparse and irregular. Voxelization turns them into sparse 3D tensors, usually storing only nonempty voxels and coordinates. Sparse convolution avoids dense work, but it needs an IN-OUT map that says which input voxels contribute to each output voxel and kernel position. A naive map search can resemble quadratic traversal over voxels; hash-based GPU methods add serialization and memory cost; prior accelerators trade parallelism, logic, or operator coverage.

The paper also observes 40-60% activation sparsity in representative sparse-convolution networks after nonlinear activation. A conventional dense processing array will not necessarily skip those zeros. Finally, extending kernels from two to three dimensions expands weights and stresses SRAM/DRAM. The source cites a typical 8-bit MinkowskiUNet layer with more than 400 KB of weights as motivation.

### Operator Scope

The architecture targets several sparse-convolution forms: submanifold 3D convolution (`Subm3`), two-step generative/downsampling convolution (`Gconv2`), transposed convolution (`Tconv2`), and wider generative convolution (`Gconv3`). The exact mapping path differs by operator. OCTENT handles `Subm3` and `Gconv2` search directly, reuses stored maps for `Tconv2`, and uses an input-stationary approach for the larger `Gconv3` search space.

### OCTENT Map Search

For voxel coordinate `(x, y, z)`, OCTENT interleaves coordinate bits into octal digits, producing an octree code. The lowest digit identifies one of eight spatial subgroups. The Neighbor Encoding Lookup Table is reformatted into a Parallel NELUT so candidate neighbors distribute across those low-digit groups. A two-dimensional table stores nonempty voxels, and queries to different low-digit subarrays can proceed concurrently.

Directly representing the entire coordinate space would make the table too large, so the design partitions space into 16 by 16 by 16 blocks. Each block fits in on-chip memory. The octree table has eight banks, one for each low octree digit; a query transmitter issues up to eight bank-safe requests per cycle. A search filter removes invalid candidates and a rectifier places valid maps into FIFO-backed map-table lanes.

### Fine-Grained Pipeline

Rather than waiting until every map is produced, the top controller begins fetching input features and weights as soon as valid maps enter the FIFO map table. Search and compute therefore overlap at block granularity. The source reports that this overlap is most useful at lower input-channel counts, where search is a larger fraction of total latency.

### SPAC Compute Core

SPAC contains a processing-element array capable of a 16 by 16 matrix times a 16 by 1 vector each cycle, plus input-feature, weight, and partial-sum memories. A gather unit uses dynamic masks to select nonzero input lanes and their weights. An output arranger tracks sparse output masks and completion. The memory and control system switches between output-stationary and input-stationary dataflows according to the operator.

### Non-Uniform Weight Caching

LiDAR and voxelized scenes often have higher horizontal than vertical resolution. The paper measures a skew in which middle vertical kernel planes account for 45-83% of map use in representative layers. The weight SRAM is divided into center, middle, upper, and lower partitions. Center weights are retained fully, middle weights receive a larger budget, and less frequent upper/lower planes receive less. This is a workload-specific cache policy, not a universal property of all sparse tensors.

### Evaluation Setup

The study uses two models and four datasets:

| Application | Dataset | Model | Paper notation |
|---|---|---|---|
| Indoor semantic segmentation | ScanNet | MinkUNet small | `Seg(i)` |
| Outdoor semantic segmentation | SemanticKITTI | MinkUNet large | `Seg(o)` |
| Object detection | KITTI | SECOND small | `Det(k)` |
| Object detection | nuScenes | SECOND large | `Det(n)` |

All networks are stated to be 8-bit and retrained to recover accuracy. SpOctA is implemented in Verilog and synthesized with Synopsys Design Compiler in 40 nm CMOS. A cycle-accurate simulator models execution. PrimeTimePX estimates logic power from benchmark switching activity, CACTI supplies SRAM area/energy, and the DRAM model assumes DDR4 at 16 GB/s and 15 pJ/bit. Baselines include NVIDIA 2080 Ti and 3090 Ti GPUs and cited point-cloud/sparse-convolution accelerators.

### Optimization Results

Figure 9 separates the three optimization families. A serial OCTENT algorithm already removes more than 65% of map-search latency; parallel hardware then removes a further 66.7-68.3% relative portion, yielding the reported 8.8-21.2x search speedup. Fine-grained pipelining reaches up to 1.68x at 16 input channels. SPAC's sparse compute becomes dominant at larger channel counts and saves up to 79.1% total processing latency in the displayed settings.

The cache plot reports 87.3% DRAM-access energy saving at 48 input channels and 82.9% at 64. Savings fall to 42.7% at 96 and 17.7% at 128 as the fixed SRAM budget covers less of the weight set. The average external-memory energy saving reported in the abstract is 57.6%.

### Cross-Platform Results

The visual comparison table reports:

| Metric | SpOctA source value |
|---|---:|
| Technology | 40 nm |
| Area | 1.06 square millimeters |
| Frequency | 400 MHz |
| On-chip SRAM | 177.4 KB |
| Peak throughput | 200 GOPS |
| Power | 83.7 mW at 1 V |
| Energy efficiency | 2.39 TOPS/W at 1 V |
| `Seg(i)` | 8.2 fps, with a 28.0 fps normalized note |
| `Seg(o)` | 214.4 fps, with a 5.4 fps normalized note |
| `Det(k)` | 44.0 fps, with a 39.1 fps normalized note |
| `Det(n)` | 31.6 fps, with a 28.1 fps normalized note |

The source states that throughput normalization is used for fair comparison. The figure reports 1.1x and 6.9x speedup for the two segmentation comparisons and 2.3x and 4.0x for the detection comparisons. These are useful author-reported comparisons but should not be treated as a common silicon benchmark without the exact normalization scripts, baseline configurations, and measurement envelopes.

### Relationship to the Three DEPs

Efficient FM Survey provides a broad systems interpretation: savings must be named by resource and denominator, and sparse operations only produce speed when the runtime/hardware can exploit them. Physical Data AI provides a representation interpretation: the chosen substrate can compress or structure the computation, but digital/model results do not automatically validate physical hardware claims. HERMES provides the 3D workload interpretation: point-cloud systems need representation compression and efficiency, yet aggregate speed must remain coupled to geometry, rare-object, and safety-relevant quality measures.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | OCTENT transforms map search into parallel, banked octree-table queries. | Author method claim | E2, E3 | Architecture and algorithm are described consistently across source formats. | High for existence |
| C2 | OCTENT yields 8.8-21.2x map-search speedup. | Author empirical claim | E2, E4 | Directly reported across four benchmarks; not independently reproduced. | Medium-high |
| C3 | Fine-grained overlap and SPAC save 44.4-79.1% processing latency. | Author empirical claim | E2, E4 | Figure 9 supports the range; workload and input-channel dependent. | Medium-high |
| C4 | Non-uniform caching saves 57.6% external-memory access energy on average. | Author empirical claim | E1, E2, E4 | Consistent with displayed 48-128-channel values; assumes the source memory model. | Medium-high |
| C5 | SpOctA reaches 200 GOPS at 400 MHz, 83.7 mW, and 1.06 square millimeters in 40 nm. | Author implementation claim | E2, E4 | Synthesized/simulated estimate, not measured silicon. | Medium-high for transcription |
| C6 | SpOctA improves speed by 1.1-6.9x and energy efficiency by 1.5-3.1x over cited accelerators. | Author comparison claim | E1, E2, E4 | Normalized cross-platform comparison; fairness cannot be independently audited. | Medium |
| C7 | The transferable mechanism is representation-to-schedule co-design plus skew-aware memory allocation. | Reviewer interpretation | E2, E6, E7 | Supported conceptually; transfer requires new workload evidence. | Medium |
| C8 | A deployment claim must pair accelerator speed with 3D task quality and safety slices. | Reviewer interpretation | E6, E8 | Strong systems requirement, not a claim made by the SpOctA paper. | Medium |

## Methodology

- `Research objective`: Preserve a source-grounded review of SpOctA, distinguish architecture and source claims from reviewer inference, connect the work to exactly three verified Black Lake DEPs, and translate the mechanism into bounded implementation paths.
- `Sources inspected`: Complete local PDF, repaired full-paper HTML, metadata HTML, TeX/source package, PDF/HTML/source extraction caches, paper-level provenance and integrity records; public arXiv metadata; author-maintained publication page; DOI/IEEE locator; live Black Lake and Black-Lake-Data README authority; and the substantive artifact for each related DEP.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, grouped by unique parent unit, derived arXiv IDs from paths/filenames, excluded used IDs, selected a uniform eligible index with PowerShell `Get-Random`, then searched arXiv, DOI, author, and exact-title code locators. Repository search identified conceptually overlapping DEPs.
- `Inclusion criteria`: Primary paper sections, figures, tables, metadata, publication records, and related DEP artifacts were included when they supported identity, mechanism, evidence, limitations, implementation relevance, or deposition rules.
- `Exclusion criteria`: Abstract-only evidence was excluded from method/result claims. Secondary summaries, unverifiable code claims, and merely keyword-similar DEPs were excluded. Local source paths and precise run timestamps were excluded from public output.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, and safety/ethics.
- `Evidence handling`: Major claims map to evidence IDs. Author claims remain labeled. Visual figure values were transcribed from rendered PDF pages and cross-checked against source text.
- `Uncertainty handling`: Missing release assets, unavailable IEEE body content, cross-process normalization uncertainty, and absent independent reproduction are explicit.
- `Extraction process`: Local PDF text used pypdf because pdftotext was unavailable; HTML used deterministic tag removal; the TeX archive used tar extraction. Full-paper review also used rendered evaluation pages.
- `Version control`: arXiv v1 and date are preserved; public repository authority came from refreshed default branches.
- `Safety handling`: Implementation examples are synthetic and advisory. No live vehicle, restricted dataset, or production-control instructions are included.
- `Reviewer stance`: DEP-ready paper report, critique, implementation translation, and replication planning.

### Random Selection and Deduplication

- PDF candidates: 75,777.
- Candidate parent units: 75,776.
- Used arXiv IDs observed: 757.
- Units excluded by used arXiv ID: 185.
- Units without a derivable arXiv ID: 185; withheld from the draw.
- Eligible units: 75,406.
- Random method: PowerShell `Get-Random` uniform zero-based index over eligible units.
- Selected index: 6,812.
- Selected base ID: `2308.09249`.
- Duplicate rejections/reselections: 0.
- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, and public dedup pointer; automation memory; Black-Lake-Data `.lake-data` and `.reports`.
- Final identity checks: arXiv ID, published DOI, normalized title, and `SpOctA` slug returned zero owning-artifact matches.
- 24-hour cutoff: public-safe date 2026-07-17; no same-paper marker found.
- Execution note: One earlier enumeration attempt ended before any random draw; the optimized, completed pass produced the single index recorded above.

## Scope, Constraints, and Assumptions

- `Scope`: The architecture, sparse-convolution mechanism, evaluation, evidence quality, implementation implications, and three related DEP bridges.
- `Temporal boundary`: Public sources and repository state inspected through 2026-07-18.
- `Evidence limits`: No RTL, simulator, synthesis constraints, switching traces, accuracy tables, or normalization scripts were released and executed during this review. IEEE page body was unavailable.
- `Assumptions`: Extracted text and visual PDF pages represent arXiv v1; author and DOI records refer to the same ICCAD paper; source-reported baseline configurations were applied as described.
- `Constraints`: Local source material is not redistributable through this workflow. Cross-platform hardware results have tool, process, memory, and workload differences. Autonomous-driving applications are safety-relevant.
- `Out of scope`: Fabrication, RTL implementation, model retraining, dataset download, cycle-simulator recreation, production deployment, vehicle control, and safety certification.
- `Intended use`: Research review, accelerator-design ideation, evaluation planning, DEP preservation, and reproducibility backlog.
- `Audience`: Hardware-architecture researchers, sparse-tensor runtime engineers, 3D perception teams, and research reviewers.
- `Depth target`: Full manuscript report with implementation and replication translation.
- `Reproducibility boundary`: Paper arithmetic and concepts can be audited; headline hardware results cannot be independently reproduced from the inspected public artifacts alone.
- `Operational boundary`: Synthetic profiling and schedule simulation only; no live sensor-control loop.
- `Data sensitivity`: Public paper and repository metadata; no private dataset or local path is published.

## Observations

- `Observed pattern`: The most effective optimizations match one bottleneck to one structural property: octree digits to SRAM banks, zeros to skipped lanes, and vertical access skew to cache partitions.
- `Observed pattern`: Benefits change with input channels. Pipeline overlap dominates when search is visible; sparse compute dominates when channel work grows; cache benefit declines when a fixed budget covers a smaller fraction of weights.
- `Technical implication`: A portable implementation needs a profiling gate. Sensor geometry, voxel size, operator mix, sparsity distribution, and kernel-plane frequency determine whether the design assumptions hold.
- `Technical implication`: Octree encoding matters because it enables collision-avoiding table structure, not because tree labels are intrinsically faster.
- `Contradiction or tension`: The paper emphasizes real-time industrial needs, yet the evidence is synthesized/simulated and lacks end-task accuracy reporting after quantization.
- `Contradiction or tension`: Cross-platform normalization enables comparison but also introduces a reproducibility burden that the public artifact set does not satisfy.
- `Cross-DEP pattern`: Efficient FM Survey and SpOctA agree that sparse mathematical work must be converted into supported execution. Physical Data and SpOctA both make representation a compute substrate. HERMES shows the downstream cost of losing task or scene quality while optimizing the 3D pipeline.
- `Open question`: How robust is the 45-83% middle-plane access skew across sensors, voxel resolutions, scenes, weather, and newer sparse/transformer hybrids?
- `Reviewer hypothesis`: A compiler that selects hash, octree, sorted/rank, or direct-map search per layer may generalize better than a single fixed search engine.

## Considerations

Hardware comparisons require a versioned envelope: process node, voltage, frequency, SRAM macro assumptions, DRAM model, precision, operator coverage, dataset, model configuration, preprocessing, and normalization. A speedup without that envelope is not portable evidence. At minimum, future artifacts should expose both raw and normalized results.

Accuracy and safety must remain coupled to performance. Quantization, sparse skipping, voxel blocking, map reuse, and sensor-specific caching can change numerical behavior or performance on rare objects. For autonomous-driving workloads, evaluation should include rare-agent recall, near-field geometry, occlusion, low-light/weather slices, latency tails, and fail-safe behavior. SpOctA itself is an accelerator study, not a certified perception system.

Maintainability is another constraint. Operator definitions, coordinate ranges, models, compilers, memory macros, and sensor layouts evolve. A practical implementation needs trace schema versioning, assertions on map correctness, bank-conflict telemetry, overflow handling, cache-miss reporting, and a fallback path to a general sparse-convolution implementation.

The related entries suggest a lifecycle contract. Efficient FM Survey contributes resource accounting; Physical Data contributes representation and evidence-boundary discipline; HERMES contributes workload quality and 3D safety slices. An implementation should be accepted only when the resource, correctness, and workload contracts pass together.

## Strengths

- The work identifies three distinct bottlenecks and supplies a matching architectural mechanism for each.
- OCTENT connects an algorithmic representation change to an explicit banked and pipelined hardware design.
- The design supports multiple common sparse-convolution operators instead of optimizing only one layer type.
- Figure 9 decomposes search, pipeline/sparsity, and caching effects rather than presenting only end-to-end speedup.
- The evaluation spans indoor/outdoor segmentation and detection across four established datasets.
- The paper reports area, power, SRAM, throughput, energy efficiency, frame rate, and breakdowns, providing more than a single performance scalar.
- The source package exposes equations, algorithms, and figure assets that make the paper easier to audit structurally.

## Weaknesses

- Results are based on synthesis, simulation, and modeling rather than reported silicon measurements.
- No official RTL, simulator, trace set, synthesis constraints, PrimeTimePX activity, CACTI configuration, or normalization scripts were established.
- The paper says 8-bit networks were retrained for accuracy recovery but does not show task-accuracy results in the reviewed evaluation.
- Cross-platform comparisons span different processes, throughputs, workloads, and operator scopes; normalization cannot fully eliminate those differences.
- The access-skew and sparsity assumptions may be sensor-, model-, layer-, and voxelization-specific.
- Latency tails, irregular/adversarial coordinate distributions, FIFO overflow, bank pressure, and worst-case cache behavior are not foregrounded.
- Energy and performance uncertainty across tool versions, SRAM macros, DRAM traffic, and physical design are not quantified.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release a minimal reproducibility kit | Reproducibility | Public sources do not reproduce the reported hardware numbers | Independent audit and easier extension | Engineering and IP review | Recreate one layer and one benchmark end to end |
| Publish raw and normalized baseline tables | Comparison | Normalization hides important denominators | More defensible speedup claims | Larger artifact and documentation burden | Third-party recomputation from raw values |
| Report post-quantization task quality | Correctness | "Recovered accuracy" is not quantified | Connects speed to perception quality | Retraining and evaluation cost | Model/dataset metrics with seeds and tolerances |
| Add worst-case spatial traces | Robustness | Bank conflicts and FIFO pressure may differ from averages | Stronger latency-tail evidence | Trace generation burden | Synthetic clustered, planar, dense, and empty scenes |
| Sweep sensor and voxel configurations | Generalization | Weight-plane skew may not transfer | Defines where non-uniform caching helps | Large experiment matrix | Profile multiple sensors, voxel sizes, and models |
| Report physical-design uncertainty | Hardware evidence | Synthesis/CACTI estimates omit layout effects | More realistic readiness assessment | Place-and-route effort | Post-layout timing, area, power, and sensitivity ranges |
| Add safe fallback behavior | Deployment | Specialized schedules can encounter unsupported shapes | Correctness under drift | Extra control and area | Differential tests against a reference operator |

## Potential Implementations

1. **Sparse Spatial Profiler**
   - `User`: Accelerator and compiler teams.
   - `Goal`: Decide whether an OCTENT/SPAC-like path fits a model and sensor trace.
   - `Core mechanism`: Measure coordinate distribution, octree-bank balance, operator mix, activation zeros, kernel-plane access, and memory traffic.
   - `Required inputs`: Public/synthetic coordinate and activation traces, layer metadata, bounded hardware profile.
   - `Outputs`: Versioned Markdown/JSON evidence with fit scores and failure cases.
   - `Risk controls`: Synthetic or licensed traces, no raw sensitive sensor upload, deterministic limits.
   - `Evaluation`: Compare profiler predictions with a reference simulator on held-out layers.

2. **Neighborhood Schedule Sandbox**
   - `User`: Sparse-tensor runtime researchers.
   - `Goal`: Compare octree, hash, rank/sort, and direct-map schedules before RTL.
   - `Core mechanism`: Execute bank and FIFO models over identical bounded coordinate sets.
   - `Required inputs`: Synthetic voxel sets, kernel shapes, bank count, FIFO depth, latency model.
   - `Outputs`: Collision, throughput, buffer, and memory-access traces.
   - `Risk controls`: No live control; hard caps on coordinates and cycles; reference-map correctness oracle.
   - `Evaluation`: Property tests plus differential IN-OUT maps against a CPU implementation.

3. **3D Efficiency Contract Runner**
   - `User`: Perception and world-model release teams.
   - `Goal`: Join task quality with accelerator resource claims.
   - `Core mechanism`: Import aggregate model outputs and accelerator traces, then evaluate latency, energy proxy, memory, geometry quality, rare-object slices, and provenance together.
   - `Required inputs`: Public/synthetic evaluation outputs, source metadata, pinned metric definitions, hardware profile.
   - `Outputs`: Signed release-gate bundle with Pareto and failure-slice reports.
   - `Risk controls`: Offline/simulator-only, licensed data, no vehicle actuation, human approval.
   - `Evaluation`: Recompute published aggregate metrics and inject synthetic failures to test gate sensitivity.

## Three Ways to Exercise This Research

1. `Octree distribution audit`: Objective - determine whether low-order octree digits balance across eight banks. Inputs - bounded synthetic coordinate sets representing uniform, clustered, planar, and road-like scenes. Method - encode coordinates, count banks, model same-cycle queries, and compare to a hash partition. Output - distribution and collision report. Success criterion - every trace has reproducible maps and explicit skew. Stop condition - coordinate bounds or reference-map correctness fail.
2. `Sparse-lane latency model`: Objective - test when activation sparsity becomes cycle savings. Inputs - synthetic 16-lane activation vectors and channel sweeps. Method - compare dense cycles, ideal zero skipping, and gather/arrange overhead. Output - latency and utilization curves. Success criterion - the model exposes a break-even sparsity rather than assuming all zeros are free. Stop condition - overhead or scheduling semantics are undefined.
3. `Cache-skew sensitivity sweep`: Objective - test non-uniform weight caching under changing sensor/voxel assumptions. Inputs - synthetic center/middle/up/down access histograms and fixed SRAM budgets. Method - allocate partitions, compute miss traffic and energy proxy, then perturb the histograms. Output - robustness envelope. Success criterion - the report identifies where uniform caching wins. Stop condition - access counts or energy denominators lack provenance.

## Example MVP Product

- `Product name`: Sparse3D Evidence Bench.
- `Target user`: Sparse-tensor compiler and 3D-perception research teams evaluating accelerator ideas before RTL investment.
- `Problem`: Paper speedups are difficult to transfer because coordinate distributions, operator coverage, sparsity, memory limits, baseline envelopes, and task-quality effects are not normalized.
- `Core workflow`: Import a bounded public/synthetic trace; validate schema; build reference IN-OUT maps; profile octree banks, sparsity, kernel-plane frequency, FIFO pressure, and memory traffic; run alternative schedules; join results with task-quality aggregates; export a public-safe evidence bundle.
- `Data requirements`: Synthetic or licensed coordinate/activation traces, layer/operator metadata, hardware/memory profile, reference outputs, source URLs, and metric definitions. Raw sensitive driving data is not required.
- `Architecture`: Local CLI and library; schema validator; CPU reference mapper; octree/hash/rank schedule simulators; sparse-lane model; cache planner; task/resource metric joiner; Markdown/JSON exporter.
- `Success metrics`: 100% differential map agreement with the reference; deterministic reruns; explicit bank/FIFO/memory counts; break-even sparsity estimate; raw and normalized resource results; task-quality slice coverage; zero private-path leakage.
- `Risk controls`: Offline-only; hard input/cycle/memory caps; licensed/public/synthetic data; no actuation; source-withholding policy; human-reviewed conclusions; unsupported operators fail closed to the reference path.
- `Limitations`: The MVP cannot predict post-layout timing/power, validate silicon, reproduce unavailable RTL, certify vehicle safety, or replace end-to-end model evaluation.
- `MVP boundary`: Trace analysis and schedule simulation only; no HDL generation or deployment.
- `Deployment model`: Local-only CLI with reproducible container/environment lockfile.
- `Evaluation plan`: Unit/property tests for encoding, differential maps, synthetic conflict cases, published-table transcription checks, and red-team tests for misleading normalization.
- `Failure modes`: Incorrect coordinate convention, hidden preprocessing, incomparable baselines, underestimated control overhead, nonrepresentative traces, or task metrics detached from performance traces.
- `Maintenance plan`: Version trace schemas, operator definitions, hardware profiles, metric denominators, source locators, and expected outputs.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| PointAcc | Accelerator baseline | General point-cloud acceleration and rank-based neighborhood processing contrasted by SpOctA | DOI locator available through paper references; MICRO 2021 |
| A Sparse Convolution Neural Network Accelerator for 3D/4D Point-Cloud Image Recognition | Accelerator baseline | Prior sparse-convolution ASIC and pipeline tradeoff | IEEE TVLSI 2022, as cited by SpOctA |
| 28 nm unified sparse-convolution accelerator | Accelerator baseline | Parallel search and object-detection comparison | ISSCC 2023, as cited by SpOctA |
| Minkowski Engine / 4D Spatio-Temporal ConvNets | Model/runtime basis | Sparse convolution and MinkUNet benchmark context | https://arxiv.org/abs/1904.08755 |
| SECOND | Model baseline | Sparse-convolution object-detection model used in KITTI/nuScenes evaluation | https://doi.org/10.3390/s18103337 |
| ScanNet | Dataset | Indoor segmentation workload | http://www.scan-net.org/ |
| SemanticKITTI | Dataset | Outdoor LiDAR segmentation workload | http://semantic-kitti.org/ |
| KITTI | Dataset | Autonomous-driving detection workload | https://www.cvlibs.net/datasets/kitti/ |
| nuScenes | Dataset | Multimodal autonomous-driving workload | https://www.nuscenes.org/ |
| Efficient FM Survey - DEP-E | Related Black Lake entry | Resource envelopes, sparse execution, and systems accounting | `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` |
| Physical Data - DEP-E | Related Black Lake entry | Representation-substrate efficiency and hardware-evidence boundaries | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` |
| HERMES World Model - DEP-E | Related Black Lake entry | 3D point-cloud/autonomous-driving workload and safety context | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2308.09249 | Identity, authors, date, subject, abstract, acceptance note | 2026-07-18 | Primary metadata |
| R2 | https://arxiv.org/pdf/2308.09249 | Full paper, figures, tables, quantitative claims | 2026-07-18 | Complete file inspected locally and withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/2308.09249 | Full-paper HTML text | 2026-07-18 | Approved fallback; complete file inspected locally and withheld |
| R4 | https://arxiv.org/e-print/2308.09249 | TeX/source sections, equations, figure inventory | 2026-07-18 | Source package inspected locally and withheld |
| R5 | https://doi.org/10.48550/arXiv.2308.09249 | arXiv DOI | 2026-07-18 | Stable identifier |
| R6 | https://doi.org/10.1109/ICCAD57390.2023.10323728 | Published DOI | 2026-07-18 | Publisher locator |
| R7 | https://ieeexplore.ieee.org/document/10323728 | IEEE publication locator | 2026-07-18 | Body unavailable to browser |
| R8 | https://lvdongxu.github.io/ | Author-maintained ICCAD publication listing | 2026-07-18 | Author context |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, source locality, attribution, commit rules | 2026-07-18 | Live default-branch authority |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E container and publication-index rules | 2026-07-18 | Live default-branch authority |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and attribution rules | 2026-07-18 | Read before using related-repository dedup context |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey/efficient_fm_survey_manuscript.md | Related resource-efficiency synthesis | 2026-07-18 | Exactly one of three related DEPs |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md | Related representation/hardware synthesis | 2026-07-18 | Exactly one of three related DEPs |
| R14 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md | Related 3D point-cloud workload synthesis | 2026-07-18 | Exactly one of three related DEPs |

## Appendix

### Source Integrity and Locality

The selected unit was initially partial because it lacked full-paper HTML. The existing PDF passed a 10 KB minimum, `%PDF-` header, and trailing `%%EOF` check and was preserved. ArXiv metadata and source were fetched with bounded attempts. The official arXiv full-paper HTML endpoint was unavailable, so one approved ar5iv fallback was collected. It passed a 5 KB minimum, 2,000-character body minimum, document-marker requirement, two-heading minimum, and two-structure-term minimum.

Final local verification facts:

- PDF: 6,442,343 bytes; header and EOF valid.
- Full HTML: 312,845 bytes; 53,023 body characters; document marker present; 90 heading/section markers; six structure terms.
- Metadata HTML: 42,555 bytes; metadata-only role.
- Source archive: 2,792,455 bytes; 21 entries; tar listing valid.
- Extraction cache: PDF, HTML, and source-text outputs present; status `cached`.
- Local records: README, provenance JSON, summary CSV, and verification report updated and parsed.
- Partial files: none.
- Public upload: no source documents, extracted text, cache files, or local verification files included.

### Replication Checklist

- Obtain or independently implement a correct CPU sparse-convolution IN-OUT map reference.
- Pin coordinate convention, voxel size, tensor layout, operator definitions, precision, and preprocessing.
- Recreate OCTENT encoding, bank mapping, query schedule, map FIFO, and block partition with assertions.
- Recreate SPAC gather/arrange behavior and input/output-stationary modes.
- Record layer traces for all four paper benchmark configurations.
- Version synthesis constraints, SRAM macros/CACTI inputs, DRAM model, voltage, frequency, and activity factors.
- Report raw task accuracy before/after 8-bit retraining.
- Publish raw and normalized baseline results plus scripts.
- Add worst-case coordinate, bank-conflict, FIFO, cache-miss, and latency-tail tests.
- Separate simulator, synthesis, post-layout, FPGA, and silicon evidence.

### Decision Usefulness

This artifact supports deciding whether SpOctA's three mechanisms deserve profiling or simulation for a sparse 3D workload. It does not support purchasing, fabricating, deploying, or safety-certifying an accelerator, nor does it establish that the reported speed/energy improvements reproduce outside the authors' evaluation flow.
