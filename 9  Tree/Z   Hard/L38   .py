                            
                                
# TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # Initialize a global variable
        # 'prev' to keep track of the
        # previously processed node.
        self.prev = None

    # Function to flatten a binary tree
    # to a right next Linked List structure
    def flatten(self, root):
        # Base case: If the current
        # node is None, return.
        if root is None:
            return

        # Recursive call to
        # flatten the right subtree
        self.flatten(root.right)

        # Recursive call to
        # flatten the left subtree
        self.flatten(root.left)

        # At this point, both left and right
        # subtrees are flattened, and 'prev'
        # is pointing to the rightmost node
        # in the flattened right subtree.

        # Set the right child of
        # the current node to 'prev'.
        root.right = self.prev

        # Set the left child of the
        # current node to None.
        root.left = None

        # Update 'prev' to the current
        # node for the next iteration.
        self.prev = root

# Print the preorder traversal of the
# Original Binary Tree
def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)

# Print the Binary Tree along the
# Right Pointers after Flattening
def print_flatten_tree(root):
    if not root:
        return
    print(root.val, end=" ")
    print_flatten_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(8)

    sol = Solution()

    print("Binary Tree Preorder: ", end="")
    print_preorder(root)
    print()

    sol.flatten(root)

    print("Binary Tree After Flatten: ", end="")
    print_flatten_tree(root)
    print()
    
                                
                            