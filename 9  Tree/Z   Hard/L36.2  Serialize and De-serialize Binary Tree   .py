

from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Encodes the tree into a single string
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        # Use a queue for level-order traversal
        q = deque([root])
        result = []
        
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("#")
           
        return " ".join(result)

    # Decodes the encoded data to a tree
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        
        # Split the data into values
        values = data.split(" ")
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1
        
        while q:
            node = q.popleft()
            
            # Add left child
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1
            
            # Add right child
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        
        return root

# Helper function to print the inorder traversal of a tree
def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Test the implementation
if __name__ == "__main__":
    # Construct a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()

    print("Original Tree: ", end="")
    inorder(root)
    print()

    # Serialize the tree
    serialized = solution.serialize(root)
    print("Serialized:", serialized)

    # Deserialize the serialized string
    deserialized = solution.deserialize(serialized)
    print("Tree after deserialization: ", end="")
    inorder(deserialized)
    print()
                           
print()
print()
# ..................ALSO REPRE ..................


from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Encodes the tree into a single string
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        # Use a queue for level-order traversal
        q = deque([root])
        result = []
        
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("#")
        
        print(result)
        return ",".join(result)

    # Decodes the encoded data to a tree
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        
        # Split the data into values
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1
        
        while q:
            node = q.popleft()
            
            # Add left child
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1
            
            # Add right child
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        
        return root

# Helper function to print the inorder traversal of a tree
def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Test the implementation
if __name__ == "__main__":
    # Construct a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()

    print("Original Tree: ", end="")
    inorder(root)
    print()

    # Serialize the tree
    serialized = solution.serialize(root)
    print("Serialized:", serialized)

    # Deserialize the serialized string
    deserialized = solution.deserialize(serialized)
    print("Tree after deserialization: ", end="")
    inorder(deserialized)
    print()
                           
# ----------   also rep  

from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Encodes the tree into a single string
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        # Use a queue for level-order traversal
        q = deque([root])
        result = []
        
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("#")
           
        return "*".join(result)

    # Decodes the encoded data to a tree
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        
        # Split the data into values
        values = data.split("*")
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1
        
        while q:
            node = q.popleft()
            
            # Add left child
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1
            
            # Add right child
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        
        return root

# Helper function to print the inorder traversal of a tree
def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Test the implementation
if __name__ == "__main__":
    # Construct a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()

    print("Original Tree: ", end="")
    inorder(root)
    print()

    # Serialize the tree
    serialized = solution.serialize(root)
    print("Serialized:", serialized)

    # Deserialize the serialized string
    deserialized = solution.deserialize(serialized)
    print("Tree after deserialization: ", end="")
    inorder(deserialized)
    print()
                           
                        