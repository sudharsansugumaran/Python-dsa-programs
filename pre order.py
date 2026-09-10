# Class Node
class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder traversal function
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Create the binary tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)

# Perform preorder traversal
preorder(root)