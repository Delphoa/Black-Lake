---
title: "VLM Probing - DEP-E"
generated_at: "2026-07-12 (public-safe date; exact execution timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of VALUE probes for internal behavior in pre-trained vision-and-language Transformers."
source_status: "URLs plus privately inspected local PDF; no source files redistributed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-12"
temporal_cutoff: "Sources and repository context inspected through 2026-07-12."
primary_url: "https://arxiv.org/abs/2005.07310"
stable_identifier: "arXiv:2005.07310v2; DOI:10.1007/978-3-030-58539-6_34"
confidence_summary: "High for paper identity and reported method/results; medium for interpretation; low for independent reproducibility because experiments and code were not run."
safety_scope: "non-sensitive research review, synthetic probe examples, evaluation-only implementation guidance"
distribution_notes: "No local paths, exact execution timestamps, source PDFs, datasets, checkpoints, or code are redistributed."
---

# VLM Probing - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract and HTML | Primary paper | HTML | arXiv:2005.07310v2 | https://arxiv.org/abs/2005.07310 | Public metadata/full-text rendering; arXiv distribution terms apply. | 2026-07-12 | Inspected. |
| S2 | arXiv paper PDF | Primary paper | PDF | arXiv:2005.07310v2 | https://arxiv.org/pdf/2005.07310 | Public paper; not redistributed in this DEP. | 2026-07-12 | Privately inspected through local PDF extraction. |
| S3 | ECVA paper page | Accepted-paper record | HTML/PDF | ECCV 2020 paper 6959 | https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/6959_ECCV_2020_paper.php | Public accepted-paper page. | 2026-07-12 | Inspected. |
| S4 | ECCV proceedings DOI | Persistent identifier | DOI | 10.1007/978-3-030-58539-6_34 | https://doi.org/10.1007/978-3-030-58539-6_34 | Publisher metadata; no publisher file collected. | 2026-07-12 | Referenced. |
| S5 | Microsoft Research page | Author/institution context | HTML | ECCV 2020 publication | https://www.microsoft.com/en-us/research/publication/behind-the-scene-revealing-the-secrets-of-pre-trained-vision-and-language-models/ | Public institutional metadata. | 2026-07-12 | Inspected. |
| S6 | VALUE code locator | Official locator named by paper | GitHub repository | Unavailable | https://github.com/JizeCao/VALUE | Availability/license could not be verified. | 2026-07-12 | Unavailable/not found. |
| S7 | Local archive evidence | Selection provenance | PDF/readme | arXiv:2005.07310 | Local path withheld | Private local evidence; no redistribution. | 2026-07-12 | Inspected. |
| S8 | VideoWeave Geometry DEP | Related research artifact | Markdown | DEP-E-20260709-VideoWeave Geometry | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Repository-generated review. | 2026-07-12 | Inspected. |
| S9 | BA-LoRA Bias DEP | Related research artifact | Markdown | DEP-E-20260709-BA-LoRA Bias | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Repository-generated review. | 2026-07-12 | Inspected. |
| S10 | HSD FTI-FDet DEP | Related research artifact | Markdown | DEP-E-20260712-HSD FTI-FDet | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Repository-generated review. | 2026-07-12 | Inspected. |

The paper lists Jize Cao, Zhe Gan, Yu Cheng, Licheng Yu, Yen-Chun Chen, and Jingjing Liu as authors. The initial arXiv submission date is 2020-05-15; the inspected PDF identifies version 2 dated 2020-07-18. The accepted work appeared in ECCV 2020, Part VI, pages 565–580.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S3-S5 | Primary/near-primary metadata | Title, authors, dates, venue, abstract, DOI. | Source identity and publication context. | High | Does not independently validate experiments. |
| E2 | S2 | Primary paper | Sections 1–4, Tables 1–5, Figures 2–4, and appendices. | Architecture, datasets, probe definitions, quantitative results, caveats, and conclusions. | High for reporting | PDF extraction has character artifacts; no experiments rerun. |
| E3 | S2 appendix | Primary paper | Random-weight baselines, full layer tables, future-design guidelines. | Baseline interpretation and source-disclosed limits. | High for reporting | Still author-reported evidence. |
| E4 | S6 | Official locator | Repository reachability check. | Code-availability boundary. | High for observed unavailability | Does not establish whether code existed previously or elsewhere. |
| E5 | S7 | Private provenance | PDF/readme presence and random-selection identity. | Archive-unit selection and extraction status. | High | Local path intentionally withheld. |
| E6 | S8-S10 | Related DEP artifacts | Executive summaries, observations, and source bases. | Cross-DEP synthesis and implementation relevance. | Medium | Related artifacts do not validate VALUE's metrics. |
| E7 | Repository and memory scans | Process evidence | IDs, titles, DOI/slug markers, recent-date markers. | Deduplication and eligibility. | High | Used-paper index deliberately over-excludes referenced IDs. |

## Executive Summary

VALUE is a diagnostic framework for probing what pre-trained vision-and-language Transformers encode. The paper studies one single-stream architecture, UNITER-base, and one two-stream architecture, LXMERT, using Flickr30k Entities, Visual Genome, attention traces, linear probes, layer-wise embeddings, mismatched captions, and random-weight controls. The contribution is not a new task model; it is a structured way to ask where multimodal fusion, modality preference, cross-modal alignment, visual relations, and linguistic information appear inside a model.

The strongest evidence supports narrower conclusions than a simple “attention explains the model” reading. UNITER representations become less separable by modality in deeper layers, a small subset of heads concentrates cross-modal behavior, matched image-text pairs carry more visual-relation signal than mismatched pairs, and both architectures encode recoverable coreference/relation information. At the same time, binary coreference detection remains weak, phrase content can leak relation labels, BERT outperforms the V+L models on linguistic probes, and attention diagnostics remain correlational.

Reviewer confidence is high that this artifact accurately reports the inspected paper and tables. Confidence is medium for using VALUE as a reusable evaluation pattern because current generative VLMs expose different representations. Confidence is low for reproducibility: the experiments were not run and the paper-linked code locator was unavailable.

## Detailed Summary

### Problem Context

By 2020, vision-and-language pre-training had improved image-text retrieval, visual question answering, referring expressions, and visual reasoning, yet downstream scores revealed little about internal mechanisms. The paper addresses that gap through five questions: how fusion changes with depth, which modality dominates decisions, where cross-modal alignment appears, whether visual relations are encoded, and how much linguistic knowledge survives multimodal pre-training.

### Architectures and Data

UNITER-base represents the single-stream family: text and image-region tokens share a 12-layer, 12-head Transformer with 768-dimensional hidden states. LXMERT represents the two-stream family: text and image features are processed separately before five cross-modality layers. Flickr30k Entities supplies noun-phrase-to-region links; Visual Genome supplies dense captions and scene-graph relations. The paper combines annotated regions with Faster R-CNN detections because the annotated sets are smaller than the typical 36-region model input.

### Probe 1: Multimodal Fusion

The authors cluster layer representations into two groups and compare them with image/text labels using normalized mutual information (NMI). Lower NMI means less modality separability and therefore greater fusion under this operational definition. UNITER's NMI moves from 0.36 to 0.20 on Flickr30k and from 0.25 to 0.16 on Visual Genome across the reported layers. LXMERT's five cross-modal layers move 0.42, 0.48, 0.67, 0.75, 0.43 on Flickr30k and 0.43, 0.56, 0.68, 0.78, 0.57 on Visual Genome. This supports a clear depth trend for UNITER but not a simple monotonic fusion story for LXMERT.

### Probe 2: Modality Importance

For UNITER, the study sums `[CLS]` attention over text or image tokens. Text attention is denser and has higher layer-level mass, especially in intermediate layers. The analysis excludes LXMERT because its two-stream attention pattern does not allow `[CLS]` to attend to both modalities in the same way. This matters because the conclusion section generalizes textual dominance more broadly than the direct experiment warrants.

### Probe 3: Cross-Modal Interaction

An UNITER head counts as image-to-text specialized when at least one visual token assigns more than half its attention to text. The maximum empirical probability is 0.92, the minimum is zero, and only 15% of heads exceed 0.5. Visual coreference probes examine attention between regions and linked noun phrases. Linear attention probes reach 75.10% VCC for UNITER and 54.47% for LXMERT, while layer-wise embedding probes exceed 93% on VCC. The authors explicitly caution that noun-phrase content may leak class information.

### Probe 4: Visual Relations

Using 32 frequent Visual Genome relations, the paper tests whether pairs of image regions encode relation existence and class. Attention probes report 69.81% VRI and 24.67% VRC for UNITER and 67.53%/18.89% for LXMERT, compared with 50%/3.33% random guesses. Layer-wise UNITER embeddings reach 86.35% VRI and 56.64% VRC. Mismatched captions pull performance toward the original visual embedding baseline, suggesting that matched text contributes relation information.

### Probe 5: Linguistic Knowledge

Nine SentEval tasks cover sentence length, syntax, tense, grammatical number, semantic odd-man-out, and coordination inversion. UNITER's best layers outperform LXMERT's across all nine reported tasks, which the authors connect to UNITER's BERT initialization. BERT-base still outperforms both multimodal models, showing that multimodal pre-training does not preserve all linguistic capability equally.

### Conclusions and Boundary

The paper argues that single-stream fusion deepens with layers, text often dominates, a subset of heads specializes in cross-modal behavior, visual relations are recoverable, and linguistic knowledge remains. A careful reading narrows these claims to the tested checkpoints, datasets, probe definitions, and 2020 architecture family. The work is best treated as a reusable evaluation design, not a causal theory of model internals.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | UNITER's image/text representations become less separable in deeper layers. | Author empirical claim | E2, Table 1 | Directly supported by falling NMI on both datasets under the paper's fusion definition. | High for tested setup |
| C2 | Text is more important than image for model decisions. | Author claim | E2, Section 3.2 | Directly supported for UNITER `[CLS]` attention, not equivalently tested for LXMERT. | Medium |
| C3 | Cross-modal behavior concentrates in a subset of UNITER heads. | Author empirical claim | E2, Figure 3 and Section 3.3 | Supported descriptively; causal necessity was not tested. | Medium-high |
| C4 | Matched captions contribute to visual-relation representations. | Author empirical claim | E2, Figure 4 and Tables 9–10 | Mismatch ablations support an association; dataset shortcuts remain possible. | Medium-high |
| C5 | Both architectures encode rich linguistic knowledge. | Author empirical claim | E2, Table 5 | Recoverable signal exists, but both trail BERT and “rich” is qualitative. | Medium |
| C6 | VALUE can guide current multimodal model review. | Reviewer interpretation | E2, E6 | The probe pattern transfers conceptually, but concrete interfaces must change. | Medium |
| C7 | The paper was eligible for this automation run. | Process claim | E5, E7 | No prior marker was found by ID/title/DOI/slug and no 24-hour marker existed. | High |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E manuscript for one randomly selected, non-duplicate arXiv paper and connect it to exactly three verified Black Lake entries.
- `Sources inspected`: Local PDF and provenance readme; arXiv metadata/HTML and public PDF; ECVA paper page; Microsoft Research publication page; DOI; paper-declared code locator; live repository READMEs; three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, grouped unique parent directories, built a used-paper index, made a uniform `Get-Random` draw, extracted the selected PDF with `pypdf`, inspected public primary sources, and searched Black Lake by conceptual keywords.
- `Inclusion criteria`: Sources had to establish identity, expose methods/results, define repository rules, document selection/dedup provenance, or overlap with multimodal fusion, representation behavior, attention specialization, or adaptation robustness.
- `Exclusion criteria`: Secondary summaries were not used for technical claims. No inaccessible code, uncollected source package, local absolute path, or unverified reproduction claim was treated as evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, and evidence-quality analysis.
- `Evidence handling`: Author claims are tied to evidence IDs and source tables/sections; reviewer interpretations are labeled; related DEP entries are synthesis context only.
- `Uncertainty handling`: Non-causal attention evidence, dataset leakage, architectural age, unavailable code, and non-reproduction are explicit.
- `Extraction process`: `pypdf` extracted 58,111 bytes of text. No local HTML or source package was available. Public arXiv HTML cross-checked headings and table values.
- `Version control`: The paper is pinned to arXiv:2005.07310v2; repository policy was read at Black Lake commit `cd1763795d659e9ef5effc6b0bd0ef00150ea5d3` and Black-Lake-Data default commit `a5617922963be56fc5a7d3172535cb3167146209`.
- `Random selection`: Uniform zero-based index over 75,761 paper units; selected index 9,460; no duplicate rejection or reselection.
- `Deduplication`: Scanned `Black-Lake/.logs`, `.reports`, `.lake-data`, automation memory, `Black-Lake-Data/.lake-data`, and `.reports`; observed 344 used arXiv IDs; 65 archive units matched used IDs; no marker matched arXiv:2005.07310, DOI, exact title, or slug.
- `24-hour validation`: Public-safe cutoff date 2026-07-11; no same-paper marker was found on or after the cutoff.
- `Reviewer stance`: Critical paper review, DEP-ready preservation, modern implementation translation, and explicit reproducibility boundary.

## Scope, Constraints, and Assumptions

- `Scope`: VALUE's probes, reported evidence, limitations, and transfer to representation auditing for current multimodal systems.
- `Temporal boundary`: Sources inspected through 2026-07-12; primary paper version is from 2020.
- `Evidence limits`: No experiment execution, checkpoint access, code inspection, figure-level visual audit, or dataset collection.
- `Assumptions`: The local PDF and arXiv v2 record refer to the same revision; public HTML/PDF and ECCV records are authentic publication artifacts.
- `Constraints`: No local paths, home identifiers, machine names, timezone labels, exact execution timestamps, or unlicensed source files may appear in public artifacts.
- `Out of scope`: Claiming causal interpretability, benchmarking modern proprietary VLMs, reproducing the paper, or auditing dataset licenses in depth.
- `Intended use`: Research review, DEP deposition, evaluation-design reference, and implementation planning for safe model audits.
- `Audience`: Multimodal researchers, ML engineers, evaluation teams, and Black Lake reviewers.
- `Depth target`: Full schema-complete manuscript with concise quantitative preservation.
- `Reproducibility boundary`: Reported values can be checked against the cited paper, but cannot be independently reproduced from this DEP alone.
- `Data sensitivity`: Public research metadata and private local archive presence; public outputs contain no private location information.

## Observations

- `Observed pattern`: Useful cross-modal behavior is unevenly distributed across layers and heads rather than uniform across the network.
- `Technical implication`: Model audits should report distributions and localized effects, not only global averages.
- `Contradiction or tension`: The conclusion generalizes textual dominance to both architectures, while the direct `[CLS]` modality-importance experiment is scoped to UNITER.
- `Evidence-quality implication`: High probe accuracy may reflect recoverable label information without proving the model uses it for downstream decisions.
- `Cross-DEP pattern`: VideoWeave, BA-LoRA, and HSD FTI-FDet all expose intermediate structure that could be measured with VALUE-like controls.
- `Open question`: Which probes remain stable for patch-token encoders, cross-attention decoders, mixture-of-experts, and generative multimodal models?
- `Reviewer hypothesis`: A modern audit should combine descriptive probes, causal ablations, output behavior tests, and leakage controls.

## Considerations

Attention is observable and convenient, but it is not automatically faithful explanation. A deployment gate should pair attention/embedding probes with interventions such as head masking, feature patching, counterfactual inputs, and behavior-level regression tests. Thresholds also require versioned datasets and architecture-specific normalization.

The datasets contain human annotations, image regions, noun phrases, and relation labels. A modern replication should review consent, licensing, representativeness, annotation bias, and protected-attribute leakage before using probes as quality gates. Public dashboards should expose aggregate metrics rather than raw user images or text.

The paper's age is both limitation and value. Region-feature models differ from current VLMs, but the experimental discipline—matched controls, random baselines, layer/head localization, and leakage caveats—remains useful.

## Strengths

- Defines five complementary probe families instead of relying on one visualization.
- Compares single-stream and two-stream architectures with explicit structural reasoning.
- Uses Flickr30k Entities and Visual Genome to connect probes with grounded relations.
- Includes random-weight and mismatched-caption controls.
- Preserves negative evidence: weak binary coreference detection, language performance below BERT, and possible phrase-label leakage.
- Provides full layer tables and design guidelines in the appendix.

## Weaknesses

- Covers only UNITER-base and LXMERT, limiting architectural generalization.
- Attention-based evidence is correlational and can be mistaken for causal explanation.
- Some probes may exploit annotation or phrase-content shortcuts.
- The modality-importance conclusion is broader than the directly comparable experiment.
- Code was unavailable during this review, and experiments were not reproduced.
- Region-detection inputs and benchmarks reflect the 2020 V+L landscape.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add causal head and feature interventions | Interpretability | Correlation does not show necessity. | Stronger mechanistic claims. | Compute and design complexity. | Mask/patch components and measure downstream deltas. |
| Build leakage-controlled relation datasets | Probe validity | Phrase content can reveal labels. | More faithful grounding estimates. | Dataset redesign may reduce scale. | Counterbalance lexical cues and test transfer. |
| Extend to current generative VLMs | External validity | Modern architectures differ. | Current implementation relevance. | Hidden APIs and large compute. | Start with open, small checkpoints and versioned hooks. |
| Report confidence intervals and seeds | Statistical rigor | Single values hide variance. | Better threshold design. | Additional runs. | Bootstrap samples and repeat probe training. |
| Combine internal and behavioral metrics | Decision usefulness | Internal signal may not affect outputs. | Safer deployment gates. | Requires task suites. | Correlate probe shifts with counterfactual behavior. |
| Archive runnable environment metadata | Reproducibility | Code locator is unavailable. | Durable future replication. | Licensing/storage review. | Preserve lockfiles, hashes, and setup notes when permitted. |

## Potential Implementations

1. `Multimodal Checkpoint Auditor`
   - `User`: VLM training and evaluation team.
   - `Goal`: Detect unexpected changes in fusion, modality balance, and grounded relation signals.
   - `Core mechanism`: Run architecture adapters that emit layer/head aggregates and linear-probe features on a versioned synthetic/public suite.
   - `Required inputs`: Checkpoint, processor, hook map, public test bundle, metric thresholds.
   - `Outputs`: Versioned audit report, regression table, accepted/rejected status.
   - `Risk controls`: Aggregate-only storage, license review, no raw user data, architecture-specific thresholds.
   - `Evaluation`: Reproduce known ablations and verify injected modality failures trigger alerts.
2. `Adapter Drift Gate`
   - `User`: PEFT/LoRA release engineer.
   - `Goal`: Prevent adaptation from collapsing representation diversity or minority-relation performance.
   - `Core mechanism`: Compare base and adapted model probes plus output behavior, borrowing BA-LoRA's drift/diversity framing.
   - `Required inputs`: Base/adapted checkpoints, public prompts/images, aggregate outputs, approved limits.
   - `Outputs`: Delta report and release decision.
   - `Risk controls`: Human review for thresholds; protected-subgroup tests where lawful and appropriate.
   - `Evaluation`: Seeded regressions and holdout relation sets.
3. `Distillation Pathway Analyzer`
   - `User`: Edge-model optimization team.
   - `Goal`: Identify which heads or feature paths retain grounded information after distillation.
   - `Core mechanism`: Compare teacher/student probes, causal masks, latency, memory, and behavior.
   - `Required inputs`: Teacher/student models, hook mappings, benchmark suite, runtime telemetry.
   - `Outputs`: Retention heatmap, prune candidates, Pareto report.
   - `Risk controls`: No automatic pruning without causal validation and downstream safety tests.
   - `Evaluation`: Accuracy-efficiency frontier and targeted failure cases.

## Three Ways to Exercise This Research

1. `Recreate one VALUE probe`: Objective—verify the modality-fusion trend on a small open VLM; inputs—one public checkpoint and a small licensed image-text set; method—extract two layers and calculate modality separability; output—a plot and metric table; success—stable direction across three seeds; stop—if hooks or licenses are unclear.
2. `Run a leakage challenge`: Objective—test whether relation probes exploit words instead of grounding; inputs—synthetic captions with controlled lexical cues and public images; method—swap or mask relation words and compare probe scores; output—a leakage gap; success—performance remains above baseline under cue removal; stop—if raw personal data enters the pipeline.
3. `Test causal head relevance`: Objective—separate descriptive specialization from necessity; inputs—a small model, synthetic/public examples, and ranked heads; method—mask top-ranked versus random heads; output—behavior and latency deltas; success—ranked interventions produce repeatable targeted effects; stop—if masking destabilizes unrelated safety-critical outputs.

## Example MVP Product

- `Product name`: CrossModal Audit Gate.
- `Target user`: ML platform teams releasing open or internal multimodal checkpoints.
- `Problem`: Aggregate accuracy can improve while grounding, modality balance, or representation diversity silently regresses.
- `Core workflow`: Register a checkpoint; select an architecture adapter; run a public/synthetic probe suite; compare with the approved baseline; review failures; export a signed Markdown/JSON decision record.
- `Data requirements`: Licensed public images/text, synthetic relation pairs, versioned labels, aggregate checkpoint outputs, and no production user content in the MVP.
- `Architecture`: Local runner, model-hook adapter, probe library, metric normalizer, threshold policy, artifact generator, and append-only decision ledger.
- `Success metrics`: Detect seeded modality ablations with at least 90% recall; zero raw-data leaks in artifacts; deterministic reruns within declared tolerance; reviewer decision time under 20 minutes.
- `Risk controls`: Local-only execution by default, public/synthetic data, content hashing, aggregate metrics, human approval, architecture-specific policies, and explicit non-causal labels for attention evidence.
- `Limitations`: Not a proof of interpretability, fairness, safety, or deployment readiness; hooks may be unavailable for closed models.
- `MVP boundary`: One open VLM family, three probe types, no training, no automatic model modification.
- `Deployment model`: Local CLI plus static report.
- `Evaluation plan`: Unit tests for metric code, golden synthetic cases, seeded failure injection, and two reviewer walkthroughs.
- `Failure modes`: Label leakage, incompatible token layouts, unstable thresholds, hidden quantization effects, and overinterpretation of attention.
- `Maintenance plan`: Version probe datasets, adapters, thresholds, model hashes, and dependency lockfiles; require review for policy changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| VALUE / Behind the Scene | Primary paper | Core probe framework reviewed here. | https://arxiv.org/abs/2005.07310 |
| UNITER | Model paper | Single-stream model examined by VALUE. | https://arxiv.org/abs/1909.11740 |
| LXMERT | Model paper | Two-stream model examined by VALUE. | https://arxiv.org/abs/1908.07490 |
| What Does BERT Look At? | Methodological neighbor | Attention-pattern analysis precedent cited by VALUE. | https://arxiv.org/abs/1906.04341 |
| Transformer Interpretability Beyond Attention Visualization | Critical follow-up | Motivates causal relevance methods beyond raw attention maps. | https://arxiv.org/abs/2012.09838 |
| VideoWeave Geometry DEP | Related Black Lake artifact | Joint multimodal latent fusion and geometry consistency. | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |
| BA-LoRA Bias DEP | Related Black Lake artifact | Representation drift/collapse and constrained adaptation. | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` |
| HSD FTI-FDet DEP | Related Black Lake artifact | Specialized attention, heterogeneous pathways, distillation. | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2005.07310 | Identity, version, authors, abstract, HTML full text. | 2026-07-12 | Primary public source. |
| R2 | https://arxiv.org/pdf/2005.07310 | Method, experiments, tables, appendices, limitations. | 2026-07-12 | Public counterpart of privately inspected PDF. |
| R3 | https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/6959_ECCV_2020_paper.php | ECCV accepted-paper context. | 2026-07-12 | Near-primary venue source. |
| R4 | https://doi.org/10.1007/978-3-030-58539-6_34 | Persistent proceedings identity. | 2026-07-12 | Publisher DOI. |
| R5 | https://www.microsoft.com/en-us/research/publication/behind-the-scene-revealing-the-secrets-of-pre-trained-vision-and-language-models/ | Institutional publication metadata. | 2026-07-12 | Author-organization source. |
| R6 | https://github.com/JizeCao/VALUE | Code availability boundary. | 2026-07-12 | Unavailable/not found; no code evidence used. |
| R7 | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Related multimodal fusion synthesis. | 2026-07-12 | Repository-relative artifact. |
| R8 | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Related representation robustness synthesis. | 2026-07-12 | Repository-relative artifact. |
| R9 | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Related attention/pathway synthesis. | 2026-07-12 | Repository-relative artifact. |

## Appendix

### Public-Safe Selection Record

| Field | Value |
|---|---|
| Candidate paper units | 75,761 |
| Selection method | Uniform zero-based `Get-Random` index with duplicate rejection |
| Selected index | 9,460 |
| Selected ID | arXiv:2005.07310v2 |
| Used IDs indexed | 344 |
| Candidate units excluded by used ID | 65 |
| Duplicate reselections | 0 |
| 24-hour public-safe cutoff date | 2026-07-11 |
| Dedup locations | Black Lake logs, reports, DEP entries, automation memory, and Black-Lake-Data DEP/report entries |

### Extraction Record

- PDF extractor: `pypdf`.
- Extracted text: 58,111 bytes.
- Local HTML: unavailable.
- Local source package: unavailable.
- Original source files collected into DEP: none.
- Exact local source location: withheld.

### Replication Checklist

- [ ] Resolve or replace the unavailable official code locator.
- [ ] Pin UNITER-base and LXMERT checkpoints and hashes.
- [ ] Verify Flickr30k Entities and Visual Genome licenses/access.
- [ ] Recreate region features and documented splits.
- [ ] Run random-weight and mismatched-caption controls.
- [ ] Repeat probes across seeds with confidence intervals.
- [ ] Add causal head/feature interventions.
- [ ] Compare with at least one current open VLM.
