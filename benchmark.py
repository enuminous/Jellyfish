from jellyfish import Node, Edge, JellyfishSystem

def build(stress=0.0):
    nodes = {
        "A": Node(health=0.55, severity=1.0),
        "B": Node(health=1.0, severity=1.2),
        "C": Node(health=1.0, severity=0.8),
        "D": Node(health=1.0, severity=1.5),
        "E": Node(health=1.0, severity=1.1),
    }
    edges = [
        Edge("A","B",0.10,0.45),
        Edge("A","C",0.05,0.35),
        Edge("B","D",0.15,0.50),
        Edge("C","D",0.10,0.45),
        Edge("D","E",0.12,0.55),
    ]
    sys = JellyfishSystem(nodes, edges, alpha=0.8)
    initial = sys.systemic_harm()
    hist = sys.simulate(steps=6, stress=stress)
    final = sys.systemic_harm()
    return {
        "stress": stress,
        "initial_harm": initial,
        "final_harm": final,
        "amplification": final/(initial+1e-9),
        "history": hist,
    }

if __name__ == "__main__":
    for s in [0.0,0.5,1.0]:
        r = build(s)
        print({
            "stress": r["stress"],
            "initial_harm": r["initial_harm"],
            "final_harm": r["final_harm"],
            "amplification": r["amplification"]
        })
