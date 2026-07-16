# Multi-Point ISAC

**Tags:** `DEP-E`, `arXiv`, `ISAC`, `sensor fusion`, `beamforming`, `wireless optimization`, `source-first`

This public-safe deposit reviews arXiv:2208.07592v2 and translates its multi-point sensing/communication model into implementation and validation ideas. The source unit was repaired from partial to verified complete before review. Original PDF, full-paper HTML, metadata, TeX/source, extracted text, and cache artifacts remain local and were not uploaded.

## Contents

- `multi_point_isac_manuscript.md` - schema-complete source-grounded manuscript with evidence ledger, methodology, limitations, implementations, and related research.
- `README.md` - deposit inventory, concise synthesis, and attribution.

No `.source/` directory is present. Public source locators are included in the manuscript.

## Summary of Items

The manuscript reviews a six-device multi-point integrated sensing and communication system. Each device is assigned to sensing or communication, effective sensing devices are screened by SINR, binary detections are fused with an optimized voting rule, and power is allocated under per-device and sum constraints. The paper uses zero-forcing, a binomial fusion surrogate, and hybrid neighborhood/convex optimization to explore the sensing-accuracy versus communication-rate frontier.

## Insights and Relevance

- More sensing devices are not always better: a remote device can consume power, add interference, and reduce the effective fusion set.
- Voting thresholds should reflect asymmetric and heterogeneous error rates; majority vote is not generally optimal.
- A deployable optimizer needs calibrated detector errors, uncertainty and drift checks, typed constraints, simulation gates, and rollback rather than direct radio authority.
- The reviewed evidence is simulation-only and does not establish field robustness or global optimality.

## Attribution Block

**Primary work:** Guoliang Li, Shuai Wang, Kejiang Ye, Miaowen Wen, Derrick Wing Kwan Ng, and Marco Di Renzo, *Multi-Point Integrated Sensing and Communication: Fusion Model and Functionality Selection*, [arXiv:2208.07592v2](https://arxiv.org/abs/2208.07592v2), [journal DOI 10.1109/LWC.2022.3213883](https://doi.org/10.1109/LWC.2022.3213883). **Review and synthesis:** Codex for Delphoa Black Lake, 2026-07-16. Source files were withheld locally; no PDF, HTML, source archive, cache, or extracted source text was uploaded.
