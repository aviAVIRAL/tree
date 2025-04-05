


# brute  

# rep 1 
                           
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

maxi = 0    # global variable 
def f(root):
    if not root:
        return 0
    
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


# rep 2 using arr

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root, maxi):
    if not root:
        return 
    
    lh = getHeight(root.left)
    rh = getHeight(root.right)

    # Update the maximum diameter
    maxi[0] = max(lh + rh, maxi[0])  
    f(root.left, maxi)
    f(root.right, maxi)

def getHeight(root):
    if not root:
        return 0
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)
    return max(leftHeight, rightHeight) + 1

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# impo 
maxi = [-1]  # List allows updating inside the function
f(root, maxi)
print(maxi[0])


# rep 3 first prefer reason leetcode eAsy representation 

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


maxi = [ -1 ] # outside the fun i define  arr 

def f(root):
    if not root:
        return True
    
    lh = getHeight(root.left)
    rh = getHeight(root.right)

    maxi[0] = max(lh + rh, maxi[0])  
    f(root.left)
    f(root.right)

def getHeight(root):
    if not root:
        return 0
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)
    return max(leftHeight, rightHeight) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

maxi = [-1]  
f(root)
print(maxi[0])



# optimal 



class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def diameterOfBinaryTree( root):
    diameter = [0]
    height(root, diameter)
    return diameter[0]

def height( node, diameter):
    if not node:
        return 0
    lh = height(node.left, diameter)
    rh = height(node.right, diameter)
    diameter[0] = max(diameter[0], lh + rh)
    return 1 + max(lh, rh)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)


    diameter = diameterOfBinaryTree(root)
    print("diameter of the BT:", diameter)


