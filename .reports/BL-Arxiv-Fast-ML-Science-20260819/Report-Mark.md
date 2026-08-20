# Report-Mark: Fast ML Science

## Source Metadata

| Field | Value |
|---|---|
| Title | *Applications and Techniques for Fast Machine Learning in Science* |
| Authors | Allison McCarn Deiana and Nhan Tran, coordinators, with 86 additional authors |
| arXiv | [2110.13041](https://arxiv.org/abs/2110.13041), v1 submitted 2021-10-25 |
| arXiv DOI | [10.48550/arXiv.2110.13041](https://doi.org/10.48550/arXiv.2110.13041) |
| Journal record | *Frontiers in Big Data* 5, Article 787421, published 2022-04-12 |
| Journal DOI | [10.3389/fdata.2022.787421](https://doi.org/10.3389/fdata.2022.787421) |
| Source formats inspected | Complete local PDF, complete local full-paper HTML, metadata HTML, public arXiv record, Frontiers/PMC record, official FastML repositories, and three related Black Lake manuscripts |
| Source status | Complete source pair verified locally; source documents withheld from public output |
| Review boundary | Date-only 2026-08-19 artifact; exact local execution time withheld |

## Concise Research Notes

The paper is a community review that defines fast machine learning in science as integrating ML into experimental data-processing infrastructure, from near-sensor feature extraction through distributed compute. It organizes the space around three connected questions: which scientific applications need fast ML, which data representations and system constraints recur across domains, and which model, software, and hardware techniques can satisfy those constraints.

The source's cross-domain taxonomy distinguishes real-time data reduction, real-time analysis, and closed-loop control. Its constraint table pairs application domains with event rates, latency, programmable versus custom systems, and energy sensitivity. The technology survey then covers efficient architectures, neural-network/hardware co-design, quantization, pruning and sparse inference, knowledge distillation, FPGA workflows, conventional CMOS hardware, and beyond-CMOS concepts.

The strongest reviewer interpretation is that the paper's durable contribution is a design vocabulary and a systems boundary, not a single accuracy or latency result. A fast-ML claim should identify the representation, the complete data path, the measured resource, the denominator, and whether the output only filters data, informs analysis, or changes an experiment.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Complete local PDF and full-paper HTML for arXiv:2110.13041 | Introduction, domain examples, data representations, Tables 2-3, technology survey, outlook | High for source reporting | Author/community review; no independent reproduction |
| E2 | [arXiv record](https://arxiv.org/abs/2110.13041) | Title, authorship, date, version, subjects, 66-page/13-figure/5-table metadata, arXiv and journal identifiers | High | Metadata is not sufficient for method/results claims |
| E3 | [Frontiers article](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2022.787421/full) and [PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC9041419/) | Published version, review scope, article outline, abstract, and publisher context | High for publication context | No new independent benchmark evidence |
| E4 | [fastml-science benchmark repository](https://github.com/fastmachinelearning/fastml-science) | Official community benchmark context with float and quantized jet-classification baselines | Medium | Companion implementation, not code for this review paper |
| E5 | [hls4ml repository](https://github.com/fastmachinelearning/hls4ml) and [FastML Foundation](https://fastmachinelearning.org/) | Public community implementation ecosystem for low-latency FPGA inference and scientific deployment | Medium | Ecosystem context; not proof of the paper's claims |
| E6 | [SpOctA manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-SpOctA%20Accelerator/spocta_accelerator_manuscript.md) | Sparse representation, map search, memory skew, and accelerator co-design | Medium | Related derived artifact, not primary evidence for this paper |
| E7 | [ELiTeFormer review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20002/DEP-A-20260809-ELiTeFormer%20FPGA/2607.03652-whitepaper-review.md) | Low-precision model/hardware co-design, FPGA resource accounting, and reproduction boundaries | Medium | Related derived artifact, not primary evidence for this paper |
| E8 | [Local AI Stack manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md) | Runtime, accelerator, quantization, edge-power, and deployment-stack constraints | Medium | Broad cross-source synthesis, not a fast-ML benchmark |
| E9 | [Black Lake README](https://github.com/Delphoa/Black-Lake/blob/main/README.md) and [DEP rules](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md) | Public filing, source locality, DEP class, index, and attribution requirements | High | Repository policy only |
| E10 | [Black-Lake-Data README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md) | Related-repository provenance and source-deposition boundary | High | Repository policy only |

## Related DEP Entries

1. **SpOctA Accelerator** - `.lake-data/DEP-E/DEP-E-20260718-SpOctA Accelerator/spocta_accelerator_manuscript.md`. Its octree encoding, bank-safe map search, sparsity-aware processing, and skew-aware caching are a concrete instance of the paper's representation-to-hardware co-design principle. The source basis is the inspected Black Lake manuscript.
2. **ELiTeFormer FPGA** - `.lake-data/DEP-A/DEP-A-20260809-ELiTeFormer FPGA/2607.03652-whitepaper-review.md`. Its hybrid efficient attention, ternary projections, FPGA implementation, resource metrics, and missing-reproduction evidence make the paper's quantization/co-design vocabulary operational. The source basis is the inspected Black Lake review.
3. **Local AI Stack** - `.lake-data/DEP-E/DEP-E-20260709-Local AI Stack/local-ai-research.md`. Its runtime, accelerator, quantization, edge-power, memory, and governance framing extends fast-ML concerns from model/hardware design to deployable serving stacks. The source basis is the inspected Black Lake manuscript.

## Synthesis Note

### Concept Bridge

Fast ML for science is best treated as a constrained data-path design problem. The primary paper supplies the vocabulary: representation, event rate, latency, energy, software/custom hardware, and task mode. SpOctA shows how an irregular spatial representation can become a bank schedule; ELiTeFormer shows how low-precision model structure can become an FPGA resource choice; Local AI Stack shows that deployment readiness also depends on runtimes, memory policy, accelerators, power, and governance. Together, they bridge from a review taxonomy to an auditable implementation ledger.

### Potential Implementations

1. **Scientific data-path requirements registry**: Capture representation type, event rate, latency budget, energy boundary, task mode, hardware class, and quality target before selecting a model or accelerator. Output a versioned requirements record and a list of unresolved denominators. Evaluate by checking whether a second reviewer can reconstruct the deployment boundary from the record alone.
2. **Matched fast-ML benchmark harness**: Run float, quantized, pruned, and distilled variants against the same public or synthetic traces. Record preprocessing, transfer, inference, fallback, task quality, throughput, latency percentiles, memory, and energy separately. Evaluate with a complete cost-quality frontier rather than a single best point.
3. **Shadow-mode instrument gateway**: Place an inference path beside an existing reduction or analysis path, with explicit reduction, analysis, control, and abstain modes. Keep the conservative path active during validation and require a human or domain rule to authorize any closed-loop action. Evaluate drift, tail failures, and end-to-end goodput before enabling control.

### Deeper Relationship Observations

1. **Representation is a scheduling contract**: In the primary paper, data representation determines suitable model and platform choices. SpOctA makes this concrete by turning octree digits into parallel table banks, so representation and hardware scheduling are not separable concerns.
2. **Compression is only useful when the consumer can exploit it**: Quantization, pruning, sparsity, and distillation reduce a model's nominal cost, but the reduction becomes a system gain only when kernels, memory movement, compiler paths, and the target device preserve it. ELiTeFormer and Local AI Stack expose this implementation boundary.
3. **Control mode changes the evidence threshold**: A reduction filter can be assessed by retained information and false drops; a closed-loop controller must additionally prove bounded failure behavior, fallback correctness, and safe response timing. Table 3's task distinction therefore implies different validation contracts, not just different labels.

### Conceptual Similarities

1. **Cross-layer co-design**: All four records connect algorithm structure to representation, memory, compute, and deployment conditions.
2. **Resource-aware evaluation**: Each record treats latency, throughput, memory, energy, or power as part of the claim rather than an afterthought.
3. **Evidence-boundary discipline**: The records distinguish source-reported results from independently reproduced measurements and keep implementation context from becoming proof of generality.

### MVP Implementations

1. **Requirements-to-platform classifier** - a local, deterministic mapping over synthetic requirements.

```python
def choose_platform(requirements):
    """Return a review suggestion, not an automatic deployment decision."""
    if requirements["task_mode"] == "closed_loop" and requirements["latency_ms"] <= 1:
        return {"candidate": "custom_or_fpga", "review": "domain safety and fallback required"}
    if requirements["energy_constrained"] or requirements["latency_ms"] <= 10:
        return {"candidate": "edge_accelerator", "review": "measure data movement and power"}
    return {"candidate": "software_programmable", "review": "benchmark end_to_end latency"}
```

2. **Matched cost ledger** - a bounded comparison record that prevents headline throughput from hiding transfer or preprocessing cost.

```python
def total_cost(sample):
    """Compute a transparent per-sample cost from synthetic or authorized traces."""
    return {
        "latency_ms": sum(sample[k] for k in ("preprocess_ms", "transfer_ms", "inference_ms", "fallback_ms")),
        "energy_mj": sample["preprocess_mj"] + sample["transfer_mj"] + sample["inference_mj"],
        "quality": sample["task_quality"],
    }
```

3. **Safe stream decision record** - a schema-first boundary for reduction, analysis, control, and abstention.

```python
def decide(stream_item, budget_ms):
    """Never actuate; return a reviewable decision for a shadow-mode test."""
    if stream_item["latency_ms"] > budget_ms or stream_item["confidence"] < 0.8:
        return {"mode": "abstain", "fallback": "conservative_path", "reason": "budget_or_confidence"}
    return {"mode": "analysis", "fallback": "conservative_path", "reason": "within_shadow_budget"}
```

### Developer Challenges

1. Define one end-to-end measurement boundary that includes sensor ingress, representation, preprocessing, transfer, inference, postprocessing, and fallback.
2. Preserve equivalent task quality while changing precision, sparsity, architecture, compiler, or hardware so that resource gains are attributable.
3. Build versioned observability for device, runtime, model, data schema, calibration, and failure state without leaking sensitive scientific data.

### Author Challenges

1. Keep the review taxonomy current as hardware, compilers, runtimes, and scientific use cases change faster than a static article can track.
2. Provide more matched, reproducible cross-domain evidence without collapsing incompatible scientific objectives into a single score.
3. Make the transition from illustrative examples to deployable, independently verifiable workflows explicit, especially for closed-loop control.

## Validation Notes

- Source gate: complete PDF and full-paper HTML verified; metadata HTML present; no partial files; source package unavailable but not required after the complete-source gate passed.
- Evidence gate: method and system claims were based on the full paper/PDF and publisher record; the abstract was used for identity and scope only.
- Visual cross-check: PDF pages containing the data-path taxonomy, Tables 2-3, technology overview, and outlook were rendered and inspected; layout was readable and table labels aligned.
- Related-entry gate: exactly three concrete conceptual overlaps were selected and tied to repository-relative paths and public GitHub URLs.
- Public-output gate: this report contains only derived Markdown, public URLs, repository-relative related paths, and public-safe source-boundary statements. No PDF, HTML, source archive, cache, extracted text, local absolute path, username, machine name, local timezone label, or exact execution timestamp is present.

## Attribution Block

- Source URL: https://arxiv.org/abs/2110.13041
  - Applies to: source identity, abstract, version, subjects, and public paper locator.
- Source URL: https://arxiv.org/html/2110.13041
  - Applies to: full-paper method, tables, figures, technology survey, and outlook.
- Source URL: https://arxiv.org/pdf/2110.13041
  - Applies to: PDF visual and text cross-check.
- Source URL: https://doi.org/10.3389/fdata.2022.787421
  - Applies to: published venue and article record.
- Source URL: https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2022.787421/full
  - Applies to: publisher abstract, outline, and published context.
- Source URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9041419/
  - Applies to: open full-text publication record and review framing.
- Source URL: https://github.com/fastmachinelearning/fastml-science
  - Applies to: official companion benchmark context.
- Source URL: https://github.com/fastmachinelearning/hls4ml
  - Applies to: official low-latency FPGA inference ecosystem context.
- Source URL: https://fastmachinelearning.org/
  - Applies to: current FastML community and project context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-SpOctA%20Accelerator/spocta_accelerator_manuscript.md
  - Applies to: related DEP 1.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20002/DEP-A-20260809-ELiTeFormer%20FPGA/2607.03652-whitepaper-review.md
  - Applies to: related DEP 2.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md
  - Applies to: related DEP 3.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: filing, source-locality, and public attribution rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E path and publication-index rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related raw-repository provenance and source-deposition rules.
- Source boundary: complete local source documents and private validation records were inspected but withheld; no source files were uploaded.
