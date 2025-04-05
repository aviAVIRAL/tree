
# leetcode repre 

print()
print()
from typing import List

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: Node) -> List[int]:
        node = root
        st = []
        ans = []
        
        while True:
            if node !=  None: #if node is not None:
                st.append(node)
                node = node.left
            else: # node ==  None:
                if len(st) == 0 : # if not st:
                    break
                node = st.pop()
                ans.append(node.data)
                node = node.right
        
        return ans

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sol = Solution()
result = sol.inorderTraversal(root)

print("Inorder Traversal:", end=" ")
for val in result:
    print(val, end=" ")

print()
print()

# simple repre 

print()
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def f(root) :
    node = root
    st = []
    ans = []
    
    while True:
        if node !=  None: #if node is not None:
            st.append(node)
            node = node.left
        else: # node ==  None:
            if len(st) == 0 : # if not st:
                break
            node = st.pop()
            ans.append(node.data)
            node = node.right
    
    return ans 

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f((root)))

print()
print()