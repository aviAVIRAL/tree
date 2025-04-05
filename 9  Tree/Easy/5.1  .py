


print()
# for simple represnttion  

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrder(root):
    ans = []
    if not root: 
        return ans

    q = deque()
    q.append(root)

    while q:
        n = len(q)
        level = []

        for _ in range(n):
            node = q.popleft() 
            level.append(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans.append(level)
    
    return ans

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = levelOrder(root)
    
    print()
    print(result)
    print()

    for x in result : 
        print(*x)