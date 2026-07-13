---
title: "Tech Intel 1100 - DEP-E"
generated_at: "2026-07-13T00:02:31Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of ten research records collected in DEP-20260712-Tech Intel 1100, emphasizing evaluation reliability, systems constraints, privacy-aware inference, and reproducibility."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-13"
temporal_cutoff: "2026-07-13"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260712-Tech%20Intel%201100"
stable_identifier: "DEP-20260712-Tech Intel 1100"
confidence_summary: "Medium: all ten arXiv records were checked, five had inspectable full HTML, and one source-title mismatch was found."
safety_scope: "non-sensitive research review"
distribution_notes: "Public URLs only; no paper files were redistributed."
---

# Tech Intel 1100 - DEP-E

## Source Metadata

| ID | Source | Authors / Organization | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|---|
| S0 | DEP-20260712-Tech Intel 1100 | Delphoa-Labs / automation deposit | Primary source bundle | Markdown repository deposit | Source DEP at `main` | [Source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260712-Tech%20Intel%201100) | Repository material; attribution retained | 2026-07-13 | Both deposited Markdown files inspected |
| S1 | Ideas Have Genomes | Yifan Zhou et al. | Primary research | arXiv record | arXiv:2607.08758v1 | https://arxiv.org/abs/2607.08758 | License linked on arXiv record | 2026-07-13 | Abstract and metadata inspected |
| S2 | BiSCo-LLM | Yuantian Shao et al. | Primary research | arXiv HTML | arXiv:2607.08643v1 | https://arxiv.org/abs/2607.08643 | Creative Commons link visible on record | 2026-07-13 | Full HTML sections inspected |
| S3 | Contravariance Theory | Dan Yamins; Aran Nayebi | Primary research | arXiv record | arXiv:2607.08561v1 | https://arxiv.org/abs/2607.08561 | License linked on arXiv record | 2026-07-13 | Abstract and metadata inspected |
| S4 | Stop Guessing When to Stop Testing | Ofir Arviv et al.; IBM Research | Primary research | arXiv HTML | arXiv:2607.08522v1 | https://arxiv.org/abs/2607.08522 | arXiv perpetual non-exclusive license | 2026-07-13 | Full HTML methods and results inspected |
| S5 | MatBind | Le Yang et al. | Primary research | arXiv record | arXiv:2607.08470v1 | https://arxiv.org/abs/2607.08470 | License linked on arXiv record | 2026-07-13 | Abstract and metadata inspected |
| S6 | Workload-Preserving DP Synthetic Data | Amir Asiaee; Kaveh Aryan | Primary research | arXiv HTML and official code link | arXiv:2607.08122v1 | https://arxiv.org/abs/2607.08122 | Creative Commons link visible; code repository linked by paper | 2026-07-13 | Full HTML methods, results, and limitations inspected |
| S7 | Score Distributions, Not Cells | Youssef Marrakchi; Davide D'Ascenzo; Sebastiano Cultrera di Montesano | Primary research | arXiv HTML | arXiv:2607.04595v1 | https://arxiv.org/abs/2607.04595 | arXiv perpetual non-exclusive license | 2026-07-13 | Full HTML methods and results inspected; source DEP title mismatch confirmed |
| S8 | Storage-Centric Genomic Analysis | Nika Mansouri Ghiasi; Onur Mutlu | Primary research | arXiv record | arXiv:2607.02552v1 | https://arxiv.org/abs/2607.02552 | License linked on arXiv record | 2026-07-13 | Abstract and metadata inspected |
| S9 | Parallel QEC Decoding | Gabriele Incardona; Davide Ferrari; Michele Amoretti | Primary research | arXiv record | arXiv:2607.08386v1 | https://arxiv.org/abs/2607.08386 | Creative Commons link visible on record | 2026-07-13 | Abstract and metadata inspected |
| S10 | Works on My QPU | Dominik Köster et al. | Primary research | arXiv HTML | arXiv:2607.08348v1 | https://arxiv.org/abs/2607.08348 | arXiv perpetual non-exclusive license | 2026-07-13 | Available HTML and quantitative study summary inspected |

No local source files were collected. Public URLs and repository-relative paths are the preserved provenance.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E0 | S0 | Source DEP | README, ten-item synthesis, attribution block | Deposit scope and original summaries | High | The deposit is a discovery layer, not independent validation |
| E1 | S1 | Primary arXiv record | Benchmark scale, tasks, and reported best-system result | Scientific-lineage evaluation claim | Medium | Abstract-level inspection only |
| E2 | S2 | Primary arXiv full HTML | Storage accounting, baselines, Table III, ablations, discussion | Low-bit compression mechanism and reported performance | High | No code, weights, or hardware reproduction performed |
| E3 | S3 | Primary arXiv record | Formal theory summary and stated conditions | Representation-alignment theory | Medium | Abstract-level inspection; theorem proofs not checked |
| E4 | S4 | Primary arXiv full HTML | Sequential-testing design, Open VLM data, experiments, stopping rules | Adaptive evaluation claim | High | Results were not rerun; paper contains a minor internal code-availability wording tension |
| E5 | S5 | Primary arXiv record | Four-modality contrastive framework and zero-shot retrieval claim | Materials representation claim | Medium | Abstract-level inspection; figures and experiments not checked |
| E6 | S6 | Primary arXiv full HTML | Causal workloads, NA+MI, five benchmarks, coverage/RMSE results, limitations | Privacy-aware causal inference claim | High | No reproduction; HTML math conversion omits some symbols in rendered text |
| E7 | S7 | Primary arXiv full HTML | CDS definition, Tahoe-100M and VCC results, source identity | Population-level evaluation claim and provenance correction | High | No dataset or code execution; no explicit limitations section found |
| E8 | S8 | Primary arXiv record | Four storage-centric systems and reported order-of-magnitude gains | Genomics systems claim | Medium | Abstract-level inspection; component studies not independently checked |
| E9 | S9 | Primary arXiv record | BP+OSD/SVD proposal and evaluation dimensions | Distributed QEC systems claim | Medium | Abstract-level inspection; numerical results not available in inspected text |
| E10 | S10 | Primary arXiv HTML | 127-paper manual sample, nearly 5,000-paper screen, code/execution rates | Quantum reproducibility claim | High | Available HTML was partial; reproduction package was not executed |

## Executive Summary

The selected DEP is best understood as a cross-domain signal about **evaluation units, stopping rules, resource accounting, and reproducibility**, not as one coherent empirical study. The strongest inspected papers share a practical lesson: trustworthy capability claims depend on choosing the right unit of analysis and recording the conditions under which a result was produced.

Three primary findings anchor this review. First, adaptive group-sequential evaluation can stop model testing when a predeclared statistical or practical criterion is met; on the Open VLM Leaderboard, the authors report an example 80% cost reduction for a 2.5-point confidence-interval allowance, while pairwise gaps above two points usually saved at least 60% of evaluation effort (E4). Second, population-level scoring can reverse a misleading single-cell conclusion: on Tahoe-100M, modest per-cell models reached 0.976-0.995 perturbation-level accuracy after pooling predictions, while their per-cell accuracy remained 0.185-0.218 (E7). Third, quantum-computing reproducibility remains weak in the inspected study: only 24.4% of a 127-paper manual sample supplied code artifacts, and 64.5% of those artifacts failed in a clean environment (E10).

The source set also shows that efficiency claims need full accounting. BiSCo-LLM reports a Qwen3-8B WikiText-2 perplexity of 10.18 versus 9.73 at full precision and a seven-task average 1.87 points below the baseline, but the method requires neural decoders, protected channels, adapters, metadata, and category-wise recovery work that must be counted (E2). In privacy-preserving causal analysis, the inspected paper demonstrates a complementary trade-off: generic workloads can minimize point RMSE, whereas causal workloads with noise-aware multiple imputation improve interval calibration at strict privacy budgets, sometimes with much wider intervals (E6).

Reviewer confidence is medium overall: five papers received full-HTML inspection, five were limited to arXiv abstracts and metadata, and no experiments were reproduced. A material provenance error was found: S0 describes arXiv:2607.04595 as a DNA-read classification paper, but the primary record is **Score Distributions, Not Cells**. That mismatch should be corrected in a future source DEP note rather than silently propagated.

## Detailed Summary

### Evaluation should match the decision

S4 reframes benchmark size as a decision variable. The method uses group sequential testing with adjusted thresholds so evaluators can inspect interim results without treating repeated looks as ordinary fixed-sample tests. It supports efficacy, equivalence-margin, precision, threshold, futility, and diminishing-return stopping. The paper evaluates 206 vision-language models across 31 Open VLM benchmarks and reports that the required sample count depends on the decision: large model gaps can be resolved early, while small gaps often require the full dataset. This is more defensible than choosing an arbitrary small subset, but it still relies on assumptions such as approximately normal test statistics, independent observations, and prespecified analysis structure.

S7 makes a related point at a different scale: when perturbation classes overlap at the cell level, per-cell accuracy measures class overlap rather than whether populations differ. Classifier Discrimination Score averages per-cell probability vectors over a perturbation population and ranks candidate perturbations using that pooled profile. On Tahoe-100M, the same linear, MLP, and Transformer models that were weak per cell became near-perfect at perturbation identification after aggregation. On the smaller VCC data, the reported perturbation-level accuracy ranged from 0.615 to 0.860 across listed configurations, still much higher than corresponding per-cell accuracy. The source DEP's description of this arXiv ID is incorrect, so only the primary record's identity and results are used here.

### Systems efficiency requires honest accounting

S2 replaces explicit vector-quantization codebooks with binary spherical codes and compact neural decoders, adds residual coding, and uses category-wise recovery distillation plus a small protected-channel path. Its Qwen3-8B comparison reports 10.18 WikiText-2 perplexity against 9.73 for FP16/BF16 and a 68.05 seven-task average against 69.92. The paper explicitly warns that nominal bit rate is insufficient: decoders, protected payloads, LoRA adapters, and metadata contribute to real storage. It also acknowledges greater calibration and optimization cost than simple post-training rounding.

S8 presents GenStore, MegIS, GRAINS, and SAGe as storage-centric designs intended to reduce data movement and preparation overhead for genomic and metagenomic workloads. The abstract reports one-to-two-order-of-magnitude improvements in performance, energy efficiency, and cost efficiency. Because only the abstract was inspected, this artifact preserves those numbers strictly as author claims rather than verified comparisons.

### Privacy and inference are separate objectives

S6 designs differentially private workloads around moments required by causal estimators, then reconstructs reusable synthetic data with maximum-entropy calibration. Its noise-aware multiple-imputation procedure propagates DP measurement uncertainty into confidence intervals. Across five benchmark settings, the paper reports that generic workloads often retain better point RMSE at looser privacy budgets, while the causal workload with NA+MI is the conservative option when calibrated coverage matters. At the reported strict setting, causal workload plus NA+MI reached near-nominal coverage on four main benchmarks, but intervals widened substantially. The authors identify feature-map choice, discretization error, privacy-dominated uncertainty, and limited generator-family coverage as constraints.

### Reproducibility is part of the result

S10 studies quantum-software reproducibility through a five-question manual framework and a larger automated screen. Its findings connect code availability, machine-readable environments, documentation, hardware descriptions, and executability. The reported 24.4% manual code-availability rate, 64.5% clean-environment failure rate among available artifacts, and 26.8% automated code-availability rate suggest that publication-level method descriptions often do not preserve runnable conditions. The proposed direction—declarative environment specifications and reusable reproduction packages—generalizes beyond quantum computing.

### Remaining discovery threads

S1 proposes structured scientific-lineage evaluation and reports 1,961 lineage traces, 1,085 curated Idea Genome objects, 920 GenomeDiff records, 42 task types, 1,029 exam instances, and only 27.3% exact accuracy for the strongest tested system. S3 states theoretical conditions under which weak affine alignment between minimal deep-network solutions implies stronger privileged-axis alignment. S5 aligns crystal structure, simulated powder X-ray diffraction, density of states, and text into one embedding space. S9 proposes parallel QEC decoding using local SVD preprocessing with belief propagation and ordered-statistics decoding. These are relevant but remain abstract-level leads in this pass.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Adaptive evaluation can reduce benchmark cost while preserving predeclared statistical guarantees. | Author claim supported by inspected methods/results | E4 | Supported within the Open VLM setting; portability depends on assumptions and stopping-rule design. | High |
| C2 | Population-level scoring can be a more valid evaluation unit than per-cell accuracy under class overlap. | Author claim supported by inspected results | E7 | Strong evidence on two datasets; generalization beyond perturbation identification remains to be tested. | High |
| C3 | Extreme low-bit compression must count auxiliary storage and recovery cost, not only nominal codes. | Author claim and reviewer interpretation | E2 | Well motivated and explicitly accounted for in the paper; deployment speed was not validated here. | High |
| C4 | Differential privacy, point accuracy, and interval calibration can favor different workload designs. | Author claim supported by inspected results | E6 | Supported across the paper's benchmarks, with visible approximation and generator-family limits. | High |
| C5 | Quantum research artifacts frequently lack runnable, durable environments. | Author claim supported by study summary | E10 | Quantitatively supported by the study's sample and screen; sampling and automated-detection details were not fully re-audited. | Medium |
| C6 | The selected DEP contains a source-identity mismatch for arXiv:2607.04595. | Reviewer observation | E0, E7 | Direct comparison of the deposited description and primary arXiv record confirms the mismatch. | High |

## Methodology

- `Research objective`: Convert the selected multi-record DEP into a provenance-preserving review that tests its summaries against primary records and identifies reusable research threads.
- `Sources inspected`: Both Markdown files in the source DEP; all ten linked arXiv abstract/metadata pages; available full HTML for S2, S4, S6, S7, and S10.
- `Discovery strategy`: Repository inspection followed by direct primary-URL inspection. No general web search or secondary-source substitution was used.
- `Inclusion criteria`: Every URL attributed by the selected DEP was retained. Empirical detail entered central claims only when methods/results were visible in inspected primary HTML.
- `Exclusion criteria`: Recommender widgets, aggregator pages, unverified code-finder results, and secondary commentary were excluded. Paper PDFs, datasets, and repositories were not downloaded or executed.
- `Analytical approach`: Conceptual, comparative, empirical, implementation, product research, safety/privacy, and replication analysis.
- `Evidence handling`: Sources received stable S/E identifiers; author claims, reviewer observations, and interpretations are labeled separately.
- `Uncertainty handling`: Abstract-only evidence is marked medium confidence; unavailable reproduction evidence is stated; the source-title mismatch is preserved rather than normalized away.
- `Extraction process`: Repository text was read directly; arXiv metadata, abstracts, methods, tables, results, discussions, and limitations were inspected where HTML was available.
- `Version control`: ArXiv v1 identifiers and the source repository's `main` path are recorded; no local execution context is published.
- `Cross-checking`: IDs and titles were compared between the source DEP and primary arXiv records. Selected metrics were checked against primary HTML tables or result text.
- `Reviewer stance`: DEP-ready preservation, critique, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The ten research records attributed by DEP-20260712-Tech Intel 1100 and their cross-cutting implications for dependable research systems.
- `Temporal boundary`: Sources accessed 2026-07-13; arXiv versions were v1 as displayed.
- `Evidence limits`: Five records were abstract-only; no PDFs, datasets, codebases, models, or hardware were executed; some HTML math symbols were missing from rendered extraction.
- `Assumptions`: Stable arXiv identifiers resolve to the cited v1 records and the public repository reflects the selected deposit.
- `Constraints`: Public-only evidence, no redistribution of source papers, no private or clinical data, and no production deployment claims.
- `Out of scope`: Independent replication, peer-review assessment, clinical validation, hardware benchmarking, security testing, and correction of the original source DEP contents.
- `Intended use`: DEP deposition, review planning, evidence triage, and design of auditable research workflows.
- `Audience`: Research engineers, evaluation designers, repository maintainers, and product teams translating research into bounded experiments.
- `Reproducibility boundary`: Readers can re-open the cited records and audit the synthesis, but cannot reproduce empirical results from this artifact alone.
- `Data sensitivity`: Public research metadata and public repository content only.

## Observations

- `Observed pattern`: Several papers improve reliability by changing the unit or timing of evaluation rather than increasing model capacity: interim decision points in S4, population aggregation in S7, workload moments in S6, and environment declarations in S10.
- `Technical implication`: Evaluation protocols should be versioned first-class artifacts with inputs, stopping conditions, aggregation units, uncertainty rules, and environment pins.
- `Contradiction or tension`: Efficiency gains can shift cost rather than remove it. S2 reduces stored weights but adds recovery training and decoders; S4 reduces evaluation samples but needs sequential-test design; S6 improves coverage by accepting wider intervals.
- `Open question`: Which protocol descriptors are sufficiently general to cover AI benchmarks, privacy-preserving inference, biological population scoring, and hardware-dependent experiments without erasing domain-specific assumptions?
- `Reviewer hypothesis`: A common “claim envelope” schema—unit of analysis, evidence budget, stopping rule, environment, and uncertainty—could make heterogeneous DEP artifacts easier to compare and extend.
- `Provenance finding`: The arXiv:2607.04595 mismatch demonstrates why identifier-level validation should precede semantic expansion.

## Considerations

- Statistical stopping rules must be chosen before observing favorable results; post hoc criteria can recreate the reliability problem they aim to solve.
- Aggregation can suppress important within-group variation. S7's CDS is effective for identification but does not preserve the full within-perturbation spread.
- Differential privacy guarantees do not imply valid downstream inference. Analysts must propagate privacy noise and disclose approximation bias.
- Compression comparisons need effective storage, calibration compute, inference kernels, latency, and energy measurements; perplexity alone is insufficient.
- Biomedical and causal examples are research settings, not clinical validation. Dataset consent, representativeness, and governance remain deployment gates.
- Reproducibility packages can still depend on unavailable quantum hardware or cloud services; environment pinning is necessary but not sufficient.
- Source deposits should validate title-ID pairs automatically and record whether evidence is abstract-only, full-text inspected, or reproduced.

## Strengths

- The DEP spans research mechanisms rather than a single application layer, exposing common reliability patterns across models, data, and hardware.
- S4, S6, and S7 provide inspectable methods and evaluation settings that support concrete implementation translation.
- S2 explicitly accounts for auxiliary compression storage and discusses optimization costs, reducing the risk of a misleading bit-rate claim.
- S10 quantifies both artifact availability and actual clean-environment execution, a stronger reproducibility signal than repository presence alone.
- Stable arXiv identifiers allow direct provenance checking and enabled detection of the S7 title mismatch.

## Weaknesses

- The source DEP offers short summaries without methods, evidence grades, version pins beyond URLs, or explicit uncertainty.
- One of ten title/summary pairs is materially inconsistent with its arXiv identifier.
- Half of the records remained abstract-only in this pass, limiting confidence in their numerical and comparative claims.
- No external source files were collected, so long-term review depends on public URLs remaining available.
- No empirical result was rerun; code availability is not equivalent to reproducibility.
- The ten records are thematically broad, so synthesis risks overgeneralization unless claims remain source-local.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add title-ID validation during DEP intake | Provenance | Prevents the S7-style mismatch | Higher trust and fewer propagated errors | API/network dependency | Compare normalized arXiv metadata before commit |
| Add evidence-status fields per finding | Source schema | Distinguishes abstract, full text, code, and reproduction | Faster downstream triage | More authoring overhead | Schema lint plus spot audit |
| Archive permitted source metadata snapshots | Durability | URLs can change or disappear | Better offline provenance | Storage and licensing review | Hash and inventory each snapshot |
| Register evaluation protocols as artifacts | Reproducibility | Stopping, aggregation, and uncertainty choices determine conclusions | Auditable cross-study comparisons | Domain schema complexity | Re-run protocol on synthetic fixtures |
| Add replication budgets | Planning | Separates paper review from independent verification | Clearer confidence progression | Compute and labor | Predefine success and stop conditions |

## Potential Implementations

### DEP provenance gate

- `User`: Repository maintainer or intake agent.
- `Goal`: Prevent identifier, title, date, and source-role mismatches.
- `Core mechanism`: Resolve stable identifiers, compare normalized metadata, and require an evidence-status label.
- `Required inputs`: DEP Markdown, public source URLs, expected titles.
- `Outputs`: Pass/fail report with exact mismatches and inaccessible sources.
- `Risk controls`: Treat remote text as evidence only; do not execute linked code; cache only permitted metadata.
- `Evaluation`: Synthetic mismatch fixtures plus periodic manual audits.

### Adaptive evaluation planner

- `User`: Model evaluation team.
- `Goal`: Match sample cost to a predeclared decision.
- `Core mechanism`: Configure group-sequential looks and stopping rules for precision, efficacy, equivalence, or futility.
- `Required inputs`: Evaluation records, metric definition, error budget, maximum sample count.
- `Outputs`: Decision trace, adjusted intervals, stop reason, and unused-sample estimate.
- `Risk controls`: Lock criteria before results, retain all interim looks, and reject unsupported distributional assumptions.
- `Evaluation`: Coverage simulation and comparison with fixed-sample baselines.

### Research claim envelope registry

- `User`: Research engineer or reviewer.
- `Goal`: Compare heterogeneous studies without collapsing their assumptions.
- `Core mechanism`: Store unit of analysis, evidence budget, aggregation, uncertainty, environment, and reproduction status beside each claim.
- `Required inputs`: Manuscripts, protocols, source metadata, optional run logs.
- `Outputs`: Searchable claim cards and reproducibility gaps.
- `Risk controls`: Public metadata by default, explicit sensitivity labels, and no automatic promotion from “code linked” to “reproduced.”
- `Evaluation`: Inter-reviewer agreement and time-to-audit on a held-out DEP set.

## Three Ways to Exercise This Research

1. `Validate source identity`: Objective—detect provenance defects; inputs—the ten source URLs and deposited titles; method—resolve each identifier and compare normalized title/date/version fields; output—a mismatch report; success criterion—all ten pairs classified; stop condition—halt and mark inaccessible identifiers rather than guessing.
2. `Simulate adaptive stopping`: Objective—test cost/reliability trade-offs; inputs—synthetic paired model scores with known effects; method—compare a fixed sample with a predeclared group-sequential design; output—coverage, sample use, and stop reasons; success criterion—target error control across simulations; stop condition—do not apply to production decisions until assumptions and calibration pass.
3. `Test aggregation units`: Objective—measure when population scoring changes conclusions; inputs—synthetic overlapping class distributions; method—compare per-item accuracy with pooled probability profiles; output—item- and group-level metrics; success criterion—recover group identity without hiding specified subgroup failures; stop condition—reject the aggregate metric if it masks safety-critical variation.

## Example MVP Product

- `Product name`: Claim Envelope
- `Target user`: Research repository maintainer.
- `Problem`: DEP summaries can preserve URLs while still losing source identity, evaluation assumptions, and reproduction status.
- `Core workflow`: Parse a DEP, resolve public identifiers, compare metadata, let a reviewer attach evidence status and claim envelopes, then emit a sanitized validation report.
- `Data requirements`: Public URLs, repository-relative Markdown, normalized metadata, and optional reviewer annotations; no private datasets.
- `Architecture`: Local CLI parser, allowlisted metadata resolvers, deterministic rule engine, Markdown/JSON output, and git diff integration.
- `Success metrics`: 100% detection on seeded title-ID mismatches, zero silent URL substitutions, reviewer agreement on evidence status, and reduced audit time.
- `Risk controls`: No linked-code execution, strict URL allowlist, bounded downloads, sensitivity flags, sanitized logs, and human approval before repository writes.
- `Limitations`: Cannot establish scientific correctness or reproducibility; metadata services may be unavailable; title normalization can produce false positives.
- `MVP boundary`: arXiv identifiers and repository Markdown only; no paper-content scoring.
- `Deployment model`: Local-only CLI in a pre-commit or review workflow.
- `Evaluation plan`: Unit tests for normalization, seeded mismatch fixtures, inaccessible-source tests, and a manual audit of ten historical DEPs.
- `Failure modes`: Redirect confusion, version drift, duplicate titles, and overclaiming when metadata matches but content does not.
- `Maintenance plan`: Version resolver rules, retain fixtures, and review source-platform changes quarterly.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Ideas Have Genomes | Primary preprint | Structured scientific-lineage reasoning and generation benchmark; abstract inspected in this pass | https://arxiv.org/abs/2607.08758 |
| BiSCo-LLM | Primary preprint | Storage-aware extreme low-bit compression; full HTML inspected in this pass | https://arxiv.org/abs/2607.08643 |
| Contravariance Theory | Primary preprint | Conditions for convergent internal representation structure; abstract inspected in this pass | https://arxiv.org/abs/2607.08561 |
| Stop Guessing When to Stop Testing | Primary preprint | Sequential stopping for statistically grounded model evaluation; full HTML inspected in this pass | https://arxiv.org/abs/2607.08522 |
| MatBind | Primary preprint | Cross-modal materials representation anchored on crystal structure; abstract inspected in this pass | https://arxiv.org/abs/2607.08470 |
| Workload-Preserving DP Synthetic Data | Primary preprint and linked official code | Causal workloads and noise-aware inference under DP; full HTML inspected in this pass | https://arxiv.org/abs/2607.08122 |
| Score Distributions, Not Cells | Primary preprint | Correct primary work for arXiv:2607.04595; population-level perturbation evaluation; full HTML inspected in this pass | https://arxiv.org/abs/2607.04595 |
| Storage-Centric Genomic Analysis | Primary preprint | Data-movement and preparation bottlenecks in genomic systems; abstract inspected in this pass | https://arxiv.org/abs/2607.02552 |
| Parallel QEC Decoding | Primary preprint | Parallel decoding design for distributed quantum computing; abstract inspected in this pass | https://arxiv.org/abs/2607.08386 |
| Works on My QPU | Primary preprint | Empirical quantum-research reproducibility study; available HTML inspected in this pass | https://arxiv.org/abs/2607.08348 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [DEP-20260712-Tech Intel 1100](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260712-Tech%20Intel%201100) | Original inventory, summaries, and attribution | 2026-07-13 | Primary source bundle; no local path published |
| R1 | [arXiv:2607.08758v1](https://arxiv.org/abs/2607.08758) | IdeaGene-Bench metadata and abstract-level claims | 2026-07-13 | Primary record; abstract inspected |
| R2 | [arXiv:2607.08643v1](https://arxiv.org/abs/2607.08643) | BiSCo-LLM mechanism, comparisons, accounting, and limitations | 2026-07-13 | Primary record and full HTML inspected |
| R3 | [arXiv:2607.08561v1](https://arxiv.org/abs/2607.08561) | Contravariance theory summary | 2026-07-13 | Primary record; abstract inspected |
| R4 | [arXiv:2607.08522v1](https://arxiv.org/abs/2607.08522) | Sequential-evaluation framework and Open VLM results | 2026-07-13 | Primary record and full HTML inspected |
| R5 | [arXiv:2607.08470v1](https://arxiv.org/abs/2607.08470) | MatBind modalities and shared-space claims | 2026-07-13 | Primary record; abstract inspected |
| R6 | [arXiv:2607.08122v1](https://arxiv.org/abs/2607.08122) | Causal workloads, NA+MI, experiments, and limitations | 2026-07-13 | Primary record and full HTML inspected; paper links official code |
| R7 | [arXiv:2607.04595v1](https://arxiv.org/abs/2607.04595) | Correct source identity, CDS mechanism, Tahoe-100M and VCC results | 2026-07-13 | Primary record and full HTML inspected; conflicts with source DEP description |
| R8 | [arXiv:2607.02552v1](https://arxiv.org/abs/2607.02552) | Storage-centric genomic systems | 2026-07-13 | Primary record; abstract inspected |
| R9 | [arXiv:2607.08386v1](https://arxiv.org/abs/2607.08386) | Parallel distributed QEC decoder proposal | 2026-07-13 | Primary record; abstract inspected |
| R10 | [arXiv:2607.08348v1](https://arxiv.org/abs/2607.08348) | Quantum reproducibility sample and reported rates | 2026-07-13 | Primary record and available HTML inspected |

## Appendix

### Source inventory and validation notes

- Source repository files inspected: `Black-Lake-Data/.lake-data/DEP-20260712-Tech Intel 1100/README.md` and `Black-Lake-Data/.lake-data/DEP-20260712-Tech Intel 1100/daily_research_findings_2026-07-12_1100.md`.
- External source files collected: none. Ten public arXiv records were inspected by URL; five exposed usable full HTML in this pass.
- Provenance defect: the deposited title and summary for arXiv:2607.04595 do not match the primary record. This artifact uses the primary record and leaves correction of the stable source deposit to a follow-on note.
- Reproduction status: no code, dataset, model, statistical analysis, or hardware experiment was rerun.

### Replication checklist

- [ ] Pin source DEP commit and all arXiv versions.
- [ ] Download permitted PDFs and record hashes if durable offline review is approved.
- [ ] Reproduce S4 coverage and sample-saving simulations from the linked official code.
- [ ] Reproduce S7 pooling results on a bounded public subset.
- [ ] Audit S6 confidence-interval coverage with the official repository and documented data scripts.
- [ ] Execute S10's reproduction template in a clean, version-pinned environment.
