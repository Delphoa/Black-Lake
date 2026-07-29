# Report-Mark: Hybrid Spectrum Markets

## Source Metadata

Lin Gao, Biying Shou, Ying-Ju Chen, and Jianwei Huang, *Combining Spot and Futures Markets: A Hybrid Market Approach to Dynamic Spectrum Access*, arXiv:1405.7175 (2014-05-28), https://arxiv.org/abs/1405.7175; https://doi.org/10.48550/arXiv.1405.7175. Verified PDF and ar5iv HTML were inspected locally and withheld.

## Concise Research Notes

The paper combines futures contracts and spot transactions for secondary-spectrum allocation. An offline stochastic policy sets shadow-price context; an online VCG auction solicits private valuations. Spatial reuse makes exact maximum-weight independent-set allocation NP-hard, motivating a polynomial-time VCG-like approximation with a welfare-loss analysis. MATLAB simulations use 20 spot users, three contract users, uniform values, and 1,000 realizations; authors report 20% average welfare improvement over a random contract-demand baseline.

## Evidence and Attribution

| ID | Evidence | Assessment |
|---|---|---|
| E1 | arXiv record | identity and metadata |
| E2 | verified PDF/full HTML | method, mechanism, proofs as source claims |
| E3 | simulation section | reported results; not reproduced |
| E4-E6 | related DEPs | conceptual context only |

## Related DEP Entries

1. [2D-RC OTFS](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md) — structured wireless allocation; source basis: arXiv:2311.08543.
2. [Telecom AI Roadmap](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md) — digital-twin and control-boundary context.
3. [SIM MARL Power](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-SIM%20MARL%20Power/sim_marl_power_manuscript.md) — simulation-only coupled wireless allocation; source basis: arXiv:2502.19675.

## Synthesis Note

### Concept Bridge
All four works allocate scarce wireless resources under constraints; this paper contributes the incentive and approximation layer.

### Potential Implementations
1. Synthetic contract-and-spot simulator.
2. Offline welfare-bound dashboard.
3. Digital-twin allocation gate.

### Deeper Relationship Observations
1. State representation defines feasible allocation.
2. Fast decisions require quality receipts.
3. Simulation needs operational gates.

### Conceptual Similarities
1. Structured state.
2. Performance/complexity tradeoff.
3. No direct live-control authority.

### MVP Implementations With Code Mock-ups
1. `def eligible(bid, reserve): return bid >= reserve`
2. `def welfare(values): return sum(values)`
3. `def receipt(ratio): return {"approx_ratio": ratio, "operational": False}`

### Developer Challenges
1. Preserve interference constraints.
2. Audit fairness and privacy.
3. Keep simulation isolated.

### Author Challenges
1. Release seeds and configurations.
2. Test correlated demand.
3. Compare newer baselines.

## Validation Notes
Frozen-pool random selection, required dedup, and complete-source verification passed. No source document is public.

## Attribution Block

- Source URL: https://arxiv.org/abs/1405.7175
  - Applies to: this report and manuscript.
  - Notes: canonical metadata.
- Source URL: https://ar5iv.labs.arxiv.org/html/1405.7175
  - Applies to: full-paper review.
  - Notes: validated fallback; source withheld.
