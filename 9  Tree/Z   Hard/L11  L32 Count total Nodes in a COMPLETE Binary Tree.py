

# brute 
                                
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# proper repre 
def f( root, cnt):
    if root is None:
        return
    cnt[0] += 1
    f(root.left, cnt)
    f(root.right, cnt)

def cntNodes( root):
    if root is None:# edge case 
        return 0
    cnt = [0]
    f(root, cnt)
    return cnt[0]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print( cntNodes(root))



  # also repr

# cnt= [0] 
def f( root):
    if root is None:
        return
    cnt[0] += 1

    f(root.left)
    f(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    cnt= [0] 
    f(root)
    print(cnt[0])
                                
                                  

# also      reperesnrtation as  repr ---------------------- 

cnt= [0] # als
def f( root):
    if root is None:
        return
    cnt[0] += 1

    f(root.left)
    f(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    # cnt= [0] 
    f(root)
    print(cnt[0])
                
                                
#  lc rep ............

# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         def f( root):
#      
#             if root == None : return
#             cnt[0] += 1 
#             f( root.left)
#             f( root.right)

#         cnt = [0]
#         f(root)
#         return cnt[0] 
# ............................

# aslo rep as Lc WITH PROPER PASSING CNT ( LIST )

# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         def f( root ,cnt):
#             # nonlocal cnt 
#             if root == None : return
#             cnt[0] += 1 
#             f( root.left ,cnt)
#             f( root.right ,cnt)

#         cnt = [0]
#         f(root ,cnt)
#         return cnt[0] 

