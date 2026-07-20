# DEP-E-20260720-Context Backdoor

#agent-security #embodied-agents #backdoor-defense #provenance #least-privilege #runtime-safety #research-review

Public-safe context: job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P05`, uniformly selected `arXiv:2408.02882v1`. The PDF-only archive unit was repaired with verified official full-paper HTML before defensive synthesis. Local paths, exact execution times, and source documents are withheld.

## Contents

- `README.md` - context, inventory, safety boundary, synthesis, and attribution.
- `context_backdoor_defense_manuscript.md` - schema-complete defensive review of contextual supply-chain risk, evidence, layered mitigations, and related DEP synthesis.

No `.source/` exists. No attack prompt, trigger, poisoned example, exploit code, payload, reproduction procedure, PDF, HTML, dataset, model, cache, or extracted source text is deposited.

## Summary of Items

The paper reports that contextual demonstrations can alter generated programs and condition downstream embodied-agent behavior. Tested prompt and program filters detected only 10% and 5% of selected cases; full-code human access improved detection to 65%; and a behavior interlock reduced reported attack success from 95% to 25% with a 10-point clean-accuracy cost. The manuscript treats these as small, author-run defense results rather than universal rates.

## Insights and Relevance

The defensible product insight is a layered execution boundary: signed context provenance, approved retrieval, complete dependency visibility, sandboxed program compilation, least privilege, simulation, independent invariants, and emergency stops. Agent Memory Forensics, Control Surfaces, and Memory Defense Layers supply complementary trace, intervention-placement, provenance, and authority patterns.

## Attribution Block

- https://arxiv.org/abs/2408.02882 - canonical metadata and source locators.
- https://arxiv.org/html/2408.02882 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2408.02882 - verified primary PDF; local copy withheld.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics - related trace-forensics DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260715-Control%20Surfaces - related control-placement DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Memory%20Defense%20Layers - related provenance/authority DEP.
- Source files: verified PDF, full-paper HTML, metadata HTML, and integrity records; all withheld locally with zero source-document uploads.
