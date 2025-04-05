                           
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root):
    if not root:
        return True
    
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)

    if abs(leftHeight - rightHeight) <= 1 \
        and f(root.left) \
        and f(root.right):
        return True

    # if abs(leftHeight - rightHeight) <= 1 and f(root.left)and f(root.right):

    return False

def getHeight(  root):
    if not root:
        return 0
    leftHeight =  getHeight(root.left)
    rightHeight =  getHeight(root.right)
    return max(leftHeight, rightHeight) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)


# Checking if the tree is balanced
if f(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")


# allso rep brute striver 
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def fun(root):
    if not root:
        return True
    
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)

    if abs(leftHeight - rightHeight) > 1: return False
    
    ln = fun(root.left) # see yaha se 
    rn = fun(root.right)
    if ln != True or rn != True:  return False
    return True

    # if abs(leftHeight - rightHeight) <= 1 and f(root.left)and f(root.right):



def getHeight(  root):
    if not root:
        return 0
    leftHeight =  getHeight(root.left)
    rightHeight =  getHeight(root.right)
    return max(leftHeight, rightHeight) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)



# Checking if the tree is balanced
if fun(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")
                    


#  ..............................................................>      
                        
 # optimal                                
# Node structure for the binary tree


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isBalanced(root):
    return dfsHeight(root) != -1

def dfsHeight(root):
    if not root:
        return 0
    
    left_height = dfsHeight(root.left)
    right_height = dfsHeight(root.right)
    
    if left_height == -1:
        return -1
    if right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    
    return max(left_height, right_height) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

if isBalanced(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")

# also rep  as 

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(node):
            if node == None:
                return 0
            
            lh = check(node.left)
            rh = check(node.right)
            
            if lh == -1 or  rh == -1: return -1
            if abs(lh-rh) > 1: return -1 
            
            return 1 + max(lh, rh)
        
        return check(root) != -1
