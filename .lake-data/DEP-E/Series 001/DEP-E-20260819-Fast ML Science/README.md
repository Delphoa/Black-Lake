# DEP-E-20260819-Fast ML Science

#fast-ml #scientific-computing #real-time-inference #hardware-co-design #edge-ai #research-review

Public-safe context: source-first review of *Applications and Techniques for Fast Machine Learning in Science* (arXiv:2110.13041; Frontiers in Big Data 5:787421). The complete PDF and full-paper HTML were verified locally after one bounded archive repair. Source documents, metadata HTML, private provenance, caches, and verification records remain local and were not uploaded.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, insights, and attribution.
- `fast_ml_science_manuscript.md`
  - Schema-complete manuscript review of the paper's applications, data representations, system constraints, deployment techniques, evidence boundaries, related research, and bounded MVP paths.

No `.source/` directory exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

### `README.md`

Defines the DEP-E research boundary and records that the original paper sources were inspected privately and withheld from the public repository.

### `fast_ml_science_manuscript.md`

Preserves a source-grounded review of fast ML for science. It covers the paper's cross-domain application taxonomy, data representations, event-rate and latency constraints, reduction/analysis/control modes, model-efficiency techniques, hardware/software co-design, evidence limits, exactly three exercise paths, and a bounded MVP product concept.

## Insights and Relevance

The paper's durable value is a shared design language for connecting scientific data representation to end-to-end latency, throughput, energy, memory, software/hardware choice, and downstream experimental risk. The related Black Lake entries show how that language becomes concrete: SpOctA turns sparse spatial structure into accelerator scheduling, ELiTeFormer turns low precision into FPGA resource choices, and Local AI Stack extends the boundary to runtimes, accelerators, edge power, memory, and governance. The deposit is therefore useful as a review and design ledger, not as proof that any single fast-ML deployment is reproducible or safe.

## Attribution Block

- Source URL: https://arxiv.org/abs/2110.13041
  - Applies to: `fast_ml_science_manuscript.md` and this README.
  - Notes: canonical paper identity, metadata, abstract, version, and public source locators.
- Source URL: https://arxiv.org/html/2110.13041
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: full-paper HTML inspected after bounded local repair; the local copy was withheld.
- Source URL: https://arxiv.org/pdf/2110.13041
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: complete PDF inspected and visually cross-checked; the local copy was withheld.
- Source URL: https://doi.org/10.3389/fdata.2022.787421
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: published Frontiers in Big Data record.
- Source URL: https://github.com/fastmachinelearning/fastml-science
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: official companion benchmark context; not a source file deposit.
- Source URL: https://github.com/fastmachinelearning/hls4ml
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: official low-latency FPGA inference ecosystem context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-SpOctA%20Accelerator/spocta_accelerator_manuscript.md
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: related DEP for sparse representation and accelerator co-design.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20002/DEP-A-20260809-ELiTeFormer%20FPGA/2607.03652-whitepaper-review.md
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: related DEP for low-precision FPGA deployment and resource accounting.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-Local%20AI%20Stack/local-ai-research.md
  - Applies to: `fast_ml_science_manuscript.md`.
  - Notes: related DEP for runtime, accelerator, quantization, edge-power, and governance constraints.
- Source boundary: all original source documents, private provenance, and verification records remained local and were not uploaded.
