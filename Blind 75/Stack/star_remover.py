class StarRemover:
    """
    A class to remove stars ('*') and their preceding characters from a given string.
    """

    def __init__(self, input_string):
        """
        Initialize the class with the input string.

        Args:
            input_string (str): The string to process.
        """
        self.input_string = input_string

    def remove_stars(self):
        """
        Process the string to remove stars and their preceding characters.

        Returns:
            str: The processed string after removing stars and their preceding characters.
        """
        character_stack = []  # Stack to track characters
        
        for char in self.input_string:
            if char != '*':
                character_stack.append(char)  # Add character to stack if not '*'
            elif character_stack:
                character_stack.pop()  # Remove the last added character if '*' is encountered
        
        return ''.join(character_stack)  # Return the processed string


# Example usage
if __name__ == "__main__":
    input_string = "abc*de**f"
    star_remover = StarRemover(input_string)
    result = star_remover.remove_stars()
    print(f"Processed string: {result}")

# Expected Output
# Processed string: abf
