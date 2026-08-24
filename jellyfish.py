from dataclasses import dataclass
from typing import Dict, List, Tuple
import math

@dataclass
class Node:
    health: float = 1.0
    severity: float = 1.0
    recovery_cost: float = 0.0

@dataclass
class Edge:
    source: str
    target: str
    base_weight: float
    stress_gain: float = 0.0
    confidence: float = 1.0

class JellyfishSystem:
    def __init__(self, nodes: Dict[str, Node], edges: List[Edge], alpha: float = 0.5):
        self.nodes = nodes
        self.edges = edges
        self.alpha = alpha

    @staticmethod
    def clip(x):
        return max(0.0, min(1.0, x))

    def dynamic_weight(self, edge: Edge, stress: float):
        return max(0.0, edge.base_weight + edge.stress_gain * stress) * edge.confidence

    def step(self, stress: float = 0.0):
        degradation = {k: 1.0 - n.health for k,n in self.nodes.items()}
        incoming = {k: 0.0 for k in self.nodes}
        edge_flow = {}

        for e in self.edges:
            w = self.dynamic_weight(e, stress)
            flow = w * degradation[e.source]
            incoming[e.target] += flow
            edge_flow[(e.source,e.target)] = flow

        new_health = {}
        for name,node in self.nodes.items():
            new_deg = self.clip(degradation[name] + self.alpha * incoming[name])
            new_health[name] = 1.0 - new_deg

        for name,h in new_health.items():
            self.nodes[name].health = h

        return {
            "degradation": {k:1.0-v for k,v in new_health.items()},
            "edge_flow": edge_flow,
            "systemic_harm": self.systemic_harm()
        }

    def systemic_harm(self):
        return sum((1.0-n.health)*n.severity + n.recovery_cost*(1.0-n.health)
                   for n in self.nodes.values())

    def simulate(self, steps: int = 5, stress: float = 0.0):
        history = []
        for _ in range(steps):
            history.append(self.step(stress))
        return history

    def critical_edges(self, top_n=3):
        flows = []
        degradation = {k:1.0-n.health for k,n in self.nodes.items()}
        for e in self.edges:
            f = e.base_weight * degradation[e.source] * e.confidence
            flows.append(((e.source,e.target), f))
        flows.sort(key=lambda x:x[1], reverse=True)
        return flows[:top_n]
