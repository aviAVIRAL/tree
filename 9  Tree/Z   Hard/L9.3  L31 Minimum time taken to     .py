

from collections import deque

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f(root, start): # parent + taget dono return krwa diya bhai is mein 
    parentMap ={}
    q = deque([root])
    # Target = None
    Target = None
    while q:
        node = q.popleft()

        if node.val == start:
            Target = node 
        # Map parent for the left child
        if node.left:
            parentMap[node.left] = node
            q.append(node.left)

        # Map parent for the right child
        if node.right:
            parentMap[node.right] = node
            q.append(node.right)
    # return Target
    return parentMap, Target 
 

def timeToBurnTree(root, start): # main function 
    
    parentMap, Target  = f(root, start) # bhai trick is he code mein kr diya dhamaal  
    
    if not Target: # edge case bhai 
        return -1
    
    q = deque([Target])
    visited = {Target: 1}
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

    start = 4  # Node to start burning the tree
    print("Time to burn the tree:", timeToBurnTree(root, start))
