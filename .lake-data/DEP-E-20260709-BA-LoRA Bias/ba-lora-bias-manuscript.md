---
title: "BA-LoRA Bias - DEP-E"
generated_at: "2026-07-09 (public-safe date)"
artifact_type: "DEP research artifact"
primary_subject: "BA-LoRA proposes output-space regularizers for bias and robustness control during parameter-efficient LLM fine-tuning."
source_status: "URLs only with local archive metadata observed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-09"
temporal_cutoff: "Sources inspected through 2026-07-09."
primary_url: "https://arxiv.org/abs/2408.04556"
stable_identifier: "arXiv:2408.04556"
confidence_summary: "Medium-high for paper identity, method, and selected reported results; lower for reproduction because code and experiments were not run."
safety_scope: "research review, robustness evaluation, non-sensitive implementation planning"
distribution_notes: "No source PDF, code snapshot, dataset, or local source file is redistributed."
---

# BA-LoRA Bias - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | BA-LoRA arXiv abstract page | Primary paper metadata | HTML | arXiv:2408.04556; metadata page reports v8 | https://arxiv.org/abs/2408.04556 | arXiv-issued DOI and license link visible; no file redistributed. | 2026-07-09 | Inspected |
| S2 | BA-LoRA arXiv HTML | Primary paper full text | HTML | HTML rendering exposed v7 text during inspection | https://arxiv.org/html/2408.04556 | arXiv HTML used for source-grounded review; version mismatch noted. | 2026-07-09 | Inspected |
| S3 | BA-LoRA public PDF | Primary paper source | PDF | arXiv:2408.04556 | https://arxiv.org/pdf/2408.04556 | Public PDF URL referenced; file not redistributed. | 2026-07-09 | Referenced |
| S4 | BA-LoRA DOI | Persistent identifier | DOI page | 10.48550/arXiv.2408.04556 | https://doi.org/10.48550/arXiv.2408.04556 | arXiv-issued DOI. | 2026-07-09 | Referenced |
| S5 | BA-LoRA official repository | Near-primary implementation | GitHub repository | `llm172/BA-LoRA`, main commit `1fe17ab3e39dcfefc630cdf386d69d942c61f16c` | https://github.com/llm172/BA-LoRA | GitHub API did not expose a license value; no files redistributed. | 2026-07-09 | Inspected |
| S6 | Local arXiv archive metadata | Selection provenance | Local metadata | arXiv:2408.04556 | Local path withheld | Local metadata confirmed title, arXiv URL, and PDF presence; not redistributed. | 2026-07-09 | Observed |
| S7 | Black-Lake README | Repository standard | Markdown | default branch | https://github.com/Delphoa/Black-Lake | Repository authority for DEP-E, logs, reports, README, and attribution rules. | 2026-07-09 | Inspected |
| S8 | Black-Lake-Data README | Related repository standard | Markdown | default branch | https://github.com/Delphoa-Labs/Black-Lake-Data | Related DEP context and raw-source attribution standard. | 2026-07-09 | Inspected |
| S9 | Local AI Stack DEP | Related DEP entry | Markdown | DEP-E-20260709-Local AI Stack | `.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md` | Repository-relative related artifact. | 2026-07-09 | Inspected |
| S10 | Agent State Review DEP | Related DEP entry | Markdown | DEP-E-20260708-Agent State Review | `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md` | Repository-relative related artifact. | 2026-07-09 | Inspected |
| S11 | Tech Intel 2338 DEP | Related DEP entry | Markdown | DEP-E-20260709-Tech Intel 2338 | `.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` | Repository-relative related artifact. | 2026-07-09 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary arXiv metadata | Title, authors, arXiv ID, DOI, submitted and revision dates, abstract, subjects, public source links. | Paper identity, research object, stable identifiers, abstract-level contribution. | High | Abstract-level evidence is insufficient for empirical validation. |
| E2 | S2 | Primary arXiv HTML | Introduction, method, experiment headings, selected result tables/text, limitations, ethics, reproducibility. | Mechanism, reported results, evidence limits, responsible-use context. | Medium-high | The HTML inspected identified v7 while metadata page reported v8; formulas and visual details may be imperfectly rendered. |
| E3 | S5 | Official repository | README/file inventory, official implementation status, ICLR 2026 statement, main commit, no license value exposed through GitHub API. | Code availability, implementation evidence, reuse caveat. | Medium | Repository was not cloned or executed; raw README access differed from rendered GitHub page. |
| E4 | S6 | Local archive metadata | Selected paper unit contained metadata for arXiv:2408.04556 and a PDF. | Random selection provenance. | Medium | Public artifacts withhold local paths; local PDF text extraction was not available. |
| E5 | S7-S8 | Repository README standards | DEP-E class, naming, contents, final Attribution Block, `.logs`, `.reports`, and `.lake-data` roles. | Artifact placement and validation. | High | Repository process evidence only. |
| E6 | S9 | Related Black-Lake DEP | PEFT compatibility and local/self-hosted model stack constraints. | Related-entry bridge for adapter deployment readiness. | Medium | Related artifact was inspected; underlying external sources were not revalidated in this pass. |
| E7 | S10 | Related Black-Lake DEP | State, monitoring, unlearning, and durable neural artifacts as review objects. | Related-entry bridge for adaptation-state and safety review. | Medium | Related artifact was inspected; underlying external sources were not revalidated in this pass. |
| E8 | S11 | Related Black-Lake DEP | Deployment simulation, model-bias, and low-precision systems evidence boundaries. | Related-entry bridge for bias/evaluation framing. | Medium | Related artifact was inspected; underlying external sources were not revalidated in this pass. |

## Executive Summary

BA-LoRA is a parameter-efficient fine-tuning method that aims to reduce "Catastrophic Inheritance": the propagation and amplification of bias, noise, and data imbalance from pre-training into downstream LoRA-style adaptation. The paper decomposes this problem into three failure modes: knowledge drift, representation collapse, and overfitting to noise. It then adds three output-space regularizers: consistency, diversity, and SVD-based regularization.

The key technical choice is to regularize logits or output distributions rather than directly penalizing adapter weights. The authors argue that output-space constraints better align with functional behavior: preserving pre-trained knowledge, maintaining representation diversity, and emphasizing robust low-rank output patterns. The method builds on PiSSA-style initialization and adapts the regularizer forms for NLU and NLG tasks.

The inspected evidence supports BA-LoRA as a promising research direction, with reported improvements over LoRA/PiSSA variants on NLG and NLU tasks, targeted noisy-pretraining probes, imbalanced MNLI analysis, and rank-sensitivity tests. Confidence is lower for reproduction because the code was not run, model/data dependencies were not collected, and the arXiv metadata/HTML version mismatch should be resolved by a later pass.

## Detailed Summary

### Problem

LoRA-style parameter-efficient fine-tuning reduces adaptation cost by updating low-rank adapter matrices while leaving most model weights frozen. BA-LoRA argues that this low-rank bottleneck can amplify inherited problems from pre-training when downstream data is noisy, imbalanced, or biased. The paper calls this problem Catastrophic Inheritance and treats it as a fine-tuning failure mode rather than only a pretraining-data problem.

### Method

The method starts from PiSSA-style low-rank initialization, which uses singular value decomposition of the original weight matrix to initialize adapter components. BA-LoRA then adds output-space regularizers:

- Consistency regularization: distills behavior from the pre-trained model to reduce knowledge drift.
- Diversity regularization: discourages representation collapse, using covariance-style decorrelation for NLU and top-k entropy diversity for NLG.
- SVD-based regularization: encourages robust low-rank structure in output logits to reduce overfitting to noisy or high-frequency patterns.

For NLU tasks, BA-LoRA combines cross-entropy with KL consistency, batch-wise logit covariance regularization, and an SVD objective. For NLG tasks, it uses token-level temperature distillation, focused entropy over plausible top-k tokens, and randomized SVD with Frobenius normalization for tractability over large vocabularies.

### Experiments and Results

The paper reports evaluations across NLG and NLU settings using models such as LLaMA-2-7B and DeBERTa-v3-base. It also discusses RoBERTa-base and T5-base as a noisy-pretraining probe, with an explicit caveat that the comparison is suggestive rather than a controlled causal test because the models differ by architecture and objective.

Specific inspected results include:

- On MNLI, the appendix reports BA-LoRA with covariance regularization at 91.26 percent accuracy, compared with 90.71 for standard LoRA and 90.41 for an entropy-regularized BA-LoRA variant.
- In an imbalanced MNLI setting, the appendix reports minority-class recall of 61.7 for BA-LoRA, compared with 5.8 for standard LoRA and 26.4 for PiSSA.
- Across rank sweeps, the paper states that BA-LoRA consistently outperforms LoRA and PiSSA across tested ranks, models, and tasks, with higher-rank BA-LoRA/PiSSA sometimes exceeding full fine-tuning.

These are reported paper results, not independently reproduced measurements.

### Limitations and Safety Notes

The paper's limitations section states that evaluation is primarily English-language and should be extended to multilingual and specialized-domain settings. It also notes that the noisy-pretraining analysis using RoBERTa and T5 is compatible with the hypothesis but not a fully controlled causal test. The ethics section frames the work as bias and robustness mitigation while acknowledging dual-use risk because parameter-efficient methods lower the barrier to adapting LLMs.

### Code and Reproducibility

The arXiv HTML states that source code is available at `https://github.com/llm172/BA-LoRA`. The public repository was inspected and includes training scripts, configs, inference utilities, and a README describing BA-LoRA options. The GitHub API reported no license value, no releases, and main commit `1fe17ab3e39dcfefc630cdf386d69d942c61f16c` during review. No code was run in this pass.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | LoRA-style PEFT can exacerbate inherited bias, noise, and imbalance during downstream adaptation. | Author claim | E1, E2 | Supported by the paper framing and experiments, but broad generalization requires more controlled evidence. | Medium |
| C2 | BA-LoRA maps Catastrophic Inheritance to knowledge drift, representation collapse, and overfitting to noise. | Author conceptual claim | E2 | Directly supported by the method framing. | High |
| C3 | The three regularizers target output behavior rather than adapter parameters. | Author method claim | E2 | Directly supported by method and discussion sections. | High |
| C4 | BA-LoRA reports better minority-class behavior than LoRA/PiSSA in the imbalanced MNLI analysis. | Author empirical result | E2 | Supported by inspected appendix table; not independently reproduced. | High for reporting, low for reproduction |
| C5 | The RoBERTa/T5 noisy-pretraining probe is suggestive rather than causal. | Author limitation and reviewer interpretation | E2 | The paper explicitly notes architecture/objective confounds. | High |
| C6 | Official code exists, but reuse/reproduction assumptions need license and dependency review. | Reviewer implementation claim | E3 | Repository exists and was inspected; no license value exposed by GitHub API. | Medium |
| C7 | No same-paper Black-Lake Arxiv DEP artifact was found before accepting this random selection. | Process claim | E4, E5 | Supported by marker checks across logs, reports, lake-data, memory, and related repository search. | High |

## Methodology

- `Research objective`: Randomly select one eligible arXiv paper from the local archive, review it source-first, and deposit a public-safe Black-Lake `.logs`, `.reports`, and `DEP-E` artifact set.
- `Sources inspected`: Local arXiv archive metadata, arXiv abstract page, arXiv HTML, public PDF URL, official BA-LoRA GitHub repository metadata, live Black-Lake README, live Black-Lake-Data README, and three related Black-Lake DEP manuscripts.
- `Discovery strategy`: Candidate PDFs were enumerated with `rg --files -g "*.pdf"`. PDF parent directories were treated as paper units. A sorted list of 72,743 paper units was sampled with PowerShell `Get-Random`.
- `Inclusion criteria`: Sources were included when they identified the selected paper, supported method/results/limitations, supplied official implementation evidence, defined repository deposition rules, or offered concrete conceptual overlap.
- `Exclusion criteria`: PDFs, code snapshots, model weights, datasets, and source archives were not copied into `.source/` because redistribution permissions and reproduction scope were not independently resolved.
- `Analytical approach`: Mixed empirical, conceptual, comparative, implementation, safety/ethics, product research, and DEP-ready provenance review.
- `Evidence handling`: Author claims are labeled as paper claims unless independently validated. Reviewer interpretations are separated from source evidence. Related DEP entries are used as conceptual bridges, not as proof of BA-LoRA results.
- `Uncertainty handling`: Version mismatch, unexecuted code, uncollected datasets, unverified license status, and unreproduced metrics are stated explicitly.
- `Extraction process`: Public HTML and repository pages were inspected. Local metadata was observed for selection provenance. No local absolute paths are published.
- `Version control`: arXiv metadata page reported v8. The inspected arXiv HTML exposed v7 text. Official repository main commit was recorded.
- `Selection and deduplication note`: Duplicate checks searched `Black-Lake/.logs`, `.reports`, `.lake-data`, automation memory, and related Black-Lake-Data search for arXiv ID, title, and slug markers. No same-paper artifact was found, so no reselection was needed.
- `Reviewer stance`: DEP-ready paper review, implementation planning, and future reproduction triage.

## Scope, Constraints, and Assumptions

- `Scope`: Review BA-LoRA as the selected Arxiv DEP paper and preserve a schema-complete DEP-E manuscript plus related log and Report-Mark.
- `Temporal boundary`: Public source access date is 2026-07-09.
- `Evidence limits`: The paper's reported results were not reproduced. Code was inspected at repository metadata/README level only. Datasets, model weights, training scripts, and hardware were not run. arXiv metadata and HTML version signals differed.
- `Assumptions`: The local archive metadata correctly identifies the selected paper unit. The public arXiv and GitHub pages are sufficient for a first-pass DEP-E review.
- `Constraints`: Public artifacts must avoid local absolute paths, home directories, usernames, machine names, local timezone labels, and exact local execution timestamps. Source files are not redistributed.
- `Out of scope`: Reproducing experiments, auditing dataset licenses, downloading model weights, collecting PDFs/code into `.source/`, or making deployment claims for high-stakes settings.
- `Intended use`: Black-Lake DEP-E deposition, future reproduction planning, PEFT robustness review, and related-entry graph expansion.
- `Audience`: Research reviewers, LLM fine-tuning engineers, safety reviewers, and Black-Lake automation maintainers.
- `Reproducibility boundary`: Another reviewer can follow the URLs and repository-relative paths, but cannot reproduce BA-LoRA from this artifact alone.
- `Data sensitivity`: Public paper/repository metadata and local archive selection metadata only; no private data collected.

## Observations

- `Observed pattern`: BA-LoRA reframes PEFT as behavior-constrained adaptation rather than only a parameter-count reduction technique.
- `Technical implication`: Adapter review should track robustness, minority-class behavior, and drift metrics alongside accuracy and training cost.
- `Evidence-quality implication`: The arXiv metadata/HTML version mismatch should be resolved before a table-level reproduction or correction pass.
- `Operational implication`: The Local AI Stack related entry suggests BA-LoRA-style adapters need registry, runtime, tokenizer, and serving compatibility evidence to become deployable artifacts.
- `Safety implication`: The ethics note's dual-use concern is real for PEFT methods because easier adaptation can support both beneficial debiasing and harmful specialization.
- `Open question`: Can BA-LoRA's output-space regularization be combined with deployment-time monitors to create a closed loop from fine-tuning to live safety checks?

## Considerations

BA-LoRA should be treated as a research method with promising reported results, not as a proven deployment control. Robustness claims depend on the selected tasks, datasets, models, regularization weights, and evaluation metrics. For high-impact domains, an adapter would need dataset governance, bias audits, minority-group performance checks, model-card updates, and monitoring after deployment.

The official repository improves inspectability, but the absence of a detected license and the lack of run validation in this pass limit what can be redistributed or claimed. A future reproduction pass should pin dependencies, model checkpoints, datasets, training seeds, hardware, and expected tables.

The method's strongest conceptual value for Black-Lake is its mapping from failure modes to regularizers. That mapping can inform adapter review checklists even before full reproduction: ask what preserves base knowledge, what prevents collapse, what reduces noisy overfit, and what evidence supports each answer.

## Strengths

- The paper gives a clear decomposition of the adaptation failure problem into knowledge drift, representation collapse, and overfitting to noise.
- The regularizers are tied to observable output-space behavior, making the method easier to reason about than opaque adapter-weight penalties.
- The inspected results include both standard benchmark performance and targeted robustness/bias analyses.
- The paper explicitly discloses important limitations around English benchmarks and confounded noisy-pretraining probes.
- An official implementation repository is publicly available for future reproduction review.

## Weaknesses

- Reported results were not reproduced in this run.
- arXiv metadata and HTML version signals differed, so version-specific claims need a later audit.
- The noisy-pretraining analysis is not a controlled causal test because RoBERTa and T5 differ in architecture and objective.
- The official repository did not expose a license through the GitHub API during inspection.
- Evaluation appears concentrated on English-language benchmarks, limiting confidence for multilingual and domain-specific deployment.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Resolve arXiv version differences | Evidence integrity | Metadata page reports v8 while HTML exposed v7. | Prevents table or wording drift in later reports. | Requires PDF/source comparison. | Compare v7/v8 PDFs, source, and result tables. |
| Reproduce core tables from official code | Reproducibility | Reported gains need executable validation. | Higher confidence in method and metrics. | Requires model weights, datasets, GPU compute, and dependency pinning. | Run official scripts at pinned commit and compare outputs. |
| Add matched-architecture noisy-pretraining probe | Causal evidence | RoBERTa/T5 comparison is confounded. | Stronger support for noisy-pretraining hypothesis. | Requires controlled pretraining variants or suitable public models. | Evaluate matched models with varied corpus quality. |
| Build adapter governance metadata | Deployment readiness | PEFT artifacts need traceable training and evaluation context. | Easier review and safer reuse. | Requires process discipline and registry design. | Require metadata fields before adapter promotion. |
| Extend multilingual/domain evaluation | Generalization | English-heavy benchmark evidence may not transfer. | Better boundary conditions. | Data and evaluation complexity. | Test multilingual GLUE-style tasks and domain-specific data with safety review. |

## Potential Implementations

1. `BA-LoRA Reproduction Harness`
   - `User`: ML engineer or research reviewer.
   - `Goal`: Re-run selected BA-LoRA experiments from the official repository and produce a traceable result ledger.
   - `Core mechanism`: Pin repository commit, dependencies, datasets, base models, hyperparameters, and expected tables.
   - `Required inputs`: Official code, model access, benchmark datasets, config files, GPU environment, and source references.
   - `Outputs`: Reproduction report, metric deltas, failed-run notes, and license/dependency inventory.
   - `Risk controls`: No private data, no unlicensed redistribution, clear model-license review, and environment isolation.
   - `Evaluation`: Match reported metrics within predeclared tolerance or record divergence.

2. `Adapter Bias Review Card`
   - `User`: Team evaluating fine-tuned LLM adapters.
   - `Goal`: Make adapter robustness and inherited-bias evidence reviewable before deployment.
   - `Core mechanism`: Record base model, adapter method, training data, regularizers, minority-class metrics, drift metrics, and known caveats.
   - `Required inputs`: Adapter metadata, evaluation results, source URLs, training config, and bias/robustness probes.
   - `Outputs`: Markdown/JSON review card and promotion decision checklist.
   - `Risk controls`: Public-safe metadata only, no sensitive training examples, and mandatory high-impact domain flags.
   - `Evaluation`: Review cards pass schema checks and catch missing bias/robustness evidence.

3. `Output-Space Regularizer Playground`
   - `User`: Research educator or prototype engineer.
   - `Goal`: Demonstrate consistency, diversity, and spectral regularization on synthetic data.
   - `Core mechanism`: Train small toy classifiers with LoRA-like adapters and compare regularizer effects on imbalance/noise.
   - `Required inputs`: Synthetic datasets, small model, configurable regularizer weights, and metric scripts.
   - `Outputs`: Plots, metric tables, and explanatory notebook.
   - `Risk controls`: Synthetic data only, no deployment claims, and clear separation from paper reproduction.
   - `Evaluation`: Minority recall, calibration, stability, and ablation comparisons on toy tasks.

## Three Ways to Exercise This Research

1. `Run a synthetic imbalance probe`: Objective: test whether output-space diversity regularization improves minority-class recall in a toy classifier. Inputs: synthetic imbalanced labels, small neural model, LoRA-like adapter, and metric script. Method: compare baseline adapter, PiSSA-like initialization, and diversity-regularized variant. Output: metric table. Success criterion: minority recall improves without unacceptable overall accuracy loss. Safety boundary: synthetic data only.
2. `Create an adapter review card`: Objective: translate BA-LoRA evidence requirements into a reusable checklist. Inputs: this manuscript, official paper URLs, and a sample adapter config. Method: fill fields for base model, data, regularizers, metrics, limitations, and source references. Output: Markdown/JSON review card. Success criterion: every deployment claim has an evidence row. Safety boundary: no sensitive examples or local paths.
3. `Audit the official repository`: Objective: determine what is needed to reproduce one main BA-LoRA table. Inputs: official repository, pinned commit, README, scripts, and requirements. Method: inspect configs and scripts without training, then list missing model/data/environment prerequisites. Output: reproduction readiness report. Success criterion: reviewer knows the exact next steps and blockers. Safety boundary: no model weights or restricted datasets downloaded without license review.

## Example MVP Product

- `Product name`: AdapterGuard Review
- `Target user`: Teams fine-tuning and deploying LoRA-style adapters.
- `Problem`: Adapter updates can improve task performance while amplifying inherited bias, noise, or imbalance, and teams often lack a structured review artifact for adapter risk.
- `Core workflow`: Register adapter metadata, attach source references, run synthetic and benchmark probes, record drift/diversity/noise metrics, generate a review card, and block promotion when evidence is missing.
- `Data requirements`: Adapter config, base model ID, training-data summary, public benchmark metrics, optional synthetic probes, regularizer weights, source URLs, and reviewer notes.
- `Architecture`: Local CLI with adapter metadata parser, metric ingester, synthetic probe runner, evidence ledger writer, sanitization scanner, and Markdown/JSON exporter.
- `Success metrics`: Percentage of adapter claims with evidence IDs, minority-class metric coverage, reproduction-readiness score, failed sanitization count, and reviewer time to decision.
- `Risk controls`: No raw sensitive training data in artifacts, license checks before source collection, local-only processing by default, high-impact domain flags, and human review before deployment.
- `Limitations`: MVP cannot prove fairness or robustness in all settings, reproduce BA-LoRA without compute/data, or certify high-impact deployment.
- `MVP boundary`: Review and evidence tracking only; no automatic deployment.
- `Deployment model`: Local CLI or repository automation step.
- `Evaluation plan`: Run on synthetic adapters and one public PEFT example, then compare generated cards with manual reviewer expectations.
- `Failure modes`: False confidence from weak probes, missing subgroup metrics, stale dependency pins, and hidden dataset bias.
- `Maintenance plan`: Update schema fields as PEFT methods, benchmarks, and repository policies evolve.

Minimal illustrative sketch:

```python
from dataclasses import dataclass

@dataclass
class AdapterEvidence:
    method: str
    base_model: str
    source_ids: list[str]
    metrics: dict[str, float]
    limitations: list[str]

def promotion_status(evidence: AdapterEvidence) -> str:
    required = {"overall_accuracy", "minority_recall", "drift_score"}
    missing = sorted(required - set(evidence.metrics))
    if missing:
        return "blocked: missing " + ", ".join(missing)
    if evidence.metrics["minority_recall"] < 0.60:
        return "review_required: weak minority recall"
    return "review_required: evidence complete"
```

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| BA-LoRA | Primary arXiv paper | Reviewed paper on bias-alleviating low-rank adaptation. | https://arxiv.org/abs/2408.04556 |
| BA-LoRA official implementation | Official repository | Code, scripts, configs, and implementation context for future reproduction. | https://github.com/llm172/BA-LoRA |
| PiSSA | Methodological precursor | BA-LoRA builds on PiSSA-style initialization. | Cited by the reviewed paper |
| LoRA | Methodological baseline | Baseline PEFT method that BA-LoRA compares against. | Cited by the reviewed paper |
| Local AI Stack DEP | Black-Lake related artifact | Adapter/runtime compatibility and PEFT deployment-stack context. | `.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md` |
| Agent State Review DEP | Black-Lake related artifact | State, monitoring, unlearning, and durable neural artifacts as review objects. | `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md` |
| Tech Intel 2338 DEP | Black-Lake related artifact | Deployment simulation, low-precision bias, and safety/governance evidence boundaries. | `.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2408.04556 | BA-LoRA metadata, abstract, arXiv ID, DOI, revision history, and public links. | 2026-07-09 | Primary arXiv metadata page inspected. |
| R2 | https://arxiv.org/html/2408.04556 | BA-LoRA method, selected results, limitations, ethics, reproducibility, and code URL. | 2026-07-09 | Public arXiv HTML inspected; version mismatch noted. |
| R3 | https://arxiv.org/pdf/2408.04556 | Source availability reference. | 2026-07-09 | PDF URL referenced; file not redistributed. |
| R4 | https://doi.org/10.48550/arXiv.2408.04556 | Persistent DOI reference. | 2026-07-09 | DOI referenced. |
| R5 | https://github.com/llm172/BA-LoRA | Official implementation repository. | 2026-07-09 | Repository inspected; no source files redistributed. |
| R6 | Local arXiv archive metadata, path withheld | Selection provenance and local PDF/readme presence. | 2026-07-09 | Local path withheld under sanitization policy. |
| R7 | https://github.com/Delphoa/Black-Lake | Output repository DEP-E, log, report, README, and attribution requirements. | 2026-07-09 | Live README inspected through GitHub API. |
| R8 | https://github.com/Delphoa-Labs/Black-Lake-Data | Related source repository DEP and attribution expectations. | 2026-07-09 | Live README inspected through GitHub API. |
| R9 | `.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md` | Related PEFT/tooling and local AI stack context. | 2026-07-09 | Repository-relative related artifact inspected. |
| R10 | `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md` | Related state, safety monitoring, unlearning, and durable artifact context. | 2026-07-09 | Repository-relative related artifact inspected. |
| R11 | `.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` | Related deployment simulation, low-precision bias, and safety-governance context. | 2026-07-09 | Repository-relative related artifact inspected. |

## Appendix

### Random Selection and Deduplication Record

- Candidate enumeration command family: `rg --files -g "*.pdf"`.
- Candidate unit rule: PDF parent directory equals one paper unit.
- Candidate count: 72,743 paper units.
- Random index: 55,421.
- Selected identifier: arXiv:2408.04556.
- Duplicate markers found before acceptance: 0.
- Reselections required: 0.
- Same-paper search keys included arXiv ID, title phrase, `BA-LoRA`, `Bias-Alleviating`, and slug variants.
- Same-paper locations checked: `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, automation memory, and related Black-Lake-Data code search.

### Source Collection Notes

No `.source/` directory was created. The deposit references public URLs and repository-relative artifacts only. The local archive PDF was not redistributed.

### Validation Checklist

- Required manuscript headings are present.
- YAML `title` and H1 are identical and under 40 characters.
- `## Evidence Ledger` exists.
- `## Key Claims and Evidence` separates author claims from reviewer interpretation.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- `## Example MVP Product` includes product name, target user, problem, workflow, data requirements, architecture, success metrics, risk controls, and limitations.
- Claims are tied to evidence ledger IDs or source references.
- Related research includes exactly three Black-Lake related entries in the core synthesis.
- Public artifact text uses repository-relative paths and public URLs, not local absolute paths.
