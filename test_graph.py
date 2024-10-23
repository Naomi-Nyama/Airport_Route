from graph import AirlineGraph
import unittest


# Helper function to create a graph from routes
def createGraph(routes):
    graph = AirlineGraph()
    for origin, destination in routes:
        graph.add_edge(origin, destination)
    return graph

class TestGraphMethods(unittest.TestCase):
    
    def test_empty_graph(self):
        """Test the behavior when the graph is empty."""
        graph = createGraph([])
        self.assertEqual(len(graph.vertices), 0)
        self.assertEqual(graph.kosaraju_scc(), [])
        print(f"Empty graph: {graph.min_additional_routes('A') if graph.vertices else 'N/A'} additional routes needed")

    def test_single_entry_graph(self):
        """Test a graph with a single entry (one vertex and no edges)."""
        graph = createGraph([("A", "A")])
        self.assertEqual(len(graph.vertices), 1)
        components = graph.kosaraju_scc()
        self.assertEqual(len(components), 1)
        self.assertIn("A", components[0])
        routes_needed = graph.min_additional_routes("A")
        print(f"Single entry graph: {routes_needed} additional routes needed")
        self.assertEqual(routes_needed, 0)

    def test_circular_graph(self):
        """Test a graph that has a circular path."""
        routes = [("A", "B"), ("B", "C"), ("C", "A")]
        graph = createGraph(routes)
        self.assertEqual(len(graph.vertices), 3)
        components = graph.kosaraju_scc()
        self.assertEqual(len(components), 1)
        self.assertSetEqual(components[0], {"A", "B", "C"})
        routes_needed = graph.min_additional_routes("A")
        print(f"Circular graph: {routes_needed} additional routes needed")
        self.assertEqual(routes_needed, 0)

    def test_disconnected_graph(self):
        """Test a graph that has disconnected components."""
        routes = [("A", "B"), ("C", "D")]
        graph = createGraph(routes)
        self.assertEqual(len(graph.vertices), 4)
        components = graph.kosaraju_scc()
        self.assertEqual(len(components), 4)
        routes_needed = graph.min_additional_routes("A")
        print(f"Disconnected graph: {routes_needed} additional routes needed")
        self.assertEqual(routes_needed, 1)  
    

if __name__ == '__main__':
    unittest.main()