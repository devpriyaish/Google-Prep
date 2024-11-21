class KnapsackSolver:
    """
    A class to solve the 0/1 Knapsack problem using dynamic programming.
    """

    def __init__(self, capacity, weights, values):
        """
        Initialize the KnapsackSolver with capacity, weights, and values.

        :param capacity: The maximum capacity of the knapsack
        :param weights: List of weights of items
        :param values: List of values of items
        """
        if not weights or not values or len(weights) != len(values) or capacity < 0:
            raise ValueError("Invalid input")

        self.capacity = capacity
        self.weights = weights
        self.values = values
        self.num_items = len(weights)
        self.dp_table = [[0] * (capacity + 1) for _ in range(self.num_items + 1)]
        self.selected_items = []

    def solve(self):
        """
        Solves the 0/1 Knapsack problem and populates the DP table.

        :return: Maximum achievable profit
        """
        for i in range(1, self.num_items + 1):
            weight = self.weights[i - 1]
            value = self.values[i - 1]

            for current_capacity in range(1, self.capacity + 1):
                # Option 1: Don't include the current item
                self.dp_table[i][current_capacity] = self.dp_table[i - 1][current_capacity]

                # Option 2: Include the current item (if it fits)
                if current_capacity >= weight:
                    self.dp_table[i][current_capacity] = max(
                        self.dp_table[i][current_capacity],
                        self.dp_table[i - 1][current_capacity - weight] + value,
                    )

        self._find_selected_items()
        return self.dp_table[self.num_items][self.capacity]

    def _find_selected_items(self):
        """
        Backtracks through the DP table to find the selected items.
        """
        remaining_capacity = self.capacity

        for i in range(self.num_items, 0, -1):
            if self.dp_table[i][remaining_capacity] != self.dp_table[i - 1][remaining_capacity]:
                item_index = i - 1
                self.selected_items.append(item_index)
                remaining_capacity -= self.weights[item_index]

    def get_selected_items(self):
        """
        Returns the indices of the selected items.

        :return: List of selected item indices
        """
        return list(reversed(self.selected_items))


if __name__ == "__main__":
    # Example 1
    solver1 = KnapsackSolver(capacity=10, weights=[3, 3, 5, 6], values=[1, 4, 8, 5])
    max_profit1 = solver1.solve()
    print(f"Maximum Profit: {max_profit1}")
    print(f"Selected Items: {solver1.get_selected_items()}")

    # Example 2
    solver2 = KnapsackSolver(capacity=7, weights=[3, 1, 3, 4, 2], values=[2, 2, 4, 5, 3])
    max_profit2 = solver2.solve()
    print(f"Maximum Profit: {max_profit2}")
    print(f"Selected Items: {solver2.get_selected_items()}")

# Expected Output
# Maximum Profit: 12
# Selected Items: [1, 2]
# Maximum Profit: 10
# Selected Items: [1, 3, 4]
