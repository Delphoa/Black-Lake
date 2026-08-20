---
title: "FGBench Chemistry - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of functional-group molecular property reasoning data and LLM benchmarking."
source_status: "verified complete v4 PDF and official HTML inspected; source and molecular data withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:2508.01055v4 and official repository inventory inspected through 2026-07-16"
primary_url: "https://arxiv.org/abs/2508.01055v4"
stable_identifier: "arXiv:2508.01055v4; DOI 10.48550/arXiv.2508.01055"
confidence_summary: "High for construction and table transcription; medium for benchmark interpretation; low for downstream molecular-design claims."
safety_scope: "research benchmark analysis only; no wet-lab, clinical, toxicity, or drug-design authorization"
distribution_notes: "Paper files, molecular data, repository contents, caches, images, and extracted text were not redistributed."
---

# FGBench Chemistry - DEP-E

## Source Metadata

| ID | Source | Role | Identifier / Version | Public Locator | Status |
|---|---|---|---|---|---|
| S1 | FGBench paper | Primary full text | arXiv:2508.01055v4; NeurIPS 2025 D&B | https://arxiv.org/abs/2508.01055v4 | Full PDF/HTML inspected |
| S2 | Official FGBench repository | Code/data documentation | `main`; MIT | https://github.com/xuanliugit/FGBench | README/tree inspected; not run |
| S3 | FGBench dataset | Dataset locator | Hugging Face | https://huggingface.co/datasets/xuan-liu/FGBench | Locator identified; not downloaded |
| S4 | Structure-Aware Systems | Related DEP | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-Structure Aware Systems/structure-aware-systems.md` | Inspected |
| S5 | Control Surfaces | Related DEP | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md` | Inspected |
| S6 | Tech Intel 2338 | Related DEP | DEP-E-20260709 | `.lake-data/DEP-E/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` | Inspected |
| S7 | Black Lake READMEs | Repository authority | live default branches | https://github.com/Delphoa/Black-Lake | Inspected |

Authors: Xuan Liu, Siru Ouyang, Xianrui Zhong, Jiawei Han, and Huimin Zhao. Submitted 2025-08-01, revised 2026-02-16. The arXiv record lists NeurIPS 2025 Datasets and Benchmarks and CC BY-SA 4.0. Repository/data component licenses must be checked independently.

## Evidence Ledger

| ID | Basis | Supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | S1 Sections 3 and Appendix A | comparison construction, functional groups, templates | High | no independent chemistry audit |
| E2 | S1 Tables 1-3 | counts, properties, benchmark sampling | High | QA pairs are dependent expansions |
| E3 | S1 Table 4/Appendix B | nine-model results | High for reporting | APIs/models/parsers not rerun |
| E4 | S1 failure/limitations | qualitative errors and missing isomerism | High | narrow examples |
| E5 | S2-S3 | code/data availability, fields, files, licenses | High for inventory | not downloaded/executed |
| E6 | S4-S6 | structure, safety, benchmark governance | Medium | conceptual only |
| E7 | Process records | draw, dedup, repair, cache | High | operational evidence |

## Executive Summary

FGBench converts ten MoleculeNet sources into functional-group-centered molecular comparison and reasoning tasks. Molecules are canonicalized, similar pairs identified, functional-group/alkane differences localized, and comparisons validated before templates generate Boolean and numeric QA. The dataset reports 42,967 comparison pairs, 245 functional groups, 27 alkane lengths, and 625,936 QA items across single-group impact, multiple-group interaction, and direct comparison.

Nine models are tested on 7,146 QA. Best Boolean accuracy is 0.687 for single-group tasks, 0.693 for interactions, and 0.703 for comparisons (o3-mini). GPT-4o drops from 0.667 single to 0.488 interaction; Llama-3.1-70B drops 0.683 to 0.530. Results support the narrow claim that interaction reasoning remains difficult.

Dataset scale needs denominator discipline. Hundreds of thousands of template questions derive from tens of thousands of paired transformations and ten upstream datasets. Scaffold/molecule/pair/source overlap and model pretraining contamination can inflate apparent generalization. Numeric properties use different units/scales, so pooled RMSE is not a universal quality score.

The official repository and dataset strengthen availability. They do not by themselves prove reproducibility: dependencies, APIs, answer parsers, model versions, seeds, data licenses, and source-dataset terms require a pinned audit. FGBench is useful benchmark infrastructure, not evidence that LLM outputs are chemically valid for molecule or drug design.

## Detailed Summary

### Construction

Ten MoleculeNet datasets cover regression and classification properties. Canonical SMILES reduce duplicates; molecular similarity identifies candidate pairs; AccFG localizes atom-level functional-group differences; validation produces comparison tuples with molecule structures, group differences, and property labels. Templates then create questions with numbered SMILES, group identities/positions, connection/disconnection information, and property direction/value targets.

Three dimensions isolate single-group effects, multiple-group interactions, and direct molecule comparison. The design makes task-relevant structure explicit. Yet “single” and “interaction” are operational categories, not causal interventions: paired molecules can differ in context, scaffold, conformation, and correlated substructure.

### Counts and Balance

The comparison set contains 42,967 pairs and the QA set 625,936 rows. Hydroxy groups dominate the listed functional groups (19.04%); C1 alkanes dominate alkane records (80.05%). Rare groups therefore need macro/group-level reporting. Ten source datasets and many property tasks also differ sharply in size and units.

### Benchmark

The 7,146-item subset includes Boolean accuracy, numeric RMSE, and answer validity. Closed models are GPT-4o and o3-mini; open/general/chemistry-tuned models include Llama, Qwen, ChemLLM, nach0, MolInstructions-tuned Llama, and LlaSMol. Separate parsers are used for some models, making parser validity part of performance.

O3-mini leads Boolean tasks but not every numeric RMSE. Llama-3.1-70B has interaction-value RMSE 38.646, while Qwen2.5-7B reports 36.307 but low validity 0.683. Nach0 comparison Boolean accuracy/validity collapse to 0.041/0.149 and its comparison numeric RMSE is extremely large. These show why accuracy, validity, units, and per-dataset breakdowns must travel together.

### Limitations and Availability

The paper explicitly omits position isomerism, chain isomerism, and stereoisomerism, and calls for graph/3D-aware extraction. Failure examples show models may rely on flawed analogies or fail property-direction reasoning. No wet-lab or prospective design evidence exists.

The official MIT repository documents Hugging Face loading, data fields, construction scripts, prompts, result files, and MoleculeNet-derived tables. Its tree also contains committed Python caches and OS metadata, indicating reproducibility hygiene could improve. No files were copied or run in this review.

## Key Claims and Evidence

| Claim | Assessment | Confidence |
|---|---|---|
| FGBench supplies localized FG reasoning data. | Supported by construction and public schema. | High |
| It contains 625,936 QA over 42,967 comparison pairs. | Supported; QA count is not independent sample count. | High |
| Current LLMs struggle with FG interactions. | Table 4 supports tested-model difficulty. | Medium-high |
| Chemistry-tuned models are superior. | Not supported consistently; several underperform general models. | High |
| FGBench enables better molecular/drug design. | Future hypothesis; benchmark results do not establish it. | Low |
| Data/code are available. | Official MIT repo and Hugging Face locator exist. | High |

## Methodology

`rg --files -g "*.pdf"` enumerated 75,777 PDFs / 75,776 parent units. Uniform `Get-Random` selected index 29,946; the first draw passed ID/DOI/title/slug/artifact/memory/companion/recent dedup.

The valid PDF plus missing HTML classified `partial`. Official latest v4 HTML and metadata were fetched once; PDF and HTML passed all integrity gates and local provenance records were updated. Missing-only extraction moved cache miss to `cached` in 0.579 seconds using `pypdf` and `html-regex` (66,093/65,496 bytes; no source).

The full paper, latest metadata, official repository README/tree, dataset locator, and exactly three DEP entries were inspected. No code, molecule, model, or API was run.

## Scope, Constraints, and Assumptions

- Benchmark/documentation review only; no chemical, clinical, toxicological, or synthesis authority.
- Results are author-reported and parser-dependent.
- v4 is treated as the current selected record; earlier-version differences were not diffed.
- Official repository availability is inventory evidence, not reproduction.
- Upstream MoleculeNet and dataset licenses/provenance need item-level review.
- Public artifacts contain no molecule tables or source payloads.

## Observations

- Explicit FG annotations create useful intermediate supervision and audit points.
- QA row count overstates independent transformation count.
- Imbalance makes micro-average results insufficient.
- Interaction tasks generally expose more weakness than single-group tasks.
- Valid-answer rate can dominate numeric comparisons.
- Different property units make aggregate RMSE hazardous.
- Training-data contamination is plausible because MoleculeNet is widely used.
- Missing stereochemistry/3D context constrains SAR reasoning.
- Public artifacts improve auditability but need environment and license hardening.

## Considerations

Use scaffold-, molecule-, pair-, group-, source-, and time-disjoint splits; report macro/group/property metrics and uncertainty. Audit template correctness, atom mappings, duplicates, source labels, and property units with chemists. Separate structure parsing, FG localization, qualitative direction, numeric prediction, and answer parsing. Treat any design suggestion as a hypothesis requiring computation, expert review, toxicity assessment, and experiments.

## Strengths

- Fine-grained localized structure is explicit.
- Construction and schema are documented publicly.
- Multiple properties and task types expose diverse failure modes.
- Results include answer validity and RMSE, not accuracy alone.
- General and chemistry-specialized models are compared.
- Limitations name missing structural distinctions.

## Weaknesses

- Dependence/contamination across templates, pairs, molecules, and sources is undercharacterized.
- Rare groups and dataset imbalance lack foregrounded macro analysis.
- Numeric properties are not normalized into one interpretable scale.
- Exact expert-validation rate/inter-rater evidence is incomplete.
- Position/chain/stereoisomerism, conformers, and 3D environment are missing.
- Model/API versions, seeds, prompts/parsers, and environment need stronger pinning.
- Repository hygiene and component-license inventory need improvement.
- Benchmark scores do not validate downstream molecule design.

## Potential Improvements

1. Publish canonical pair/scaffold/source/group-disjoint manifests and contamination checks.
2. Add rare-group macro metrics and balanced challenge subsets.
3. Normalize/report numeric errors by property and unit with strong baselines.
4. Add chemist double-review, disagreement, and correction ledgers.
5. Extend stereochemistry, positional/chain isomers, conformers, and 3D context.
6. Pin model/API snapshots, prompts, parsers, seeds, environment, and raw aggregate outputs.
7. Add retrieval/tool baselines and oracle structure controls.
8. Remove generated caches/OS metadata and publish SBOM/license inventory.
9. Evaluate calibration and abstention.
10. Establish a downstream safety gate that forbids direct design claims.

## Potential Implementations

### Split Leakage Auditor

Compute molecule, pair, scaffold, functional-group, source, and template overlap before scoring.

### Chemical Evidence Card

Version dataset lineage, units, balance, expert validation, contamination, model/parser configuration, and per-property metrics.

### Structure-Ablation Harness

Compare no-FG, FG identity, localized FG, graph neighborhood, and 3D context under identical pairs and models.

## Three Ways to Exercise This Research

1. **Schema audit** - validate public synthetic/sample rows, atom indices, unit labels, and template reversibility; output error ledger; stop on license/provenance gaps.
2. **Leakage-safe split replay** - construct molecule/scaffold/pair/source-disjoint subsets and compare reported metrics; output overlap and confidence report; stop if independence cannot be proven.
3. **Expert challenge set** - chemists curate rare groups, interactions, isomers, and counterexamples; output agreement/calibration; stop before any wet-lab or therapeutic recommendation.

## Example MVP Product

### FGBench Evidence Auditor

- User: chemistry benchmark maintainers and reviewers.
- Inputs: authorized dataset manifest and model-output aggregates.
- Flow: lineage/license validation, overlap detection, unit checks, parser audit, per-group scoring, calibration, report.
- Output: Markdown/JSON evidence card; no molecule payload in public output.
- Safety: research evaluation only; no molecule generation or experimental recommendation.

```python
def validate_split(train_ids: set[str], test_ids: set[str]) -> None:
    overlap = train_ids & test_ids
    if overlap:
        raise ValueError(f"split leakage: {len(overlap)} identifiers")
```

## Related Research and Reading

| Entry | Relevance | Boundary |
|---|---|---|
| Structure-Aware Systems | Preserving task-relevant structure and testing damage/shift aligns with localized FGs. | Heterogeneous portfolio; no FGBench validation. |
| Control Surfaces | Pepti-drift demonstrates in-silico biological safety limits and mechanism-aligned controls. | Peptide generation differs from property QA. |
| Tech Intel 2338 | LifeSciBench/artifact governance supports workflow-realistic scientific evaluation and availability audits. | Broad first-pass synthesis. |

## Source References

1. https://arxiv.org/abs/2508.01055v4
2. https://arxiv.org/html/2508.01055v4
3. https://arxiv.org/pdf/2508.01055
4. https://doi.org/10.48550/arXiv.2508.01055
5. https://github.com/xuanliugit/FGBench
6. https://huggingface.co/datasets/xuan-liu/FGBench
7. `.lake-data/DEP-E/DEP-E-20260714-Structure Aware Systems/structure-aware-systems.md`
8. `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md`
9. `.lake-data/DEP-E/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md`

## Appendix

Workflow: first draw index 29,946; no dedup; partial repaired with official v4 HTML; cache miss to cached; sources withheld. Key denominators: 42,967 comparison pairs, 625,936 QA rows, 7,146 benchmark rows, 245 groups, 27 alkane lengths, ten upstream datasets. No `.source/` was created.
