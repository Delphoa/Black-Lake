# DEP-E-20260730-MCPWorld Benchmark

#arxiv #computer-use-agents #mcp #benchmark #evaluation #research

This DEP-E preserves a public-safe, source-grounded review of MCPWorld. The reviewed paper's source documents were verified locally and are withheld from this public deposit; only a derived manuscript and public locators are included.

## Contents

- `mcpworld_manuscript.md` — schema-complete manuscript review of MCPWorld, including evidence, limitations, implementation implications, and related DEP synthesis.

## Summary of Items

`mcpworld_manuscript.md` records the paper's white-box evaluation design for GUI, MCP/API, and hybrid computer-use agents. It separates author-reported benchmark results from reviewer interpretation, records source-integrity and dedup validation, and provides bounded implementation paths for reproducible agent evaluation.

## Insights and Relevance

MCPWorld connects computer-use benchmarking with a practical observability problem: task success should be tied to an auditable application-state event rather than only surface UI matching or a self-reported completion signal. Its reported hybrid advantage is useful evidence for tool-plus-GUI evaluation, but it is bounded by one dated agent configuration, the completeness of the MCP tool surface, and white-box application access. The related Black Lake entries add state-trace, reliability-gate, and benchmark-governance perspectives that make the result more useful for future evaluator design.

## Attribution Block

- Source URL: https://arxiv.org/abs/2506.07672
  - Applies to: `mcpworld_manuscript.md`.
  - Notes: Canonical paper identity, authors, date, category, license locator, DOI, and official-code locator.
- Source URL: https://arxiv.org/html/2506.07672
  - Applies to: `mcpworld_manuscript.md`.
  - Notes: Full-paper evidence for the method, benchmark composition, experiments, results, limitations, and appendices.
- Source URL: https://github.com/SAAgent/MCPWorld
  - Applies to: `mcpworld_manuscript.md`.
  - Notes: Official implementation availability and MIT-license context; no code was executed.
- Source file: Withheld locally
  - Applies to: all files in this DEP.
  - Notes: No PDF, HTML, source archive, cache, extracted text, receipt, or other original source file was uploaded.
