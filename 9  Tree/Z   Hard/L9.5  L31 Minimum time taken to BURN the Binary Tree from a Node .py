# striver represnattaiion hai  


from collections import deque

# Definition for a binary tree node
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to find the maximum distance from the target node
def findMaxDistance(parentMap, target):
    q = deque([target])
    visited = {target: 1}
    maxDistance = 0
    while q:
        size = len(q)
        foundNewNode = False #  ye  bata ta hai ki kuch na kuch bhai burn kr diya hai node ( matlab q mein kuch na kuch dal diya hai bhai )


        for _ in range(size):
            node = q.popleft()
            # Visit left child
            if node.left and node.left not in visited:
                visited[node.left] = 1
                q.append(node.left)
                foundNewNode = True # ye true bata ta hai ki kuch na kuch bhai burn kr diya hai node ( matlab q mein kuch na kuch dal diya hai bhai )
            # Visit right child
            if node.right and node.right not in visited:
                visited[node.right] = 1
                q.append(node.right)
                foundNewNode = True
            # Visit parent node
            if node in parentMap and parentMap[node] not in visited:
                visited[parentMap[node]] = 1
                q.append(parentMap[node])
                foundNewNode = True
        # If a new node was added, increase the distance
        if foundNewNode:
            maxDistance += 1
    return maxDistance

# Function to map all parent nodes and find the target node
def mapParents(root, parentMap, start):
    q = deque([root])
    targetNode = None

    while q:
        node = q.popleft()

        # Check if the current node is the target
        if node.val == start:
            targetNode = node # targetNode is res in strive video

        # Map parent for the left child
        if node.left:
            parentMap[node.left] = node
            q.append(node.left)

        # Map parent for the right child
        if node.right:
            parentMap[node.right] = node
            q.append(node.right)

    return targetNode

# Main function to calculate the time to burn the tree
def timeToBurnTree(root, start):
    parentMap = {}
    targetNode = mapParents(root, parentMap, start)
    return findMaxDistance(parentMap, targetNode)

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


print()
# also rep as 



from collections import deque

# Definition for a binary tree node
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to find the maximum distance from the target node
def findMaxDistance(parentMap, target):
    q = deque([target])
    visited = {target: 1}
    maxDistance = 0
    while q:
        size = len(q)
        foundNewNode = 0 #  impo 

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

# Function to map all parent nodes and find the target node
def mapParents(root, parentMap, start):
    q = deque([root])
    targetNode = None

    while q:
        node = q.popleft()

        # Check if the current node is the target
        if node.val == start:
            targetNode = node # targetNode is res in strive video

        # Map parent for the left child
        if node.left:
            parentMap[node.left] = node
            q.append(node.left)

        # Map parent for the right child
        if node.right:
            parentMap[node.right] = node
            q.append(node.right)

    return targetNode

# Main function to calculate the time to burn the tree
def timeToBurnTree(root, start):
    parentMap = {}
    targetNode = mapParents(root, parentMap, start)
    return findMaxDistance(parentMap, targetNode)

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
