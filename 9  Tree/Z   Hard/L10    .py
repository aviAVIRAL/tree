

# brute 
                                
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def f( root, cnt):
    if root is None:
        return
    cnt[0] += 1

    f(root.left, cnt)
    f(root.right, cnt)

def cntNodes( root):
  
    if root is None:# edge case
        return 0

    cnt = [0]

    ans = f(root, cnt)

    return cnt[0]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print( cntNodes(root))

