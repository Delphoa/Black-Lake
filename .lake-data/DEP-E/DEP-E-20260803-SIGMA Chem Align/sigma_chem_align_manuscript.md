---
title: "SIGMA - DEP-E"
generated_at: "2026-08-03 (public date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of structure-invariant alignment and isomorphic decoding for molecular language models."
source_status: "verified complete local PDF and full-paper HTML inspected; public URLs only; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-03"
temporal_cutoff: "arXiv:2603.25062v1 and public author context inspected through 2026-08-03"
primary_url: "https://arxiv.org/abs/2603.25062"
stable_identifier: "arXiv:2603.25062v1; DOI 10.48550/arXiv.2603.25062"
confidence_summary: "High for source identity and method/result transcription; medium for empirical interpretation; low for external chemical utility and reproducibility."
safety_scope: "research evaluation only; no wet-lab, clinical, synthesis, or autonomous chemical-design authority"
distribution_notes: "PDF, HTML, metadata, extracted text, caches, and other original source files remain local and were not redistributed."
---

# SIGMA - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2603.25062v1 | https://arxiv.org/abs/2603.25062 | Metadata is not used alone for method or result claims. | 2026-08-03 | Inspected |
| S2 | SIGMA paper | Primary artifact | PDF | arXiv:2603.25062v1; 15 pages | https://arxiv.org/pdf/2603.25062 | Complete local copy inspected and withheld. | 2026-08-03 | Integrity-verified and inspected |
| S3 | SIGMA paper | Primary artifact | Full-paper HTML | arXiv:2603.25062v1 | https://arxiv.org/html/2603.25062 | Complete local copy inspected and withheld; not an abstract page. | 2026-08-03 | Integrity-verified and inspected |
| S4 | arXiv DOI | Persistent identity | DOI | 10.48550/arXiv.2603.25062 | https://doi.org/10.48550/arXiv.2603.25062 | Public persistent locator. | 2026-08-03 | Recorded |
| S5 | Xinyu Wang publications | Author context | Web page | 2026 publication listing | https://www.xinyuwang1209.com/publications/ | Author-maintained context; no code claim inferred from absence alone. | 2026-08-03 | Inspected |
| S6 | FGBench Chemistry DEP | Related research | Markdown | DEP-E-20260716 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-FGBench%20Chemistry/fgbench_chemistry_manuscript.md | Repository synthesis only; no source file copied. | 2026-08-03 | Inspected |
| S7 | Graph Alignment DEP | Related research | Markdown | DEP-E-20260722 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Graph%20Alignment/graph_alignment_manuscript.md | Repository synthesis only; no source file copied. | 2026-08-03 | Inspected |
| S8 | Equivariant Contrastive DEP | Related research | Markdown | DEP-E-20260721 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Equivariant%20Contrastive/equivariant_contrastive_manuscript.md | Repository synthesis only; no source file copied. | 2026-08-03 | Inspected |
| S9 | Black Lake README and DEP rules | Repository authority | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Filing, source locality, attribution, and commit rules. | 2026-08-03 | Inspected |
| S10 | Black-Lake-Data README | Companion authority | Markdown | Live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion DEP and attribution context. | 2026-08-03 | Inspected |

Authors: Xinyu Wang, Fei Dou, Jinbo Bi, and Minghu Song. The arXiv record identifies SIGMA as a cs.LG preprint submitted on 2026-03-26, with secondary subjects cs.AI and q-bio.QM, and notes submission to ICML 2026. The author publication page lists it as a 2026 arXiv preprint. No acceptance or peer-reviewed publication record was established in the inspected sources.

The local source unit was complete before review. The PDF measured 2,358,330 bytes, began with `%PDF-`, and contained a trailing `%%EOF`. The full-paper HTML measured 361,481 bytes, contained 66,317 visible body characters after script/style removal, had article/LaTeXML markers, 91 heading or section markers, and seven paper-structure terms. Exact local paths are intentionally omitted from this public artifact.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S2-S3 | Primary paper | Introduction, method, equations, Algorithm 1, Tables 1-3, Figures 4-8, conclusion, impact statement, and appendices | Problem, method, setup, reported metrics, implementation boundary, and limitations | High for transcription | No experiment rerun; source files withheld |
| E2 | S1 and S4 | Official metadata | Title, authors, version, date, subjects, DOI, page/figure count, and submission status | Bibliographic identity and temporal boundary | High | Metadata does not validate empirical results |
| E3 | S2-S3 Tables 1-2 | Primary empirical evidence | TIS, validity, uniqueness, novelty, internal diversity, FCD, PMO scores, scaffold counts, and run count | Reported performance and comparison claims | High for reporting | Three PMO runs; baseline provenance and uncertainty remain limited |
| E4 | S2-S3 Sections 3-4 and Appendix B-C | Primary method evidence | Functional-equivalence views, probe suffix, projection head, dense alignment, IsoBeam, ZINC split, hyperparameters, and hardware | Mechanism and reproduction requirements | High | Projection dimension differs between method text and appendix/table |
| E5 | S5 | Author context | Publication listing and SIGMA summary | Author-context and release-status cross-check | Medium | Absence of a code link is not proof of permanent absence |
| E6 | S6-S8 | Related DEP evidence | Chemistry benchmark controls, graph alignment, and equivariant contrastive evaluation | Cross-source synthesis and implementation cautions | Medium-high | No joint experiment with SIGMA |
| E7 | S9-S10 and process records | Repository/process authority | DEP placement, public-safe attribution, source locality, and dedup/no-source rules | Deposition compliance | High | Not research evidence |

## Executive Summary

SIGMA addresses a known tension in SMILES-based molecular generation: a single molecular graph can have many valid string traversals, while a standard autoregressive model treats those strings as separate sequences. The authors call the resulting representation problem trajectory divergence and manifold fragmentation. SIGMA keeps the efficient sequence representation but adds structure-aware supervision: pairs of syntactically different views are required to encode the same graph and share a valid suffix, and an InfoNCE-style loss aligns their projected hidden states token by token. IsoBeam extends the same structural identity idea to decoding by pruning valid candidates that duplicate a structure already represented in the beam. The paper presents the method in the complete arXiv paper and official HTML [E1](https://arxiv.org/html/2603.25062).

The source-reported experiments use a GPT-2 Small backbone trained on ZINC-250k. SIGMA reports TIS `0.041`, validity `0.998`, uniqueness `0.814`, novelty `0.798`, internal diversity `0.910`, and FCD `0.752` in the unconditional generation table. In PMO tasks, the paper reports similar peak optimization scores but larger scaffold counts in several tasks; for Osimertinib, it reports `7,731 +/- 190` scaffolds for SIGMA versus `5,667 +/- 941` for the baseline over three runs [E3](https://arxiv.org/html/2603.25062).

Reviewer confidence is high for the identity, mechanism, and transcription of the paper's reported evidence; medium for the claim that the method improves exploration within this benchmark; and low for external chemical utility or reproducibility. The main boundaries are one dataset and random split, small qualitative visualization samples, three-run PMO summaries, missing public implementation at review time, unclear normalization of stereochemistry and tautomers, the runtime cost of repeated partial-structure validation, and a source inconsistency between `d_proj=128` in the method text and a 256-dimensional projection head in Appendix B/Table 3. These results do not establish synthesis feasibility, drug efficacy, clinical value, or autonomous chemical-design authority.

## Detailed Summary

### Problem Context

SMILES linearizes molecular graphs into sequences that Transformer language models can process efficiently. The linearization is not unique: traversal order, branch order, and starting atom can change the string without changing the underlying graph. Standard sequence likelihood can therefore assign different hidden trajectories to structurally equivalent prefixes. The source argues that this creates syntax-defined clusters, weakens sample efficiency, and lets beam search spend capacity on isomorphic duplicates [E1](https://arxiv.org/html/2603.25062).

Randomized SMILES augmentation exposes a model to multiple views, but the paper argues that passive exposure may not force local invariance at each decoding step. Graph generators encode structure more directly but can be more expensive or less scalable. SIGMA is positioned between these alternatives: maintain a sequence backbone, use explicit graph equivalence to supervise latent alignment, and apply structural pruning only where it is useful during decoding.

### Functional-Equivalence View Construction

The training pair is not defined by arbitrary string similarity. SIGMA samples distinct traversal histories and requires two prefixes to be compatible with the same suffix. The paper states a dual consistency condition: the prefixes must differ, and concatenating each prefix with the shared suffix must reconstruct the same molecular graph under an InChIKey hashing oracle. When an incomplete prefix has an open ring or branch, a chemically stable probe suffix is appended temporarily for verification. The probe is an evaluation aid, not part of the model's intended sequence.

Structural negatives are chosen so that a negative prefix plus the shared suffix does not hash to the same graph. This is intended to keep the contrastive boundary chemical rather than purely syntactic. Appendix C further describes cutting a non-ring bond, adding an attachment marker, and producing canonical and randomized views of the same subgraph.

### Architecture and Objective

The backbone is GPT-2 Small: 12 Transformer decoder layers, 12 attention heads, hidden size 768, maximum sequence length 128, and approximately 124M trainable parameters. A projection head is used only for the structural objective so that the backbone can retain syntax-sensitive features needed for next-token prediction. The main method text states `d_proj=128`, while Appendix B and Table 3 state a 768-to-256 projection head. This unresolved version or documentation mismatch is material for reproduction.

For a positive pair, the model processes two views with shared weights. The normal language-model loss is computed from the backbone logits. Projected token states are normalized and compared with cosine similarity. At each suffix position, the positive state is contrasted with structural negatives using temperature `tau=0.1`; the loss is averaged across the suffix and added to the NLL with a balancing coefficient `lambda`. The paper's gradient argument is that shared suffix inputs cause the alignment gradient to flow backward into the prefix representation, making the suffix objective a proxy for prefix invariance. This is a source argument, not a separately proven guarantee for all model configurations.

### IsoBeam Decoder

IsoBeam expands a beam with top-k candidates ordered by cumulative log probability. An invalid partial SMILES is kept because future tokens may close a ring or branch. A valid partial is parsed and assigned a structural identifier, described as an InChIKey derived through RDKit. If the identifier is already in the current beam, the lower-probability candidate is pruned; otherwise it is retained and the identifier is recorded. The algorithm uses a hash map for constant-time duplicate checks after structure parsing.

This design trades extra chemistry validation for a more diverse beam. It is not automatically safe to assume that valid partial strings have stable or task-appropriate identity semantics. A reproduction must specify treatment of stereochemistry, tautomerism, disconnected fragments, attachment markers, sanitization failures, and whether the identifier reflects partial structure, completed molecule, or a normalized form.

### Data and Training

The paper trains on ZINC-250k, described as 250,000 commercially available drug-like molecules, with a 220,000/20,000/10,000 random train/validation/test split. It uses a character-level tokenizer with 69 tokens, randomized SMILES generated on the fly with RDKit, two views per molecule, batch size 64, 50 epochs, AdamW, peak learning rate `5 x 10^-4`, weight decay `0.01`, gradient clipping at 1.0, 2,000 warmup steps, and temperature `0.1`. The reported environment is PyTorch 2.1.0, RDKit 2023.09.5, Transformers 4.35.0, and one NVIDIA A100 40GB GPU [E4](https://arxiv.org/html/2603.25062).

The random split is practical for a first benchmark but leaves open questions about scaffold, series, stereochemical, and temporal separation. Molecular language data are also widely reused, so pretraining or benchmark contamination should be considered before treating novelty or generalization as established.

### Experimental Results

The unconditional-generation table compares graph and sequence baselines. SIGMA reports TIS `0.041`, lower than RandSMILES `2.677` and LTCL `1.698`, which is consistent with stronger latent agreement under the paper's metric definition. It reports validity `0.998`, uniqueness `0.814`, novelty `0.798`, internal diversity `0.910`, and FCD `0.752`. FCD is lower than the displayed sequence baselines CharRNN `0.965`, RandSMILES `0.892`, and LTCL `0.834`; the table also includes graph baselines with different reported validity and FCD values. These are source values, not independently recomputed metrics.

The PMO benchmark uses the REINVENT protocol and includes multiproperty objectives such as Sitagliptin, Zaleplon, Fexofenadine, Osimertinib, and Perindopril plus median-molecule tasks. The paper reports means and standard deviations over three runs. SIGMA generally improves scaffold count and diversity, while peak scores are close to baseline. The Osimertinib example is the strongest narrative: `7,731 +/- 190` versus `5,667 +/- 941` scaffolds. The table also contains tasks where gains are smaller, so the claim is best described as a benchmark-specific exploration advantage rather than a universal improvement.

The beam-width experiment varies `K` from 100 to 50,000. The source says standard beam search saturates near 5,000 because additional candidates are isomorphic variants, while IsoBeam continues to find distinct scaffolds and exceeds 11,000 at `K=50,000`, approximately twice the baseline. The paper does not provide a full latency, energy, or memory curve across the same widths, and RDKit validation cost may change the operational conclusion.

### Limitations Disclosed or Identified

The impact statement acknowledges dual-use concerns for generative chemistry and relies on standard safety protocols and responsible code release. This artifact therefore treats any implementation as research-only and evaluation-bounded. The paper does not supply wet-lab validation, synthesis feasibility, toxicity evidence, pharmacological efficacy, or a clinical path.

The paper says code and pretrained models will be made publicly available upon acceptance. The inspected arXiv and author context did not establish an available author-designated implementation repository. The result is a clear reproduction boundary: a competent reviewer can inspect the method and metrics, but cannot rerun the full pipeline from a pinned public release based on the inspected sources alone.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | SMILES-based autoregressive models can map structurally equivalent graphs to divergent latent trajectories. | Author claim and conceptual framing | E1 | Directly supported as the source's problem definition; its prevalence across models requires broader measurement. | Medium-high |
| C2 | SIGMA aligns equivalent views with a token-level contrastive objective over shared suffix trajectories. | Source-supported mechanism | E1, E4 | Supported by the equations, view-construction description, and appendix. | High |
| C3 | IsoBeam reduces isomorphic redundancy by pruning structure identifiers in the beam. | Source-supported algorithm | E1, E4 | Algorithm and prose are clear; exact behavior depends on chemistry parsing and identity normalization. | High for transcription |
| C4 | SIGMA improves TIS, FCD, and validity over the displayed sequence baselines on ZINC-250k. | Author-reported empirical result | E3 | Table values support the within-benchmark comparison, but no rerun or statistical test was performed here. | Medium-high |
| C5 | SIGMA improves goal-directed exploration. | Author-reported empirical result | E3 | Scaffold-count gains, including Osimertinib, support a narrow PMO claim; three runs and one benchmark family limit generalization. | Medium |
| C6 | IsoBeam approximately doubles distinct-scaffold discovery at beam width 50,000. | Author-reported scaling result | E3, E4 | Supported by the paper's Figure 6 narrative; cost-quality evidence is incomplete. | Medium |
| C7 | SIGMA maximizes mutual information between equivalent paths. | Author theoretical framing | E1 | InfoNCE-style alignment is present, but direct mutual-information measurement is absent. | Low-medium |
| C8 | The work establishes chemical validity, synthesis feasibility, or drug-design utility. | Unsupported implication | No supporting evidence | Rejected; the source has no wet-lab, synthesis, clinical, or external utility validation. | High rejection confidence |

## Methodology

- `Research objective`: Preserve the paper's mechanism, evidence scope, limitations, reproducibility boundary, and safe implementation implications for a DEP-E research artifact.
- `Sources inspected`: Complete local PDF and official full-paper HTML; official arXiv metadata and DOI; author-maintained publication page; three related Black Lake DEP manuscripts; live Black Lake and Black-Lake-Data READMEs; and exact public repository searches for the paper ID and title.
- `Discovery strategy`: Enumerate the local archive with `rg --files -g "*.pdf"`; collapse paths to parent paper units; derive identifiers; scan Black Lake artifacts, automation memory, metadata-only inventory, and live repository contexts; freeze a sorted pool; sample with uniform PowerShell `Get-Random`; validate the selected source unit; then inspect primary text and related DEP evidence.
- `Inclusion criteria`: Full-paper method, data, evaluation, appendix, source-integrity evidence, author release context, and related DEP entries with concrete overlap in molecular benchmarking, graph alignment, or invariance-aware contrastive learning.
- `Exclusion criteria`: Abstract-only evidence for detailed claims; unverified code or dataset assumptions; local absolute paths; original source-file redistribution; wet-lab, clinical, synthesis, or harmful chemical operationalization; and background citations not needed for the selected paper's mechanism or related-entry synthesis.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Author claims, direct paper evidence, reviewer interpretation, negative availability findings, and implementation proposals are labeled separately. Numerical values are kept with their metric direction, baseline context, and run-count limits.
- `Uncertainty handling`: Missing public code, documentation inconsistency, random-split limitations, proxy metrics, three-run reporting, incomplete normalization policy, and no independent reproduction remain explicit rather than being smoothed into a deployment claim.
- `Random selection`: 75,960 PDFs became 75,957 parent units; 75,640 prior-ID units and 185 identifier-incomplete units were excluded; a sorted pool of 132 units was sampled at zero-based index 23; duplicate reselections were zero.
- `Dedup/reselection validation`: Exact ID, DOI, normalized title, slug, Black Lake artifact, automation memory, metadata inventory, same-paper 24-hour marker, and live exact ID/title searches found no owner; the first valid draw was accepted.
- `Source-gate validation`: The selected PDF and full-paper HTML passed all required structural checks before review. The unit was complete initially, so no repair process was invoked.

## Scope, Constraints, and Assumptions

- `Scope`: Source-grounded review of SIGMA's structural-invariance hypothesis, view construction, contrastive objective, IsoBeam decoder, reported evaluation, limitations, and bounded research-to-implementation translation.
- `Temporal boundary`: Public sources and repository context inspected on 2026-08-03; primary paper version is arXiv:2603.25062v1.
- `Evidence limits`: No experiment, code, pretrained model, chemical oracle, or dataset was executed. The author states that code and models will be released upon acceptance, but no public implementation was established in the bounded search.
- `Assumptions`: The arXiv record, DOI, and author publication page identify the same v1 preprint; table values are transcribed as displayed; `+/-` denotes the source's reported standard-deviation notation.
- `Constraints`: Public artifacts must contain no local paths or source files. Chemistry-related examples are research-only, synthetic or benchmark-oriented, and must not provide wet-lab, synthesis, or harmful-design instructions.
- `Out of scope`: Clinical decisions, drug efficacy, toxicity conclusions, synthesis planning, autonomous molecule design, proprietary dataset assessment, and claims of acceptance or production readiness.
- `Intended use`: DEP preservation, research review, replication planning, benchmark governance, and safe implementation ideation.
- `Audience`: Molecular ML researchers, benchmark maintainers, representation-learning engineers, and reviewers evaluating evidence quality.
- `Reproducibility boundary`: Full-text mechanism and reported metrics are inspectable; independent reproduction requires a pinned implementation, preprocessing and normalization policy, source data manifests, seeds, exact oracle behavior, and measured compute.
- `Data sensitivity`: Public research topic; source files and any molecular payloads remain local and are not redistributed by this artifact.

## Observations

- `Observed pattern`: The paper aligns training trajectories and decoding candidates using related notions of structural equivalence. This is conceptually coherent, but the two uses operate at different stages and need separate cost and failure analysis.
- `Observed pattern`: SIGMA's largest displayed gains are in TIS and scaffold exploration, while peak PMO scores are often similar. This suggests the method's strongest value proposition is exploration and representation consistency, not universal objective optimization.
- `Technical implication`: The identity oracle is part of the learning and search specification. A change in RDKit version, sanitization, stereochemistry, tautomer policy, or attachment-point encoding can change positive pairs and pruning decisions.
- `Technical implication`: The projection head is a sensible way to separate syntax-sensitive next-token prediction from structure-sensitive alignment, but the 128 versus 256 dimensionality discrepancy blocks faithful reproduction until resolved.
- `Contradiction or tension`: The paper describes a strict shared-suffix protocol, while Appendix C describes canonical and randomized views of a cut subgraph. These may be compatible, but the exact mapping from prefix construction to suffix alignment should be made executable and unambiguous.
- `Reviewer hypothesis`: A structure-aware beam can improve diversity even when the learned latent space changes little, so IsoBeam should be ablated independently from SIGMA rather than treated as a single inseparable gain.
- `Open question`: Whether the reported scaffold advantage survives scaffold splits, out-of-distribution chemotypes, and explicit stereochemical evaluation is not established.

## Considerations

The benchmark uses a random split of a widely used dataset. A future evaluation should include scaffold or series splits, a contamination audit, and clear treatment of repeated or near-duplicate molecules. Novelty and FCD are useful proxies but do not establish synthetic accessibility, biological activity, or safety. Scaffold count is a diversity measure, not a substitute for objective quality.

IsoBeam introduces a potentially large validation cost because it parses many partial sequences. The reported A100 setup and batch-processing note are not enough to decide whether the method is efficient in a practical service or research loop. A deployment-style audit should report wall-clock latency, GPU and CPU utilization, memory, invalid-prefix rate, cache hit rate, and quality at each beam width.

The chemistry domain has dual-use risk. Safe follow-on work should use public benchmark data, bounded offline evaluation, synthetic structure identifiers where possible, and human review. It should not produce synthesis instructions, toxicity-optimization recipes, or autonomous selection of real-world compounds for consequential use.

## Strengths

- The paper identifies a concrete failure mode of sequence linearization and gives it an operational name, trajectory divergence, that can be measured.
- The positive-pair construction includes an explicit graph-equivalence oracle rather than relying only on random augmentation.
- The projection-decoupled architecture acknowledges the tension between syntax needed for generation and invariance desired for representation learning.
- Dense token-level alignment is mechanistically connected to autoregressive decoding rather than applied only to a global pooled vector.
- IsoBeam turns structure identity into a decoding constraint and reports a beam-width scaling experiment instead of only a single beam size.
- The paper includes implementation details for dataset split, tokenizer, optimizer, software environment, GPU, and beam-width range, which improves the replication starting point even though code is not public.
- The source explicitly acknowledges chemical dual-use concerns and does not claim clinical or experimental validation.

## Weaknesses

- The evaluation is concentrated on ZINC-250k and a PMO benchmark family, with a random split and no demonstrated scaffold or external-domain transfer.
- PMO results use three runs and report standard deviations, but the paper does not show significance tests or robust uncertainty analysis across tasks.
- The t-SNE analysis uses 10 molecules and 50 views per molecule, so it is illustrative rather than a broad quantitative validation.
- The paper's source text is inconsistent about projection dimension: the method gives `d_proj=128`, while Appendix B/Table 3 give 256.
- The public implementation and pretrained models were not available in the bounded search; the paper's promised release is conditional on acceptance.
- The exact normalization and failure policy for stereochemistry, tautomers, disconnected graphs, attachment markers, and invalid partial SMILES is not fully specified.
- Repeated RDKit checks may change the latency and memory profile materially at beam widths up to 50,000; the paper does not publish a complete cost-quality frontier.
- FCD, TIS, novelty, uniqueness, internal diversity, and scaffold count are proxy metrics. They do not establish synthesis feasibility or biological utility.
- The contrastive formulation is described as mutual-information maximizing, but no direct mutual-information measurement is presented.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Pin the equivalence oracle | Reproducibility | Chemistry identity decisions affect both positive pairs and pruning | Stable cross-version behavior | Requires explicit normalization policy and test fixtures | Publish oracle version, fixtures, and pass/fail cases for rings, stereochemistry, tautomers, and attachment points |
| Add scaffold and series splits | Generalization | Random splits can overstate transfer across related molecules | More credible out-of-distribution evidence | Lower scores and more data-management work | Report random, scaffold, series, and temporal split results with contamination checks |
| Separate SIGMA from IsoBeam | Attribution | Training and decoding changes may contribute differently | Clearer causal attribution | More runs and larger evaluation matrix | Four-way ablation: baseline, SIGMA-only, IsoBeam-only, and combined |
| Publish cost-quality curves | Systems | Structure checking can dominate large-beam decoding | Practical beam-width selection | Requires profiling across hardware and batch sizes | Report latency, memory, valid outputs, unique scaffolds, and objective score at each `K` |
| Resolve projection dimensions | Implementation | Architecture ambiguity prevents faithful reproduction | Unblocks code-paper conformance | Small documentation change, possibly checkpoint incompatibility | Add a single canonical config and assert output dimension in training tests |

## Potential Implementations

1. `Equivalence-aware representation benchmark`: Use public or synthetic molecular views to measure TIS-like trajectory agreement, validity, uniqueness, novelty, diversity, and leakage across declared transformations. Keep the oracle versioned and report failures rather than coercing invalid prefixes into positives.
2. `Research-only structure-aware decoder`: Implement a bounded local decoder that caches synthetic or authorized structure IDs, compares standard beam with IsoBeam, and records candidate count, pruning, latency, memory, valid completion rate, and distinct-structure count. Include a conservative fallback to standard beam when parsing or identity checks fail.
3. `Chemistry benchmark conformance service`: Combine FGBench-style construction audits with graph-alignment and equivariant-contrastive diagnostics. The service should produce a versioned evidence bundle, reject ambiguous splits or normalization, and keep all chemical payloads within the authorized evaluation boundary.

## Three Ways to Exercise This Research

1. `Synthetic trajectory audit`: Objective: test the logic of shared-suffix alignment without chemical data. Inputs: short token routes, declared structure IDs, and synthetic negatives. Method: create equivalent and non-equivalent route pairs, run the acceptance oracle, and report false-positive and false-negative cases. Output: an auditable pair-validation table. Success criterion: all hand-labeled toy cases receive the expected equivalence label. Stop condition: stop when the oracle is ambiguous or an implementation begins making claims about real molecules.
2. `Public ZINC metric reproduction`: Objective: reproduce the reported metric definitions under an authorized, pinned benchmark setup. Inputs: an eventual public SIGMA release, the stated ZINC split, fixed seeds, and a versioned chemistry toolkit. Method: run baseline, SIGMA-only, IsoBeam-only, and combined conditions, then report TIS, validity, uniqueness, novelty, internal diversity, FCD, scaffold count, and compute cost. Output: a table with confidence intervals and split manifests. Success criterion: central values and metric directions are within a predeclared tolerance. Stop condition: stop if code, data license, normalization, or source version cannot be pinned.
3. `Decoder cost frontier`: Objective: determine whether structure-aware pruning is worthwhile at different beam widths. Inputs: a safe benchmark workload, a standard decoder, a bounded IsoBeam implementation, and resource telemetry. Method: sweep `K` over a small predefined set, record valid completions, unique structures, scaffold count, latency, memory, and parse failures, and compare fallback behavior. Output: a cost-quality frontier. Success criterion: identify a beam width that improves distinct-structure yield without exceeding an agreed resource budget. Stop condition: stop on repeated parser failures, unbounded memory growth, or evidence that identity normalization is unstable.

## Example MVP Product

- `Product name`: Structure-Aware ChemLM Evaluation Gate.
- `Target user`: A molecular-ML researcher or benchmark maintainer validating a new sequence generator in an offline, authorized environment.
- `Problem`: A model can look strong on string likelihood or validity while duplicating equivalent molecular structures, leaking related scaffolds across splits, or trading diversity for objective quality without clear evidence.
- `Core workflow`: Register paper/model/data/oracle versions; validate pair and split manifests; run baseline, invariant-training, and structure-aware-decoding evaluations; compute a metric vector; profile resource use; and produce a review bundle with accepted claims, failed gates, and fallback recommendations.
- `Data requirements`: Public or authorized molecular benchmark data, declared graph/view transformations, train/validation/test manifests, normalization fixtures, synthetic negatives, and no unapproved sensitive or proprietary payloads.
- `Architecture`: Local-only Python runner; versioned preprocessing and oracle adapter; model adapter; standard and structure-aware decoder adapters; metric calculator; resource telemetry; Markdown/JSON evidence report; and human approval gate before any external use.
- `Success metrics`: Correct oracle fixtures, no split leakage, reproducible metric calculations, TIS reduction without unacceptable validity loss, distinct-structure improvement at a declared resource budget, and complete provenance for every reported number.
- `Risk controls`: Research-only scope; no wet-lab or synthesis outputs; no autonomous consequential selection; local processing for source and molecular data; explicit parser-failure handling; structure-oracle version pinning; standard-decoder fallback; resource ceilings; and human review of any conclusion.
- `Limitations`: The MVP cannot establish chemical activity, safety, synthesis feasibility, clinical value, or generalization beyond its benchmark. It depends on valid identity semantics, licensed data, available code, and careful metric interpretation.
- `MVP boundary`: No model training service, no real-world compound recommendation, no external deployment, and no inference from benchmark scores to therapeutic decisions.
- `Deployment model`: Local-only batch runner or notebook in an authorized research environment.
- `Evaluation plan`: Unit tests for oracle fixtures; split-leakage checks; deterministic smoke tests; four-way ablation; repeated-seed metrics; resource profiling; and independent review of source and license boundaries.
- `Failure modes`: False equivalence, missed equivalence, parser instability, data leakage, metric gaming, scaffold-count inflation without objective value, memory blow-up at large beams, and source/version drift.
- `Maintenance plan`: Pin chemistry-toolkit versions and fixtures; refresh benchmark manifests; review oracle changes; invalidate old results after model or data changes; and retain a standard-decoder fallback.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| FGBench Chemistry - DEP-E | Related DEP and molecular benchmark review | Functional-group comparison construction, leakage, validity, imbalance, and downstream-claim boundaries | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-FGBench%20Chemistry/fgbench_chemistry_manuscript.md; arXiv:2508.01055 |
| Graph Alignment - DEP-E | Related DEP and graph representation review | Alignment/uniformity, graph-aware equivalence, and representation evaluation | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Graph%20Alignment/graph_alignment_manuscript.md; arXiv:2308.09292 |
| Equivariant Contrastive - DEP-E | Related DEP and contrastive review | Transformation-aware invariance and augmentation transfer | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Equivariant%20Contrastive/equivariant_contrastive_manuscript.md; arXiv:2211.05290 |
| Randomized SMILES augmentation | Methodological neighbor cited by SIGMA | Baseline strategy that exposes sequence models to alternate linearizations | arXiv:1703.07076 |
| Learning-order autoregressive models | Graph-generation neighbor cited by SIGMA | Graph-based autoregressive alternative and baseline context | arXiv:2503.05979 |
| ZINC | Dataset and benchmark context cited by SIGMA | Source of the reported 250k-molecule generation benchmark | https://zinc15.docking.org/ |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2603.25062 | Identity, authors, version, date, subjects, abstract, and source links | 2026-08-03 | Metadata record; detailed claims use full text |
| R2 | https://arxiv.org/pdf/2603.25062 | Complete paper, tables, figures, appendix, and source-reported results | 2026-08-03 | Complete local copy inspected; not redistributed |
| R3 | https://arxiv.org/html/2603.25062 | Searchable full paper, algorithm, method, tables, and appendix | 2026-08-03 | Complete local copy inspected; not redistributed |
| R4 | https://doi.org/10.48550/arXiv.2603.25062 | Persistent arXiv identity | 2026-08-03 | Public DOI |
| R5 | https://www.xinyuwang1209.com/publications/ | Author publication listing and release context | 2026-08-03 | Author context; no code availability inferred from absence alone |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-FGBench%20Chemistry/fgbench_chemistry_manuscript.md | Molecular benchmark and chemistry-evaluation bridge | 2026-08-03 | Related DEP manuscript |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Graph%20Alignment/graph_alignment_manuscript.md | Graph alignment and uniformity bridge | 2026-08-03 | Related DEP manuscript |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Equivariant%20Contrastive/equivariant_contrastive_manuscript.md | Contrastive and equivariance bridge | 2026-08-03 | Related DEP manuscript |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Processed-repository authority and source locality | 2026-08-03 | Live README inspected before drafting |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-08-03 | Live README inspected before drafting |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion DEP and attribution context | 2026-08-03 | Live README inspected before drafting |
| R12 | https://arxiv.org/abs/1703.07076 | Randomized SMILES methodological context | 2026-08-03 | Cited by SIGMA; not independently reviewed as a full paper |
| R13 | https://arxiv.org/abs/2503.05979 | Learning-order graph-generation context | 2026-08-03 | Cited by SIGMA; not independently reviewed as a full paper |
| R14 | https://zinc15.docking.org/ | Dataset context | 2026-08-03 | Public dataset locator; no data copied |

The private local source unit is recorded here only as `verified complete PDF plus full-paper HTML retained locally`; the exact filesystem path and all source bytes are intentionally withheld from the public artifact.

## Appendix

### Selection Audit

- Enumeration command: `rg --files -g "*.pdf"` against the configured local arXiv archive root.
- Unit model: each PDF parent directory counted as one paper unit; nearby metadata informed identity and title checks.
- Pool: 75,960 PDFs; 75,957 parent units; 75,640 prior-ID exclusions; 185 identifier-incomplete units; 132 eligible units.
- Random draw: sorted eligible parent-unit pool; PowerShell `Get-Random`; zero-based index 23; duplicate exclusions 0; reselections 0.
- Acceptance: exact ID, DOI, normalized title, slug, artifact, memory, metadata-inventory, live-repository, and 24-hour checks found no owner; complete source gate passed before review.

### Source-Gate Checklist

- PDF size at least 10 KB: pass.
- PDF begins with `%PDF-`: pass.
- PDF contains trailing `%%EOF`: pass.
- Full-paper HTML at least 5 KB: pass.
- Body has at least 2,000 characters after removing scripts and styles: pass.
- Article/main/LaTeXML marker: pass.
- At least two heading or section markers: pass.
- At least two structure terms: pass.
- Abstract-only, error, conversion-notice, missing, or truncated classification: rejected; the selected unit was complete.

### Reproduction Checklist

1. Pin the paper version, model configuration, projection dimension, tokenizer, ZINC split manifest, RDKit and Transformers versions, seeds, and hardware.
2. Implement and test the equivalence oracle on rings, branches, attachment points, stereochemistry, tautomers, disconnected fragments, and invalid partials.
3. Run baseline, SIGMA-only, IsoBeam-only, and combined conditions with repeated seeds.
4. Report TIS, validity, uniqueness, novelty, internal diversity, FCD, scaffold count, objective quality, latency, memory, parser failures, and pruned candidates together.
5. Add scaffold/series splits, contamination checks, and an explicit stop condition preventing benchmark scores from being used as chemical or clinical authority.

### Attribution and Source Boundary

This manuscript is a generated, public-safe research artifact. Original PDF, full-paper HTML, metadata HTML, source archive, extracted text, cache, and any chemical payload were not committed, staged, uploaded, or attached. Public claims should be traced to the URLs in `## Source References` and the evidence IDs in `## Evidence Ledger`.
