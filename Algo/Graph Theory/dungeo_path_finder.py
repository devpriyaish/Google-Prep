from collections import deque

class DungeonPathFinder:
    """
    The DungeonPathFinder class is designed to solve the dungeon traversal problem using
    the Breadth-First Search (BFS) algorithm. The goal is to find the shortest path 
    from the start point ('S') to the exit ('E') in a dungeon grid. The dungeon consists 
    of empty spaces ('.'), walls ('#'), a start point, and an exit point.
    
    Attributes:
        dungeon (list[list[str]]): A 2D grid representing the dungeon layout.
        start (tuple[int, int]): The starting position of the solver (row, column).
        rows (int): The number of rows in the dungeon.
        cols (int): The number of columns in the dungeon.
        visited (list[list[bool]]): A 2D list tracking whether a cell has been visited.
        dr (list[int]): Row direction changes for up, down, left, right (BFS).
        dc (list[int]): Column direction changes for up, down, left, right (BFS).
        reached_end (bool): A flag to indicate if the end point ('E') is reached.
    """
    
    def __init__(self, dungeon, start, rows, cols):
        """
        Initializes the DungeonPathFinder with the given dungeon, start position, and grid dimensions.
        
        Args:
            dungeon (list[list[str]]): The 2D grid representing the dungeon.
            start (tuple[int, int]): The starting position (row, column) in the dungeon.
            rows (int): The number of rows in the dungeon.
            cols (int): The number of columns in the dungeon.
        """
        self.dungeon = dungeon
        self.start = start
        self.rows = rows
        self.cols = cols
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]  # Initialize visited grid
        self.dr = [-1, 1, 0, 0]  # Row direction changes (up, down, left, right)
        self.dc = [0, 0, 1, -1]  # Column direction changes (up, down, left, right)
        self.reached_end = False  # Flag to track if the exit is reached

    def find_shortest_path(self):
        """
        Finds the shortest path from the start point ('S') to the exit ('E') using a breadth-first search (BFS) approach.
        
        Returns:
            int: The minimum number of moves to reach the exit ('E'), or -1 if the exit is not reachable.
        """
        sr, sc = self.start  # Start row and column
        qr = deque([sr])  # Queue for rows to explore
        qc = deque([sc])  # Queue for columns to explore
        self.visited[sr][sc] = True  # Mark the start point as visited
        move_count = 0  # Number of moves taken to reach the exit
        nodes_left_in_layer = 1  # Number of nodes left to explore in the current BFS layer
        nodes_in_next_layer = 0  # Number of nodes to explore in the next BFS layer

        while qr:
            r = qr.popleft()  # Dequeue the row to explore
            c = qc.popleft()  # Dequeue the column to explore

            # Check if the current position is the exit
            if self.dungeon[r][c] == 'E':
                self.reached_end = True  # Set the reached_end flag to True
                break

            # Explore the neighbors and add valid ones to the queue
            nodes_in_next_layer += self.explore_neighbors(r, c, qr, qc)
            nodes_left_in_layer -= 1

            # If all nodes in the current layer are explored, move to the next layer
            if nodes_left_in_layer == 0:
                nodes_left_in_layer = nodes_in_next_layer
                nodes_in_next_layer = 0
                move_count += 1  # Increment the move count for each layer

        # Return the move count if the end is reached, otherwise return -1
        return move_count if self.reached_end else -1

    def explore_neighbors(self, r, c, qr, qc):
        """
        Explores the valid neighbors of the current cell (r, c) and adds them to the queue.
        
        Args:
            r (int): The row index of the current cell.
            c (int): The column index of the current cell.
            qr (deque): Queue storing row indices of the next cells to explore.
            qc (deque): Queue storing column indices of the next cells to explore.
        
        Returns:
            int: The number of valid neighbors added to the queue.
        """
        added_nodes = 0  # Counter for added valid neighbors

        # Explore the 4 possible directions (up, down, left, right)
        for i in range(4):
            rr = r + self.dr[i]  # New row after applying direction
            cc = c + self.dc[i]  # New column after applying direction

            # Check if the new cell is valid for exploration
            if self.is_valid(rr, cc):
                qr.append(rr)  # Add the new row to the queue
                qc.append(cc)  # Add the new column to the queue
                self.visited[rr][cc] = True  # Mark the new cell as visited
                added_nodes += 1  # Increment the counter for added nodes

        return added_nodes

    def is_valid(self, r, c):
        """
        Checks if the given position (r, c) is valid for exploration.
        
        A position is valid if:
        - It is within the bounds of the dungeon grid.
        - It is not a wall ('#').
        - It has not been visited before.
        
        Args:
            r (int): The row index of the cell to check.
            c (int): The column index of the cell to check.
        
        Returns:
            bool: True if the position is valid, False otherwise.
        """
        if r < 0 or c < 0 or r >= self.rows or c >= self.cols:  # Out of bounds
            return False
        if self.dungeon[r][c] == '#':  # Wall cell
            return False
        if self.visited[r][c]:  # Already visited
            return False
        return True  # Valid cell

# Usage Example
dungeon_map = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]

start_position = (0, 0)  # Starting position (row, column)
rows = len(dungeon_map)  # Number of rows in the dungeon
cols = len(dungeon_map[0])  # Number of columns in the dungeon

path_finder = DungeonPathFinder(dungeon_map, start_position, rows, cols)  # Create a DungeonPathFinder instance
result = path_finder.find_shortest_path()  # Get the result

# Provide detailed output
if result != -1:
    print(f"The shortest path from the start 'S' to the exit 'E' is {result} moves.")
else:
    print("The exit 'E' is not reachable from the start 'S'.")
    
# Expected Output 
# The shortest path from the start 'S' to the exit 'E' is 9 moves.
