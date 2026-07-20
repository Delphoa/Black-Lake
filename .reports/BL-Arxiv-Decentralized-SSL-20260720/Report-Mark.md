# Report-Mark: Decentralized SSL

- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P07`
- Review date: 2026-07-20

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Decentralized Unsupervised Learning of Visual Representations* |
| Authors | Yawen Wu; Zhepeng Wang; Dewen Zeng; Meng Li; Yiyu Shi; Jingtong Hu |
| Identifier | arXiv:2111.10763v2; DOI:10.48550/arXiv.2111.10763 |
| Submitted / revised | 2021-11-21 / 2022-04-22 |
| Record | https://arxiv.org/abs/2111.10763 |
| Full-paper fallback | https://ar5iv.labs.arxiv.org/html/2111.10763 |
| PDF | https://arxiv.org/pdf/2111.10763 |
| Source state | Verified complete after approved fallback; all source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260720-8636EDC7`; `BLAD-2200-20260720-8636EDC7-P07` |

## Concise Research Notes

The paper proposes collaborative contrastive learning (CCL) for unlabeled visual data held by distributed clients. Each round exchanges models and features. Feature fusion expands local negative queues with remote features; neighborhood matching pulls local representations toward nearby local/remote features, addressing class fragmentation under non-IID partitions. Raw images remain local, but derived features and models are shared.

On CIFAR-10 IID linear evaluation, the full approach reports 88.90% top-1, 0.38 points below centralized MoCo, 10.92 above FedCA, and 5.28 above FedSwAV. On CIFAR-100 it exceeds the best baseline by 6.40, 6.09, and 4.86 points across IID and two non-IID settings. Experiments also cover Fashion-MNIST, 1%/10% semi-supervision, collaborative finetuning, and ablations.

Privacy is not proven merely because raw images stay local. The protocol uploads feature queues and model states, relies on InstaHide-style transformed images for feature generation, and supplies no modern membership/inversion/property-inference audit, differential-privacy guarantee, secure aggregation proof, or communication/energy accounting. The reported datasets are small benchmarks and do not represent real client populations.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Sections 3-5 | Round protocol, model/feature exchange, fusion, neighborhood matching | No execution or security proof |
| Section 6 | CIFAR-10/100 and Fashion-MNIST results | Author-run, small benchmarks, synthetic partitions |
| CIFAR-10 linear evaluation | 88.90%, +10.92 vs FedCA, +5.28 vs FedSwAV | One primary setting |
| Privacy discussion | Raw data local; transformed-feature sharing | No empirical leakage audit or formal guarantee |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md` - derived signals can leak sensitive behavior despite protected primary content.
2. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - device/cloud information contracts require bandwidth, privacy, and runtime evidence.
3. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - representation probes can test what shared features encode.

## Synthesis Note

### Concept Bridge

CCL treats feature exchange as a collaboration primitive. XPRINT warns that protected payloads can still leak through derived signals, Device Tuning frames the boundary as a measurable information contract, and VLM Probing supplies tests for encoded attributes.

### Potential Implementations

1. Build an offline simulator that sweeps client skew, participation, and label budgets with fixed seeds.
2. Add membership, inversion, and property-inference audits to every shared-feature configuration.
3. Record communication bytes, compute, energy, privacy budget, and accuracy in one signed ledger.

### Deeper Relationship Observations

1. Feature sharing can improve representation diversity while enlarging the privacy attack surface.
2. Non-IID accuracy and privacy risk may vary by client, making averages insufficient.
3. Representation probes are useful both for task utility and unintended sensitive-attribute leakage.

### Conceptual Similarities

1. All four artifacts analyze information crossing system boundaries.
2. Each requires measurement of what the transmitted representation retains.
3. Each benefits from worst-case slices rather than aggregate utility alone.

### MVP Implementations with Code Mock-Ups

1. Split auditor: `for skew in skews: score(run(seed, skew, clients))`.
2. Leakage gate: `assert max(audit_attacks(features)) <= policy.leakage_ceiling`.
3. Cost receipt: `sign({accuracy, bytes_sent, joules, dp_epsilon, attack_auc})`.

### Developer Challenges

1. Reproducing client partitions, queues, synchronization, and negative sampling exactly.
2. Auditing high-dimensional features without collecting sensitive client data centrally.
3. Scaling communication and nearest-neighbor matching under client churn.

### Author Challenges

1. Demonstrating security against current feature/model leakage attacks.
2. Moving from synthetic image benchmarks to realistic clients and shifts.
3. Reporting communication, compute, energy, fairness, and privacy together.

## Validation Notes

- First uniform draw at index 60,174 of 75,776; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with verified PDF and approved ar5iv full-paper HTML after official HTML 404.
- Claims are tied to full-paper sections; privacy interpretation is explicitly marked.
- Exactly three related entries and three items in each required synthesis subsection.
- Public allowlist is Markdown/JSON only; zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2111.10763 - canonical metadata, authors, version history, DOI, and public locators.
- https://ar5iv.labs.arxiv.org/html/2111.10763 - verified full-paper fallback; local copy withheld.
- https://arxiv.org/pdf/2111.10763 - verified PDF; local copy withheld.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-XPRINT%20Traffic%20Privacy - related derived-signal privacy evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-Device%20Tuning%20MTL - related device/cloud contract evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing - related representation-probing evidence.
- Source files: PDF, fallback full-paper HTML, metadata HTML, and integrity records; all withheld locally.
