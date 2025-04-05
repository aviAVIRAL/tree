




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f( root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base case
    if root is None or root == p or root == q:
        return root
    
    # also rep 
    # if root is None : return root   
    # if root == p or root == q: return root

    
    left = f(root.left, p, q)
    right = f(root.right, p, q)

    if left is None:
        return right
    elif right is None:
        return left
    else:  # Both left and right are not None, we found our result
        return root


def main():
    # Create a sample binary tree
    # Example tree:
    #         3
    #        / \
    #       5   1
    #      / \  / \
    #     6  2 0   8
    #       / \
    #      7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Assign p and q nodes
    p = root.left.left    # Node with value 6
    q = root.left.right.right  # Node with value 4

    # Call the function
    
    lca = f(root, p, q)

    # Print the result
    print(f"LCA of {p.val} and {q.val} is:   {lca.val}")

if __name__ == "__main__":
    main()
