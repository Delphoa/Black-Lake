# Report-Mark: Shuffled Autoregression

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Shuffled Autoregression For Motion Interpolation* |
| Authors | Shuo Huang; Jia Jia; Zongxin Yang; Wei Wang; Haozhe Wu; Yi Yang; Junliang Xing |
| Canonical record | [arXiv:2306.06367v1](https://arxiv.org/abs/2306.06367v1) |
| arXiv DOI | [10.48550/arXiv.2306.06367](https://doi.org/10.48550/arXiv.2306.06367) |
| Publisher DOI | [10.1109/ICASSP49357.2023.10095312](https://doi.org/10.1109/ICASSP49357.2023.10095312) |
| Venue | IEEE ICASSP 2023 |
| Dates | Submitted 2023-06-10; arXiv v1 |
| Public implementation | No official code repository was established by the inspected author page or exact-name GitHub repository search |
| Review date | 2026-07-24; exact local execution time withheld |
| Source state | Complete and verified after bounded local repair; all source files withheld locally and not uploaded |

## Concise Research Notes

**Problem.** Motion interpolation must synthesize a plausible pose sequence from isolated endpoints. Left-to-right autoregression accumulates errors because later frames condition on an increasingly long chain of predicted poses, while non-autoregressive models can over-smooth motion. Classical interpolation uses flexible two-sided keyframe influence, but learned sequence models often impose a fixed temporal dependency order.

**Method.** Shuffled AutoRegression (SAR) makes generation order and frame dependencies explicit as a directed acyclic graph. The paper instantiates a three-stage graph: generate sparse keyframes through divide and conquer, fill short intervals frame by frame for local continuity, and regenerate the sequence in parallel for global smoothing. A Flexible Dependency Attention Mask (FDAM), described as a shuffled transpose of graph adjacency, constrains a GPT-2-style temporal decoder so each target frame sees only its declared predecessors. Spatial pose encoding uses joint attention; a spatial decoder maps temporal embeddings back to poses.

**Training and data.** The first training phase uses teacher forcing with MSE. The second freezes the model while producing the first two stages from endpoint-only input, then trains the smoothing pass against ground truth. Experiments use a constructed AMASS/SMPL+H corpus of 166,696 windows, roughly split 70/10/20, with sequence length 31. The pose encoder has four blocks, 1,248-dimensional pose embeddings, and 12 attention heads; the temporal decoder has six blocks with eight heads. The reported keyframe set is `[1, 9, 19, 29]`.

**Reported evidence.** The full model reports MPJAE `0.0102`, MPJPE `0.0365`, and NPSS `0.089`, compared with BERT `0.0153`, `0.0466`, and `0.095`. Original chronological autoregression degrades to `0.1847`, `0.3461`, and `6.594`. A binary-search dependency order reports `0.0152`, `0.0584`, and `0.107`; removing smoothing reports `0.0121`, `0.0387`, and `0.096`. These ablations support the importance of both graph topology and smoothing in the tested setting.

**Boundary evidence.** The paper evaluates one constructed dataset, one endpoint-interpolation setting, one short architecture description, and a single displayed qualitative sequence selected from 20 test samples. It reports no seed variance, user study, physical-contact metric, cross-dataset transfer, latency, compute cost, parameter count, or tested multi-keyframe/other-domain extension. Table 1's signed Neighbor-L2 presentation is internally difficult to interpret: the narrative says closeness to ground truth is better, while the caption also says lower is better and mixes ground-truth-relative and full-model-relative values. This review preserves the ambiguity and does not derive a corrected value.

**Reviewer interpretation.** SAR's durable idea is broader than the reported motion model: dependency topology is an error-control surface. A practical derivative should compile one graph into the training mask, inference schedule, and trace validator; measure stage-wise error and maximum dependency depth; enforce acyclicity; and treat topology transfer as a new experiment rather than a free consequence of the framework.

## Evidence and Attribution

| Evidence | Source location | Assessment |
|---|---|---|
| SAR expresses generation order and conditioning as a DAG | Sections 1 and 3 of the [full paper](https://ar5iv.labs.arxiv.org/html/2306.06367) | Direct source claim; high confidence. |
| FDAM is derived from shuffled transposed graph adjacency | Section 3.2.2 and Figure 2 | Direct mechanism claim; high confidence for the described construction. |
| Three stages: keyframes, frame-by-frame fill, smoothing | Section 3.1.2 and Figure 2 | Direct source claim; high confidence. |
| AMASS corpus has 166,696 windows and approximate 70/10/20 splits | Section 4.1 | Direct source claim; split granularity and subject isolation are not specified. |
| Full model reports MPJAE `0.0102`, MPJPE `0.0365`, NPSS `0.089` | Table 1, visually checked on PDF page 4 | Direct numeric claim; experiments not reproduced. |
| Original AR reports `0.1847`, `0.3461`, and `6.594` on the same three metrics | Table 1 ablation rows | Strong within-paper negative evidence for chronological order in this setup. |
| Binary-search order and no-smoothing variants both underperform the full model | Table 1 and Section 4.4 | Supports contribution of graph topology and smoothing; no multi-seed uncertainty. |
| Neighbor-L2 normalization is ambiguous | Table 1 caption, row values, and Section 4.3 prose | Reviewer finding grounded in a source inconsistency; no correction inferred. |
| The qualitative figure is one representative sequence chosen from 20 samples | Section 4.3 and Figure 3 | Direct source boundary; not a blinded or statistical human evaluation. |
| No official code repository was established | Author page and exact-name GitHub repository search | Negative discovery evidence, not proof that no code exists anywhere. |
| Graph compilation, stage telemetry, and topology tests are needed for deployment | Method structure and missing operational evidence | Reviewer recommendations, not author-validated features. |

The complete PDF, full-paper HTML, metadata HTML, TeX/source archive, rendered pages, provenance records, and verification reports were used only in the private source-first workflow. They remain withheld locally. Public links identify the evidence without redistributing local source artifacts.

## Related DEP Entries

1. **AR-Drag Motion Control** — `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md`. Source basis: the inspected manuscript reviews few-step frame-wise autoregressive video diffusion, Self-Rollout, cache state, and exposure-bias failure. Relevance: both works make generated history a first-class error source, but SAR changes the dependency topology while AR-Drag aligns training with the existing causal rollout.
2. **Structured Thoughts** — `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md`. Source basis: the inspected review describes a pruning-aware custom attention mask that encodes which temporary and durable tokens remain visible, plus inference-time state deletion. Relevance: both systems turn a semantic dependency policy into attention visibility and require exact agreement between training masks and runtime transitions.
3. **InterDance Reactive 3D Dance Generation** — `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md`. Source basis: the inspected manuscript reviews leader-conditioned 3D duet motion generation and a large-scale interaction dataset. Relevance: it provides a neighboring human-motion domain where temporal coherence, interaction constraints, diversity, and physical plausibility would test whether SAR-style dependency design transfers beyond endpoint interpolation.

## Synthesis Note

### Concept Bridge

Shuffled Autoregression, AR-Drag, Structured Thoughts, and InterDance share a hidden systems object: the graph of information allowed to influence each generated state. SAR exposes that object directly as frame dependencies and compiles it into FDAM. AR-Drag focuses on whether the state seen during training matches the generated history seen during inference. Structured Thoughts uses a visibility mask to teach a model which scratch state will disappear at runtime. InterDance supplies a harder motion domain in which dependencies include not only time but another moving person and music.

The bridge suggests a single engineering rule: specify dependency semantics once, then derive training visibility, inference scheduling, cache/state mutation, and audit traces from that specification. A mismatch in any surface changes the actual model. The graph also creates measurable risk variables—maximum path depth, fan-in, unreachable targets, stale-state reads, and stage-specific error growth—that end-to-end loss alone can hide.

### Potential Implementations

1. **Graph-to-mask compiler:** Accept a versioned acyclic dependency graph and emit its topological schedule, FDAM tensor, dependency-depth report, and deterministic synthetic fixtures.
2. **Stage-aware motion audit:** Measure endpoint error, local continuity, physical plausibility, and diversity after keyframe, local-fill, and smoothing stages instead of reporting only the final sequence.
3. **Cross-domain dependency laboratory:** Compare chronological, binary-search, SAR, and interaction-aware graphs under matched models on synthetic sequences before using authorized motion datasets.

### Deeper Relationship Observations

1. **Order and visibility are the same control at different layers.** SAR changes frame order and FDAM together; Structured Thoughts changes token visibility and runtime retention together. Separating those choices invites train-inference mismatch.
2. **Error follows information paths, not wall-clock position.** SAR shortens or redistributes prediction chains, while AR-Drag improves the fidelity of each history state. These are complementary levers: topology controls where errors can travel; rollout alignment controls what each node actually receives.
3. **Human-motion constraints enlarge the graph.** InterDance adds partner interaction and music to temporal dependencies. A transferable SAR should represent external anchors and bilateral constraints explicitly rather than assuming a one-dimensional time DAG is sufficient.

### Conceptual Similarities

1. **Explicit intermediate state:** Predicted frames, KV history, durable outcomes, and partner-motion features are all intermediate state whose provenance affects later outputs.
2. **Structured sparsity:** FDAM, pruning-aware visibility, and bounded history restrict which prior states can influence a target, trading flexibility for controllability and efficiency.
3. **Stage-specific failure propagation:** A missing keyframe, corrupted rollout, insufficient outcome summary, or misread partner pose can survive downstream smoothing and appear only as an end-to-end quality failure.

### MVP Implementations with Code Mock-Ups

1. **Acyclic schedule validator.** This bounded utility rejects missing nodes and cycles before a graph can become an attention mask.

```python
from collections import defaultdict, deque


def topological_order(nodes: set[int], edges: list[tuple[int, int]]) -> list[int]:
    children: dict[int, list[int]] = defaultdict(list)
    indegree = {node: 0 for node in nodes}
    for source, target in edges:
        if source not in nodes or target not in nodes:
            raise ValueError("edge references an unknown node")
        children[source].append(target)
        indegree[target] += 1
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    order: list[int] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for target in children[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    if len(order) != len(nodes):
        raise ValueError("dependency graph contains a cycle")
    return order
```

2. **Dependency-mask compiler.** Rows are target frames and columns are permitted predecessors; tests should compare this tensor with the runtime schedule.

```python
def dependency_mask(
    order: list[int], edges: list[tuple[int, int]]
) -> list[list[bool]]:
    position = {node: index for index, node in enumerate(order)}
    if len(position) != len(order):
        raise ValueError("order contains duplicate nodes")
    mask = [[False] * len(order) for _ in order]
    for source, target in edges:
        if position[source] >= position[target]:
            raise ValueError("edge violates topological order")
        mask[position[target]][position[source]] = True
    return mask
```

3. **Path-depth telemetry.** Maximum predecessor depth is a simple topology risk indicator; it is not a substitute for empirical motion error.

```python
def dependency_depths(
    order: list[int], edges: list[tuple[int, int]]
) -> dict[int, int]:
    parents = {node: [] for node in order}
    for source, target in edges:
        parents[target].append(source)
    depth: dict[int, int] = {}
    for node in order:
        depth[node] = 0 if not parents[node] else 1 + max(depth[p] for p in parents[node])
    return depth
```

### Developer Challenges

1. **One semantic source of truth:** Graph direction, topological order, tensor row/column conventions, padding, active-frame state, and inference updates must be generated and tested together.
2. **State and position correctness:** Shuffled generation changes when frames become valid; batching, positional encoding, caches, masking, and smoothing must not leak unavailable or future state.
3. **Stage-aware observability:** Developers need traces for graph version, active dependencies, path depth, per-stage losses, contact violations, endpoint error, and fallback decisions without logging restricted motion data.

### Author Challenges

1. **Clarify metric semantics:** The signed Neighbor-L2 transformation, its comparison target, and lower-versus-closer-to-zero direction should be defined unambiguously and accompanied by raw values.
2. **Strengthen experimental validity:** Subject-level split rules, multiple seeds, confidence intervals, stronger motion baselines, physical metrics, and blinded human preference tests are needed.
3. **Test the broad claim:** Multi-keyframe interpolation, longer sequences, cross-dataset motion, other interpolation domains, and topology sensitivity should be evaluated rather than left as architectural possibilities.

## Validation Notes

- **Random selection:** 75,780 PDFs mapped to 75,777 paper units. A used index of 1,204 arXiv base IDs excluded 297 units; 185 identifier-incomplete units were withheld. `Get-Random` selected zero-based index 30,096 from 75,295 eligible units.
- **Deduplication:** The scan covered Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and the corresponding Black-Lake-Data surfaces. Exact matching used arXiv ID, both DOI values, canonical title, normalized title, archive token, and slug. Duplicate rejections/reselections: 0. Recent-marker cutoff: 2026-07-23.
- **Initial source state:** Partial because a valid PDF existed without verified full-paper HTML.
- **Repair:** The valid PDF was preserved. A bounded acquisition obtained metadata HTML, an approved ar5iv full-paper fallback, and the arXiv source package. No partial bytes were accepted as progress.
- **PDF validation:** 2,310,025 bytes, `%PDF-` header, terminal `%%EOF`, five pages, unencrypted. All five pages were rendered; the method diagram and Table 1 were visually inspected and legible despite non-fatal local font-substitution warnings.
- **HTML validation:** 189,178 bytes, 30,036 stripped body characters, valid full-document marker, 43 heading markers, and six paper-structure terms.
- **Supporting artifacts:** Metadata HTML 41,910 bytes; source package 2,641,656 bytes; zero partial files; seven author-profile links.
- **Review boundary:** Full paper, source structure, public metadata, conference/author context, and exactly three related entries were inspected. Code and experiments were not executed, and no official code repository was established.
- **Public-output gate:** The intended submission allowlist consists only of this report, the generated log, the DEP README, the manuscript, and the DEP-E publication index update.
- **Source-upload gate:** No PDF, HTML, source archive, extracted text, render, cache, local provenance record, or verification file belongs in the public commit. Source files were withheld locally.

## Attribution Block

| Source | Attribution | Use and boundary |
|---|---|---|
| [arXiv:2306.06367v1](https://arxiv.org/abs/2306.06367v1) | Shuo Huang, Jia Jia, Zongxin Yang, Wei Wang, Haozhe Wu, Yi Yang, and Junliang Xing | Canonical metadata, abstract, subject classes, version, and public locators; accessed 2026-07-24. |
| [Full-paper ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2306.06367) | Same authors; ar5iv conversion of the arXiv paper | Searchable methods, experiments, conclusion, and references; verified local copy withheld. |
| [arXiv PDF](https://arxiv.org/pdf/2306.06367) | Same authors | Primary paper, figures, Table 1, and pagination; verified local copy withheld. |
| [arXiv DOI](https://doi.org/10.48550/arXiv.2306.06367) | DataCite/arXiv persistent record | Persistent identifier. |
| [IEEE DOI](https://doi.org/10.1109/ICASSP49357.2023.10095312) | IEEE ICASSP 2023 | Publisher and proceedings locator. |
| [ICASSP 2023 program](https://icassp23-static-program.pages.dev/) | IEEE ICASSP 2023 organizers | Official program context and author listing. |
| [Tsinghua HCSI publication page](https://hcsi.cs.tsinghua.edu.cn/) | Jia Jia's HCSI group | Author-maintained venue/publication context. |
| Local metadata HTML, full-paper HTML, PDF, source archive, rendered pages, attribution record, summary, and integrity reports | Original paper authors and locally generated verification metadata | Evidence only; all files withheld locally and none uploaded. |
| `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Delphoa/Black-Lake DEP-E artifact | Related autoregressive motion-generation synthesis. |
| `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md` | Delphoa/Black-Lake DEP-A artifact | Related custom-attention-mask and runtime-state synthesis. |
| `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` | Delphoa/Black-Lake DEP-E artifact | Related human-motion generation and evaluation synthesis. |
