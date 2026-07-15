# Constraint-Gated Workflow Synthesis

## A whitepaper-grade archival intake review of the ComfyUI-R1 DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260714-ComfyUI R1`  
**Source commit:** `398f692812550135476e8d560be1d2a01fa2982e`  
**Paired task indicator:** `BL-DEPPAIR-20260715-80239D97`  
**Direction:** `DEP-E -> DEP-A`  
**Review date:** 2026-07-15  
**Review scope:** complete two-file repository record, canonical arXiv v1 and publication context, method and evidence reconstruction, claim vetting, implementation status, re-conceptualization, and replication planning  
**Provenance boundary:** review-only source action; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes  
**Reproduction boundary:** no training, workflow execution, repository code execution, or benchmark reproduction was performed.

---

## Executive assessment

The selected DEP-E is a complete public-safe research package with a README and a detailed manuscript on ComfyUI-R1. Both tracked files were read from beginning to end. The package inventories its contents, distinguishes arXiv v1 from a later ACL Findings record, reports the knowledge-base pipeline, SFT and GRPO stages, hybrid reward, experiments, limitations, current implementation surface, related Black Lake records, and source-locality policy. It does not contain source documents or a `.source` directory.

ComfyUI-R1’s central contribution is a useful pattern for agentic generation: permit a model to propose a structured artifact, but place deterministic validity gates ahead of graded similarity rewards. The model emits a compact code-like workflow representation. Format tags, DAG validity, node allowlisting, and consistency between selected nodes and emitted workflow nodes can veto the reward. Only outputs that survive those gates receive a graded node-selection signal. This separation between probabilistic planning and deterministic structural checks is more durable than the paper’s “R1” branding.

The evidence is favorable inside the paper’s setting. On a 200-workflow held-out set with pre-retrieved candidate nodes, the full model reports 0.97 format validity, 0.62 node F1, and 0.51 graph F1. The SFT-only code variant reports 0.95, 0.60, and 0.48; the SFT-only JSON variant reports 0.92, 0.57, and 0.45. On ComfyBench, where retrieval is added, the paper reports a 0.67 execution pass rate versus 0.56 for GPT-4o plus ComfyAgent.[^paper] These are author-reported results. They do not establish semantic quality, safety, licensing, or robustness to a changing plugin ecosystem.

The canonical arXiv article, the later ACL publication record, and the current ComfyUI-Copilot repository were inspected directly.[^record][^acl][^code] The ACL record confirms publication in Findings of ACL 2026 and adds a generalization claim in its abstract. This review keeps that context separate from the v1 tables. The current integration repository shows an active product surface but is not a pinned, self-contained reproduction bundle for the paper’s model, curated knowledge bases, prompts, checkpoints, and evaluation outputs.

Bottom line: the DEP-E record merits archival intake as a technically strong, evidence-calibrated review. The method demonstrates constrained workflow synthesis under a narrow benchmark. Its most valuable future test is not another overlap table; it is whether the gating pattern continues to reject unsafe or invalid graphs while accepting diverse, semantically correct alternatives under version shift.

### Principal strengths

- A reversible JSON-to-code representation makes graph structure easier to inspect and validate.
- Hard format, DAG, and node-fidelity checks prevent a positive reward for structurally invalid outputs.
- The paper reports node- and graph-level measures, representation and training-stage ablations, and an end-to-end execution benchmark.
- The source DEP clearly separates paper evidence, later publication metadata, current repository state, and reviewer inference.
- Security, plugin trust, dataset lineage, secret exposure, and sandboxing are treated as deployment concerns rather than inferred successes.

### Principal qualifications

1. The main evaluation provides candidate nodes, so it tests reasoning over retrieved context more than open-world retrieval.
2. The curated workflows, generated rationales, and node documentation have incomplete public provenance and licensing evidence.
3. One reference graph can penalize valid alternatives and reward reference imitation.
4. Execution pass rate does not measure user intent, image quality, resource safety, privacy, or plugin trust.
5. The public integration surface is inspectable but does not prove exact reproduction of the reported tables.

---

## 1. The problem and research question

ComfyUI represents generative media pipelines as directed graphs of nodes. This exposes compositional power, but users must choose compatible nodes, satisfy typed connections, order execution, configure models, and manage a fast-changing ecosystem. An LLM that emits raw JSON can hallucinate components, produce malformed edges, or generate a graph that parses but does not do what the user asked. Multi-agent decomposition can add coordination error.

The research question is whether domain post-training and explicit reasoning can generate better workflows than prompting strong closed models, and whether rule-based structural feedback can improve that reasoning without executing every candidate during training. The authors construct node and workflow knowledge bases, transform workflows into a code-like representation, generate long reasoning traces for SFT, and then use GRPO with a hybrid reward.

This problem is a special case of structured program synthesis under a changing vocabulary. The output must satisfy syntax, graph, component, version, and semantic constraints. ComfyUI-R1 directly handles only a subset: expected format, DAG structure, candidate-node membership, node-set consistency, and reference-node overlap. Parameter validity, type compatibility, model availability, resource budgets, plugin permissions, and semantic output quality are not all encoded in the reported reward.

---

## 2. Technical reconstruction

### 2.1 Knowledge bases and representation

The node pipeline reportedly begins with about 40,000 nodes and retains 7,238 after exact deduplication and removal of entries lacking input/output parameters. Where structured documentation is absent, Claude 3.5 generates standardized descriptions from repositories. The workflow pipeline begins with about 27,000 community workflows and retains 3,917 after validity filtering, exact deduplication, reversible conversion, irrelevant-data removal, and exclusion of nodes outside the node knowledge base. The average retained workflow has 21 nodes.

Each retained workflow is represented as original JSON, topologically ordered function-call-like code, and a natural-language description. The representation is reversible: a parser maps JSON to ordered calls and back. This provides a structured intermediate language aligned with a code-pretrained backbone while retaining import compatibility. The paper’s ablation modestly favors code over JSON, but does not isolate whether token length, ordering, training familiarity, or parser regularity causes the gain.

### 2.2 Supervised fine-tuning

The backbone is Qwen2.5-Coder-7B-Instruct. For every reference workflow, the candidate set includes all reference nodes and random distractors equal to 80% of the reference-node count. Qwen-Max, Claude 3.5, and GPT-4o generate instructions and workflow-design rationales. Of 3,917 workflows, 3,717 support training and 200 testing, yielding 11,140 training samples and 600 test samples. The model learns to emit selected nodes, a design rationale, and code-form workflow output.

This construction creates several dependencies. Synthetic instructions and rationales inherit closed-model preferences. Random distractors may be easier than realistic near-neighbor nodes. A workflow-level split does not automatically prevent node, package, template, or source-site leakage. The paper does not supply a complete lineage and contamination audit.

### 2.3 Reward and GRPO

The reward has four parts. Format validation checks required blocks. Structure validation checks that parsed code is a DAG. Node fidelity rejects nodes outside the candidate set and rejects disagreement between the explicit selection block and the nodes actually used. Node-selection accuracy rewards overlap with the reference node set. The combined reward is veto-based: a failure in format, structure, or fidelity makes the total negative; otherwise overlap supplies the graded signal.

GRPO samples four outputs per input, normalizes rewards within the group, clips the policy ratio at 0.2, and uses a KL coefficient of 0.001. SFT runs for one epoch on eight 80 GB A100 GPUs at learning rate 1e-5 with per-GPU batch size one. RL uses the same GPU count for 300 steps, learning rate 1e-6, and total batch size 64. Training and inference allow up to 32,768 tokens.

The equations define an optimization surrogate, not a guarantee of correct workflow behavior. A graph may pass every gate while calling an unsafe custom node, using wrong parameters, leaking data, exhausting memory, or producing irrelevant media. Conversely, a safe and useful graph with a different node set can receive a lower score.

---

## 3. Source inventory and integrity assessment

The source directory contains exactly `README.md` and `comfyui_r1_manuscript.md`. The README supplies tags, context, complete inventory, item summaries, relevance, source-withholding policy, primary locators, repository standards, related records, and final Attribution Block. The manuscript contains metadata, a nine-item evidence ledger, technical and quantitative synthesis, methodology, constraints, observations, improvements, four implementations, three exercises, an MVP, related reading, references, selection and integrity notes, and a replication checklist.

`git ls-files` confirms both files at the source commit. No source document, image, workflow, checkpoint, model, cache, validation output, or local path is present. The README’s inventory matches the directory. The manuscript uses arXiv v1 for empirical evidence and treats the later ACL record as separate context. It explicitly states that code was inspected but not executed.

Direct inspection verified the arXiv title, eight authors, v1 date, work-in-progress comment, subject categories, full-paper links, and CC BY 4.0 locator. The complete HTML contains introduction, related work, knowledge-base construction, SFT, reward definitions, GRPO, experiments, three result tables, case studies, conclusion, and references. The ACL Anthology record confirms Findings 2026, pages 2999–3013, and DOI `10.18653/v1/2026.findings-acl.146`.[^acl] The current ComfyUI-Copilot repository was available, but no end-to-end reproduction was attempted.

The DEP-E reports prior local integrity checks for the PDF, HTML, and source archive. Those bytes are outside this checkout; the present review treats their checks as repository-reported process evidence. The complete canonical HTML was directly inspected, so the source is not abstract-only.

---

## 4. Architecture and operational pipeline

The full pipeline is data collection, filtering, reversible representation, synthetic instruction/rationale generation, SFT, reward-gated GRPO, and evaluation. At inference, the main test supplies an instruction and candidate nodes. The model reasons, selects nodes, and emits code. A parser recovers a graph for metric calculation or execution.

The ComfyBench variant adds retrieval: it uses `text-embedding-3-small` to retrieve the top three similar workflows, unions their nodes, and passes that set to the generator. This creates a two-stage error surface. Retrieval can omit necessary nodes or introduce distractors; generation can misuse the candidate set. Reporting only final pass rate hides which stage failed.

For production, at least four more gates are needed. A schema/type gate should validate ports and parameter ranges. A trust gate should verify node identity, version, signature, permissions, and origin. A resource gate should estimate model downloads, memory, disk, runtime, and network behavior. A semantic gate should evaluate instruction satisfaction and output policy. None should automatically execute untrusted plugins.

---

## 5. Independent re-conceptualization

### 5.1 Proposal–verifier workflow synthesis

Reviewer inference: ComfyUI-R1 is a proposal–verifier system. The language model proposes a plan and program; deterministic checks verify a subset of structural invariants; a softer metric grades similarity among survivors. The mechanism is portable to infrastructure templates, data pipelines, agent plans, and API workflows.

The analogy breaks because the verifier is incomplete. Passing it is not semantic correctness or safety. It is a minimum structural certificate. The system should never label a passing workflow “safe” without additional policy and runtime evidence.

### 5.2 Learned planning over a frozen action catalog

The candidate node set is an action catalog. Restricting actions reduces hallucination and makes membership checks possible. This resembles constrained planning more than open-ended code generation. It predicts that performance will depend heavily on candidate recall and catalog freshness. Time-split evaluation against newly introduced, renamed, deprecated, or malicious nodes would directly test this claim.

### 5.3 Transferable principle

The durable design principle is **hard gates before soft preference**. Invalid structure should not receive positive reward because it resembles a reference. Yet hard gates must be independently tested for false rejection and incomplete coverage. The system needs an explicit unknown state when the verifier cannot decide.

---

## 6. Experimental design and evidence reconstructed

The main test contains 200 held-out workflows and 600 samples. Inputs include pre-retrieved candidate nodes. Metrics are format validity plus node- and graph-level precision, recall, and F1. Graph matching follows the WorFEval family using longest-chain and maximum-common-induced-subgraph logic. Baselines include few-shot and chain-of-thought prompting for Qwen2.5-Coder, Qwen-Max, GPT-4o, Claude 3.5, Claude 3.7, and a GPT-4o ComfyAgent implementation.

This is a meaningful model-and-representation test but a limited end-to-end system test. Candidate retrieval is mostly factored out. The small test set comes from the same curation process as training. There is no reported confidence interval, repeated training seed, human semantic evaluation, plugin-version time split, adversarial node-description test, or data-lineage audit.

The ablation compares SFT+GRPO, SFT-only code, and SFT-only JSON. It identifies a small RL increment and a small representation increment. It does not ablate individual reward gates, distractor hardness, reasoning length, synthetic rationales, node-document generation, or group size. The end-to-end ComfyBench experiment provides retrieval plus execution, but reported GPT-4o numbers are taken from the baseline paper rather than necessarily rerun under identical infrastructure.

---

## 7. Results and quantitative audit

The principal table reports the full model at 0.97 format validity, node precision 0.67, recall 0.58, F1 0.62, graph precision 0.52, recall 0.51, and F1 0.51. Claude 3.5 CoT also reaches 0.97 format validity but reports node F1 0.57 and graph F1 0.38. Prompted Qwen2.5-Coder CoT reports 0.41, 0.22, and 0.10 for format, node F1, and graph F1.

The ablation reports SFT-only code at 0.95/0.60/0.48 and SFT-only JSON at 0.92/0.57/0.45. Relative to SFT-only code, GRPO adds 0.02 format validity, 0.02 node F1, and 0.03 graph F1. Domain SFT accounts for far more of the gap from the raw backbone. Claims that RL is essential should therefore be calibrated: it improves the reported setting, but the major adaptation occurs earlier.

ComfyBench reports pass rates of 0.23 for GPT-4o few-shot, 0.28 for GPT-4o CoT, 0.52 for GPT-4o RAG, 0.56 for GPT-4o plus ComfyAgent, and 0.67 for ComfyUI-R1. The 0.11 absolute difference is clear as reported. Hardware, plugin versions, service configuration, retry behavior, and denominator details should be pinned before treating it as a universal execution advantage.

No result establishes visual quality, alternative-graph acceptance, node trust, safe external calls, parameter correctness, or long-term maintenance. The assessment is **supported under tested conditions for structural overlap and execution pass rate; unresolved for semantic and operational quality**.

---

## 8. Ablations and causal evidence

The available ablations support two narrow conclusions. Code representation modestly outperforms JSON in the SFT-only setting. Adding GRPO modestly improves an already strong SFT model. They do not show which reward component matters. A reward gate could be redundant, overly strict, or exploitable.

The necessary next ablation removes or perturbs one gate at a time while measuring invalid outputs, false rejects, alternative valid solutions, and semantic task success. Another should compare exact node-set overlap with multi-reference, execution-grounded, and property-based rewards. Repeated seeds are needed because a two- or three-point F1 change may fall within training or sampling variance.

Reasoning length is also untested as a causal factor. A 32k token ceiling permits expensive traces but does not prove they are required. Compare concise plans, hidden-state planning, and long visible reasoning under equal latency and output quality. This is especially important for privacy and cost.

---

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| ComfyUI-R1 combines CoT SFT with GRPO and a hybrid reward. | Complete method and equations. | Strongly supported as method description. | Code execution and table reproduction were not performed. |
| The full model reaches 97% format validity, 0.62 node F1, and 0.51 graph F1. | Table 1 in arXiv v1. | Strongly supported as author-reported values. | 200-workflow set, candidate nodes supplied, no intervals. |
| Code is better than JSON for workflow generation. | SFT ablation favors code by 0.03 node and graph F1. | Supported under one tested representation pair. | Tokenization, ordering, and parser effects are not isolated. |
| GRPO materially improves reasoning. | Full model modestly exceeds SFT-only. | Promising but limited. | No seed variance or reward-component ablation. |
| ComfyUI-R1 beats ComfyAgent end to end by 0.11 pass rate. | ComfyBench Table 3. | Supported as reported. | Baseline numbers are sourced; runtime parity and versions are unclear. |
| A valid DAG is a safe workflow. | No safety evaluation establishes this. | Not established. | Valid graphs can invoke malicious or costly nodes. |
| The system generalizes to new nodes. | Later ACL abstract asserts this; v1 tables do not directly test it. | Unresolved for this review’s v1 evidence. | Requires a versioned time-split and full later-paper comparison. |
| Public artifacts are sufficient for exact reproduction. | Integration repository and paper links exist. | Not established. | Pinned KB, checkpoint, prompts, environment, and expected outputs remain incomplete. |

---

## 10. External primary-source context

The arXiv record pins v1 and labels it work in progress.[^record] The ACL Anthology later lists the paper in Findings of ACL 2026 with authoritative PDF, checklist, pages, and DOI.[^acl] The later abstract changes some framing, including generalization to newly introduced nodes. That claim should be evaluated from the later complete paper, not retroactively attached to v1’s tables.

The paper-linked repository now resolves to `ATH-MaaS/ComfyUI-Copilot`, an AI assistance integration for ComfyUI.[^code] Repository availability is useful, but product integration and scientific reproduction are distinct. A user-facing tool may call APIs or offer workflow features without exposing the model weights, data curation, training pipeline, or exact benchmark environment.

The DEP-E relates ComfyUI-R1 to ConMax, Structure Aware Systems, and SAILFISH. The connections are conceptually useful: reward-shaped reasoning, explicit deterministic/probabilistic boundaries, and broad graph discovery followed by precise checks. None independently reproduces this paper.

---

## 11. Research notes and critical considerations

The dataset is part of the method. Community workflows, generated documentation, synthetic instructions, and rationales may carry licensing, privacy, content-safety, and provenance issues. A versioned knowledge-base card should record source, license, opt-out, removal, transformation, hash, node version, and documentation confidence.

The candidate-set construction may be unrealistically easy. Random distractors equal to 80% of the reference count may not resemble the hard choices users face: multiple samplers, schedulers, loaders, adapters, and deprecated variants with similar names. Retrieval errors can dominate generation quality in production.

The reward prefers one reference node set. Valid workflows form an equivalence class. Different graphs may use alternative nodes, fuse stages, or satisfy the same output predicate more efficiently. Multi-reference and execution/property evaluation should supplement overlap.

Long reasoning traces raise privacy and security issues if they include user prompts, local paths, model names, or secrets. A production system should emit concise explanations and retain sensitive internal traces only under explicit policy. Plugin descriptions and workflow examples are untrusted input and can contain prompt injection.

Execution requires a separate security model: no automatic plugin installation, signed manifests, permissions, egress controls, secret isolation, timeouts, quotas, filesystem boundaries, and human approval. Passing a paper reward is not authorization to execute.

---

## 12. Potential implications

Scientifically, the paper demonstrates that domain-specific structure and validators can outperform generic prompting on a constrained artifact-generation task. The result supports research on verifier-guided agents, but not the claim that longer reasoning alone causes the improvement.

For agent systems, the key pattern is staged assurance: retrieve an allowlisted action set, propose a plan, compile to an intermediate representation, validate invariants, and only then consider sandboxed execution. Stage-specific metrics localize failure.

For product design, a safe near-term use is an offline drafting and inspection copilot. The user should see required nodes, permissions, compatibility, estimated resources, and unresolved issues before export. Automatic installation and execution should remain out of scope.

For governance, dataset and plugin provenance must be as reviewable as model output. An unsafe node can make a perfect graph harmful. Release evidence should report trust coverage, unknown-node rate, false rejection, semantic success, resource violations, and safety incidents alongside F1.

---

## 13. Falsifiable hypotheses

### Hypothesis 1: hard gates drive reliability more than long reasoning

**Proposition:** Deterministic graph and vocabulary gates account for more invalid-output reduction than long visible CoT.  
**Motivating evidence:** The reward vetoes structural failures, while SFT provides most of the performance gain.  
**Predicted observation:** Concise-plan models with identical gates approach format and execution performance at lower latency.  
**Falsifier:** Long CoT retains a large advantage after gates, model, data, and compute are matched.  
**Minimum test:** Controlled trace-length ablation with identical validators and hidden test workflows.

### Hypothesis 2: multi-reference evaluation changes model ranking

**Proposition:** Models that generate diverse valid graphs are undervalued by single-reference overlap.  
**Motivating evidence:** The reward and metrics privilege one reference node set.  
**Predicted observation:** Some low-overlap workflows pass semantic and execution predicates and change ranking under multi-reference scoring.  
**Falsifier:** Single-reference F1 remains tightly correlated with multi-reference semantic success.  
**Minimum test:** Expert-approved alternatives for at least fifty public toy tasks.

### Hypothesis 3: candidate recall dominates under time shift

**Proposition:** On newly introduced or renamed nodes, retrieval recall explains more end-to-end failure than generation quality.  
**Motivating evidence:** The main test supplies candidate nodes, while ComfyUI changes rapidly.  
**Predicted observation:** Oracle candidate sets recover most performance lost in a time-split evaluation.  
**Falsifier:** Performance remains poor with oracle candidates.  
**Minimum test:** Version-pinned historical catalog and future node release slice.

---

## 14. Deployment and governance considerations

Appropriate use is offline drafting, education, synthetic validation, and benchmark research. Poor fit includes unattended execution, automatic plugin installation, processing private media through unknown services, or workflows that control high-impact systems.

Required safeguards are signed/versioned manifests, schema and type validation, deny-by-default unknown nodes, secret redaction, no network egress by default, bounded parsers, quotas, sandboxed optional execution, content and license policy, human approval, and immutable provenance. Public reports should contain aggregate outcomes and public locators, not user media, prompts, keys, or local paths.

---

## 15. Replication and falsification agenda

First, obtain or reconstruct a versioned bundle containing the exact node and workflow KBs, source lineage, generated instructions and rationales, split manifests, prompts, checkpoint, training configuration, dependencies, and expected metrics. Reproduce parsing round trips and Table 1 before training.

Second, rerun SFT and GRPO with at least three seeds, equal hardware accounting, and full reward logs. Report confidence intervals and every invalid-output class. Isolate each reward component and test reward loopholes with controlled graph mutations.

Third, build a multi-reference benchmark using synthetic or clearly licensed nodes. For each task, preserve several valid graphs plus semantic and resource predicates. Compare single-reference F1, multi-reference F1, execution, instruction satisfaction, edit burden, and cost.

Fourth, run a time-split ecosystem test. Freeze a historical catalog for training and evaluate renamed, deprecated, version-conflicting, and newly introduced nodes. Measure retrieval recall, generator recovery with oracle candidates, unknown-node handling, and false confidence.

Fifth, perform security and provenance testing. Seed malicious metadata, prompt injection, unsigned plugins, external calls, excessive resource requests, and secret-like values. A production candidate should reject or surface every case without execution.

The highest-priority falsifier is evidence that the structural gains disappear under multi-reference semantic evaluation or that valid alternative graphs are systematically rejected. That would show the method is optimizing reference conformity rather than useful workflow synthesis.

---

## 16. Durable restatement

> ComfyUI-R1 shows that a domain-adapted model can generate structurally better ComfyUI workflows when it plans in a code-like representation and is denied positive reward for malformed format, invalid DAGs, or unauthorized nodes. Its reported gains are real within a small, curated, mostly candidate-supplied benchmark, but they do not certify semantic quality, safe execution, dataset rights, or robustness to ecosystem change.

The artifact should be remembered as a proposal–verifier architecture with incomplete verification. Future value depends on widening the gates, testing diverse valid outputs, and separating retrieval, generation, validation, execution, and safety evidence.

---

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment | Boundary |
|---|---|---|---|
| DEP-E README | inventory, source policy, results summary, attribution | Sections 3 and 10 | repository context |
| Manuscript metadata and evidence ledger | versions, sources, code status, related DEPs | Sections 3 and 10 | later ACL context separated |
| Knowledge-base construction | 40k/7,238 nodes; 27k/3,917 workflows; generated docs | Section 2 | provenance not independently audited |
| SFT construction | 3,717/200 workflows; 11,140/600 samples; distractors | Sections 2 and 6 | contamination and licensing unresolved |
| Reward equations | format, DAG, fidelity, overlap, veto | Sections 2, 5, 8 | not executed |
| GRPO and hardware | group 4, clip 0.2, KL 0.001, eight A100s | Section 2 | costs author-reported |
| Table 1 | prompt baselines and full results | Section 7 | candidate nodes supplied |
| Table 2 | SFT/RL and code/JSON ablations | Sections 7 and 8 | no seed variance |
| Table 3 | ComfyBench pass rates | Section 7 | baseline parity uncertain |
| Figures 1–5 | overview, data example, qualitative outputs | Sections 2, 4, 7 | qualitative evidence only |
| Case studies | style adherence and image combination examples | Section 7 boundary | not independently judged |
| Conclusion and references | claimed significance and context | Sections 10 and 16 | novelty scoped |
| DEP methodology, constraints, observations | process and critique | Sections 11–15 | reviewer content distinguished |
| Code example and MVP | offline DAG validator and product proposal | Sections 12–15 | proposal, not paper result |
| Selection/integrity appendix | local source checks and dedup | Appendix B | private bytes not re-inspected |

The canonical arXiv v1 contains three quantitative tables and five numbered figures. No appendix appears in the v1 HTML. The later ACL paper has a separate checklist and authoritative PDF; a full version-delta review is outside this intake.

---

## Appendix B. Source and evidence notes

### Primary reviewed artifact

The complete repository record `.lake-data/DEP-E/DEP-E-20260714-ComfyUI R1` at commit `398f692812550135476e8d560be1d2a01fa2982e` was read in full.[^dep] It contains exactly two tracked Markdown files. No source file was modified, moved, copied, renamed, or reclassified.

### Directly inspected primary evidence

- https://arxiv.org/abs/2506.09790
- https://arxiv.org/html/2506.09790
- https://aclanthology.org/2026.findings-acl.146/
- https://github.com/ATH-MaaS/ComfyUI-Copilot
- https://github.com/Delphoa/Black-Lake/commit/398f692812550135476e8d560be1d2a01fa2982e

### Evidence boundary

The complete DEP-E, canonical v1 metadata, complete v1 HTML, ACL publication record, and current integration repository surface were inspected. The ACL PDF was not used to overwrite v1 table evidence. No paper PDF, dataset, workflow, source archive, model, checkpoint, or code was committed. Experiments and workflows were not independently reproduced or executed. Paper reports, external evidence, reviewer inference, and hypotheses are labeled separately.

### Provenance pair

`BL-DEPPAIR-20260715-80239D97` documents `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. Intake and deposition become complete only after atomic repository submission with both ledger rows.

---

## Footnotes

[^paper]: Xu et al., “ComfyUI-R1: Exploring Reasoning Models for Workflow Generation,” arXiv:2506.09790v1, complete paper at https://arxiv.org/html/2506.09790.
[^record]: Canonical v1 metadata and source links: https://arxiv.org/abs/2506.09790.
[^acl]: Findings of ACL 2026 record, pages 2999–3013 and DOI: https://aclanthology.org/2026.findings-acl.146/.
[^code]: Current paper-linked integration surface: https://github.com/ATH-MaaS/ComfyUI-Copilot.
[^dep]: Source DEP-E: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-ComfyUI%20R1.
