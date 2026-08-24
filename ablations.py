from jellyfish import Node, Edge, JellyfishSystem

def run(dynamic=True):
    nodes = {
        "A": Node(health=0.55),
        "B": Node(),
        "C": Node(),
        "D": Node(),
    }
    gain = 0.5 if dynamic else 0.0
    edges = [
        Edge("A","B",0.10,gain),
        Edge("B","C",0.10,gain),
        Edge("C","D",0.10,gain),
    ]
    sys = JellyfishSystem(nodes, edges, alpha=0.8)
    initial = sys.systemic_harm()
    sys.simulate(6, stress=1.0)
    final = sys.systemic_harm()
    return final/(initial+1e-9)

if __name__ == "__main__":
    print("full dynamic amplification:", run(True))
    print("no stress-conditioned edges:", run(False))
