import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Directed weighted graph oluştur (create a directed weighted graph)
G = nx.DiGraph()

# Kenarlar (kaynak, hedef, ağırlık) -> (source, target, weight)
# This graph contains positive and negative edge weights (but no negative cycles).
edges = [
    (1, 2, 3),
    (1, 3, 8),
    (1, 5, -4),
    (2, 4, 1),
    (2, 5, 7),
    (3, 2, 4),
    (4, 1, 2),
    (4, 3, -5),
    (5, 4, 6)
]

# Kenarları ekle (add all edges to the graph)
for u, v, w in edges:
    G.add_edge(u, v, weight=w)


def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths
    between all pairs of nodes in a weighted directed graph.
    
    Parameters:
        graph (nx.DiGraph): Directed graph with 'weight' attributes on edges.
    
    Returns:
        matrix (ndarray): Shortest path distance matrix
        nodes (list): Node labels in the order corresponding to the matrix
    """

    # 1) Prepare node indexing
    # Map each node to a row/column index in the adjacency matrix
    nodes = sorted(graph.nodes())
    node_to_index = {node: idx for idx, node in enumerate(nodes)}

    # 2) Initialize distance matrix
    # Fill with +inf meaning "no path known yet"
    matrix = np.full((len(graph.nodes), len(graph.nodes)), np.inf)

    # Distance from a node to itself is 0. Since there is no self loop
    np.fill_diagonal(matrix, 0)

    # 3) Fill initial distances from edges
    # If an edge (u,v) exists, set matrix[u][v] = weight
    for u, v, edge in graph.edges(data=True):
        i = node_to_index[u]
        j = node_to_index[v]
        matrix[i][j] = edge["weight"]

    # 4) Core Floyd-Warshall triple loop
    # For each intermediate node k, check if using k as a "bridge"
    # provides a shorter path between i and j.
    for k in range(len(graph.nodes)):
        # Note: the inner two loops could be replaced with numpy vectorization
        # to update a whole row/column at once, but here we keep them explicit
        # to clearly illustrate the algorithm’s mechanics.
        for i in range(len(graph.nodes)):
            for j in range(len(graph.nodes)):
                # Relaxation step: update distance if a shorter path is found
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    return matrix, nodes


# --- Run the algorithm ---
matrix_out, nodes_out = floyd_warshall(G)

print("Raw output matrix:\n", matrix_out)

print("\nMy Algorithm’s Result:")
# Use pandas DataFrame for nice tabular display
print(pd.DataFrame(matrix_out, index=nodes_out, columns=nodes_out))

# --- Compare with NetworkX’s built-in implementation ---
print("\nNetworkX Result:")
distances = nx.floyd_warshall(G)   # returns dict-of-dicts {u: {v: dist}}
nodes = sorted(G.nodes())
df = pd.DataFrame(index=nodes, columns=nodes)

for u in nodes:
    for v in nodes:
        df.loc[u, v] = distances[u][v]

print(df)

# --- Visualization of the graph ---
pos = nx.spring_layout(G, seed=42)  # layout for consistent positions
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=14,
    font_weight='bold'
)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.title("Example Graph for Floyd-Warshall", fontsize=14)
plt.show()
