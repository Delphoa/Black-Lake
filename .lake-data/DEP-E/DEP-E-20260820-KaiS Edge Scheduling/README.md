# DEP-E-20260820-KaiS Edge Scheduling

#edge-computing #kubernetes #multi-agent-reinforcement-learning #graph-neural-networks #scheduling #ml-systems

Deposition date: 2026-08-20

DEP class: DEP-E

Subject title: Tailored Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud System

Public-safe context: this DEP-E contains a source-grounded review of `arXiv:2101.06582v1`. Original paper files, metadata, receipts, caches, and local verification material were withheld under the repository's arXiv-source policy.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, relationship notes, and complete attribution.
- `kais_edge_scheduling_manuscript.md`
  - Schema-complete manuscript covering the KaiS mechanism, evidence ledger, experimental results, limitations, implementation paths, and a bounded MVP.

## Summary of Items

The manuscript reconstructs KaiS as a two-time-scale control system: decentralized coordinated actor-critic agents dispatch requests every short slot, while a centralized GNN-based policy performs lower-frequency service orchestration. It preserves the reported Google Cloud/k3s setup, modified Alibaba workload traces, baseline comparisons, throughput and scheduling-cost results, and the gap between the paper's prototype and the adjusted public simulator.

The review also records the random-selection and dedup process, the initially partial source state, the bounded repair, and the complete-source verification gate. Quantitative results remain explicitly author-reported because no training or systems experiment was rerun.

## Insights and Relevance

KaiS is valuable less as a ready-to-deploy scheduler than as an early decomposition of edge-cloud control by decision locality and cadence. The related Black Lake entries show the same boundary from three sides: device/cloud partitioning must account for transfer cost, edge/cloud inference must make latency and information exposure explicit, and centralized-training/decentralized-execution MARL needs strong constraint and rollback gates. A modern implementation should retain KaiS's local dispatch/global orchestration split while adding Kubernetes-native policy enforcement, trace-complete evaluation, uncertainty reporting, and shadow-mode fallback.

## Attribution Block

- Source URL: https://arxiv.org/abs/2101.06582
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Canonical title, authors, arXiv ID, submission date, subjects, abstract, public artifact links, and license locator.
- Source URL: https://arxiv.org/html/2101.06582
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Official full-paper HTML used for searchable method, implementation, experiment, results, and reference evidence.
- Source URL: https://arxiv.org/pdf/2101.06582
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Canonical ten-page paper used for complete-paper and layout verification.
- Source URL: https://doi.org/10.48550/arXiv.2101.06582
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Persistent arXiv identity.
- Source URL: https://doi.org/10.1109/INFOCOM42981.2021.9488701
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Published IEEE INFOCOM 2021 identity.
- Source URL: https://github.com/XiaofeiTJU/KaiS
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Paper-linked Apache-2.0 simulator repository inspected at commit `35d3514ba4b59d68e64772aeba870327a54ccead`.
- Source URL: https://github.com/alibaba/clusterdata
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Workload-trace program cited by the paper and the KaiS simulator README.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md` and `kais_edge_scheduling_manuscript.md`.
  - Notes: Live repository authority for public-safe source handling, DEP contents, naming, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md` and the DEP-E publication-index update.
  - Notes: Live class-container and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Companion repository authority used for cross-repository deduplication.
- Source file: `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md`
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Device/cloud representation split, transfer-cost measurement, and deployment-boundary bridge.
- Source file: `.lake-data/DEP-A/DEP-A-20260719-Edge Cloud Split/2607.13093-whitepaper-review.md`
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Edge/cloud partitioning, latency, bandwidth, and privacy relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md`
  - Applies to: `kais_edge_scheduling_manuscript.md`.
  - Notes: Centralized-training/decentralized-execution MARL, constraint handling, and simulation-evidence relationship.
- Source-handling note: original PDF, full-paper HTML, metadata HTML, acquisition receipt, provenance, verification records, extracted source text, and other private archive material were withheld locally and were not uploaded.
