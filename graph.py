from collections import defaultdict, deque
from typing import List, Set, Dict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u: str, v: str) -> None:
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
    
    def get_transpose(self) -> 'Graph':
        transpose = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                transpose.add_edge(v, u)
        return transpose
    
    def dfs(self, v: str, visited: Set[str], collection: List[str] | Set[str] = None) -> None:
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, collection)
        if collection is not None:
            if isinstance(collection, list):
                collection.append(v)
            else:  # set
                collection.add(v)
    
    def kosaraju_scc(self) -> List[Set[str]]:
        stack = []  
        visited = set()
        

        for vertex in self.vertices:
            if vertex not in visited:
                self.dfs(vertex, visited, stack)
        
 
        transpose = self.get_transpose()
        
 
        visited.clear()
        components = []
        
       
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = set()
                transpose.dfs(vertex, visited, component)
                components.append(component)
        
        return components
    
    def compress_graph(self, components: List[Set[str]]) -> tuple['Graph', Dict[str, int]]:
        compressed = Graph()
        vertex_to_component = {}
        

        for i, component in enumerate(components):
            for vertex in component:
                vertex_to_component[vertex] = i
        
    
        for u in self.graph:
            u_component = vertex_to_component[u]
            for v in self.graph[u]:
                v_component = vertex_to_component[v]
                if u_component != v_component:
                    compressed.add_edge(str(u_component), str(v_component))
        
        return compressed, vertex_to_component
    
    def min_additional_routes(self, start: str) -> int:
   
        components = self.kosaraju_scc()
        

        compressed_graph, vertex_to_component = self.compress_graph(components)
        
   
        start_component = str(vertex_to_component[start])
    
        in_degrees = defaultdict(int)
        for u in compressed_graph.graph:
            for v in compressed_graph.graph[u]:
                in_degrees[v] += 1
        
        count = 0
        for component in compressed_graph.vertices:
            if component != start_component and in_degrees[component] == 0:
                count += 1
        
        return count
    
graph = Graph()
    
routes = [
         ("DSM", "ORD"), 
    ("ORD", "BGI"), 
    ("BGI", "LGA"),
    ("JFK", "LGA"),
    ("ICN", "JFK"),
    ("HND", "JFK"),
    ("HND", "ICN"),
    ("EWR", "HND"),
    ("SFO", "DSM"),
    ("LHR", "SFO"),
    ("EYW", "LHR"),
    ("SFO", "SAN"),
    ("SAN", "EYW"),
    ("EWR", "HND"),
    ("TLV", "DEL"), ("DEL", "DOH"), 
    ("DEL", "CDG"), ("CDG", "BUD"), ("CDG", "SIN"),("SIN", "CDG")
    ]
    
   
for origin, destination in routes:
        graph.add_edge(origin, destination)
    

print("1. Graph Structure:")
print("Number of airports:", len(graph.vertices))
print("Airports:", sorted(list(graph.vertices)))
print("\nExisting routes:")
for origin in sorted(graph.graph.keys()):
        for destination in sorted(graph.graph[origin]):
            print(f"{origin} -> {destination}")
    

print("\n2. Strongly Connected Components:")
components = graph.kosaraju_scc()
for i, component in enumerate(components):
        print(f"Component {i + 1}: {sorted(list(component))}")
    
 
start_airports = ["EYW", "DSM", "SFO", "TLV"]
for start in start_airports:
        result = graph.min_additional_routes(start)
        print(f"From {start}: {result} additional routes needed")


