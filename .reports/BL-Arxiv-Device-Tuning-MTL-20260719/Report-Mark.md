# Report-Mark: Device Tuning MTL

## Source Metadata

- Title: *Device Tuning for Multi-Task Large Model*.
- Authors: Penghao Jiang, Xuanchen Hou, and Yinsi Zhou.
- Affiliations printed in the paper: The Australian National University and Deakin University.
- arXiv ID: `2302.10820v1`.
- arXiv-issued DOI: `10.48550/arXiv.2302.10820`.
- Submitted: 2023-02-21.
- Subject: Computer Vision and Pattern Recognition (`cs.CV`).
- Venue evidence: Listed among accepted papers for the Deployable AI workshop at AAAI 2023.
- License: Creative Commons Attribution 4.0 on the arXiv record.
- Primary records: https://arxiv.org/abs/2302.10820, https://arxiv.org/pdf/2302.10820, https://ar5iv.labs.arxiv.org/html/2302.10820, https://arxiv.org/e-print/2302.10820, and https://doi.org/10.48550/arXiv.2302.10820.
- Source-locality policy: Complete source files, cache outputs, and integrity records were retained locally and withheld; temporary renderings were removed after inspection, and no `.source/` directory was created.

### Selection Record

- `rg --files -g "*.pdf"` found 75,778 PDFs representing 75,776 unique PDF-parent paper units.
- PowerShell `Get-Random` uniformly selected zero-based index 74,319.
- First draw accepted; exclusions 0; reselections 0.
- No arXiv ID, DOI, normalized-title, slug, public artifact, memory, companion-repository, or active-worktree same-paper match was found.
- Initial source state `partial` was repaired to verified `complete` before review.
- Cache state moved from miss to `cached` with PDF, HTML, and TeX/source text.

## Concise Research Notes

### Problem

The paper targets a real systems tension: vision transformers can be expensive for resource-constrained devices, while a cloud-only model incurs transmission and central-compute costs. It proposes a shared device/cloud architecture intended to reduce the representation sent upstream and to support many tasks without deploying a separate large model for each task.

### Method

A device encoder pools a hidden sequence from shape `T x D` to `T' x D`, with `T' < T`; the paper later says the sequence is halved. Self-attention and feed-forward processing continue on the pooled representation, and the result is passed to a cloud decoder. The introduction also says cloud parameters are shared, device parameters are task-specific, and gradient normalization dynamically balances task losses. Those multi-task and balancing elements are not defined in the method section, equations, or experiments.

### Evidence

The empirical section contains only two ImageNet-1k top-1/parameter tables. It supplies no training recipe, multi-task task list, task-specific heads, gradient-balancing result, dataset split, optimizer, schedule, pretraining source, repeated seeds, FLOPs, latency, memory, energy, bandwidth, serialized payload, or ablation. The architecture figure clarifies a device encoder/cloud decoder split, but it does not specify transport encoding, deployment boundary, or failure behavior.

### Results

- Table 1: the proposed 2.2M-parameter model reports 70.6% top-1, versus the best listed same-scale baseline, MobileNetV2, at 69.8% and 2.6M parameters. This is a 0.8 percentage-point gain with about 15.4% fewer parameters.
- Table 2: the proposed 15.6M-parameter model reports 78.0%, compared with DenseNet-169 at 76.2%/14M, EfficientNet-B0 at 76.3%/5.3M, ResNet-101 at 77.4%/44.5M, and ResNet-101-SE at 77.6%/49.3M.
- Table 2 is not a clean matched-budget frontier: the proposed model ranges from about 11% larger than DenseNet-169 to almost three times EfficientNet-B0's parameters, while being far smaller than the two ResNet variants.

### Limitations and Reviewer Interpretation

The table values support a compact ImageNet classifier point, not the broader claims of multi-task generalization, reduced communication, or device/cloud efficiency. Sequence shortening plausibly reduces attention arithmetic and message size, but the paper never reports the original/pooled token counts by stage, data type, serialization, network, hardware, or end-to-end measurement. The later CVPR Workshops paper by overlapping authors is a useful successor context, but its NLP results cannot be transferred backward as evidence for this vision paper.

## Evidence and Attribution

| ID | Evidence | Inspected material | Supports | Boundary |
|---|---|---|---|---|
| E1 | Verified arXiv v1 PDF, full-paper HTML, and TeX/source | Entire four-page paper, equations, figures, tables, references | Method and printed results | Author report; no reproduction |
| E2 | arXiv abstract/metadata and DOI | Identity, authors, date, subject, license, venue note | Provenance | Abstract not used for empirical claims |
| E3 | Visual PDF renderings | All four pages, Figures 1-2, Tables 1-2 | Layout and table verification | Nonfatal font substitution; content legible |
| E4 | Official DAI 2023 accepted-paper page | Title and authors | Workshop appearance | Does not add methods/results |
| E5 | Focused implementation search | Paper, metadata, workshop page, GitHub ID/title queries | No author-linked code located | Absence is time-bounded, not proof none exists |
| E6 | CVF open-access successor paper | Title, authors, venue, abstract | Related successor context | Different paper/task/evidence object |
| E7 | Three Black Lake DEP entries | Edge/cloud split, token merging, conditional vision compute | Concept bridges | Associations do not transfer claims |
| E8 | Public cache summary | Extractor names, statuses, output byte counts | Processing provenance | Extracted text remained local |

## Related DEP Entries

1. [Efficient and Privacy Aware Edge Cloud Collaborative Inference](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260719-Edge%20Cloud%20Split/2607.13093-whitepaper-review.md) - shares the endpoint/cloud partition and compressed-message boundary, but adds explicit latency, bandwidth, device-profile, and privacy measurements that expose what the selected paper leaves unmeasured.
2. [K-Token Merging](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-K%20Token%20Merging/2604.15153-whitepaper-review.md) - directly parallels pre-attention sequence compression by merging token embeddings and treats compression as a quality/resource frontier rather than assuming fewer tokens equal deployment speed.
3. [Dynamic Multi-path Neural Network](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-DMNN%20Conditional%20Paths/dmnn_conditional_paths_manuscript.md) - offers a compact-vision comparison where reported FLOP savings are explicitly separated from latency, memory, energy, and compiler realization.

## Synthesis Note

### Concept Bridge

Device Tuning sits at the intersection of three control decisions: where a model is split, how much intermediate state crosses the split, and which parameters remain shared versus task-specific. Edge Cloud Split makes the split measurable; K-Token Merging makes representation reduction a quality frontier; DMNN makes compute activation conditional and warns that arithmetic counts are not runtime evidence. Together they turn the selected paper's architectural sketch into a testable systems program: define the information boundary, measure achieved compression, preserve task outcomes, and account for every device, transport, and cloud cost.

### Potential Implementations

1. **Split-inference evidence harness**: Run a small transformer at multiple device/cloud boundaries and record pooled tensor shape, serialized bytes, device latency, transport latency, cloud latency, peak memory, energy, and fixed-denominator quality.
2. **Protected token-pooling layer**: Pool adjacent visual tokens while retaining immutable provenance for protected regions, then compare average, learned, and no-pooling controls across ratios and failure slices.
3. **Multi-task adapter laboratory**: Share a cloud backbone, attach task-specific device modules, implement an explicit GradNorm-style or fixed-weight control, and publish per-task interference, aggregate quality, and resource costs.

### Deeper Relationship Observations

1. **The split is an information contract**: A device/cloud architecture is not defined by a diagram alone; it needs tensor identity, dimensions, precision, serialization, encryption, retry, privacy, and fallback semantics.
2. **Compression has three ledgers**: Reduced tokens/bytes are representation gain, lower latency/energy is execution gain, and preserved task accuracy is outcome gain. The selected paper measures only a narrow outcome/parameter slice.
3. **Multi-task claims require interference evidence**: Shared parameters can save copies while still causing negative transfer, gradient domination, or task-specific regressions; aggregate ImageNet accuracy cannot reveal those behaviors.

### Conceptual Similarities

1. **Selective state reduction**: Device Tuning pools hidden tokens, K-Token Merging compresses embeddings, and DMNN activates only selected paths to reduce the state or computation exposed downstream.
2. **Shared core plus local specialization**: The selected paper's cloud/shared and device/task-specific parameter language mirrors broader modular systems that separate common capacity from endpoint-specific control.
3. **Frontier rather than scalar ranking**: All four records are properly judged on quality versus parameters, compute, bytes, latency, memory, energy, and failure coverage rather than one favorable headline metric.

### MVP Implementations with Code Mock-Ups

1. **Compression manifest** - records achieved rather than requested sequence reduction.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class CompressionRecord:
    input_tokens: int
    output_tokens: int
    hidden_width: int

    @property
    def reduction(self) -> float:
        if self.input_tokens <= 0:
            raise ValueError("input_tokens must be positive")
        if not 0 < self.output_tokens <= self.input_tokens:
            raise ValueError("invalid output token count")
        return 1.0 - (self.output_tokens / self.input_tokens)
```

2. **End-to-end split trace** - prevents device/cloud cost from collapsing into parameter count.

```python
def split_trace(device_ms, uplink_ms, cloud_ms, downlink_ms,
                payload_bytes, top1, quality_floor):
    parts = [device_ms, uplink_ms, cloud_ms, downlink_ms]
    if any(value < 0 for value in parts) or payload_bytes < 0:
        raise ValueError("costs must be non-negative")
    return {
        "end_to_end_ms": sum(parts),
        "payload_bytes": payload_bytes,
        "top1": top1,
        "quality_pass": top1 >= quality_floor,
    }
```

3. **Fixed-denominator outcome card** - retains timeouts and errors as outcomes.

```python
def outcome_card(outcomes):
    allowed = {"correct", "wrong", "timeout", "error"}
    if not outcomes or any(item not in allowed for item in outcomes):
        raise ValueError("invalid fixed-denominator outcome list")
    total = len(outcomes)
    return {
        label: sum(item == label for item in outcomes) / total
        for label in sorted(allowed)
    }
```

### Developer Challenges

1. **Boundary instrumentation**: The runtime must attribute pooling, device compute, serialization, transfer, cloud compute, retries, and fallback separately without perturbing the result beyond a declared bound.
2. **Comparable training**: Reconstructed baselines need one data, augmentation, resolution, optimizer, schedule, epoch, precision, seed, and hardware manifest rather than heterogeneous published numbers.
3. **Task isolation and governance**: Shared/cloud and task-specific/device parameters require versioned ownership, per-task gradient telemetry, negative-transfer alerts, privacy controls, and reversible rollout.

### Author Challenges

1. **Specify the complete method**: Define pooling type and position, compression ratio, split tensor, shared/task-specific parameters, task heads, loss, gradient-normalization algorithm, and device/cloud protocol.
2. **Release reproducibility artifacts**: Publish code, configs, checkpoints, data/split locators, training logs, seeds, expected outputs, and an environment lock matched to arXiv v1.
3. **Test the claims directly**: Add multiple tasks, per-task and aggregate metrics, matched-budget baselines, pooling/split/gradient ablations, and measured latency, memory, energy, bytes, privacy, and tail failures across device/network profiles.

## Validation Notes

- The source-integrity gate passed before synthesis: valid PDF plus verified full-paper HTML with the required body, document, heading, and structure markers.
- The extraction cache public summary passed its public-safety scan with zero findings.
- The manuscript title contract, required headings, exact-three contracts, JSON validity, publication index, public-safe paths, and code mock-up syntax are validated before submission.
- The staged source-upload gate must show only generated Markdown/README/index and dedup JSON paths; no PDF, HTML, source archive, cache, extracted text, local path, or `.source/` artifact is allowed.
- No empirical result, code, model, or benchmark was independently reproduced.

## Attribution Block

- Source URL: https://arxiv.org/abs/2302.10820
  - Applies to: identity, authors, date, subject, license, DOI, abstract, and venue note.
  - Notes: Metadata/abstract source; not treated as full-paper evidence.
- Source URL: https://arxiv.org/pdf/2302.10820
  - Applies to: method, figures, equations, tables, conclusion, and references.
  - Notes: Complete PDF was inspected locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2302.10820
  - Applies to: full-paper structure and text cross-check.
  - Notes: Approved full-paper fallback used after official arXiv HTML was unavailable; local copy withheld.
- Source URL: https://arxiv.org/e-print/2302.10820
  - Applies to: exact equations, tables, and method wording.
  - Notes: TeX/source archive remained local and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2302.10820
  - Applies to: persistent arXiv identity.
  - Notes: arXiv-issued DataCite DOI.
- Source URL: https://sites.google.com/view/dai-2023/accepted-papers
  - Applies to: DAI 2023 accepted-paper status.
  - Notes: Official workshop list.
- Source URL: https://openaccess.thecvf.com/content/CVPR2023W/MobileAI/html/Jiang_High-Efficiency_Device-Cloud_Collaborative_Transformer_Model_CVPRW_2023_paper.html
  - Applies to: successor-publication context.
  - Notes: Different paper; no claims transferred to the selected work.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260719-Edge%20Cloud%20Split/2607.13093-whitepaper-review.md
  - Applies to: related edge/cloud measurement bridge.
  - Notes: Repository evidence only; claims remain scoped to its own sources.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-K%20Token%20Merging/2604.15153-whitepaper-review.md
  - Applies to: related sequence-compression bridge.
  - Notes: Repository evidence only; claims remain scoped to its own sources.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-DMNN%20Conditional%20Paths/dmnn_conditional_paths_manuscript.md
  - Applies to: related conditional-compute bridge.
  - Notes: Repository evidence only; claims remain scoped to its own sources.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: public filing, attribution, and source-locality policy.
  - Notes: Live repository authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E container and publication-index rules.
  - Notes: Live filing authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion-repository dedup scope.
  - Notes: Live related-repository authority.
