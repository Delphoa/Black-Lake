---
title: "Dental-Lung MR - DEP-E"
generated_at: "2026-07-25 (exact execution time withheld)"
artifact_type: "DEP research artifact; paper report; implementation brief; replication plan"
primary_subject: "A source-grounded review of Mendelian-randomization and lung-function mediation evidence linking dental traits with lung-cancer outcomes."
source_status: "Complete local PDF and official full-paper HTML inspected; all source files withheld from the public DEP."
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-25"
temporal_cutoff: "arXiv v1 plus public bibliographic context through 2026-07-25"
primary_url: "https://arxiv.org/abs/2507.18287v1"
stable_identifier: "arXiv:2507.18287v1; DOI 10.48550/arXiv.2507.18287; DOI 10.1109/BIBM66473.2025.11357049"
confidence_summary: "High for source identity and transcription; medium for causal interpretation; low for clinical translation without independent reproduction and intervention evidence."
safety_scope: "Research review only; not medical advice, diagnosis, patient risk estimation, or screening policy."
distribution_notes: "Generated Markdown and public URLs only; private scholarly source files were not deposited."
---

# Dental-Lung MR - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Dissecting the Dental Lung Cancer Axis via Mendelian Randomization and Mediation Analysis* | Primary reviewed work | arXiv paper record | arXiv:2507.18287v1 | https://arxiv.org/abs/2507.18287v1 | Public scholarly record; redistribution rights were not assumed | 2026-07-25 | Metadata and abstract inspected |
| S2 | Official full-paper representation | Primary method and result evidence | Full-paper HTML | arXiv:2507.18287v1 | https://arxiv.org/html/2507.18287v1 | Source document retained locally and not deposited | 2026-07-25 | Complete body, tables, figures, limitations, and references inspected |
| S3 | arXiv PDF | Primary visual and layout evidence | PDF | arXiv:2507.18287v1 | https://arxiv.org/pdf/2507.18287v1 | Source document retained locally and not deposited | 2026-07-25 | Eight pages rendered and inspected |
| S4 | IEEE BIBM proceedings record | Later publication context | DOI / publisher record | 10.1109/BIBM66473.2025.11357049 | https://doi.org/10.1109/BIBM66473.2025.11357049 | Bibliographic context; no publisher file collected | 2026-07-25 | DOI established |
| S5 | DBLP BIBM record | Independent bibliographic locator | Bibliographic record | `conf/bibm/ZhangLWNWY25` | https://dblp.org/rec/conf/bibm/ZhangLWNWY25 | Metadata locator; not empirical evidence | 2026-07-25 | Venue and pages inspected |
| S6 | Causal DP Workloads - DEP-E | Related causal-inference artifact | Repository manuscript | DEP-E-20260722 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Causal%20DP%20Workloads/causal-dp-workloads.md | Public generated review | 2026-07-25 | Estimand, privacy, and uncertainty sections inspected |
| S7 | Agent Systems Map - DEP-E | Related governed-GWAS artifact | Repository manuscript | DEP-E-20260720 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-Agent%20Systems%20Map/agent-systems-map.md | Public generated review | 2026-07-25 | NAIS GWAS and governance sections inspected |
| S8 | ClinRAG-GRAPH review | Related clinical-translation artifact | Repository whitepaper review | DEP-A-20260717 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ClinRAG%20Graph/2607.00798-whitepaper-review.md | Public generated review | 2026-07-25 | Multi-center evidence and governance sections inspected |

### Primary work identity

- **Title:** *Dissecting the Dental Lung Cancer Axis via Mendelian Randomization and Mediation Analysis*
- **Authors:** Wenran Zhang; Huihuan Luo; Linda Wei; Ping Nie; Yiqun Wu; Dedong Yu.
- **Version:** arXiv v1, submitted 2025-07-24.
- **arXiv category:** `cs.CV`. This category is preserved as metadata but is unusual for the paper's epidemiology and Mendelian-randomization content.
- **Later publication:** IEEE International Conference on Bioinformatics and Biomedicine (BIBM) 2025, pages 1443-1449, according to the DOI and DBLP record.
- **Public code:** The paper says the project would be open-sourced upon acceptance. A bounded exact-name and arXiv-ID search did not establish an official public repository.
- **Local source paths:** Withheld from this public artifact. The verified PDF, HTML, provenance, cache, renders, receipt, and verification records remain private.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary paper metadata | Canonical title, authors, v1 date, abstract, headline results | Work identity and author-level summary | High | Abstract contains exposure-sample wording that differs from Table I |
| E2 | S2-S3 | Primary full paper | Methods, Figure 1, software versions, instrument rules, sensitivity analyses | Two-step MR and mediation mechanism | High for transcription | No raw data, code, or independent estimator audit |
| E3 | S2-S3 | Primary full paper | Table I and methods data-source descriptions | Exposure, mediator, and outcome datasets and sample sizes | High for table transcription | Abstract reports larger dental "cases" counts without reconciliation |
| E4 | S2-S3 | Primary full paper | Results, Figure 2, Tables II-IV | Odds ratios, lung-function effects, heterogeneity, pleiotropy, and mediation | High for transcription; medium for inference | Multiple outcomes, wide intervals, significant diagnostics, and no independent reproduction |
| E5 | S2-S3 | Primary full paper | Discussion, conclusion, and reference context | Author interpretation, strengths, and disclosed limits | High for what authors state | Discussion does not convert MR evidence into intervention evidence |
| E6 | S4-S5 | Publisher and bibliographic records | DOI, BIBM venue, pages, and later title form | Publication context | High | Bibliographic evidence only |
| E7 | S6 | Related DEP manuscript | Causal workloads, identification assumptions, approximation, and interval calibration | Causal-estimand and uncertainty bridge | High for related-artifact content | Not an independent validation of the dental-lung paper |
| E8 | S7 | Related DEP manuscript | Governed 286,422-person hypertension GWAS and phenotype reconciliation | Protected-data and human-governance bridge | High for related-artifact content | Different disease, data, and research system |
| E9 | S8 | Related DEP review | Multi-center pCR prediction, external AUCs, domain adaptation, evidence grounding | Clinical-translation and domain-shift bridge | High for related-artifact content | Predictive modeling differs from causal estimation |
| E10 | E2-E5 | Reviewer synthesis | Diagnostics, source discrepancies, and missing evidence jointly considered | Clinical action is not established | Medium-high | A replication or revised paper could alter the assessment |

## Executive Summary

The paper uses two-sample Mendelian randomization (MR) to test whether genetic liability to periodontitis or dental caries is associated with overall lung cancer, adenocarcinoma, small-cell lung carcinoma, and squamous-cell lung cancer. It then applies a two-step mediation analysis to ask whether FVC, FEV1, or FEV1/FVC carries part of a significant oral-trait effect. The main estimator is inverse-variance weighting (IVW), with MR-Egger, weighted median, MR-PRESSO, Cochran's Q, PhenoScanner filtering, and height-adjusted multivariable MR as supporting analyses (E2).

The authors report positive dental-caries associations with overall lung cancer and all three subtypes. The overall IVW estimate is OR 2.525 (95% CI 1.454-4.384, p=0.001); the subtype odds ratios range from 2.456 to 4.175. Periodontitis is not significant. Dental caries is also associated with lower FVC and FEV1, and those lung-function measures are inversely associated with squamous-cell lung cancer. The reported mediation proportions are 5.124% through FVC and 5.890% through FEV1 (E4).

Confidence is high that these numbers and methods are transcribed correctly from a complete source. Confidence is only medium in the paper's broad causal interpretation and low for direct clinical translation. Significant heterogeneity, MR-Egger intercept signals in parts of the mediator analysis, wide subtype intervals, European-only data, binary outcomes, survival selection, unquantified sample overlap, no described multiplicity correction, and no independent reproduction all matter. The abstract also labels much larger dental sample counts than Table I. These findings support a causal-research hypothesis and replication agenda; they do not establish that dental treatment prevents lung cancer or justify a new screening rule (E3-E5, E10).

## Detailed Summary

### Problem and background

Oral disease and lung cancer share plausible observational pathways: oral microbes may enter the respiratory tract; inflammation and immune responses may affect pulmonary tissue; and impaired lung function can correlate with cancer risk. Observational evidence is difficult to interpret because smoking affects both oral and pulmonary outcomes, reverse causation is possible, and clinical cohorts may be selected or underpowered.

MR uses genetic variants as instrumental variables to estimate an exposure-outcome relationship under three core ideas: variants are associated with the exposure, do not share unblocked causes with the outcome, and affect the outcome only through the exposure. Two-sample MR estimates the variant-exposure and variant-outcome relationships in different summary datasets. These assumptions are not guaranteed by sample size; pleiotropy, phenotype definition, sample overlap, population structure, selection, and weak instruments can invalidate an estimate.

### Data and instrument selection

Table I reports 44,563 participants for the periodontitis exposure and 26,792 for dental caries, both from GLIDE-related data. The methods describe the overall lung-cancer GWAS as 29,266 cases plus 56,450 controls of European ancestry. Lung-function GWAS data cover 400,102 European-ancestry participants. Subtype table totals are 65,864 for adenocarcinoma, 23,371 for small-cell carcinoma, and 62,467 for squamous-cell cancer (E3).

The paper's abstract instead says the genetic instruments derive from data including 487,823 dental-caries and 506,594 periodontitis "cases." These figures do not match Table I. They may refer to a broader upstream meta-analysis population rather than the phenotype-specific samples used here, but that is not established by the inspected source. The exposure scale and denominator need clarification.

The authors use a genome-wide significance threshold of `5 x 10^-8` for dental caries but relax the periodontitis threshold to `5 x 10^-6` to obtain additional variants. They clump variants at `r^2 < 0.001` over a stated 10,000 kb window and require F statistics above 10. After harmonization and filtering, the text reports 20 final periodontitis instruments and 15 final dental-caries instruments. Lung-function analyses begin with 241 FVC, 271 FEV1, and 305 FEV1/FVC variants; the mediator-outcome harmonization retains 207, 240, and 276, respectively (E2).

### Estimation and diagnostics

IVW is the primary estimator. MR-Egger and weighted-median estimates are supporting checks. PhenoScanner is used to remove variants associated with candidate confounders, especially smoking-related traits. MR-PRESSO identifies outliers and tests whether their removal materially changes an estimate. Cochran's Q tests heterogeneity. The MR-Egger intercept tests directional pleiotropy, although a nonsignificant intercept is not proof that all exclusion restrictions hold.

For lung-function effects, the authors add multivariable MR with height because height can influence spirometric traits. For mediation, the exposure-to-mediator coefficient is multiplied by the mediator-to-outcome coefficient. The product is divided by the total exposure-outcome effect to obtain a mediated proportion, and bootstrap confidence intervals are reported (E2).

The implementation uses R 4.3.1, TwoSampleMR 0.5.7, MRPRESSO 1.0, MRInstruments 0.3.2, MRPracticals 0.0.1, and RMediation 1.2.2. Exact scripts, package lockfiles, random seeds, harmonized variant lists, and result manifests were not available from an established official repository.

### Oral traits and lung cancer

The primary reported IVW estimates for dental caries are:

| Outcome | OR | 95% CI | p value | Source note |
|---|---:|---:|---:|---|
| Overall lung cancer | 2.525 | 1.454-4.384 | 0.001 | Significant heterogeneity: Q p=0.006 |
| Adenocarcinoma | 2.456 | 1.299-4.642 | 0.006 | Wide interval |
| Small-cell lung carcinoma | 4.175 | 1.316-13.247 | 0.015 | Very wide interval |
| Squamous-cell lung cancer | 2.880 | 1.236-6.713 | 0.014 | Headline subtype result |

The MR-Egger intercept for dental caries and overall lung cancer is reported as `-0.003`, p=0.915. One MR-PRESSO outlier is identified, but its removal does not materially change the result according to a distortion-test p value of 0.555. The paper says secondary estimators are directionally robust. Exact secondary estimates are not tabulated in the inspected main paper.

Periodontitis is null for overall lung cancer after one height-associated instrument is removed: OR 1.137 (95% CI 0.797-1.623, p=0.479). One later MR-PRESSO outlier materially affects the estimate, but the outlier-removed result remains nonsignificant: OR 0.546 (95% CI 0.259-1.151, p=0.130). The paper reports no significant periodontitis effect for the three subtypes (E4).

### Lung function and mediation

Dental caries is associated with lower FVC and FEV1:

| Mediator | Caries effect | 95% CI | p value | Heterogeneity p | MR-Egger intercept p |
|---|---:|---:|---:|---:|---:|
| FVC | OR 0.819 | 0.726-0.923 | 0.001 | 0.004 | 0.043 |
| FEV1/FVC | OR 1.024 | 0.875-1.197 | 0.771 | `2.868 x 10^-8` | 0.025 |
| FEV1 | OR 0.857 | 0.769-0.954 | 0.005 | 0.004 | 0.710 |

The significant FVC intercept and the significant FEV1/FVC intercept are warnings for directional pleiotropy in parts of the mediator analysis. The ratio is not significant as a caries mediator and does not enter the reported significant mediation path.

For the second mediation step, FVC is inversely associated with squamous-cell lung cancer (`beta=-0.271`, OR 0.762, 95% CI 0.604-0.962, p=0.022), and FEV1 is also inverse (`beta=-0.402`, OR 0.669, 95% CI 0.549-0.815, p=`6.38 x 10^-5`). The corresponding overall lung-cancer effects are not significant. The authors report an indirect effect of 0.054 (95% CI 0.006-0.121) for FVC and 0.062 (95% CI 0.016-0.123) for FEV1, producing mediated proportions of 5.124% and 5.890% (E4).

These proportions imply that most of the reported caries-squamous association is not explained by the measured spirometric path. The mediation result also inherits assumptions from both MR steps. A significant product is not insulated from pleiotropy, measurement differences, sample overlap, selection, or multiplicity.

### Publication and implementation context

The reviewed source is arXiv v1 from July 2025. Public bibliographic records later identify an IEEE BIBM 2025 proceedings version at pages 1443-1449 with DOI `10.1109/BIBM66473.2025.11357049` (E6). The arXiv record remains v1 in the inspected evidence set, so possible proceedings revisions were not silently substituted.

The paper says the project would be open-sourced upon acceptance. A bounded search by exact title, arXiv ID, and DOI did not establish an official repository. This is negative discovery evidence only. Code and data availability should be rechecked before any replication.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Genetic liability to dental caries is associated with overall lung cancer under IVW. | Author empirical claim | E4 | Supported as a reported result; heterogeneity and MR assumptions limit the causal wording. | High for transcription; medium for inference |
| C2 | Dental caries is associated with adenocarcinoma, small-cell, and squamous-cell lung cancer. | Author empirical claim | E4 | All three displayed estimates are significant at 0.05, but intervals are wide and no multiplicity correction is described. | Medium |
| C3 | Periodontitis has no causal effect on lung cancer. | Author null conclusion | E4-E5 | No significant effect is reported, but a null result is not proof of no effect across populations or instrument choices. | Medium |
| C4 | FVC and FEV1 mediate small portions of the caries-squamous relationship. | Author mediation claim | E4 | Reported proportions are 5.124% and 5.890%; the chain has heterogeneity and an FVC pleiotropy signal. | Medium |
| C5 | Sensitivity analyses eliminate major pleiotropy concerns. | Implied robustness claim | E2, E4 | Only partly supported. Table II has significant MR-Egger intercepts for FVC and FEV1/FVC, and MR-PRESSO cannot prove exclusion restrictions. | Medium-low |
| C6 | The dental exposure sample sizes are unambiguous. | Implied metadata claim | E1, E3 | Rejected. Abstract and Table I use materially different counts and labels. | High rejection confidence |
| C7 | The results generalize beyond European ancestry. | Possible broad inference | E3, E5 | Not established; all contributing consortia are described as European ancestry. | Low |
| C8 | Dental treatment would reduce lung-cancer incidence. | Possible intervention inference | E2-E5 | Not established. No dental intervention or screening trial was conducted. | Low |
| C9 | The results justify changing clinical screening guidelines. | Author-facing implication | E5, E10 | Premature without replication, intervention utility, calibration, decision curves, harms, costs, and guideline review. | Low |
| C10 | The paper's analysis is independently reproducible from the public record. | Reviewer assessment | E1-E6 | Not established; no official code, lockfile, harmonized SNP manifest, or executed reproduction was available. | High rejection confidence |
| C11 | A biomedical causal result needs a governed evidence chain before clinical use. | Reviewer synthesis | E7-E10 | Strongly supported as a cross-artifact design principle; implementation remains prospective. | Medium-high |

## Methodology

- `Research objective`: Preserve the paper's MR design, reported effects, diagnostics, limitations, publication context, and safe implementation implications in a schema-complete DEP-E artifact.
- `Sources inspected`: Canonical arXiv metadata; complete PDF; verified official full-paper HTML; IEEE DOI; DBLP BIBM record; and exactly three related Black Lake artifacts.
- `Discovery strategy`: Enumerated the private archive with `rg --files -g "*.pdf"`, grouped PDFs by parent paper unit, derived arXiv identifiers, built a cross-repository used-paper index, selected uniformly with PowerShell `Get-Random`, enforced a complete-source gate, rendered the PDF, searched public publication and code surfaces, and inspected related DEP records.
- `Inclusion criteria`: Primary-paper identity, method, data, instruments, estimators, tables, figures, diagnostics, results, discussion, limitations, publication records, and related entries with a concrete conceptual bridge.
- `Exclusion criteria`: Abstract-only empirical synthesis, unverified code claims, patient-level interpretation, source-file redistribution, invented DOI metadata, and unrelated medical artifacts.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product-research, and replication analysis.
- `Evidence handling`: Major source claims map to evidence IDs. Numerical values are labeled as reported. Reviewer interpretations and possible clinical inferences are separated from author evidence.
- `Uncertainty handling`: Source discrepancies, significant diagnostics, missing multiplicity policy, absent code, and unperformed reproduction remain explicit. No value was guessed or silently corrected.
- `Extraction process`: Local PDF and official HTML were validated independently. Searchable PDF/HTML text supported section extraction; all eight PDF pages were rendered and inspected for layout, Tables I-IV, and Figures 1-3.
- `Version control`: The scientific review is pinned to arXiv:2507.18287v1. Later BIBM metadata is treated as publication context, not as an unseen replacement manuscript.
- `Cross-checking`: Title, authors, date, venue, DOI, pages, sample tables, effect estimates, diagnostics, and limitations were cross-checked across the primary source and public records where available.
- `Safety handling`: Medical claims are bounded to research interpretation. No patient data, diagnosis, risk scoring, treatment recommendation, or screening advice is included.
- `Random selection`: 75,780 PDFs mapped to 75,777 units. A used index of 1,362 arXiv IDs excluded 352 units; 185 identifier-incomplete units were withheld. Uniform zero-based eligible index 70,409 was drawn from 75,240 units.
- `Deduplication and reselection validation`: Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and fetched Black-Lake-Data `origin/main` surfaces were checked. No match existed for arXiv ID, arXiv DOI, IEEE DOI, hyphenated/unhyphenated title, normalized title, or planned slug. The 24-hour cutoff was 2026-07-24. Duplicate rejections/reselections: 0.
- `Source repair`: Initial state was partial because full-paper HTML was absent. The existing valid PDF was preserved. A first brokered ID-search request failed closed on redirect and produced no partials; one final exact-title request acquired official full-paper HTML. The source unit and private cache were then verified.
- `Reviewer stance`: Source-grounded paper report, critique, DEP preservation record, implementation brief, medical-safety boundary, and replication plan.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's dental-trait exposures, lung-cancer outcomes, lung-function mediators, two-step MR workflow, reported diagnostics, results, limitations, related-DEP synthesis, and bounded implementation ideas.
- `Temporal boundary`: arXiv v1 and public bibliographic/code-discovery context through 2026-07-25.
- `Evidence limits`: No raw GWAS summary statistics, participant data, harmonized SNP list, analysis script, package environment, phenotype codebook, or proceedings manuscript was inspected. No estimate or diagnostic was independently recomputed.
- `Assumptions`: The validated local PDF and official full-paper HTML represent arXiv v1; the DOI/DBLP record correctly identifies the later proceedings version; table transcription is faithful to the rendered pages.
- `Constraints`: Public output contains no local paths, usernames, machine names, exact execution timestamps, timezone labels, or source files. Medical content remains research-only.
- `Out of scope`: Diagnosing or advising patients; estimating absolute risk; recommending dental treatment to prevent cancer; modifying screening criteria; certifying causal identification; or reproducing the analysis.
- `Intended use`: DEP deposition, literature review, replication planning, evidence-workbench design, and governance discussion.
- `Audience`: Epidemiologists, geneticists, dental and pulmonary researchers, research engineers, clinical-AI reviewers, and Black Lake maintainers.
- `Depth target`: Full manuscript review with evidence ledger, technical reconstruction, critical interpretation, implementation paths, and replication checklist.
- `Reproducibility boundary`: Source claims are inspectable, but numerical reproduction requires upstream GWAS versions, exact phenotype definitions, variant lists, harmonization rules, scripts, package locks, seeds, and expected outputs.
- `Operational boundary`: Any real biomedical analysis requires institutional approval, secure computation, domain review, and aggregate-only publication where appropriate. No patient-facing action may derive directly from this artifact.
- `Data sensitivity`: Public scholarly metadata plus private local scholarly source copies; no participant-level or controlled biomedical data were accessed.

## Observations

- `Observed pattern`: Dental caries is positive across all four displayed cancer outcomes, while periodontitis is null. The consistency of direction is notable, but the subtype intervals are wide and related tests are not multiplicity-adjusted in the paper.
- `Observed pattern`: The mediation proportions are small. FVC and FEV1 explain only about five to six percent of the reported caries-squamous effect.
- `Diagnostic tension`: The paper describes sensitivity analyses as robust, but Table II reports significant heterogeneity and MR-Egger intercept signals for FVC and FEV1/FVC. Robustness is therefore estimator- and path-specific.
- `Metadata tension`: The abstract's 487,823/506,594 dental "cases" do not match Table I's 26,792/44,563 exposure sample sizes. Downstream summaries should not repeat both without qualification.
- `Technical implication`: An MR evidence system should store every estimate with exposure scale, outcome, ancestry, instrument count, estimator, harmonization version, heterogeneity, pleiotropy, outlier, overlap, and multiplicity status.
- `Clinical implication`: Even a valid liability estimate does not define the absolute benefit or harm of treating caries, measuring spirometry, or changing low-dose CT eligibility.
- `Open question`: Would the caries estimates survive corrected multiplicity, nonoverlapping samples, alternative clumping and instrument thresholds, colocalization, Steiger directionality, and diverse-ancestry replication?
- `Reviewer hypothesis`: The large caries odds ratios and small mediation fractions may reflect a mixture of true shared biology, instrument/phenotype scaling, residual pleiotropy, selection, and unmodeled pathways. Only transparent replication can distinguish them.

## Considerations

- **Medical safety:** This artifact must not be rendered as patient advice. Genetic liability and population summary estimates are not individual risk.
- **Multiplicity:** A preregistered primary outcome and an explicit family-wise or false-discovery procedure are needed for the related outcome and mediator tests.
- **Instrument validity:** Report per-SNP associations, F statistics, PhenoScanner exclusions, Steiger directionality, leave-one-out plots, and outlier decisions.
- **Sample overlap:** Quantify overlap between dental and lung-function GWAS sources, especially where UK Biobank contributes to both, and evaluate weak-instrument bias under overlap.
- **Phenotype semantics:** Distinguish participants, cases, controls, effective sample sizes, broad dental-trait definitions, and the scale corresponding to a one-unit genetic-liability change.
- **Population transfer:** Replicate in ancestrally diverse cohorts and report transportability rather than assuming a European estimate generalizes.
- **Selection:** Test survivor and collider-bias sensitivity, particularly for cancer GWAS enrollment and smoking-related selection.
- **Clinical translation:** Require prospective cohorts, intervention evidence, calibration, decision-curve analysis, harms, costs, patient values, and guideline governance.
- **Privacy:** Protected genotype and health data should remain institution-local, with aggregate outputs, immutable job records, and least-privilege access.
- **Maintenance:** Publication versions, GWAS releases, variant annotations, packages, and code repositories can change. Every result needs a refresh and invalidation rule.

## Strengths

- The paper addresses an important confounding-heavy question with a design intended to reduce reverse causation.
- Exposure, mediator, outcome, and mediation stages are separated and visually explained through a directed acyclic graph.
- Multiple estimators and diagnostics are used rather than relying on IVW alone.
- The authors inspect outliers, heterogeneity, pleiotropy, instrument strength, candidate confounders, and height in the lung-function stage.
- The paper reports subtype effects and separates periodontitis from dental caries.
- The discussion acknowledges ancestry, binary phenotypes, subtype, survival-selection, smoking, and collider limitations.
- The complete source is concise enough for full table and figure inspection, and the later BIBM record supplies publication context.

## Weaknesses

- The abstract and Table I present materially different dental sample counts and labels.
- The exposure scale behind the large odds ratios is not clear enough for safe interpretation.
- No explicit multiple-testing correction is described despite several related cancer and mediator outcomes.
- Significant heterogeneity and MR-Egger intercept signals complicate the robustness narrative.
- The relaxed periodontitis instrument threshold creates a different instrument-quality regime from dental caries.
- Sample overlap is not quantified.
- All datasets are European ancestry, limiting transportability.
- Binary phenotypes, survivor selection, and residual smoking confounding remain.
- No official code, exact environment, harmonized variant manifest, or independent reproduction was established.
- Clinical prevention and screening implications extend beyond the evidence supplied by MR.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Reconcile every sample count and exposure scale | Metadata and interpretation | Abstract and Table I differ materially | Prevents denominator and odds-ratio misinterpretation | Requires upstream GWAS audit | Versioned data dictionary and source-linked table |
| Predeclare primary hypotheses and multiplicity control | Statistical validity | Several related outcomes and mediators are tested | Reduces false-positive risk | Lower apparent discovery count | Registered analysis plan plus corrected q/p values |
| Publish exact harmonized SNP manifests | Reproducibility | Instrument filtering determines the result | Enables independent rerun and diagnostic audit | Privacy/redistribution review may be needed | Checksums, variant tables, exclusion reasons, expected counts |
| Quantify sample overlap and weak-instrument bias | MR validity | UK Biobank may contribute to multiple stages | Clarifies bias direction and magnitude | Requires consortium metadata | Nonoverlap sensitivity and simulation |
| Add colocalization and directionality checks | Exclusion and direction assumptions | Shared loci can act through alternate pathways | Stronger mechanistic confidence | More modeling and locus data | Colocalization posterior, Steiger tests, locus plots |
| Replicate across ancestries and cohorts | Generalization | Current evidence is European-only | Tests transportability and heterogeneity | Data access and harmonization cost | Prespecified meta-analysis with ancestry-stratified estimates |
| Separate prediction, causality, and intervention claims | Clinical translation | MR does not establish treatment benefit | Safer interpretation and guideline use | May narrow conclusions | Clinical-evidence ladder with explicit gate criteria |
| Release code, lockfile, and executed result manifest | Reproducibility | Paper promises code but none was established | Auditable computational lineage | Engineering and maintenance burden | Containerized rerun with table-level equality checks |

## Potential Implementations

### MR evidence dossier

- `User`: Epidemiology reviewers and research-integrity teams.
- `Goal`: Turn a paper into a structured, versioned causal-evidence record.
- `Core mechanism`: Capture phenotype definitions, sample counts, instruments, estimator results, diagnostic p values, multiplicity, ancestry, overlap, source versions, and claim boundaries.
- `Required inputs`: Public paper sources, supplement, code/manifests when available, and reviewer annotations.
- `Outputs`: Evidence ledger, discrepancy report, diagnostic matrix, and replication checklist.
- `Risk controls`: No patient data, no automatic causal verdict, explicit unavailable fields, and human statistical review.
- `Evaluation`: Double extraction against expert reviewers and table-level transcription tests.

### Governed GWAS reanalysis broker

- `User`: Institutional genetic epidemiology teams.
- `Goal`: Reproduce a declared analysis without exporting protected genotype or health data.
- `Core mechanism`: Approved workflows execute near the data; only aggregate QC, estimates, diagnostics, and signed manifests leave the secure environment.
- `Required inputs`: Authorized datasets, phenotype codebooks, workflow container, access policy, and analysis plan.
- `Outputs`: Aggregate results, job receipt, source hashes, exclusion counts, and comparison with the paper.
- `Risk controls`: Least privilege, aggregate-only policy, minimum-cell rules, immutable logs, human approval, and no model-generated phenotype changes without review.
- `Evaluation`: Reproducibility, privacy-policy conformance, phenotype agreement, and deterministic reruns.

### Clinical translation readiness gate

- `User`: Guideline, clinical-AI, and translational research committees.
- `Goal`: Prevent a research association from becoming a patient action before its evidence ladder is complete.
- `Core mechanism`: Require causal replication, population transport, intervention utility, calibration, decision curves, harms, costs, and governance evidence.
- `Required inputs`: Replication studies, intervention evidence, external validation, stakeholder review, and policy thresholds.
- `Outputs`: Ready/not-ready decision with explicit missing evidence and owner.
- `Risk controls`: No patient scoring, conservative default, conflict-of-interest record, periodic re-review, and domain-expert veto.
- `Evaluation`: Retrospective application to known translated and nontranslated biomarkers plus committee usability tests.

### Diagnostic consistency monitor

- `User`: Research engineers maintaining MR evidence collections.
- `Goal`: Detect internal inconsistencies before publication or deposition.
- `Core mechanism`: Compare abstract, methods, tables, figures, supplement, and code manifests for sample counts, instruments, signs, intervals, and p values.
- `Required inputs`: Structured extraction of every source surface.
- `Outputs`: Mismatch list with source coordinates and severity.
- `Risk controls`: Never autocorrect; require source-linked resolution; preserve the original statement.
- `Evaluation`: Seeded discrepancies and blinded reviewer resolution rates.

## Three Ways to Exercise This Research

1. `Table-to-ledger audit`: Objective - test whether every headline statement maps to a source table or paragraph; inputs - the public arXiv HTML and a blank evidence-ledger template; method - independently extract sample counts, instruments, estimates, diagnostics, and limitations, then compare the abstract with Tables I-IV; output - a discrepancy and provenance ledger; success criterion - every numeric claim has a source coordinate and the sample-count mismatch remains explicit; stop condition - do not infer a correction without upstream evidence.
2. `Synthetic MR diagnostic lab`: Objective - understand how pleiotropy, heterogeneity, weak instruments, and multiplicity affect interpretation; inputs - synthetic summary statistics with known data-generating assumptions; method - run IVW and toy sensitivity checks across controlled violations; output - diagnostic-response plots and a reviewer checklist; success criterion - the exercise detects the seeded violations; stop condition - do not transfer synthetic behavior into a clinical claim.
3. `Clinical-evidence ladder workshop`: Objective - separate association, causal estimation, prediction, intervention, and guideline evidence; inputs - this paper, the three related DEP artifacts, and a blank translation matrix; method - assign each claim to its evidence level and list the next required study; output - a gated research roadmap; success criterion - no screening or treatment recommendation passes without intervention and utility evidence; stop condition - stop at research planning, not patient decision support.

## Example MVP Product

- `Product name`: MR Evidence Workbench.
- `Target user`: Epidemiologists, evidence reviewers, and governed biomedical research teams.
- `Problem`: MR papers often distribute critical assumptions and diagnostics across abstracts, prose, tables, supplements, and code, making overinterpretation and silent mismatch likely.
- `Core workflow`: Register a paper version; extract source metadata and tables; map claims to evidence; capture instruments and diagnostics; flag discrepancies and missing fields; attach related evidence; export a public-safe review and a private replication plan.
- `Data requirements`: Public scholarly sources by default. Protected GWAS data are optional and remain institution-local behind a separately authorized broker.
- `Architecture`: Local parser and reviewer UI; versioned evidence graph; validation engine; public-safe export layer; optional institution-local execution adapter; immutable audit receipt.
- `Success metrics`: Table transcription accuracy; claim-to-evidence coverage; seeded-discrepancy recall; inter-reviewer agreement; zero private-path or participant-data leaks; time to complete a replication-ready dossier.
- `Risk controls`: No patient-level scoring; no automatic causal or clinical verdict; conservative missing-field states; least-privilege execution; aggregate-only exports; domain-expert approval; immutable provenance; medical-use warning.
- `Limitations`: The MVP cannot prove MR assumptions, validate phenotype quality, replace expert causal analysis, or establish clinical utility.
- `MVP boundary`: One paper version, public sources, manually reviewed extraction, and offline research use.
- `Deployment model`: Local desktop or institution-hosted service with no default external data transfer.
- `Evaluation plan`: Unit tests for schema and arithmetic; seeded source inconsistencies; blinded double extraction; expert review of diagnostic flags; public-safety scans.
- `Failure modes`: Wrong table parsing, conflated exposure scales, missing diagnostic context, stale source versions, overconfident clinical wording, or protected-data leakage.
- `Maintenance plan`: Version-pinned schemas, source refresh receipts, invalidation when paper/GWAS/code versions change, dependency monitoring, and periodic expert audit.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Causal DP Workloads - DEP-E | Related DEP manuscript | Shows why causal estimands and calibrated uncertainty must survive data-release and transformation choices | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Causal%20DP%20Workloads/causal-dp-workloads.md |
| Agent Systems Map - DEP-E | Related DEP manuscript | NAIS provides governed GWAS execution, aggregate-only outputs, and human phenotype reconciliation | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-Agent%20Systems%20Map/agent-systems-map.md |
| ClinRAG-GRAPH review | Related DEP review | Adds multi-center testing, domain shift, evidence grounding, and clinical-translation governance | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ClinRAG%20Graph/2607.00798-whitepaper-review.md |
| BIBM 2025 proceedings record | Publisher context | Establishes the later proceedings DOI for the reviewed work | https://doi.org/10.1109/BIBM66473.2025.11357049 |
| DBLP BIBM record | Bibliographic context | Confirms title form, author list, venue, and pages 1443-1449 | https://dblp.org/rec/conf/bibm/ZhangLWNWY25 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2507.18287v1 | Canonical identity, authors, v1 date, abstract, and headline results | 2026-07-25 | Primary record |
| R2 | https://arxiv.org/html/2507.18287v1 | Complete methods, data descriptions, results, tables, figures, discussion, limitations, and references | 2026-07-25 | Primary full text; source file withheld locally |
| R3 | https://arxiv.org/pdf/2507.18287v1 | Visual confirmation of eight pages, Tables I-IV, and Figures 1-3 | 2026-07-25 | Primary PDF; source file withheld locally |
| R4 | https://doi.org/10.48550/arXiv.2507.18287 | Stable arXiv DOI | 2026-07-25 | Bibliographic locator |
| R5 | https://doi.org/10.1109/BIBM66473.2025.11357049 | IEEE BIBM proceedings context | 2026-07-25 | No publisher file collected |
| R6 | https://dblp.org/rec/conf/bibm/ZhangLWNWY25 | BIBM title, authors, venue, and pages | 2026-07-25 | Bibliographic locator |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Causal%20DP%20Workloads/causal-dp-workloads.md | Causal estimands, privacy, approximation, and interval calibration | 2026-07-25 | Related DEP; inspected |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-Agent%20Systems%20Map/agent-systems-map.md | Governed biomedical GWAS, phenotype reconciliation, and aggregate-only execution | 2026-07-25 | Related DEP; inspected |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ClinRAG%20Graph/2607.00798-whitepaper-review.md | Clinical prediction, external validation, evidence grounding, and governance | 2026-07-25 | Related DEP; inspected |

No local source paths or files are listed in this public artifact. The private source inventory contains the verified PDF, official full-paper HTML, search-provenance records, extraction cache, rendered pages, receipt, and verification records; none was deposited or uploaded.

## Appendix

### A. Random selection and deduplication record

| Field | Value |
|---|---|
| Enumeration command | `rg --files -g "*.pdf"` |
| PDF count | 75,780 |
| Parent-unit count | 75,777 |
| Used arXiv base IDs | 1,362 |
| Used-ID units excluded | 352 |
| Identifier-incomplete units withheld | 185 |
| Eligible units | 75,240 |
| Selection method | PowerShell `Get-Random`, uniform array index |
| Selected zero-based index | 70,409 |
| Selected ID | 2507.18287 |
| Duplicate rejections/reselections | 0 |
| 24-hour cutoff date | 2026-07-24 |
| Exact-match fields | arXiv ID; arXiv DOI; IEEE DOI; normalized title; title variants; slug |
| Dedup surfaces | Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; fetched Black-Lake-Data `origin/main` equivalents |

### B. Source-integrity verification

| Check | Result |
|---|---|
| Initial state | Partial: complete PDF present, full-paper HTML absent |
| Repair | Bounded brokered exact-title acquisition after one failed-closed ID-search redirect |
| Existing PDF preserved | Yes; byte-identical to broker copy |
| PDF size | 3,192,319 bytes |
| PDF header | `%PDF-` present |
| PDF trailer | `%%EOF` present |
| PDF pages | 8, unencrypted |
| PDF SHA-256 | `007BC2DD4B8CD88C822F0F8A7E78A40B5BD43803F79AE6457ADF766C6486FE1A` |
| Full-paper HTML | Official arXiv HTML |
| HTML size | 187,338 bytes |
| Stripped body characters | 53,098 |
| Document marker | Present |
| Heading markers | 48 |
| Structure terms | Six |
| Partial files | 0 |
| Local cache | PDF and HTML text cached |
| TeX/source package | Not collected |
| Public source upload | None |

### C. Replication checklist

- [ ] Obtain exact dental, lung-function, and TRICL/ILCCO summary-statistics releases with licenses and checksums.
- [ ] Resolve abstract-versus-Table-I sample counts and define every phenotype and exposure scale.
- [ ] Publish exact selected, excluded, harmonized, palindromic, confounder-associated, and outlier SNP lists.
- [ ] Pin R, package, reference-panel, clumping, and PhenoScanner versions.
- [ ] Quantify sample overlap across exposure, mediator, and outcome datasets.
- [ ] Predeclare primary outcomes, mediator tests, and multiplicity correction.
- [ ] Reproduce IVW, weighted-median, MR-Egger, MR-PRESSO, Cochran Q, MVMR, and mediation tables.
- [ ] Add leave-one-out, Steiger, colocalization, and robust/weak-instrument sensitivity analyses.
- [ ] Reconcile every result between prose, tables, figures, supplement, and code output.
- [ ] Replicate in independent and diverse-ancestry cohorts.
- [ ] Separate causal-estimation evidence from intervention, absolute-risk, screening, and guideline claims.
- [ ] Publish a signed result manifest and compare every expected value before declaring reproduction.
