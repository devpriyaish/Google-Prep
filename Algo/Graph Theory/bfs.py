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
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        # Add the edge in both directions (undirected graph)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def bfs(self, start_node):
        """
        Perform BFS traversal starting from the given node.
        
        Args:
            start_node (int): The node from where BFS traversal begins.
        
        Returns:
            list: A list of nodes in the order they were traversed.
        """
        # Initialize the queue with the start node, visited set, and traversed list
        queue = deque([start_node])
        visited = set([start_node])  # Track visited nodes
        traversed = []  # List to store the traversal order

        while queue:
            node = queue.popleft()  # Dequeue a node
            traversed.append(node)  # Add it to the traversal list

            # Add unvisited neighbors to the queue
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    queue.append(neighbor)  # Enqueue the neighbor

        return traversed


# Create a graph and add edges
g = Graph()

# List of edges to be added to the graph
edges = [[1, 2], [1, 3], [2, 5], [4, 5]]

# Add the edges to the graph
for u, v in edges:
    g.add_edge(u, v)

# Perform BFS traversal starting from node 1
traversal_result = g.bfs(1)
print(f"BFS traversal starting from node 1: {traversal_result}")

# Expected Output
# BFS traversal starting from node 1: [1, 2, 3, 5, 4]
