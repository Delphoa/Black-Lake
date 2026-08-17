# HiKonv as Packed Convolution Arithmetic

## a whitepaper-grade archival intake review of DEP-E-20260817-HiKonv Maximizing the

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260817-HiKonv Maximizing the`
**Source commit:** `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`
**Paired task indicator:** `BL-DEPPAIR-20260818-9040FC87`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-08-18
**Review scope:** complete tracked repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is the complete DEP-E record centered on Chen et al., HiKonv: Maximizing the Throughput of Quantized Convolution With Novel Bit-wise Management and Computation (arXiv:2208.00763), plus the complete 14-page canonical paper. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

HiKonv treats a full-width multiplication as a container for many aligned low-bit convolution products, using spacing, ordering, sign correction, and carry management to make the packed result separable. CPU and FPGA evaluations support meaningful layer and model speedups, but overflow bounds, packing overhead, architecture-specific instruction behavior, and inherited quantization accuracy define the real applicability envelope.

The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- HiKonv treats a full-width multiplication as a container for many aligned low-bit convolution products, using spacing, ordering, sign correction, and carry management to make the packed result separable. CPU and FPGA evaluations support meaningful layer and model speedups, but overflow bounds, packing overhead, architecture-specific instruction behavior, and inherited quantization accuracy define the real applicability envelope.
- Low-bit feature and weight sequences are packed into separated slices of two full-width operands. One multiplication creates a structured superposition of partial products whose slice positions encode convolution offsets.
- A spacing parameter reserves enough bits to prevent unwanted overlap. Slice ordering makes vertical partial-product accumulation correspond to convolution sums; equations derive supported sequence lengths from multiplier and operand widths.
- Signed inputs require two's-complement correction and increment/decrement logic. Multi-iteration convolutions combine shifted prior partial results with new products, so the method is more than naive SIMD packing.

### Principal qualifications

1. Packed arithmetic is exact only when slice spacing, accumulation length, sign handling, and carry bounds are correct for every layer.
2. Packing, extraction, shifts, and correction consume instructions or FPGA logic; headline multiplication density is not end-to-end throughput.
3. Results depend on specific CPU multipliers, compiler behavior, ARM/x86 paths, FPGA DSP geometry, and quantized layer shapes.
4. The study accelerates already-quantized models; it does not establish that a target model retains acceptable accuracy at the chosen bit-widths.

## 1. Problem framing and research question

Low-bit convolution often widens operands to a processor's native multiplier width, wasting arithmetic lanes. The paper asks how many convolution multiply-accumulates can be encoded into one existing CPU multiply or FPGA DSP operation without changing the hardware multiplier itself.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

Low-bit feature and weight sequences are packed into separated slices of two full-width operands. One multiplication creates a structured superposition of partial products whose slice positions encode convolution offsets.

### 2.2 Stage 2

A spacing parameter reserves enough bits to prevent unwanted overlap. Slice ordering makes vertical partial-product accumulation correspond to convolution sums; equations derive supported sequence lengths from multiplier and operand widths.

### 2.3 Stage 3

Signed inputs require two's-complement correction and increment/decrement logic. Multi-iteration convolutions combine shifted prior partial results with new products, so the method is more than naive SIMD packing.

### 2.4 Stage 4

CPU implementations use native integer multipliers and shifts; FPGA designs wrap DSP multipliers with packing, split/increment, and output registers. Weight compression and runtime feature extraction reduce storage while preserving throughput under the assumed logic budget.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `hikonv_maximizing_the_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

HiKonv is an arithmetic serialization format: independent low-bit convolutions are encoded into the bit lanes of one multiplication and decoded afterward. The format is valid only under a carry-isolation contract. This view suggests verifying every packed kernel with property tests over worst-case signed values before measuring speed.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The paper reports up to 7.6x speedup for 1-D convolution and 2.74x and 3.19x for 4-bit signed and unsigned 2-D convolution over its CPU baselines.

### 7.2 Evidence unit 2

For a 4-bit Ultranet model, reported end-to-end latency improves by up to 2.4x on x86-64 and 2.03x on ARM. Layer gains do not translate uniformly because non-convolution work and packing reduce the realizable model-level fraction.

### 7.3 Evidence unit 3

On FPGA, a single DSP processes multiple low-bit convolution operations that would conventionally require several DSPs; the reported model implementation outperforms the compared state of the art by 2.37x in latency.

### 7.4 Evidence unit 4

Theoretical examples claim one 32-bit CPU multiplier can encode 128 binary, thirteen 4-bit, or five 8-bit convolution operations, while one 27x18 DSP can encode 60, eight, or two. These capacities require the derived no-overlap and correction conditions.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| One native multiplier can compute several exact low-bit convolution terms in parallel. | The paper derives packing/correction equations and validates CPU and FPGA implementations. | Supported within the stated bit-width, length, and overflow bounds. |
| HiKonv improves complete-model latency on CPU and FPGA. | Ultranet and FPGA evaluations report roughly twofold or greater improvements. | Supported for the reported platforms and model; not a universal processor claim. |
| Nominal packed operation count equals realized application speedup. | End-to-end gains are smaller than peak packed arithmetic density and vary by layer/platform. | Rejected. |
| This intake reproduced HiKonv. | No kernel, compiler, CPU, FPGA, quantized model, or timing test was run. | Rejected. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2208.00763](https://arxiv.org/abs/2208.00763) — Canonical arXiv identity and version record.
- [https://arxiv.org/pdf/2208.00763](https://arxiv.org/pdf/2208.00763) — Complete canonical paper inspected page by page; no source document uploaded.
- [https://doi.org/10.48550/arXiv.2208.00763](https://doi.org/10.48550/arXiv.2208.00763) — Persistent primary-source identifier.

### Associated DEP records

- No associated DEP record was asserted beyond relationships verified in the selected source.

External context is used to verify identity, locate complete evidence, and clarify version or implementation status. It is not added to inflate the selected source's evidentiary weight. A related paper, code repository, or DEP can make a mechanism easier to understand without independently reproducing the result.


## 11. Research notes and critical considerations

The first audit obligation is identity. A durable review binds every conclusion to an immutable repository source state and to stable public source locators. Titles and short names are insufficient because papers change versions, code changes behavior, and composite records can be corrected without changing their topic. The source commit and paired task indicator are therefore evidence, not administrative decoration.

The second obligation is denominator integrity. Every reported metric needs its unit of analysis, included and excluded cases, aggregation rule, configuration-selection process, and failure policy. A result conditioned on successful parsing, feasible compilation, completed generation, or selected checkpoints describes that conditional population. It must not be silently presented as end-to-end performance.

The third obligation is coordinate matching. Model revision, data split, preprocessing, random seed, prompt, judge, optimizer, hardware, budget, and stopping rule define the coordinates of an empirical claim. Comparisons made in different coordinates may still be informative, but they are not controlled evidence of one component's causal contribution. This intake uses calibrated phrases such as “paper reports,” “DEP-E reports,” and “supported under tested conditions” to keep that distinction visible.

The fourth obligation is negative evidence. Missing code, absent seeds, unreconciled tables, ambiguous operators, unavailable raw traces, and lack of external validation are findings. They do not prove a method is wrong, but they limit the strength and reuse of its claims. A public archival artifact should preserve those limits rather than optimize for a favorable narrative.

Finally, reproducibility is a ladder: an artifact can be available, inspectable, runnable, result-reproducing, and independently replicated. This review establishes inspectability for the selected DEP-E and directly checked public evidence. It does not claim execution or reproduction. The experiments were not independently rerun or reproduced.

## 12. Potential implications and failure modes

For research intake, the practical unit should be a claim-evidence-condition tuple. A headline claim without its metric, denominator, and tested envelope is too weak for downstream automation. A condition without immutable source identity is too unstable for audit. The derived DEP-A therefore treats provenance, mechanism, evidence, and limitations as linked records.

For implementation, stage boundaries should be observable. Inputs, transformations, selected policies, outputs, validator results, and failures should be recorded without exposing sensitive data in public summaries. If a learned judge or heuristic influences data selection, its identity and disagreement should be logged separately from the target system's result.

For governance, high-impact uses need independent domain review. Passing a source-integrity validator or reproducing a benchmark does not certify security, clinical safety, legal compliance, fairness, privacy, or production readiness. The methodology provides auditability, observability, and traceable lineage only.

Common failure modes include distribution shift, silent exclusion of hard cases, leakage across splits, selection on the evaluation set, metric gaming, stale calibration, correlated evaluators, uncounted preprocessing cost, and deployment hardware that changes the resource tradeoff. Each requires an explicit falsifier and stop condition.


## 13. Falsifiable hypotheses

The following are reviewer inferences and proposals, not findings of the source:

### Hypothesis 1

**Proposition:** Property-based worst-case tests will find signed carry-bound defects earlier than random numerical comparisons in new HiKonv kernel ports.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Realized speedup will be predicted by the fraction of time in packable convolution plus packing/extraction cost, not by theoretical operations per multiply.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Auto-tuning slice spacing and packed sequence length per layer will improve end-to-end latency over a fixed global packing configuration.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

## 14. Deployment and governance considerations

Appropriate use begins with bounded offline research, explicit data rights, immutable configuration, and human approval. High-stakes or production uses require domain-specific validation, threat modeling, access control, privacy review, monitoring, rollback, and incident handling outside the scope of this archival intake.

Every promotion decision should retain raw metric components, slice outcomes, exclusions, uncertainty, and cost. Composite scores may summarize but must not hide a failed safety, quality, fairness, or resource floor. A learned evaluator should never be the sole authority for the system it trained or selected.

Public artifacts should contain stable source locators and public-safe evidence only. Private source files, caches, credentials, execution traces, user data, and machine-specific paths remain outside the repository. Corrections append new provenance rather than silently rewriting prior evidence.

## 15. Replication and falsification agenda

1. **Identity gate.** Pin paper version, code commit, dataset revision, model/checkpoint, prompts, preprocessing, dependency lock, hardware, and evaluation policy. Verify licenses separately for each artifact.
2. **Source conformance.** Reconstruct every equation, table definition, exclusion rule, and configuration from complete primary evidence. Unit-test ambiguous thresholds, operators, and sign conventions before running expensive work.
3. **Baseline reproduction.** Reproduce baseline outputs first. A proposed-method result is uninterpretable if the local baseline does not match the reported operating range.
4. **Matched comparison.** Equalize data access, tuning/search budget, compute, preprocessing, failure handling, and metric code. Preserve per-case outputs and selection logs.
5. **Uncertainty.** Use repeated seeds, patient/group-aware folds, or repeated scenarios as appropriate. Report intervals and effect distributions, not only selected point estimates.
6. **Negative controls.** Shuffle, invert, or remove the proposed signal while matching capacity. Test whether the named mechanism, rather than extra parameters or search, explains the result.
7. **Shift tests.** Evaluate neighboring models, datasets, devices, workloads, and temporal states. Declare the envelope in which calibration or configuration is valid.
8. **Failure accounting.** Count refusals, parse failures, infeasible cases, timeouts, out-of-memory states, and discarded samples. Report conditional and end-to-end metrics separately.
9. **Operational measurement.** Include preprocessing, calibration, service calls, data generation, storage, communication, synchronization, and retries in cost claims.
10. **Independent review.** Separate the team or evaluator that constructs evidence from the authority that approves deployment. Archive the final evidence card and stop decision.

The agenda is successful if it can disconfirm the mechanism. A rerun that reproduces only a headline average is insufficient when the causal signal, denominator, or resource boundary remains untested.

## 16. Durable restatement

> HiKonv treats a full-width multiplication as a container for many aligned low-bit convolution products, using spacing, ordering, sign correction, and carry management to make the packed result separable. CPU and FPGA evaluations support meaningful layer and model speedups, but overflow bounds, packing overhead, architecture-specific instruction behavior, and inherited quantization accuracy define the real applicability envelope.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | complete manifest and attribution boundary | read from beginning to end; every heading, table row, claim, limitation, proposal, URL, related-record reference, and attribution entry accounted for |
| `hikonv_maximizing_the_manuscript.md` | complete substantive DEP-E artifact with 2182 words | read from beginning to end; every heading, table row, claim, limitation, proposal, URL, related-record reference, and attribution entry accounted for |
| `arXiv:2208.00763 complete canonical PDF` | HiKonv: Maximizing the Throughput of Quantized Convolution With Novel Bit-wise Management and Computation; 14 pages and 12412 extracted words | PDF header and terminal marker passed; every page inspected; complete body, equations, tables, figures, limitations, appendices where present, acknowledgments, and references accounted for; no experiment or code rerun |
| `canonical PDF page 1` | 931 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 2` | 973 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 3` | 800 extracted words; labels: Figure 1 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 4` | 963 extracted words; labels: Figure 2 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 5` | 665 extracted words; labels: Figure 2, Figure 3 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 6` | 799 extracted words; labels: Figure 3 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 7` | 719 extracted words; labels: Figure 4, Figure 4a, Figure 4b | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 8` | 1022 extracted words; labels: Figure 2, Figure 5 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 9` | 897 extracted words; labels: Figure 5, Figure 6, Figure 8 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 10` | 880 extracted words; labels: Figure 7, Figure 8, Figure 9, Figure 10 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 11` | 658 extracted words; labels: Figure 10, Figure 11, Figure 11a, Figure 11b, Figure 12, Figure 13, Figure 13a, Figure 13b | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 12` | 857 extracted words; labels: Figure 14, Table I, Table II | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 13` | 1081 extracted words; labels: Table I, Table II, Table III | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 14` | 1167 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `Figure 1 provides the opportunity to simply segment out the` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 10: FPGA HiKonv 2-D convolution.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 11: Speedup for different bitwidth.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 12: Evaluation with 4-bit layers on X86 64 CPUs.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 13: Evaluation with 4-bit layers on ARM.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 14: 4-bit Ultranet full model evaluation.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 1: INT4 optimization on DSP48E2 [19].` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 2 is for the case where all elements of the sequences` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 2, the output of one block depends on the mul-` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 2: Binary view of the ideal process of P rod= A × B.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 3: Computation of FXN,K 1-D convolution.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 4 shows two examples of multipliers with different` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 4: Throughput of processing units with different` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 5: A numerical example of a F3,2 1-D convolution.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 6: Input packing for signed integer f sequence.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 7: Weight compression.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 8: Micro-architecture of a single DSP convolver.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 9: FPGA HiKonv 1-D convolution output processing.` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `central equations and algorithms` | 30 equation-number candidates plus all displayed/inline mathematical definitions | variables, signs, objectives, constraints, and guarantee boundaries reconstructed; extraction ambiguity preserved rather than guessed |
| `appendix, references, disclosures, and final page` | appendix detected: True; references detected: True | supplementary settings, failure examples, source lineage, acknowledgments, and end-of-document integrity checked |
| `private evidence-layer map` | source DEP-E report; directly inspected primary evidence; reviewer inference; hypothesis/proposal | all public claims assigned to one evidence layer; no reproduction or source-copy claim |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260818-9040FC87` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260817-HiKonv%20Maximizing%20the
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff
[^primary-one]: Primary public source: https://arxiv.org/abs/2208.00763
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2208.00763
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
