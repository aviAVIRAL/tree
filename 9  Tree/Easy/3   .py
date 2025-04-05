



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level = []

            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level)
        return ans

def printList(lst):
    for num in lst:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")

    for level in result:
        printList(level)
