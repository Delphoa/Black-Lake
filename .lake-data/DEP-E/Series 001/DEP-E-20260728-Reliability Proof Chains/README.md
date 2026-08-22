# DEP-E-20260728-Reliability Proof Chains

**Tags:** `agent-reliability`, `evidence-gates`, `verification`, `security`, `provenance`, `DEP-E`

This DEP-E entry deposits a cross-domain research manuscript derived from `Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 1102`. It examines how agentic systems become more trustworthy when intermediate outputs are converted into inspectable evidence and passed through independent gates. Chai, a differential-testing workflow for security libraries, is the newly expanded supporting source in this pass.

## Contents

- `README.md` — artifact inventory, summaries, and attribution.
- `reliability-proof-chains.md` — schema-complete DEP research artifact.

No paper PDF, source archive, repository checkout, model, dataset, benchmark payload, mobile trace, laboratory sample, clinical record, or quantum workload is deposited.

## Summary

The reviewed works cover scientific protocol translation, long-agent memory, formal proof repair, repository-scale vulnerability analysis, retrieval attacks, mobile GUI control, autonomous scientific research, multimodal safety steering, medical reasoning, and quantum-computation equivalence. Their domains differ, but their strongest mechanisms share a pattern: preserve the evidence-bearing intermediate state, apply a domain-specific gate, retain rejected outcomes, and escalate disagreement instead of allowing a single model judgment to stand in for validation.

The newly reviewed Chai paper makes this pattern especially concrete. Its mutation programs deterministically build equivalent security objects for multiple libraries, discrepancies become machine-checkable signals, and downstream reverse-dependency search converts parser divergence into a targeted impact audit. Chai also illustrates the limits of such chains: coverage remains empirical, manual preparation is substantial, and confirmed library discrepancies do not automatically establish downstream exploitability.

## Key Insights and Relevance

- A reliable agent pipeline is better modeled as an evidence graph than as a sequence of confident answers.
- Lossless state preservation, deterministic replay, executable verification, comparative validation, and explicit safety stops are complementary gates rather than interchangeable ones.
- Aggregate benchmark gains can conceal weak dimensions, proprietary evaluation surfaces, or unresolved integrity failures.
- Adversarial sources such as KidnapRAG show why provenance and trust boundaries must be enforced before retrieved material is allowed to shape reasoning.
- Chai adds a useful implementation pattern: compare independently maintained systems on identical bytes, then audit the consequences of disagreements rather than treating disagreement as the final result.
- The proposed MVP is an evidence-gate ledger that stores claims, artifacts, validators, disagreements, and release decisions with reproducible provenance.

## Attribution Block

- Source repository: [Black-Lake-Data](https://github.com/Delphoa-Labs/Black-Lake-Data)
- Output repository: [Black-Lake](https://github.com/Delphoa/Black-Lake)
- Source DEP: [DEP-20260702-Tech Intel 1102](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260702-Tech%20Intel%201102)
- Source repository guidance: [Black-Lake-Data README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md)
- Output repository guidance: [Black-Lake README](https://github.com/Delphoa/Black-Lake/blob/main/README.md)
- Prior related artifact: [BEAGLE Learner](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260710-BEAGLE%20Learner)
- Prior related artifact: [SAILFISH Vetting](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-SAILFISH%20Vetting)
- Jiang, Yankai, et al. [ProtoPilot](https://arxiv.org/abs/2606.31763)
- Liao, Ning, et al. [ACE](https://arxiv.org/abs/2606.31564)
- Breen, Benjamin, et al. [AxDafny](https://arxiv.org/abs/2606.32007)
- Armillotta, Michele, et al. [Antaeus](https://arxiv.org/abs/2607.01138)
- Choi, Chanwoo, et al. [KidnapRAG](https://arxiv.org/abs/2607.00422) and [official code](https://github.com/chanwoochoi316/KidnapRAG)
- Cao, Wanxia, et al. [Xiaomi-GUI-0](https://arxiv.org/abs/2606.31410) and [project page](https://seerray-lab.github.io/Xiaomi-GUI-0/)
- Tang, Qiong, et al. [FARS](https://arxiv.org/abs/2606.31651)
- D'Incà, Moreno, et al. [MARS](https://arxiv.org/abs/2606.31876)
- Zheng, Xianda, et al. [Evo-PI](https://arxiv.org/abs/2606.31800) and [official code](https://github.com/zhengxianda/Evo_PI)
- Werner, Matthias. [Global transverse-field Ising universality](https://arxiv.org/abs/2607.01227)
- Villa, Corban, et al. [Chai](https://arxiv.org/abs/2606.26933)
