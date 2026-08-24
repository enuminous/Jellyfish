# JELLYFISH Architecture

## Pipeline

1. Node/Edge Ingestor
2. Dependency Graph Builder
3. Stress-Conditioned Edge Engine
4. Propagation Simulator
5. Cascade Analyzer
6. Harm Aggregator
7. Critical-Path Detector
8. Recovery Bottleneck Analyzer
9. Audit Reporter

## Inputs

- node health
- dependency edges
- stress state
- edge confidence
- severity weights
- repair/recovery actions

## Outputs

```json
{
  "systemic_harm": 1.82,
  "cascade_fraction": 0.43,
  "amplification_factor": 3.7,
  "critical_nodes": ["B", "D"],
  "critical_edges": [["A","B"],["B","D"]],
  "latent_links_activated": 2
}
```

## Design principle

JELLYFISH should preserve causal attribution of propagated harm.

A system-level score without a path explanation is insufficient.

## Integration

WOLF can feed early degradation signals into JELLYFISH.

ELEPHANT can preserve historical cascade and recovery traces.

CHAMELEON can compare dependency behavior across environments.

MAGPIE can audit evidence for inferred dependency links.
