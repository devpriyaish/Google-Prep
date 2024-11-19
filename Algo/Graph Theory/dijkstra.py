import heapq
from typing import List, Optional


class Edge:
    """Represents a directed edge between two nodes with a certain cost."""
    
    def __init__(self, from_node: int, to_node: int, cost: float):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost


class Node:
    """Represents a node with an ID and value, used in the priority queue."""

    def __init__(self, node_id: int, value: float):
        self.id = node_id
        self.value = value

    def __lt__(self, other: "Node") -> bool:
        """Define comparison for the priority queue."""
        return self.value < other.value


class Dijkstra:
    """Dijkstra's algorithm to find the shortest path in a graph."""

    def __init__(self, num_nodes: int):
        """
        Initialize the graph and supporting structures.

        :param num_nodes: Number of nodes in the graph.
        """
        self.num_nodes = num_nodes
        self.graph: List[List[Edge]] = [[] for _ in range(num_nodes)]
        self.distances: List[float] = [float('inf')] * num_nodes
        self.previous: List[Optional[int]] = [None] * num_nodes

    def add_edge(self, from_node: int, to_node: int, cost: float):
        """
        Add a directed edge to the graph.

        :param from_node: Starting node of the edge.
        :param to_node: Ending node of the edge.
        :param cost: Cost of the edge.
        """
        self.graph[from_node].append(Edge(from_node, to_node, cost))

    def _reset_state(self):
        """Reset distances and previous nodes for a fresh calculation."""
        self.distances = [float('inf')] * self.num_nodes
        self.previous = [None] * self.num_nodes

    def calculate_shortest_path(self, start: int, end: int) -> float:
        """
        Run Dijkstra's algorithm to find the shortest path from `start` to `end`.

        :param start: The starting node.
        :param end: The ending node.
        :return: The cost of the shortest path from `start` to `end`. Returns infinity if unreachable.
        """
        self._reset_state()
        self.distances[start] = 0

        visited = [False] * self.num_nodes
        priority_queue = [Node(start, 0)]

        while priority_queue:
            current_node = heapq.heappop(priority_queue)

            if visited[current_node.id]:
                continue
            visited[current_node.id] = True

            # Stop early if we've reached the target node
            if current_node.id == end:
                break

            for edge in self.graph[current_node.id]:
                if visited[edge.to_node]:
                    continue

                new_distance = self.distances[edge.from_node] + edge.cost
                if new_distance < self.distances[edge.to_node]:
                    self.distances[edge.to_node] = new_distance
                    self.previous[edge.to_node] = edge.from_node
                    heapq.heappush(priority_queue, Node(edge.to_node, new_distance))

        return self.distances[end]

    def reconstruct_path(self, start: int, end: int) -> List[int]:
        """
        Reconstruct the shortest path from `start` to `end`.

        :param start: The starting node.
        :param end: The ending node.
        :return: A list of nodes representing the path from `start` to `end`. Empty if no path exists.
        """
        distance = self.calculate_shortest_path(start, end)
        if distance == float('inf'):
            return []

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.previous[current]

        return path[::-1]


# Example usage
if __name__ == "__main__":
    num_nodes = 5
    edges = [[0, 1, 4], [0, 2, 2], [1, 3, 5], [2, 1, 1], [2, 3, 8], [3, 4, 6]]
    
    dijkstra = Dijkstra(num_nodes)
    
    for source, destination, cost in edges:
        dijkstra.add_edge(source, destination, cost)

    start_node = 0
    end_node = 4

    shortest_distance = dijkstra.calculate_shortest_path(start_node, end_node)
    shortest_path = dijkstra.reconstruct_path(start_node, end_node)

    print(f"Shortest distance from {start_node} to {end_node}: {shortest_distance}")
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")

# Expected Output
# Shortest distance from 0 to 4: 14
# Shortest path from 0 to 4: [0, 2, 1, 3, 4]
