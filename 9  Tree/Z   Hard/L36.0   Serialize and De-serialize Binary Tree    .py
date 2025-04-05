
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    #      1
    #    /   \
    #   2     3
    #        / \
    #       4   5
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
            if node == None: result.append("#") 
            else: result.append(str(node.val))
            if node:
                q.append(node.left)
                q.append(node.right)

     # result     : ['1', '2', '3', '#', '#', '4', '5', '#', '#', '#', '#']       
        x = " ".join(result)  #  x   : 1 2 3 # # 4 5 # # # #
        return x 

# also rep ---------------
        # while q:
        #     node = q.popleft()
        #     if node == None: result.append("#") 
        #     if node:
        #         result.append(str(node.val))
        #         q.append(node.left)
        #         q.append(node.right)
            
        # return " ".join(result)

#also re present ==============
        # while q:
        #     node = q.popleft()
        #     if node:
        #         result.append(str(node.val))
        #         q.append(node.left)
        #         q.append(node.right)
        #     else:
        #         result.append("#")
           
        # return " ".join(result)

#------------------------------------------
    # Decodes the encoded data to a tree
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None     # data : 1 2 3 # # 4 5 # # # #
        
        # Split the data into arr
        arr = data.split(" ")
        # arr :  ['1', '2', '3', '#', '#', '4', '5', '#', '#', '#', '#']
        
        root = TreeNode(int(arr[0]))
        q = deque([root])
        i = 1
        
        while q:
            node = q.popleft()
            
            # Add left child
            if arr[i] != "#":
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1
            
            # Add right child
            if arr[i] != "#":
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1
        
        return root


def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

if __name__ == "__main__":
  
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
                           
                        