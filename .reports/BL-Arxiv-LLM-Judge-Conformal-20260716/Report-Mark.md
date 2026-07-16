# Report-Mark: LLM Judge Conformal

## Source Metadata

| Field | Value |
|---|---|
| Title | Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction |
| Authors | Huanxin Sheng; Xinyi Liu; Hangfeng He; Jieyu Zhao; Jian Kang |
| Identifier | arXiv:2509.18658v1; DOI 10.48550/arXiv.2509.18658 |
| Submitted | 2025-09-23 |
| Primary record | https://arxiv.org/abs/2509.18658v1 |
| Official code | https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge |
| Code pin | `6c5d8302999b028d460dd1a7b78d698c56f7b7b7` |
| Source integrity | Repaired from partial to verified complete before review |
| Source policy | PDF, HTML, metadata, TeX/source, and extracted cache withheld locally |

## Concise Research Notes

The paper applies split conformal prediction to the token-logit features of rating-based LLM judges. It compares seven regression-style and two ordinal methods, uses a held-out calibration set to form intervals, and defines interval width as an uncertainty signal. A discrete boundary adjustment maps continuous endpoints onto rating labels and is proved to have non-decreasing coverage under the paper's assumptions.

Experiments cover SummEval (1,600 samples), DialSumm (1,400), and four roughly 200-sample ROSCOE reasoning subsets. Three judge models, G-Eval and SocREval, nine conformal methods, 50/50 calibration-test splits, and 30 random seeds form the main grid. Representative evidence includes the reported LVD e-SNLI/Qwen2.5-72B/SocREval coverage increase from 85.96% to 95.53% after adjustment, and an 88.7% MSE reduction from 3.907 to 0.443 for a SummEval fluency midpoint example.

The key limitation is exchangeability. A nominal interval is not automatically valid after a judge, prompt, population, annotation policy, or data distribution changes. Human labels also carry subjectivity and bias, and the interval midpoint is a heuristic rather than a classical mean or mode.

## Evidence and Attribution

- Complete PDF, official full-paper HTML, metadata HTML, and TeX/source archive were inspected after local integrity verification.
- The source archive supplied method equations, tables, limitations, ethics, prompts, and experiment details.
- The official repository README, tree, notebooks, and scripts were inventoried at the pinned commit; code was not executed and no license was visible.
- All original source artifacts and extracted text remain local and were excluded from the repository.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` - directly complements interval calibration by distinguishing faithful expression from correctness and documenting evaluator-proxy risk.
2. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - supplies a neighboring finite-sample interval framework and makes on-distribution transfer assumptions operationally explicit.
3. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` - shows another use of model confidence as a control signal, here for reasoning compression rather than evaluation abstention.

## Synthesis Note

### Concept Bridge

The shared pattern is a calibrated control surface. A model emits a score or confidence proxy; a statistical or learned layer converts it into an uncertainty-aware signal; an application then decides whether to accept, abstain, compress, re-evaluate, or escalate. The selected paper contributes interval-valued evaluation, PAC Confidence contributes finite-sample decision bounds, RLMF separates stated from factual confidence, and ConMax shows confidence-dependent resource allocation. Their combination favors visible assumptions and separate gates over a single opaque trust number.

### Potential Implementations

1. **Evaluation evidence card** - wrap every LLM-judge rating with interval, support count, judge/prompt versions, calibration manifest, and shift status.
2. **Human-review router** - prioritize cases using interval width and downstream cost while enforcing workload and slice-fairness budgets.
3. **Judge regression monitor** - replay a fixed calibration suite after model or prompt changes and block deployment when empirical coverage falls below policy.

### Deeper Relationship Observations

1. RLMF and conformal judging optimize different targets: one asks whether uncertainty language tracks a proxy for internal support; the other asks whether human labels fall inside a calibrated score interval.
2. PAC Confidence and the selected paper both rely on finite calibration evidence, so distribution shift is a shared invalidation mechanism even though their interval constructions differ.
3. ConMax and interval judging both treat confidence as a downstream control input, but resource savings and correctness assurance must remain independently measured.

### Conceptual Similarities

1. **Proxy visibility:** every method depends on a measurable surrogate—token logits, bin correctness, sampled consistency, or auxiliary-model confidence.
2. **Conditional validity:** conclusions hold within a versioned model, data, prompt, and calibration envelope.
3. **Gate composition:** useful systems translate uncertainty into bounded accept, abstain, review, or resource-allocation actions.

### MVP Implementations with Code Mock-ups

1. **Split-conformal interval helper**

~~~python
import numpy as np

def split_interval(prediction, calibration_errors, alpha=0.1):
    errors = np.asarray(calibration_errors, dtype=float)
    rank = int(np.ceil((len(errors) + 1) * (1 - alpha)))
    q = np.sort(errors)[min(rank - 1, len(errors) - 1)]
    return float(prediction - q), float(prediction + q)
~~~

This toy symmetric construction assumes exchangeable calibration and test cases. A real implementation must validate split lineage, empty inputs, method choice, and coverage by slice.

2. **Discrete boundary adjustment**

~~~python
import math

def rating_bounds(lower, upper, minimum=1, maximum=5):
    adjusted_lower = max(minimum, math.floor(lower))
    adjusted_upper = min(maximum, math.ceil(upper))
    return adjusted_lower, adjusted_upper
~~~

This deliberately conservative example expands toward valid labels. It does not reproduce every paper-specific adjustment case or prove coverage.

3. **Offline review policy**

~~~python
def route_interval(lower, upper, shift_ok, max_width=1.5):
    if not shift_ok:
        return "recalibrate"
    if upper - lower > max_width:
        return "human_review"
    return "eligible_for_policy_check"
~~~

The final state is not automatic acceptance: application-specific risk, fairness, and fallback gates still decide whether a score may be used.

### Developer Challenges

1. Preserve calibration/test separation and detect when model, prompt, or label changes invalidate the stored interval policy.
2. Implement multiple conformal methods without hiding method-specific assumptions behind one generic confidence API.
3. Report interval width, empirical coverage, slice support, review load, and decision cost without collapsing them into one score.

### Author Challenges

1. Establish coverage behavior under realistic judge updates, prompt drift, covariate shift, and temporally changing annotations.
2. Clarify data licenses and publish a reproducible environment manifest for the official repository.
3. Compare interval-based routing with stronger human and repeated-judge baselines under equal compute and decision-cost budgets.

## Validation Notes

- Random selection used a uniform draw over 75,776 PDF-parent units; the first draw passed dedup.
- Review did not begin until PDF and full-paper HTML independently passed the mandatory source gate.
- Missing-only extraction changed the cache from miss to `cached` with all three text outputs present.
- Required exact-three sections were counted; the three Python blocks are bounded and require syntax validation before submission.
- No local absolute path, username, machine name, local timezone label, or exact local execution timestamp appears.
- The staged source-upload gate must contain only generated Markdown and the derived dedup JSON.

## Attribution Block

- Primary paper: https://arxiv.org/abs/2509.18658v1
- PDF locator: https://arxiv.org/pdf/2509.18658
- Full-paper HTML locator: https://arxiv.org/html/2509.18658
- TeX/source locator: https://arxiv.org/e-print/2509.18658
- Official implementation: https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge
- Related Black Lake sources: the three repository-relative paths listed above
- Source-file statement: original paper documents, code snapshots, and extraction caches were not copied into this report or DEP.
