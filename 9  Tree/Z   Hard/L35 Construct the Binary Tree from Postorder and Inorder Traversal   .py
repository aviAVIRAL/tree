                            
from typing import List

# TreeNode class definition
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Function to build a binary tree
        from inorder and postorder traversals
        """
        if len(inorder) != len(postorder):
            return None

        # Create a map to store the indices
        # of elements in the inorder traversal
        # mp = {val: i for i, val in enumerate(inorder)}

        mp ={} # also rep # mp = {val: idx for idx, val in enumerate(inorder)}
        for i in range(0, len(inorder)):
            mp[inorder[i]] = i 

        # Call the recursive function
        # to build the binary tree
        return self.f(inorder, 0, len(inorder) - 1, postorder, 0,
                                     len(postorder) - 1, mp)

    def f(self, inorder: List[int], inoderStart, inoderEnd, postorder: List[int], postoderStart, postoderEnd, mp):
        """
        Recursive function to build a binary
        tree from inorder and postorder traversals
        """
        # Base case: If the subtree
        # is empty, return None
        if postoderStart > postoderEnd or inoderStart > inoderEnd:
            return None

        # Create a new TreeNode
        # with the root value from postorder
        root = TreeNode(postorder[postoderEnd])

        # Find the index of the root
        # value in inorder traversal
        inRoot = mp[postorder[postoderEnd]]

        # Number of nodes in the left subtree
        elmLeft = inRoot - inoderStart

        # Recursively build the
        # left and right subtrees
        root.left = self.f(inorder, inoderStart, inRoot - 1, postorder,
                                         postoderStart, postoderStart + elmLeft - 1, mp)

        root.right = self.f(inorder, inRoot + 1, inoderEnd, postorder,
                                          postoderStart + elmLeft, postoderEnd - 1, mp)

        # Return the root of
        # the constructed subtree
        return root

# Function to print the--------------------------------
# inorder traversal of a tree
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

# Function to print the given list
def printList(lst):
    for item in lst:
        print(item, end=" ")
    print()

# Example input lists
inorder = [40, 20, 50, 10, 60, 30]
postorder = [40, 50, 20, 60, 30, 10]

# Display the input lists
print("Inorder List: ", end="")
printList(inorder)

print("Postorder List: ", end="")
printList(postorder)

sol = Solution()

# Build the binary tree and
# print its inorder traversal
root = sol.buildTree(inorder, postorder)

print("Inorder of Unique Binary Tree Created:")
printInorder(root)
print()

                           
                        