---
title: "GenPT Psychometrics - DEP-E"
generated_at: "2026-08-20"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of GenPT for projective evaluation of persona-conditioned LLM agents."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "Public records and repository state inspected on 2026-08-20"
primary_url: "https://arxiv.org/abs/2606.00860"
stable_identifier: "arXiv:2606.00860v1; DOI: 10.48550/arXiv.2606.00860; ACL DOI: 10.18653/v1/2026.acl-long.1901"
confidence_summary: "Medium-high for method and reported results; medium for generalization because the evaluation uses small simulated-persona samples and was not independently reproduced."
safety_scope: "offline, synthetic, non-clinical agent evaluation"
distribution_notes: "Public artifact contains derived Markdown and public URLs only. Original source files remain local and are not redistributed."
---

# GenPT Psychometrics - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | Collection / License Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *GenPT: Beyond Self-Report for Reliable LLM Psychometrics via Generative Projective Testing* | Primary paper | PDF and full-paper HTML | arXiv:2606.00860v1; `cs.SI`; 2026-05-30 | [arXiv abstract](https://arxiv.org/abs/2606.00860), [arXiv HTML](https://arxiv.org/html/2606.00860), [arXiv PDF](https://arxiv.org/pdf/2606.00860) | Complete local source pair verified; source files withheld | 2026-08-20 | Inspected in full |
| S2 | ACL publication record | Publication context | HTML / PDF locator | 2026.acl-long.1901v2; July 2026; pages 40958–40974 | [ACL Anthology](https://aclanthology.org/2026.acl-long.1901/) | Published-record context; ACL materials and source rights remain governed by the venue | 2026-08-20 | Inspected |
| S3 | arXiv DOI record | Stable identifier | DOI | 10.48550/arXiv.2606.00860 | [DOI](https://doi.org/10.48550/arXiv.2606.00860) | Identifier locator | 2026-08-20 | Inspected |
| S4 | Official GenPT repository | Near-primary implementation | Git repository | main branch; README and `pyproject.toml` inspected | [GitHub repository](https://github.com/sci-m-wang/GenPT), [project metadata](https://github.com/sci-m-wang/GenPT/blob/main/pyproject.toml) | Public code/stimuli context; no visible repository license file established; AnnaAgent data is not included | 2026-08-20 | Inspected at README/file level |
| S5 | Agent State Review | Related DEP | Markdown | DEP-E-20260708 | [Black Lake manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md) | Derived repository artifact; source files remain governed by its attribution block | 2026-08-20 | Inspected |
| S6 | Agent Reliability Gates | Related DEP | Markdown | DEP-E-20260728 | [Black Lake manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260728-Agent%20Reliability%20Gates/agent-reliability-gates.md) | Derived repository artifact | 2026-08-20 | Inspected |
| S7 | OMGEval Benchmark | Related DEP | Markdown | DEP-E-20260717 | [Black Lake manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md) | Derived repository artifact | 2026-08-20 | Inspected |

The local source unit was initially partial because the PDF existed without a full-paper HTML companion. A bounded repair fetched the official full-paper HTML and refreshed the archive unit's README, provenance, machine-readable summary, acquisition receipt, and verification report. The PDF passed the 10 KB, `%PDF-`, and trailing `%%EOF` gate. The full-paper HTML passed the 5 KB, visible-body, document-marker, heading, and structure-term gates. No original source file or local archive path is included in this public artifact.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary paper | Full paper problem statement, three stages, stimulus design, scoring formulas, experiment settings, Tables 1–2, limitations, ethics, and appendices | Method, reported metrics, boundary conditions, and safety scope | High for source reporting | No independent rerun; small persona samples |
| E2 | S1, S2, S3 | Primary/public publication records | Title, authors, dates, versions, venue, pages, DOI, and public code locator | Work identity and publication context | High | ACL v2 and arXiv v1 are distinct versions |
| E3 | S1 | Primary paper | Stage 1 fixed behaviors, three Interpreter/Diagnostician backbones, 15 CharacterRAG and 15 sampled AnnaAgent personas, four target families | Evaluation design and sample boundary | High | Simulated agents are not human participants; task subsets are small |
| E4 | S1 | Primary paper | Questionnaire and GenPT reliability/validity tables, DCR, weighted kappa, longitudinal shifts, and exact-match/Hamming metrics | Main reported findings | High for transcription; medium for interpretation | Values are author-reported and backbone-dependent |
| E5 | S4 | Official implementation | Pipeline layout, stimuli, scripts, metrics, dependencies, and AnnaAgent data exclusion note | Implementation availability and reproducibility boundary | High for observed repository state | No execution, dependency install, model run, or dataset collection |
| E6 | S5–S7 | Related DEP manuscripts | State traces, reliability gates, evidence validation, judge uncertainty, human comparison, and reproduction limits | Cross-DEP synthesis and safer translation | Medium | Related artifacts are not independent validation of GenPT |

## Executive Summary

GenPT is a source-grounded proposal for evaluating persona-conditioned LLM agents through projective rather than direct self-report tasks. It collects free-form behavior from TAT-like images, Rorschach-style cards, and sentence stems; an LLM Interpreter produces structured psychological indicators; and a Diagnostician maps those indicators to trait or risk labels (E1, E3).

The paper's strongest reported result is a reliability contrast under social-desirability framing: the questionnaire baseline shows pronounced downward directional consistency on suicide ideation, while no tested GenPT backbone simultaneously shows high agreement and the same fake-good drift signature. Its longitudinal result is more conditional: Qwen3-8B shows a reported depression shift of 0.80 versus 0.08 for the questionnaire, but Phi-4-mini and Intern-S1 are much closer to the baseline (E4).

The evidence supports a complementary, offline research instrument rather than a clinical or person-profiling product. Personality validity favors the questionnaire baseline, the risk-task sample is only fifteen personas per evaluation subset, the effect varies by backbone, and no independently reproduced experiment was performed (E1, E4, E5). Confidence is therefore medium-high for the mechanism and reported table values, and medium for generalization.

## Detailed Summary

### Problem Context

The paper argues that direct questionnaires applied to LLM agents may be contaminated by training exposure and distorted by social-desirability or context framing. A direct item can make the assessment intent obvious, inviting aligned or role-conforming answers. GenPT instead uses ambiguous prompts whose target construct is hidden from the Examinee, while keeping the downstream scoring pipeline inspectable (E1).

The research object is a persona-conditioned agent, not a human participant. A persona supplies the intended state for evaluation, and the system asks whether agent behavior can recover that state under controlled conditions. This framing makes the work an evaluation of simulated-agent behavior, not evidence about intrinsic model psychology or human mental health.

### GenPT Mechanism

The pipeline has three stages:

- **Examinee / Behavior Collection**: the persona-conditioned model produces stories for eight TAT-like images, descriptions and inquiries for ten Rorschach-style cards, and completions for twenty sentence stems.
- **Interpreter**: a model scores TAT narratives on eight SCORS-G dimensions, converts Rorschach utterances into four simplified Rorschach domains using 22 text-verifiable variables, and scores sentence completions into five adjustment domains.
- **Diagnostician**: a task-specific prompt maps the combined indicators and explanations to five Big Five levels, four MBTI axes, or 0–3 depression and suicide-risk levels.

The design holds Stage 1 outputs and prompts fixed while comparing Qwen3-8B, Phi-4-mini-reasoning, and Intern-S1-mini as Interpreter/Diagnostician backbones. The paper uses fifteen CharacterRAG fictional characters for personality assessment and fifteen sampled AnnaAgent profiles for risk tasks, with separate reliability and validity subsets drawn from the underlying dialogue-profile pool (E1, E3).

### Experimental Logic

Personality traits are treated as relatively stable: the desired behavior is stable output under neutral, job-interview, counselling, and prolonged-context perturbations. Depression and suicide risk are treated as state-like: the desired behavior is resistance to social-desirability framing but responsiveness to meaningful counselling context. The paper operationalizes these expectations with linearly weighted Cohen's kappa and Directional Consistency Ratio (DCR), then evaluates criterion validity with exact-match accuracy for ordinal labels and Hamming distance for MBTI (E1, E4).

### Reported Results

The social-desirability table reports questionnaire suicide DCR of 0.71 under job framing and 0.88 under clinical framing, with high kappa values. GenPT's risk-task kappa values are low or negative in several cells, but the paper argues that no backbone shows the combined high-kappa, high-directional fake-good pattern. On personality tasks, GenPT has lower kappa than the questionnaire and similar mild one-sided drift.

For longitudinal context, Qwen3-8B produces absolute mean shifts of 0.80 for depression and 0.20 for suicide, versus 0.08 and 0.10 for the questionnaire. Intern-S1 produces 0.07 and 0.13, while Phi-4-mini produces 0.00 and 0.07. This spread shows that context responsiveness is not a property of the stimulus protocol alone; it depends on the Interpreter/Diagnostician backbone.

Criterion validity is mixed. The questionnaire scores 0.373 on Big Five and 0.733 mean MBTI Hamming distance, compared with GenPT Big Five scores of 0.333, 0.240, and 0.293 and MBTI Hamming distances of 1.200, 2.200, and 1.667 for Qwen3, Phi-4, and Intern-S1. On depression, GenPT scores 0.200, 0.400, and 0.400 versus 0.133 for the questionnaire. On suicide, Qwen3 reaches 0.400 versus 0.200, Phi-4 0.267, and Intern-S1 0.067 (E4).

### Limitations and Ethics

The authors identify limited backbone and cultural coverage and higher computational cost than direct questionnaires. The review adds that exact-match values on fifteen-persona subsets are fragile, and a low kappa may reflect sparse labels or instability rather than useful non-bias. The paper states that the work uses simulated agents rather than human subjects, requests research-only use, and warns against clinical deployment without validation and professional oversight (E1).

The mental-health framing is dual-use. A safe implementation must not infer mental states of real people, expose private dialogue, or make clinical, employment, insurance, or access decisions. Projective outputs should remain review evidence with explicit uncertainty, not hidden profiling features.

### Implementation Availability

The official GenPT repository exposes a core package, generated stimuli, CharacterRAG data, questionnaires, scripts, metrics, and a `pyproject.toml`. It states that AnnaAgent data is not included because it contains real help-seeker conversations, and the reproduction commands require local model serving and substantial dependencies. This supports inspectability and a bounded reproduction path, but not end-to-end reproducibility in this run (E5).

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | GenPT provides an explicit Examinee → Interpreter → Diagnostician assessment pipeline over generated projective stimuli. | Author claim, directly supported | E1, E3 | The stages, inputs, intermediate scores, and outputs are specified in the inspected full paper. | High |
| C2 | Direct questionnaires show systematic social-desirability drift, most visibly on suicide ideation, in the tested setup. | Author empirical claim | E1, E4 | Tables directly report the DCR/kappa pattern, but the conclusion is bounded by the sampled personas and prompts. | Medium-high |
| C3 | GenPT avoids the questionnaire's combined high-agreement fake-good signature on tested risk-task cells. | Author claim with reviewer qualification | E1, E4 | Supported within the paper's diagnostic regime; low or negative kappa in several GenPT cells means absence of that signature is not equivalent to reliable measurement. | Medium |
| C4 | Qwen3-8B shows substantially larger longitudinal depression movement than the questionnaire baseline. | Author empirical claim | E1, E4 | The reported 0.80 versus 0.08 shift is clear; other backbones do not reproduce the same magnitude. | Medium |
| C5 | GenPT is weaker than questionnaires on the paper's clean-persona personality tasks. | Author claim and reviewer interpretation | E1, E4 | Big Five accuracy and MBTI Hamming results support complementarity rather than replacement. | High for this setup |
| C6 | The study supports evaluation of simulated persona recovery, not clinical psychometrics or intrinsic model psychology. | Reviewer interpretation grounded in scope | E1, E3 | The Examinee is a persona-conditioned model and the ethics section rejects clinical deployment without validation. | High |
| C7 | The official repository improves inspectability but does not establish reproducibility. | Reviewer implementation observation | E5 | Code and public stimuli are visible, while AnnaAgent data, model services, and exact run outputs are not fully available in this review. | High |
| C8 | Safe downstream use requires behavior provenance, calibration, abstention, and independent review. | Reviewer synthesis | E5, E6, E7 | Related DEP evidence supports the governance pattern; no joint GenPT experiment was run. | Medium-high |

## Methodology

- `Research objective`: Preserve and critically translate a complete-paper review of GenPT into a reusable DEP-E artifact for offline agent evaluation and safety planning.
- `Sources inspected`: Verified local arXiv v1 PDF/full-paper HTML/metadata HTML; public arXiv HTML and metadata; ACL Anthology v2 record; official GenPT repository README and `pyproject.toml`; live Black Lake and Black-Lake-Data READMEs; and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Enumerate local PDF candidates with `rg --files -g "*.pdf"`; collapse each PDF parent directory into one paper unit; derive modern arXiv IDs; reconcile IDs and title/slug signals against repository artifacts and automation memory; inspect the selected unit's adjacent metadata; repair missing full-paper HTML through the bounded approved collector; inspect full-paper sections and tables; inspect public publication and code records; and match exactly three related DEP entries by concrete conceptual overlap.
- `Inclusion criteria`: Primary-paper identity, full-paper method, evaluation design, reported results, limitations, ethics, implementation availability, repository governance, source integrity, and related evidence about evaluation reliability or state inspection.
- `Exclusion criteria`: Previously deposited papers, same-paper 24-hour markers, identifier-incomplete units, abstract-only evidence for method/results claims, source-file redistribution, unexecuted code claims, and clinical or person-level deployment claims.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, replication, and provenance analysis.
- `Evidence handling`: Evidence IDs separate direct primary-source reporting, public publication context, implementation inspection, related DEP synthesis, and reviewer interpretation. Quantitative results are retained with task, baseline, backbone, and sample context.
- `Uncertainty handling`: Version differences, small persona subsets, missing AnnaAgent data, unexecuted code, backbone dependence, and the distinction between non-directional drift and reliable measurement remain explicit.
- `Source-integrity methodology`: The selected unit was initially partial because full-paper HTML was missing. The valid PDF was preserved; official full-paper HTML was acquired by a bounded repair; PDF header/EOF and HTML size/body/marker/heading/structure checks passed; metadata, provenance, machine summary, receipt, and verification records were refreshed; no partial files remain.
- `Random selection`: 75,967 PDFs, 75,964 unique PDF-parent units, 187 identifier-incomplete units, 1,937 prior-ID exclusions, and 73,840 eligible units were recorded. The sorted eligible pool was sampled uniformly with PowerShell `Get-Random` at zero-based index 660.
- `Dedup/reselection validation`: Exact arXiv ID `2606.00860`, arXiv DOI, normalized title, GenPT slug, Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, relevant Black-Lake-Data searches, and same-paper markers within the preceding 24 hours were checked. No owning record was found; duplicate exclusions and reselections were zero.
- `Version control`: The primary source is arXiv v1; ACL Anthology v2 is recorded as publication context; the official repository was inspected at its current default-branch state without claiming a pinned experiment commit.
- `Safety handling`: Examples are synthetic, offline, local-only, non-clinical, and review-only. No human profiling, clinical diagnosis, real help-seeker data, private credentials, or consequential automation is proposed.
- `Reviewer stance`: Critical paper review, DEP-ready preservation, implementation translation, safe evaluation planning, and replication-boundary analysis.

## Scope, Constraints, and Assumptions

- `Scope`: GenPT's problem framing, three-stage mechanism, stimuli, scoring, experimental design, reported reliability and validity results, official implementation context, limitations, ethics, and bounded downstream uses.
- `Temporal boundary`: Sources and repository records inspected on 2026-08-20; arXiv v1 submitted 2026-05-30; ACL version 2 published July 2026.
- `Evidence limits`: No model inference, API call, dataset download, source-package redistribution, code execution, human annotation, clinical validation, statistical recomputation, or independent reproduction was performed.
- `Assumptions`: The verified local PDF and full-paper HTML represent arXiv:2606.00860v1; ACL Anthology's record represents the related version 2; the paper-linked GitHub repository is the official implementation because the paper and ACL record link to it.
- `Constraints`: Public artifacts cannot disclose local paths, usernames, machine identifiers, local timezone labels, exact local execution times, original source files, private dialogue data, or credentials. Mental-health content is discussed only for simulated agents and safe evaluation.
- `Out of scope`: Human diagnosis, profiling, employment or insurance decisions, clinical deployment, user surveillance, autonomous risk action, claims about intrinsic model consciousness, and redistribution of copyrighted or sensitive source materials.
- `Intended use`: Black Lake DEP-E preservation, research review, safety evaluation planning, and bounded replication design.
- `Audience`: Agent-evaluation researchers, safety reviewers, ML engineers, benchmark maintainers, and governance stakeholders.
- `Reproducibility boundary`: The public paper and repository define a plausible reproduction path, but a full rerun requires model services, dependencies, exact prompts, and governed persona data that were not collected or executed here.
- `Data sensitivity`: Public scholarly records plus synthetic/persona research context; the source archive includes private local copies that are not part of the public artifact.

## Observations

- `Observed pattern`: GenPT's useful unit of evidence is not the final label alone; it is the chain from stimulus to behavior to rubric score to diagnosis.
- `Technical implication`: Social-desirability resistance and longitudinal responsiveness should be tested as separate perturbation axes because a system can be stable under framing yet inert under meaningful context.
- `Contradiction or tension`: The paper describes low kappa on some GenPT risk cells as compatible with non-directional drift, but low agreement can also reflect noise or sparse support; a gate must keep both interpretations visible.
- `Cross-source pattern`: Agent State Review, Agent Reliability Gates, and OMGEval all favor inspectable intermediate evidence, explicit uncertainty, and bounded claims over single aggregate scores.
- `Open question`: Which calibration and abstention policy can distinguish useful sensitivity from backbone-specific narrative variance without importing clinical assumptions?
- `Reviewer hypothesis`: The most transferable contribution is an evidence-preserving evaluation protocol for simulated agents, not a standalone psychometric test.

## Considerations

- **Safety and ethics**: The mental-health labels are high-risk constructs. Any implementation must use fictional or explicitly authorized synthetic personas, prohibit inference about real people, and require human review before interpretation is reused.
- **Measurement validity**: Generated stimuli may reduce exposure to classical instruments but do not prove zero contamination or construct equivalence. New stimuli, rubrics, and prompt templates need independent audit.
- **Calibration and abstention**: The system should emit uncertainty, missing-evidence states, and abstentions when scores are unstable, conflicting, or out of distribution.
- **Reproducibility and cost**: Multi-turn behavior collection plus interpretation and diagnosis costs more than direct questionnaires; model versions, prompts, decoding settings, and source hashes must be recorded.
- **Data governance**: AnnaAgent data is not included in the official repository because it contains real help-seeker conversations. Public artifacts must not recreate or expose that data.
- **Operational boundary**: A dashboard may support research review, but no output should trigger clinical, employment, insurance, moderation, or access decisions.

## Strengths

- Separates behavior collection, interpretation, and diagnosis, making the measurement chain inspectable.
- Tests both invariance to social framing and responsiveness to longitudinal context instead of treating reliability as one scalar.
- Reports an explicit complementary result: questionnaire strength on clean traits and GenPT strength in some risk-task conditions.
- Provides public code/stimulus structure and a reproducibility boundary rather than implying that repository presence equals reproduced results.
- States ethics, computational cost, backbone coverage, and non-clinical intent in the primary paper.

## Weaknesses

- Validity and reliability are estimated on small persona subsets, making exact-match differences and kappa values fragile.
- The strongest longitudinal result is concentrated in Qwen3-8B and does not generalize uniformly to Phi-4-mini or Intern-S1.
- Simulated persona recovery is not evidence of intrinsic model psychology, human psychological validity, or clinical utility.
- The evaluation does not establish independent human or multi-judge validation for all intermediate scores and final labels.
- The public repository omits AnnaAgent source data and does not, by itself, provide a complete reproducible release with outputs and environment pinning.
- Cultural and multilingual coverage is limited, and the generated stimuli/rubrics may encode the authors' cultural or theoretical assumptions.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Expand persona panels and report confidence intervals | Empirical validity | Fifteen-persona subsets make exact-match gains unstable | Better uncertainty and power | More governed data and compute | Preregistered stratified evaluation with bootstrap intervals |
| Add independent interpreters and blinded human audits | Measurement validity | One backbone can carry shared bias from interpretation to diagnosis | Detect rubric and judge dependence | Annotation cost and rater disagreement | Inter-rater agreement, blinded adjudication, and calibration analysis |
| Add explicit abstention and out-of-distribution checks | Safety | Low agreement should not become an overconfident label | Safer failure behavior | Coverage reduction and policy design | Selective-risk curves and refusal-quality tests on synthetic shifts |
| Compare multiple stimulus-generation recipes and cultures | Construct validity | New stimuli are not automatically contamination-free or equivalent | Test robustness and cultural transfer | New review and licensing work | Held-out stimuli, contamination probes, and locale-specific review |
| Release a reproducible evaluation manifest | Reproduction | Repository layout alone does not pin models, prompts, outputs, and seeds | Lower replication ambiguity | Storage and source-governance burden | Clean-room rerun of public CharacterRAG-only subset |

## Potential Implementations

1. **Offline synthetic-persona evaluator**
   - `User`: Agent-evaluation researcher.
   - `Goal`: Compare projective and self-report-like probes on fictional personas.
   - `Core mechanism`: Freeze stimuli and Stage 1 behavior, run multiple interpreters/diagnosticians, and emit paired condition records.
   - `Required inputs`: Public or synthetic persona profiles, generated stimuli, versioned prompts, model endpoints, and an evidence schema.
   - `Outputs`: Behavior traces, structured scores, labels, uncertainty, and a review-only report.
   - `Risk controls`: No real people, no private help-seeker data, no clinical labels in production, abstention on missing evidence, and local-only storage.
   - `Evaluation`: Repeated seeds, backbone swaps, perturbation matrices, calibration, and reviewer agreement.

2. **Perturbation reliability gate**
   - `User`: Safety or benchmark reviewer.
   - `Goal`: Detect framing-induced drift without suppressing meaningful context response.
   - `Core mechanism`: Compare neutral, social-framing, and long-context conditions with paired kappa/DCR, accuracy, coverage, and abstention metrics.
   - `Required inputs`: Frozen paired predictions, condition metadata, task semantics, and expected direction rules.
   - `Outputs`: Gate decision, drift classification, uncertainty, and human-review queue.
   - `Risk controls`: Review-only status, no automatic intervention, no person-level inference, and explicit low-support warnings.
   - `Evaluation`: Synthetic shift tests, known-noise controls, and independent audit of selected cases.

3. **Evidence-bound research dashboard**
   - `User`: Research lead or governance reviewer.
   - `Goal`: Make every label traceable to behavior, rubric, model version, and source.
   - `Core mechanism`: Local evidence store plus provenance-preserving visual views of stimulus, response, score, explanation, uncertainty, and decision.
   - `Required inputs`: Structured JSON/Markdown records, public source URLs, and reviewer annotations.
   - `Outputs`: Reproducible review packets and gap reports.
   - `Risk controls`: Local-only processing, access control, redaction, no raw sensitive dialogue, immutable source references, and manual publication gate.
   - `Evaluation`: Trace completeness, second-reviewer reconstruction, redaction checks, and schema validation.

## Three Ways to Exercise This Research

1. **Synthetic perturbation smoke test**: Create five fictional personas and fixed text-only stimuli; compare neutral versus job-framing versus counselling-framing prompts; record output hashes, ordinal labels, DCR, and abstentions; success means the ledger is complete and no result is used for a real-person decision; stop if any private or human-derived data enters the run.
2. **Interpreter agreement audit**: Use the same synthetic behavior traces with two independent rubric prompts and one human reviewer; compare score agreement, missing fields, and explanation overlap; success means disagreement is visible and routed to review; stop if a model output is treated as clinical truth.
3. **Evidence-gated reproduction slice**: Run only the public CharacterRAG-style slice with a pinned small model or deterministic stub; reproduce the data-flow and metric calculations without claiming paper-level performance; success means a second reviewer can reconstruct every output from the manifest; stop when dependencies, model weights, or licensing cannot be verified.

## Example MVP Product

- `Product name`: Persona Evidence Gate.
- `Target user`: Agent-evaluation engineer or safety reviewer.
- `Problem`: Multi-stage agent assessments can hide prompt, model, provenance, and uncertainty changes behind one final label.
- `Core workflow`: Load fictional personas and frozen stimuli, collect behavior, run versioned interpreters, compute paired perturbation metrics, attach source/evidence IDs, and route unstable cases to human review.
- `Data requirements`: Synthetic or authorized persona profiles, public-safe stimuli, model/version manifest, prompt templates, expected condition semantics, and reviewer decisions.
- `Architecture`: Local evidence store, deterministic schema validator, model adapter, paired-condition evaluator, calibration/abstention gate, and Markdown report generator.
- `Success metrics`: Trace completeness, rerun determinism, calibration error, abstention precision, reviewer reconstruction time, and zero leakage of restricted inputs.
- `Risk controls`: Local-only mode, no credentials in logs, no real-person profiling, no clinical or consequential decisions, explicit uncertainty, redaction, audit trail, and manual export approval.
- `Limitations`: It cannot establish psychometric validity, replace professional assessment, or remove backbone/cultural bias by itself.
- `MVP boundary`: Offline research review only; no hosted user profiling, no clinical workflow, no automated intervention, and no ingestion of real help-seeker conversations.
- `Evaluation plan`: Schema tests, synthetic perturbation controls, two-reviewer trace audits, model/version drift checks, and safe-failure tests.
- `Failure modes`: Missing evidence, prompt leakage, unstable interpreters, distribution shift, overconfident labels, and reviewer misinterpretation of simulated-agent results.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| GenPT ACL publication | Primary publication | Published version, abstract, DOI, and official code link | [ACL Anthology](https://aclanthology.org/2026.acl-long.1901/) |
| GenPT repository | Official implementation | Pipeline, stimuli, metrics, scripts, dependencies, and data boundary | [GitHub](https://github.com/sci-m-wang/GenPT) |
| Large Language Model Psychometrics: A Systematic Review | Primary contextual review | Broader validation, evaluation, and enhancement context cited by the paper | [arXiv:2505.08245](https://arxiv.org/abs/2505.08245) |
| InCharacter | Methodological neighbor | Psychological-interview evaluation of role-playing agents | [ACL Anthology search context](https://aclanthology.org/) |
| AnnaAgent | Dataset/system context | Dialogue-grounded simulated mental-health profiles referenced by GenPT; source data requires governance | [ACL Anthology search context](https://aclanthology.org/) |
| Agent State Review | Related DEP | Stateful evidence traces and runtime monitoring | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` |
| Agent Reliability Gates | Related DEP | Calibration, rejection, and evidence validation | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` |
| OMGEval Benchmark | Related DEP | Judge uncertainty, human comparison, and reproduction boundary | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2606.00860 | E1–E3; identity, abstract, authors, version, and public metadata | 2026-08-20 | Metadata page; abstract alone is not used for method/results claims |
| R2 | https://arxiv.org/html/2606.00860 | E1, E3, E4; full method, tables, limitations, ethics, and appendices | 2026-08-20 | Public full-paper HTML cross-check |
| R3 | https://arxiv.org/pdf/2606.00860 | E1; primary PDF integrity and page-level source | 2026-08-20 | Verified local copy withheld from public output |
| R4 | https://doi.org/10.48550/arXiv.2606.00860 | E2; stable arXiv DOI | 2026-08-20 | Identifier locator |
| R5 | https://aclanthology.org/2026.acl-long.1901/ | E2; publication venue, version 2, pages, and DOI | 2026-08-20 | ACL record |
| R6 | https://doi.org/10.18653/v1/2026.acl-long.1901 | E2; published DOI | 2026-08-20 | Identifier locator |
| R7 | https://github.com/sci-m-wang/GenPT | E5; implementation and stimulus availability | 2026-08-20 | Official paper-linked repository |
| R8 | https://github.com/sci-m-wang/GenPT/blob/main/pyproject.toml | E5; dependency and package metadata | 2026-08-20 | Official repository file |
| R9 | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | E6; state traces, evidence replay, and runtime monitoring | 2026-08-20 | Repository-relative related artifact |
| R10 | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` | E6; calibration, rejection, evidence gates, and intervention limits | 2026-08-20 | Repository-relative related artifact |
| R11 | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` | E6; judge uncertainty, human comparison, and reproducibility limits | 2026-08-20 | Repository-relative related artifact |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Deposition rules and source-locality boundary | 2026-08-20 | Live README inspected before writing |
| R13 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion provenance and source-deposition rules | 2026-08-20 | Live README inspected before writing |

## Appendix

### Validation and Distribution Record

- **Selection**: The selected unit was drawn uniformly from a sorted eligible parent-unit pool after `rg --files -g "*.pdf"` enumeration and ownership-oriented deduplication.
- **Source integrity**: Initial partial state was repaired before review. PDF and full-paper HTML passed the required integrity thresholds; metadata, provenance, summary, receipt, and verification records were refreshed; no partial files remain.
- **Deduplication**: Exact ID, DOI, normalized title, slug, Black Lake artifacts, automation memory, Black-Lake-Data search results, and same-paper 24-hour markers were checked; no prior owning deposit was found.
- **Public allowlist**: The intended staged set is this manuscript, its DEP README, the job log, the Report-Mark, and the DEP-E publication-index row. Original PDF, HTML, source package, caches, extracted text, private provenance, and local archive paths are excluded.
- **Source files**: No original source file is deposited; all source documents remain local-only.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.00860
  - Applies to: identity, authors, abstract, version, and metadata.
- Source URL: https://arxiv.org/html/2606.00860
  - Applies to: method, scoring, experiments, tables, limitations, ethics, and appendices.
- Source URL: https://aclanthology.org/2026.acl-long.1901/
  - Applies to: ACL publication context, version 2, venue, pages, and DOI.
- Source URL: https://github.com/sci-m-wang/GenPT
  - Applies to: official implementation, stimuli, dependencies, and reproducibility boundary.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: public DEP filing, index maintenance, and source-locality requirements.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion repository provenance and source-deposition requirements.
- Source files: none deposited; original source files remain withheld locally.
