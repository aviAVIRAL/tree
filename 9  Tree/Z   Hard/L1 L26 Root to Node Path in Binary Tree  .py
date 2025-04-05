

print()
                            
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

arr = [ ]
def f( root, x):
    
    if not root:
        return False

    arr.append(root.data)

    if root.data == x:
        return True

    if f(root.left, x) or f(root.right, x):
        return True

    arr.pop()
    return False

def solve( A, B):
    
    if not A:
        return arr
    f(A, B)

    return arr

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)


    target_leaf_dataue = 7

    path = solve(root, target_leaf_dataue)

    print(path)

                        
print()    
# also rep  
                            
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


arr = [ ]
def f( root, x):
    
    if not root:
        return False

    arr.append(root.data)

    if root.data == x:
        return True

    if f(root.left, x) : return True 
    if f(root.right, x) :return True

    arr.pop()
    return False

def solve( A, B):
    
    if not A:
        return arr
    f(A, B)

    return arr

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)


    target_leaf_dataue = 7

    path = solve(root, target_leaf_dataue)

    print(path)


    # print(f"Path from root to leaf with dataue {target_leaf_dataue}: ", end="")
    # for i in range(len(path)):
    #     print(path[i], end="")
    #     if i < len(path) - 1:
    #         print(" -> ", end="")
                           
                        
print()
print()
# rep                         
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def getPath(self, root, arr, x):
      
        if not root:
            return False

        arr.append(root.data)

        if root.data == x:
            return True

        if self.getPath(root.left, arr, x) or self.getPath(root.right, arr, x):
            return True

        arr.pop()
        return False

    def solve(self, A, B):
     
        arr = []

        if not A:
            return arr
        self.getPath(A, arr, B)

        return arr

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()

    target_leaf_dataue = 7

    path = sol.solve(root, target_leaf_dataue)

    print(f"Path from root to leaf with dataue {target_leaf_dataue}: ", end="")
    for i in range(len(path)):
        print(path[i], end="")
        if i < len(path) - 1:
            print(" -> ", end="")
                           
                        