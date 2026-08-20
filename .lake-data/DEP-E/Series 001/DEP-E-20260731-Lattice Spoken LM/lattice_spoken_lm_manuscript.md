---
title: "Lattice Spoken LM - DEP-E"
generated_at: "2026-07-31 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of two-stage neural lattice language-model pretraining for spoken-language understanding."
source_status: "Verified complete local PDF, full-paper HTML fallback, and metadata HTML inspected; all source files withheld."
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-31"
temporal_cutoff: "Public primary sources and repository context inspected through 2026-07-31."
primary_url: "https://arxiv.org/abs/2007.02629"
stable_identifier: "arXiv:2007.02629v2; DOI:10.18653/v1/2020.acl-main.347"
confidence_summary: "High for source identity, method transcription, and displayed results; medium for causal attribution; low for current-system transfer or deployment readiness."
safety_scope: "Offline research evaluation and authorized spoken-language prototyping only."
distribution_notes: "No PDF, HTML, metadata page, source archive, dataset, code, cache, extracted text, receipt, render, verification record, or local path is redistributed."
---

# Lattice Spoken LM - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public-Safe Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | `2007.02629v2` | https://arxiv.org/abs/2007.02629 | Metadata only; not the paper body. | 2026-07-31 | Inspected |
| S2 | arXiv PDF | Primary paper | PDF | `2007.02629v2` | https://arxiv.org/pdf/2007.02629 | Verified local copy withheld. | 2026-07-31 | Inspected in full and rendered |
| S3 | ar5iv full paper | Primary paper rendering | HTML | Latest rendering of `2007.02629` | https://ar5iv.labs.arxiv.org/html/2007.02629 | Approved fallback after official HTML routes were unavailable; local copy withheld. | 2026-07-31 | Inspected in full |
| S4 | ACL Anthology | Official venue record | HTML | `2020.acl-main.347` | https://aclanthology.org/2020.acl-main.347/ | ACL metadata and publication-license context. | 2026-07-31 | Inspected |
| S5 | ACL DOI | Official identifier | DOI | `10.18653/v1/2020.acl-main.347` | https://doi.org/10.18653/v1/2020.acl-main.347 | Persistent publisher identity. | 2026-07-31 | Resolved through official record |
| S6 | Lattice-ELMo | Official implementation | Repository | commit `202e369c0d41ff4e62353073478d25fec4b18cca` | https://github.com/MiuLab/Lattice-ELMo | No visible repository license established; code not run or redistributed. | 2026-07-31 | README, tree, and commit inspected |
| S7 | Ontology ASR Correction | Related Black Lake research | Markdown | DEP-A-20260731 | `.lake-data/DEP-A/DEP-A-20260731-Ontology ASR Correction/2606.13464-whitepaper-review.md` | Synthesis context only. | 2026-07-31 | Inspected |
| S8 | Cued Speech MLLM | Related Black Lake research | Markdown | DEP-E-20260720 | `.lake-data/DEP-E/DEP-E-20260720-Cued Speech MLLM/cued_speech_mllm_manuscript.md` | Synthesis context only. | 2026-07-31 | Inspected |
| S9 | HeadRouter Audio | Related Black Lake research | Markdown | DEP-A-20260720 | `.lake-data/DEP-A/DEP-A-20260720-HeadRouter Audio/2604.23717-whitepaper-review.md` | Synthesis context only. | 2026-07-31 | Inspected |
| S10 | Workflow evidence | Selection and integrity evidence | Private records | Current automation run | Withheld local context | Used only for selection, deduplication, source integrity, and locality validation. | 2026-07-31 | Verified |

**Paper metadata.** Chao-Wei Huang and Yun-Nung Chen; submitted 2020-07-06 and revised 2020-11-02; ACL 2020 short paper, pages 3764-3769; arXiv subjects `cs.CL`, `cs.AI`, and `cs.LG`; arXiv DOI https://doi.org/10.48550/arXiv.2007.02629.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4, S5 | Official metadata and venue records | Title, authors, dates, version, subjects, venue, pagination, DOI values | Source identity and publication status | High | Metadata and abstract do not validate results |
| E2 | S2 | Primary PDF | Full method, equations, Figures 1-2, Tables 1-2, ablations, conclusion, references | Technical reconstruction and displayed results | High for transcription | No independent experiment or proof |
| E3 | S3 | Primary full-paper rendering | Searchable section text, equations, dataset counts, hyperparameters, accuracies, and result prose | Cross-check of E2 | High for transcription | Fallback conversion may alter typography |
| E4 | S6 | Official implementation | Repository scope, Python requirement, provided SNIPS data, non-redistribution statement for ATIS/SWDA/MRDA, run commands | Artifact availability and reproduction boundary | Medium-high | Code not executed; no visible license file established |
| E5 | S7-S9 | Related DEP artifacts | ASR correction, multimodal evidence fusion, and audio-token selection mechanisms | Cross-DEP synthesis | Medium | No joint experiment or claim transfer |
| E6 | S10 | Private process evidence | Random selection counts, dedup scopes, integrity repair, file validation, and no-source-upload checks | Workflow validity | High | Public artifact intentionally withholds local identity |

## Executive Summary

Huang and Chen propose a neural lattice language model that transfers contextual language pretraining from ordinary text sequences to ASR lattices. The central insight is structural: a sequence is a degenerate lattice, so an LSTM language model trained on abundant written text can initialize a LatticeLSTM and then be adapted on scarcer target-task lattices. The model predicts posterior-weighted outgoing lattice transitions, freezes the adapted encoder, and supplies contextualized node representations to downstream intent or dialogue-act classifiers.

Across ATIS, SNIPS, SWDA, and MRDA, the source reports that the proposed model improves on an ASR 1-best biLSTM+ELMo baseline, with relative error reduction from `3.2%` to `42%`. It is the strongest displayed ASR-output system on SNIPS, SWDA, and MRDA; BERT-base is slightly higher on ATIS. Ablations lower accuracy when either pretraining stage is removed. These are useful, coherent results, but the evidence is bounded: at least three runs are averaged without variance or significance tests, SNIPS speech is synthetic, historical ASR pipelines dominate the setup, and the claimed efficiency/data-demand advantages are not measured directly.

The review's confidence is high for source identity, method transcription, and displayed numbers; medium for attributing gains uniquely to the proposed mechanism; and low for direct transfer to current ASR, transformer, streaming, or production systems. The durable implementation lesson is to preserve structured uncertainty through explicit interfaces and receipts rather than collapse it before the downstream task can use it.

## Detailed Summary

### Problem Context

Conventional spoken-language understanding commonly receives a single ASR transcript. That modular interface is convenient but discards alternative recognition hypotheses and their probabilities. N-best lists, word-confusion networks, and lattices preserve more uncertainty, but most pretrained language models in the paper's period were trained on linear written text and could not directly consume graph-structured ASR output.

The paper asks how to obtain contextualized lattice representations without pretraining an expensive lattice model on a massive speech-derived lattice corpus.

### Lattice Representation

An input lattice is an edge-labeled directed acyclic graph. Each edge records its previous node, next node, word label, and transition probability. A LatticeRNN traverses the graph in topological order. For each node, the model pools incoming edge hidden states using the ASR transition probabilities. Any ordinary word sequence is representable as a linear-chain lattice, making the sequential RNN a strict special case.

This containment relation enables weight transfer: an LSTM and LatticeLSTM with the same cell architecture can share initialization even though one operates on sequences and the other on DAGs.

### Lattice Language-Model Objective

At node `n`, the target distribution over the next word is induced by outgoing lattice-edge probabilities. A linear decoder maps the node representation to a softmax distribution. Training minimizes KL divergence between the posterior-derived target distribution and the predicted distribution. A sequential language model is recovered when every node has only the linear-chain successor.

The objective therefore trains the encoder to summarize all paths leading to a node while predicting the distribution of plausible next transitions rather than a single next token.

### Two-Stage Pretraining

**Stage 1** trains a bidirectional sequential LSTM language model on general written text using the ELMo cell architecture.

**Stage 2** constructs a bidirectional LatticeLSTM with the same cells, initializes it from Stage 1, reverses lattices for the backward direction, and continues pretraining on target-task lattices using the lattice language-model objective.

The authors argue this is more approachable than training on a large lattice corpus because written text is easier to collect and sequential RNNs are easier to parallelize. The architecture supports that argument, but the paper does not report a matched resource or data-efficiency experiment.

### Target Classifier

The adapted lattice LM is frozen. Hidden states from its layers are linearly combined into contextualized node embeddings. A newly trained two-layer LatticeLSTM consumes those embeddings, max-pools over nodes, and applies a linear softmax classifier with cross-entropy loss.

The classifier hidden size is `300`. Adam uses learning rate `0.0001` for language-model pretraining and `0.001` for classifier training. The checkpoint with best validation accuracy is evaluated.

### Datasets and Results

Intent detection uses ATIS and SNIPS; dialogue-act recognition uses SWDA and MRDA. SNIPS originally contains text, so the study synthesizes a spoken version using a commercial text-to-speech service. ATIS is transcribed by a WSJ-trained Kaldi recognizer, while the other datasets use a Kaldi-released ASR system. Word error rates range from `15.55%` on ATIS to `45.61%` on SNIPS.

The proposed model reports accuracies of `95.84`, `95.37`, `62.88`, and `72.04` on ATIS, SNIPS, SWDA, and MRDA. The matched ASR 1-best ELMo baseline reports `94.99`, `91.98`, `61.65`, and `68.52`. BERT-base is higher on ATIS (`95.97`) but lower on the other three displayed tasks. Removing Stage 1 or Stage 2 lowers every displayed proposed-model result. Evaluating the lattice-trained model on 1-best inputs also lowers every result, supporting the value of retaining the lattice at inference within this setup.

### Implementation Artifact

The official repository provides Python training and evaluation commands for 1-best baselines, LatticeLSTM baselines, lattice language-model fine-tuning, and the final classifier. It provides a processed SNIPS route and states that ATIS, SWDA, and MRDA cannot be redistributed. The repository is useful implementation evidence but is not a reproduction receipt: code was not run, no visible license file was established, and the historical environment and restricted datasets require deliberate reconstruction.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Sequential language-model weights can initialize a LatticeLSTM because a sequence is a linear-chain lattice. | Source-supported mechanism | E2, E3 | Structurally supported when recurrent cell architecture and parameter shapes match. | High |
| C2 | The two-stage model improves over the ASR 1-best ELMo baseline on all four displayed datasets. | Author-reported empirical claim | E2, E3 | Numerically supported by Table 2; no uncertainty or significance evidence is provided. | High for transcription; medium for robustness |
| C3 | Both pretraining stages contribute. | Author-reported ablation claim | E2, E3 | Removing either stage lowers all four displayed accuracies, but interactions and variance remain unreported. | Medium-high |
| C4 | Lattice input remains useful after pretraining. | Author-reported empirical claim | E2, E3 | Proposed lattice results exceed its 1-best evaluation on every displayed dataset. | Medium-high |
| C5 | The approach reduces speech-data demand and is more efficient. | Author claim with architectural rationale | E2, E3 | Plausible but not directly measured with data-volume, runtime, memory, or compute evidence. | Low-medium |
| C6 | The results generalize to current spoken-language systems. | Unsupported implication | No supporting evidence | Not established across modern ASR models, streaming constraints, accents, channels, languages, or transformer-based graph encoders. | High rejection confidence |
| C7 | Structured uncertainty should be preserved across system interfaces when downstream tasks can exploit it. | Reviewer interpretation | E2-E5 | Strong design hypothesis grounded in the paper and related artifacts; requires current-system validation. | Medium |

## Methodology

- `Research objective`: Determine the paper's mechanism, evidence, limitations, implementation relevance, and relationship to existing Black Lake research.
- `Sources inspected`: Complete PDF; verified full-paper HTML fallback; arXiv metadata; ACL Anthology record; both DOI identities; official implementation repository; exactly three related DEP artifacts.
- `Discovery strategy`: Required local `rg --files -g "*.pdf"` enumeration, repository-wide dedup search, local source-integrity inspection and repair, full-paper text extraction, six-page visual PDF review, official-record browsing, repository inspection, and conceptual DEP search.
- `Selection method`: `75,960` PDFs were collapsed to `75,957` parent units. `476` units matched used IDs and `185` identifier-incomplete units were withheld. PowerShell `Get-Random` selected zero-based eligible index `21,552` from `75,296` eligible units.
- `Deduplication`: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and fetched Black-Lake-Data equivalents were searched by arXiv ID, DOI values, canonical/normalized title, implementation token, and planned slugs. No duplicate or recent same-paper marker was found; public-safe cutoff date `2026-07-30`.
- `Source integrity`: The initial unit was partial because full-paper HTML was absent. Review paused while a bounded publisher-broker repair preserved the valid PDF, fetched metadata, obtained an approved ar5iv full-paper fallback, updated private provenance/verification records, and left no partial files.
- `Inclusion criteria`: Primary or official near-primary evidence, complete paper body, implementation material directly linked by the authors, and related DEPs with concrete mechanism overlap.
- `Exclusion criteria`: Abstract-only technical claims, secondary summaries as primary evidence, unverified current-performance claims, unexecuted code claims, local path disclosure, and source-file redistribution.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product, safety/ethics, and replication analysis.
- `Evidence handling`: Author claims, displayed measurements, reviewer calculations, interpretations, and unsupported implications are labeled separately and tied to ledger IDs.
- `Uncertainty handling`: Missing variance, restricted datasets, old dependencies, absent efficiency measurements, non-executed code, and transfer uncertainty remain explicit.
- `Version control`: arXiv `v2`, ACL Anthology ID, both DOI values, and official repository commit `202e369c0d41ff4e62353073478d25fec4b18cca` are pinned.
- `Reviewer stance`: DEP-ready source preservation, critical paper review, implementation translation, and bounded replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The lattice language-model objective, staged transfer, classifier design, dataset/evaluation evidence, official implementation, and relationships to uncertainty-preserving speech systems.
- `Temporal boundary`: Public evidence and repository context inspected through `2026-07-31`.
- `Evidence limits`: No experiment, code path, model, or dataset was executed; no source package was available; run-level dispersion and modern baselines are absent.
- `Assumptions`: The canonical latest arXiv record is `v2`; the verified fallback rendering represents the complete paper; displayed table values are authoritative for transcription.
- `Constraints`: Restricted speech datasets, unclear repository licensing, privacy and consent concerns around speech, historical dependencies, compute cost, and no source redistribution.
- `Out of scope`: Current state-of-the-art ranking, clinical or legal use, production deployment, participant-level fairness claims, and independent reproduction.
- `Intended use`: Research preservation, architecture review, uncertainty-aware SLU prototyping, benchmark planning, and follow-on replication.
- `Audience`: Speech/NLP researchers, ML engineers, data-governance reviewers, and product teams evaluating uncertainty-preserving voice interfaces.
- `Reproducibility boundary`: The full paper and code locator support a reconstruction plan, not a reproduced result.
- `Operational boundary`: The artifact discusses authorized, privacy-preserving speech processing only; it does not authorize collection or reuse of restricted corpora.
- `Data sensitivity`: Speech, transcripts, speaker identity, dialogue history, and derived lattices may be personal or restricted even when represented as graph state.

## Observations

- `Observed pattern`: The largest displayed gain over ASR 1-best ELMo occurs on synthetic-spoken SNIPS, which also has the highest WER; this is consistent with lattices helping under recognition ambiguity, but one dataset does not establish a causal WER-gain law.
- `Observed pattern`: Plain biLatticeLSTM is not enough; the proposed pretraining contributes materially in the displayed comparison.
- `Technical implication`: A modern system should retain raw ASR output, lattice topology, arc posteriors, pruning settings, and model version so downstream gains or failures can be traced.
- `Technical implication`: Arc posterior calibration is part of representation quality because the pooling rule weights hidden states by those probabilities.
- `Contradiction or tension`: The paper motivates efficiency but evaluates accuracy only; architectural economy and realized end-to-end efficiency remain separate claims.
- `Evidence-quality implication`: "Averaged over at least three runs" is insufficient for close comparisons such as the `0.13`-point ATIS gap to BERT-base.
- `Open question`: Would current transducer/CTC n-best graphs, neural rescoring, or encoder-decoder confidence structures preserve the same transfer advantage?
- `Reviewer hypothesis`: The staged special-to-general lifting pattern could transfer beyond RNN lattices to graph-aware transformer adapters if the uncertainty distribution and cost boundary remain explicit.

## Considerations

**Posterior quality.** Weighted pooling assumes arc probabilities are meaningful. Miscalibration, aggressive pruning, duplicated labels, or decoder bias can overemphasize the wrong paths. Calibration and oracle-lattice diagnostics should accompany downstream accuracy.

**Privacy and governance.** Speech, dialogue acts, and recognition alternatives may expose identities, intent, errors, or sensitive context. A derivative system should minimize retention, encrypt stored lattices, separate tenants, support deletion, restrict purpose, and avoid logging raw speech or transcripts by default.

**Dataset rights.** The official repository states that ATIS, SWDA, and MRDA cannot be redistributed. Reproduction requires authorized acquisition and dataset-specific terms, not copying source-era bundles into a public artifact.

**Operational cost.** Lattices increase graph size, batching complexity, memory traffic, and tail latency. Beam size and posterior pruning need an explicit cost-quality frontier with conservative 1-best or refusal fallback.

**Monitoring.** Production-like testing should join source audio identity, ASR version, lattice statistics, posterior entropy, SLU prediction, confidence, fallback, latency, and correction outcomes without exposing raw sensitive content.

**Model age.** ELMo and LatticeLSTM remain historically informative but should be treated as a mechanism baseline. Current adoption decisions require comparisons against modern speech encoders, lattice-aware transformers, n-best rerankers, and end-to-end models under matched evidence.

## Strengths

- Defines a clear graph-structured language-model objective rather than using a lattice only as a downstream feature container.
- Exploits the formal containment of sequences within lattices to make staged transfer technically coherent.
- Separates abundant written-text pretraining from scarce target-lattice adaptation.
- Evaluates both intent detection and dialogue-act recognition across four datasets and materially different WER levels.
- Includes strong source-era baselines, lattice-only baselines, two stage-removal ablations, and a 1-best evaluation of the proposed model.
- Reports exact dataset sizes, class counts, WER, oracle WER, optimizer, learning rates, and classifier hidden size.
- Provides an official code repository with a concrete training flow.
- Makes the information loss of 1-best ASR interfaces tangible and testable.

## Weaknesses

- No standard deviations, confidence intervals, significance tests, seeds, per-example outcomes, or failure slices.
- "At least three" runs is imprecise and prevents exact uncertainty reconstruction.
- Efficiency and reduced speech-data demand are argued but not measured.
- Synthetic TTS speech for SNIPS limits ecological validity.
- Missing ATIS audio makes the manual and ASR test sets non-identical.
- Best-validation selection is underdocumented.
- Historical ASR, ELMo, and RNN baselines limit current decision usefulness.
- Restricted datasets and no established repository license complicate reproduction and reuse.
- No calibration analysis links ASR arc probabilities to downstream reliability.
- No speaker, accent, channel, language, lattice-density, or tail-latency analysis.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish per-run and paired outcomes | Statistical evidence | Close accuracy differences need uncertainty | Credible effect estimates | More storage and analysis | Seeded paired bootstrap or hierarchical tests |
| Measure staged-transfer cost | Efficiency | Architecture alone does not prove efficiency | Decision-useful compute/data frontier | Instrumentation overhead | Match accuracy, data volume, wall time, memory, and energy |
| Calibrate arc posteriors | Representation quality | Weighted pooling inherits ASR probability errors | Better reliability and debugging | Calibration may shift ranking | Reliability diagrams, ECE, Brier score, oracle comparisons |
| Sweep lattice pruning | Cost-quality tradeoff | Lattice size governs information and cost | Deployable operating envelope | Larger experiment grid | Beam/posterior thresholds versus accuracy, latency, and memory |
| Use natural and shifted speech | External validity | Synthetic SNIPS and source-era audio are narrow | Better transfer evidence | Data and consent burden | Accent, noise, channel, speaker, and language slices |
| Add modern baselines | Comparative evidence | Current systems use different encoders/decoders | Contemporary relevance | Significant engineering effort | Matched evidence access and fixed compute budgets |
| Publish an explicit code license and environment | Reproducibility | Availability is not legal or executable portability | Safer reuse and replay | Maintenance burden | Clean-environment build and table-level smoke test |
| Add conservative fallback | Operational safety | Invalid lattices or low confidence should not force output | Bounded failure behavior | Lower automated coverage | Coverage-risk and fallback-utility curves |

## Potential Implementations

1. **Lattice-versus-1-best evaluation gateway.** `User`: speech ML engineer. `Goal`: measure whether structured ASR alternatives improve an authorized classifier. `Core mechanism`: validate a lattice, run matched 1-best and lattice-aware paths, and compare prediction, confidence, latency, and failure. `Required inputs`: public or authorized audio-derived lattices, labels, pinned ASR/model configurations. `Outputs`: paired metric ledger and per-slice disagreement report. `Risk controls`: local processing, data minimization, encryption, no raw content in logs, and explicit fallback. `Evaluation`: paired accuracy, calibration, latency, memory, and worst-slice outcomes.
2. **Posterior and pruning audit tool.** `User`: ASR/SLU evaluator. `Goal`: determine whether arc probabilities and pruning preserve useful evidence. `Core mechanism`: sweep posterior calibration and beam thresholds while holding the downstream model fixed. `Required inputs`: versioned lattices, labels, calibration split, and resource telemetry. `Outputs`: cost-quality-calibration frontier and counterexample set. `Risk controls`: immutable splits, no cross-user aggregation without authorization, and capped graph sizes. `Evaluation`: ECE, Brier score, oracle coverage, downstream accuracy, graph size, and tail latency.
3. **Reversible context-aware correction sandbox.** `User`: conversational-system researcher. `Goal`: combine lattice alternatives with structured dialogue memory without erasing the raw transcript. `Core mechanism`: retain original ASR output, generate candidate corrections from lattice and memory evidence, require calibrated support, and record accept/abstain reason. `Required inputs`: authorized conversation context, lattice, ontology version, and evaluation labels. `Outputs`: candidate edits, provenance receipt, and correction-risk report. `Risk controls`: purpose limitation, access control, deletion, no autonomous consequential action, and human review. `Evaluation`: WER/CER, correction harm rate, abstention utility, privacy review, and drift.

## Three Ways to Exercise This Research

1. **Tiny lattice pooling test.** `Objective`: verify the representation mechanism on a synthetic DAG. `Inputs`: three toy lattices with normalized posteriors and hand-computable hidden states. `Method`: implement topological traversal and weighted pooling, compare with a linear-chain special case, then perturb posterior calibration. `Output`: deterministic node-state and sensitivity report. `Success criterion`: exact agreement with hand calculations and visible degradation under miscalibration. `Stop condition`: invalid topology, posterior sum, or hidden-state shape. `Safety boundary`: synthetic data and bounded local execution only.
2. **Matched 1-best versus lattice benchmark.** `Objective`: test the central empirical claim on a small authorized dataset. `Inputs`: immutable audio/label manifest, one ASR version, derived 1-best text and lattices, two matched classifiers, and fixed seeds. `Method`: run paired folds, retain per-example outcomes, report accuracy/calibration/latency/memory, and stratify by WER and lattice density. `Output`: reproducible evidence card. `Success criterion`: replayable runs and a predeclared statistically supported difference. `Stop condition`: split leakage, unequal evidence access, or missing resource telemetry. `Safety boundary`: no source redistribution or production ranking.
3. **Stage-transfer ablation.** `Objective`: test whether cheap sequential pretraining improves scarce-lattice adaptation. `Inputs`: synthetic or authorized text/lattice data, one cell architecture, fixed compute budgets, and four conditions: scratch, Stage 1 only, Stage 2 only, both. `Method`: match parameter count and tuning, sweep lattice-data fractions, and publish all runs. `Output`: data-efficiency and compute frontier. `Success criterion`: the two-stage path improves a predeclared metric at matched total cost across multiple seeds. `Stop condition`: unmatched compute, unstable training, or inaccessible data rights. `Safety boundary`: no claim beyond the tested model and dataset.

## Example MVP Product

- `Product name`: Lattice Evidence Gate.
- `Target user`: Speech/NLP research engineer or model-governance reviewer.
- `Problem`: A 1-best ASR API hides uncertainty, while raw lattices can be large, poorly calibrated, privacy-sensitive, and difficult to audit.
- `Core workflow`: Import an authorized public-safe lattice manifest; validate topology and probabilities; derive the 1-best path; run matched baseline and lattice-aware classifiers; display disagreements, entropy, calibration, resource cost, and failure slices; export a source-safe receipt.
- `Data requirements`: Public or explicitly authorized lattices and labels, immutable split manifest, ASR/model/version pins, and no raw secrets or unapproved speech.
- `Architecture`: Local CLI or notebook with lattice validator, normalization/calibration module, baseline runner, lattice-aware adapter, paired evaluator, telemetry collector, and receipt exporter.
- `Success metrics`: Reproducible paired accuracy, calibration improvement, bounded P95/P99 latency and memory, replay success, fallback utility, and reviewer comprehension.
- `Risk controls`: Local-only default, data minimization, graph-size ceiling, no raw transcript logging, access control, encryption, retention/deletion policy, visible abstention, and no autonomous consequential decision.
- `Limitations`: Does not reproduce the historical paper by default; does not prove ASR posterior correctness, production readiness, cross-language transfer, or legal permission to use restricted corpora.
- `MVP boundary`: One lattice schema, one small authorized dataset, one 1-best baseline, one lattice-aware adapter, and offline evaluation only.
- `Deployment model`: Local CLI/notebook; no hosted speech ingestion.
- `Evaluation plan`: Unit tests for graph validity and pooling; malformed-lattice tests; paired benchmark with fixed seeds; calibration/pruning sweep; privacy and receipt-schema review.
- `Failure modes`: Cycles, disconnected nodes, unnormalized or stale posteriors, graph explosion, evidence leakage, distribution shift, false confidence, slow tail cases, and misleading aggregate gains.
- `Maintenance plan`: Version lattice schema, ASR/model pins, calibration method, benchmark manifest, and receipt format; rerun smoke tests after every dependency or model change.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| *Adapting Pretrained Transformer to Lattices for Spoken Language Understanding* | Author follow-up paper | Extends pretrained-model adaptation to transformer lattice inputs and tests a neighboring mechanism. | https://arxiv.org/abs/2011.00780 |
| *Self-Attentional Models for Lattice Inputs* | Primary methodological neighbor | Provides a transformer-era approach for representing lattice structure. | https://aclanthology.org/P19-1115/ |
| *Deep Contextualized Word Representations* | Primary baseline | Defines ELMo, the sequential pretrained representation used for Stage 1. | https://aclanthology.org/N18-1202/ |
| Official Lattice-ELMo repository | Official implementation | Supplies the historical training/evaluation flow and dataset-availability boundary. | https://github.com/MiuLab/Lattice-ELMo |
| Ontology ASR Correction DEP | Related Black Lake research | Structured conversational evidence for reversible ASR correction after recognition. | `.lake-data/DEP-A/DEP-A-20260731-Ontology ASR Correction/2606.13464-whitepaper-review.md` |
| Cued Speech MLLM DEP | Related Black Lake research | Multimodal evidence fusion for spoken recognition under scarce labeled data. | `.lake-data/DEP-E/DEP-E-20260720-Cued Speech MLLM/cued_speech_mllm_manuscript.md` |
| HeadRouter Audio DEP | Related Black Lake research | Task-aware audio representation selection with an explicit cost-quality boundary. | `.lake-data/DEP-A/DEP-A-20260720-HeadRouter Audio/2604.23717-whitepaper-review.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2007.02629 | Identity, authors, dates, version, subjects, abstract context, arXiv DOI, and source locators. | 2026-07-31 | Metadata only. |
| R2 | https://arxiv.org/pdf/2007.02629 | Full method, figures, tables, experiments, ablations, conclusion, and references. | 2026-07-31 | Verified local PDF withheld. |
| R3 | https://ar5iv.labs.arxiv.org/html/2007.02629 | Searchable full-paper rendering and quantitative cross-checks. | 2026-07-31 | Approved fallback; verified local HTML withheld. |
| R4 | https://arxiv.org/e-print/2007.02629 | Source-package availability check. | 2026-07-31 | Unavailable after the bounded attempt. |
| R5 | https://doi.org/10.48550/arXiv.2007.02629 | Persistent arXiv identity. | 2026-07-31 | arXiv-issued DOI. |
| R6 | https://aclanthology.org/2020.acl-main.347/ | ACL venue, publisher, pagination, citation, and publication-license context. | 2026-07-31 | Official venue record. |
| R7 | https://doi.org/10.18653/v1/2020.acl-main.347 | Persistent ACL publication identity. | 2026-07-31 | Publisher DOI. |
| R8 | https://github.com/MiuLab/Lattice-ELMo | Official implementation, dataset restrictions, and run flow. | 2026-07-31 | Commit pinned; not executed; no visible license established. |
| R9 | https://arxiv.org/abs/2011.00780 | Author follow-up on pretrained transformers and lattices. | 2026-07-31 | Primary related reading. |
| R10 | https://aclanthology.org/P19-1115/ | Self-attentional lattice-input context. | 2026-07-31 | Primary related reading. |
| R11 | https://aclanthology.org/N18-1202/ | ELMo baseline context. | 2026-07-31 | Primary related reading. |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260731-Ontology%20ASR%20Correction/2606.13464-whitepaper-review.md | Related structured ASR-correction synthesis. | 2026-07-31 | Related DEP only. |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Cued%20Speech%20MLLM/cued_speech_mllm_manuscript.md | Related multimodal spoken-recognition synthesis. | 2026-07-31 | Related DEP only. |
| R14 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260720-HeadRouter%20Audio/2604.23717-whitepaper-review.md | Related task-aware audio-token synthesis. | 2026-07-31 | Related DEP only. |

## Appendix

### A. Source-Integrity Summary

- Initial classification: `partial`.
- Repair result: `complete`.
- PDF: `879,903` bytes, valid header, trailing EOF, six unencrypted pages.
- Full-paper HTML: `161,386` bytes, `30,357` body characters, document marker, `35` headings, six structure terms.
- Metadata HTML: `41,604` bytes.
- Unexpected partial files: `0`.
- Source package: unavailable after one bounded broker attempt.
- Source policy: every original source, cache, receipt, render, and verification artifact remains local and withheld.

### B. Reproduction Checklist

- [ ] Obtain each restricted dataset through an authorized channel and document terms.
- [ ] Pin the official repository commit and create an explicit environment manifest.
- [ ] Reconstruct the source-era ELMo and Kaldi assumptions or define a justified modern-equivalence boundary.
- [ ] Publish lattice schema, pruning settings, posterior normalization, and graph statistics.
- [ ] Fix immutable train/validation/test splits and check speaker or dialogue leakage.
- [ ] Match parameter counts, evidence access, data volume, and compute across ablations.
- [ ] Record exact run count, seeds, per-run results, confidence intervals, and paired tests.
- [ ] Report calibration, accuracy, latency, memory, graph size, and failure outcomes.
- [ ] Stratify by WER, lattice density, entropy, class, speaker, accent, noise, and channel.
- [ ] Preserve every timeout, invalid lattice, divergence, and fallback.
- [ ] Compare against current 1-best, n-best, lattice-aware transformer, and end-to-end baselines.
- [ ] Publish source-safe derived receipts without redistributing speech, transcripts, or source files.

### C. Selection and Dedup Summary

- Random method: required PDF enumeration, unique parent units, identifier resolution, global used-ID exclusion, then uniform `Get-Random`.
- Candidate counts: `75,960` PDFs; `75,957` units; `75,296` eligible after `476` used-ID exclusions and `185` identifier-incomplete exclusions.
- Selected zero-based eligible index: `21,552`.
- Used-paper index: `1,690` arXiv base IDs.
- Duplicate/recent-marker reselections: `0`.
- Dedup scopes: both repository families, automation memory, and the four Black Lake artifact areas.
- Public-safe 24-hour cutoff date: `2026-07-30`.

### D. Decision Boundary

This artifact supports investigating uncertainty-preserving spoken-language representations, graph-aware pretraining, and matched lattice-versus-1-best evaluation. It does not establish current state of the art, production readiness, legal access to restricted datasets, calibration of a particular ASR lattice, or safety of an autonomous voice decision system.
