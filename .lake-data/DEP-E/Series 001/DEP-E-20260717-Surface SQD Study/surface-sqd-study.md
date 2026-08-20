---
title: "Surface SQD - DEP-E"
generated_at: "2026-07-17T00:02:46Z"
artifact_type: "DEP research artifact"
primary_subject: "Iterative full-paper review of sample-based quantum diagonalization for lithium-oxygen surface-reaction energy calculations."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-17"
temporal_cutoff: "Canonical sources and repository context available through 2026-07-17."
primary_url: "https://arxiv.org/abs/2503.10923"
stable_identifier: "arXiv:2503.10923v2; DOI:10.1038/s41598-026-58228-0"
confidence_summary: "Medium-high for the documented workflow and reported results; lower for independent accuracy and scalability because no calculation, hardware run, or source-specific reproduction package was reproduced."
safety_scope: "research review, materials-science simulation, non-operational battery interpretation"
distribution_notes: "Generated synthesis only; no paper PDF, source archive, dataset, hardware output, or external source file is redistributed."
---

# Surface SQD - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected source DEP | Primary provenance bundle | Repository Markdown | DEP-20260624-Tech Intel 2338 | Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338/README.md | Repository material; preserve attribution. | 2026-07-17 | Inspected. |
| S2 | Daily Research Findings | Primary generated source artifact | Repository Markdown | daily_research_findings_2026-06-24_2338.md | Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338/daily_research_findings_2026-06-24_2338.md | Generated discovery synthesis; claims require primary-source checking. | 2026-07-17 | Inspected. |
| S3 | Prior Black-Lake processing trail | Iteration context | Report, Report-Mark, log, and manuscript | 2026-07-09 pass | Black-Lake-Data/.reports/BL-DEP-20260624-Tech Intel 2338-20260709/README.md; Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338/BL-DEP-Mark001 Report-Mark.md; Black-Lake/.logs/20260709-DEP-20260624-Tech Intel 2338-LOG.md; Black-Lake/.lake-data/DEP-E/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md | Repository artifacts; used to identify the expansion pool and prior evidence boundary. | 2026-07-17 | Inspected. |
| S4 | Scaling active spaces in simulations of surface reactions through sample-based quantum diagonalization | Primary paper record | arXiv metadata and full-paper HTML | arXiv:2503.10923v2, revised 2025-10-29 | https://arxiv.org/abs/2503.10923; https://arxiv.org/html/2503.10923 | arXiv record links a Creative Commons license; no source file collected. | 2026-07-17 | Canonical record and full text inspected. |
| S5 | Scientific Reports article | Peer-reviewed publication record | Journal article page | DOI:10.1038/s41598-026-58228-0; published 2026-06-22 | https://www.nature.com/articles/s41598-026-58228-0 | Open access under CC BY 4.0; publisher page labels the displayed manuscript as an unedited early-access version. | 2026-07-17 | Abstract, publication metadata, appendix locator, authorship, and license inspected. |
| S6 | Quantum computation of reactions on surfaces using local embedding | Methodological predecessor | Journal article cited by S4 | DOI:10.1038/s41534-023-00753-1 | https://doi.org/10.1038/s41534-023-00753-1 | Discovery/related-work source; not independently full-text reviewed in this pass. | 2026-07-17 | Citation and identifier inspected through S4. |
| S7 | Chemistry Beyond Exact Solutions on a Quantum-Centric Supercomputer | SQD method neighbor | arXiv paper cited by S4 | arXiv:2405.05068 | https://arxiv.org/abs/2405.05068 | Discovery/related-work source; not independently full-text reviewed in this pass. | 2026-07-17 | Citation and identifier inspected through S4. |
| S8 | Quantum-centric computation of molecular excited states with extended sample-based quantum diagonalization | Ext-SQD method neighbor | arXiv paper cited by S4 | arXiv:2411.00468 | https://arxiv.org/abs/2411.00468 | Discovery/related-work source; not independently full-text reviewed in this pass. | 2026-07-17 | Citation and identifier inspected through S4. |
| S9 | Local Unitary Cluster Jastrow ansatz | State-preparation method | Journal article cited by S4 | DOI:10.1039/D3SC02516K | https://doi.org/10.1039/D3SC02516K | Discovery/related-work source; not independently full-text reviewed in this pass. | 2026-07-17 | Citation and identifier inspected through S4. |
| S10 | Live repository standards | Deposition authority | Repository Markdown | main branch fetched 2026-07-17 | Black-Lake/README.md; Black-Lake/.lake-data/README.md; Black-Lake-Data/README.md | Repository authority for paths, DEP class, index, attribution, and source-side reporting. | 2026-07-17 | Inspected after fetch. |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S3 | Repository provenance | Selected DEP inventory, ten-item prior reading pool, first-pass evidence boundary, prior log, and exact copied reference sections. | Selection lineage, iterative-expansion status, and source inventory. | High | Repository records establish provenance, not scientific validity. |
| E2 | S4 | Canonical arXiv record | Title, authors, v1/v2 dates, 25-page/7-figure extent, abstract, 80-qubit and 32-orbital headline claims, and journal DOI. | Paper identity and canonical abstract-level claims. | High | Abstract does not expose all experimental detail; some values differ from the rendered full text. |
| E3 | S4 | Full paper | DFT-to-active-space workflow, DDA, CCSD natural orbitals, Jordan-Wigner mapping, LUCJ preparation, SQD/Ext-SQD mechanics, and classical comparators. | Method and mechanism claims. | High | The HTML renderer omits several mathematical symbols and table values. |
| E4 | S4 | Full paper figures/tables and surrounding text | Table 1 circuit sizes; 93.57% average forbidden configurations; 97.46%/98.32% at 30 orbitals; 2,714 gates; small-space CASCI comparison; classical bottleneck beyond 30 orbitals. | Quantitative findings and scaling limits. | Medium-high | No raw samples, calibration snapshot, uncertainty analysis, or independent rerun was available. |
| E5 | S4 | Full paper discussion and declarations | Noise, circuit-depth, state-preparation, and classical-diagonalization limits; listed open-source packages and closed-source VASP dependency. | Reproducibility and deployment limits. | High | Listing dependencies is not a source-specific code/data release. |
| E6 | S5 | Publisher record | Peer-reviewed venue, publication date, DOI, author affiliations, CC BY 4.0 license, early-access warning, and abstract claims. | Publication status, attribution, and license. | High | Main publisher HTML exposed limited body text during inspection. |
| E7 | S6-S9 | Primary-paper reference list | Stable identifiers and roles of local embedding, SQD, Ext-SQD, and LUCJ predecessor work. | Related research expansion. | Medium | These works were discovered and identified but not independently reviewed in full. |
| E8 | S10 | Repository standards | Containerized DEP-E filing, publication-index maintenance, final Attribution Block, and source-file restrictions. | Deposit shape and submission validation. | High | Policy evidence only. |

## Executive Summary

This iterative pass expands the earlier abstract-level treatment of `arXiv:2503.10923` into a full-paper review. The paper studies lithium-oxygen surface-reaction energies with a hybrid workflow: classical geometry optimization and electronic-structure calculations feed a density-difference and coupled-cluster-natural-orbital active-space selector; a truncated two-layer Local Unitary Cluster Jastrow circuit samples electronic configurations on IBM quantum hardware; Sample-Based Quantum Diagonalization (SQD) and Extended SQD (Ext-SQD) then diagonalize selected configuration subspaces on classical compute.

The strongest evidence is methodological, not a general quantum-advantage demonstration. The authors report that Ext-SQD stays close to CASCI in small active spaces and reaches lower variational energies than feasible HCI/CCSD comparisons at larger spaces. Yet the hardware samples are dominated by invalid electron-count configurations: 93.57% on average, rising at 30 orbitals to 97.46% for the reactant and 98.32% for the product. Ext-SQD improves the usable subspace through single excitations, but its classical diagonalization grows quickly and becomes the stated bottleneck beyond roughly 30 orbitals.

Reviewer confidence is medium-high that the paper demonstrates a coherent hybrid pipeline on real hardware. Confidence is lower that it establishes practical materials-discovery superiority, battery-performance prediction, or scalable quantum advantage. The calculation was not reproduced; raw device samples and a source-specific workflow release were not identified; VASP is closed source; and the public record contains visible scale tensions. The canonical abstract says up to 32 orbitals and 80 qubits, while the rendered full text describes quantum calculations up to 30 orbitals and Table 1 lists 76 total qubits for those circuits. Likewise, the abstract names CASCI validation up to 12 orbitals, whereas the full text discusses CASCI feasibility and comparisons up to 14. These values are preserved as version or reporting tensions rather than silently reconciled.

## Detailed Summary

### Problem and scientific setting

The research object is an oxygen-reduction reaction at a lithium-metal electrode surface. Exact correlated-electron solutions are intractable at useful system sizes, while common density-functional approximations can miss strong-correlation effects. The paper therefore asks whether a carefully embedded, active-space quantum calculation can improve ground-state and reaction-energy estimates without requiring the full electronic problem to run on quantum hardware.

This is a computational chemistry study. It does not experimentally measure battery cycle life, dendrite suppression, safety, or device performance. The reaction-energy calculations are intended as inputs to materials understanding, and the paper's battery implications should remain at that level.

### Classical preparation and active-space selection

Geometry optimization uses VASP for a lithium slab treated periodically in the surface plane, with a reported 6.1 angstrom slab thickness and a 12 angstrom vacuum layer. Subsequent DFT/electronic-structure work uses PySCF, a GTH-DZV basis, GTH pseudopotentials, the PBE functional, and density fitting. The full text states that the electronic-structure calculation is restricted to the gamma point after checking that additional k-points did not materially change the electronic density.

The active-space pipeline is physically targeted. Pipek-Mezey localization is followed by density-difference analysis (DDA) between reactant and product. Orbitals are ranked by contribution to the reaction-associated density change, with a threshold scan used to find a stable ranking region. The selected space is refined with CCSD natural orbitals and grows outward from the highest occupied and lowest unoccupied natural orbitals. The authors report no fractionally occupied natural orbitals in the studied systems, which limits how strongly the example itself probes multireference character.

### Quantum sampling and diagonalization

The active-space Hamiltonian is mapped with Jordan-Wigner encoding. A truncated two-layer LUCJ circuit is preferred because its sampled distribution is less dominated by the Hartree-Fock reference than the non-truncated one-layer circuit shown in Figure 5. Circuits were built with `ffsim`, mapped to calibrated qubits on `ibm_torino`, and sampled into bitstring distributions.

SQD projects the Hamiltonian into a configuration subspace recovered from noisy samples while enforcing particle-number and spin-sector constraints. Ext-SQD starts from SQD results, discards very small-amplitude configurations, and expands the selected space with excitation operators. This paper limits Ext-SQD to single excitations. That design improves the variational space but causes the classical subspace dimension to grow rapidly; the authors explicitly state that the bottleneck moves from quantum sampling to classical diagonalization beyond 30 orbitals.

### Reported comparisons and limits

CASCI provides the strongest exact active-space reference where feasible, while HCI and CCSD are used at larger spaces. The paper reports Ext-SQD below the chemical-accuracy threshold relative to CASCI in the small-space regime and lower variational energies than HCI/CCSD beyond it. This comparison requires care: CCSD is non-variational and can fall below the true ground-state energy, while CASCI, HCI, SQD, and Ext-SQD are treated as variational upper bounds for a fixed Hamiltonian. A lower variational energy is informative within that setting, but it is not by itself an experimental validation of reaction energy.

The quantum samples are extremely noisy in the physical-symmetry sense. Table 1 and the surrounding discussion report an average 93.57% forbidden configurations with incorrect Hamming weight. At 30 orbitals the forbidden share rises to 97.46% for the reactant and 98.32% for the product, and the largest displayed product circuit uses 76 total qubits, two-qubit depth 298, 2,714 CNOT gates, and 5,455 one-qubit gates. The paper calls this near the useful hardware limit. Ext-SQD can recover better energies from the resulting subspace, but the recovery and excitation machinery is a substantial part of the claimed performance.

### Publication and reproducibility context

The arXiv record was submitted in March 2025 and revised in October 2025. Scientific Reports records receipt in November 2025, acceptance in June 2026, and publication on 22 June 2026 under CC BY 4.0. The publisher page visible during this review warns that the displayed manuscript is an unedited early-access version.

The paper lists PySCF, `ffsim`, Qiskit SDK, Qiskit Addons SQD, and Ray as open-source packages used, with VASP as closed source. No study-specific repository, input deck, raw quantum samples, calibration snapshot, or one-command reproduction workflow was identified in the inspected declarations. Reproduction would also require access to comparable IBM hardware or a deliberately bounded simulator study.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | A reaction-targeted DDA plus CCSD-natural-orbital selector can produce a compact active space for the lithium-oxygen surface calculation. | Author claim | E3 | The workflow is documented and physically motivated; its optimality is not independently tested. | Medium-high |
| C2 | Truncated two-layer LUCJ sampling yields a more relevant configuration distribution than the compared one-layer non-truncated circuit. | Author claim | E3, E4 | Supported by the Figure 5 comparison described in text, but only for the studied setup. | Medium |
| C3 | Ext-SQD improves on standard SQD by adding single excitations and gives closer small-space CASCI agreement. | Author claim | E3, E4 | Directly supported by the method and reported comparisons; no independent rerun. | Medium-high |
| C4 | The demonstrated scaling limit is jointly quantum and classical rather than purely a qubit-count problem. | Reviewer interpretation | E4, E5 | Strongly supported by high forbidden-sample rates, circuit growth, and the classical subspace-diagonalization bottleneck. | High |
| C5 | The paper demonstrates a real-hardware hybrid workflow, not a general or end-to-end quantum advantage for battery materials. | Reviewer assessment | E2-E6 | The evidence shows feasibility and comparative energies, but not total runtime, cost, uncertainty, or superiority over the best classical production workflow. | High |
| C6 | Headline scale values differ between the canonical abstract and rendered body. | Evidence-quality observation | E2-E4 | Abstract: 32 orbitals/80 qubits and CASCI through 12 orbitals; body: quantum results through 30 orbitals, 76-qubit Table 1 circuits, and CASCI discussion through 14. | High |
| C7 | The public dependency list does not establish full reproducibility. | Reviewer assessment | E5 | Raw inputs, device data, calibration, and source-specific orchestration were not identified. | High |

## Methodology

- `Research objective`: Expand one randomly selected prior related-reading item into a source-first, schema-complete DEP research artifact while preserving the selected source DEP's provenance.
- `Sources inspected`: Selected DEP README and findings file; prior report, Report-Mark, log, DEP README, and manuscript; canonical arXiv record; complete arXiv full-paper HTML; Scientific Reports article metadata/abstract/license; live Black-Lake and Black-Lake-Data README standards; selected method citations in the full paper's reference list.
- `Discovery strategy`: Repository marker inspection established prior material older than the 24-hour cutoff. PowerShell `Get-Random` selected one of the prior manuscript's ten related-reading items. Primary arXiv and publisher records were then inspected, followed by citation tracing for the immediate SQD, Ext-SQD, local-embedding, and LUCJ lineage.
- `Inclusion criteria`: Direct evidence about paper identity, workflow, active-space construction, hardware sampling, comparator methods, reported scale, limitations, code declarations, and publication status; near-primary method sources were included as annotated related reading.
- `Exclusion criteria`: Secondary summaries, marketing claims, unverified code-finder links, unrelated battery chemistry, and references not needed to explain the selected mechanism were excluded. No external file was collected.
- `Analytical approach`: Conceptual, empirical, comparative, implementation, product research, and replication analysis.
- `Evidence handling`: Author claims, source metadata, reviewer interpretation, and unresolved reporting tensions are labeled separately. Quantitative claims are tied to the canonical abstract or full-paper table/figure discussion.
- `Uncertainty handling`: Missing mathematical symbols in HTML, publisher early-access status, scale discrepancies, inaccessible raw samples, and lack of independent reproduction are explicit.
- `Extraction process`: Repository Markdown and web-rendered primary sources were read directly. Figures and tables were assessed from captions and surrounding extracted text; no image-based digitization or independent numeric recomputation was performed.
- `Version control`: arXiv v2 and the 2026 Scientific Reports DOI are preserved separately. The internal full-text HTML title variant is treated as a version artifact, while the canonical arXiv and journal title controls citation.
- `Reviewer stance`: Iterative DEP-ready review, evidence critique, and bounded replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The selected paper's hybrid active-space, LUCJ, SQD, and Ext-SQD workflow for lithium-oxygen surface-reaction energies, plus immediate method lineage.
- `Temporal boundary`: Sources accessed 2026-07-17; arXiv v2 revised 2025-10-29; journal publication dated 2026-06-22.
- `Evidence limits`: No paper PDF was stored, no raw samples or calibration data were available, HTML omitted some symbols/table fields, and no calculation or device run was reproduced.
- `Assumptions`: The canonical arXiv record and DOI identify the same research work despite the internal full-text title variant. Reported Table 1 values are interpreted from the rendered body as applying to the displayed 30-orbital circuits.
- `Constraints`: Public artifacts use repository-relative paths, public URLs, date-only or UTC-only provenance, and no local system information. Source documents are evidence only.
- `Out of scope`: Proving chemical accuracy, benchmarking total wall-clock advantage, validating battery performance, adjudicating all active-space methods, or making operational battery-design recommendations.
- `Intended use`: DEP deposition, source-preserving semantic-web expansion, technical review, and replication backlog planning.
- `Audience`: Quantum-computing researchers, computational chemists, materials-science reviewers, and Black-Lake maintainers.
- `Reproducibility boundary`: A bounded classical or simulator reconstruction is plausible from public method descriptions and packages; exact hardware reproduction is not supported by the inspected artifact set.
- `Data sensitivity`: Public research and repository material only.

## Observations

- `Observed pattern`: The paper's useful contribution is orchestration across several approximations—geometry, basis, active-space choice, ansatz, noisy sampling, configuration recovery, excitation expansion, and classical diagonalization—rather than a single quantum algorithm operating in isolation.
- `Technical implication`: Active-space selection and post-processing can dominate scientific validity even when the headline scale is expressed in qubits.
- `Evidence-quality observation`: A result that survives 93-98% forbidden raw configurations depends heavily on recovery and subspace construction; reporting should separate raw hardware quality from recovered energy quality.
- `Comparative observation`: Lower variational energy is meaningful for a fixed Hamiltonian, but comparison with non-variational CCSD and literature reaction energies does not replace experimental or higher-accuracy end-to-end validation.
- `Contradiction or tension`: The public abstract/body differences in orbital, qubit, and CASCI scales may reflect revision granularity, rounding, or different reactant/product cases. The inspected sources do not resolve this cleanly.
- `Open question`: How much of Ext-SQD's improvement persists under matched total classical cost, matched configuration-space dimension, and held-out active-space choices?

## Considerations

Reproduction should begin with a small active space and an exact CASCI reference, not with an 80-qubit device target. That isolates active-space selection, ansatz sampling, recovery, and excitation-expansion errors before hardware noise and classical scaling interact.

Any product or materials claim needs uncertainty accounting across geometry optimization, pseudopotentials, functional choice, gamma-point restriction, active-space thresholding, finite sampling, device calibration, recovery, and classical diagonalization. A single reaction-energy curve is not a battery-safety or lifetime prediction.

The dependency surface is mixed. Much of the workflow names open-source packages, but VASP is closed source and comparable IBM hardware access is nontrivial. A reproducibility package should provide open alternatives or explicitly distinguish exact reproduction from method-equivalent replication.

## Strengths

- The study connects a chemically motivated embedding and active-space pipeline to real quantum-hardware samples rather than presenting an isolated toy Hamiltonian.
- Small-space CASCI comparisons give a meaningful reference regime before exact diagonalization becomes infeasible.
- The paper exposes difficult scaling facts, including invalid-sample rates, gate growth, and the classical Ext-SQD bottleneck.
- Ext-SQD's mechanism is interpretable: sampled configurations are expanded with controlled excitation operators rather than corrected by an opaque learned model.
- The journal record provides stable authorship, DOI, publication dates, and an open-access license.

## Weaknesses

- Raw quantum samples, calibration snapshots, study-specific code, inputs, and execution manifests were not identified in the inspected public declarations.
- The very high forbidden-configuration rate means reported energy quality is inseparable from recovery and classical expansion choices.
- CASCI validation is limited to small spaces; larger-space comparisons rely on HCI and CCSD, each with its own approximation boundary.
- Ext-SQD's single-excitation subspace grows quickly and shifts the bottleneck to classical diagonalization, weakening simple qubit-scale narratives.
- The paper does not establish total runtime, energy, cost, or accuracy advantage against a best-effort classical workflow at matched resources.
- Canonical abstract and body scale values are not fully aligned in the inspected renderings.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release source-specific inputs, raw bitstrings, calibration data, and manifests. | Reproducibility | Package names alone cannot recreate the study. | Independent audit of recovery, sampling, and energies. | Hardware/provider data may require redaction. | Re-run small cases and compare hashes, counts, and energies. |
| Report matched-cost ablations for SQD, Ext-SQD, HCI, and CCSD. | Comparative evaluation | Current methods consume different quantum and classical resources. | Clearer attribution of advantage. | Requires careful implementation parity. | Compare error versus wall time, memory, samples, and subspace dimension. |
| Resolve 12/14-orbital and 76/80-qubit reporting differences. | Publication clarity | Scale claims should be unambiguous. | Cleaner downstream citation and replication. | Minor editorial effort. | Add a versioned table mapping each system, orbital count, and qubit count. |
| Add uncertainty propagation across the full chemistry pipeline. | Scientific validity | Geometry, functional, basis, active space, noise, and sampling all contribute. | More defensible reaction-energy conclusions. | Substantial compute and methodological work. | Sensitivity analysis and error bars at each pipeline stage. |
| Parallelize and benchmark Ext-SQD diagonalization. | Classical scaling | The paper identifies serial x86 post-processing as the current bottleneck. | Tests whether larger spaces are practically reachable. | May shift rather than remove bottlenecks. | Strong/weak scaling with fixed configuration sets. |
| Test alternative active-space selectors and stronger-correlation systems. | Generalization | The studied natural occupations are near zero or two. | Shows whether the method survives genuinely multireference cases. | Harder references and larger uncertainty. | Pre-register selection rules and compare against exact small-space solutions. |

## Potential Implementations

### 1. SQD Evidence Replayer

- `User`: Quantum-chemistry reviewer.
- `Goal`: Audit how sampled configurations, recovery, and single excitations change energy estimates.
- `Core mechanism`: Import public or synthetic bitstrings, enforce electron/spin constraints, build SQD and Ext-SQD subspaces, and compare with exact small-space references.
- `Required inputs`: Small Hamiltonian, electron/spin sector, bitstrings, recovery parameters, excitation order, and CASCI reference.
- `Outputs`: Subspace sizes, discarded-sample rates, energy errors, and cost traces.
- `Risk controls`: Synthetic or openly licensed molecules by default; no proprietary provider data.
- `Evaluation`: Deterministic replay tests and agreement with CASCI on toy systems.

### 2. Active-Space Sensitivity Ledger

- `User`: Computational chemist choosing a hybrid workflow.
- `Goal`: Quantify how DDA thresholds and natural-orbital ordering affect reaction energies.
- `Core mechanism`: Sweep selection thresholds, freeze each chosen space, and compare classical and simulated SQD estimates.
- `Required inputs`: Reactant/product densities, localized orbitals, CCSD natural occupations, and reference energies.
- `Outputs`: Stable-selection regions, orbital provenance, and energy-sensitivity plots.
- `Risk controls`: Preserve input licenses; avoid implying material performance from electronic-energy estimates alone.
- `Evaluation`: Selection stability and held-out reference error.

### 3. Hybrid Cost Frontier

- `User`: Research program manager evaluating quantum-centric chemistry claims.
- `Goal`: Compare error against total quantum and classical resource cost.
- `Core mechanism`: Normalize qubits, gates, samples, recovery iterations, subspace dimension, CPU time, memory, and error for SQD, Ext-SQD, HCI, and CCSD.
- `Required inputs`: Reproducible run manifests and matched Hamiltonians.
- `Outputs`: Pareto frontiers and bottleneck transitions.
- `Risk controls`: Label provider-specific assumptions and missing costs; no extrapolated advantage without measured support.
- `Evaluation`: Repeated runs with uncertainty intervals and independent cost accounting.

## Three Ways to Exercise This Research

1. `Exact small-space replay`: Objective: reproduce the SQD-to-Ext-SQD mechanism on a public toy Hamiltonian. Inputs: a 2- to 6-orbital model, synthetic noisy bitstrings, and exact diagonalization. Method: compare raw SQD, recovered SQD, and single-excitation Ext-SQD. Output: deterministic error and subspace-size ledger. Success criterion: every energy change is traceable to a configuration operation. Stop condition: stop before hardware access if simulator behavior cannot match the exact reference. Safety boundary: public synthetic chemistry only.
2. `Forbidden-sample stress test`: Objective: measure whether the recovery pipeline remains stable at the paper's reported invalid-sample fractions. Inputs: valid samples plus controlled Hamming-weight corruption from 90% through 99%. Method: sweep corruption and random seeds while holding the Hamiltonian fixed. Output: recovery success, bias, variance, and failure thresholds. Success criterion: predeclared accuracy and stability bounds. Stop condition: stop when recovery becomes underdetermined. Safety boundary: no private device telemetry.
3. `Matched-cost comparator`: Objective: test Ext-SQD against HCI and CCSD under a fixed classical budget. Inputs: one open Hamiltonian, reproducible solver versions, and resource caps. Method: record wall time, memory, subspace size, and energy error. Output: a cost-error frontier. Success criterion: conclusions remain stable across repeated runs. Stop condition: stop if methods cannot be configured comparably. Safety boundary: no material-performance claim from a single electronic-structure benchmark.

## Example MVP Product

- `Product name`: SQD Audit Bench
- `Target user`: Quantum-computing and computational-chemistry review teams.
- `Problem`: Hybrid quantum-chemistry claims combine device samples, recovery, selected-CI expansion, and classical diagonalization, making it difficult to identify where accuracy and cost originate.
- `Core workflow`: Load a small Hamiltonian and sampled or synthetic bitstrings; validate symmetry sectors; run SQD and single-excitation Ext-SQD; compare against CASCI/HCI; export an evidence ledger.
- `Data requirements`: Open Hamiltonians, explicit electron/spin sectors, bitstrings, solver parameters, environment versions, and exact or high-confidence references.
- `Architecture`: Local Python CLI using PySCF and open SQD tooling, a deterministic configuration store, isolated solver adapters, and Markdown/JSON report generation.
- `Success metrics`: Exact replay determinism; energy error versus reference; recovered valid-sample rate; subspace dimension; peak memory; wall time; and percentage of claims with direct traces.
- `Risk controls`: Local-only processing, no credentials or provider tokens in reports, public/synthetic examples by default, license ledger, and explicit separation between electronic-energy estimates and battery performance.
- `Limitations`: The MVP does not reproduce IBM hardware noise, proprietary VASP geometry optimization, or production-scale materials discovery.
- `MVP boundary`: Small active spaces and auditability, not advantage claims.
- `Deployment model`: Local CLI/notebook.
- `Evaluation plan`: Golden small-space fixtures, corruption sweeps, matched-cost comparisons, and independent reviewer replay.
- `Failure modes`: Incorrect particle sectors, hidden solver defaults, unstable recovery, memory blow-up, or misleading comparison of variational and non-variational energies.
- `Maintenance plan`: Pin solver versions and refresh fixtures when SQD APIs or reference implementations change.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Scaling active spaces in simulations of surface reactions through sample-based quantum diagonalization | Primary paper and journal article | **Expanded in this pass:** full methods, figures/tables, hardware sampling, scale limits, declarations, and publication metadata were inspected. | https://arxiv.org/abs/2503.10923; https://doi.org/10.1038/s41598-026-58228-0 |
| Quantum computation of reactions on surfaces using local embedding | Methodological predecessor | **New in this pass:** the selected paper identifies this as the prior local-embedding and active-space workflow. | https://doi.org/10.1038/s41534-023-00753-1 |
| Chemistry Beyond Exact Solutions on a Quantum-Centric Supercomputer | SQD method neighbor | **New in this pass:** direct SQD lineage for configuration sampling, recovery, and quantum-selected diagonalization. | https://arxiv.org/abs/2405.05068 |
| Quantum-centric computation of molecular excited states with extended sample-based quantum diagonalization | Ext-SQD method neighbor | **New in this pass:** direct lineage for excitation-expanded SQD subspaces. | https://arxiv.org/abs/2411.00468 |
| Bridging physical intuition and hardware efficiency for correlated electronic states: the local unitary cluster Jastrow ansatz for electronic structure | State-preparation method | **New in this pass:** the LUCJ ansatz used to generate hardware samples. | https://doi.org/10.1039/D3SC02516K |
| Predicting model behavior before release by simulating deployment | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://openai.com/index/deployment-simulation/; https://cdn.openai.com/pdf/predicting-llm-safety-before-release-by-simulating-deployment.pdf |
| Introducing LifeSciBench | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://openai.com/index/introducing-life-sci-bench/ |
| Towards autonomous medical artificial intelligence agents | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://www.nature.com/articles/s41586-026-10675-5 |
| UltraQuant: 4-bit KV Caching for Context-Heavy Agents | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://arxiv.org/abs/2606.20474 |
| LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://arxiv.org/abs/2606.20529 |
| Habituation at the Gate | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://arxiv.org/abs/2606.22721 |
| SoK: Security and Privacy of Foundation-Model-Powered Robots | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://arxiv.org/abs/2606.16788 |
| Rethinking Shrinkage Bias in LLM FP4 Pretraining | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://arxiv.org/abs/2606.20381 |
| Evidence of scaling advantage on an NP-complete problem with enhanced quantum solvers | Prior DEP reading | Preserved from the earlier multi-source pass; not re-reviewed here. | https://doi.org/10.1038/s43588-026-01007-8 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338/README.md | Selected DEP identity, contents, source inventory, and attribution. | 2026-07-17 | Repository file inspected. |
| R2 | Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338/daily_research_findings_2026-06-24_2338.md | Original ten-finding synthesis and SQD paper discovery record. | 2026-07-17 | Repository generated artifact inspected. |
| R3 | Black-Lake-Data/.reports/BL-DEP-20260624-Tech Intel 2338-20260709/README.md | Prior processing scope and evidence limits. | 2026-07-17 | Older than the eligibility cutoff; inspected for iterative context. |
| R4 | Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338/BL-DEP-Mark001 Report-Mark.md | Exact prior related-reading and source-reference sections. | 2026-07-17 | Older than the eligibility cutoff; inspected. |
| R5 | Black-Lake/.logs/20260709-DEP-20260624-Tech Intel 2338-LOG.md | Prior questions, challenges, selection record, and expansion recommendation. | 2026-07-17 | Older than the eligibility cutoff; inspected. |
| R6 | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md | Prior baseline manuscript and ten-item expansion pool. | 2026-07-17 | Full manuscript inspected. |
| R7 | https://arxiv.org/abs/2503.10923 | Canonical title, authors, v2 date, abstract claims, extent, license link, and journal DOI. | 2026-07-17 | Primary canonical record. |
| R8 | https://arxiv.org/html/2503.10923 | Full methods, figures/tables, results, discussion, limitations, dependencies, and reference lineage. | 2026-07-17 | Primary full text inspected; renderer omits some symbols and fields. |
| R9 | https://doi.org/10.1038/s41598-026-58228-0 | Peer-reviewed publication, authorship, dates, abstract, CC BY 4.0 license, and early-access status. | 2026-07-17 | Publisher page inspected. |
| R10 | https://doi.org/10.1038/s41534-023-00753-1 | Local-embedding predecessor identified by the selected paper. | 2026-07-17 | Discovery source; full text not independently reviewed. **New in this pass.** |
| R11 | https://arxiv.org/abs/2405.05068 | SQD method neighbor identified by the selected paper. | 2026-07-17 | Discovery source; full text not independently reviewed. **New in this pass.** |
| R12 | https://arxiv.org/abs/2411.00468 | Ext-SQD method neighbor identified by the selected paper. | 2026-07-17 | Discovery source; full text not independently reviewed. **New in this pass.** |
| R13 | https://doi.org/10.1039/D3SC02516K | LUCJ state-preparation method identified by the selected paper. | 2026-07-17 | Discovery source; full text not independently reviewed. **New in this pass.** |
| R14 | Black-Lake/README.md | DEP-E placement, README, log, commit, and public-source rules. | 2026-07-17 | Live repository authority inspected after fetch. |
| R15 | Black-Lake/.lake-data/README.md | DEP class and publication-index maintenance rules. | 2026-07-17 | Live repository authority inspected after fetch. |
| R16 | Black-Lake-Data/README.md | Source DEP, report, and attribution expectations. | 2026-07-17 | Live repository authority inspected after clone. |

## Appendix

### Automation Selection Record

- Automation family: `Black-Lake Data Processing & Review`; `Black-Lake Data Processing & Review 0900`.
- Run timestamp: 2026-07-17T00:02:46Z.
- Eligibility cutoff: 2026-07-16T00:02:46Z.
- Canonical candidates: 57.
- Excluded within 24 hours: 2.
- Eligible candidates: 55.
- Excluded DEPs: `DEP-20260708-Tech Intel 0104` and `DEP-20260712-Tech Intel 1100`.
- Random DEP draw: PowerShell `Get-Random` over sorted eligible canonical DEP directory names selected `DEP-20260624-Tech Intel 2338`.
- Prior same-family material: 2026-07-09 report, Report-Mark, log, and DEP-E manuscript; all older than the cutoff.
- Expansion pool: ten items preserved in the prior manuscript's `Related Research and Reading` section.
- Random expansion draw: PowerShell `Get-Random` selected `arXiv:2503.10923`; canonical and full-text primary sources were accessible, so no redraw was needed.

### Replication Checklist

- Pin Hamiltonian, geometry, basis, pseudopotentials, functional, k-point choice, active-space rule, and electron/spin sector.
- Start with a small system that supports CASCI or exact diagonalization.
- Preserve raw and recovered bitstrings separately.
- Record circuit mapping, gate counts, depth, samples, calibration, and random seeds.
- Record SQD recovery iterations, batch sizes, discarded amplitudes, excitation order, and subspace dimensions.
- Compare accuracy and cost against matched HCI and CCSD settings.
- Report uncertainty, failures, and differences between simulator and hardware runs.

### Source Collection Notes

No external paper PDF, source archive, code repository, dataset, quantum-hardware output, or calibration file was collected or deposited. Public URLs and repository-relative provenance are preserved.
