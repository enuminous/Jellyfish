import unittest
from jellyfish import Node, Edge, JellyfishSystem

class TestJellyfish(unittest.TestCase):
    def test_failure_propagates(self):
        nodes = {"A":Node(0.5), "B":Node(1.0)}
        edges = [Edge("A","B",0.5)]
        s = JellyfishSystem(nodes, edges, alpha=1.0)
        s.step()
        self.assertLess(s.nodes["B"].health, 1.0)

    def test_stress_increases_dynamic_weight(self):
        e = Edge("A","B",0.1,0.5)
        s = JellyfishSystem({"A":Node(),"B":Node()}, [e])
        self.assertGreater(s.dynamic_weight(e,1.0), s.dynamic_weight(e,0.0))

    def test_no_edge_no_propagation(self):
        nodes = {"A":Node(0.5), "B":Node(1.0)}
        s = JellyfishSystem(nodes, [], alpha=1.0)
        s.step()
        self.assertEqual(s.nodes["B"].health, 1.0)

if __name__ == "__main__":
    unittest.main()
