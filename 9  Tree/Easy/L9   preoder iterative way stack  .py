print()
# si,ple repr e

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def f( root) :
    ans = []

    if root is None:
        return ans
    
    st = []
    st.append(root)
    
    while st:#while st != []:while len(st)!= 0:
        node = st.pop()
        
        ans.append(node.val)
        
        if node.right:   # pheile right reason LIFO
            st.append(node.right)
        
        if node.left:
            st.append(node.left)
    
    return ans

# main()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f(root))

print()
print()

# leetcode repre 
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        if root is None:
            return ans
        
        st = []
        st.append(root)
        
        while st:#while st != []:while len(st)!= 0:
            root = st.pop()
            
            ans.append(root.val)
            
            if root.right:   # pheile right reason LIFO
                st.append(root.right)
            
            if root.left:
                st.append(root.left)
        
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Initializing the Solution class
sol = Solution()

# Getting the preorder traversal
result = sol.preorderTraversal(root)

# Displaying the preorder traversal result
print("Preorder Traversal:", end=" ")
for val in result:
    print(val, end=" ")
print()
                           
                        