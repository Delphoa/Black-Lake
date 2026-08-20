---
title: "DiscourseFlip Risk Review"
generated_at: "2026-07-19 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded defensive review of discourse-level opinion manipulation against black-box retrieval-augmented generation."
source_status: "verified complete local PDF, full-paper HTML, metadata HTML, and source package inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "Sources and repository context inspected through 2026-07-19."
primary_url: "https://arxiv.org/abs/2606.01212"
stable_identifier: "arXiv:2606.01212v2; DOI:10.48550/arXiv.2606.01212"
deployment_job_id: "BLAD-2200-20260719-7D93E819"
deployment_item_id: "BLAD-2200-20260719-7D93E819-P02"
confidence_summary: "High for source identity, method transcription, reported experiments, and defense comparisons; medium for generalization; low for universal deployment conclusions because experiments were not reproduced."
safety_scope: "defensive research, authorized synthetic-corpus evaluation, provenance monitoring, and non-operational security analysis"
distribution_notes: "No PDF, HTML, metadata page, TeX/source archive, extracted text, cache, payload, attack prompt, dataset, model, or local path is redistributed."
---

# DiscourseFlip Risk Review

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2606.01212v2 | https://arxiv.org/abs/2606.01212 | Metadata page is not full-paper evidence. | 2026-07-19 | Inspected. |
| S2 | Official full-paper rendering | Primary paper | HTML | arXiv:2606.01212v2 | https://arxiv.org/html/2606.01212 | Verified local copy withheld. | 2026-07-19 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2606.01212v2 | https://arxiv.org/pdf/2606.01212 | Verified local copy withheld. | 2026-07-19 | Inspected through extraction and cross-checks. |
| S4 | Paper source package | Primary source | TeX archive | arXiv:2606.01212v2 | https://arxiv.org/e-print/2606.01212 | Local package and extracted text withheld. | 2026-07-19 | Inspected for equations, tables, defenses, and appendices. |
| S5 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2606.01212 | https://doi.org/10.48550/arXiv.2606.01212 | Persistent locator. | 2026-07-19 | Resolved through arXiv metadata. |
| S6 | Self-Correcting RAG DEP-A | Related research | Markdown | DEP-A-20260715 | `.lake-data/DEP-A/DEP-A-20260715-Self-Correcting RAG/2604.10734-whitepaper-review.md` | Repository review, not primary evidence for DiscourseFlip. | 2026-07-19 | Inspected. |
| S7 | Memory Defense Layers DEP-E | Related research | Markdown | DEP-E-20260718 | `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md` | Repository-generated defensive synthesis. | 2026-07-19 | Inspected. |
| S8 | Agent Memory Forensics DEP-E | Related research | Markdown | DEP-E-20260711 | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` | Repository-generated defensive synthesis. | 2026-07-19 | Inspected. |
| S9 | Selection, repair, and cache records | Process evidence | Private records | `BLAD-2200-20260719-7D93E819-P02` | Local paths withheld | Used only for selection, integrity, extraction, and no-source-upload claims. | 2026-07-19 | Verified. |

The paper lists Yuyang Gong, Miaokun Chen, Jiawei Liu, Zhuo Chen, Guoxiu He, Wei Lu, XiaoFeng Wang, and Xiaozhong Liu. The canonical record shows submission on 2026-05-31 and revision on 2026-06-03. Deployment job ID: `BLAD-2200-20260719-7D93E819`. Deployment item ID: `BLAD-2200-20260719-7D93E819-P02`.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Canonical metadata | Title, authors, identifier, version, dates, subjects, DOI. | Source identity. | High | Metadata does not validate method or results. |
| E2 | S2-S4 | Primary full paper | Introduction, threat model, graph-guided method, metrics, datasets, tables, user study, defense evaluation, ablations, conclusion, appendices. | Mechanism and reported evidence. | High for transcription | No experiment was rerun. |
| E3 | S2-S4, main result tables | Primary quantitative evidence | Cross-generator, cross-retriever, pro/con RASR, coverage, DLI, and ASV. | Comparative performance. | High for reported values | Statistical uncertainty and independent reproduction are absent here. |
| E4 | S2-S4, user study | Primary human-subject evidence | 81-participant randomized study, two topics, normalized opinion shift, attribution conditions. | Short-session behavioral evidence. | Medium-high | Small, narrow, short-duration sample; durability and population validity unknown. |
| E5 | S2-S4, defense section | Primary defense evidence | Paraphrasing, random masking, perplexity, GRADA, top-k neutralization, topic safeguards. | Residual risk across five RAG surfaces. | High for reported comparisons | Implementations and thresholds are study-specific. |
| E6 | S9 | Process evidence | Uniform draw, cross-repository dedup, bounded repair, byte/marker validation, extraction cache. | Eligibility and complete-source gate. | High | Private source locations are withheld. |
| E7 | S6 | Related DEP evidence | Diversified evidence portfolio, NLI contradiction checking, source-authority boundary. | Retrieval and generation bridge. | Medium | Not a poisoning-defense validation. |
| E8 | S7 | Related DEP evidence | Architectural visibility, provenance-bearing state, privileged recall, action gates. | Defense-in-depth bridge. | Medium | Persistent memory differs from search RAG. |
| E9 | S8 | Related DEP evidence | Graph/trajectory signatures and trace-only limitations. | System-level detection bridge. | Medium | Different delayed-action outcome. |

## Executive Summary

DiscourseFlip studies an indirect RAG poisoning threat: instead of targeting one query, an adversary distributes influence across the semantic network surrounding a topic. The paper constructs topic graphs, allocates a bounded document budget across central and neighboring semantic units, and measures both retrieval entry and downstream opinion change. This review intentionally omits operational prompts, payload-generation procedures, and executable attack logic.

Across 40 topics, 5,843 probe queries, two generators, and three retrievers, the paper reports higher network coverage and stance variation than three adapted baselines. An 81-participant study reports target-direction opinion movement in 51.85% of exposed participants and low correct attribution of the manipulation target. Defense tests suggest that input paraphrasing, token masking, perplexity filtering, reranking, neutral rewriting, or root-topic safeguards alone leave residual network-level risk.

The durable defensive insight is architectural: document admission, source authority, retrieval composition, semantic-neighborhood behavior, response stance, and user feedback must be evaluated as one control path. The evidence does not show universal RAG compromise. It is bounded by corpus-write assumptions, graph construction, agent and classifier models, selected topics, short exposure, and no independent reproduction.

## Detailed Summary

### Threat and Objective

A conventional RAG pipeline retrieves a top-k evidence set for a query, then conditions a generator on that set. The paper assumes a black-box adversary can inject a limited number of documents but cannot modify the retriever, generator, or system prompt. Rather than repeatedly matching one target query, the attack distributes documents around related semantic units so many contextualized queries retrieve an aligned narrative.

The optimization distinguishes a document budget, a content budget, and a bounded retrieval-oriented edit budget. Its graph represents relations among a root topic, neighboring concepts, and query nodes. An agentic optimizer iteratively stabilizes core coverage, expands into adjacent units, and consolidates documents. Those mechanics are recorded only to support threat understanding; this artifact omits prompts, procedural pseudocode, optimized text, and operational recommendations.

### Data and Systems

The experimental corpus contains 679,402 chunks. Forty topics across four domains yield 5,843 probe queries, about 146 nodes per topic on average. The RAG systems use LangChain with Llama3.1-8B-Instruct or Qwen3-8B-Instruct as generators and BGE, DPR, or Qwen3-Embedding as retrievers. The agent backbone is reported as Qwen3-Next-80B-A3B-Instruct, with separate surrogate retriever/generator components and an external opinion classifier. Default evaluation retrieves five chunks and permits ten injected documents.

Metrics include retrieval attack success (whether adversarial evidence enters context), node coverage (fraction of graph nodes whose answers change in the target direction), stance variation (magnitude of opinion shift), and document leverage (network influence per injected document). The separation prevents a retrieval hit from being treated automatically as behavioral success.

### Main Evidence

The paper reports that DiscourseFlip leads all tested method/model/retriever/direction combinations. For Llama3.1 with BGE, coverage is reported as 27.09% pro versus 8.97% for the strongest baseline and 32.52% con versus 14.60%. With Qwen3-Embedding and Llama3.1, reported retrieval success remains 16.33% pro and 13.42% con while previous methods are described as nearly zero. Document leverage is often reported above 90% with BGE.

These comparisons support the structural hypothesis within the tested setup: distributing coherent evidence over a query network can retain influence under stronger retrievers. They do not independently prove why each gain occurs; graph allocation, large-model generation quality, surrogate transfer, and opinion classification are bundled.

### Human Evidence

The randomized controlled user study includes 81 college students and two topics. Control participants see clean RAG answers; manipulated participants receive responses influenced toward a target stance over four question-answer rounds per topic. Opinions use a seven-point scale normalized to [0,1]. The authors report target-direction movement for 51.85% of exposed participants and average shifts of 22.57% and 23.72% for the two topics.

A camouflage condition asks participants to attribute manipulation. Correct target attribution is reported at 22.22% for one topic and 7.41% for the other, with most responses attributed elsewhere or judged normal. The protocol demonstrates short-session perceptual risk; it does not establish long-term persuasion, ecological validity, representative demographics, or effects outside the selected topics.

### Mitigation Evidence

The defense analysis covers input, corpus, retrieval, top-k content, and generation. Query paraphrasing reduces but does not eliminate reported manipulation. Random masking weakens trigger-dependent baselines more than semantically coherent documents. Perplexity distributions for fluent evidence-based documents overlap the clean corpus. GRADA reranking reduces reported DiscourseFlip retrieval success and stance variation but leaves substantial residual values. Neutral rewriting is stronger against instruction-driven content than factually framed evidence. Root-topic neutrality reduces DiscourseFlip yet retains approximately 60% of original coverage and 45% of original stance variation.

The authors recommend an adaptive system-level stack. Reviewer interpretation adds a necessary qualification: expanding protection across a semantic neighborhood must not turn viewpoint disagreement into a threat label. Source authority, corroboration, insertion history, behavioral drift, and human review should constrain any graph-based alert.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| Discourse-level allocation broadens opinion manipulation beyond direct queries in the tested RAG systems. | Author empirical claim | E2, E3 | Supported as reported across the tested matrix; not reproduced. | Medium-high |
| The method retains measurable retrieval and stance effects under stronger embedding retrievers. | Author empirical claim | E3 | Supported by the reported Qwen3-Embedding values. | Medium-high |
| Short-session exposure can shift participant ratings while manipulation remains difficult to attribute. | Author human-study claim | E4 | Supported within two topics and 81 college participants; generalization is limited. | Medium |
| No single evaluated defense reliably eliminates the reported risk. | Author empirical claim | E5 | Supported for the implementations and operating points tested. | Medium-high |
| A composed, provenance-aware, graph-level defense is a better match than a single surface detector. | Reviewer inference | E5, E7-E9 | Mechanistically well motivated; requires independent evaluation. | Medium |
| The paper proves universal vulnerability of RAG systems. | Overbroad claim | E2-E5 | Not supported; write access, models, corpora, topics, metrics, and defenses are bounded. | High |
| The selected source was complete and non-duplicate before review. | Process claim | E6 | First draw passed dedup; partial unit was repaired and verified before synthesis. | High |

## Methodology

- `Research objective`: Produce a source-grounded, defensive DEP-E review of one uniformly selected, non-duplicate arXiv paper while preserving method, aggregate evidence, limitations, and safe implementation implications.
- `Sources inspected`: Canonical arXiv metadata, verified PDF, official full-paper HTML, source package, extracted PDF/HTML/source text, live repository authorities, private process evidence, and three related DEP manuscripts.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, collapsed paths to parent-directory units, selected a uniform PowerShell index, resolved identity from adjacent metadata, scanned all dedup surfaces, repaired the selected source, extracted three text representations, and searched Black Lake by concrete defensive overlap.
- `Inclusion criteria`: Evidence had to establish identity, expose method/results/limits, document defense results, prove source/dedup status, or support a retrieval, provenance, architectural, or graph-detection relationship.
- `Exclusion criteria`: Abstract-only claims, secondary summaries, operational attack prompts, executable payload logic, optimized malicious text, unrelated keyword hits, and source files prohibited from public deposition were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, defensive implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Author claims, reported measurements, reviewer interpretations, and process claims are labeled separately and tied to evidence IDs.
- `Uncertainty handling`: Non-reproduction, graph and classifier dependence, bundled model components, topic selection, human-study sampling, and defense operating points are explicit.
- `Extraction process`: Preflight found local PDF/HTML/source extraction tools. PDF, HTML, and source-package extraction all succeeded after bounded repair.
- `Version control`: The paper is pinned to arXiv v2. No official implementation repository was relied upon or executed.
- `Cross-checking`: Main metrics, experimental settings, user-study percentages, defense values, ablations, and conclusion were checked across official HTML and source text; PDF integrity supplied a complete-document cross-format check.
- `Safety handling`: The source is dual-use. This review preserves threat abstractions and aggregate evidence but omits operational prompts, procedures, attack code, and payloads. Implementations are defensive only.
- `Reviewer stance`: DEP-ready preservation with critical defensive translation.

### Random Selection and Deduplication

- Candidate enumeration: 75,778 PDFs and 75,776 unique PDF-parent paper units.
- Uniform selected index: 28,341 (one-based).
- Accepted identity: arXiv:2606.01212v2.
- Dedup scopes: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; this automation's memory; current Black-Lake-Data relevant records; and current-job paper set.
- Dedup keys: arXiv ID, DOI, exact/normalized title, slug, artifact markers, and preceding-24-hour markers using public-safe cutoff date 2026-07-18.
- Exclusions: 0. Reselections: 0. First draw accepted.

### Source Integrity and Cache

- Initial state: partial because full-paper HTML was missing.
- Repair: preserved the existing valid PDF and retrieved official full-paper HTML, metadata HTML, and source package with one bounded direct-HTTPS attempt per missing artifact.
- PDF: 1,115,948 bytes, `%PDF-` header, trailing `%%EOF`.
- Full-paper HTML: 337,747 bytes; 83,606 body characters; `article` and LaTeXML document markers; 78 heading/section markers; eight paper-structure terms; no rejected-payload markers.
- Unexpected partials: 0.
- Cache: `cached`; PDF text 90,607 bytes, HTML text 82,711 bytes, source text 113,237 bytes.
- Locality: original and extracted source files remain local and are excluded from all public staging.

## Scope, Constraints, and Assumptions

- `Scope`: Threat abstraction, reported experiments, human evidence, defense evaluation, three related DEP bridges, and defensive implementation guidance.
- `Temporal boundary`: Sources accessed through 2026-07-19; later revisions or replications are not included.
- `Evidence limits`: Experiments, models, corpora, prompts, classifiers, and defense implementations were not run; no participant-level data were inspected.
- `Assumptions`: Tables and percentages are interpreted as printed; arXiv v2 is the reviewed version; stance scores are accepted as study measurements rather than objective truth.
- `Constraints`: Source files stay local; no offensive procedure is operationalized; any future evaluation must use an authorized synthetic or licensed corpus.
- `Out of scope`: Corpus poisoning, persuasion campaigns, payload generation, target selection, real-user experimentation, censorship automation, security certification, and universal novelty proof.
- `Intended use`: Research preservation, threat modeling, defensive evaluation planning, and provenance-aware product ideation.
- `Audience`: RAG engineers, retrieval researchers, safety teams, provenance architects, and governance reviewers.
- `Depth target`: Full manuscript review with implementation and replication boundaries.
- `Reproducibility boundary`: Complete source detail supports planning, but no result is independently reproduced here.
- `Operational boundary`: Alerts may route authorized review or conservative fallback; they must not label viewpoints, people, or publishers as malicious without direct evidence.
- `Data sensitivity`: Public research references; future telemetry could contain user queries, political views, or browsing data and requires minimization.

## Observations

- `Observed pattern`: Defenses that rely on unnatural text or token triggers are weaker against fluent, factually framed evidence.
- `Observed pattern`: Protecting only the root topic misses semantically adjacent queries that do not activate the same rule.
- `Technical implication`: Risk scoring should aggregate corpus provenance, source diversity, retrieval spread, and response drift across a neighborhood.
- `Contradiction or tension`: More semantic-neighborhood coverage can improve defense while also increasing false positives against legitimate minority evidence.
- `Contradiction or tension`: A stance classifier makes the outcome measurable but can inherit cultural or political biases that shape the apparent attack success.
- `Open question`: Which minimal cross-surface signals identify coordinated influence without monitoring or suppressing normal opinion diversity?
- `Reviewer hypothesis`: Provenance-aware source independence plus graph-level behavioral drift will outperform text-only anomaly detection under matched false-positive budgets.

## Considerations

Opinion manipulation research involves political and social viewpoints, making false positives unusually harmful. A defensive system must distinguish coordinated corpus influence from genuine disagreement, evolving consensus, satire, advocacy, or newly reported evidence. Provenance and behavioral changes are safer starting points than ideological labels.

Telemetry joins can expose sensitive user queries and inferred beliefs. The smallest viable audit should use synthetic probe queries, aggregate drift metrics, short retention, access controls, deletion support, and no individual profiling. Human review should see source histories and conflicting evidence, not just a scalar risk score.

The human study reports short-term changes, not lasting persuasion. Ethical translation should avoid treating participants as passive endpoints and should require consent, debriefing, preregistered harm thresholds, demographic disclosure, and independent oversight for future behavioral studies.

## Strengths

- Frames RAG poisoning as a network-level systems risk instead of a single-trigger problem.
- Evaluates two generators, three retrievers, two target directions, 40 topics, and multiple defense surfaces.
- Separates retrieval entry, node coverage, stance magnitude, and document leverage.
- Includes a randomized human study rather than relying solely on an automated stance classifier.
- Tests both general RAG defenses and opinion-specific safeguards.
- Reports budget and top-k ablations that expose saturation and context-dilution behavior.
- States a need for adaptive system-level defenses rather than claiming one universal filter.

## Weaknesses

- The graph, large agent backbone, surrogate components, and external stance classifier bundle multiple sources of performance.
- No independent replication or production RAG evaluation is available in this review.
- The user study is small, college-only, two-topic, short-duration, and dependent on self-reported ratings.
- Opinion classification and target-direction scoring can encode normative and cultural assumptions.
- Corpus-write and retrievability assumptions may not transfer to strongly governed or closed corpora.
- Defense implementations and thresholds are selected examples, not exhaustive best-in-class evaluations.
- Aggregate results may hide topic, domain, or query strata where the method fails.
- The source exposes operational material whose responsible release and downstream use require stronger governance than ordinary benchmark code.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Factor graph allocation from generator quality | Causal attribution | Bundled agent and graph effects obscure mechanism | Cleaner evidence | Expensive factorial runs | Matched random/centrality/agent ablations |
| Add source-authority and independence baselines | Defense realism | Text-only defenses omit provenance | Stronger system controls | Metadata availability | Matched false-positive evaluation on synthetic corruption |
| Audit stance classifiers across cultures and domains | Measurement validity | Opinion labels are normative | Lower metric bias | Human annotation burden | Multi-annotator calibration and disagreement reporting |
| Expand human study and measure durability | Behavioral evidence | Two short topics cannot establish lasting effects | Better external validity | Ethical and recruitment cost | Preregistered longitudinal study with debriefing |
| Report per-topic distributions and uncertainty | Statistical clarity | Means can hide failures and outliers | More calibrated claims | Larger tables | Bootstrap intervals and complete strata |
| Test composed defenses | Systems relevance | Single-surface controls are structurally incomplete | Actionable mitigation | Integration complexity | Source gate + retrieval monitor + generation fallback ablation |

## Potential Implementations

1. **Semantic Neighborhood Risk Lab**
   - `User`: Authorized RAG safety and retrieval teams.
   - `Goal`: Detect coordinated response drift around high-impact topics before production release.
   - `Core mechanism`: Build a versioned synthetic query graph, replay clean and candidate corpora, and compare retrieval source mix plus response stance across nodes.
   - `Required inputs`: Authorized corpus snapshots, synthetic probes, source metadata, pinned retriever/generator, calibrated stance indicators.
   - `Outputs`: Drift map, source-concentration report, false-positive review queue.
   - `Risk controls`: Offline only, no user profiling, viewpoint-neutral labels, human adjudication, immutable baselines.
   - `Evaluation`: Detection recall at fixed false-positive and source-diversity budgets.
2. **Provenance-Aware Evidence Gate**
   - `User`: RAG platform engineer.
   - `Goal`: Prevent low-authority coordinated sources from dominating context.
   - `Core mechanism`: Score source authority, independence, insertion history, corroboration, and conflict before diversified top-k selection.
   - `Required inputs`: Chunk provenance, domain identity, timestamp, trust policy, contradiction signals.
   - `Outputs`: Admitted evidence portfolio with reason codes and fallback status.
   - `Risk controls`: Preserve minority sources, appeals, transparent thresholds, conservative abstention.
   - `Evaluation`: Clean utility, corruption resistance, source coverage, and viewpoint false positives.
3. **Cross-Surface Incident Ledger**
   - `User`: Security operations and model-governance team.
   - `Goal`: Trace how corpus changes alter retrieval and responses.
   - `Core mechanism`: Join corpus admission, chunk versions, retrieval ranks, source diversity, drift alerts, and response outcomes under short retention.
   - `Required inputs`: Privacy-minimized events and versioned policy decisions.
   - `Outputs`: Incident timeline, affected semantic nodes, rollback candidate set.
   - `Risk controls`: Aggregate probes, tenant isolation, deletion propagation, least privilege, human approval.
   - `Evaluation`: Time to explain, rollback precision, privacy review, and analyst burden.

## Three Ways to Exercise This Research

1. `Synthetic neighborhood replay`: Construct neutral fictional topics and licensed documents, create a clean and intentionally imbalanced corpus without persuasive attack text, and measure graph-wide retrieval/source drift. Success is detecting imbalance at a fixed false-positive rate; stop before real political targets or users are involved.
2. `Defense composition ablation`: Compare text anomaly checks, source provenance gates, diversified selection, contradiction checks, and their composition on an offline corpus. Success is improved robustness without material clean-utility collapse; stop if source metadata or licensing is incomplete.
3. `Stance metric audit`: Have diverse blinded annotators rate synthetic answers and compare their distributions with multiple automated classifiers. Success is calibrated uncertainty and explicit disagreement strata; stop if annotator safety, consent, or sample representation is inadequate.

## Example MVP Product

- `Product name`: RAG Neighborhood Watch.
- `Target user`: Authorized retrieval-security and model-governance teams.
- `Problem`: Existing dashboards inspect suspicious documents or explicit topics but miss coordinated source concentration and response drift across related queries.
- `Core workflow`: Register an authorized corpus snapshot; define synthetic topic graphs; run pinned retrieval/generation replays; compare source diversity and stance distributions with a clean baseline; route high-drift, low-independence neighborhoods to human review.
- `Data requirements`: Versioned authorized corpus, source metadata, synthetic probes, pinned model outputs, minimal aggregate evaluation labels.
- `Architecture`: Offline replay runner, graph store, provenance joiner, drift evaluator, policy engine, human-review UI, and static evidence report.
- `Success metrics`: Detection recall at fixed false-positive rate, clean answer utility, source-diversity preservation, rollback precision, and analyst time.
- `Risk controls`: No real-user targeting, no viewpoint blacklists, no payload generation, short retention, role-based access, human authorization, appeals, and immutable audit records.
- `Limitations`: Graph and stance metrics remain model-dependent; source authority can encode institutional bias; offline probes cannot reproduce all live behavior.
- `MVP boundary`: No live corpus mutation, automated censorship, user profiling, political targeting, or production blocking without reviewed policy.
- `Deployment model`: Local batch tool inside an authorized research environment.
- `Evaluation plan`: Unit tests, synthetic-corpus smoke test, matched false-positive benchmark, privacy review, red-team review of false positives, and staged shadow deployment.
- `Failure modes`: Graph drift, classifier bias, coordinated trusted domains, missing provenance, alert floods, minority-source suppression, and baseline contamination.
- `Maintenance plan`: Pin models and corpora, version graphs and thresholds, refresh baselines after approved changes, sample false negatives, and require governance review before expansion.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Self-Correcting RAG | Black Lake DEP-A | Diversified evidence portfolios, contradiction checks, and source-authority limitation | `.lake-data/DEP-A/DEP-A-20260715-Self-Correcting RAG/2604.10734-whitepaper-review.md` |
| Memory Defense Layers | Black Lake DEP-E | Control-surface visibility, provenance-bearing state, and defense composition | `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md` |
| Agent Memory Forensics | Black Lake DEP-E | Graph/trajectory signals for delayed poisoning and trace-classifier limits | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` |
| GRADA | Primary defense cited by the paper | Similarity-discrepancy reranking defense evaluated in the study | Paper bibliography; see primary source for exact version |
| ReliabilityRAG | Primary defense cited by the paper | Confidence-aware evidence aggregation context | Paper bibliography; see primary source for exact version |
| Traceback of poisoning attacks to RAG | Primary defense cited by the paper | Retrospective source localization | Paper bibliography; see primary source for exact version |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2606.01212 | Identity, metadata, abstract, version, DOI locator | 2026-07-19 | Canonical metadata; not full-paper evidence. |
| R2 | https://arxiv.org/html/2606.01212 | Full threat model, experiments, user study, defenses, limitations | 2026-07-19 | Verified complete local rendering withheld. |
| R3 | https://arxiv.org/pdf/2606.01212 | Full-paper cross-check and integrity | 2026-07-19 | Verified local PDF withheld. |
| R4 | https://arxiv.org/e-print/2606.01212 | Equations, tables, configuration, appendices | 2026-07-19 | Source package and extraction withheld. |
| R5 | https://doi.org/10.48550/arXiv.2606.01212 | Persistent identity | 2026-07-19 | arXiv-issued DOI. |
| R6 | `.lake-data/DEP-A/DEP-A-20260715-Self-Correcting RAG/2604.10734-whitepaper-review.md` | Retrieval/generation bridge | 2026-07-19 | Related synthesis only. |
| R7 | `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md` | Architectural defense bridge | 2026-07-19 | Related synthesis only. |
| R8 | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` | Graph/trajectory detection bridge | 2026-07-19 | Related synthesis only. |
| R9 | Private selection, integrity, and extraction records | Randomness, dedup, repair, cache, source locality | 2026-07-19 | Local paths and files withheld; no source uploaded. |

## Appendix

### Selection and Integrity Receipt

- Automation: `Black Lake Arxiv DEP 2200 x10`.
- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P02`.
- Random method: uniform PowerShell index after `rg` PDF enumeration and unique parent-unit collapse.
- Candidate units: 75,776; selected one-based index: 28,341.
- Duplicate exclusions: 0; reselections: 0; public-safe 24-hour cutoff date: 2026-07-18.
- Initial source state: partial. Final state after bounded repair: complete.
- PDF integrity: 1,115,948 bytes; header and EOF checks passed.
- Full-paper HTML integrity: 337,747 bytes; 83,606 body characters; required document, heading, and paper-structure markers passed.
- Cache status: `cached` for PDF, HTML, and source-package text.
- Original sources and cache: withheld locally.
- Public-source uploads: zero.

### Defensive Reproduction Checklist

- Use only synthetic, licensed, or explicitly authorized corpora.
- Pin arXiv v2, retriever, generator, embedding model, stance evaluator, and corpus snapshot.
- Omit or disable attack-generation prompts and payload-writing components.
- Record source identities, insertion histories, chunk hashes, and retrieval traces.
- Separate source authority, relevance, corroboration, stance, and response quality.
- Report per-topic distributions, confidence intervals, and false-positive strata.
- Compare individual defenses with a composed defense stack under matched clean utility.
- Audit minority-viewpoint and new-evidence false positives with diverse human reviewers.
- Minimize query telemetry and prohibit individual belief profiling.
- Stop before live corpus mutation, real-user persuasion studies, or automated blocking.
