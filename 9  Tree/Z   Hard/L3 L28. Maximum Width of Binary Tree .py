from collections import deque

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def widthOfBinaryTree( root: TreeNode) -> int:
    if not root:
        return 0
    ans = 0
    q = deque([(root, 0)])

    while q:
        size = len(q)
        mmin = q[0][1]
        first, last = 0, 0

        for i in range(size):
            cur_id = q[0][1] - mmin
            node = q[0][0]
            q.popleft()

            if i == 0:
                first = cur_id

            if i == size - 1:
                last = cur_id

            if node.left:
                q.append((node.left, cur_id * 2 + 1))

            if node.right:
                q.append((node.right, cur_id * 2 + 2))

        ans = max(ans, last - first + 1)

    return ans

def main():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    max_width = widthOfBinaryTree(root)
    print(f"Maximum width of the binary tree is: {max_width}")

if __name__ == "__main__":
    main()
