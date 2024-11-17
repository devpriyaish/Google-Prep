class MaxAverageFinder:
    """
    A class to find the maximum average of any subarray of size 'k' in a list of integers.
    """

    def __init__(self, numbers, subarray_size):
        """
        Initialize with the list of numbers and subarray size.

        Args:
            numbers (List[int]): The list of integers.
            subarray_size (int): The size of the subarray to consider.
        """
        self.numbers = numbers
        self.subarray_size = subarray_size

    def find_max_average(self):
        """
        Find the maximum average of any subarray of size 'k'.

        Returns:
            float: The maximum average value.
        """
        k = self.subarray_size
        numbers = self.numbers

        # Initialize the sum of the first subarray of size 'k'
        max_sum = current_sum = sum(numbers[:k])

        # Slide the window across the list and update the sum
        for i in range(k, len(numbers)):
            current_sum += numbers[i] - numbers[i - k]
            max_sum = max(max_sum, current_sum)

        # Calculate and return the maximum average
        return max_sum / k


# Example usage
if __name__ == "__main__":
    numbers = [1, 12, -5, -6, 50, 3]
    subarray_size = 4
    max_average_finder = MaxAverageFinder(numbers, subarray_size)
    result = max_average_finder.find_max_average()
    print(f"Maximum average of subarrays of size {subarray_size}: {result}")

# Expected Output
# Maximum average of subarrays of size 4: 12.75
