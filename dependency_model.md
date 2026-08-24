# Dependency Model

## Node schema

```json
{
  "id": "service-A",
  "health": 0.92,
  "severity": 1.3,
  "recovery_cost": 0.4
}
```

## Edge schema

```json
{
  "source": "service-A",
  "target": "service-B",
  "base_weight": 0.25,
  "stress_gain": 0.40,
  "activation_threshold": 0.5,
  "confidence": 0.85
}
```

## Dynamic edge weight

`w_ij(t) = base_weight + stress_gain * stress(t)`

## Node update

A simple reference rule:

`d_j(t+1) = clip(base_j + alpha * propagated_j, 0, 1)`

where propagated stress depends on upstream degradation.

## Hidden link test

A latent link is operationally interesting when:

`effect_under_low_stress ≈ 0`

but:

`effect_under_high_stress > threshold`

## Cascade metric

For perturbation `P`:

`Cascade(P) = total degradation after horizon / initial perturbation magnitude`

## Recovery bottleneck

After repair input `r_i(t)`, compare expected versus actual restoration rate.

Persistent downstream drag indicates a recovery dependency.
