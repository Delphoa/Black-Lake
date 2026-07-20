# DEP-E-20260720-Decentralized SSL

#federated-learning #self-supervised-learning #contrastive-learning #non-iid #privacy #representation-learning #research-review

Public-safe context: job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P07`, uniformly selected `arXiv:2111.10763v2`. Official HTML was unavailable; the valid PDF plus one approved ar5iv fallback passed the complete-source gate. Local paths, exact execution times, and source documents are withheld.

## Contents

- `README.md` - deposit context, inventory, source/privacy boundary, synthesis, and attribution.
- `decentralized_ssl_manuscript.md` - schema-complete review of CCL, feature fusion, neighborhood matching, evidence, privacy gaps, implementation paths, and related DEP synthesis.

No `.source/` exists. No image, feature tensor, model, dataset, PDF, HTML, code, cache, or extracted source text is deposited.

## Summary of Items

CCL exchanges models and derived features between clients, uses feature fusion to enlarge contrastive queues, and uses neighborhood matching to align representations across clients. It reports 88.90% CIFAR-10 IID linear accuracy, 10.92 points above FedCA and 5.28 above FedSwAV, plus 4.86-6.40-point gains over the best CIFAR-100 baselines across three partitions.

The manuscript rejects the shortcut that local raw data equals privacy. Feature queues and models cross boundaries, while the paper provides no current leakage audit, formal privacy guarantee, secure aggregation proof, or systems-cost accounting.

## Insights and Relevance

The reusable artifact is a joint utility/privacy/cost harness. XPRINT illustrates leakage from derived signals, Device Tuning treats the split as an information contract, and VLM Probing offers methods to test what representations encode.

## Attribution Block

- https://arxiv.org/abs/2111.10763 - metadata, version history, DOI, and locators.
- https://ar5iv.labs.arxiv.org/html/2111.10763 - verified full-paper fallback; local copy withheld.
- https://arxiv.org/pdf/2111.10763 - verified PDF; local copy withheld.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-XPRINT%20Traffic%20Privacy - related privacy DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-Device%20Tuning%20MTL - related device/cloud DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing - related representation DEP.
- Source files: verified PDF, fallback HTML, metadata HTML, and integrity records; all withheld locally with zero source-document uploads.
