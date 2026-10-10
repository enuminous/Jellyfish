# JELLYFISH — EFMW Zoo #28

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Jellyfish) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Joint Evaluation of Latent Links, Yield, Failure, Interdependence & Systemic Harm**

JELLYFISH is an experimental EFMW-inspired framework for mapping weak or hidden dependencies among components and estimating how local failures can propagate into system-level harm.

## Core question

> Which apparently minor local dependency becomes dangerous when the rest of the system begins to fail around it?

JELLYFISH treats dependency structure as dynamic rather than static. It tracks latent links, propagated load, failure amplification, and harm accumulation across a network.

## Primary outputs

- dependency exposure
- latent-link strength
- cascade susceptibility
- amplification factor
- critical-path concentration
- systemic harm score
- recovery bottlenecks

## Repository contents

- `theory.md`
- `architecture.md`
- `dependency_model.md`
- `limitations.md`
- `jellyfish.py`
- `benchmark.py`
- `ablations.py`
- `test_jellyfish.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_jellyfish.py
```

## Zoo position

MAGPIE #24 tracks grounding.

WOLF #25 tracks distributed precursors.

ELEPHANT #26 tracks long-memory integrity.

CHAMELEON #27 tracks context-dependent behavior.

**JELLYFISH #28 asks how hidden dependencies turn local weakness into systemic failure.**
