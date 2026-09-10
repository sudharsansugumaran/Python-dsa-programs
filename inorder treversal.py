# Class Node
class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder traversal function
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Create the binary tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

# Perform inorder traversal
inorder(root)
