# Arxiv DEP Job Log: How to Forget FOLTR

## Job Status

- Status: complete and ready for repository submission.
- Selected paper: *How to Forget Clients in Federated Online Learning to Rank?*
- Authors: Shuyi Wang; Bing Liu; Guido Zuccon.
- Identifier: arXiv:2401.13410v1.
- Public date: 2026-08-04. Exact local execution time is intentionally withheld.

## Selection and Deduplication

- Candidate enumeration: `rg --files -g "*.pdf"` against the local arXiv archive.
- Candidate PDFs: 75,960.
- Unique parent-directory paper units: 75,957.
- Owning artifact and memory files scanned: 3,314.
- Prior unique paper identifiers found in owning trees: 1,414.
- Prior-ID unit exclusions: 545.
- Units with incomplete normalized identifiers: 0.
- Eligible units after ownership deduplication: 75,412.
- Random method: sorted eligible parent units, then uniform zero-based PowerShell `Get-Random` draw; accepted draw index 52,166.
- Diagnostic inventory-only reconciliation was discarded before the freeze because `.lists` is a metadata-only mirror and is not ownership evidence.
- Reselections after the corrected freeze: 0.
- Same-paper markers within the recent 24-hour window: 0.

## Source Integrity Gate

The selected unit initially classified as `partial`: its valid PDF existed, but a verified full-paper HTML artifact was missing. The local archive was repaired with the bounded brokered single-paper process before review. The final verification pass confirmed a PDF beginning with `%PDF-`, a trailing `%%EOF`, 2,375,508 bytes, and 17 readable pages; the full-paper HTML was 503,162 bytes with 71,491 body characters, 37 heading markers, an article/main/LaTeXML document marker, and the required paper-structure terms. The optional source archive was unavailable through the brokered request and was not needed for review. PDFs, HTML, metadata, verification records, and caches remain local and were not copied to the public repository.

## Generated Public Outputs

- `.logs/20260804-Arxiv-How-to-Forget-FOLTR-LOG.md`
- `.reports/BL-Arxiv-How-to-Forget-FOLTR-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` index attribution row.

## Related DEP Entries

Exactly three related entries were selected from existing Black-Lake DEP-E artifacts: Agent State Review for parameter-level and auditable unlearning context; SMES Expert Sparsity for online ranking and cost-aware serving; and RPDG Incremental Grad for cached component updates and explicit state/cost accounting.

## Next-Review Questions

1. Can the proposed unlearning method be independently reproduced with a public implementation and pinned experiment manifest?
2. Does the poisoning-based verification signal remain informative when the departing client is not otherwise distinguishable from its peers?
3. What privacy, deletion, and model-quality guarantees hold when stored historical updates are compressed, encrypted, or partially unavailable?

## Challenges

1. Translating an offline nDCG convergence result into an auditable, production-safe deletion guarantee without exposing client data.
2. Separating the cost of stored historical updates, recalibration, communication, and verification from the paper's main training-step comparison.
3. Designing a benign, reproducible verification harness that tests residual contribution without operationalizing poisoning against real clients.

## Submission Gate

Before commit, the staged allowlist must contain only generated Markdown files in `.logs`, `.reports`, `.lake-data`, and the required index row. No PDF, HTML, source archive, extracted text, cache, local path, or source-document copy may be staged. Slack notification is sent only after a successful repository push.
