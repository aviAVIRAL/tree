

# levell ode3er se rep se kiya hai bhai 



from collections import deque, defaultdict

# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    # Function to perform vertical order traversal
    # and return a 2D list of node values
    def findVertical(self, root):
        # Map to store nodes based on
        # vertical and level information
        nodes = defaultdict(lambda: defaultdict(lambda: set()))

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical and level information
        q = deque([(root, (0, 0))])

        # BFS traversal
        while q:
            # Retrieve the node and its vertical
            # and level information from
            # the front of the queue
            temp, (x, y) = q.popleft()

            # Insert the node value into the
            # corresponding vertical and level
            # in the map
            nodes[x][y].add(temp.data)

            # Process left child
            if temp.left:
                q.append((temp.left, (x - 1, y + 1)))

            # Process right child
            if temp.right:
                q.append((temp.right, (x + 1, y + 1)))

        # Prepare the final result list
        # by combining values from the map
        ans = []
        for x, y_vals in nodes.items():
            col = []
            for y, values in y_vals.items():
                # Insert node values
                # into the column list
                col.extend(sorted(values))
            # Add the column list
            # to the final result
            ans.append(col)

        return ans

# Helper function to
# print the result
def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()

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

    solution = Solution()

    # Get the Vertical traversal
    verticalTraversal = solution.findVertical(root)

    # Print the result
    print("Vertical Traversal: ")
    printResult(verticalTraversal)
                           
print("......................")
print()
from collections import deque, defaultdict

# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to perform vertical order traversal
    # and return a 2D list of node values
    def findVertical(self, root):
        # Map to store nodes based on vertical information
        nodes = defaultdict(list)  # Changed to defaultdict(list)

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical and level information
        q = deque([(root, (0, 0))])

        # BFS traversal
        while q:
            # Retrieve the node and its vertical
            # and level information from
            # the front of the queue
            temp, (x, y) = q.popleft()

            # Insert the node value into the
            # corresponding vertical in the map
            nodes[x].append(temp.data)  # Changed to append, since we're using lists

            # Process left child
            if temp.left:
                q.append((temp.left, (x - 1, y + 1)))

            # Process right child
            if temp.right:
                q.append((temp.right, (x + 1, y + 1)))

        # Prepare the final result list by sorting node values at each vertical level
        ans = []
        for x in sorted(nodes.keys()):  # Sort by vertical level (x-coordinate)
            ans.append(sorted(nodes[x]))  # Sort nodes at the same vertical level

        return ans

# Helper function to print the result
def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()

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

    solution = Solution()

    # Get the Vertical traversal
    verticalTraversal = solution.findVertical(root)

    # Print the result
    print("Vertical Traversal: ")
    printResult(verticalTraversal)



print("..............")
print()
# also rep 
                           
print("../////////////............")
print()
from collections import deque, defaultdict

# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to perform vertical order traversal
    # and return a 2D list of node values
    def findVertical(self, root):
        # Map to store nodes based on vertical information
        nodes = defaultdict(list)  # Changed to defaultdict(list)

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical and level information
        q = deque(  ) # also rep as  q = deque( [  ] )
        q.append(  (root, (0, 0))   )

        # BFS traversal
        while q:
            # Retrieve the node and its vertical
            # and level information from
            # the front of the queue
            temp, (x, y) = q.popleft()

            # Insert the node value into the
            # corresponding vertical in the map
            nodes[x].append(temp.data)  # Changed to append, since we're using lists

            # Process left child
            if temp.left:
                q.append((temp.left, (x - 1, y + 1)))

            # Process right child
            if temp.right:
                q.append((temp.right, (x + 1, y + 1)))

        # Prepare the final result list by sorting node values at each vertical level
        ans = []
        for x in sorted(nodes.keys()):  # Sort by vertical level (x-coordinate)
            ans.append(sorted(nodes[x]))  # Sort nodes at the same vertical level

        return ans

# als rep 
        # ans = []
        # sol = sorted(nodes)
        # for x in sol  : 
        #     we= sorted(nodes[x])
        #     ans.append(we)
        # return ans 


# Helper function to print the result
def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()

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

    solution = Solution()

    # Get the Vertical traversal
    verticalTraversal = solution.findVertical(root)

    # Print the result
    print("Vertical Traversal: ")
    printResult(verticalTraversal)



print("..............")
print()

# mosr esy rep 
        
print()
from collections import deque, defaultdict

# Node structure for the binary tree
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


print()
# .............................


# inoder rep  reccursiiin se kiya hai 
print()
from collections import deque, defaultdict

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def f(root, x, mp):

    if root is None: return 
    f(root.left, x-1, mp )
    mp[x].append(root.data)
    f(root.right, x + 1, mp)

def findVertical(root): 
    mp = defaultdict(list)
    
    f(root, 0, mp )

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

    ans = findVertical(root)

    print("Vertical Traversal: ")
    
    for x in ans :
        print(*x)
    print()

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


