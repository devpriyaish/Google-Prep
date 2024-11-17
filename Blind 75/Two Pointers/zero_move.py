class ZeroMover:
    """
    A class to handle operations related to moving zeros in a list.
    """

    def __init__(self, numbers):
        """
        Initialize the list of numbers.

        Args:
            numbers (List[int]): The list of integers to process.
        """
        self.numbers = numbers

    def move_zeros_to_end(self):
        """
        Move all zeros in the list to the end, maintaining the relative order of non-zero elements.
        This operation is performed in-place.
        """
        write_pointer = 0  # Pointer for the position to place the next non-zero element

        for read_pointer in range(len(self.numbers)):
            if self.numbers[read_pointer] != 0:
                # Swap the current non-zero element with the element at the write pointer
                self.numbers[write_pointer], self.numbers[read_pointer] = (
                    self.numbers[read_pointer],
                    self.numbers[write_pointer],
                )
                write_pointer += 1


# Example usage
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    zero_mover = ZeroMover(nums)
    zero_mover.move_zeros_to_end()
    print(f"List after moving zeros: {zero_mover.numbers}")

# Expected Output
# List after moving zeros: [1, 3, 12, 0, 0]
