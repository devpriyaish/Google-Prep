class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)      # Traverse left subtree
        print(root.value, end=" ")  # Visit root
        inorder(root.right)     # Traverse right subtree

# Preorder Traversal
def preorder(root):
    if root:
        print(root.value, end=" ")  # Visit root
        preorder(root.left)      # Traverse left subtree
        preorder(root.right)     # Traverse right subtree

# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)     # Traverse left subtree
        postorder(root.right)    # Traverse right subtree
        print(root.value, end=" ")  # Visit root

# Example Tree: 
#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test the traversals
print("Inorder Traversal: ")
inorder(root)  # Output: 4 2 5 1 3
print("\nPreorder Traversal: ")
preorder(root)  # Output: 1 2 4 5 3
print("\nPostorder Traversal: ")
postorder(root)  # Output: 4 5 2 3 1
