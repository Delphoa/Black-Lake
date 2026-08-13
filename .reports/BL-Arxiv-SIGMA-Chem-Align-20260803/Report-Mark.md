# Report-Mark: SIGMA Chem Align

## Source Metadata

- `Title`: *SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning*.
- `Authors`: Xinyu Wang; Fei Dou; Jinbo Bi; Minghu Song.
- `arXiv`: `2603.25062v1`; submitted 2026-03-26; 15 pages and 6 figures; categories `cs.LG`, `cs.AI`, and `q-bio.QM`.
- `Status`: Submitted to ICML 2026; no acceptance or peer-reviewed venue record was established in the inspected sources.
- `DOI`: https://doi.org/10.48550/arXiv.2603.25062.
- `Primary sources`: https://arxiv.org/abs/2603.25062, https://arxiv.org/pdf/2603.25062, and https://arxiv.org/html/2603.25062.
- `Author context`: https://www.xinyuwang1209.com/publications/ lists SIGMA as a 2026 arXiv preprint and describes structure-invariant alignment plus isomorphic beam search.
- `Source state`: Complete before review. The private local unit contained the full PDF and full-paper HTML; source files were not redistributed.
- `Public-source policy`: Generated Markdown and public locators only. No PDF, HTML, source archive, extracted text, cache, private path, or executable research artifact was uploaded.
- `Implementation status`: The paper says code and pretrained models will be made public upon acceptance. A bounded exact-title/ID search found no author-designated implementation repository at review time.

## Concise Research Notes

### Research Question

Can an autoregressive molecular language model retain the scalability of SMILES while learning that syntactically different strings may encode the same molecular graph, and can structure-aware decoding spend beam capacity on distinct molecules rather than isomorphic duplicates?

### Method

SIGMA has two connected parts. During training, it constructs positive pairs from distinct traversal histories that are required to reconstruct the same graph with a shared valid suffix. An InChIKey oracle checks structural equivalence; a temporary probe suffix makes incomplete prefixes checkable when rings or branches are open. A projection head separates syntax needed for next-token prediction from a lower-dimensional space used for structural alignment. An InfoNCE-style cosine objective is averaged across suffix tokens and added to the language-model NLL.

During inference, IsoBeam expands candidates by cumulative log probability, retains invalid partial SMILES for future completion, and uses a structure identifier to prune valid candidates that duplicate a higher-probability graph already in the beam. The intended effect is to reduce isomorphic redundancy and increase scaffold exploration.

### Experimental Setup

The backbone is GPT-2 Small with 12 layers, 12 attention heads, hidden size 768, maximum sequence length 128, and approximately 124M parameters. Training uses ZINC-250k with a 220k/20k/10k train/validation/test split, a 69-token character vocabulary, two views per molecule, batch size 64, 50 epochs, AdamW, temperature 0.1, and one NVIDIA A100 40GB GPU. The paper names PyTorch 2.1.0, RDKit 2023.09.5, and Transformers 4.35.0.

### Evidence and Results

- The unconditional-generation table reports SIGMA TIS `0.041`, validity `0.998`, uniqueness `0.814`, novelty `0.798`, internal diversity `0.910`, and FCD `0.752`. RandSMILES reports TIS `2.677` and FCD `0.892`; LTCL reports TIS `1.698` and FCD `0.834`. TIS is lower-is-better; FCD is also lower-is-better.
- The PMO table reports means and standard deviations over three runs. For Osimertinib, the displayed scaffold count rises from `5,667 +/- 941` for the baseline to `7,731 +/- 190` for SIGMA, while peak optimization scores remain close. This supports a source-reported exploration gain within that benchmark setting, not a general drug-design claim.
- The IsoBeam analysis scales beam width from 100 to 50,000. The paper reports standard beam search saturating near 5,000 and IsoBeam finding more than 11,000 scaffolds at 50,000, approximately twice the baseline. This is a structural-diversity result with an unreported full cost-quality frontier.
- The paper uses t-SNE on 50 randomized views of 10 molecules and an acetophenone token-similarity heatmap to illustrate latent alignment. These are useful mechanism visualizations but small, qualitative samples.

### Reviewer Assessment

The durable contribution is the separation of representation invariance from syntactic prediction and the extension of the same structural identity idea into decoding. The result is a coherent research hypothesis: align equivalent trajectories at multiple token positions, then stop the decoder from spending its limited beam on equivalent outputs.

The evidence is encouraging but bounded. ZINC-250k, random splitting, three PMO runs, proxy metrics, no independent rerun, no public implementation, uncertain chemistry-normalization policy, and a projection-dimension inconsistency prevent claims of broad chemical validity, synthesis feasibility, or deployment readiness. The source also says the contrastive objective maximizes mutual information, but the inspected experiments do not directly measure mutual information; this is treated as a theoretical framing rather than an independently verified result.

## Evidence and Attribution

| Evidence ID | Evidence | Claim Support | Reviewer Handling |
|---|---|---|---|
| E1 | Complete local PDF and official full-paper HTML for arXiv:2603.25062v1 | Problem, method, equations, algorithm, experiments, tables, appendix, and limitations | Inspected before synthesis; source files withheld |
| E2 | https://arxiv.org/abs/2603.25062 | Identity, authors, version, dates, subjects, abstract, DOI, and submission status | Metadata only; not used alone for empirical claims |
| E3 | https://arxiv.org/html/2603.25062 and the PDF tables | TIS, FCD, validity, PMO scaffold counts, beam-width findings, hyperparameters | Source-reported values; not independently reproduced |
| E4 | https://www.xinyuwang1209.com/publications/ | Author-maintained preprint listing and release context | Supports author-context check, not proof of permanent code absence |
| E5 | FGBench Chemistry, Graph Alignment, and Equivariant Contrastive DEP manuscripts | Benchmark governance, graph alignment, and invariance-aware contrastive bridges | Related synthesis only; no joint experiment claimed |
| E6 | Live Black Lake and Black-Lake-Data READMEs | Filing, attribution, public-source locality, and no-source-upload policy | Repository authority, not research evidence |
| E7 | Selection, dedup, and source-integrity checks | Eligibility, complete-paper gate, and public-output boundary | Process evidence summarized without private paths |

## Random Selection and Dedup Evidence

- Enumeration used `rg --files -g "*.pdf"` against the local arXiv archive root.
- The 75,960 PDF paths collapsed to 75,957 unique parent units. Candidate identities were derived from PDF filenames and parent folders; nearby archive metadata was used for the selected unit.
- The frozen pool was sorted by parent-unit identity and sampled uniformly with PowerShell `Get-Random`. The selected zero-based eligible-pool index was 23.
- Repository, metadata-inventory, and automation-memory reconciliation observed 68,990 unique arXiv ID markers. It excluded 75,640 parent units by prior identifiers and withheld 185 units with no derivable arXiv identifier, leaving 132 eligible units.
- Before acceptance, exact searches for `2603.25062`, `10.48550/arXiv.2603.25062`, the normalized title, and SIGMA-related slugs returned no match in Black Lake artifacts, automation memory, or the metadata-only Black-Lake-Data inventory. Exact ID and title searches in both live repository contexts also returned no result.
- Duplicate reselections: zero. Same-paper 24-hour marker: none found. The first valid draw was accepted after the source gate passed.

## Source-Integrity Evidence

- Initial classification: complete; review began only after validation.
- PDF: 2,358,330 bytes; begins with `%PDF-`; trailing bytes include `%%EOF`.
- Full-paper HTML: 361,481 bytes; 66,317 visible body characters after removing scripts and styles; article/LaTeXML document markers; 91 heading or section markers; seven structure terms including Introduction, Methodology, Experiments, Conclusion, References, and Appendix.
- Abstract-only pages were not counted as full text. The retained HTML was the full paper, not the `/abs/` metadata page.
- Repair: none. No local README, provenance record, machine summary, or verification report needed repair updates because the unit was already complete.
- Source locality: all original source material and review derivatives remain in the private archive. No `.source/` directory was created.

## Related DEP Entries

Exactly three related entries were selected from the current Black Lake repository state:

| Entry | Concrete Relevance | Source Basis |
|---|---|---|
| [FGBench Chemistry](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-FGBench%20Chemistry/fgbench_chemistry_manuscript.md) | Shares the molecular/SMILES domain and shows why pair construction, scaffold or molecule leakage, property-unit discipline, validity, and functional-group coverage must accompany language-model scores. | Review of arXiv:2508.01055v4 and the official FGBench repository recorded by that DEP. |
| [Graph Alignment](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Graph%20Alignment/graph_alignment_manuscript.md) | Provides a direct graph-representation neighbor: alignment and uniformity objectives need graph-aware equivalence, stable negatives, and evaluation beyond a single embedding metric. | Review of arXiv:2308.09292 and DOI 10.1145/3583780.3615185 recorded by that DEP. |
| [Equivariant Contrastive](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Equivariant%20Contrastive/equivariant_contrastive_manuscript.md) | Supplies a contrastive/equivariance bridge for testing whether augmentation-induced invariance transfers beyond the training transformation family. | Review of arXiv:2211.05290 and its full-paper evidence recorded by that DEP. |

## Synthesis Note

### Concept Bridge

SIGMA, FGBench, Graph Alignment, and Equivariant Contrastive all make representation assumptions testable by introducing an explicit structural relation: equivalent molecular views, localized functional-group changes, graph-level alignment, or transformation-linked sequential views. The shared engineering lesson is that a representation claim needs a declared equivalence oracle, controlled positives and negatives, leakage-aware splits, and metrics that separate invariance from task utility. SIGMA adds a second control surface: the same structural identity used for learning can govern decoder allocation, but only if the identity oracle is valid for partial structures and its compute cost is measured.

### Potential Implementations

1. `Equivalence-aware molecular benchmark`: Build a research-only harness that generates synthetic graph/view pairs, checks declared equivalence with a versioned oracle, and reports trajectory agreement separately from validity, novelty, and diversity.
2. `Structure-aware decoding audit`: Compare standard beam search with an authorized local IsoBeam-style decoder using cached synthetic structure IDs, measuring unique structures, validity, latency, memory, and the number of pruned candidates at each width.
3. `Chemistry representation conformance gate`: Combine FGBench-style leakage checks, Graph Alignment-style alignment/uniformity diagnostics, and SIGMA-style TIS into one report that rejects a claimed gain when split integrity, normalization, or task utility is not established.

### Deeper Relationship Observations

1. `Equivalence is the hidden data contract`: SIGMA's positive pairs, Graph Alignment's graph objective, and Equivariant Contrastive's augmentations all depend on a transformation preserving the intended semantics; an incorrect oracle teaches the model the wrong invariance.
2. `Training invariance and inference diversity are coupled but not identical`: SIGMA can reduce latent fragmentation while IsoBeam changes search allocation; FGBench's property reasoning shows that improved structural awareness still does not establish downstream chemical validity.
3. `The right metric is a vector, not a scalar`: TIS, FCD, validity, uniqueness, novelty, internal diversity, scaffold count, latency, and memory answer different questions; a single favorable metric can hide a harmful trade-off.

### Conceptual Similarities

1. All four artifacts treat structural or transformation-aware relationships as first-class supervision or evaluation objects rather than implicit model behavior.
2. All require controlled positives, meaningful negatives, and explicit checks against representation shortcuts or leakage.
3. All support a provenance-first workflow in which benchmark results remain bounded by the data construction, oracle, split, and reproduction evidence actually inspected.

### MVP Implementations with Code Mock-ups

1. `Synthetic trajectory-equivalence gate`: A dependency-free check for whether two token routes are declared equivalent and share the same future suffix.

```python
def equivalent_route_pair(route_a, route_b, shared_suffix, oracle):
    if route_a == route_b:
        return False
    if not oracle(route_a + shared_suffix):
        return False
    if not oracle(route_b + shared_suffix):
        return False
    return True

toy_oracle = lambda sequence: sequence.count("graph-A") == 1
print(equivalent_route_pair("view-graph-A|", "alt-graph-A|", "graph-A", toy_oracle))
```

2. `Structure-aware beam ledger`: A bounded synthetic beam that keeps one candidate per declared structure ID and records pruning.

```python
def unique_beam(candidates, width):
    seen = set()
    kept = []
    pruned = 0
    for score, structure_id, token_route in sorted(candidates, reverse=True):
        if structure_id in seen:
            pruned += 1
            continue
        seen.add(structure_id)
        kept.append((score, structure_id, token_route))
        if len(kept) == width:
            break
    return {"kept": kept, "pruned": pruned, "unique_structures": len(seen)}

beam = [(0.9, "A", "route-1"), (0.8, "A", "route-2"), (0.7, "B", "route-3")]
print(unique_beam(beam, width=2))
```

3. `Metric-vector acceptance gate`: A research-only comparison that prevents a scaffold-count gain from hiding invalidity or cost regressions.

```python
def accept(reference, candidate):
    return (
        candidate["validity"] >= reference["validity"] - 0.01
        and candidate["unique_structures"] >= reference["unique_structures"]
        and candidate["latency_ms"] <= reference["latency_ms"] * 1.25
        and candidate["memory_mb"] <= reference["memory_mb"] * 1.25
    )

baseline = {"validity": 0.99, "unique_structures": 100, "latency_ms": 10, "memory_mb": 100}
candidate = {"validity": 0.995, "unique_structures": 130, "latency_ms": 11, "memory_mb": 110}
print({"accepted": accept(baseline, candidate)})
```

### Developer Challenges

1. Implement a chemistry-normalization and partial-graph oracle whose handling of stereochemistry, tautomerism, ring closures, attachment points, and invalid prefixes is explicit, deterministic, and version-pinned.
2. Measure the end-to-end IsoBeam frontier, including RDKit validation, GPU utilization, candidate expansion, memory pressure, latency, and quality at each beam width.
3. Build leakage-aware evaluation splits and a reproducible metric ledger that separates invariance, generative quality, exploration, and downstream objective performance.

### Author Challenges

1. Publish the code, pretrained models, environment lock, data-preparation commands, and evaluation scripts needed to reproduce the central tables before making implementation claims.
2. Resolve and document the projection-head dimensionality difference between the main method text (`d_proj=128`) and Appendix B/Table 3 (`256`).
3. Add multi-dataset, scaffold-split, stereochemistry-aware, repeated-seed, and cost-quality evaluations with confidence intervals and external validation of chemical utility.

## Validation Notes

- Manuscript/report contract: required schema headings, evidence ledger, source references, explicit uncertainty, safe implementations, and final attribution blocks are present.
- Exact-count contracts: three related DEP entries; three Synthesis Note potential implementations; three deeper relationship observations; three conceptual similarities; three MVP implementations with three code mock-ups; three developer challenges; three author challenges.
- Code validation target: all three Python mock-ups are dependency-free, bounded, and use synthetic identifiers or metrics only.
- Selection contract: 75,960 PDFs, 75,957 parent units, 132 eligible units, selected index 23, zero duplicate reselections.
- Source-gate contract: complete PDF and full-paper HTML verified before review; no repair and no abstract-only substitution.
- Public-output allowlist: generated Markdown under `.logs`, `.reports`, and `.lake-data`, including the DEP-E publication-index update; no source binary, cache, local path, or `.source/` directory.
- Reproduction boundary: reported values were inspected in the complete paper and official HTML; no experiment, code, dataset, model, or chemical oracle was executed.

## Attribution Block

- Source URL: https://arxiv.org/abs/2603.25062
  - Applies to: `Report-Mark.md`.
  - Notes: Canonical identity, authors, dates, subjects, version, DOI, and submission status.
- Source URL: https://arxiv.org/pdf/2603.25062
  - Applies to: `Report-Mark.md`.
  - Notes: Public equivalent of the complete PDF used for method, result, appendix, and table review; not redistributed.
- Source URL: https://arxiv.org/html/2603.25062
  - Applies to: `Report-Mark.md`.
  - Notes: Official full-paper HTML used for searchable section-level review; not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2603.25062
  - Applies to: `Report-Mark.md`.
  - Notes: Persistent arXiv DOI.
- Source URL: https://www.xinyuwang1209.com/publications/
  - Applies to: `Report-Mark.md`.
  - Notes: Author-maintained publication listing and bounded code/release-context check.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-FGBench%20Chemistry/fgbench_chemistry_manuscript.md
  - Applies to: `Report-Mark.md`.
  - Notes: Related DEP for molecular reasoning benchmark construction and evaluation boundaries.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-Graph%20Alignment/graph_alignment_manuscript.md
  - Applies to: `Report-Mark.md`.
  - Notes: Related DEP for graph alignment and uniformity.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Equivariant%20Contrastive/equivariant_contrastive_manuscript.md
  - Applies to: `Report-Mark.md`.
  - Notes: Related DEP for equivariant contrastive learning.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `Report-Mark.md`.
  - Notes: Live processed-repository authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `Report-Mark.md`.
  - Notes: Live DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `Report-Mark.md`.
  - Notes: Live related-repository authority and dedup context.
- Source handling: No PDF, HTML, source archive, extracted text, cache, private path, or `.source/` file was uploaded, committed, or attached.
