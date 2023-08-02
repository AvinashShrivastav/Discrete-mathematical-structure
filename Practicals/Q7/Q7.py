# Write a Program to check if a given graph is a complete graph. Represent the graph using
# the Adjacency List representation.

def is_complete_graph(adjacency_list):
    num_vertices = len(adjacency_list)
    
    # Check if each pair of vertices is connected
    for i in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if i != j and j not in adjacency_list[i]:
                return False
    
    return True

# Example usage
graph = {
    1: [2, 3, 4],  # Vertex 1 is connected to vertices 2, 3, and 4
    2: [1, 3, 4],  # Vertex 2 is connected to vertices 1, 3, and 4
    3: [1, 2, 4],  # Vertex 3 is connected to vertices 1, 2, and 4
    4: [1, 2]   # Vertex 4 is connected to vertices 1, 2, and 3
}

result = is_complete_graph(graph)
if result:
    print("The graph is a complete graph.")
else:
    print("The graph is not a complete graph.")
