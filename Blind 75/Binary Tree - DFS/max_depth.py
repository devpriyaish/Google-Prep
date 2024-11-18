from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    """
    A class representing a binary tree with utility methods.
    """

    @staticmethod
    def max_depth(root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree.
        
        :param root: Root node of the binary tree
        :return: Maximum depth of the tree
        """
        if root is None:
            return 0
        left_depth = BinaryTree.max_depth(root.left)
        right_depth = BinaryTree.max_depth(root.right)
        return 1 + max(left_depth, right_depth)


# Example Usage
if __name__ == "__main__":
    # Creating a binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5

    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)

    # Calculate maximum depth
    max_depth = BinaryTree.max_depth(root)
    print(f"Maximum Depth of the Binary Tree: {max_depth}")

# Expected Output
# Maximum Depth of the Binary Tree: 3
