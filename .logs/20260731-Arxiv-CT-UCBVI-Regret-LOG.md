# Arxiv DEP Log: CT-UCBVI Regret

## Public-Safe Run Summary

- Paper: *Square-root regret bounds for continuous-time episodic Markov decision processes*.
- arXiv ID: 2210.00832v2; arXiv DOI: 10.48550/arXiv.2210.00832; publisher DOI: 10.1287/moor.2022.0283.
- Selection method: sorted unique PDF-parent units followed by a uniform PowerShell Get-Random draw.
- Candidate count: 75,960 PDFs representing 75,957 parent paper units; selected zero-based index: 70,174.
- Exclusions and reselections: 0 duplicate exclusions, 0 other exclusions, and 0 reselections; the first draw was accepted after identifier checks.
- Dedup validation: no matching arXiv ID, DOI, normalized title, slug, processed DEP artifact, or same-paper marker appeared in Black-Lake logs, reports, DEP entries, staging, automation memory, or inspected Black-Lake-Data context.
- Source integrity: initial state was partial because a valid PDF lacked full-paper HTML. A bounded brokered repair preserved the PDF and added metadata and full-paper HTML. Final validation passed the PDF header/trailer, HTML body, document-marker, heading, and paper-structure gates; no partial transfer files remained.
- Public sources: https://arxiv.org/abs/2210.00832; https://doi.org/10.48550/arXiv.2210.00832; https://doi.org/10.1287/moor.2022.0283.
- Source policy: original PDF, HTML, metadata, provenance, and receipts remain local. No source files were copied into this repository.

## Output Paths

- .logs/20260731-Arxiv-CT-UCBVI-Regret-LOG.md
- .reports/BL-Arxiv-CT-UCBVI-Regret-20260731/Report-Mark.md
- .lake-data/DEP-E/DEP-E-20260731-CT-UCBVI Regret/README.md
- .lake-data/DEP-E/DEP-E-20260731-CT-UCBVI Regret/ct_ucbvi_regret_manuscript.md
- .lake-data/DEP-E/.index/pubs-index.md

## Validation Notes

- The manuscript uses the complete required heading contract, matching compact YAML and H1 titles, an evidence ledger, three bounded exercises, an MVP specification, and public-only source locators.
- The Report-Mark records exactly three related DEP entries and exact-three synthesis, implementation, observation, similarity, developer-challenge, and author-challenge sets.
- The DEP entry contains no .source directory. The publication index adds one canonical, source-grounded row.

## Next-Review Questions

1. Does the final journal version materially change the 2023 arXiv v2 theorem statements, proof gap, or experimental presentation?
2. Can a small event-driven benchmark reproduce the predicted square-root episode scaling while measuring planning cost and numerical-integration error?
3. How can Bernstein-style value confidence be adapted to random jump counts and truncated holding times without the current loose state and horizon dependence?

## Challenges

1. The paper's source-level experiments cover one two-state maintenance example, not a benchmark suite or real operational deployment.
2. The public publisher record states that a prior-version proof gap required a substantial new argument, while the final journal full text was not inspected in this run.
3. No author-designated implementation, seeds, numerical grid specification, or full reproducibility package was located in the inspected public sources.
