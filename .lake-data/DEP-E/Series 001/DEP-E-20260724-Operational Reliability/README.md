# DEP-E-20260724-Operational Reliability

**Tags:** #operational-reliability #agent-memory #tool-use #evaluation #dependency-provenance #scientific-ai #research-review

This DEP-E package contains a public-safe, source-first synthesis of ten works collected in `DEP-20260703-Tech Intel 1102`. It examines reliable state and context management, model-state architecture, open-world tool shifts, safety-evaluation labels, skill supply chains, benchmark stability, rare-disease reasoning, geochemical tool use, and error suppression in a quantum-data-center experiment.

## Contents

- `README.md` - package inventory, context, synthesis, relevance, and attribution.
- `operational-reliability.md` - schema-complete research manuscript with an evidence ledger, critical review, implementation paths, MVP design, related research, and source references.

No `.source/` directory is included. Nine primary papers were reviewed through complete arXiv HTML, one temporary paper PDF was rendered and visually inspected, and six official public repository states were inspected at immutable commit pins. The temporary PDF and its page renderings were removed after validation; no external source file was deposited.

## Summary of Items

The manuscript reviews all ten works beyond the source DEP summaries and ties their reported evidence to an operational-reliability model. AutoMem, Self-GC, and State-Prediction Separation treat retained state as an engineered substrate. OpenAgent, Adversarial Pragmatics, the skill-supply-chain study, and the coding-benchmark audit expose failures caused by environmental shift, transitive authority, evaluator collapse, and scoring policy. RareDxR1, PHREEQC-MCQ-200, and the fiber-interconnected quantum study show why high-stakes or scientific claims require release, per-item, and experiment-boundary checks.

## Insights and Relevance

The cross-source result is a chain model of reliability: versioned state, explicit authority and dependency graphs, diagnostic evaluation with per-item accounting, and domain-specific evidence gates must all remain visible. A high scalar score cannot substitute for recoverability, source pins, failure-stage labels, retained-item analysis, or a clear distinction between emulation, benchmark evidence, and deployment readiness.

The package turns that synthesis into bounded implementation concepts: a reliability ledger, a synthetic state-retention testbench, a tool-shift and evaluator audit harness, a static skill dependency gate, and evidence gates for clinical or hardware-facing claims.

## Attribution Block

- Selected source bundle: Delphoa Labs, [`DEP-20260703-Tech Intel 1102`](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/0f6545b828537a6edecee1412ea8ebfa6dc42f94/.lake-data/DEP-20260703-Tech%20Intel%201102), including the [`daily research findings`](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f6545b828537a6edecee1412ea8ebfa6dc42f94/.lake-data/DEP-20260703-Tech%20Intel%201102/daily_research_findings_2026-07-03_1102.md).
- Shengguang Wu, Hao Zhu, Yuhui Zhang, Xiaohan Wang, and Serena Yeung-Levy, *AutoMem: Automated Learning of Memory as a Cognitive Skill*, [arXiv:2607.01224v1](https://arxiv.org/abs/2607.01224v1), [full HTML](https://arxiv.org/html/2607.01224v1), and [official release at `1987b8f`](https://github.com/autoLearnMem/AutoMem/tree/1987b8f6d202212ec3c0c78ab2a01ae02aca4e8b).
- Xubin Hao, Hongjin Meng, Xin Yin, Jiawei Zhu, and Chenpeng Cao, *Self-GC: Self-Governing Context for Long-Horizon LLM Agents*, [arXiv:2607.00692v1](https://arxiv.org/abs/2607.00692v1) and [full HTML](https://arxiv.org/html/2607.00692v1).
- Giovanni Monea, Nathan Godey, Kianté Brantley, and Yoav Artzi, *The State-Prediction Separation Hypothesis*, [arXiv:2607.01218v1](https://arxiv.org/abs/2607.01218v1), [full HTML](https://arxiv.org/html/2607.01218v1), and [official release at `7e405f4`](https://github.com/lil-lab/sps/tree/7e405f4596db39ce57ae3eea4efb7c1d21645b34).
- Song-Lin Lv, Weiming Wu, Rui Zhu, Zi-Jian Cheng, and Lan-Zhe Guo, *Can Agents Generalize to the Open World?*, [arXiv:2607.01084v1](https://arxiv.org/abs/2607.01084v1), [full HTML](https://arxiv.org/html/2607.01084v1), and [official release at `769692c`](https://github.com/LAMDA-NeSy/OpenAgent/tree/769692c14719d28c491fae992a3f814f1bb46f52).
- Brett Reynolds, *Adversarial Pragmatics for AI Safety Evaluation*, [arXiv:2607.01153v2](https://arxiv.org/abs/2607.01153v2), [full HTML](https://arxiv.org/html/2607.01153v2), and [official release at `b2819fb`](https://github.com/BrettRey/adversarial-pragmatics-for-ai-safety-evaluation/tree/b2819fbcb0033b020c57083a28e3eaf53ac649eb).
- Changguo Jia, Tianqi Zhao, Runzhi He, and Minghui Zhou, *Skills Are Not Islands: The Hidden Supply Chain Behind Agent Skills*, [arXiv:2607.01136v1](https://arxiv.org/abs/2607.01136v1) and [full HTML](https://arxiv.org/html/2607.01136v1).
- Zhi Chen, Zhensu Sun, Yuling Shi, David Lo, and Lingxiao Jiang, *Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?*, [arXiv:2607.01211v2](https://arxiv.org/abs/2607.01211v2), [full HTML](https://arxiv.org/html/2607.01211v2), and [official public data at `44a1cb8`](https://github.com/chenzhi-cz/performance-optimization-benchmark-reliability/tree/44a1cb86a9f765b0375b4cfb479641f3c19f0774).
- Deyang Jiang, Haoran Wu, Ziyi Wang, Yiming Rong, Yunlong Zhao, Ye Jin, and Bo Xu, *RareDxR1: Learning to Reason at the Knowledge Frontier for Rare Disease Diagnosis*, [arXiv:2607.00147v1](https://arxiv.org/abs/2607.00147v1), [full HTML](https://arxiv.org/html/2607.00147v1), and [official placeholder repository at `a6f4d07`](https://github.com/jdy18/RareDxR1/tree/a6f4d073c08a775064ed777e451799bfc1ba90cf).
- Ke Zhang, Sahchit Chundur, Mohammad Javad Qomi, and Maziar Raissi, *PHREEQC-MCQ-200: Diagnostic Evaluation of LLMs With and Without Geochemical Tools*, [arXiv:2607.00436v1](https://arxiv.org/abs/2607.00436v1), [full HTML](https://arxiv.org/html/2607.00436v1), and [PHREEQC Version 3 documentation](https://www.usgs.gov/software/phreeqc-version-3).
- Seyed Navid Elyasi, Sima Bahrani, Rui Wang, Dimitra Simeonidou, Paolo Monti, and Rui Lin, *Experimental Quantification of Layered Error Suppression in Fiber-Interconnected Quantum Data Centers*, [arXiv:2607.00735v1](https://arxiv.org/abs/2607.00735v1) and [paper PDF](https://arxiv.org/pdf/2607.00735v1).
- Related standards and architectural context: [SPDX Specification 3.0.1](https://spdx.github.io/spdx-spec/v3.0.1/), [CycloneDX specification overview](https://cyclonedx.org/specification/overview/), and J. Liu and L. Jiang, *Quantum Data Center: Perspectives*, [DOI:10.1109/MNET.2024.3397836](https://doi.org/10.1109/MNET.2024.3397836).

This package is an independent research review and does not imply author endorsement. All cited source documents remain under their original terms and are linked rather than redistributed.
