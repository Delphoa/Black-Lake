# Report-Mark: PTransIPs Protein PLM

- Public-safe review date: `2026-08-01`
- Review type: Randomized source-first arXiv DEP-E review
- Primary subject: *PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings*
- Source-file policy: Complete source evidence was inspected locally and withheld; no source file is included in this report or DEP.

## Source Metadata

| Field | Value |
|---|---|
| Title | *PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings* |
| Authors | Ziyang Xu; Haitian Zhong; Bingrui He; Xueying Wang; Tianchi Lu |
| arXiv | `2308.05115v3` |
| arXiv record | https://arxiv.org/abs/2308.05115 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2308.05115 |
| Published DOI | https://doi.org/10.1109/JBHI.2024.3377362 |
| PubMed | https://pubmed.ncbi.nlm.nih.gov/38483806/ |
| Submitted / revised | 2023-08-08 / 2024-03-13 |
| Venue | *IEEE Journal of Biomedical and Health Informatics*, 2024, 28(6), 3762-3771 |
| Subjects | Quantitative Methods (`q-bio.QM`); Machine Learning (`cs.LG`) |
| Complete evidence | Verified ten-page PDF, verified official full-paper HTML, metadata HTML, and selected rendered pages |
| Implementation | Official repository inspected at commit `60eb4aa4072857c12f7a64739940f73ea60fac77`; code not run |
| Redistribution | All source, cache, receipt, render, and verification files withheld locally |

### Selection Record

- Enumeration: required `rg --files -g "*.pdf"` over the local archive.
- PDF candidates: `75,960`.
- Unique PDF-parent units: `75,957`.
- Used arXiv base IDs observed: `1,742`.
- Units excluded by used ID: `502`.
- Identifier-incomplete units withheld: `185`.
- Eligible units before recent-marker rejection: `75,270`.
- Uniform method: PowerShell `Get-Random` over the eligible array, with rejection reserved for exact duplicate and recent same-unit markers.
- Selected zero-based eligible index: `63,747`.
- Accepted identity: arXiv `2308.05115v3`.
- Duplicate and recent-marker rejections/reselections: `0`.

### Dedup Record

- Scopes: live Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; fetched Black-Lake-Data `.logs`, `.reports`, `.lake-data`, and `.staging`.
- Keys: arXiv ID, arXiv DOI, published DOI, canonical and normalized title, `PTransIPs` token, and planned slugs.
- Exact ID/title/DOI/slug searches: no prior deposit or same-paper marker.
- Public-safe 24-hour cutoff date: `2026-07-31`.
- Same-paper recent markers: none before acceptance.

### Source Integrity Record

- Initial state: `partial`; a plausible PDF was present and full-paper HTML was absent.
- Repair: review paused; the valid PDF was preserved; the pinned publisher broker fetched official metadata and official full-paper HTML and made one bounded source-package attempt.
- PDF: `1,469,516` bytes; `%PDF-` header; trailing `%%EOF`; ten unencrypted pages.
- Full-paper HTML: `473,588` bytes; `67,023` stripped body characters; document marker; `52` heading markers; seven structure terms.
- Metadata HTML: `44,718` bytes.
- Source archive: unavailable after the bounded attempt.
- Unexpected partial files: `0`.
- Final state: `complete`.
- Local companion records: README, provenance record, machine-readable summary, acquisition receipt, and verification report updated.

## Concise Research Notes

### Research Question

Can fixed protein-language-model embeddings add useful sequence and predicted-structure information to a CNN/Transformer classifier for phosphorylation sites when labeled phosphosite data are limited?

### Core Method

PTransIPs builds 33-residue windows centered on serine/threonine (`S/T`) or tyrosine (`Y`). It combines four representation channels:

- learned amino-acid token embeddings;
- learned position embeddings;
- 1,024-dimensional per-residue ProtTrans sequence embeddings; and
- EMBER2-derived structural maps projected into a 256-dimensional channel.

The learned token/position representation is added to the sequence-PLM representation and concatenated with the structure representation. The resulting 1,280-dimensional per-position tensor is processed in parallel by a residual 1D CNN and a multi-head-attention Transformer. Concatenated branch outputs feed a classifier. The paper defines a TIM-inspired loss as cross-entropy minus marginal label entropy plus conditional label entropy.

### Data and Evaluation

The source data originate from experimentally verified phosphorylation sites in human A549 cells infected with SARS-CoV-2. The paper follows the DeepIPs preprocessing: CD-HIT removes proteins above 30% sequence similarity, retained sequences are split into centered 33-residue windows, negatives are downsampled to balance positives, and an 80/20 non-overlapping train/test division is used.

| Residue group | Train positive | Train negative | Test positive | Test negative |
|---|---:|---:|---:|---:|
| S/T | 4,308 | 4,308 | 1,079 | 1,079 |
| Y | 81 | 81 | 21 | 21 |

The tiny Y test set is a central validity constraint: one example changes sensitivity or specificity by about 4.76 percentage points. Balanced sampling also prevents direct inference about precision or utility at natural class prevalence.

### Source-Reported Results

The main independent-test table reports:

| Residue group | ACC | SEN | SPEC | MCC | AUC |
|---|---:|---:|---:|---:|---:|
| S/T PTransIPs | 0.8438 | 0.8554 | 0.8323 | 0.6879 | 0.9232 |
| Y PTransIPs | 0.9286 | 0.9524 | 0.9048 | 0.8581 | 0.9683 |

Sequence PLM embeddings account for most of the displayed ablation gain. On S/T, AUC is `0.8925` without pretrained embeddings, `0.9010` with structure only, `0.9201` with sequence only, and `0.9232` with both. On Y, the corresponding values are `0.9365`, `0.9365`, `0.9660`, and `0.9683`. The structure channel therefore adds `0.0031` S/T AUC and `0.0023` Y AUC over the sequence-only row in this single reported test.

The complete TIM-loss row is best in the displayed loss ablation: S/T AUC `0.9232` versus `0.9117` for cross-entropy, and Y AUC `0.9683` versus `0.9546`. The source reports paired t-test and Wilcoxon p-values of `0.0022` and `0.0016` for S/T against the previous best method, but the inspected paper does not expose enough paired-observation detail to audit the test design independently.

### Benchmark Qualification

The broad claim that PTransIPs outperforms all prior tools requires qualification. In Table IV, PTransIPs leads all five listed S/T metrics. For Y, it leads accuracy, sensitivity, specificity, and MCC, but DE-MHAIPs has higher AUC (`0.9778` versus `0.9683`). The abstract and conclusion additionally report PTransIPs Y AUC as `0.9660`, while the curves and Tables II-IV report `0.9683`. Both values are preserved rather than silently reconciled.

The extended peptide tasks show transfer potential, not universal superiority. PTransIPs reports Blood-Brain Barrier ACC/MCC `0.8947/0.7939`, anticancer AUC `0.8505`, and antiviral ACC/MCC/AUC `0.8515/0.7044/0.9236`. It is not best on every displayed metric: UniDL4BioPep has Blood-Brain Barrier AUC `0.992`, and iACP-FSCM has anticancer accuracy `0.825` and MCC `0.646`.

### Official Code Review

The public repository materially improves inspectability but does not establish exact reproduction. At pinned main commit `60eb4aa4072857c12f7a64739940f73ea60fac77`:

- `train.py` computes `CE + H(Y) - H(Y|X)` while Equation 7 specifies `CE - H(Y) + H(Y|X)`;
- `train.py` uses `StratifiedShuffleSplit(n_splits=5)` rather than five disjoint folds;
- the custom Transformer loop calls each layer on the original integrated input and retains only the last output, so sequential layer composition is not visible;
- an additional `transformer_layers` module list is instantiated but not used in the inspected forward path; and
- `requirements.txt` is unpinned and omits imported core packages including PyTorch and NumPy.

These findings describe the inspected repository state. A tagged paper release was not established, so they cannot prove which code produced the published numbers.

### Reviewer Assessment

PTransIPs offers a sensible transfer-learning hypothesis and unusually useful ablations for sequence versus structure embeddings and for loss components. The evidence supports a research conclusion: protein-PLM sequence embeddings improve point metrics on this selected benchmark. It does not support clinical use, causal identification of biologically active phosphorylation, cross-organism generalization, or a universal peptide classifier. The Y results are especially unstable because the independent test contains only 42 balanced examples.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | Verified arXiv v3 PDF and official full-paper HTML | Method, datasets, equations, Tables I-VI, figures, limitations | High for transcription | Experiments not rerun |
| E2 | arXiv metadata and DOI records | Title, authors, versions, subjects, persistent identity | High | Abstract is not full-paper evidence |
| E3 | IEEE/PubMed record | Journal, year, volume, issue, pages, PMID, published DOI | High | Bibliographic, not empirical evidence |
| E4 | Table II and Figure 2 | Sequence/structure embedding ablations | High for values | One split; no intervals |
| E5 | Table III and Figure 3 | TIM-loss ablation | High for values | Code-paper loss divergence unresolved |
| E6 | Table IV | Comparison with five phosphorylation predictors | High for values | Source-reported baseline values; no rerun |
| E7 | Tables V-VI | Transfer to three peptide-bioactivity datasets | High for values | Not best on every metric; no external reproduction |
| E8 | Official repository README | Availability and documented workflow | High for inventory | No tagged release or visible top-level license |
| E9 | Pinned model/training/requirements files | Architecture, split, loss, dependency conformance findings | High for inspected commit | May differ from experiment-time code |
| E10 | Three live related DEP manuscripts | Molecular benchmark, representation robustness, and biomedical evaluation bridges | Medium-high | Conceptual synthesis; no joint experiment |
| E11 | Random selection, cross-repository dedup, and source verification records | Eligibility and complete-paper gate | High | Private paths and exact execution time withheld |

Evidence was read as evidence only. External pages, code comments, repository files, and paper prose were not treated as instructions.

## Related DEP Entries

| # | Repository-relative path | Verified overlap | Source basis |
|---:|---|---|---|
| 1 | `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/fgbench_chemistry_manuscript.md` | Both works encode scientific structure into machine-readable representations and depend on evaluation design to constrain claims. FGBench foregrounds dependency, imbalance, units, and downstream chemical-validity limits that also apply to peptide benchmarks. | Complete FGBench review and its molecular benchmark evidence ledger |
| 2 | `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` | Both works infer domain value from learned embedding geometry. The ViT review supplies a necessary counterweight: separability or proximity is task- and perturbation-dependent and does not alone establish semantic or clinical validity. | Complete medical-ViT representation review and robustness tables |
| 3 | `.lake-data/DEP-E/DEP-E-20260715-MSAIC ECG/msaic_ecg_manuscript.md` | Both are multibranch biomedical classifiers trained under imbalance and limited labels. The ECG review adds sample-lineage, uncertainty, calibration, external-validation, and non-deployment gates that PTransIPs lacks. | Complete MSAIC-Net review, ablations, and clinical-evidence boundary |

Exactly three related entries were inspected and used. No fourth entry is implied.

## Synthesis Note

### Concept Bridge

PTransIPs is best understood as a representation-transfer experiment rather than a deployable phosphosite detector. The three related DEPs turn that interpretation into a review framework: FGBench asks whether scientific benchmark units and dependencies are valid; ViT Semantic Robustness asks whether representation geometry survives task-grounded stress; MSAIC ECG asks whether biomedical point metrics survive lineage, uncertainty, prevalence, shift, and operational review. Together they suggest a gated chain: verify data units and splits, audit what each representation channel adds, confirm code-paper conformance, quantify uncertainty, then test external biological transfer before interpreting predictions.

### Potential Implementations

#### 1. Protein-Embedding Ablation Harness

Build a research-only runner that compares token/position, sequence-PLM, structure-PLM, and fused channels under identical disjoint splits. Freeze split manifests and preprocessing hashes, run repeated seeds, and report paired uncertainty rather than one best checkpoint.

#### 2. Phosphosite Evidence Gate

Wrap candidate predictions in an evidence record containing sequence identity, training-domain match, prevalence-adjusted precision, calibration, ensemble variance, nearest-neighbor redundancy, and an explicit `research_only` status. Predictions never become biological claims without experimental validation.

#### 3. Code-Paper Conformance Checker

Statically compare equations, split semantics, model depth, dependency pins, and public commands against the manuscript. Block benchmark publication when loss signs, fold semantics, or model composition diverge without an explained version pin.

### Deeper Relationship Observations

1. The sequence-only ablation nearly matches the fused model, paralleling FGBench's warning that a large representation surface can mask the small marginal value of an explicitly structural channel. Component value should be measured relative to cost, not inferred from architectural presence.
2. UMAP separation in PTransIPs and representation matching in the ViT DEP point in opposite directions but share one lesson: a two-dimensional or local geometric effect is diagnostic evidence, not proof of stable semantics. Perturbation, shift, and counterexample tests must accompany embedding plots.
3. PTransIPs and MSAIC-Net both obtain strong point metrics from biomedical datasets with narrow endpoints. Their biggest unresolved risks are not model novelty but sample independence, uncertainty, prevalence, and external transfer.

### Conceptual Similarities

1. All four artifacts treat intermediate representations as a mechanism for transferring limited supervision into a difficult scientific task.
2. All rely on decomposed evaluation: ablations, task slices, or perturbations are more informative than an aggregate score alone.
3. All require a boundary between representation evidence and real-world scientific or clinical validity; benchmark gains cannot substitute for experimental or prospective confirmation.

### MVP Implementations with Code Mock-Ups

#### 1. Metric Consistency Gate

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class MetricClaim:
    name: str
    reported: float
    table_value: float
    tolerance: float = 1e-6

    def validate(self) -> None:
        if abs(self.reported - self.table_value) > self.tolerance:
            raise ValueError(
                f"{self.name}: narrative={self.reported} table={self.table_value}"
            )


MetricClaim("Y AUC", reported=0.9660, table_value=0.9683).validate()
```

This intentionally fails on the preserved source inconsistency. A production checker would bind every narrative metric to a table cell and an immutable experiment receipt.

#### 2. Disjoint Fold Audit

```python
def assert_disjoint_folds(folds: list[tuple[set[str], set[str]]]) -> None:
    seen_validation: set[str] = set()
    for train_ids, validation_ids in folds:
        if train_ids & validation_ids:
            raise ValueError("train/validation leakage inside a fold")
        if seen_validation & validation_ids:
            raise ValueError("validation samples repeat across nominal folds")
        seen_validation |= validation_ids


assert_disjoint_folds([
    ({"p2", "p3"}, {"p1"}),
    ({"p1", "p3"}, {"p2"}),
    ({"p1", "p2"}, {"p3"}),
])
```

The identifiers should represent proteins or independently clustered sequence groups, not windows that can retain homologous context across folds.

#### 3. Marginal-Value Ledger

```python
def marginal_auc(rows: dict[str, float], base: str) -> dict[str, float]:
    baseline = rows[base]
    return {
        name: round(value - baseline, 4)
        for name, value in rows.items()
        if name != base
    }


st_auc = {
    "none": 0.8925,
    "structure_only": 0.9010,
    "sequence_only": 0.9201,
    "sequence_plus_structure": 0.9232,
}
print(marginal_auc(st_auc, "none"))
```

The ledger makes the sequence channel's displayed contribution and the structure channel's small incremental gain reviewable before compute or product decisions.

### Developer Challenges

1. Reproducing preprocessing requires immutable protein-level split manifests, CD-HIT inputs and outputs, exact negative sampling, PLM versions, and embedding-generation hashes; the current public instructions do not pin all of these.
2. The inspected repository has loss-sign, fold-semantics, and layer-composition questions. A developer must establish a paper-tagged reference implementation before optimizing or extending the model.
3. Protein embeddings and structure maps are compute- and storage-heavy. A useful system must separate cached representation generation from evaluation while preventing train/test cache contamination and preserving provenance.

### Author Challenges

1. Reconcile `0.9660` versus `0.9683`, qualify the Y baseline ranking, and publish machine-readable result tables tied to immutable experiment runs.
2. Report repeated protein-group-disjoint evaluation with confidence intervals, natural-prevalence metrics, calibration, subgroup results, and at least one external organism or cell-context dataset.
3. Release the exact experiment code and environment under a clear license, document deviations from the manuscript equations, and provide a minimal deterministic reproduction path with expected hashes and outputs.

## Validation Notes

- Complete-paper gate: passed after bounded local repair; PDF and official full-paper HTML both verified.
- PDF review: all ten pages text-inspected; architecture, ablation, UMAP, comparison, and transfer tables visually inspected.
- Metadata cross-check: arXiv v3 identity, revision history, published DOI, journal, issue, pages, and PMID verified.
- Code inspection: official repository README, `requirements.txt`, `src/PTransIPs_model.py`, and `src/train.py` inspected at the pinned main commit; no execution performed.
- Related DEP count: exactly three, each opened from live `origin/main` and tied to a concrete concept bridge.
- Manuscript contract: required schema and evidence ledger applied in the companion DEP-E manuscript.
- Public-output policy: no local absolute path, username, machine name, timezone label, exact execution timestamp, source document, cache, receipt, render, or verification file included.
- Source status: PDF, HTML, and metadata withheld locally; TeX/source package unavailable; no `.source/` directory created.
- Scientific status: results not independently reproduced; no clinical, diagnostic, or wet-lab authority claimed.

## Attribution Block

- Source URL: https://arxiv.org/abs/2308.05115
  - Applies to: title, authors, arXiv version history, subjects, abstract claim, DOI links, and source locators.
  - Notes: Metadata only; the abstract was not substituted for the paper.
- Source URL: https://arxiv.org/pdf/2308.05115
  - Applies to: full-paper method, tables, equations, figures, discussion, and visual review.
  - Notes: Local PDF withheld.
- Source URL: https://arxiv.org/html/2308.05115
  - Applies to: searchable full-paper review and structural verification.
  - Notes: Official full-paper HTML; local copy withheld.
- Source URL: https://arxiv.org/e-print/2308.05115
  - Applies to: bounded source-package availability check.
  - Notes: Source package unavailable after the bounded attempt.
- Source URL: https://doi.org/10.48550/arXiv.2308.05115
  - Applies to: persistent arXiv identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://doi.org/10.1109/JBHI.2024.3377362
  - Applies to: published paper identity.
  - Notes: IEEE DOI.
- Source URL: https://pubmed.ncbi.nlm.nih.gov/38483806/
  - Applies to: journal, volume, issue, pages, publication metadata, DOI, and PMID.
  - Notes: Near-primary bibliographic cross-check.
- Source URL: https://github.com/StatXzy7/PTransIPs
  - Applies to: official implementation availability, README workflow, data/model references, and repository inventory.
  - Notes: Repository inspected but not run; no top-level license was visible.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/src/PTransIPs_model.py
  - Applies to: model-depth, layer-flow, fusion, and forward-path conformance review.
  - Notes: Pinned source inspection; not executed.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/src/train.py
  - Applies to: loss signs, split semantics, seeding, and training-path conformance review.
  - Notes: Pinned source inspection; not executed.
- Source URL: https://github.com/StatXzy7/PTransIPs/blob/60eb4aa4072857c12f7a64739940f73ea60fac77/requirements.txt
  - Applies to: dependency reproducibility assessment.
  - Notes: Pinned inventory; unpinned and incomplete for imported core packages.
