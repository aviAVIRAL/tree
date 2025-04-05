

# rep 1 
                           
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

maxi = 0    # global variable 
def f(root):
    if  root is None:
        return
    
    global maxi # impo 
    
    lh = height(root.left)
    rh = height(root.right)

    maxi = max(lh + rh , maxi ) 
    f(root.left)
    f(root.right)


def height(  root):
    if not root:
        return 0
    leftHeight =  height(root.left)
    rightHeight =  height(root.right)
    return 1 + max(leftHeight, rightHeight) 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)


f(root)
print(maxi)

Let’s dry-run the provided code deeply to understand each step.

Tree Structure:
plaintext
Copy code
         1
       /   \
      2     3
     / \
    4   5
         \
          6
           \
            7
Initial Setup
Global variable: maxi = 0

This stores the maximum diameter (sum of heights of left and right subtrees for any node).
f(root) is called: Traverses the tree to calculate diameter and calls height(root).

Execution Flow
Step 1: f(root) where root = Node(1)
Check if root is None: Not None, continue.
Call height(root.left) (left subtree of Node 1):
Step 2: height(root.left) where root.left = Node(2)
Check if root.left is None: Not None, continue.
Call height(root.left.left) (left subtree of Node 2):
Step 3: height(root.left.left) where root.left.left = Node(4)
Check if root.left.left is None: Not None, continue.
Call height(root.left.left.left) (left subtree of Node 4):
root.left.left.left is None, return 0.
Call height(root.left.left.right) (right subtree of Node 4):
root.left.left.right is None, return 0.
Compute height of Node 4:
leftHeight = 0, rightHeight = 0
height = 1 + max(0, 0) = 1
Return 1 to the caller (height(root.left) for Node 2).
Step 4: height(root.left.right) where root.left.right = Node(5)
Check if root.left.right is None: Not None, continue.
Call height(root.left.right.left) (left subtree of Node 5):
root.left.right.left is None, return 0.
Call height(root.left.right.right) (right subtree of Node 5):
Step 5: height(root.left.right.right) where root.left.right.right = Node(6)
Check if root.left.right.right is None: Not None, continue.
Call height(root.left.right.right.left) (left subtree of Node 6):
root.left.right.right.left is None, return 0.
Call height(root.left.right.right.right) (right subtree of Node 6):
Step 6: height(root.left.right.right.right) where root.left.right.right.right = Node(7)
Check if root.left.right.right.right is None: Not None, continue.
Call height(root.left.right.right.right.left) (left subtree of Node 7):
root.left.right.right.right.left is None, return 0.
Call height(root.left.right.right.right.right) (right subtree of Node 7):
root.left.right.right.right.right is None, return 0.
Compute height of Node 7:
leftHeight = 0, rightHeight = 0
height = 1 + max(0, 0) = 1
Return 1 to the caller (height(root.left.right.right) for Node 6).
Step 7: Back to height(root.left.right.right) for Node 6
Compute height of Node 6:
leftHeight = 0, rightHeight = 1
height = 1 + max(0, 1) = 2
Return 2 to the caller (height(root.left.right) for Node 5).
Step 8: Back to height(root.left.right) for Node 5
Compute height of Node 5:
leftHeight = 0, rightHeight = 2
height = 1 + max(0, 2) = 3
Return 3 to the caller (height(root.left) for Node 2).
Step 9: Back to height(root.left) for Node 2
Compute height of Node 2:
leftHeight = 1 (from Node 4), rightHeight = 3 (from Node 5)
height = 1 + max(1, 3) = 4
Return 4 to the caller (height(root.left) for Node 1).
Step 10: height(root.right) where root.right = Node(3)
Check if root.right is None: Not None, continue.
Call height(root.right.left) (left subtree of Node 3):
root.right.left is None, return 0.
Call height(root.right.right) (right subtree of Node 3):
root.right.right is None, return 0.
Compute height of Node 3:
leftHeight = 0, rightHeight = 0
height = 1 + max(0, 0) = 1
Return 1 to the caller (height(root.right) for Node 1).
Step 11: Back to f(root) for Node 1
Compute diameter at Node 1:
lh = 4 (from Node 2), rh = 1 (from Node 3)
diameter = lh + rh = 4 + 1 = 5
Update maxi = max(5, 0) = 5
**Call f(root.left) and f(root.right) recursively to compute diameter for their subtrees.
Recursive Calls for f(root.left) and f(root.right)
Similar recursive steps are repeated for the left and right subtrees, but the maximum diameter (maxi = 5) remains unchanged, as no larger path exists.
Final Output
After all recursive calls, the program prints maxi = 5, which corresponds to the longest path (from Node 4 to Node 7).