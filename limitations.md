# Limitations and Falsification

JELLYFISH is an experimental dependency and cascade framework.

## Limitations

- Correlation can be mistaken for dependency.
- Edge weights may be poorly identified.
- Dynamic topology can overfit sparse incidents.
- Cascade simulation may be sensitive to update rules.
- Hidden dependencies may be unobservable before failure.
- Harm severity weights are partly normative.

## Falsification criteria

JELLYFISH's central hypothesis is weakened if:

1. Static graph metrics perform equally well.
2. Stress-conditioned edges do not improve held-out cascade prediction.
3. Removing nonlinear propagation has no effect.
4. Latent-link detection fails replication.
5. The model only succeeds with post-failure information.
6. Claimed critical paths are unstable to small parameter changes.

## Claim boundary

JELLYFISH estimates dependency risk under a configured model. It does not establish real-world causation without external evidence.
