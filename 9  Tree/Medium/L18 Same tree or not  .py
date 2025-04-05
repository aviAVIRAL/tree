                            
# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class with a function to check if two binary trees are identical
class Solution:
    def isIdentical(self, node1, node2):
        # If both nodes are None, they are identical
        if node1 is None and node2 is None:
            return True
        # If only one of the nodes is None, they are not identical
        if node1 is None or node2 is None:
            return False
        # Check if the current nodes have the same data value
        # and recursively check their left and right subtrees
        return (node1.data == node2.data
                and self.isIdentical(node1.left, node2.left)
                and self.isIdentical(node1.right, node2.right))

# Creating nodes for binary trees in Python
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)

# Creating an instance of the Solution class
solution = Solution()

# Checking if the binary trees are identical
if solution.isIdentical(root1, root2):
    print("The binary trees are identical.")
else:
    print("The binary trees are not identical.")
                           
                        