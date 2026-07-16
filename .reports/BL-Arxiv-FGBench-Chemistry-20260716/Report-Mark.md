# Report-Mark: FGBench Chemistry

## Review Status

- Paper: arXiv:2508.01055v4; NeurIPS 2025 Datasets and Benchmarks
- Source: verified complete latest PDF/official HTML
- Review: construction, task taxonomy, Tables 1-4, appendices, limitations, official repo/data availability
- Reproduction: none; source/molecular files withheld

## Source Metadata

| Field | Value |
|---|---|
| Title | FGBench: A Dataset and Benchmark for Molecular Property Reasoning at Functional Group-Level in Large Language Models |
| Authors | Xuan Liu; Siru Ouyang; Xianrui Zhong; Jiawei Han; Huimin Zhao |
| ID / DOI | arXiv:2508.01055v4 / 10.48550/arXiv.2508.01055 |
| Dates | 2025-08-01; revised 2026-02-16 |
| Availability | MIT repository and Hugging Face dataset live; inspected, not downloaded/run |

## Concise Research Notes

FGBench turns ten MoleculeNet sources into 42,967 validated molecular comparison pairs and 625,936 templated QA rows with localized functional-group differences. Tasks cover single-group effects, interactions, and direct comparison across 245 groups.

Nine models are evaluated on 7,146 rows. O3-mini leads Boolean accuracy at 0.687/0.693/0.703 across single/interaction/comparison. GPT-4o and Llama-3.1-70B decline on interactions. Numeric RMSE and validity vary widely, so no one aggregate ranking is chemically sufficient.

The main evidence gap is independence: template rows share pairs/molecules/source data, and MoleculeNet may have appeared in model training. The paper explicitly omits positional, chain, and stereoisomerism and 3D context. Official availability improves auditability but does not substitute for an expert chemistry and contamination audit.

## Evidence and Attribution

| ID | Evidence | Boundary |
|---|---|---|
| R1 | Full v4 construction/method | no independent chemical audit |
| R2 | Tables 1-4 and Appendix B | author-reported; parser/unit dependent |
| R3 | Failure/limitations | selected examples; explicit isomer gaps |
| R4 | Official repo README/tree/dataset locator | not downloaded/executed |
| R5 | Three DEP artifacts | conceptual context only |
| R6 | Selection/repair/cache records | operational evidence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-Structure Aware Systems/structure-aware-systems.md` - structure preservation and shift/damage tests.
2. `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md` - in-silico peptide safety boundaries.
3. `.lake-data/DEP-E/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` - life-science benchmark/artifact governance.

## Synthesis Note

### Concept Bridge

FGBench makes molecular substructure explicit; Structure-Aware Systems generalizes why task-relevant structure and verifiable boundaries matter; Control Surfaces prevents in-silico biological scores from becoming safety claims; Tech Intel 2338 emphasizes workflow-realistic scientific benchmarks and artifact audits. Together they motivate an evidence auditor centered on lineage, split independence, units, expert validation, and downstream authority limits.

### Potential Implementations

1. **Split-leakage auditor** - molecule/pair/scaffold/group/source/template overlap and contamination flags.
2. **Chemical benchmark card** - units, balance, lineage, expert corrections, parser/model versions, calibration, per-property metrics.
3. **Structure-ablation harness** - no-FG, identity, localization, graph-neighborhood, and 3D context under matched pairs.

### Deeper Relationship Observations

1. Structure-Aware Systems predicts FGBench's benefit: explicit localized groups expose reasoning steps that flattened SMILES-only tasks hide.
2. Control Surfaces shows the same score-to-reality gap: predicted peptide safety and property QA both require experimental/domain validation before decisions.
3. Tech Intel 2338 shows availability is multidimensional—dataset, rubric, code, licenses, versions, and scoring artifacts—not one badge.

### Conceptual Similarities

1. Each artifact argues that the evaluation unit must match the mechanism of interest.
2. Each separates inspectable benchmark evidence from deployment or scientific validity.
3. Each benefits from structured provenance, explicit constraints, and failure-led review.

### MVP Implementations with Code Mock-ups

1. **Identifier overlap**

```python
def assert_disjoint(train: set[str], test: set[str]) -> None:
    if train & test:
        raise ValueError("molecular split overlap")
```

2. **Unit-aware metric**

```python
def require_unit(property_name: str, unit: str) -> None:
    if not property_name or not unit:
        raise ValueError("property and unit required")
```

3. **Authority gate**

```python
def route_output(calibrated: bool, expert_reviewed: bool) -> str:
    return "research_only" if not (calibrated and expert_reviewed) else "review_candidate"
```

### Developer Challenges

1. Canonicalizing molecules/scaffolds/atom maps without hiding stereochemical or tautomer differences.
2. Tracking lineage across ten source datasets, comparisons, templates, properties, units, and model outputs.
3. Reproducing API/model/parser behavior while preserving licenses and preventing source payload publication.

### Author Challenges

1. Publish contamination-resistant split manifests and effective independent-sample accounting.
2. Add rare-group macro results, expert agreement, stereochemistry/3D context, normalized per-property baselines, and uncertainty.
3. Pin environments/APIs/parsers/seeds, clean repository artifacts, and document component licenses.

## Validation Notes

- Uniform first draw: index 29,946/75,776; no exclusions/reselections/dedup.
- PDF 5,996,608 bytes with valid header/EOF; official v4 HTML 351,922 bytes/65,713 body chars/65 headings/six terms; final complete.
- Cache miss to cached in 0.579 seconds; 66,093/65,496 PDF/HTML text bytes; no source.
- Official repo/data inventoried only; no code/data/model/API run.
- Schema/count/public-safety and seven-file no-source allowlist checked before submission.

## Attribution Block

- Paper: https://arxiv.org/abs/2508.01055v4
- HTML/PDF: https://arxiv.org/html/2508.01055v4 ; https://arxiv.org/pdf/2508.01055
- DOI: https://doi.org/10.48550/arXiv.2508.01055
- Code/data: https://github.com/xuanliugit/FGBench ; https://huggingface.co/datasets/xuan-liu/FGBench
- Nature: independent review; no result reproduced; no source or molecular-data file uploaded.
