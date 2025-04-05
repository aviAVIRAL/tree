 # i m p  
# queue in python3,12 version mein error de rahah hai 
# code sahee hai 100 % but 
# error is coming 
# :  ImportError: cannot import name 'Queue' from 'queue'
#


# 100 % corect code 

# not work in  3.12 python version only 



import queue # from queue import Queue 

class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        ans = []
        if root is None:
            return ans
        
        q = queue.Queue()
        q.put(root)
 
        while q.qsize() != 0 : # working 100 % youtuber fourofour
        # while not q.empty(): by striker 
        # while  q.empty() == 0 : # woking 
        # while q :  not working  do not use it 
            size = q.qsize()
            level = []
 
            for _ in range(size):
                node = q.get() # remove 
                level.append(node.val)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            
            ans.append(level)
        
        return ans

def printVector(vec):
    print(" ".join(map(str, vec)))

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")

    for level in result:
        printVector(level)

print()
