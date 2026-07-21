# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP` manual explicit-paper run
- Deployment job ID: `BLAD-MANUAL-20260721-260705189`
- Deployment item ID: `BLAD-MANUAL-20260721-260705189-P01`
- Public-safe date: 2026-07-21
- Selection mode: explicit user selection; no random draw was performed
- Selected paper: *When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents*
- Identifier: `arXiv:2607.05189v1`
- URL: https://arxiv.org/abs/2607.05189v1

## Selection and Deduplication

- The user supplied the canonical paper URL directly.
- Deduplication checked arXiv base ID `2607.05189`, DOI `10.48550/arXiv.2607.05189`, normalized title, and the `Stealth-Memory-Injection` slug across current Black Lake artifacts, indexes, and the local archive summary.
- Duplicate exclusions: 0.
- Reselections: 0.
- A complete existing local bundle was reused; network download count for this run: 0.

## Source Integrity

- PDF: 2,898,185 bytes; SHA-256 `c40f26c2bc0513144e3d629a376f5ca849a5a1b762bc606c31a07fa89f6b9174`.
- Full-paper HTML: 538,354 bytes; SHA-256 `3cdc3c4ccf13ab0842b0c9a67bcc3180ec809a9994a4c8b20b9cc25e76dceb6b`.
- Abstract HTML: 44,783 bytes; SHA-256 `6bc8e256ffead499ed59b091eda25b3a4f52067de456dd51509d91975c6843f5`.
- Source archive: 3,255,483 bytes; SHA-256 `03d179cd53e813c6f90ad2d56b9a6b76b7f76405c433f5e0f750c197a65f49eb`.
- Complete-source gate passed. No `.part` files were present. Source files and extraction caches remain local.

## Research Questions

1. Which state transition lets untrusted email content acquire durable authority over later agent behavior?
2. How well do the paper's proxy objectives, held-out benchmark, transfer tests, and defense evaluations support its cross-system claims?
3. Which provenance, visibility, write-policy, retrieval-policy, and action-authorization controls can prevent or contain the reported failure mode?

## Research Challenges

1. Separate paper-reported evidence from reviewer inference while preserving exact metric denominators and model-specific results.
2. Reconstruct the full method and evaluation without redistributing operational attack payloads or making exploitation easier.
3. Assess reproducibility despite the absence of a publicly linked code, data, checkpoint, or executable experiment repository.

## Defensive Safety Boundary

The public artifacts discuss the attack only at the level needed to understand state transitions, measurement, and controls. Concrete malicious emails, trigger phrases, optimization prompts, attack templates, payloads, and step-by-step reproduction procedures are omitted.

## Public Outputs

- `.logs/20260721-Arxiv-Stealth-Memory-Injection-LOG.md`
- `.reports/BL-Arxiv-Stealth-Memory-Injection-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/stealth_memory_trust_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260717-FARMA Reasoning Poison/README.md`
2. `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md`
3. `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md`

Only generated Markdown and the deduplication JSON may be staged. Source documents, extracted text, renderings, private caches, and validation receipts remain local.
