                            
from typing import List

# -----------------------------------------------------------
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# -----------------------------------------------------------
def buildTree( preorder , inorder  ):
    
    mp ={} # also rep # mp = {val: idx for idx, val in enumerate(inorder)}
    for i in range(0, len(inorder)):
        mp[inorder[i]] = i 

    root = f(preorder, 0, len(preorder)-1, inorder, 0, 
             len(inorder)-1, mp)
    
    return root

def f( preorder, preStart, preEnd, inorder, inStart, inEnd, mp):
    if preStart > preEnd or inStart > inEnd:
        return None

    root = TreeNode(preorder[preStart])
    inRoot = mp[root.val]
    numsLeft = inRoot - inStart
    root.left = f(preorder, preStart + 1, preStart + numsLeft,
                                inorder, inStart, inRoot - 1, mp)

    root.right = f(preorder, preStart + numsLeft + 1, preEnd,
                                    inorder, inRoot + 1, inEnd, mp)

    return root
#------------------------
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

# Function to print the given list
def printList(lst):
    for val in lst:
        print(val, end=" ")
    print()

# ----------------------------------------
if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]
    
    print("Inorder List: ", end="")
    printList(inorder)
    
    print("Preorder List: ", end="")
    printList(preorder)
    

    root = buildTree(preorder, inorder)
    
    print("Inorder of Unique Binary Tree Created:")
    printInorder(root)
    print()
                           
                        