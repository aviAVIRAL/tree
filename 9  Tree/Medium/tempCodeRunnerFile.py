




# also rep as 
print()
        
print()
from collections import deque, defaultdict

# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


mp = defaultdict(list) # outside the funtion define  kr diy bhai 

def f(root, x):

    if root is None: return 
    f(root.left, x-1 )
    mp[x].append(root.data)
    f(root.right, x + 1)

def findVertical(root):                                                                                                                                       
    
    f(root, 0 )

    ans = []
    sol = sorted(mp)
    for x in sol  : 
        we= sorted(mp[x])
        ans.append(we)
    return ans 


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    ans = findVertical(root)

    print("Vertical Traversal: ")
    
    for x in ans :
        print(*x)
    print()





print()
from collections import deque, defaultdict

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def findVertical(root):
    mp = defaultdict(list)  # Changed to defaultdict(list)

    q = deque(  ) # also rep as  q = deque( [  ] )
    q.append(  (root,  0)   )

    while q:

        node, x = q.popleft()

        mp[x].append(node.data)  # Changed to append, since we're using lists

        if node.left:
            q.append((node.left, x-1))

        if node.right:
            q.append((node.right, x+1))

    ans = []
    sol = sorted(mp)
    for x in sol  : 
        we= sorted(mp[x])
        ans.append(we)
    return ans 


if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)


    # Get the Vertical traversal
    ans = findVertical(root)

    # Print the result
    print("Vertical Traversal: ")
    
    for x in ans :
        print(*x)
    print()
    # print(verticalTraversal)

