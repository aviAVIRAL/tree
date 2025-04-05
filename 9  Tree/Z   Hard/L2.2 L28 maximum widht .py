


# isko meine appne tarike se kiya hai bhai  100 % coorect hai code 

from collections import deque

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def widthOfBinaryTree( root: TreeNode) -> int:
    if not root:
        return 0
    
    q = deque([(root, 0)])
    width = -1

    while q:
        size = len(q)
        
        width = max ( width, q[-1][1] - q[0][1] +1)
        for i in range(size):
            node, ind = q.popleft()

            if node.left:
                q.append((node.left, ind * 2 + 1))

            if node.right:
                q.append((node.right, ind * 2 + 2))


    return width


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


