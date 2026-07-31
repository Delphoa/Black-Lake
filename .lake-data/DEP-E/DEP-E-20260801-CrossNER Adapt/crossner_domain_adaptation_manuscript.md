---
title: "CrossNER - DEP-E"
generated_at: "2026-08-01"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of CrossNER, a low-resource cross-domain named entity recognition benchmark and domain-adaptive pre-training study."
source_status: "URLs only; complete local source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-01"
temporal_cutoff: "arXiv:2012.04373v2; public source access through 2026-08-01"
primary_url: "https://arxiv.org/abs/2012.04373"
stable_identifier: "arXiv:2012.04373v2; DOI:10.48550/arXiv.2012.04373"
confidence_summary: "High for source identity and transcription of inspected methods and tables; medium for transfer interpretation; low for independent reproducibility and deployment generalization."
safety_scope: "Offline research evaluation and nonbinding implementation planning"
distribution_notes: "Public URLs and derived Markdown only; local paper files, caches, extracted text, and repair records were withheld."
---

# CrossNER - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Canonical metadata | HTML | 2012.04373v2; revised 2020-12-13 | https://arxiv.org/abs/2012.04373 | Public metadata; arXiv terms apply | 2026-08-01 | Inspected |
| S2 | CrossNER paper | Primary artifact | PDF | v2; 14 pages; valid local PDF | https://arxiv.org/pdf/2012.04373 | Local copy withheld; public URL cited | 2026-08-01 | Integrity-verified and inspected |
| S3 | CrossNER paper | Primary artifact | Full-paper HTML | ar5iv rendering; valid local HTML | https://ar5iv.labs.arxiv.org/html/2012.04373 | Approved fallback; local copy withheld | 2026-08-01 | Integrity-verified and inspected |
| S4 | CrossNER paper | Official route attempt | Full-paper HTML | arXiv HTML endpoint | https://arxiv.org/html/2012.04373 | Returned 404 during bounded repair; not used as paper evidence | 2026-08-01 | Attempted |
| S5 | CrossNER repository | Official implementation and data locator | GitHub repository | Public default branch; no commit pin observed | https://github.com/zliucr/CrossNER | Repository license visible as MIT; dataset and third-party corpus rights require separate review | 2026-08-01 | README and inventory inspected |
| S6 | DoubleTransfer MEDIQA - DEP-E | Related processed artifact | Markdown manuscript | DEP-E-20260719 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-DoubleTransfer%20MEDIQA/doubletransfer_mediqa_manuscript.md | Synthesis context; primary source remains separately attributed | 2026-08-01 | Inspected |
| S7 | Dataset Baselines - DEP-E | Related processed artifact | Markdown manuscript | DEP-E-20260721 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Dataset%20Baselines/dataset_baselines_manuscript.md | Synthesis context; primary source remains separately attributed | 2026-08-01 | Inspected |
| S8 | OMGEval Benchmark - DEP-E | Related processed artifact | Markdown manuscript | DEP-E-20260717 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md | Synthesis context; primary source remains separately attributed | 2026-08-01 | Inspected |
| S9 | Repository governance | Deposition authority | Markdown | Live default branches | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository rules | 2026-08-01 | Inspected live |
| S10 | DEP filing rules | Deposition authority | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-08-01 | Inspected live |

Paper title: *CrossNER: Evaluating Cross-Domain Named Entity Recognition*.

Authors: Zihan Liu, Yan Xu, Tiezheng Yu, Wenliang Dai, Ziwei Ji, Samuel Cahyawijaya, Andrea Madotto, and Pascale Fung.

Publication context: the arXiv record states that the work was accepted in AAAI-2021. The arXiv record reports submission on 2020-12-08 and revision to v2 on 2020-12-13.

Source locality: a valid PDF, a valid full-paper HTML rendering, metadata HTML, and repair/verification records were inspected privately. The source package was unavailable. No source file, cache, extracted text, or local filesystem path is redistributed by this manuscript.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Canonical paper metadata | Title, authors, dates, subjects, venue status, abstract, DOI, and code/data locator | Identity and publication context | High | Metadata does not establish empirical claims |
| E2 | S2-S3 | Primary full paper | Introduction, dataset construction, adaptation settings, masking methods, tables, analysis, and conclusion | Method, data, reported results, and source-disclosed limitations | High for source reporting | Experiments were not independently rerun |
| E3 | S2-S3, Tables 1-3 | Primary empirical evidence | Domain sizes, labeled split sizes, corpus variants, F1 values, and masking comparisons | Benchmark composition and performance claims | High for transcription | No confidence intervals or independent reproduction |
| E4 | S2-S3, Sections on annotation and error analysis | Primary dataset evidence | Human annotation workflow, pre-annotation, label hierarchy, and specialized-label confusion | Data quality and failure interpretation | High for source reporting | Inter-annotator agreement and item-level audit are not reported |
| E5 | S5 | Official repository evidence | Dataset/code inventory, commands, historical dependency versions, and license visibility | Artifact availability and implementation boundary | Medium-high | Current repository is not a pinned 2020 environment |
| E6 | S6-S8 | Related DEP evidence | Transfer, dataset/baseline governance, multilingual benchmark slicing, and evaluator controls | Cross-DEP synthesis | Medium | Related artifacts do not validate CrossNER |
| E7 | Private process record | Selection and integrity evidence | Random draw, dedup scan, bounded repair, and complete-source verification | Eligibility and source-gate compliance | High | Local paths and exact execution times intentionally withheld |

## Executive Summary

CrossNER addresses a narrow but important evaluation problem: whether NER systems can transfer from a general source domain to specialized target domains with very little labeled target data. The work contributes a human-annotated benchmark over politics, natural science, music, literature, and artificial intelligence, plus five unlabeled domain-related corpora intended for domain-adaptive pre-training.

The benchmark combines general and domain-specialized entity categories. Target-domain training sets contain only 100 or 200 examples per domain, while development and test sets are larger. The paper evaluates direct target fine-tuning, source pre-training followed by target fine-tuning, and joint source/target training. Within DAPT, it compares domain-level, entity-level, task-level, and integrated corpora with token-level or span-level masking.

The strongest reported average in the main comparison is 69.63 F1 for source pre-training followed by target fine-tuning with the integrated corpus and span-level masking. The corresponding token-level integrated setup averages 68.29, while the cited prior baseline with DAPT averages 68.71. The paper reports that selecting content with plentiful or specialized entities can make smaller corpora competitive with larger domain corpora.

The evidence supports a benchmark and data-selection pattern, not a universal adaptation guarantee. The inspected paper is English-only, the target domains are uneven in corpus size, label hierarchies create semantic collisions, and independent reproduction was not performed. A practical successor should preserve source lineage, split manifests, label definitions, annotation disagreement, per-label uncertainty, and an abstention boundary.

## Detailed Summary

### Problem context

NER systems often learn from large general-domain corpora, but a target domain may use entity categories that are absent or semantically overloaded in the source domain. The paper uses the example of a generic person label versus a specialized artist label to make the problem concrete. Existing cross-domain benchmarks, as characterized by the authors, frequently use target data that is broad, near the source domain, or limited to general categories.

### CrossNER dataset

CrossNER covers five target domains: politics, natural science, music, literature, and artificial intelligence. Its entity labels are domain-specific as well as general. Examples in the paper include politician, election, political party, scientist, enzyme, protein, song, band, album, writer, book, field, algorithm, and metrics.

Each domain has a domain-related unlabeled corpus gathered from Wikipedia categories and subcategories. The corpus sizes differ sharply. Natural-science and music corpora are much larger than the artificial-intelligence corpus, so performance comparisons reflect both label difficulty and corpus availability.

The authors select 1,000 development and test examples per domain in the stated collection process, while Table 1 reports the final per-domain counts. Training uses 100 or 200 labeled examples per domain. The source domain is CoNLL-2003 English newswire with person, location, organization, and miscellaneous labels.

### Annotation process

The paper describes DBpedia Ontology and Wikipedia hyperlinks as pre-annotation aids. Two trained annotators label each sample, and an NER expert reviews the annotations and resolves disagreements. The source reports intermediate correction and modification rates, including that a substantial fraction of hyperlink-associated entities were corrected during annotation.

This workflow reduces labeling burden but also makes the ontology and pre-annotation source part of the benchmark’s measurement contract. A later benchmark cannot assume that a different ontology or annotation team will preserve the same label boundaries.

### Domain-adaptive pre-training

DAPT is applied before downstream NER fine-tuning. The domain-level corpus is the largest available corpus for a domain. The entity-level corpus retains sentences with plentiful entities. The task-level corpus retains sentences with domain-specialized entities. The integrated corpus combines entity-level and task-level material after upsampling the task-level component.

The masking comparison modifies BERT-style token masking so that isolated masked positions are moved toward adjacent masked positions, increasing the number of masked spans. The paper’s interpretation is that span prediction requires more context than predicting isolated tokens and may therefore improve domain understanding.

### Training settings and baselines

The method uses BERT representations and evaluates three settings: direct target-domain fine-tuning, source-domain pre-training followed by target fine-tuning, and joint source/target training. Baselines include BiLSTM-CRF, Coach, and prior cross-domain NER methods. Results are averaged over three runs in the main table, but the inspected source does not provide confidence intervals or a full seed manifest.

### Reported results

The main table reports the following relevant averages:

| Configuration | Masking | Corpus | Average F1 |
|---|---|---|---:|
| Direct target fine-tuning | None | BERT without DAPT | 61.44 |
| Source pre-training then target fine-tuning | None | BERT without DAPT | 64.89 |
| Source pre-training then target fine-tuning | Token-level | Integrated | 68.29 |
| Source pre-training then target fine-tuning | Span-level | Integrated | 69.63 |
| Prior baseline | Span-level plus integrated DAPT | Cited prior model | 68.71 |

The source reports that the span-level integrated configuration outperforms the same corpus with token-level masking by 1.34 average F1 points in the source-pre-training setting. It also reports that source training becomes more helpful as the target training set becomes very small.

### Failure cases and boundary conditions

The paper reports that source-domain training can hurt some specialized categories. In music, the generic person label can absorb artist instances, and the generic organization label can absorb band instances. The paper reports that 84.81% of person entities were misclassified as artist in the best model’s analysis. This is a source-reported error pattern, not an independently measured current-model statistic.

The benchmark is English-only and does not test multilingual transfer, cross-annotation transfer, contemporary large encoders, or domain adaptation under real operational latency and maintenance constraints. The artificial-intelligence corpus is much smaller than the other domain corpora, and Wikipedia/DBpedia coverage may reflect source-specific popularity and ontology bias.

### Implementation relevance

The practical pattern is a versioned adaptation harness rather than a direct prescription to use the 2020 BERT stack. A modern implementation should keep a manifest of corpus membership, labels, licenses, source and target splits, model versions, seeds, masking policy, and evaluation slices. It should compare content selection against corpus scale and should make specialized-label recall and calibrated abstention visible alongside macro and micro F1.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | CrossNER fills a cross-domain NER benchmark gap with specialized labels across five target domains. | Author contribution claim | E1, E2, E4 | Supported by the inspected dataset description and label tables. | High |
| C2 | Entity-focused and task-focused corpora can be more effective for DAPT than much larger domain-level corpora. | Author empirical claim | E2, E3 | Supported in the reported comparisons; independent transfer is untested. | Medium-high |
| C3 | Span-level masking improves the integrated corpus setup over token-level masking. | Author empirical claim | E2, E3 | The stated table difference is 1.34 average F1 in one setting; broader generalization is not established. | Medium-high |
| C4 | Source-domain training helps more when target labels are scarce. | Author analysis claim | E2, E3 | Consistent with reported curves and discussion; no current-model replication was run. | Medium |
| C5 | Specialized-label hierarchies expose errors hidden by aggregate NER scores. | Reviewer interpretation | E2, E4 | The paper’s artist/person and band/organization examples support this interpretation. | High |
| C6 | The benchmark design transfers unchanged to other languages and modern encoders. | Derived inference | E2, E4 | Rejected as unsupported; the inspected evidence is English-only and model-era specific. | High |
| C7 | A future adaptation system should pair corpus selection with provenance, split controls, and abstention. | Reviewer implementation synthesis | E2, E5, E6 | Reasonable downstream design guidance, not a source-tested result. | Medium |

## Methodology

- Research objective: preserve a source-grounded review of CrossNER and translate its benchmark and DAPT mechanisms into auditable, nonbinding implementation guidance.
- Sources inspected: the local verified PDF and full-paper HTML; local metadata and verification records; the official arXiv metadata page; the approved ar5iv full-paper rendering; the author-linked CrossNER repository; three related Black Lake DEP manuscripts; and the live Black Lake repository README and DEP README.
- Discovery strategy: enumerated local PDF candidates with rg --files -g "*.pdf"; treated each PDF parent directory as a paper unit; sorted unique units; made a uniform random draw; then searched repository-relative artifacts, automation memory, and both repositories for deduplication markers and related DEP context.
- Random selection: 75,960 PDF candidates collapsed to 75,957 unique parent-directory units. A fresh uniform PowerShell Get-Random draw over the sorted units selected zero-based index 42,378 and arXiv:2012.04373. An earlier helper failed before metadata acceptance while normalizing a path; it was discarded and not used as a manual selection.
- Inclusion criteria: the selected paper had to be a unique eligible unit, have a valid PDF and verified full-paper HTML, and have enough method, experiment, results, and limitation evidence for a full review. Related entries had to have concrete overlap with transfer, dataset/benchmark construction, or evaluation governance.
- Exclusion criteria: prior CrossNER markers, same-paper DOI/title/slug matches, same-paper markers within the public 24-hour cutoff, abstract-only or invalid documents, and source files as public outputs were excluded.
- Analytical approach: empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication-boundary analysis.
- Evidence handling: claims are labeled as author claims, source metadata, reviewer interpretation, derived inference, or implementation synthesis. Quantitative values are transcribed from the inspected table and paired with evidence IDs.
- Uncertainty handling: missing source package, absent independent rerun, unpinned current repository state, English-only coverage, uneven corpus sizes, and annotation/ontology uncertainties are stated rather than filled by inference.
- Source-integrity repair: the initial unit had a valid PDF but no full-paper HTML. A bounded single-paper repair attempted official arXiv HTML and PDF routes, then used the approved ar5iv fallback. The final PDF and full-paper HTML passed the required structural checks before review. Local README, attribution/provenance, machine summary, and verification records were updated.
- Deduplication validation: scanned Black Lake .logs, .reports, .lake-data, and .staging; the automation memory; and live GitHub searches in Black-Lake and Black-Lake-Data for arXiv ID, DOI, normalized title, and slug. Exclusions and reselections were both zero. The public 24-hour marker cutoff was 2026-07-31.
- Extraction process: inspected full-paper HTML structure and text, read the PDF content, cross-checked core metadata and results against the public ar5iv rendering, and inspected the official repository README. No code or experiment was executed.
- Version control: the reviewed paper is pinned to arXiv v2 and the cited public repository is identified by URL without inventing a commit pin. Related DEP paths are repository-relative and tied to their existing manuscript files.
- Safety handling: all implementation examples are synthetic, offline, auditable, and nonbinding. They do not process private or regulated data and do not make high-stakes decisions.
- Reviewer stance: DEP-ready paper review, comparative synthesis, implementation planning, and bounded replication analysis.

## Scope, Constraints, and Assumptions

- Scope: CrossNER’s benchmark design, annotation workflow, DAPT corpus-selection and masking mechanisms, reported NER results, limitations, implementation relevance, and synthesis with exactly three related DEP entries.
- Temporal boundary: arXiv:2012.04373v2 and public source access through 2026-08-01.
- Evidence limits: the source package was unavailable; the official arXiv HTML route returned 404; the public code repository was not pinned to a historical commit; experiments, metrics, and annotation quality were not independently reproduced.
- Assumptions: reported table values are transcribed as author-reported; the cited ar5iv rendering is treated as a full-text fallback because it passed the local structure gate; related DEP manuscripts are synthesis context rather than primary validation.
- Constraints: no source files may leave the private local archive; repository outputs must be public-safe Markdown; data and corpus redistribution rights require separate review; current dependencies may not reproduce the historical environment.
- Out of scope: independent retraining, benchmark redistribution, human annotation, current leaderboard claims, multilingual deployment, clinical or legal decision use, and any claim that benchmark gains prove production readiness.
- Intended use: research review, future benchmark design, offline implementation planning, replication backlog, and downstream DEP discovery.
- Audience: researchers, dataset maintainers, evaluation engineers, and reviewers of domain-adaptation systems.
- Reproducibility boundary: the method and many settings are described, but exact source membership, seeds, environment, final artifacts, and table-reproduction commands are not fully pinned by the inspected source set.
- Operational boundary: examples are illustrative and nonbinding; any real deployment requires authorized data, privacy review, license review, calibration, monitoring, and human oversight.
- Data sensitivity: public research metadata and public repository context; local source documents were private working material and were not redistributed.

## Observations

- Observed pattern: the integrated corpus is smaller than the domain-level corpus but reports the strongest average in the source-pretraining setting, suggesting that task-relevant content density is a useful variable alongside corpus size.
- Observed pattern: specialized label hierarchies create errors that aggregate F1 can conceal. A model may improve generic labels while collapsing a domain-specific label into its parent category.
- Technical implication: a benchmark that exposes domain shift should report per-domain and per-label results, confusion matrices, and label-hierarchy-aware metrics rather than one pooled score.
- Contradiction or tension: the benchmark aims to represent diverse target domains, but corpus sizes and ontology coverage are uneven, especially for artificial intelligence.
- Reviewer hypothesis: the DAPT selection pattern may generalize to evidence retrieval and evaluation pipelines, where relevance density can matter more than retaining every available document.
- Open question: whether span-level masking still improves transfer for current encoders when the domain corpus, tokenizer, and training objective are changed.

## Considerations

- Adoption: the dataset’s value depends on stable label definitions, auditable split manifests, and clear separation between source and target data.
- Data governance: Wikipedia, DBpedia, and derived corpora have distinct licensing and attribution obligations; a repository license does not automatically grant rights to every included corpus.
- Evaluation risk: three-run averages without confidence intervals can make small differences look decisive. Future reports should expose seed variance, paired tests, and per-slice uncertainty.
- Fairness and representativeness: English domain labels and Wikipedia-derived corpora may not represent all communities or writing styles within a domain.
- Security and privacy: NER systems can expose sensitive entities. Any deployment needs redaction policy, access control, retention limits, and audit logs.
- Maintenance: domain vocabularies, ontology mappings, models, and corpora drift. A benchmark refresh should preserve historical versions rather than silently overwrite them.
- Product boundary: benchmark scores may guide model selection, but they should not become unqualified proxies for people, institutions, clinical status, or other high-impact decisions.

## Strengths

1. The benchmark makes cross-domain transfer concrete through specialized entity categories rather than only changing document topics.
2. The paper varies corpus selection, masking, and source/target training order, providing more mechanism evidence than a single end-to-end comparison.
3. The annotation workflow combines pre-annotation aids with two annotators and expert review, making the intended quality-control path explicit.
4. The official repository exposes data and example commands, which lowers the barrier to bounded offline follow-up even though exact historical reproduction remains incomplete.

## Weaknesses

1. The inspected source is English-only, so multilingual transfer and cross-cultural label validity remain untested.
2. Corpus sizes, domain coverage, and specialized-label difficulty are uneven, complicating direct comparison across domains.
3. The paper does not provide a complete modern reproduction bundle with pinned environment, seeds, split manifests, checkpoints, and table-generation commands.
4. The ontology and Wikipedia collection process may encode coverage and popularity bias that is not captured by aggregate scores.
5. The reported label-hierarchy confusion indicates that source-domain pre-training can introduce systematic errors in specialized categories.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Versioned source, target, and corpus manifests | Reproducibility | Prevent silent data drift and leakage | Auditable reruns | Storage and maintenance overhead | Hash every input and verify split disjointness |
| Hierarchy-aware evaluation | Metrics | Generic labels can hide specialized-label collapse | Better diagnosis of transfer quality | More complex reporting | Report parent/child confusion, macro F1, calibration, and abstention |
| Multilingual and cross-ontology extension | Generalization | English and DBpedia coverage are narrow | Tests portability of the benchmark contract | Annotation and equivalence burden | Replicate label definitions with independent annotators and measure agreement |
| Seed and ablation uncertainty | Statistical validity | Three-run averages do not expose variability | More credible comparisons | More compute | Pre-register seeds, paired tests, and confidence intervals |
| License and provenance card | Governance | Corpus rights and source lineage differ | Safer redistribution and maintenance | Documentation effort | Audit every source and derived artifact before release |

## Potential Implementations

1. **Offline domain-adaptation lab:** run direct fine-tuning, source pre-training then target fine-tuning, and joint training on synthetic or authorized data with a frozen split manifest. Required outputs are per-domain F1, per-label confusion, calibration, and provenance. The risk control is a nonbinding, local-only boundary.
2. **Corpus relevance profiler:** score candidate unlabeled sentences by domain match, entity density, task relevance, license, and duplication status, then compare full-domain and selective corpora. The risk control is to retain the selection audit and never treat the profiler as a truth authority.
3. **Specialized-label review service:** expose NER predictions with parent/child label confidence, source spans, ontology version, and abstention rules. The risk control is human review for low-confidence or out-of-domain cases and no high-impact automated action.

## Three Ways to Exercise This Research

1. **Synthetic label-hierarchy test:** create a small synthetic corpus with parent and specialized entity labels; compare token-level and span-level masking or simple context models. Success means the intended label distinctions are measurable; stop if labels overlap ambiguously.
2. **Frozen transfer comparison:** use a public, authorized dataset pair with explicit source and target domains; run direct fine-tuning, source-then-target fine-tuning, and joint training under identical splits and seeds. Success means a reproducible comparison table; stop if split leakage or license status is unclear.
3. **Boundary and abstention study:** perturb domain vocabulary, label ontology, and target sample size; record specialized-label recall, calibration, and abstentions. Success means the operating envelope is visible; stop before connecting outputs to consequential decisions.

## Example MVP Product

- Product name: Domain Evidence NER Lab
- Target user: Researcher or evaluation engineer comparing domain-adaptation strategies.
- Problem: Aggregate NER scores do not show whether a model learned specialized target labels or merely retained generic source labels.
- Core workflow: Register a versioned source/target dataset pair, validate provenance and splits, select an adaptation corpus, train bounded candidate runs, evaluate per-domain and per-label metrics, and emit an evidence report with abstention conditions.
- Data requirements: Authorized token-labeled text, label ontology and hierarchy, source/corpus manifests, split hashes, model configuration, seeds, and license metadata.
- Architecture: Local manifest validator, corpus relevance profiler, training adapter, deterministic evaluator, calibration and shift checker, and Markdown evidence reporter.
- Success metrics: Reproducible run manifests, zero split leakage, macro F1 by domain, specialized-label recall, calibration error, and review utility under a declared threshold.
- Risk controls: Local-only processing for sensitive text, license checks, no raw text in public logs, human review for abstentions, immutable test splits, and explicit nonbinding output labels.
- Limitations: The MVP does not establish real-world generalization, multilingual validity, annotation fairness, or production readiness.
- MVP boundary: Synthetic or authorized public datasets only; no automated high-impact decisions and no source-file redistribution.
- Deployment model: Local CLI or notebook with Markdown output.
- Evaluation plan: Smoke tests for manifests and split disjointness, small synthetic mechanism tests, repeated-seed comparison, and manual review of specialized-label confusion.
- Failure modes: Ontology mismatch, leakage, stale corpora, unsupported language, label collapse, calibration drift, and misleading aggregate scores.
- Maintenance plan: Version the ontology, source manifests, model dependencies, evaluation thresholds, and benchmark revisions; preserve old runs for comparison.

## Related Research and Reading

### Selected related DEP entries

| Entry | Relationship | Public locator |
|---|---|---|
| DoubleTransfer MEDIQA - DEP-E | Multi-source transfer and low-resource medical NLU; useful for separating source complementarity, sampling, and distribution shift. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-DoubleTransfer%20MEDIQA/doubletransfer_mediqa_manuscript.md |
| Dataset Baselines - DEP-E | Dataset and baseline construction with explicit provenance, frozen splits, and benchmark/deployment boundaries. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Dataset%20Baselines/dataset_baselines_manuscript.md |
| OMGEval Benchmark - DEP-E | Multilingual and culturally localized benchmark slices; useful for measurement coverage and aggregate-score governance. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md |

### Primary and near-primary reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| CrossNER | Primary paper | Reviewed benchmark and DAPT method | https://arxiv.org/abs/2012.04373 |
| CrossNER repository | Official implementation and data locator | Dataset files, commands, dependency notes, and license context | https://github.com/zliucr/CrossNER |
| BERT | Foundational method | Base masked-language-model and NER fine-tuning lineage referenced by the paper | https://arxiv.org/abs/1810.04805 |
| Don’t Stop Pretraining | Methodological neighbor | Domain-adaptive and task-adaptive pre-training context | https://arxiv.org/abs/2004.10964 |
| Cross-Domain NER using Cross-Domain Language Modeling | Prior method named by the paper | Direct cross-domain NER comparison context | https://aclanthology.org/P19-1236/ |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2012.04373 | Canonical title, authors, dates, abstract, subjects, venue status, DOI, and public repository locator | 2026-08-01 | Primary metadata |
| R2 | https://doi.org/10.48550/arXiv.2012.04373 | Stable DOI for the reviewed paper | 2026-08-01 | Primary identifier |
| R3 | https://arxiv.org/pdf/2012.04373 | PDF evidence for method, tables, analysis, and conclusion | 2026-08-01 | Inspected locally; source file withheld |
| R4 | https://ar5iv.labs.arxiv.org/html/2012.04373 | Full-paper HTML cross-check and structured text | 2026-08-01 | Approved fallback; local file withheld |
| R5 | https://arxiv.org/html/2012.04373 | Official HTML route attempted during repair | 2026-08-01 | Returned 404; not accepted as evidence |
| R6 | https://github.com/zliucr/CrossNER | Official code/data availability, dependency notes, commands, and license visibility | 2026-08-01 | Repository inspected; no code run |
| R7 | https://aclanthology.org/P19-1236/ | Prior cross-domain NER comparison named in the paper | 2026-08-01 | Near-primary context |
| R8 | https://arxiv.org/abs/1810.04805 | BERT foundation referenced by the paper | 2026-08-01 | Foundational context |
| R9 | https://arxiv.org/abs/2004.10964 | Domain- and task-adaptive pre-training context | 2026-08-01 | Methodological neighbor |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-DoubleTransfer%20MEDIQA/doubletransfer_mediqa_manuscript.md | Related transfer and distribution-shift synthesis | 2026-08-01 | Repository-generated context |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Dataset%20Baselines/dataset_baselines_manuscript.md | Related dataset and baseline governance synthesis | 2026-08-01 | Repository-generated context |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md | Related multilingual benchmark and slice-evaluation synthesis | 2026-08-01 | Repository-generated context |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Live repository layout, attribution, public-safety, and source-locality rules | 2026-08-01 | Deposition authority |
| R14 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-08-01 | Deposition authority |
| R15 | Private local archive verification record | Candidate selection, deduplication, repair, and complete-source gate | 2026-08-01 | Local path withheld; not redistributed |

## Appendix

### Selection and source-integrity record

- Candidate enumeration: 75,960 PDF files; 75,957 unique parent-directory paper units.
- Accepted draw: sorted unique parent units, uniform zero-based PowerShell Get-Random index 42,378.
- Selected paper: arXiv:2012.04373, CrossNER: Evaluating Cross-Domain Named Entity Recognition.
- Dedup locations: Black Lake .logs, .reports, .lake-data, .staging; automation memory; live Black-Lake and Black-Lake-Data searches.
- Duplicate exclusions: 0. Reselections: 0. Public 24-hour cutoff: 2026-07-31.
- Initial source status: partial because the full-paper HTML was missing; the PDF was preserved.
- Repair: official arXiv HTML routes returned 404; approved ar5iv full-paper HTML was retrieved through the bounded repair process.
- Final integrity: PDF valid with size, header, and EOF checks; full-paper HTML valid with at least 5 KB, more than 2,000 body characters, a document marker, multiple headings, and multiple paper-structure terms.
- Source package: unavailable; no source package, PDF, HTML, metadata page, extracted text, cache, or repair record is included in this DEP.
- Public allowlist: this DEP contains only README.md and this generated manuscript Markdown file.
