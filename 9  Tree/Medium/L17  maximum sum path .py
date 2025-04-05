
                            
class Node:
    def __init__(self, val):
        # Constructor to initialize
        # the node with a value
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMaxPathSum(self, root, maxi):
        # Recursive function to find the maximum path sum
        # for a given subtree rooted at 'root'
        # The variable 'maxi' is a reference parameter
        # updated to store the maximum path sum encountered

        # Base case: If the current node is None, return 0
        if root is None:
            return 0

        # Calculate the maximum path sum
        # for the left and right subtrees
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))

        # Update the overall maximum
        # path sum including the current node
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.data)

        # Return the maximum sum considering
        # only one branch (either left or right)
        # along with the current node
        return max(leftMaxPath, rightMaxPath) + root.data

    def maxPathSum(self, root):
        # Function to find the maximum
        # path sum for the entire binary tree

        # Initialize maxi to the
        # minimum possible integer value
        maxi = [float('-inf')] 
        # Call the recursive function to
        # find the maximum path sum
        self.findMaxPathSum(root, maxi)
        # Return the final maximum path sum
        return maxi[0]

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# Creating an instance of the Solution class
solution = Solution()

# Finding and printing the maximum path sum
maxPathSum = solution.maxPathSum(root)
print("Maximum Path Sum:", maxPathSum)
                           
                        