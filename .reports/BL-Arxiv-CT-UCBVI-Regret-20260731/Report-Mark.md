# Report-Mark: CT-UCBVI Regret

## Source Metadata

| Field | Record |
|---|---|
| Paper | *Square-root regret bounds for continuous-time episodic Markov decision processes* |
| Authors | Xuefeng Gao; Xun Yu Zhou |
| Primary version reviewed | arXiv:2210.00832v2, submitted 2022-10-03 and revised 2023-10-03 |
| Persistent identifiers | arXiv DOI 10.48550/arXiv.2210.00832; publisher DOI 10.1287/moor.2022.0283 |
| Public locators | https://arxiv.org/abs/2210.00832; https://arxiv.org/pdf/2210.00832; https://arxiv.org/html/2210.00832 |
| Later publication context | Mathematics of Operations Research publisher record: accepted 2024-11-09 and published online 2025-02-12; final full text was not inspected |
| Local source state | Complete verified PDF, metadata HTML, and full-paper HTML; source package unavailable; all source files withheld locally |

## Research Notes

The paper treats finite-horizon episodic learning in a tabular continuous-time Markov decision process, where each state-action pair has an unknown exponential holding-time rate and an unknown next-state distribution. CT-UCBVI estimates both quantities between episodes, builds a confidence bonus that covers their joint value error, and plans with a modified value iteration.

The substantive difference from discrete-time UCBVI is not merely a smaller time step. End-of-horizon holding times can be truncated, jump counts are random, and the continuous-time Bellman operator needs finitely terminated approximation. The paper uses a Poisson-process argument for rate confidence, a contraction analysis for approximate value iteration, and expectation-level bounds rather than a direct pathwise count argument.

Theorem 1 gives a worst-case upper bound with square-root dependence on the episode count. Theorem 2 supplies a matching square-root lower-bound dependence on episodes and actions under its tree-structured construction assumptions. The upper and lower bounds do not match tightly in states, horizon, or rate parameters. The only empirical illustration is a two-state machine operation-and-repair model averaged over 30 independent runs; its expected-regret curve is compared visually with the much larger worst-case bound through 10 million episodes.

## Evidence and Attribution

| ID | Evidence | Attribution and use |
|---|---|---|
| E1 | arXiv metadata | Confirms title, authors, v2 date, subjects, arXiv identifier, and arXiv DOI. |
| E2 | Verified arXiv v2 PDF and full-paper HTML | Supports CTMDP formulation, Algorithms 1-2, Theorems 1-2, proofs, simulation setup, and stated limits. |
| E3 | Publisher record | Confirms the later journal record and alerts readers that a prior-version proof gap required a substantial new argument. |
| E4 | GPMD Regularized RL DEP-E | Provides a nearby tabular-RL convergence and approximation-error comparison. |
| E5 | RRT-CBF Motion DEP-E | Provides a continuous-time control and execution-safety bridge. |
| E6 | SIM MARL Power DEP-E | Provides an empirical policy-optimization and constrained-system comparison. |

The PDF, metadata HTML, full-paper HTML, source-package status record, and acquisition receipts were inspected locally but are not redistributed. Public claims in this report point only to the public locators above.

## Related DEP Entries

1. [GPMD Regularized RL DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md) — related through tabular policy improvement, convergence guarantees, and explicit approximation-error boundaries.
2. [RRT-CBF Motion DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md) — related through finite-horizon continuous-time decision making and the gap between theoretical planning and safe execution.
3. [SIM MARL Power DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-SIM%20MARL%20Power/sim_marl_power_manuscript.md) — related through learning under coupled dynamics and the need to separate source-reported policy gains from deployment evidence.

## Synthesis Note

### Concept Bridge

CT-UCBVI supplies a model-based uncertainty-accounting layer for event-driven dynamics: estimate what is not known, convert that uncertainty into a bounded planning preference, and evaluate regret against a known-model comparator. The three related DEP entries make the bridge operational. GPMD highlights convergence and approximation-error accounting; RRT-CBF adds a constraint-and-tracking layer that regret theory does not provide; SIM MARL power demonstrates why observed policy gains must be distinguished from guarantee strength.

### Potential Implementations

1. **Event-driven planning sandbox.** A researcher supplies a synthetic finite CTMDP, an episode horizon, and a rate bound; the tool logs rate and transition confidence separately, computes optimistic policies, and plots regret against episodes. It must remain simulation-only and show confidence failures rather than silently clipping them.
2. **Maintenance-policy evaluator.** An operations analyst compares conservative and optimistic repair policies on a simulated machine fleet. Inputs are a vetted simulator and bounded rate priors; outputs are cumulative reward, jump count, confidence width, and policy changes. It must not control real equipment.
3. **Confidence-aware control harness.** A controls engineer places a CT-UCBVI-like proposal generator behind a hard constraint checker and a fallback policy. Inputs are a digital twin and safety envelopes; outputs are proposed actions plus rejection reasons. Constraint checks, not an exploration bonus, remain the authorization boundary.

### Deeper Relationship Observations

1. Both CT-UCBVI and GPMD make approximation explicit, but CT-UCBVI's error originates in continuous-time planning and partial observations whereas GPMD assumes bounded evaluator and optimizer errors.
2. The rate-confidence term is a temporal-data analogue of count confidence: total dwell time carries information even when end-of-episode truncation hides a next state.
3. RRT-CBF and SIM MARL both expose a missing layer in the selected paper: regret controls average learning loss, not hard feasibility, tail latency, communication cost, or policy rollback.

### Conceptual Similarities

1. All four artifacts separate a model or policy update from the evidence used to justify it.
2. All four require a declared boundary between source-supported behavior and reviewer or engineering inference.
3. All four benefit from bounded simulations before any claim about operational control.

### MVP Implementations with Code Mock-ups

1. **Rate-confidence ledger**

~~~python
from math import log, sqrt

def rate_radius(total_time, lambda_max, state_count, action_count, episodes, delta):
    ledger = 4 * log(2 * state_count * action_count * episodes / delta)
    denominator = max(total_time, ledger / lambda_max)
    return sqrt(lambda_max * ledger / denominator)
~~~

2. **Optimistic action scorer**

~~~python
def optimistic_score(estimated_reward, rate_radius, transition_radius, horizon):
    bonus = horizon * horizon * rate_radius + horizon * transition_radius
    return estimated_reward + bonus
~~~

3. **Simulation-only deployment gate**

~~~python
def choose_with_guard(proposed_action, allowed_actions, fallback_action):
    if proposed_action in allowed_actions:
        return proposed_action, 'accepted-by-static-simulation-guard'
    return fallback_action, 'fallback-required'
~~~

### Developer Challenges

1. Numerical quadrature and interpolation must preserve a visible planning-error budget; a discretized implementation cannot inherit the paper's theoretical guarantees automatically.
2. Event logs need separate dwell-time, completed-transition, and truncated-transition records so confidence calculations are auditable.
3. A realistic evaluator needs reproducible seeds, confidence intervals, runtime profiles, and failure handling rather than only cumulative-regret curves.

### Author Challenges

1. Release a reference implementation, grid settings, seeds, and a reproducible benchmark suite for CT-UCBVI.
2. Compare with stronger continuous-time and discretization baselines under matched compute and report uncertainty across repeated runs.
3. Reconcile the arXiv v2 and final journal versions with a public change summary, especially around the publisher-noted proof correction.

## Validation Notes

- Source identity was reconciled against arXiv metadata, the complete local source pair, and the official publisher record.
- The selected source passed the complete-paper gate: PDF size, header, and EOF passed; full-paper HTML exceeded body, marker, heading, and structural-term thresholds; no partial files remained.
- Selection used one uniform random index across 75,957 parent paper units. Exact identifier, DOI, title, slug, and recent-marker checks found no prior owning artifact.
- The report contains no source files, local filesystem details, local timestamps, usernames, machine names, or .source directory.

## Attribution Block

- Source URL: https://arxiv.org/abs/2210.00832
  - Applies to: this Report-Mark and the DEP-E manuscript.
  - Notes: Canonical arXiv metadata, authors, versions, and primary public identifier.
- Source URL: https://arxiv.org/pdf/2210.00832
  - Applies to: this Report-Mark and the DEP-E manuscript.
  - Notes: Public full-paper PDF locator; inspected source copy remains local.
- Source URL: https://arxiv.org/html/2210.00832
  - Applies to: this Report-Mark and the DEP-E manuscript.
  - Notes: Public full-paper HTML locator; inspected source copy remains local.
- Source URL: https://doi.org/10.1287/moor.2022.0283
  - Applies to: this Report-Mark and the DEP-E manuscript.
  - Notes: Publisher record used for later-version context only.
- Source URL: https://github.com/Delphoa/Black-Lake
  - Applies to: related-entry synthesis and deposited paths.
  - Notes: Public repository containing the three related DEP entries.
