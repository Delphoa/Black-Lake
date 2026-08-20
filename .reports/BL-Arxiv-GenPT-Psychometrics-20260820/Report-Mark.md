# Report-Mark: GenPT Psychometrics

## Source Metadata

| Field | Value |
|---|---|
| Title | *GenPT: Beyond Self-Report for Reliable LLM Psychometrics via Generative Projective Testing* |
| Authors | Ming Wang; Shuang Wu; Bixuan Wang; Lu Lin; Yuxin Chen; Xiaocui Yang; Daling Wang; Shi Feng; Yifei Zhang; Yufan Sun |
| arXiv | [2606.00860v1](https://arxiv.org/abs/2606.00860), submitted 2026-05-30 |
| arXiv DOI | [10.48550/arXiv.2606.00860](https://doi.org/10.48550/arXiv.2606.00860) |
| Published context | [ACL Anthology 2026.acl-long.1901](https://aclanthology.org/2026.acl-long.1901/), version 2, July 2026 |
| Published DOI | [10.18653/v1/2026.acl-long.1901](https://doi.org/10.18653/v1/2026.acl-long.1901) |
| Source formats inspected | Verified local PDF/full-paper HTML/metadata HTML, public arXiv HTML, ACL record, official code repository, and three related Black Lake manuscripts |
| Source status | Complete source pair verified locally; all source documents withheld from public output |
| Review boundary | Date-only 2026-08-20 artifact; exact local execution time withheld |

## Concise Research Notes

GenPT adapts projective-testing ideas for persona-conditioned language and multimodal-language agents. It asks whether newly generated, ambiguous stimuli can reduce contamination and social-desirability effects that may distort direct questionnaires. The design separates behavior collection from interpretation and diagnosis: the Examinee produces narratives, percepts, and sentence completions; an Interpreter maps those outputs to SCORS-G, simplified Rorschach, and SCT indicators; a Diagnostician maps the structured indicators to Big Five, MBTI, depression-risk, or suicide-ideation labels.

The tested protocol uses eight TAT-like storytelling prompts, ten Rorschach cards, and twenty sentence stems. Stage 1 behavior is held fixed while three interpreter/diagnostician backbones are compared. Fifteen CharacterRAG personas support personality tasks, and fifteen sampled AnnaAgent profiles support risk tasks. The paper reports questionnaire baselines with stronger personality-task results, while GenPT has higher reported depression accuracy across the three backbones and reaches the best reported suicide accuracy with Qwen3-8B.

The most useful interpretation is bounded complementarity rather than replacement. In the paper's perturbation tests, questionnaire suicide scores show strong downward directional drift under social-desirability framing, while no GenPT backbone shows the same high-agreement fake-good signature. The Qwen3-8B configuration also shows a large longitudinal depression shift. These findings are author-reported on small simulated-persona samples; they do not establish clinical validity, human psychological inference, or general backbone-independent reliability.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Complete local arXiv:2606.00860v1 PDF and full-paper HTML | Problem framing, three-stage mechanism, stimulus counts, scoring definitions, experiments, tables, limitations, and ethics | High for source reporting | Author-reported results; no independent rerun |
| E2 | [arXiv metadata](https://arxiv.org/abs/2606.00860) and [full HTML](https://arxiv.org/html/2606.00860) | Version, title, authors, subjects, full-paper section structure, public source locators, and paper claims | High | The arXiv v1 record is not the later ACL version 2 |
| E3 | [ACL Anthology record](https://aclanthology.org/2026.acl-long.1901/) | Published venue, pages 40958–40974, version 2, ACL DOI, and code/stimuli link | High for publication context | Publication metadata does not independently validate the experiments |
| E4 | [Official GenPT repository](https://github.com/sci-m-wang/GenPT) and [pyproject](https://github.com/sci-m-wang/GenPT/blob/main/pyproject.toml) | Public pipeline layout, stimuli, evaluation scripts, dependencies, and AnnaAgent data exclusion note | High for observed availability | No code, model, data, or experiment was executed; no visible repository license file was established |
| E5 | [Agent State Review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md) | State traces, context replay, and runtime monitoring as inspectable review objects | Medium | Related derived artifact, not independent GenPT evidence |
| E6 | [Agent Reliability Gates](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md) | Calibration, rejection, evidence gates, and intervention boundaries | Medium | Cross-domain synthesis; no joint experiment with GenPT |
| E7 | [OMGEval Benchmark](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md) | Benchmark validity, judge uncertainty, human comparison, and reproducibility limits | Medium | Methodological neighbor rather than a psychometrics source |

## Related DEP Entries

1. **Agent State Review** — `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md`. Its source basis connects persistent state, evidence replay, and runtime monitoring to the need for auditable behavioral traces; this is directly relevant to GenPT's Examinee outputs and context perturbations.
2. **Agent Reliability Gates** — `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md`. Its source basis treats calibration, rejection, and evidence gates as reliability boundaries; this supplies the missing deployment discipline around GenPT's interpreter and diagnostician outputs.
3. **OMGEval Benchmark** — `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md`. Its source basis examines judge uncertainty, limited human comparison, benchmark versioning, and reproducibility; these concerns transfer to evaluating a multi-stage psychometric pipeline.

## Synthesis Note

### Concept Bridge

GenPT turns ambiguous behavior into structured assessment evidence, but the bridge from generated behavior to a psychological label is itself a measurement system. Agent State Review supplies the state-trace lens, Agent Reliability Gates supplies the calibration and rejection lens, and OMGEval supplies the benchmark/judge-governance lens. Together they imply that a usable GenPT-derived evaluation record must preserve raw behavior provenance, interpreter uncertainty, diagnostician calibration, perturbation conditions, and abstention decisions. The practical destination is an evidence-bound agent-evaluation harness, not an autonomous clinical profiler.

### Potential Implementations

1. **Synthetic persona evaluation harness**: Run GenPT-style behavior collection on fictional, consent-free personas and preserve each stimulus, response, interpreter score, diagnosis, model version, and perturbation condition. Require abstention when the evidence ledger is incomplete; evaluate reproducibility across seeds and backbones.
2. **Perturbation reliability gate**: Treat neutral, job-framing, counselling-framing, and long-context conditions as paired probes. Report exact-match accuracy, ordinal agreement, DCR, calibration, and missing-output rates together, with a human review queue for surprising shifts.
3. **Evidence-bound research dashboard**: Present behavioral excerpts, rubric dimensions, model/version metadata, source citations, and reviewer decisions in a local-only dashboard. Keep the dashboard in shadow mode and prohibit person-level inference or consequential actions.

### Deeper Relationship Observations

1. **Behavior becomes state only through a traceable transformation**: GenPT's Interpreter and Diagnostician are state-construction layers, so their prompts, schemas, and uncertainty are part of the evidence rather than incidental implementation details.
2. **Context sensitivity and reliability are not opposites**: a good system should resist social framing while responding to a genuinely changed narrative context; the distinction requires paired perturbations and explicit hypotheses, not one aggregate score.
3. **The strongest result needs the strongest gate**: a reported suicide-risk advantage is precisely where small samples, label construction, cultural coverage, and misuse risk demand abstention, calibration, and independent review before any transfer claim.

### Conceptual Similarities

1. **Inspectable intermediate state**: all four records make intermediate evidence, state, or scoring steps visible instead of collapsing evaluation into a single headline label.
2. **Perturbation-aware validity**: the records treat framing, context, judge choice, or evidence selection as variables that can change conclusions and therefore must be logged.
3. **Evidence-bounded generalization**: each record separates source-reported performance from reproduction, deployment readiness, and broader claims about people or environments.

### MVP Implementations

1. **Synthetic perturbation ledger** — local-only paired evaluation record for fictional personas.

```python
def record_probe(persona_id, condition, output, scores, source_url):
    return {
        "persona_id": persona_id,
        "condition": condition,
        "output_hash": hash(output),
        "scores": scores,
        "source_url": source_url,
        "decision": "review_only",
    }
```

2. **Reliability gate calculator** — transparent toy calculation over already-collected synthetic ordinal predictions.

```python
def directional_consistency(baseline, perturbed):
    changes = [b != p for b, p in zip(baseline, perturbed)]
    if not any(changes):
        return {"dcr": 0.5, "status": "no_change"}
    up = sum(p > b for b, p in zip(baseline, perturbed))
    down = sum(p < b for b, p in zip(baseline, perturbed))
    return {"dcr": max(up, down) / (up + down), "status": "review_only"}
```

3. **Evidence-complete report gate** — refuse publication when provenance or safety fields are missing.

```python
def publication_gate(record):
    required = {"source_url", "model_version", "condition", "uncertainty", "risk_scope"}
    missing = sorted(required - record.keys())
    return {"publish": not missing, "missing": missing, "action": "human_review"}
```

### Developer Challenges

1. Define and validate a stable schema for behavior, rubric scores, explanations, model versions, perturbations, uncertainty, and abstention.
2. Distinguish content responsiveness from prompt sensitivity with enough paired samples, calibration data, and independent evaluators.
3. Build privacy-preserving, reproducible test fixtures without shipping sensitive dialogue data, licensed instruments, or uncontrolled model outputs.

### Author Challenges

1. Expand model, language, culture, and persona coverage while preserving a defensible ground-truth construction process.
2. Report uncertainty, confidence intervals, abstention behavior, and stronger baselines so small exact-match differences are not overinterpreted.
3. Clarify the intended non-clinical boundary and provide independent validation that generated stimuli, rubrics, and diagnostic prompts do not create new construct or contamination artifacts.

## Validation Notes

- Source gate: initial partial state repaired; PDF and full-paper HTML passed all required integrity checks; metadata HTML, provenance, and verification records are present; source package unavailable; no partial files remain.
- Evidence gate: methods, tables, conclusion, limitations, ethics, and implementation availability were based on complete source inspection and cross-checked against public arXiv, ACL, and official-repository records.
- Dedup gate: exact arXiv ID, DOI, normalized title, slug, repository artifacts, automation memory, Black-Lake-Data search results, and preceding-24-hour markers were checked before acceptance; no owning record found.
- Related-entry gate: exactly three concrete conceptual overlaps are listed above and tied to repository-relative paths and public GitHub URLs.
- Public-output gate: this report contains derived Markdown, public URLs, repository-relative paths, and public-safe source-boundary statements only. No PDF, HTML, source archive, cache, extracted source text, local absolute path, username, machine name, local timezone label, or exact execution timestamp is present.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.00860
  - Applies to: paper identity, authors, abstract, arXiv version, and public locator.
- Source URL: https://arxiv.org/html/2606.00860
  - Applies to: method, scoring framework, experiments, results, limitations, ethics, and appendices.
- Source URL: https://aclanthology.org/2026.acl-long.1901/
  - Applies to: ACL publication context, version 2, pages, and DOI.
- Source URL: https://github.com/sci-m-wang/GenPT
  - Applies to: official code, stimuli, repository layout, and reproducibility boundary.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: public artifact filing and source-locality rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion repository provenance and source-deposition boundary.
- Source files: withheld locally; none were uploaded, committed, or attached to Slack.
