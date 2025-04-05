

print()
print()

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root, arr):
    if not root: # if root is None:  # if root == None:
        return
    arr.append(root.data)
    f(root.left, arr)
    f(root.right, arr)

def f(root):
    arr = []
    f(root, arr)
    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    Ans = f(root)
    print("f Traversal:", end=" ")
    for x in Ans:
        print(x, end=" ")
    print()

print()
# also rep more simple 


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root):
    if not root:
        return
    arr.append(root.data)
    f(root.left)
    f(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    arr = []
    f(root)
    print(arr)    #   print(*arr)


# also represent as  

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root, arr):
    if not root:
        return
    arr.append(root.data)
    f(root.left, arr)
    f(root.right, arr)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    arr = []
    f(root, arr)
    print(arr)    #   print(*arr)

print()
print("________")


# rep  

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class solution : 
    def f(self, root, arr):
        if not root:
            return
        arr.append(root.data)
        self.f(root.left, arr) # self impo 
        self.f(root.right, arr)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    sol = solution()
    arr = []
    sol.f(root, arr)
    print(arr)    

print()
print("...........")
# also repre  ....................................... 
print()
print()

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root):
    if not root:
        return
    print(root.data, end = " ")
    f(root.left)
    f(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # arr = []
    f(root)
    # print(arr)


# ALSO REP R 
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def f(self, root):
        if not root:
            return
        print(root.data, end= " ")
        self.f(root.left)
        self.f(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    sol = Solution()

    sol.f(root)

print()
print()
print()
 
# also pre striver in video for more simple 

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(node):  # root ki repalce with name node
    if not node:    
        return
    print(node.data, end = " ")
    f(node.left)
    f(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # arr = []
    f(root)
    # print(arr)

print()
print()
print()
print()