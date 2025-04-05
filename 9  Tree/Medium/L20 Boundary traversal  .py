


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def isLeaf(root):
    return not root.left and not root.right

# # also rep  
# def isLeaf( root):
#     if not root.left and not root.right: return True 
#     else : return False
def addLeftBoundary(root, res):
    curr = root.left
    while curr:
        if not isLeaf(curr):
            res.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def addRightBoundary(root, res):
    curr = root.right
    temp = []
    while curr:
        if not isLeaf(curr):
            temp.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    for i in range(len(temp) - 1, -1, -1):
        res.append(temp[i])

def addLeaves(root, res):
    if isLeaf(root):
        res.append(root.data)
        return
    if root.left:
        addLeaves(root.left, res)
    if root.right:
        addLeaves(root.right, res)

def f( root):
    res = []
    if not root:
        return res
    if not isLeaf(root):
        res.append(root.data)
    addLeftBoundary(root, res)
    addLeaves(root, res)
    addRightBoundary(root, res)
    return res



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


res = f(root)

for x in res : 
    print(x, end = " ")


# also rep 

print()


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def isLeaf(root):
    return not root.left and not root.right

# # also rep  
# def isLeaf( root):
#     if not root.left and not root.right: return True 
#     else : return False
def addLeftBoundary(node, res):
    
    while node:
        if not isLeaf(node):
            res.append(node.data)
        if node.left:
            node = node.left
        else:
            node = node.right

def addRightBoundary(node, res):
    temp = []
    while node:
        if not isLeaf(node):
            temp.append(node.data)
        if node.right:
            node = node.right
        else:
            node = node.left
    for i in range(len(temp) - 1, -1, -1):
        res.append(temp[i])

def addLeaves(root, res):
    if isLeaf(root):
        res.append(root.data)
        return
    if root.left:
        addLeaves(root.left, res)
    if root.right:
        addLeaves(root.right, res)

def f( root):
    res = []
    if not root:
        return res
    if not isLeaf(root):
        res.append(root.data)
    addLeftBoundary(root.left, res)
    addLeaves(root, res)
    addRightBoundary(root.right, res)
    return res



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


res = f(root)

for x in res : 
    print(x, end = " ")
print()
print()


# .............................
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isLeaf( root):
    """
    Function to check if a node is a leaf
    """
    return not root.left and not root.right

# # also rep  
# def isLeaf( root):
#     if not root.left and not root.right: return True 
#     else : return False 

def addLeftBoundary( root, res):
    """
    Function to add the left boundary of the tree
    """
    curr = root.left
    while curr:
        if not isLeaf(curr):
            # If the current node is not a leaf,
            # add its value to the result
            res.append(curr.data)
        # Move to the left child if it exists,
        # otherwise move to the right child
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def addRightBoundary( root, res):
    """
    Function to add the right boundary of the tree
    """
    curr = root.right
    temp = []
    while curr:
        if not isLeaf(curr):
            # If the current node is not a leaf,
            # add its value to a temporary vector
            temp.append(curr.data)
        # Move to the right child if it exists,
        # otherwise move to the left child
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    # Reverse and add the values from
    # the temporary vector to the result
    for i in range(len(temp) - 1, -1, -1):
        res.append(temp[i])

def addLeaves( root, res):
    """
    Function to add the leaves of the tree
    """
    if isLeaf(root):
        # If the current node is a leaf,
        # add its value to the result
        res.append(root.data)
        return
    # Recursively add leaves of
    # the left and right subtrees
    if root.left:
        addLeaves(root.left, res)
    if root.right:
        addLeaves(root.right, res)

def printBoundary( root):
    """
    Main function to perform the
    boundary traversal of the binary tree
    """
    res = []
    if not root:
        return res
    # If the root is not a leaf,
    # add its value to the result
    if not isLeaf(root):
        res.append(root.data)

    # Add the left boundary, leaves,
    # and right boundary in order
    addLeftBoundary(root, res)
    addLeaves(root, res)
    addRightBoundary(root, res)

    return res

# Helper function to......................
# print the result
def printResult(result):
    for val in result:
        print(val, end=" ")
    print()

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Get the boundary traversal
result = printBoundary(root)

# Print the result
print("Boundary Trav", end=" ")
printResult(result)
                           
                        