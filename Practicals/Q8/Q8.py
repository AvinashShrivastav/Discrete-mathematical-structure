# Write a Program to accept a directed graph G and compute the in-degree and out-degree
# of each vertex.


def compute_degrees(graph):
    degrees = {}
    
    # Initialize degrees dictionary with all vertices
    for vertex in graph:
        degrees[vertex] = {'in_degree': 0, 'out_degree': 0}
    
    # Compute in-degree and out-degree for each vertex
    for vertex in graph:
        for adjacent_vertex in graph[vertex]:
            # Increment out-degree of the current vertex
            degrees[vertex]['out_degree'] += 1
            # Increment in-degree of the adjacent vertex
            degrees[adjacent_vertex]['in_degree'] += 1
    
    return degrees

# Example usage
graph = {
    'A': ['B', 'C', 'D'],  # Vertex A has outgoing edges to B, C, D
    'B': ['C', 'D'],       # Vertex B has outgoing edges to C, D
    'C': ['D'],            # Vertex C has an outgoing edge to D
    'D': []                # Vertex D has no outgoing edges
}

degrees = compute_degrees(graph)
for vertex in degrees:
    in_degree = degrees[vertex]['in_degree']
    out_degree = degrees[vertex]['out_degree']
    print(f"Vertex {vertex}: In-Degree = {in_degree}, Out-Degree = {out_degree}")
