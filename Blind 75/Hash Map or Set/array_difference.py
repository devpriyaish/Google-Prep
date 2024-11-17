class DifferenceFinder:
    """
    A class to find the distinct integers in two arrays that are not present in each other.
    """

    def __init__(self, array1, array2):
        """
        Initialize the class with two arrays.

        Args:
            array1 (List[int]): The first integer array.
            array2 (List[int]): The second integer array.
        """
        self.array1 = array1
        self.array2 = array2

    def find_unique_elements(self):
        """
        Find the distinct integers in array1 that are not in array2 and vice versa.

        Returns:
            List[List[int]]: A list containing two lists:
                - Elements unique to array1.
                - Elements unique to array2.
        """
        set1 = set(self.array1)
        set2 = set(self.array2)

        unique_to_array1 = set1 - set2
        unique_to_array2 = set2 - set1

        return [list(unique_to_array1), list(unique_to_array2)]


# Example usage
if __name__ == "__main__":
    nums1 = [1, 2, 3, 3]
    nums2 = [3, 4, 5, 5]

    difference_finder = DifferenceFinder(nums1, nums2)
    result = difference_finder.find_unique_elements()
    print(f"Unique elements in nums1: {result[0]}")
    print(f"Unique elements in nums2: {result[1]}")

# Expected Output
# Unique elements in nums1: [1, 2]
# Unique elements in nums2: [4, 5]
