from collections import defaultdict
from typing import List, Dict, Optional


class Edge:
    """
    Represents a directed, weighted edge in a graph.
    """

    def __init__(self, from_node: int, to_node: int, weight: int):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


class DirectedAcyclicGraph:
    """
    Represents a directed acyclic graph (DAG) and provides methods for topological sorting
    and shortest path calculations.
    """

    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.graph: Dict[int, List[Edge]] = defaultdict(list)

    def add_edge(self, from_node: int, to_node: int, weight: int):
        """
        Adds a directed, weighted edge to the graph.
        """
        self.graph[from_node].append(Edge(from_node, to_node, weight))

    def _dfs(self, at: int, visited: List[bool], ordering: List[int], index: int) -> int:
        """
        Depth-first search helper for topological sorting.
        """
        visited[at] = True
        for edge in self.graph.get(at, []):
            if not visited[edge.to_node]:
                index = self._dfs(edge.to_node, visited, ordering, index)
        ordering[index] = at
        return index - 1

    def topological_sort(self) -> List[int]:
        """
        Performs topological sorting on the DAG.
        """
        visited = [False] * self.num_nodes
        ordering = [0] * self.num_nodes
        index = self.num_nodes - 1

        for at in range(self.num_nodes):
            if not visited[at]:
                index = self._dfs(at, visited, ordering, index)

        return ordering

    def shortest_path_from(self, start: int) -> List[Optional[int]]:
        """
        Calculates the shortest paths from the start node to all other nodes in the DAG.
        """
        # Perform topological sorting
        topsort = self.topological_sort()

        # Initialize distances with None (infinity)
        distances = [None] * self.num_nodes
        distances[start] = 0

        # Relax edges in topological order
        for node_index in topsort:
            if distances[node_index] is not None:
                for edge in self.graph.get(node_index, []):
                    new_distance = distances[node_index] + edge.weight
                    if distances[edge.to_node] is None:
                        distances[edge.to_node] = new_distance
                    else:
                        distances[edge.to_node] = min(distances[edge.to_node], new_distance)

        return distances


# Example Usage
if __name__ == "__main__":
    # Initialize the graph
    num_nodes = 7
    dag = DirectedAcyclicGraph(num_nodes)

    # Add edges
    dag.add_edge(0, 1, 3)
    dag.add_edge(0, 2, 2)
    dag.add_edge(0, 5, 3)
    dag.add_edge(1, 3, 1)
    dag.add_edge(1, 2, 6)
    dag.add_edge(2, 3, 1)
    dag.add_edge(2, 4, 10)
    dag.add_edge(3, 4, 5)
    dag.add_edge(5, 4, 7)

    # Perform topological sorting
    ordering = dag.topological_sort()
    print("Topological Ordering:", ordering)  # Output: [6, 0, 5, 1, 2, 3, 4]
    
    source_node = 0

    # Find shortest paths from node 0
    shortest_paths = dag.shortest_path_from(source_node)
    print(f"Shortest Distance from Node {source_node} to Node 4:", shortest_paths[4])  # Output: 8
    print(f"Shortest Distance from Node {source_node} to Node 6:", shortest_paths[6])  # Output: None


# Expected Output
# Topological Ordering: [6, 0, 5, 1, 2, 3, 4]
# Shortest Distance from Node 0 to Node 4: 8
# Shortest Distance from Node 0 to Node 6: None
