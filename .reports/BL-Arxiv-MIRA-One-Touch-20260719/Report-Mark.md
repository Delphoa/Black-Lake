# Report-Mark: MIRA One-Touch Routing

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P05`
- Review date: 2026-07-19
- Review type: source-first multimodal recommendation and mobile deployment synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *MIRA: Empowering One-Touch AI Services on Smartphones with MLLM-based Instruction Recommendation* |
| Authors | Zhipeng Bian; Jieming Zhu; Xuyang Xie; Quanyu Dai; Zhou Zhao; Zhenhua Dong |
| Stable identifier | arXiv:2509.13773v1 |
| Submission history | Submitted 2025-09-17 |
| DOI | https://doi.org/10.48550/arXiv.2509.13773 |
| Primary record | https://arxiv.org/abs/2509.13773 |
| Full-paper HTML | https://arxiv.org/html/2509.13773 |
| PDF | https://arxiv.org/pdf/2509.13773 |
| Source state | Verified complete after bounded repair; all source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P05` |

## Concise Research Notes

### Problem

Predefined smartphone AI services are difficult to discover and invoke from the object a user is currently viewing. The paper frames instruction recommendation as mapping a long-pressed image or text object to one or more valid, context-relevant actions.

### Method

MIRA combines three layers. A supervised multimodal model emits a structured trace that extracts entities, links them to likely intent, and proposes an instruction. A library of about 80 high-level reasoning templates is retrieved by embedding similarity to refine that trace. After the reasoning delimiter, a tokenizer-aligned prefix tree masks invalid next tokens so the final instruction must belong to the predefined action library.

### Evidence

The authors report 4,952 training pairs and 956 test pairs, collected from 1,000 smartphone users with at least three annotations per sample and inter-annotator agreement of kappa 0.85. Across four InternVL2.5 and Qwen2.5VL model sizes, MIRA exceeds zero-shot and vanilla SFT baselines. The reported Qwen2.5VL-7B point has F1 0.9121 and HR@3 0.9629. Template augmentation raises reported F1 by 15.8% to 24.1% relative to initial reasoning across the four models. A 100-participant study over 500 trigger objects reports validity ratios of 93% and 95% for two model variants.

### Limits

The baselines do not include sequence recommenders because the task definition differs. The study reports two-GPU experiments and model-level inference times, not a full on-device energy, memory, thermal, privacy, or end-to-end latency evaluation. The paper identifies text/image-only coverage, long-tail template gaps, retrieval misalignment, ambiguous triggers, sensitive content, and data quality as open issues. Performance and user-study results remain source-reported.

## Evidence and Attribution

| Claim | Source basis | Reviewer qualification |
|---|---|---|
| Structured reasoning, template retrieval, and prefix-constrained decoding form the pipeline. | Full-paper sections 3.1-3.3. | Architecture transcription; not an independent effectiveness result. |
| Qwen2.5VL-7B MIRA reports F1 0.9121 and HR@3 0.9629. | Table 1 and section 4.3.1. | Source-reported on the paper's task and split. |
| Template augmentation reports 15.8%-24.1% F1 gains. | Table 2 and section 4.3.2. | Useful ablation, but template construction uses a closed model and a fixed dataset. |
| Prefix constraints guarantee library membership. | Section 3.3. | They constrain syntax/candidate identity, not intent correctness or action safety. |
| Mobile readiness is not established by parameter count alone. | Tables 1-4 plus limitations. | Reviewer interpretation requiring device-level measurements and privacy controls. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - supplies a representation-audit perspective for multimodal models beyond end-task scores.
2. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - connects conditional routing to real runtime, batching, and stability constraints.
3. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - places model compression and edge serving inside an end-to-end resource lifecycle.

## Synthesis Note

### Concept Bridge

MIRA is best understood as a bounded action router: perception produces a task hypothesis, retrieval supplies a reusable reasoning scaffold, and a finite-state decoder restricts output to an approved vocabulary. The related deposits show what the paper does not close. VLM probing asks whether the representation actually contains the needed entities and relations; conditional-path evaluation asks whether dynamic routing remains stable and efficient under deployment load; the efficiency survey asks whether training, inference, memory, energy, privacy, and runtime compatibility are measured together. The combined design target is an auditable, confidence-aware mobile action recommender whose output is constrained twice: first by evidence quality and policy, then by an allowlisted instruction grammar.

### Potential Implementations

1. Build an offline trigger-to-action evaluator that slices F1, hit rate, abstention, and privacy risk by modality, intent ambiguity, and rare-entity category.
2. Add a policy-aware trie whose terminal actions carry permission scope, confirmation requirements, and data-retention labels.
3. Create a template registry with provenance, similarity diagnostics, drift monitoring, and human approval before new templates become active.

### Deeper Relationship Observations

1. Constrained decoding turns open generation into finite candidate selection, but the upstream representation and retrieval stages remain open-ended error sources.
2. A template library resembles a conditional-compute controller: both route an input to a specialized path and therefore need coverage, stability, and fallback tests.
3. Smaller parameter counts can improve deployability, yet device suitability is a systems property involving memory traffic, thermals, privacy, and interaction latency.

### Conceptual Similarities

1. MIRA and VLM probing both treat intermediate structure as measurable evidence rather than relying only on a final answer.
2. MIRA template retrieval and DMNN routing both select conditional pathways from input-dependent signals.
3. MIRA's edge-device motivation and the efficiency survey both require lifecycle-wide rather than model-only optimization.

### MVP Implementations with Code Mock-Ups

1. Policy-annotated instruction trie:

```python
def allowed_next(prefix, trie, grants):
    node = trie
    for token in prefix:
        node = node["children"].get(token)
        if node is None:
            return []
    return [t for t, child in node["children"].items()
            if child.get("permission", "none") in grants]
```

2. Template retrieval with an abstention band:

```python
def choose_template(scores, low=0.50, high=0.70):
    best_id, best = max(scores.items(), key=lambda item: item[1])
    if best < low:
        return {"route": "abstain", "score": best}
    return {"route": best_id, "score": best,
            "review": best < high}
```

3. Slice-aware evaluation record:

```python
def record_case(case, prediction, valid_actions):
    return {
        "modality": case["modality"],
        "intent_count": len(valid_actions),
        "correct": prediction in valid_actions,
        "abstained": prediction is None,
        "sensitive": case.get("sensitive", False),
    }
```

### Developer Challenges

1. Tokenizer changes can invalidate trie edges and require reproducible rebuilding, versioning, and regression tests.
2. Template embeddings can drift across model releases, altering routes even when the template text is unchanged.
3. Device measurements must include UI capture, model execution, network calls, memory pressure, and thermal throttling rather than isolated model latency.

### Author Challenges

1. Establish generalization on new users, languages, devices, and long-tail tasks without leaking private trigger content.
2. Compare against stronger retrieval and finite-candidate classification baselines under equal compute and annotation budgets.
3. Demonstrate that user-study preference and offline metrics predict safe, useful actions in prospective deployment.

## Validation Notes

- Random method: uniform index 11,296 of 75,776 unique PDF-parent units from 75,778 PDFs; first draw.
- Dedup: no arXiv ID, DOI, normalized-title, slug, prior cron, 24-hour, or current-job collision; 0 exclusions and 0 reselections.
- Integrity: partial-to-complete repair in one bounded attempt; verified PDF and official full-paper HTML; cache status `cached`; no partials.
- Structure: all required Report-Mark sections are present; the synthesis has exactly three items in each mandated category and three syntax-checked Python mock-ups.
- Safety: proposed actions are offline or confirmation-gated; source claims are separated from reviewer interpretation.
- Public-safety: no local paths, exact local timestamps, timezone labels, machine names, or user identifiers are disclosed.
- Source locality: no PDF, HTML, extracted text, metadata file, cache, or other original source was uploaded.

## Attribution Block

- https://arxiv.org/abs/2509.13773 - canonical metadata, authorship, abstract, identifier, and submission history.
- https://arxiv.org/html/2509.13773 - primary full-paper evidence for method, experiments, tables, limitations, and references.
- https://arxiv.org/pdf/2509.13773 - independently validated complete paper rendering; withheld locally.
- https://doi.org/10.48550/arXiv.2509.13773 - persistent identifier.
- `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - related multimodal evaluation context.
- `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - related conditional routing context.
- `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - related resource-efficiency context.
- Source files: PDF, full-paper HTML, metadata HTML, extracted text, and cache records were inspected locally and withheld from the repository and Slack.
