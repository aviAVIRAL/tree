from collections import deque

class Solution:
    def markParents(self, root, parent):
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
        # Step 1: Map parent nodes
        parent = {}
        self.markParents(root, parent)


        # Step 2: Perform BFS to find nodes at distance K
# ................................................................................
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



# .....................
#  
class Solution:
def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    
    ans = []

    parent = {}  # mp  i sparent here baby dol 
    q = deque()
    q.append(root)

    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()

            if node.left:
                parent[node.left.val] = node
                q.append(node.left)

            if node.right:
                parent[node.right.val] = node
                q.append(node.right)
# ...............................................
visited = {}
q.append(target)
while k > 0 and q:
    size = len(q)

    for _ in range(size):
        node = q.popleft()

        visited[node.val] = 1

        if node.left and node.left.val not in visited:
            q.append(node.left)

        if node.right and node.right.val not in visited:
            q.append(node.right)

        if node.val in parent and parent[node.val].val not in visited:
            q.append(parent[node.val])

    k -= 1

while q:
    ans.append(q.popleft().val)

return ans