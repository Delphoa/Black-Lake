# Report-Mark: Dental-Lung Cancer MR

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Dissecting the Dental Lung Cancer Axis via Mendelian Randomization and Mediation Analysis* |
| Authors | Wenran Zhang; Huihuan Luo; Linda Wei; Ping Nie; Yiqun Wu; Dedong Yu |
| Canonical record | [arXiv:2507.18287v1](https://arxiv.org/abs/2507.18287v1) |
| arXiv DOI | [10.48550/arXiv.2507.18287](https://doi.org/10.48550/arXiv.2507.18287) |
| Publisher DOI | [10.1109/BIBM66473.2025.11357049](https://doi.org/10.1109/BIBM66473.2025.11357049) |
| Publication context | arXiv v1 submitted 2025-07-24; later indexed as IEEE BIBM 2025, pages 1443-1449 |
| arXiv category | `cs.CV`, despite the paper's epidemiology and Mendelian-randomization subject matter |
| Public implementation | The paper says the project would be open-sourced upon acceptance; a bounded exact-name search did not establish an official public repository |
| Review date | 2026-07-25; exact local execution time withheld |
| Source state | Complete and verified after bounded local repair; all source files withheld locally and not uploaded |
| Safety boundary | Research review only; not medical advice, a clinical risk calculator, or a screening recommendation |

## Concise Research Notes

**Problem.** Observational studies connect oral disease with lung cancer, but smoking, reverse causation, selection, and other confounders make the relationship difficult to interpret. The paper asks whether genetic instruments for periodontitis and dental caries support causal associations with overall lung cancer and three subtypes, and whether forced vital capacity (FVC), forced expiratory volume in one second (FEV1), or their ratio mediates any association.

**Method.** The authors use a two-step, two-sample summary-data Mendelian-randomization design. Inverse-variance weighting (IVW) is the primary estimator. They screen variants with PhenoScanner, remove incompatible or palindromic alleles and selected confounders, use MR-Egger and weighted-median estimators as secondary checks, apply MR-PRESSO and Cochran's Q for outliers and heterogeneity, and use multivariable MR to adjust lung-function analyses for height. A product-of-coefficients mediation analysis estimates the indirect effect, with the delta method and bootstrap intervals.

**Data.** Table I reports exposure GWAS sample sizes of 44,563 for periodontitis and 26,792 for dental caries, lung-function samples of 400,102, and an overall lung-cancer dataset of 85,716 people, described in the methods as 29,266 cases and 56,450 controls of European ancestry. The abstract instead says the dental instruments derive from 487,823 dental-caries and 506,594 periodontitis "cases." The review preserves this discrepancy rather than reconciling the terms or denominators without the upstream GWAS records.

**Primary reported results.** Dental caries is associated with overall lung cancer under IVW (OR 2.525, 95% CI 1.454-4.384, p=0.001), adenocarcinoma (OR 2.456, 95% CI 1.299-4.642, p=0.006), small-cell lung carcinoma (OR 4.175, 95% CI 1.316-13.247, p=0.015), and squamous-cell lung cancer (OR 2.880, 95% CI 1.236-6.713, p=0.014). Periodontitis is null for overall lung cancer after the authors' confounder screen (OR 1.137, 95% CI 0.797-1.623, p=0.479) and remains nonsignificant after one MR-PRESSO outlier is removed.

**Mediation evidence.** Dental caries is associated with lower FVC (OR 0.819, 95% CI 0.726-0.923, p=0.001) and FEV1 (OR 0.857, 95% CI 0.769-0.954, p=0.005). FVC and FEV1 are inversely associated with squamous-cell lung cancer in the second step. The reported mediated proportions are 5.124% through FVC and 5.890% through FEV1. These are small indirect paths, not evidence that lung-function change explains most of the reported caries association.

**Boundary evidence.** The caries-to-overall-cancer IVW estimate has significant heterogeneity (Q p=0.006). Table II reports heterogeneity for all three lung-function traits and MR-Egger intercept p values of 0.043 for FVC and 0.025 for FEV1/FVC, which raise directional-pleiotropy concerns in parts of the proposed mediation chain. The paper tests several related outcomes without describing a multiple-testing correction. All contributing consortia are European-ancestry; the authors also disclose binary cancer phenotypes, incomplete molecular subtype dissection, survival selection, smoking confounding, and collider bias as limitations.

**Reviewer interpretation.** The paper supplies a useful, auditable causal-inference hypothesis: inherited liability to dental caries may be linked to lung-cancer outcomes, with a small lung-function pathway. It does not establish that treating caries reduces lung-cancer incidence, that a patient with caries has the reported odds ratio, or that dental status should be added to screening criteria. A defensible implementation would be a research evidence workbench that exposes assumptions, instruments, diagnostics, multiplicity, and source versions - not a patient-facing risk score.

## Evidence and Attribution

| Evidence | Source location | Assessment |
|---|---|---|
| Canonical title, six authors, v1 date, abstract, and headline metrics | [arXiv record](https://arxiv.org/abs/2507.18287v1) | Primary metadata and author claims; high confidence for identity and transcription. |
| Two-step MR design, instrument selection, software versions, and mediation formula | Methods and Figure 1 in the [full paper](https://arxiv.org/html/2507.18287v1) | Direct method evidence; assumptions were not independently audited against raw data. |
| Exposure, mediator, and outcome sample sizes | Table I, visually checked on PDF page 2 | Direct table evidence; conflicts with larger "cases" counts in the abstract. |
| Dental caries to overall lung cancer: OR 2.525, CI 1.454-4.384, p=0.001 | Results and Figure 2, visually checked on PDF pages 4-5 | Direct reported result; significant heterogeneity and no independent reproduction. |
| Caries associations with three lung-cancer subtypes | Results and Figure 2 | Direct reported results; wide subtype confidence intervals and multiplicity limit precision. |
| Periodontitis null result | Results section and Figure 2 | Direct reported result; source also notes smoking-related interference may differ by oral trait. |
| Caries to FVC and FEV1 effects | Table II, visually checked on PDF page 4 | Direct reported results; FVC has an MR-Egger intercept p=0.043 and both traits have heterogeneity. |
| FVC and FEV1 to squamous-cell lung cancer | Table III, visually checked on PDF page 4 | Direct reported results; overall lung-cancer effects were not significant. |
| Mediation proportions 5.124% and 5.890% | Table IV, visually checked on PDF page 4 | Direct reported estimates; small proportions with no independent recomputation. |
| European-only ancestry, binary outcomes, subtype, survival, and confounding limits | Discussion and conclusion | Author-disclosed boundary evidence; high confidence for stated limitations. |
| BIBM 2025 publication and pages 1443-1449 | [DBLP record](https://dblp.org/rec/conf/bibm/ZhangLWNWY25) and [IEEE DOI](https://doi.org/10.1109/BIBM66473.2025.11357049) | Public bibliographic context; the reviewed scholarly source remains arXiv v1. |
| No official code repository was established | Exact-title and arXiv-ID search | Negative discovery evidence, not proof that code is absent. |
| Clinical action is not established | MR design, reported diagnostics, and missing intervention evidence | Reviewer assessment; the paper is not a randomized treatment or screening trial. |

The complete PDF, official full-paper HTML, search-provenance snapshot, rendered pages, local extraction cache, collector receipt, and verification records were used only in the private source-first workflow. They remain withheld locally. Public links identify the evidence without redistributing source artifacts.

## Related DEP Entries

1. **Causal DP Workloads** - `.lake-data/DEP-E/DEP-E-20260722-Causal DP Workloads/causal-dp-workloads.md`. Source basis: the inspected manuscript reviews estimand-specific causal workloads, identification assumptions, privacy noise, approximation bias, and interval calibration. Relevance: both artifacts show that preserving a point estimate is insufficient; a causal workflow must preserve its estimand, assumptions, diagnostics, and uncertainty.
2. **Agent Systems Map / NAIS** - `.lake-data/DEP-E/DEP-E-20260720-Agent Systems Map/agent-systems-map.md`. Source basis: the inspected manuscript covers a governed 286,422-person hypertension GWAS, aggregate-only execution, phenotype disagreement, and human-directed reconciliation. Relevance: it supplies the execution-governance complement to this paper's summary-GWAS analysis, especially for protected data, phenotype definitions, reproducibility, and expert review.
3. **ClinRAG-GRAPH** - `.lake-data/DEP-A/DEP-A-20260717-ClinRAG Graph/2607.00798-whitepaper-review.md`. Source basis: the inspected review covers multi-center clinical prediction, domain-adversarial learning, evidence-grounded inference, internal/external AUCs, and prospective-validation needs. Relevance: it shows the additional calibration, domain-shift, explanation, and governance evidence needed before a biomedical research signal becomes a clinical decision surface.

## Synthesis Note

### Concept Bridge

The paper and the three related entries describe successive layers of a trustworthy biomedical evidence system. Dental-Lung MR asks whether genetic instruments support a causal hypothesis and exposes instrument, pleiotropy, heterogeneity, and mediation diagnostics. Causal DP Workloads asks whether a privacy-preserving release retains the estimand and uncertainty needed for causal analysis. Agent Systems Map's NAIS case asks how protected GWAS computation is governed, versioned, and corrected when phenotype definitions disagree. ClinRAG-GRAPH asks how a downstream clinical model handles center shift, multimodal evidence, and external validation.

The bridge is not a single predictive model. It is a chain of evidence contracts: source identity, phenotype definition, causal estimand, instrument validity, diagnostic status, privacy/governance boundary, external validation, and human decision authority. A break anywhere in that chain should prevent a research association from being rendered as a patient-level recommendation.

### Potential Implementations

1. **MR evidence dossier:** Parse a paper's declared exposure, outcome, instruments, estimators, diagnostics, effect sizes, ancestry, and multiplicity policy into a versioned reviewer checklist.
2. **Governed reanalysis broker:** Route approved GWAS jobs to institution-local execution, return aggregate diagnostics only, and require human sign-off when phenotype definitions, sample overlap, or harmonization differ.
3. **Clinical translation gate:** Join causal-evidence quality with external-validation, calibration, decision-curve, and intervention-evidence requirements before allowing any screening or decision-support claim.

### Deeper Relationship Observations

1. **Uncertainty is an artifact, not decoration.** MR heterogeneity and pleiotropy, DP interval calibration, center-shift performance, and phenotype discordance all change what downstream decisions are defensible.
2. **Phenotypes are executable definitions.** Dental-caries liability, hypertension labels, pCR outcomes, and lung-cancer subtypes are not merely names; each must be versioned with inclusion, coding, and harmonization rules.
3. **Causal and predictive evidence answer different questions.** MR estimates an exposure-outcome relation under instrumental assumptions, while ClinRAG predicts an outcome under distributional assumptions. Neither automatically supplies the other's validity.

### Conceptual Similarities

1. **Evidence-linked computation:** Each entry ties a conclusion to source records, transformations, diagnostics, and a bounded evaluation surface.
2. **Domain-shift sensitivity:** European-only consortia, institution-specific GWAS, and external clinical centers all expose failures when a result crosses populations or sites.
3. **Human-governed escalation:** Phenotype disputes, anomalous diagnostics, privacy constraints, and clinical consequences require explicit review rather than silent model continuation.

### MVP Implementations with Code Mock-Ups

1. **Claim-to-evidence validator.** This toy utility rejects a dossier when a claim has no valid evidence identifier.

```python
def validate_claim_map(
    evidence_ids: set[str], claims: dict[str, list[str]]
) -> list[str]:
    errors: list[str] = []
    for claim_id, references in claims.items():
        if not references:
            errors.append(f"{claim_id}: no evidence")
            continue
        missing = sorted(set(references) - evidence_ids)
        if missing:
            errors.append(f"{claim_id}: unknown evidence {missing}")
    return errors
```

2. **MR diagnostic gate.** This bounded check flags a result for review; it does not estimate causality or make a clinical decision.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class MRDiagnostics:
    effect_p: float
    heterogeneity_p: float | None
    egger_intercept_p: float | None
    corrected_alpha: float


def review_flags(item: MRDiagnostics) -> list[str]:
    flags: list[str] = []
    if item.effect_p >= item.corrected_alpha:
        flags.append("effect does not pass the declared multiplicity threshold")
    if item.heterogeneity_p is not None and item.heterogeneity_p < 0.05:
        flags.append("significant heterogeneity")
    if item.egger_intercept_p is not None and item.egger_intercept_p < 0.05:
        flags.append("possible directional pleiotropy")
    return flags
```

3. **Mediation arithmetic check.** This verifies sign and proportion arithmetic on synthetic inputs while refusing a zero total effect.

```python
def mediation_summary(
    exposure_to_mediator: float,
    mediator_to_outcome: float,
    total_effect: float,
) -> dict[str, float]:
    if total_effect == 0:
        raise ValueError("total effect must be nonzero")
    indirect = exposure_to_mediator * mediator_to_outcome
    proportion = 100.0 * indirect / total_effect
    return {
        "indirect_effect": indirect,
        "mediation_percent": proportion,
    }
```

### Developer Challenges

1. **Semantic normalization:** Exposure scales, odds ratios, beta coefficients, case/control counts, ancestry, version identifiers, and diagnostic p values must retain their source meanings instead of being flattened into one score.
2. **Negative-evidence handling:** Missing multiple-testing correction, code, sample-overlap analysis, or external validation must remain visible and must trigger a review state rather than a fabricated default.
3. **Privacy and auditability:** Real GWAS or clinical integration needs institution-local processing, least-privilege access, aggregate-only outputs, immutable job records, and no patient data in logs or public artifacts.

### Author Challenges

1. **Resolve source inconsistencies:** Reconcile the abstract's 487,823/506,594 "cases" with Table I's 26,792/44,563 exposure sample sizes and define the exposure scale underlying each odds-ratio interpretation.
2. **Strengthen statistical validity:** Predeclare the hypothesis family and multiplicity policy; quantify sample overlap; report harmonized SNP inventories; address heterogeneity and the Table-II MR-Egger intercept signals in the mediation interpretation.
3. **Validate translation claims:** Release the promised code and manifests, reproduce the analysis independently, test diverse ancestries and prospective cohorts, and evaluate dental intervention or screening utility before recommending clinical-policy changes.

## Validation Notes

- **Random selection:** `rg --files -g "*.pdf"` enumerated 75,780 PDFs in 75,777 parent units. A 1,362-ID used index excluded 352 used units; 185 identifier-incomplete units were withheld. Uniform zero-based eligible index 70,409 was drawn from 75,240 units.
- **Deduplication:** Delphoa/Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and fetched Delphoa-Labs/Black-Lake-Data `origin/main` surfaces were checked. No match existed for arXiv ID, either DOI, normalized title, or planned slug. The 24-hour cutoff was 2026-07-24. Duplicate rejections/reselections: 0.
- **Source gate:** Initial state was partial because full-paper HTML was absent. The valid PDF was preserved. The first brokered ID-search attempt failed closed on a redirected surface and produced no partials; one final exact-title attempt acquired official full-paper HTML.
- **PDF verification:** 3,192,319 bytes, `%PDF-` header, trailing `%%EOF`, eight unencrypted pages, and SHA-256 `007BC2DD4B8CD88C822F0F8A7E78A40B5BD43803F79AE6457ADF766C6486FE1A`.
- **HTML verification:** 187,338 bytes, 53,098 stripped body characters, full-document marker, 48 heading markers, and six structure terms.
- **Visual review:** All eight pages were rendered and inspected. Tables I-IV and Figures 1-3 were legible; no clipping or page corruption affected the reviewed values.
- **Cache:** Local-only PDF and HTML text extraction completed. No TeX/source package was collected.
- **Related entries:** Exactly three verified repository artifacts were used, each with an inspected source basis and a distinct relevance reason.
- **Medical safety:** The report separates paper claims from reviewer interpretation and explicitly rejects patient-level risk, treatment-prevention, and screening-policy inferences.
- **Public safety:** Public files contain date-only markers, repository-relative paths, and public URLs. Local paths, usernames, machine names, local timezone labels, and exact execution timestamps are withheld.
- **No-source-upload gate:** The intended staged set contains generated Markdown only. No PDF, HTML, source archive, search snapshot, cache, extracted source text, receipt, or private verification file is eligible for staging.

## Attribution Block

- Source URL: https://arxiv.org/abs/2507.18287v1
  - Applies to: `Report-Mark.md`
  - Notes: Canonical paper identity, authors, submission date, abstract, and primary public record.
- Source URL: https://arxiv.org/html/2507.18287v1
  - Applies to: `Report-Mark.md`
  - Notes: Official full-paper evidence for methods, results, tables, figures, discussion, limitations, and references.
- Source URL: https://arxiv.org/pdf/2507.18287v1
  - Applies to: `Report-Mark.md`
  - Notes: Public locator for the visually inspected paper PDF; no PDF was deposited.
- Source URL: https://doi.org/10.48550/arXiv.2507.18287
  - Applies to: `Report-Mark.md`
  - Notes: Stable arXiv DOI.
- Source URL: https://doi.org/10.1109/BIBM66473.2025.11357049
  - Applies to: `Report-Mark.md`
  - Notes: IEEE BIBM proceedings DOI and later publication context.
- Source URL: https://dblp.org/rec/conf/bibm/ZhangLWNWY25
  - Applies to: `Report-Mark.md`
  - Notes: Bibliographic record for BIBM 2025 pages 1443-1449.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Causal%20DP%20Workloads/causal-dp-workloads.md
  - Applies to: `Report-Mark.md`
  - Notes: Related DEP evidence for causal estimands, privacy, and uncertainty calibration.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-Agent%20Systems%20Map/agent-systems-map.md
  - Applies to: `Report-Mark.md`
  - Notes: Related DEP evidence for governed GWAS execution and phenotype reconciliation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ClinRAG%20Graph/2607.00798-whitepaper-review.md
  - Applies to: `Report-Mark.md`
  - Notes: Related DEP evidence for multi-center clinical prediction, evidence grounding, and translation boundaries.
- Source files: Withheld locally.
  - Applies to: `Report-Mark.md`
  - Notes: The private PDF, HTML, provenance, cache, renders, receipt, and verification records were not copied, staged, or uploaded.
