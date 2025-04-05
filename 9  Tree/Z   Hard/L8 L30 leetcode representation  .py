

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                top = queue.popleft()

                if top.left:
                    parent[top.left.val] = top
                    queue.append(top.left)

                if top.right:
                    parent[top.right.val] = top
                    queue.append(top.right)

        visited = {}
        queue.append(target)
        while k > 0 and queue:
            size = len(queue)

            for _ in range(size):
                top = queue.popleft()

                visited[top.val] = 1

                if top.left and top.left.val not in visited:
                    queue.append(top.left)

                if top.right and top.right.val not in visited:
                    queue.append(top.right)

                if top.val in parent and parent[top.val].val not in visited:
                    queue.append(parent[top.val])

            k -= 1

        while queue:
            ans.append(queue.popleft().val)

        return ans
    

    # --------------------- also repr enset ---------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def parentmarking(root) :
    """Marks parent nodes for each node in the tree."""
    queue = deque([root])
    parent = {}

    while queue:
        top = queue.popleft()

        if top.left:
            parent[top.left] = top  # Map child node to its parent
            queue.append(top.left)

        if top.right:
            parent[top.right] = top  # Map child node to its parent
            queue.append(top.right)

    return parent

class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        # Map parent nodes
        parent = parentmarking(root)

        # Perform BFS to find nodes at distance K
        visited = set()
        queue = deque([target])
        visited.add(target)

        while k > 0 and queue:
            size = len(queue)

            for _ in range(size):
                top = queue.popleft()

                # Visit left child
                if top.left and top.left not in visited:
                    queue.append(top.left)
                    visited.add(top.left)

                # Visit right child
                if top.right and top.right not in visited:
                    queue.append(top.right)
                    visited.add(top.right)

                # Visit parent node
                if top in parent and parent[top] not in visited:
                    queue.append(parent[top])
                    visited.add(parent[top])

            k -= 1

        # Collect all nodes at distance K
        while queue:
            ans.append(queue.popleft().val)

        return ans

