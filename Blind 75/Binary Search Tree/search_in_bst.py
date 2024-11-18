from typing import Optional, List


class TreeNode:
    """
    Represents a node in a binary search tree.
    """

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        """
        Initializes a TreeNode with a value and optional left and right child nodes.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Provides solutions to binary search tree problems.
    """

    @staticmethod
    def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Searches for a node with the given value in a binary search tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary search tree.
            val (int): The value to search for.

        Returns:
            Optional[TreeNode]: The node with the given value, or None if not found.
        """
        while root:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return None

    @staticmethod
    def tree_to_list(root: Optional[TreeNode]) -> List[int]:
        """
        Converts a binary tree to a list using level-order traversal.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list representation of the tree in level-order.
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values to clean up the list
        while result and result[-1] is None:
            result.pop()

        return result


if __name__ == "__main__":
    # Create a binary search tree
    """
        Tree structure:
              4
             / \
            2   7
           / \
          1   3
    """
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # Search for a value in the BST
    solution = Solution()

    # Example 1: Search for the value 2
    search_result = solution.search_bst(root, 2)
    result_list = solution.tree_to_list(search_result)
    print(f"Tree as list for value 2: {result_list}")  # Output: [2, 1, 3]

    # Example 2: Search for a value not in the tree
    search_result = solution.search_bst(root, 5)
    result_list = solution.tree_to_list(search_result)
    print(f"Tree as list for value 5: {result_list}")  # Output: []

# Expected Output
# Tree as list for value 2: [2, 1, 3]
# Tree as list for value 5: []
