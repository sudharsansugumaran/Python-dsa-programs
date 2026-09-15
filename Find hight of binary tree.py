# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find height of binary tree
def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


# Create the binary tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


# Find and print height
print("Height of Binary Tree:", height(root))