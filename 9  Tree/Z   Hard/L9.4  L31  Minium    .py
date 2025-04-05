
# impo 

  # TARGET = root.left.left
# IMPO adress / node full goven hai therfore no need to find taget value bhai 


from collections import deque

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f(root): 
    parentMap ={}
    q = deque([root])
  
    while q:
        node = q.popleft()

        if node.left:
            parentMap[node.left] = node
            q.append(node.left)

        if node.right:
            parentMap[node.right] = node
            q.append(node.right)
    return parentMap
 

def timeToBurnTree(root, TARGET): # main function 
    
    parentMap  = f(root) #  
    
    q = deque([TARGET])
    visited = {TARGET: 1}
    maxDistance = 0
    while q:
        size = len(q)
        foundNewNode = 0 

        for _ in range(size):
            node = q.popleft()
            # Visit left child
            if node.left and node.left not in visited:
                visited[node.left] = 1
                q.append(node.left)
                foundNewNode = 1 # ye 1 bata ta hai ki kuch na kuch bhai burn kr diya hai node ( matlab q mein kuch na kuch dal diya hai bhai )
            # Visit right child
            if node.right and node.right not in visited:
                visited[node.right] = 1
                q.append(node.right)
                foundNewNode = 1
            # Visit parent node
            if node in parentMap and parentMap[node] not in visited:
                visited[parentMap[node]] = 1
                q.append(parentMap[node])
                foundNewNode = 1
        # If a new node was added, increase the distance
        if foundNewNode:
            maxDistance += 1
    return maxDistance


# -------------------------------------
# Example usage
if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    TARGET = root.left.left # IMPO adress / node full goven hai therfore no need to find taget value bhai 
    print("Time to burn the tree:", timeToBurnTree(root, TARGET))
