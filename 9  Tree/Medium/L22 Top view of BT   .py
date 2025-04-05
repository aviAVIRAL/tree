
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def topView(self, root):
        if not root:
            return []

        mp = {}  
        q = deque([(root, 0)])  

        while q:
            node, line = q.popleft()

            if line not in mp:
                mp[line] = node.data

# also rep 
            # if line not in mp:
            #     mp[line] = node.data
            
            # elif line in mp : 
            #     continue

            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))

        sol = sorted(mp)
        ans = []
        for x in sol: 
            ans.append(mp[x])
        return ans
       
       
# # also rep        
#         ans = [mp[key] for key in sorted(mp)]
#         return ans


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)
    obj = Solution()
    result = obj.topView(root)

    # Print the top view
    print("Top View:", result)
print()


