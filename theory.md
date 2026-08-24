# JELLYFISH Theory

## 1. Problem

Complex systems frequently contain dependencies that are:
- indirect,
- weak in normal operation,
- hidden by redundancy,
- activated only under stress,
- visible only after multiple components degrade.

Static topology alone is not enough.

JELLYFISH models dependency activation and harm propagation over time.

## 2. System graph

Let:

`G_t = (V, E_t)`

where vertices are components and weighted edges represent dependency strength.

Each edge has:

`e_ij(t) = (w_ij, latency_ij, confidence_ij, activation_ij)`

## 3. Component state

Each node has state:

`x_i(t) in [0,1]`

where:
- `1` = fully healthy
- `0` = failed

Define local degradation:

`d_i(t) = 1 - x_i(t)`

## 4. Propagated stress

Candidate propagated stress on node `j`:

`p_j(t) = sum_i w_ij(t) * d_i(t)`

A nonlinear activation may be applied:

`a_j(t) = sigmoid(k*(p_j(t)-theta_j))`

## 5. Latent-link activation

A link may be weak during normal operation and strengthen under stress:

`w_ij(t) = w_ij^0 + lambda_ij * s(t)`

where `s(t)` is a global or local stress indicator.

This is a key JELLYFISH mechanism: topology effectively changes under load.

## 6. Cascade susceptibility

For an initial failure set `F0`, define:

`C = failed_or_degraded_after_T / |V|`

or severity-weighted equivalent.

## 7. Amplification factor

Let direct initial harm be `H0`.

Let total downstream harm be `HT`.

`A = HT / (H0 + eps)`

High `A` indicates strong cascade amplification.

## 8. Critical-path concentration

If most propagated harm passes through a few edges, define concentration:

`K = sum_e p_e^2`

where `p_e` is normalized propagated harm contribution.

High concentration indicates brittle dependency structure.

## 9. Systemic harm

A candidate harm functional:

`H_t = sum_i severity_i * d_i(t) + beta * cascade_risk_t + gamma * recovery_cost_t`

## 10. EFMW interpretation

The EFMW-inspired layer is relational recursion across dynamically changing dependencies.

The system does not evaluate isolated failures. It asks how one local disturbance changes the conditions under which other dependencies become important.

## 11. Falsifiable prediction

JELLYFISH should add value when:
- dependencies are latent,
- topology changes under stress,
- multiple weak links interact,
- cascades are nonlinear,
- recovery is path-dependent.

If static graph centrality and standard reliability models capture the same failures, JELLYFISH adds no justified complexity.
