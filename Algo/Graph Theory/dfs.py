from collections import deque


class Graph:
    def __init__(self):
        """Initialize an empty graph represented by a dictionary."""
        self.graph = {}

    def add_edge(self, node1, node2):
        """
        Add an undirected edge between node1 and node2.
        
        Args:
            node1 (int): The first node in the edge.
            node2 (int): The second node in the edge.
        """
        # Ensure both nodes exist in the graph, initializing with empty lists if not
        self.graph.setdefault(node1, []).append(node2)
        self.graph.setdefault(node2, []).append(node1)

    def dfs(self, node, visited=None):
        """
        Perform DFS traversal starting from the given node.

        Args:
            node (int): The node to start the DFS traversal from.
            visited (set): Set of visited nodes to avoid revisiting.

        Returns:
            list: A list of nodes in the order they were visited.
        """
        # Initialize visited set if not provided
        if visited is None:
            visited = set()

        # Add the current node to visited and the traversal list
        visited.add(node)
        traversed = [node]

        # Recur for all unvisited neighbors
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                traversed.extend(self.dfs(neighbor, visited))

        return traversed

# Create a graph and add edges
g = Graph()

# List of edges to be added to the graph
edges = [[1, 2], [1, 3], [2, 5], [4, 5]]

# Add the edges to the graph
for u, v in edges:
    g.add_edge(u, v)

# Perform DFS and BFS traversal starting from node 1
dfs_result = g.dfs(1)

print(f"DFS traversal starting from node 1: {dfs_result}")

# Expected Output
# DFS traversal starting from node 1: [1, 2, 5, 4, 3]
