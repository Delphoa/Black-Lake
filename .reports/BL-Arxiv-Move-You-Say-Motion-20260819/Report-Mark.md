# Report-Mark: Move You Say Motion

## Source Metadata

| Field | Value |
| --- | --- |
| Title | Move as You Say, Interact as You Can: Language-guided Human Motion Generation with Scene Affordance |
| Authors | Zan Wang, Yixin Chen, Baoxiong Jia, Puhao Li, Jinlu Zhang, Jingze Zhang, Tengyu Liu, Yixin Zhu, Wei Liang, Siyuan Huang |
| arXiv | 2403.18036v1 |
| DOI | 10.48550/arXiv.2403.18036 |
| Publication context | CVPR 2024 |
| Review basis | Verified local PDF and full-paper HTML plus public arXiv, project, and official code references |
| Source handling | Source files and derived caches withheld locally; no source files uploaded |

## Concise Research Notes

The paper addresses language-guided human motion generation in a 3D scene. Its central design is an explicit scene-affordance representation that connects language, geometry, and motion before motion synthesis. The Affordance Map Diffusion Model predicts a spatial-temporal affordance map, while the Affordance-aware Motion Diffusion Model uses that map to generate SMPL-X motion. Evaluation spans HumanML3D, HUMANISE, and a novel-scene set. The results suggest improved scene-aware contact and goal behavior on the reported benchmarks, while failure cases show that semantic and geometric plausibility can still diverge for unseen interactions or complex descriptions.

## Evidence Ledger

| ID | Evidence | Basis |
| --- | --- | --- |
| E1 | The system uses a two-stage affordance-map and motion-diffusion design. | Official full-paper method sections |
| E2 | The affordance map is derived from distances between scene points and motion joints, with temporal max pooling. | Official full-paper formulation |
| E3 | HumanML3D, HUMANISE, and a novel-scene set are used for evaluation. | Official full-paper datasets and experiments |
| E4 | HUMANISE reports goal distance 0.156, contact 95.86, and non-collision 99.69 for the encoder-conditioned configuration. | Official full-paper result table |
| E5 | The novel-scene split lacks ground-truth motions and reports weaker quality and action scores than established benchmarks. | Official full-paper novel-scene evaluation |
| E6 | Failure cases include unseen human-scene interactions and complex descriptions; diffusion inference is slower. | Official full-paper limitations and failure analysis |

## Related DEP Entries

1. [AR-Drag Motion](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260720-AR-Drag%20Motion) — motion control and sequence responsiveness provide a deployment-oriented comparison for language-conditioned motion.
2. [Habitat Synthetic Scenes](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260724-Habitat%20Synthetic%20Scenes) — scene scale and realism frame the data-coverage constraints of affordance learning.
3. [NaLA A 3D Native LLM](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260809-NaLA%20A%203D%20Native%20LLM) — native 3D language grounding provides a conceptual bridge to spatial intermediate representations.

## Synthesis Note

### Concept Bridge

The paper turns a difficult multimodal contract into an explicit affordance map: language identifies an intended interaction, scene geometry supplies possible locations, and motion must satisfy both. This intermediate interface connects naturally to AR-Drag's controllable temporal motion, Habitat's need for broad and realistic scene coverage, and NaLA's language-to-3D spatial grounding. The shared lesson is that an auditable spatial state can make an end-to-end generator easier to evaluate and integrate.

### Potential Implementations

1. A scene-aware motion authoring service that converts a natural-language instruction into candidate affordance maps, motion clips, and contact/collision diagnostics.
2. An affordance annotation quality gate that checks whether language, scene regions, and joint trajectories agree before a motion sample enters a training set.
3. A human-in-the-loop simulation controller that lets an operator select, edit, or reject affordance maps before expensive diffusion sampling.

### Deeper Relationship Observations

1. An explicit affordance map is a reusable contract: it can mediate training, debugging, human correction, and downstream evaluation rather than serving only as an internal tensor.
2. Scene diversity and motion diversity are coupled: a motion model may appear strong on familiar furniture while failing when geometry, viewpoint, or interaction affordance shifts.
3. Spatial grounding and temporal generation should expose separate state and failure signals, because a good-looking sequence can still target the wrong object or contact region.

### Conceptual Similarities

1. The four sources use intermediate structure to make multimodal reasoning more inspectable: affordance maps, controllable motion states, scene assets, or native 3D layouts.
2. Each source separates reported benchmark performance from deployment reliability, where latency, coverage, or unseen configurations become decisive.
3. Each source benefits from bounded representations of the environment, making data provenance and evaluation scope part of the system contract.

### MVP Implementations with Code Mock-ups

1. Affordance map construction for a scene-motion pair:

~~~python
def affordance_map(scene_points, joint_points, sigma=0.8):
    distances = pairwise_l2(scene_points, joint_points)
    joint_scores = exp(-0.5 * distances / (sigma ** 2))
    return temporal_max_pool(joint_scores)
~~~

2. Candidate motion generation with explicit grounding checks:

~~~python
def propose_motion(text, scene, adm, amdm, max_candidates=4):
    maps = adm.sample(text=text, scene=scene, count=max_candidates)
    clips = [amdm.sample(text=text, scene=scene, affordance=m) for m in maps]
    return rank_by_goal_contact_collision(clips, maps)
~~~

3. An evaluation record that preserves semantic and geometric signals separately:

~~~python
def evaluation_record(reference, candidate, contact, collision):
    return {
        "semantic_match": score_text_motion(reference, candidate),
        "goal_distance": measure_goal(candidate),
        "contact_rate": contact,
        "non_collision_rate": 1.0 - collision,
    }
~~~

### Developer Challenges

1. Keep the affordance representation stable across point-cloud density, coordinate frames, scene scale, and missing geometry.
2. Expose stage-specific diagnostics so a failure can be attributed to language grounding, affordance prediction, or motion decoding.
3. Bound inference latency and memory for interactive use without silently changing the evaluation protocol.

### Author Challenges

1. Clarify how much improvement comes from the explicit affordance representation versus data processing, conditioning choices, or model capacity.
2. Expand unseen-scene and unseen-interaction evaluation with ground-truth-light metrics and human judgments that distinguish wrong-object grounding from stylistic variation.
3. Report reproducibility details for data preparation, checkpoint selection, random seeds, and the public implementation path.

## Validation Notes

- The local paper unit was initially partial and was repaired before review.
- PDF and full-paper HTML passed the mandatory size, marker, structure, and integrity checks.
- The required missing-only extraction-cache pass completed with pypdf and html-regex.
- Dedup validation found no existing arXiv ID, DOI, normalized-title, slug, or 24-hour marker.
- No source files, extracted source text, or caches are included in this public report.

## Attribution Block

Primary sources: [arXiv abstract](https://arxiv.org/abs/2403.18036), [full-paper HTML](https://arxiv.org/html/2403.18036), [DOI](https://doi.org/10.48550/arXiv.2403.18036), [project page](https://afford-motion.github.io/), and [official implementation](https://github.com/afford-motion/afford-motion). Related context is linked above from the public Black Lake repository. Source files were withheld locally and no source file was uploaded.
