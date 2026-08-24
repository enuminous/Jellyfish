from jellyfish import Node, Edge, JellyfishSystem

nodes = {
    "database": Node(health=0.65, severity=1.5),
    "api": Node(health=1.0, severity=1.2),
    "billing": Node(health=1.0, severity=1.4),
}

edges = [
    Edge("database","api",base_weight=0.2,stress_gain=0.4),
    Edge("api","billing",base_weight=0.15,stress_gain=0.5),
]

system = JellyfishSystem(nodes, edges, alpha=0.7)

for t, state in enumerate(system.simulate(5, stress=0.8)):
    print("step", t, state)
