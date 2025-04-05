from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def markParents(self, root, parent):
        """Map each node to its parent."""
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.left:
                parent[node.left] = node
                q.append(node.left)

            if node.right:
                parent[node.right] = node
                q.append(node.right)

    def distanceK(self, root, target, k):
        """Find all nodes at distance K from the target node."""
        # Step 1: Map parent nodes
        parent = {}
        self.markParents(root, parent)

        # Step 2: Perform BFS to find nodes at distance K
        visited = set()
        q = deque()
        q.append(target)
        visited.add(target)
        distance = 0
        while q:
            if distance == k:
                break
            distance += 1
            for _ in range(len(q)):
                node = q.popleft()
                # Visit left child
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                # Visit right child
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                # Visit parent node
                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
                    visited.add(parent[node])

        # Collect all nodes at distance K
        result = []
        while q:
            result.append(q.popleft().val)

        return result
# Construct a binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Target node
target = root.left  # Node with value 5

# Distance K
k = 2

# Find all nodes at distance K from the target
solution = Solution()
result = solution.distanceK(root, target, k)
print("Nodes at distance K:", result)


    #       3
    #    /     \
    #   5       1
    #  / \     / \
    # 6   2   0   8
    #    / \
    #   7   4

# also rep  ---------------------------------------------------------------

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def markParents(self, root, parent):
        """Map each node to its parent."""
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.left:
                parent[node.left] = node
                q.append(node.left)

            if node.right:
                parent[node.right] = node
                q.append(node.right)

    def distanceK(self, root, target, k):
        """Find all nodes at distance K from the target node."""
        # Step 1: Map parent nodes
        parent = {}
        self.markParents(root, parent)

        # Step 2: Perform BFS to find nodes at distance K
        visited = set()
        q = deque()
        q.append(target)
        visited.add(target)
        distance = 0 
        while q:
            if distance == k:
                break # impo 
            for _ in range(len(q)):
                node = q.popleft()
                # Visit left child
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                # Visit right child
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                # Visit parent node
                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
                    visited.add(parent[node])
            distance += 1  # impo

        # Collect all nodes at distance K
        result = []
        while q:
            result.append(q.popleft().val)

        return result
# Construct a binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Target node
target = root.left   # impo # adress ki form mein given hai bhai # Node with value 5

# Distance K
k = 2

# Find all nodes at distance K from the target
solution = Solution()
result = solution.distanceK(root, target, k)
print("Nodes at distance K:", result)


    #       3
    #    /     \
    #   5       1
    #  / \     / \
    # 6   2   0   8
    #    / \
    #   7   4
