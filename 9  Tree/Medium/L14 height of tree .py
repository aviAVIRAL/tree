
# using recursion 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def f(root):
    if root is None: return 0
    lh = f(root.left)
    rh = f(root.right)
    return 1 + max(lh, rh)
  
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    print("height  depth is :")
    print(f(root))

print()
# ...................................
# using queue or deque 
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        q = deque()
        level = 0
        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# Finding the maximum depth
solution = Solution()
depth = solution.maxDepth(root)

print("Maximum depth of the binary tree:", depth)
print()
