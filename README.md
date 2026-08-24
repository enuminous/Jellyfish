# JELLYFISH — EFMW Zoo #28

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
