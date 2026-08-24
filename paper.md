# JELLYFISH: Joint Evaluation of Latent Links, Yield, Failure, Interdependence & Systemic Harm

## Abstract

JELLYFISH is an experimental framework for evaluating dynamically activated dependencies and cascading harm in complex systems. It models components as a time-varying dependency graph in which edge strength may increase under stress, allowing weak or latent links to become operationally important only during degradation.

## 1. Motivation

Static dependency maps miss a common failure mode: a relationship that is harmless during normal operation can become critical under load.

JELLYFISH explicitly models this transition.

## 2. Model

System graph:

`G_t=(V,E_t)`

Node degradation:

`d_i=1-x_i`

Dynamic edge:

`w_ij(t)=w_ij^0 + lambda_ij*s(t)`

Propagated stress:

`p_j=sum_i w_ij*d_i`

Node update:

`d_j(t+1)=clip(d_j(t)+alpha*p_j,0,1)`

## 3. Metrics

- cascade fraction
- amplification factor
- systemic harm
- critical-edge concentration
- latent-link activation rate
- recovery bottleneck score

## 4. Baselines

- static dependency graph
- degree centrality
- betweenness centrality
- fault tree analysis
- reliability block diagrams
- Bayesian networks
- standard cascade models

## 5. Ablations

- remove stress-conditioned edges
- remove nonlinear propagation
- equalize all edge weights
- remove edge confidence
- randomize topology
- remove severity weighting

## 6. Falsification

If static or conventional reliability models match JELLYFISH on held-out cascade prediction under equal information access, the proposed dynamic dependency layer is not justified.

## 7. Claim boundary

JELLYFISH is a candidate systems-risk model. Simulated cascade prediction does not establish real-world causal structure without independent evidence.
