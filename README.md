# Airport_Graph-Exercise

This project implements a directed graph data structure to model airport routes, using Kosaraju's algorithm to find Strongly Connected Components (SCCs). The script calculates the minimum number of additional routes required to ensure all airports are reachable from a given starting airport.

# Key Features:
Graph Representation: The graph is represented using adjacency lists, with directed edges between airports.
Kosaraju's Algorithm: Used to identify Strongly Connected Components (SCCs) in the airport routes graph.
Graph Compression: After identifying SCCs, the graph is compressed into a smaller version where each SCC is a single node.
Minimum Route Calculation: The script computes the minimum number of additional routes needed to ensure all airports are reachable from a specified starting airport.
Why Kosaraju's Algorithm?
Kosaraju's algorithm was chosen for its simplicity and clarity. It separates the task of finding SCCs into two distinct phases, which aligns well with the need to compress the graph and calculate additional routes. While Tarjan's algorithm is also efficient, Kosaraju's algorithm is easier to implement and debug for this type of problem.

# How It Works:
Graph Creation: Routes between airports are added to the graph.
Strongly Connected Components: Kosaraju's algorithm is applied to find SCCs.
Graph Compression: The graph is compressed into SCCs, reducing complexity.
Route Calculation: The minimum number of additional routes is calculated for a given starting airport.

# Test Exexution and Result from the solution:
<img width="616" alt="Screenshot 2024-10-23 at 23 52 09" src="https://github.com/user-attachments/assets/50f50fcc-0248-440f-9876-1a4f68c421c1">

<img width="663" alt="Screenshot 2024-10-23 at 23 37 16" src="https://github.com/user-attachments/assets/faf32f89-77b1-4a1f-940a-ca815e47bdc0">
