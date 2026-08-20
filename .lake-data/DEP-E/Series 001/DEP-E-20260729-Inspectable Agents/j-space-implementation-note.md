---
title: "J-Space Implementation Note"
artifact_id: "DEP-E-JSPACE-IMPLEMENTATION-20260729"
dep_class: "DEP-E"
profile_id: "j-space-workspace-20260729"
record_object_type: "implementation note"
source_scope: "J-space research only"
implementation_status: "bounded research design; not production guidance"
generated_at: "2026-07-29"
---

# J-Space Implementation Note

## Objective

Design a reproducible, local-only harness for studying Jacobian-lens readouts and interventions on an authorized open model. The first implementation must test the method, not deploy a monitor.

## System Boundary

In scope:

- one pinned open model;
- public or synthetic prompts;
- layer-wise averaged Jacobian fitting;
- token-direction readouts and sparse decompositions;
- swaps, clamping, and matched random controls;
- immutable run receipts and exported evidence packets.

Out of scope:

- proprietary-model reproduction;
- real-user data;
- production traffic;
- intent, deception, or consciousness classification;
- autonomous access control or enforcement;
- storing raw chain-of-thought or hidden states beyond the local research run.

## Proposed Architecture

```text
public/synthetic tasks
        |
        v
  model adapter ---- model/version hash
        |
        +----> Jacobian fitter ---- lens manifest
        |
        +----> task runner -------- behavioral baseline
                         |
                         v
                 readout + intervention
                         |
                         v
              controls / effect estimator
                         |
                         v
               evidence packet exporter
```

## Core Records

| Record | Required fields |
|---|---|
| Model manifest | model identifier, revision, tokenizer, dtype, device class, dependency lock hash |
| Lens manifest | layer, prompt-set digest, source/target position policy, averaging rule, normalization, build seed |
| Task record | task family, public/synthetic source, expected intermediate, expected answer, split |
| Intervention record | direction, magnitude, layer/position, operation, matched control, clamp set |
| Result record | baseline output, intervention output, ranking, effect, uncertainty, failure state |
| Evidence packet | claim, linked records, reviewer assessment, limitations, reproducibility receipt |

## Implementation Phases

### Phase 0: Contract tests

- Pin dependencies and model revision.
- Confirm deterministic tokenization and task fixtures.
- Verify Jacobian shape, normalization, and serialization.
- Fail closed on missing hashes or schema fields.

### Phase 1: Readout baseline

- Fit a small lens on public text.
- Compare token rankings with logit-lens and random-map baselines.
- Measure stability across seeds and prompt subsamples.
- Do not proceed if rankings are unstable or controls perform equivalently.

### Phase 2: Causal toy tasks

- Use synthetic two-hop and arithmetic tasks with known intermediates.
- Run dose-controlled swaps and matched random directions.
- Clamp candidate coordinates to test mediation.
- Report all trials, including intervention failures.

### Phase 3: Workspace tests

- Compare report-required and automatic variants of the same property.
- Estimate sparse occupancy and effect by normalized layer.
- Pre-register the layer-band rule on a discovery split and freeze it for confirmation.

### Phase 4: Audit research

- Use synthetic, clearly labeled scenarios only.
- Require a behavior-first trigger and human-selected causal test.
- Export evidence packets; never emit an automated intent label.

## Acceptance Tests

| Test | Pass condition |
|---|---|
| Rebuild stability | Repeated lens builds meet a predeclared similarity tolerance |
| Control separation | Candidate directions outperform matched random controls with uncertainty reported |
| Mediation | Clamping changes the residual-component effect in the predicted direction |
| Negative-result retention | Failed and null trials appear in exports and aggregate metrics |
| Provenance completeness | Every result resolves to model, lens, task, and intervention manifests |
| Privacy boundary | No real-user prompts or persistent raw activations are present |
| Claim discipline | Export labels distinguish source result, reproduction result, and reviewer inference |

## Stop Conditions

- Lens construction cannot be reproduced from the recorded manifest.
- Candidate effects do not separate from matched controls.
- Results depend on post-hoc layer or task selection.
- Hidden-state retention exceeds the approved local research boundary.
- Reviewers begin treating readouts as ground-truth intent labels.
- Model or dataset licensing is incompatible with the proposed work.

## Dependencies and Provenance

The official repository declares Python 3.10+, PyTorch, Hugging Face Hub, Transformers 5.5+, and NumPy for `jlens` 0.1.0. A new implementation should inspect and pin the exact current dependency graph before execution. This profile inspected the repository but did not install or run it.

## Verification Backlog

1. Reconstruct the repository's documented minimal example on synthetic input.
2. Add schema validation for every core record.
3. Freeze a public task suite and random-direction baseline.
4. Reproduce at least one qualitative readout and one causal toy result.
5. Publish aggregate receipts without model weights, raw activations, or restricted prompts.

## Sources

- Primary method and reported controls: https://transformer-circuits.pub/2026/workspace/index.html
- Official implementation: https://github.com/anthropics/jacobian-lens
- Package metadata: https://github.com/anthropics/jacobian-lens/blob/main/pyproject.toml
- License: https://github.com/anthropics/jacobian-lens/blob/main/LICENSE
