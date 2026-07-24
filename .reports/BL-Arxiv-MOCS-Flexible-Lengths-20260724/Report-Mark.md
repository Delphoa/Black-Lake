# Report-Mark: MOCS Flexible Lengths

Public-safe run date: 2026-07-24

## Source Metadata

| Field | Value |
|---|---|
| Title | How to Construct Mutually Orthogonal Complementary Sets with Non-Power-of-Two Lengths? |
| Authors | Shing-Wei Wu; Chao-Yu Chen; Zilong Liu |
| Stable identifier | arXiv:2003.06991v1 |
| arXiv submitted | 2020-03-16 |
| Manuscript chronology | Received 2019-10-15; accepted 2020-02-14 |
| Published record | *IEEE Transactions on Information Theory* 67(6), 3464-3472, June 2021 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2003.06991 |
| IEEE DOI | https://doi.org/10.1109/TIT.2020.2980818 |
| Primary record | https://arxiv.org/abs/2003.06991 |
| Full paper | https://arxiv.org/pdf/2003.06991 and https://ar5iv.labs.arxiv.org/html/2003.06991 |
| Official code | No paper-specific official implementation was located in the inspected primary records or targeted public search |
| Source integrity | Initially partial; repaired to verified complete before review |
| Distribution boundary | Source documents, renderings, and private processing records were withheld; public URLs only |

## Concise Research Notes

### Problem

A mutually orthogonal complementary set is parameterized as `(M,N,L)`: `M` complementary sequence sets, `N` constituent sequences per set (the flock size), and sequence length `L`. The universal bound is `M <= N`; equality is a complete complementary code. Generalized-Boolean-function constructions were strongest at power-of-two lengths, leaving flexible non-power-of-two lengths with large `M` as the paper's target.

### Method

The paper represents `q`-ary sequences through generalized Boolean functions over binary variables. Theorem 3 partitions variables into ordered chains, adds quadratic terms along each chain, truncates the length-`2^m` GBF sequence to `L = 2^(m-1) + 2^t`, and applies structured linear offsets to construct a Golay complementary set.

Theorem 4 creates several mutually orthogonal GCSs by adding offsets at chain endpoints. Corollary 5 introduces a branch term that depends on the last binary variable and expands the set family to `M = 2^k` with flock size `N = 2^(k+1)`, hence `M/N = 1/2`. The appendices prove the zero autocorrelation and cross-correlation sums through index pairing, cancellation, and a Hamming-weight argument.

### Evidence and Results

The evidence is constructive and theorem-based. Example 1 produces `(8,36)` and `(8,40)` GCSs and identifies the latter as outside one earlier construction. Example 2 gives `(2,8,40)` and `(2,8,48)` MOCSs under Theorem 4. Examples 3 and 4 use Corollary 5 to give `(4,8,48)` and `(8,16,48)` MOCSs.

Table I compares availability for set sizes 4, 8, and 16 across selected lengths. Table II enumerates even-length `(M,N)` availability and shows that Theorem 4 may yield several ratios, while Corollary 5 fixes `M/N = 1/2`. The construction family includes non-power-of-two lengths when `1 <= t < m-1`; the boundary `t = m-1` returns a power-of-two length.

### Limitations

The review found no reference implementation, machine-checked proof, or independent enumeration of the examples. The paper does not report generation complexity, hardware measurements, PAPR, BER, radar ambiguity, or robustness under channel impairments. Its length family and partition/bijection conditions do not cover arbitrary lengths.

Two textual tensions need explicit qualification. First, the introduction defines `r = N/M` while calling it upper-bounded by one, contradicting `M <= N`; the remainder uses the coherent ratio `M/N`. Second, the abstract's "maximal achievable" half-flock wording is stronger than the inspected result: Corollary 5 constructs `M/N = 1/2`, but the paper does not establish a universal impossibility of larger ratios for all non-power-of-two MOCSs.

The prose below Table I mentions length 18, although Table I's visible length columns omit 18; length 18 appears in Table II. This is an editorial inconsistency, not a refutation of the construction.

### Implementation Relevance

The work is directly implementable as a bounded algebraic compiler: accept `q,m,k,t`, a partition, and per-block permutations; generate the q-ary sequences; and emit an exhaustive correlation certificate. Its practical promise is matching code length to non-power-of-two resource allocations while retaining exact complementary and mutual-orthogonality identities.

A credible engineering transfer must connect the formal certificate to system metrics. The related 4-adic sequence DEP adds a complexity/security lens, 2D-RC OTFS adds a geometry-aware receiver lens, and Multi-Point ISAC adds power, interference, sensing, and communications tradeoffs. Code-level orthogonality is valuable but not sufficient for deployment.

### Reviewer Interpretation

The strongest contribution is a reusable constructive proof pattern: encode a combinatorial family through GBF chains, truncate it in a controlled binary region, and pair terms so off-peak correlation cancels. Confidence is high that the paper states and proves the displayed constructions; confidence is lower in unverified transcription details and practical advantage. The half-ratio should be treated as an achieved construction ratio, not a settled global optimum.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Boundary |
|---|---|---|---|
| E1 | Complete nine-page PDF and full-paper HTML, including definitions, Theorems 3-4, Corollary 5, Examples 1-4, Tables I-II, conclusion, and appendices | Construction mechanism, formal claims, examples, limitations, and notation tensions | Proofs were reviewed but not machine-checked or independently re-derived |
| E2 | Visual inspection of all nine PDF pages | Equation layout, table structure, publication metadata, proof flow, and editorial inconsistencies | Visual inspection does not establish theorem correctness |
| E3 | arXiv metadata and version history | Title, authors, identifier, date, DOI, subject, and publisher comment | Metadata does not validate results |
| E4 | IEEE DOI plus Essex and National Cheng Kung institutional records | Published venue, volume, issue, pages, and publication month | Institutional metadata supports identity, not technical claims |
| E5 | Private integrity and process records | Uniform selection, dedup, PDF/HTML validation, and bounded repair | Local paths and source files are intentionally withheld |
| E6 | Three inspected DEP manuscripts | Sequence-complexity, wireless-receiver, and ISAC system bridges | Related DEPs do not validate this paper's theorems |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md`
   - Relevance: This DEP reviews interleaved quaternary sequences of even length with optimal autocorrelation and their 4-adic complexity. It is the closest theoretical bridge for asking whether a sequence family that satisfies correlation identities also resists short algebraic representation.
   - Source basis: The DEP reviews `arXiv:2209.10279` from a verified PDF and full-paper HTML, preserving the sequence, interleaving, autocorrelation, and complexity claims as source-reported evidence.

2. `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
   - Relevance: 2D-RC operates in the OTFS delay-Doppler domain and evaluates symbol detection under high mobility. It supplies a receiver-side complement to the selected paper's transmitter/code-side use of algebraic correlation structure for multicarrier systems.
   - Source basis: The DEP reviews `arXiv:2311.08543v2`, including delay-Doppler circular structure, pilot-based online learning, BER/BLER comparisons, and complexity limits.

3. `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
   - Relevance: Multi-Point ISAC couples radar sensing, communication rate, interference, and power allocation. It provides the system-level bridge needed to test whether a formally orthogonal sequence family improves end-to-end sensing/communications tradeoffs.
   - Source basis: The DEP reviews `arXiv:2208.07592v2`, exact and surrogate voting, functionality selection, beamforming, and a six-device ray-traced simulation.

## Synthesis Note

### Concept Bridge

The selected paper supplies an algebraic signal layer: GBF chains and structured offsets produce exact aperiodic autocorrelation cancellation within each GCS and cross-correlation cancellation across MOCS members. The 4-adic DEP asks a neighboring mathematical question about sequence complexity after interleaving. The 2D-RC DEP shifts to receiver inference and shows that performance improves when the model respects delay-Doppler geometry. The Multi-Point ISAC DEP moves to system coordination, where sensing value competes with communication rate, power, and interference.

Together they suggest a proof-carrying wireless experiment stack. A code compiler emits flexible-length sequences plus an exact correlation certificate. A channel-aware receiver evaluates recovery under matched OTFS/OFDM conditions. An ISAC allocator measures whether better correlation actually changes sensing, rate, and power tradeoffs. A sequence-complexity audit prevents a correlation-optimal family from being treated as automatically unpredictable or secure.

### Potential Implementations

1. **Flexible-length code compiler**: Generate q-ary GCS/MOCS candidates from theorem parameters and emit exact `(M,N,L)` metadata plus correlation residuals.
2. **OTFS/OFDM receiver benchmark**: Place certified flexible-length codes into a synthetic multicarrier channel and compare matched receivers, PAPR, BER/BLER, latency, and resource utilization.
3. **ISAC waveform evidence sandbox**: Compare flexible MOCSs with power-of-two CCC and paraunitary baselines under simulated radar ambiguity, sensing accuracy, rate, power, and interference constraints.

### Deeper Relationship Observations

1. Correlation, algebraic complexity, and learned detectability are distinct properties: a family can cancel aperiodic correlation exactly while still being easy to represent or poorly matched to a receiver.
2. The selected paper and 2D-RC both gain from respecting binary/circular structure, but they place that structure on opposite sides of the link: algebraic sequence generation versus geometry-aware inference.
3. Multi-Point ISAC shows why local optimality must be carried upward with evidence; a waveform-level gain can disappear when remote sensors consume power, add interference, or contribute redundant views.

### Conceptual Similarities

1. All four works replace unconstrained search with a structured design space: GBF chains, interleaving algebra, circular reservoirs, or discrete functionality allocation.
2. Each work treats interference or dependence explicitly through correlation sums, sequence complexity, delay-Doppler coupling, or multi-device SINR and voting.
3. Each contribution is most reusable when its assumptions become machine-checkable inputs and its output includes a certificate, not only a claimed optimum.

### MVP Implementations with Code Mock-Ups

#### MVP 1: Length-Family Enumerator

Enumerate the paper's admissible flexible lengths and label the power-of-two boundary.

```python
def flexible_lengths(m):
    if m < 2:
        raise ValueError("m must be at least 2")
    rows = []
    for t in range(1, m):
        length = 2 ** (m - 1) + 2 ** t
        rows.append({
            "m": m,
            "t": t,
            "length": length,
            "non_power_of_two": length & (length - 1) != 0,
        })
    return rows

assert [row["length"] for row in flexible_lengths(6)] == [34, 36, 40, 48, 64]
```

#### MVP 2: Aperiodic Correlation Checker

Compute a bounded complex correlation sum for toy q-ary sequences.

```python
import cmath

def aperiodic_correlation(left, right, shift, q):
    if q <= 1 or len(left) != len(right):
        raise ValueError("equal-length sequences and q > 1 required")
    total = 0j
    for index in range(len(left)):
        other = index + shift
        if 0 <= other < len(right):
            phase = (left[index] - right[other]) % q
            total += cmath.exp(2j * cmath.pi * phase / q)
    return total

assert abs(aperiodic_correlation([0, 0], [0, 0], 0, 2) - 2) < 1e-9
```

#### MVP 3: Proof-Carrying Catalog Record

Reject a sequence-family record unless identity, parameters, and verification residuals are complete.

```python
def catalog_record(parameters, residuals, source_urls):
    required = {"q", "m", "k", "t", "M", "N", "L"}
    missing = sorted(required - parameters.keys())
    if missing:
        raise ValueError(f"missing parameters: {missing}")
    if not source_urls or max(abs(value) for value in residuals) > 1e-9:
        raise ValueError("uncertified sequence family")
    return {
        "parameters": dict(parameters),
        "max_residual": max(abs(value) for value in residuals),
        "sources": list(source_urls),
        "status": "verified-to-tolerance",
    }
```

### Developer Challenges

1. Translate every binary-index, permutation, and truncation convention without silently reversing bit order or confusing `M/N` with the introduction's printed `N/M`.
2. Scale exact autocorrelation and cross-correlation verification beyond toy families while preserving an auditable exact or bounded numerical certificate.
3. Integrate code generation with OFDM, OTFS, and ISAC simulators under matched power, bandwidth, channel, and receiver assumptions.

### Author Challenges

1. Release a reference generator and verification suite that reproduces Examples 1-4 and Tables I-II from pinned parameters.
2. Clarify the performance-ratio notation, the Table I length-18 statement, and the scope of the abstract's "maximal achievable" wording.
3. Evaluate the constructions on hardware or a reproducible system simulator with generation cost, storage, PAPR, BER/BLER, radar ambiguity, and interference metrics.

## Validation Notes

- Uniform selection used a PowerShell `Get-Random` index over 75,777 unique PDF-parent units from 75,780 PDFs; selected zero-based index 42,505.
- No prior Arxiv DEP artifact or same-paper 24-hour marker was found. Duplicate exclusions, other exclusions, and reselections were all zero.
- The only related Black-Lake-Data hit was a metadata-only author-inventory row and did not count as prior processing.
- Source state changed from partial to complete before review. The existing PDF exceeded 10 KB, began with `%PDF-`, ended with `%%EOF`, and retained a verified SHA-256. Full-paper HTML exceeded 5 KB and 2,000 body characters, had three document markers, 51 heading markers, seven paper-structure term classes, no bad marker, and zero partials.
- The source package was not collected because the strict publisher broker rejected a changed `/e-print/` to `/src/` redirect. This did not affect the PDF-plus-full-HTML completeness gate.
- All nine PDF pages were rendered and visually inspected; equations, examples, tables, conclusion, references, and appendices were legible despite nonfatal renderer font-substitution warnings.
- Three standard-library Python mock-ups pass syntax validation.
- No experiment, proof assistant, sequence generator, or official implementation was executed.
- No source file, local path, machine name, local timezone label, or exact execution timestamp is included.

## Attribution Block

- https://arxiv.org/abs/2003.06991
  - Applies to: Source identity, title, authors, arXiv date/version, subject, abstract, public links, and DOI metadata.
- https://arxiv.org/pdf/2003.06991
  - Applies to: Complete-paper definitions, theorems, examples, tables, proof appendices, and visual inspection; local copy withheld.
- https://ar5iv.labs.arxiv.org/html/2003.06991
  - Applies to: Verified full-paper text inspection; local rendering withheld.
- https://arxiv.org/e-print/2003.06991
  - Applies to: Public source-package locator; no source package was uploaded or included.
- https://doi.org/10.48550/arXiv.2003.06991
  - Applies to: Persistent arXiv identity.
- https://doi.org/10.1109/TIT.2020.2980818
  - Applies to: Published article identity.
- https://repository.essex.ac.uk/30464/
  - Applies to: Institutional publication record and accepted-version metadata.
- https://researchoutput.ncku.edu.tw/en/publications/how-to-construct-mutually-orthogonal-complementary-sets-with-non--2/
  - Applies to: Venue, volume, issue, pages, article number, publication month, and peer-reviewed status.
- `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md`
  - Applies to: Quaternary sequence, interleaving, autocorrelation, and 4-adic-complexity bridge; source basis `https://arxiv.org/abs/2209.10279`.
- `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
  - Applies to: OTFS receiver, delay-Doppler geometry, detection, and complexity bridge; source basis `https://arxiv.org/abs/2311.08543`.
- `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
  - Applies to: Radar/communications fusion, power, interference, and functionality-selection bridge; source basis `https://arxiv.org/abs/2208.07592`.
- Source files and private integrity records
  - Applies to: Selection, repair, and source-integrity verification only; all were withheld locally and none were uploaded.
