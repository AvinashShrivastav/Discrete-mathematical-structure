# Write a Program to check if a given graph is a complete graph. Represent the graph using
# the Adjacency Matrix representation.


def is_complete_graph(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    
    # Check if each pair of vertices is connected
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and not adjacency_matrix[i][j]:
                return False
    
    return True

# Example usage
graph = [
    [0, 1, 1, 1],  # Vertex 1 is connected to vertices 2, 3, and 4
    [1, 0, 1, 1],  # Vertex 2 is connected to vertices 1, 3, and 4
    [1, 1, 0, 1],  # Vertex 3 is connected to vertices 1, 2, and 4
    [1, 1, 1, 0]   # Vertex 4 is connected to vertices 1, 2, and 3
]

result = is_complete_graph(graph)
if result:
    print("The graph is a complete graph.")
else:
    print("The graph is not a complete graph.")
