class StringGCD:
    """
    A class to calculate the greatest common divisor (GCD) of two strings.
    """

    def __init__(self, first_string, second_string):
        """
        Initialize the two strings for GCD calculation.

        Args:
            first_string (str): The first string.
            second_string (str): The second string.
        """
        self.first_string = first_string
        self.second_string = second_string

    def is_valid_divisor(self, substring_length):
        """
        Check if a substring of the given length is a valid common divisor of both strings.

        Args:
            substring_length (int): Length of the potential divisor substring.

        Returns:
            bool: True if the substring is a valid common divisor, False otherwise.
        """
        len_first, len_second = len(self.first_string), len(self.second_string)

        # Ensure the length is a divisor of both string lengths
        if len_first % substring_length != 0 or len_second % substring_length != 0:
            return False

        potential_divisor = self.first_string[:substring_length]
        repeat_count_first = len_first // substring_length
        repeat_count_second = len_second // substring_length

        return (
            self.first_string == potential_divisor * repeat_count_first
            and self.second_string == potential_divisor * repeat_count_second
        )

    def calculate_gcd(self):
        """
        Calculate the greatest common divisor of two strings.

        Returns:
            str: The GCD substring, or an empty string if no common divisor exists.
        """
        shorter_length = min(len(self.first_string), len(self.second_string))

        for substring_length in range(shorter_length, 0, -1):
            if self.is_valid_divisor(substring_length):
                return self.first_string[:substring_length]

        return ""


# Example usage
if __name__ == "__main__":
    string1 = "ABABAB"
    string2 = "ABAB"

    gcd_finder = StringGCD(string1, string2)
    gcd_result = gcd_finder.calculate_gcd()
    print(f"The GCD of strings '{string1}' and '{string2}' is: '{gcd_result}'")

# Expected Output
# The GCD of strings 'ABABAB' and 'ABAB' is: 'AB'
