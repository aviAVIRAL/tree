
# optimal  
# short cut rerpre 






# optimal 


class TreeNode:
    def __init__( self,x):
        self.val = x
        self.left = None
        self.right = None


def findHeightLeft( node):
    hght = 0
    while node:
        hght += 1
        node = node.left
    return hght

def findHeightRight( node):
    hght = 0
    while node:
        hght += 1
        node = node.right
    return hght
                                
                     

def countNodes( root):

    if not root:
        return 0

    lh = findHeightLeft(root)
    rh = findHeightRight(root)

    if lh == rh:
        return (1 << lh) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print(countNodes(root))
                            

# optimal 
            #   prooper representation  
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
 
        if not root:
            return 0

        lh = self.findHeightLeft(root)
        rh = self.findHeightRight(root)

        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def findHeightLeft(self, node):
        hght = 0
        while node:
            hght += 1
            node = node.left
        return hght

    def findHeightRight(self, node):
        hght = 0
        while node:
            hght += 1
            node = node.right
        return hght


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    totalNodes = sol.countNodes(root)

    print(f"Total number of nodes : {totalNodes}")
                                
                            