# Report-Mark: SAILFISH Vetting

## Source Metadata

| Field | Value |
|---|---|
| Paper | *SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds* |
| Authors | Priyanka Bose; Dipanjan Das; Yanju Chen; Yu Feng; Christopher Kruegel; Giovanni Vigna |
| arXiv | 2104.08638v2; submitted 2021-04-17, revised 2021-12-13 |
| Venue | 2022 IEEE Symposium on Security and Privacy, pages 161-178 |
| DOI | https://doi.org/10.1109/SP46214.2022.9833721 |
| Primary records | https://arxiv.org/abs/2104.08638; https://fredfeng.github.io/papers/sailfish.pdf |
| Official implementation | https://github.com/ucsb-seclab/sailfish |
| Access date | 2026-07-13 |
| Source collection | One local archive PDF and adjacent metadata were inspected; no source file was deposited or redistributed. |
| Review posture | Defensive research review. Paper claims are separated from released-artifact facts and reviewer inference. |

## Concise Research Notes

SAILFISH addresses state-inconsistency bugs in Ethereum smart contracts, especially reentrancy and transaction-order dependence (TOD). The paper defines the target behaviorally: two schedules begin from the same contract state but reach different final states because an attacker alters call control flow or transaction order. It then narrows detection to *hazardous access* pairs, where two public-reachable operations touch the same storage state and at least one operation writes.

The system is intentionally staged. EXPLORE constructs a storage dependency graph (SDG) from Slither-derived control/data-flow facts and queries it for possible hazardous accesses. When the graph produces a candidate, REFINE symbolically evaluates the relevant slice rather than the entire contract. A domain-specific value-summary analysis (VSA) supplies path-conditioned approximations of storage values so the symbolic evaluator can reject infeasible candidates without paying for exhaustive path-by-path summaries.

The paper evaluates 89,853 deduplicated Solidity contracts collected from Etherscan through 2020 after excluding 2,068 contracts that used very old Solidity versions or Vyper. Reported mean analysis time is 30.79 seconds per contract. On a manually inspected 750-contract sample, the authors report 26 reentrancy and 110 TOD vulnerabilities; SAILFISH reports zero false negatives and 11/59 false positives for the two classes. Across contracts uniquely flagged by SAILFISH and manually selected for tractability, the authors report 47 previously unknown exploitable contracts, including 11 with Ether-draining impact.

The ablation is central evidence for VSA rather than decorative architecture. Static-only analysis produces 3,391 reentrancy and 14,485 TOD warnings; symbolic refinement with havoc reduces those to 2,436 and 10,560; VSA-guided refinement further reduces them to 2,076 and 7,555. The paper also reports a 21.50% timeout rate when replacing VSA with path-by-path summaries on a 2,000-contract subset, supporting the claimed precision/scalability tradeoff.

The limitations are material. SAILFISH depends on source code and Slither's call graph/taint analysis, does not claim soundness, abstracts away complex Solidity semantics such as exception propagation, transaction reversion, and out-of-gas behavior, and loses precision around unresolved calls, inline assembly, loops, and collections. The historical corpus and toolchain also limit direct claims about current Solidity or proxy-heavy contracts. The official repository does provide code, data, Docker guidance, and test cases, but this review did not execute them.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Assessment |
|---|---|---|---|
| E1 | Local PDF-derived full text, identified by arXiv:2104.08638v2 | Definitions, architecture, experimental setup, tables, ablation, limitations, appendices | Primary and direct; extraction contained some typographic noise. |
| E2 | arXiv metadata and abstract | Authors, dates, version, subject areas, journal reference, arXiv DOI | Primary metadata. |
| E3 | IEEE/DOI and UCSB SecLab publication records | Venue, pages, publisher DOI, publication context | Primary or institutional metadata. |
| E4 | `ucsb-seclab/sailfish` README | Current public availability of code/data, Docker workflow, example invocation | Official artifact documentation; execution not reproduced. |
| E5 | Three Black-Lake-Data DEP artifacts plus their cited arXiv abstracts | Conceptual bridges to staged vulnerability discovery, graph propagation, and verification-backed reasoning | Related context only; not validation of SAILFISH. |

## Related DEP Entries

Exactly three existing entries were selected after inspecting both their repository text and cited primary abstract.

| Related entry | Concrete overlap | Source basis |
|---|---|---|
| [Antaeus finding](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260702-Tech%20Intel%201102/daily_research_findings_2026-07-02_1102.md) | Both systems reduce expensive security reasoning by first prioritizing a smaller candidate surface, then validating findings with broader context and traceable evidence. SAILFISH uses SDG queries plus symbolic refinement; Antaeus uses repository signals plus context-grounded comparative validation. | DEP synopsis and https://arxiv.org/abs/2607.01138. |
| [Chai finding](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260626-Tech%20Intel%201103/daily_research_findings_2026-06-26_1103.md) | Both turn program relations into graph-guided security search. SAILFISH queries storage dependencies for hazardous access; Chai propagates validated library-level discrepancy signals through a cryptographic dependency graph. | DEP synopsis and https://arxiv.org/abs/2606.26933. |
| [VeriChat finding](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260706-Tech%20Intel%200104/daily_research_findings_2026-07-06_0104.md) | Both use a broad, relatively inexpensive reasoning layer and then invoke more precise tools. SAILFISH couples static exploration to SMT-backed symbolic evaluation; VeriChat couples agent reasoning to syntax, synthesis, simulation, and formal verification. | DEP synopsis and https://arxiv.org/abs/2607.01668. |

## Synthesis Note

### Concept Bridge

Across SAILFISH and the three related entries, the recurring design pattern is *candidate compression followed by evidence-producing refinement*. A cheap first stage preserves recall by over-approximating or prioritizing; a narrower second stage spends more computation on feasibility, context, or proof. The bridge is not that the systems share an implementation. It is that they separate search-space management from confidence generation and preserve enough provenance for a human to audit why a candidate survived.

### Potential Implementations

1. **State-diff pull-request gate** - Build storage-dependency summaries for changed smart-contract functions, flag newly introduced hazardous-access pairs, and require a bounded feasibility check before presenting review findings. Inputs are source diffs and compiler metadata; outputs are traceable candidate slices; controls include repository-local execution, dependency pinning, and no transaction broadcasting.
2. **Analyzer disagreement workbench** - Run multiple defensive analyzers on a synthetic or authorized corpus, normalize warnings to storage/call relations, and route disagreements through a SAILFISH-inspired refinement layer. The goal is evidence-rich triage rather than an ensemble vote; success is measured by independently labeled precision/recall and stable reproductions.
3. **Modern-Solidity compatibility harness** - Replay known-safe and known-vulnerable toy patterns across compiler generations, proxy patterns, and Slither versions, recording when SDG construction, taint resolution, or VSA behavior changes. The output is a versioned compatibility matrix, not an automatic security certification.

### Deeper Relationship Observations

1. SAILFISH's hazardous access is an explicit intermediate representation of suspicion; Antaeus safety conditions and Chai discrepancy leads play the same epistemic role by making the reason for expensive follow-up inspectable.
2. VSA demonstrates that more precise summaries are not automatically more useful: representation cost and downstream solver burden matter. VeriChat's tool routing exposes an analogous systems question—when to invoke a formal tool and what context to feed it.
3. The strongest shared operational value is not raw finding count but *triage economics*: each system tries to reduce human review or high-cost analysis while retaining evidence links and visible failure boundaries.

### Conceptual Similarities

1. **Two-stage assurance:** Broad candidate discovery is followed by a narrower validation or verification stage.
2. **Graph/context grounding:** Relations among state, functions, repositories, dependencies, or verification artifacts constrain otherwise noisy search.
3. **Explicit uncertainty:** Over-approximation, false positives, hallucination risk, or missing instrumentation are treated as workflow inputs rather than hidden defects.

### MVP Implementations with Code Mock-ups

#### 1. Hazardous-Access Slice Viewer

This local-only toy finds cross-function read/write pairs over a synthetic access inventory. It is a review aid, not a Solidity analyzer.

```python
from itertools import combinations

def hazardous_pairs(accesses):
    pairs = []
    for left, right in combinations(accesses, 2):
        same_state = left["slot"] == right["slot"]
        cross_function = left["function"] != right["function"]
        has_write = "write" in {left["mode"], right["mode"]}
        if same_state and cross_function and has_write:
            pairs.append((left, right))
    return pairs
```

#### 2. Summary-Guided Feasibility Gate

This bounded mock-up rejects a candidate when a required precondition conflicts with the state at the call boundary. It deliberately avoids exploit generation.

```python
def feasible(candidate, state_at_call, required_preconditions):
    for name, expected in required_preconditions.items():
        observed = state_at_call.get(name, "unknown")
        if observed != "unknown" and observed != expected:
            return {"candidate": candidate, "feasible": False, "reason": name}
    return {"candidate": candidate, "feasible": True, "reason": "needs deeper check"}
```

#### 3. Analyzer Regression Ledger

This mock-up records defensive analyzer outcomes against human labels so compatibility changes remain auditable.

```python
def score(rows):
    tp = sum(r["predicted"] and r["label"] for r in rows)
    fp = sum(r["predicted"] and not r["label"] for r in rows)
    fn = sum(not r["predicted"] and r["label"] for r in rows)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "precision": precision, "recall": recall}
```

### Developer Challenges

1. Reconstruct a trustworthy interprocedural storage graph across inheritance, libraries, proxies, inline assembly, and compiler versions without silently dropping unresolved edges.
2. Preserve useful path conditions in summaries while bounding solver complexity, loops, collections, external return values, and transaction-level semantics.
3. Build a reproducible evaluation corpus with independent labels, tool/version pins, timeout accounting, and evidence that distinguishes detection, exploitability, and business impact.

### Author Challenges

1. Re-evaluate SAILFISH on a current, independently sampled contract corpus and report how proxy architecture and newer Solidity semantics change precision, recall, timeout, and error rates.
2. Publish a fully pinned artifact manifest connecting each paper table and ablation figure to exact commands, corpus hashes, expected outputs, and known nondeterminism.
3. Tighten the unsoundness map by isolating the empirical effect of Slither call-graph gaps, imprecise taint, exception/reversion semantics, collection abstraction, and inter-contract destination resolution.

## Validation Notes

- The local PDF-derived text was cross-checked against the author-hosted public PDF view where extraction noise affected typography or table context.
- Quantitative statements are attributed to the authors and were not represented as independently reproduced.
- The official repository was inspected for availability and documented workflow; repository presence was not treated as evidence that the experiments reproduce today.
- Random selection used one uniform index over 75,761 PDF-parent paper units; the first draw was eligible with no exclusions or reselections.
- Cache extraction used `missing-only`; the initial miss became a partial cache with PDF text present and no local HTML/source text.
- Dedup scans covered the public index, Black Lake artifacts, automation memory, Black-Lake-Data, and same-paper worktree markers.
- The DEP short description is 16 characters, within the 25-character limit.
- The manuscript title and H1 are identical and within 40 characters.
- Public-safe scanning excludes local paths, usernames, machine identifiers, exact timestamps, and local timezone labels.
- No source files were collected or redistributed; no `.source/` directory is present.

## Attribution Block

- Source URL: https://arxiv.org/abs/2104.08638
  - Applies to: paper identity, authors, abstract, dates, version, journal reference, and arXiv identifier.
  - Notes: Primary arXiv metadata record inspected on 2026-07-13.
- Source URL: https://fredfeng.github.io/papers/sailfish.pdf
  - Applies to: architecture, evaluation, limitations, tables, figures, conclusion, and appendices.
  - Notes: Author-hosted public paper used to cross-check the locally extracted full text.
- Source URL: https://doi.org/10.1109/SP46214.2022.9833721
  - Applies to: publisher DOI, venue, pagination, and publication identity.
  - Notes: IEEE conference version identifier.
- Source URL: https://seclab.cs.ucsb.edu/publications/priyanka_sailfish_22/
  - Applies to: institutional publication metadata and author/venue confirmation.
  - Notes: UCSB SecLab publication record.
- Source URL: https://github.com/ucsb-seclab/sailfish
  - Applies to: released code/data availability and documented Docker/test workflow.
  - Notes: Official repository inspected but not executed.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260702-Tech%20Intel%201102/daily_research_findings_2026-07-02_1102.md
  - Applies to: Antaeus related-entry synthesis.
  - Notes: Existing DEP artifact, cross-checked with https://arxiv.org/abs/2607.01138.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260626-Tech%20Intel%201103/daily_research_findings_2026-06-26_1103.md
  - Applies to: Chai related-entry synthesis.
  - Notes: Existing DEP artifact, cross-checked with https://arxiv.org/abs/2606.26933.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260706-Tech%20Intel%200104/daily_research_findings_2026-07-06_0104.md
  - Applies to: VeriChat related-entry synthesis.
  - Notes: Existing DEP artifact, cross-checked with https://arxiv.org/abs/2607.01668.
