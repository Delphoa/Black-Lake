---
title: "Device Tuning MTL - DEP-E"
generated_at: "2026-07-19"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of a pooled device encoder and cloud decoder proposed for compact multi-task vision transformers."
source_status: "verified PDF, approved full-paper HTML fallback, TeX/source, metadata, workshop record, and successor context inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "arXiv:2302.10820v1 plus public workshop, successor-publication, and code-availability records inspected through 2026-07-19"
primary_url: "https://arxiv.org/abs/2302.10820"
stable_identifier: "arXiv:2302.10820v1; DOI 10.48550/arXiv.2302.10820"
confidence_summary: "High for identity, printed architecture, and table transcription; medium for mechanism interpretation; low for multi-task, communication, reproducibility, and deployment claims."
safety_scope: "offline research, synthetic prototyping, and measured edge/cloud evaluation; no production or autonomous-system authorization"
distribution_notes: "Paper PDF, HTML, metadata, TeX/source, extraction cache, and integrity records remain local and are not redistributed; temporary page renderings were removed after inspection, and no .source directory was created."
---

# Device Tuning MTL - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Device Tuning for Multi-Task Large Model | Primary paper | PDF, full HTML, TeX/source | arXiv:2302.10820v1 | https://arxiv.org/abs/2302.10820 | CC BY 4.0 shown on arXiv; local copies withheld | 2026-07-19 | Complete and inspected |
| S2 | arXiv DOI record | Stable identity | DOI metadata | 10.48550/arXiv.2302.10820 | https://doi.org/10.48550/arXiv.2302.10820 | DataCite/arXiv DOI | 2026-07-19 | Resolved |
| S3 | Deployable AI 2023 accepted papers | Venue context | Official workshop page | DAI 2023 | https://sites.google.com/view/dai-2023/accepted-papers | Public workshop record | 2026-07-19 | Inspected |
| S4 | High-Efficiency Device-Cloud Collaborative Transformer Model | Successor context | CVF open-access proceedings page | CVPR Workshops 2023 | https://openaccess.thecvf.com/content/CVPR2023W/MobileAI/html/Jiang_High-Efficiency_Device-Cloud_Collaborative_Transformer_Model_CVPRW_2023_paper.html | Different paper; claims not transferred | 2026-07-19 | Abstract and record inspected |
| S5 | Black Lake repository guidance | Filing authority | README | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository authority | 2026-07-19 | Inspected |
| S6 | Black Lake DEP guidance | Filing/index authority | README | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public repository authority | 2026-07-19 | Inspected |
| S7 | Black-Lake-Data guidance | Companion dedup authority | README | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository authority | 2026-07-19 | Inspected |
| S8 | Three related Black Lake DEPs | Conceptual context | DEP-A/DEP-E reviews | repository records | See `## Related Research and Reading` | Derived public artifacts; associations do not transfer claims | 2026-07-19 | Inspected |

Authors: Penghao Jiang, Xuanchen Hou, and Yinsi Zhou. The paper prints affiliations with The Australian National University and Deakin University, was submitted on 2023-02-21, and is classified under Computer Vision and Pattern Recognition (`cs.CV`). The arXiv metadata describes it as an accepted DAI 2023 workshop paper and exposes only an arXiv-issued DOI; no separate publisher DOI for this title was identified.

Source-integrity status is `complete`. A valid 290,141-byte PDF with a `%PDF-` header and trailing `%%EOF` was preserved. The initially missing full paper was repaired with a 77,672-byte approved ar5iv HTML fallback containing 18,911 body characters, document markers, 30 heading/section markers, and five paper-structure terms. Metadata HTML and a valid 10-entry TeX/source archive were also retained locally. No partial file remained, and none of these source or derivative files is present in this repository.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 PDF/HTML/TeX | Primary paper | Full method, equations, tables, figures, references | Architecture and printed claims | High for transcription | Four-page workshop paper; underspecified method |
| E2 | S1 Tables 1-2 | Primary empirical | Parameter counts and ImageNet-1k top-1 values | Compact-classifier result | High for transcription | No recipe, uncertainty, compute, or matched controls |
| E3 | S1 Figures 1-2 | Primary visual | Device/cloud illustration and device-encoder/cloud-decoder sketch | Intended system boundary | Medium-high | Diagram omits tensor/transport/runtime details |
| E4 | S1 introduction versus method/experiments | Primary negative evidence | Multi-task, task-specific, and gradient-normalization language disappears from technical evaluation | Claim/evidence gap | High | Absence may reflect paper length, but remains material |
| E5 | S2/S3 | Primary metadata/venue | Identity, date, license, workshop listing | Provenance | High | Venue page adds no technical evidence |
| E6 | Focused GitHub and paper-record search | Availability inspection | No author-linked implementation, config, checkpoint, or data manifest found | Reproducibility boundary | Medium-high | Time-bounded negative search; future release remains possible |
| E7 | S4 | Primary successor record | Overlapping authors and related device/cloud transformer concept | Follow-on reading | High for metadata | Different title, authorship, task domain, and experiments |
| E8 | S8 | Related repository evidence | Edge/cloud metrics, token compression, conditional vision compute | Concept bridges and implementation controls | High for inspected DEP content | No claim transfer between research objects |
| E9 | Public extraction summary | Processing record | `pypdf`, HTML-regex, and tarfile status plus byte counts | Cache methodology | High | Extracted source text remained local |

## Executive Summary

*Device Tuning for Multi-Task Large Model* proposes a device encoder that pools a transformer hidden sequence before forwarding it to a cloud decoder. The stated intuition is that halving the token sequence reduces local attention work and device-to-cloud communication while shared cloud parameters and task-specific device parameters support multiple tasks. The introduction additionally invokes gradient normalization for task balancing.

The paper's direct evidence is much narrower. Two ImageNet-1k tables report top-1 accuracy and parameter counts. The strongest same-scale point is 70.6% top-1 at 2.2M parameters, compared with MobileNetV2 at 69.8% and 2.6M: a reported 0.8 percentage-point gain with about 15.4% fewer parameters. No task inventory, multi-task result, gradient-normalization definition, pooling ablation, training recipe, FLOP count, measured latency, memory, energy, bandwidth, or payload size is reported.

The defensible conclusion is therefore that the paper documents a promising compact vision/split-transformer hypothesis and one favorable ImageNet parameter-accuracy point. It does not establish the advertised multi-task generalization, communication reduction, or device/cloud efficiency. Confidence is high for the printed architecture and tables, medium for reconstruction of the intended split, and low for reproducibility or deployment generality because no official implementation or complete experimental specification was found.

## Detailed Summary

### Problem and Motivation

The paper frames vision transformers as accurate but expensive for resource-constrained devices. Cloud-only execution centralizes compute but introduces transmission and service dependence; device-only compact models may lose accuracy. The proposed design seeks a middle ground where the device performs early representation work, compresses the state, and relies on a cloud component for later computation.

The introduction presents two goals. First, improve the device resource-to-performance tradeoff while using cloud and device capacity jointly. Second, learn one scalable model across multiple tasks instead of maintaining a large independent model for every task. These are meaningful goals, but they require separate evidence: representation size, execution cost, outcome quality, task interference, and failure behavior.

### Transformer Baseline

The paper restates a conventional pre-layer computation with multi-head self-attention, feed-forward processing, residual connections, and layer normalization. Given hidden states `h` in `R^(T x D)`, the device encoder creates `h'` in `R^(T' x D)` for `T' < T`. Attention then operates on the shorter sequence. This is the central formal mechanism.

### Device Encoder and Cloud Decoder

Figure 2 shows an embedding, a pooling step, self-attention, feed-forward processing, a device encoder boundary, and an upward transfer into a cloud decoder. The prose says close tokens are merged into larger semantic components and later says sequence length is halved. It does not identify whether pooling is average, max, convolutional, learned, attention-based, or task-conditioned; where it is placed relative to patch embedding and positional encoding; or how spatial identity is preserved.

The paper also does not define the transfer representation. Missing fields include tensor precision, quantization, serialization, dimensions at the network boundary, uplink protocol, privacy, retry/fallback behavior, cloud state, batching, and whether gradients cross the boundary during training. Without these, “reduced communication” is an architectural expectation rather than a measured system result.

### Multi-Task and Gradient-Balancing Claims

The introduction says shared parameters live in the cloud, task-specific parameters live on devices, and gradient normalization dynamically balances multi-task training. The method section contains no task-indexed objective, gradient norm, target training rate, loss weight, adapter/head definition, device parameter ownership, or update schedule. The experiments contain no task list or per-task result. The TeX/source confirms that the terms appear in the introduction but are not elaborated elsewhere.

This omission is central because “multi-task” is in the title and headline contribution. A single ImageNet classification table cannot measure negative transfer, task imbalance, shared-representation benefit, per-task regression, or reduction in deployed model copies.

### Experimental Evidence

The experiments state that the framework is pretrained and then fine-tuned for downstream tasks, but disclose no dataset split beyond ImageNet-1k, image resolution, pretraining source, augmentation, optimizer, schedule, batch size, epochs, regularization, precision, hardware, seeds, or checkpoint-selection rule. There is no ablation for pooling type, pooling ratio, split depth, cloud decoder size, task-specific parameters, or gradient normalization.

Table 1 compares compact CNNs against the proposed model:

| Model | Parameters | Top-1 (%) | Reviewer note |
|---|---:|---:|---|
| MobileNetV1 | 2.6M | 68.4 | Published comparator |
| MobileNetV2 | 2.6M | 69.8 | Best listed baseline |
| MobileNetV3 | 2.5M | 67.4 | Value is lower than the common large MobileNetV3 result; recipe undisclosed |
| ShuffleNetV2 | 2.3M | 69.4 | Near parameter match |
| ESPNetV2 | 2.3M | 69.2 | Near parameter match |
| Ours | 2.2M | 70.6 | Author-reported best row |

Table 2 compares different backbones:

| Model | Parameters | Top-1 (%) | Relative parameter context |
|---|---:|---:|---|
| DenseNet-169 | 14M | 76.2 | Proposed model is about 11.4% larger |
| EfficientNet-B0 | 5.3M | 76.3 | Proposed model is about 2.94 times larger |
| ResNet-101 | 44.5M | 77.4 | Proposed model is about 65% smaller |
| ResNet-101-SE | 49.3M | 77.6 | Proposed model is about 68% smaller |
| Ours | 15.6M | 78.0 | Best printed top-1 |

The second table shows a favorable point but mixes very different model sizes. It cannot by itself support scalability, compute efficiency, or communication efficiency.

### Visual Evidence

Figure 1 is a product-style mobile-recognition illustration rather than an experiment. Figure 2 shows the conceptual split and pooling location. All four PDF pages were rendered and inspected; Tables 1-2 match the TeX values, and no hidden appendix, extra experiment, or implementation note is present. Nonfatal renderer font warnings did not make the figures, equations, or tables unreadable.

### External and Successor Context

The official DAI 2023 accepted-paper list confirms the selected title and authors. A later CVPR Workshops 2023 paper, *High-Efficiency Device-Cloud Collaborative Transformer Model*, shares Penghao Jiang and Yinsi Zhou and develops a closely related device/cloud transformer concept for language modeling. It is useful evidence that the research direction continued, but it is a distinct publication with different authors and experiments. Its claims cannot repair missing evidence in arXiv:2302.10820v1.

### Code and Artifact Availability

No code URL appears in the selected paper, arXiv metadata, or DAI page. Focused GitHub searches for the exact title and arXiv ID found no author-linked repository; two ID hits were a third-party paper index and an unrelated text file. No configuration, checkpoint, data manifest, training log, or environment lock was found. No code, model, dataset, or result was executed for this review.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Device-side sequence pooling reduces representation length. | Mechanism | E1/E3 | Directly supported at the shape/prose level; operator unspecified. | High |
| C2 | The proposed compact classifier outperforms listed same-scale baselines. | Author empirical claim | E2 | Supported by Table 1 under unknown training comparability; best margin is 0.8 points. | High for transcription, medium for comparison |
| C3 | The architecture reduces device/cloud communication. | Author systems claim | E1/E3 | Plausible from fewer tokens, but no bytes, precision, transport, or end-to-end measurement is provided. | Low-medium |
| C4 | The system is a massively multi-task framework. | Author claim | E4 | Unsupported by the disclosed experiment; only ImageNet classification appears. | Low |
| C5 | Gradient normalization balances tasks. | Author mechanism claim | E4 | Mentioned but not specified, derived, cited as a concrete implementation, or evaluated. | Low |
| C6 | The method scales across backbones. | Author empirical claim | E2 | Table 2 reports one proposed point against heterogeneous published models; no controlled backbone sweep is described. | Low-medium |
| C7 | The method is efficient on devices. | Deployment implication | E1/E2/E3 | Parameters alone do not establish latency, memory, energy, throughput, or reliability. | Low |
| C8 | No reselection was required. | Process claim | Dedup records | Exact ID/DOI/title/slug/artifact/memory/companion/worktree scans were clear. | High |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E review of one uniformly selected local arXiv unit, preserving the architecture, quantitative evidence, missing evidence, repository context, and implementation relevance.
- `Sources inspected`: Verified full PDF, approved full-paper HTML fallback, TeX/source archive, abstract metadata, arXiv DOI/license, rendered pages, official DAI accepted-paper list, CVF successor record, focused GitHub searches, live repository authorities, public cache summary, and exactly three related DEP artifacts.
- `Discovery strategy`: Used `rg --files -g "*.pdf"` to enumerate the archive, collapsed PDFs by parent directory, selected a PowerShell `Get-Random` index, resolved identity from nearby metadata, scanned public artifacts/memory/worktrees and Black-Lake-Data for duplicates, then reviewed local primary sources and authoritative public records.
- `Inclusion criteria`: Sources directly supporting paper identity, method, tables, figures, venue, availability, filing authority, or a concrete device/cloud, sequence-compression, or compact-vision concept bridge.
- `Exclusion criteria`: Abstract-only evidence was excluded from technical conclusions; generic title-term inventory hits did not count as duplicates; secondary aggregators did not support major claims; local source files were excluded from public output.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, systems, product-research, and replication analysis.
- `Evidence handling`: Author claims, table values, reviewer computations, negative evidence, successor context, and implementation proposals are labeled separately. Quantitative values were checked against both TeX and rendered tables.
- `Uncertainty handling`: Missing implementation, absent training details, unmatched baselines, time-bounded code search, and unmeasured system behavior remain explicit rather than inferred.
- `Extraction process`: Source integrity was classified first; missing full-paper HTML was repaired and strictly verified; a private `missing-only` cache extracted PDF text with `pypdf`, HTML text with a regex parser, and TeX/source text with `tarfile`.
- `Version control`: Paper pinned to arXiv v1; public repository authorities read from their live default branches on the access date; successor work treated as a separate evidence object.
- `Random selection methodology`: 75,778 PDFs collapsed to 75,776 parent-paper units; uniform zero-based draw index 74,319; first draw accepted; zero exclusions and reselections.
- `Cache methodology`: Initial miss; local repair preceded extraction; `missing-only` completed in 0.352 seconds with 17,777 PDF-text bytes, 19,172 HTML-text bytes, and 35,052 source-text bytes; final status `cached`; `pdftotext` was unavailable and `pypdf` succeeded as fallback.
- `Dedup/reselection validation`: No arXiv ID, DOI, normalized-title, slug, artifact, memory, companion-repository, or active-worktree match; no same-paper marker within 24 hours; generic companion title-term hits were metadata-only.
- `Reviewer stance`: Paper report, critique, DEP-ready preservation, implementation brief, product translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv v1 identity, architecture, equations, figures, tables, claims, venue evidence, implementation availability, successor context, exactly three related DEP bridges, and bounded implementation implications.
- `Temporal boundary`: Sources and repository records accessed on 2026-07-19.
- `Evidence limits`: No training run, inference benchmark, dataset download, checkpoint, source execution, code audit, or result reproduction. No separate publisher version for the selected title was identified.
- `Assumptions`: The verified PDF, approved full-paper HTML fallback, and TeX/source correspond to arXiv v1; printed percentages are top-1 points on the authors' ImageNet setup; related DEP links remain repository-resolvable.
- `Constraints`: Local source files and derivatives cannot be uploaded. Example implementations use synthetic or authorized inputs. Device/cloud deployment would require privacy, security, availability, and data-governance review.
- `Out of scope`: Reconstructing missing authors' code as if faithful, certifying device efficiency, asserting multi-task generalization, production deployment, or transferring results from the successor paper.
- `Intended use`: Research review, DEP deposition, replication planning, edge/cloud measurement design, and safe MVP ideation.
- `Audience`: Computer-vision researchers, ML systems engineers, edge-AI developers, multi-task-learning researchers, and technical reviewers.
- `Reproducibility boundary`: Another reviewer can trace every printed equation/table and rebuild an independent hypothesis, but cannot faithfully reproduce the reported model without architecture and training details.
- `Data sensitivity`: Public research records only in this artifact; original source files and any future evaluation images remain withheld or separately governed.
- `Operational boundary`: The manuscript does not authorize autonomous or safety-critical use and does not treat parameter count as a deployment certification.

## Observations

- `Observed pattern`: The paper's strongest evidence is a compact ImageNet point, not a multi-task system result.
- `Observed pattern`: Sequence halving is the only concrete compression ratio, while the pooling operator and spatial preservation mechanism remain unnamed.
- `Contradiction or tension`: The title and introduction foreground multi-task learning and gradient normalization, but the method and experiments never define or evaluate either.
- `Contradiction or tension`: The paper claims reduced communication and device efficiency but reports only parameters and top-1 accuracy.
- `Technical implication`: Any implementation must separately measure representation, execution, and outcome gains; none can stand in for the others.
- `Technical implication`: Table 2 needs matched recipes and resource budgets before it can support scalability or efficiency conclusions.
- `Open question`: Does a learned or fixed pooling operator preserve small/rare visual regions, and how does degradation vary by class, spatial scale, and compression ratio?
- `Open question`: Does a device/cloud split still help under weak networks, retries, privacy controls, batching, quantization, and cloud outage?
- `Reviewer hypothesis`: The design becomes substantially more credible when the split tensor is versioned, protected tokens/regions bypass compression, and a controller selects ratios from measured quality/cost frontiers.

## Considerations

### Measurement Semantics

Parameter count is a storage/model-capacity proxy. It is not FLOPs, latency, throughput, peak memory, energy, bandwidth, message bytes, cloud cost, or tail reliability. A deployment study must report each selected metric with hardware, software, precision, batch, concurrency, network, and denominator.

### Baseline Fairness

MobileNet, ShuffleNet, ESPNet, DenseNet, EfficientNet, and ResNet results are sensitive to resolution, augmentation, optimizer, schedule, pretraining, distillation, and checkpoint selection. The paper does not show that all rows use one recipe. A replication should train or evaluate competent baselines under matched conditions and report confidence intervals.

### Multi-Task Interference

Shared parameters can reduce duplication but also create gradient domination, negative transfer, and fairness concerns across tasks or endpoints. Per-task losses, gradients, quality, update frequency, and rollback state should be logged. An aggregate score must not hide a task-specific regression.

### Privacy, Security, and Availability

Intermediate activations can leak inputs or attributes even when they are shorter. Transport encryption, endpoint/cloud trust, retention, access control, replay protection, integrity, outage behavior, and local fallback are part of the split design. This paper does not evaluate them.

### Maintenance and Versioning

Pooling layers, cloud decoders, task-specific modules, tokenization/patching, and transport schemas must be version-compatible. A cloud update can invalidate an endpoint encoder; a task update can shift gradients into other tasks. Compatibility tests and reversible rollout are required.

## Strengths

- The paper identifies a relevant device/cloud design space before current foundation-model split inference became widespread.
- The shape-level mechanism is legible: shorten the sequence before later attention and cloud decoding.
- Table 1 presents a favorable parameter/accuracy point against several compact CNNs.
- The architecture naturally motivates separate shared and endpoint-specific modules.
- The short paper is transparent enough that major missing fields are identifiable rather than hidden in a complex pipeline.
- The CC BY 4.0 arXiv record and available TeX/source improve inspectability.

## Weaknesses

- The claimed multi-task framework has no disclosed task set, task objective, head/module definition, or per-task result.
- Gradient normalization is mentioned but not specified, cited as an implemented algorithm, or evaluated.
- Pooling type, placement, spatial semantics, split tensor, device/cloud protocol, and cloud decoder are underspecified.
- ImageNet training and evaluation details are absent, preventing a fair replication.
- Table 2 mixes parameter scales and cannot establish a controlled scalability frontier.
- No pooling ratio, split location, architecture component, or gradient-balancing ablation is reported.
- No FLOPs, latency, throughput, memory, energy, bandwidth, serialized bytes, privacy, or failure evidence supports the systems claims.
- No code, configuration, checkpoint, data manifest, or environment was found.
- No repeated seeds, uncertainty, calibration, class slices, or failure analysis is present.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Specify pooling, split, tensor schema, and decoder | Method | Makes the architecture implementable | Faithful replication | May expose that some savings are assumed | Shape/unit tests plus reference forward pass |
| Publish the complete training manifest | Reproducibility | Baseline values depend on recipe | Fair comparisons | Engineering/documentation work | Independent rerun with hash-pinned config |
| Add a real multi-task suite | Core claim | ImageNet alone cannot test multi-task learning | Measures transfer and interference | Dataset/task balancing complexity | Per-task and aggregate metrics with fixed denominators |
| Compare fixed weights, GradNorm, and no balancing | Optimization | Gradient normalization is currently unsupported | Isolates claimed mechanism | Additional tuning | Repeated-seed factorial ablation |
| Sweep pooling ratios/types and split depths | Compression | One implied halving point hides the frontier | Selects robust operating regions | Larger experiment matrix | Quality, tokens, bytes, latency, memory, energy curves |
| Measure end-to-end systems cost | Deployment | Parameters are not runtime evidence | Tests communication/efficiency claims directly | Hardware/network instrumentation | Device/network/cloud profiles with p50/p95/p99 |
| Protect salient/rare regions and add fallback | Robustness | Pooling can erase small or rare evidence | Reduces catastrophic compression failures | Extra metadata and compute | Class/region slices, abstention, recovery tests |
| Release code, checkpoints, and expected outputs | Availability | Enables audit and successor work | Higher confidence and reuse | Maintenance burden | Clean-room reproduction and artifact checklist |

## Potential Implementations

1. **SplitTrace Bench**
   - `User`: Edge-AI and ML-systems team.
   - `Goal`: Determine whether a device/cloud split creates real savings at matched quality.
   - `Core mechanism`: Instrument multiple split depths and pooling ratios, then measure device, transport, and cloud stages separately.
   - `Required inputs`: Authorized evaluation images, model revisions, network profiles, device/cloud hardware, quality threshold.
   - `Outputs`: Quality/resource Pareto curves, fixed-denominator failures, trace manifests, and fallback report.
   - `Risk controls`: Local-only raw images, encrypted transport in authorized tests, redacted logs, no production rollout.
   - `Evaluation`: Repeated runs across strong/weak networks, batch sizes, precision modes, and class/region slices.

2. **Protected Visual Token Pooler**
   - `User`: Vision-model researcher.
   - `Goal`: Reduce token length without silently erasing small or safety-relevant regions.
   - `Core mechanism`: Pool low-risk adjacent tokens while protected regions retain original tokens and provenance pointers.
   - `Required inputs`: Patch embeddings, protection mask, pooling policy, compression budget.
   - `Outputs`: Compressed sequence, token map, achieved ratio, protected-token audit, reconstruction/quality diagnostics.
   - `Risk controls`: Conservative no-pooling fallback, immutable provenance, synthetic/public test data, failure threshold.
   - `Evaluation`: Compare average, learned, random, and no-pooling controls across ratios and region sizes.

3. **Multi-Task Gradient Ledger**
   - `User`: Multi-task training team.
   - `Goal`: Test whether shared cloud parameters and device-specific modules help multiple tasks without hidden regressions.
   - `Core mechanism`: Version task modules, log per-task losses/gradient norms, and compare fixed, uncertainty-based, and GradNorm-style weighting.
   - `Required inputs`: At least three authorized tasks, shared backbone, task modules, reproducible training manifest.
   - `Outputs`: Per-task quality, interference matrix, gradient traces, model-copy savings, resource and rollback ledger.
   - `Risk controls`: Per-task quality floors, early stop on regression, reversible checkpoints, access separation.
   - `Evaluation`: Repeated-seed single-task versus joint-training factorial study.

## Three Ways to Exercise This Research

1. **Rebuild the printed evidence sheet**: Objective - verify the paper's numerical claims without implying reproduction; inputs - Tables 1-2; method - transcribe values, compute parameter ratios and top-1 deltas, and flag unmatched budgets; output - a fixed table with reviewer calculations; success criterion - every value traces to a printed cell; stop condition - do not invent missing recipes or uncertainty.
2. **Run a synthetic split-cost pilot**: Objective - test the representation/execution distinction; inputs - synthetic token tensors, three pooling ratios, a loopback transport simulator, and a toy transformer; method - measure tokens, serialized bytes, device/pool/cloud time, and peak memory; output - a Pareto plot and trace ledger; success criterion - achieved compression and every cost stage are reported; stop condition - no claim of paper reproduction or production network behavior.
3. **Design a three-task interference test**: Objective - make the multi-task claim falsifiable; inputs - three public toy classification tasks, one shared backbone, task heads, fixed and gradient-normalized weighting; method - compare single-task and joint training over repeated seeds; output - per-task deltas, gradient traces, and failure flags; success criterion - no aggregate score hides a task below its floor; stop condition - halt when a task regression exceeds the declared bound.

## Example MVP Product

- `Product name`: SplitTrace Lab.
- `Target user`: ML systems team evaluating edge/cloud transformer partitions.
- `Problem`: Architecture diagrams and parameter counts are often mistaken for communication, latency, memory, or energy evidence.
- `Core workflow`: Register a model and authorized dataset; define candidate split/pooling policies; run synthetic smoke tests; benchmark device, transport, and cloud stages; preserve fixed-denominator outcomes; compare against device-only, cloud-only, and no-pooling controls; publish a public-safe evidence card.
- `Data requirements`: Public or authorized evaluation inputs, model/config hashes, tensor schema, device/network/cloud profiles, quality floors, and aggregate telemetry.
- `Architecture`: Local CLI orchestrator; pluggable model adapter; device/cloud workers in an authorized lab; trace collector; immutable manifest store; Pareto analyzer; static Markdown/HTML report generator.
- `Success metrics`: Matched-quality p50/p95/p99 latency, serialized bytes, peak memory, energy per example, throughput, failure/timeout rate, task-specific quality, achieved compression, and reproducible manifest coverage.
- `Risk controls`: Local-only raw inputs, least-privilege endpoints, encrypted authorized transport, no secrets in logs, redacted public reports, conservative fallback, human approval before non-lab deployment.
- `Limitations`: Lab networks may not represent production; instrumentation changes timing; synthetic tasks do not establish real-world safety; protected-token rules can miss unknown salient regions.
- `MVP boundary`: No autonomous decisions, no production traffic, no claim of faithful paper implementation, no unrestricted data collection, and no model/source redistribution.
- `Deployment model`: Local CLI plus isolated test workers and static evidence report.
- `Evaluation plan`: Unit-test tensor/schema validation; compare no-pooling and random-pooling controls; sweep three ratios and split depths; repeat across three network profiles and seeds; reviewer sign-off on failures.
- `Failure modes`: Schema mismatch, silent precision change, pooling erasure, stale cloud decoder, retry amplification, privacy leakage, instrumentation bias, aggregate masking of task failures, and missing baseline parity.
- `Maintenance plan`: Pin model/runtime/network profiles; invalidate results on schema or dependency changes; audit controls quarterly; retain append-only experiment manifests.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Efficient and Privacy Aware Edge Cloud Collaborative Inference | Related Black Lake DEP-A | Same device/cloud information boundary with measured latency, bandwidth, and privacy limits | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260719-Edge%20Cloud%20Split/2607.13093-whitepaper-review.md |
| K-Token Merging | Related Black Lake DEP-A | Direct latent sequence compression and compression-quality frontier | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-K%20Token%20Merging/2604.15153-whitepaper-review.md |
| Dynamic Multi-path Neural Network | Related Black Lake DEP-E | Compact vision and conditional compute with explicit runtime-evidence caveats | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-DMNN%20Conditional%20Paths/dmnn_conditional_paths_manuscript.md |
| High-Efficiency Device-Cloud Collaborative Transformer Model | Successor publication context | Related device/cloud transformer direction by overlapping authors | https://openaccess.thecvf.com/content/CVPR2023W/MobileAI/html/Jiang_High-Efficiency_Device-Cloud_Collaborative_Transformer_Model_CVPRW_2023_paper.html |
| GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks | Method baseline | Provides an explicit, testable gradient-normalization method missing from the selected paper | https://arxiv.org/abs/1711.02257 |
| Rethinking Spatial Dimensions of Vision Transformers (PiT) | Pooling neighbor | Earlier transformer pooling design cited by the selected paper | https://openaccess.thecvf.com/content/ICCV2021/html/Heo_Rethinking_Spatial_Dimensions_of_Vision_Transformers_ICCV_2021_paper.html |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2302.10820 | Identity, abstract, authors, date, subject, license, DOI, venue note | 2026-07-19 | Metadata only for abstract-level content |
| R2 | https://arxiv.org/pdf/2302.10820 | Full method, figures, equations, tables, references | 2026-07-19 | Local copy inspected and withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/2302.10820 | Full-paper text and structure cross-check | 2026-07-19 | Approved fallback after official HTML unavailable; local copy withheld |
| R4 | https://arxiv.org/e-print/2302.10820 | Exact TeX equations, tables, and terminology | 2026-07-19 | Local archive inspected and withheld |
| R5 | https://doi.org/10.48550/arXiv.2302.10820 | Persistent arXiv identity | 2026-07-19 | arXiv-issued DOI |
| R6 | https://creativecommons.org/licenses/by/4.0/ | License terms linked by arXiv | 2026-07-19 | Does not authorize this automation to upload local source files |
| R7 | https://sites.google.com/view/dai-2023/accepted-papers | DAI 2023 accepted-paper status | 2026-07-19 | Official workshop page |
| R8 | https://openaccess.thecvf.com/content/CVPR2023W/MobileAI/html/Jiang_High-Efficiency_Device-Cloud_Collaborative_Transformer_Model_CVPRW_2023_paper.html | Successor context | 2026-07-19 | Separate evidence object |
| R9 | https://doi.org/10.1109/CVPRW59228.2023.00214 | Successor publisher identity | 2026-07-19 | Not the selected paper's DOI |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Filing, source-locality, attribution policy | 2026-07-19 | Live default branch read before drafting |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E location and publication-index rule | 2026-07-19 | Live default branch read before drafting |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository dedup authority | 2026-07-19 | Live default branch read before drafting |
| R13 | Related DEP URLs in `## Related Research and Reading` | Concrete conceptual synthesis | 2026-07-19 | Exactly three related repository entries inspected |
| R14 | https://arxiv.org/abs/1711.02257 | Explicit GradNorm method baseline | 2026-07-19 | Related reading, not evidence for selected implementation |
| R15 | Focused GitHub public search for the exact title and arXiv ID | Time-bounded implementation availability | 2026-07-19 | No author-linked repository found; third-party/unrelated hits rejected |
| R16 | Public-safe extraction-cache summary | Extractor status, fallback, and output byte counts | 2026-07-19 | Summary validated with zero findings; cache and extracted text withheld |

## Appendix

### Replication Checklist

- [ ] Pin arXiv v1 source hashes and the local integrity record.
- [ ] Define input resolution, patching, positional encoding, pooling operator, ratio, and layer placement.
- [ ] Define device encoder, cloud decoder, split tensor, precision, serialization, transport, retries, and fallback.
- [ ] Define shared versus task-specific parameters, tasks, heads, losses, update ownership, and gradient-balancing algorithm.
- [ ] Release code, environment lock, configurations, checkpoints, data/split locators, seeds, and expected outputs.
- [ ] Reproduce no-pooling/device-only/cloud-only baselines before testing the proposed split.
- [ ] Train/evaluate compact baselines under one matched ImageNet recipe.
- [ ] Sweep pooling types, ratios, and split depths with repeated seeds.
- [ ] Report parameters, FLOPs, serialized bytes, device/cloud memory, latency percentiles, throughput, energy, failures, and quality.
- [ ] Add at least three tasks and publish per-task interference and regression floors.
- [ ] Stress small objects, rare classes, weak networks, cloud outages, stale versions, quantization, batching, concurrency, privacy probes, and recovery.
- [ ] Preserve fixed-denominator results and an append-only public-safe evidence card.

### Process and Source-Locality Record

- Uniform selection: 75,776 parent-paper units; zero-based draw 74,319; first draw accepted.
- Dedup: Exact ID, DOI, normalized title, slug, public artifact, automation memory, companion-repository, and 24-hour worktree scans clear.
- Initial integrity: `partial` because full-paper HTML was missing.
- Repair: Valid PDF preserved; metadata, approved ar5iv full paper, and 10-entry TeX/source archive collected with bounded retries.
- Final integrity: `complete`; zero partial files.
- Cache: Miss to `cached`; `pypdf`, HTML-regex, and tarfile succeeded; `pdftotext` unavailable.
- Review: All four PDF pages, two figures, two tables, equations, TeX/source, official workshop record, successor record, and focused code search inspected.
- Reproduction: None; no code/model/data execution.
- Distribution: No PDF, HTML, metadata page, TeX/source archive, cache, extracted text, local integrity record, temporary rendering, or `.source/` directory was uploaded.
