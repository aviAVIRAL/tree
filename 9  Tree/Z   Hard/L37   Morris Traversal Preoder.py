


                            
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getInorder( root):
    inorder = []
    cur = root
    while  cur :  #  cur is not None:

        if cur.left == None: # is None:
            inorder.append(cur.val)
            cur = cur.right
        
        else:
            prev = cur.left
            while prev.right !=  None and prev.right != cur: # while prev.right  and prev.right != cur:
                prev = prev.right

            if prev.right == None: # case 1 threade make
                prev.right = cur
                inorder.append(cur.val) # impo yaha kr diya hai bus  
                cur = cur.left

            else:                   # case 2 thr. remove
                prev.right = None
                # inorder.append(cur.val) # preoder ke liyr bus ye change   
                cur = cur.right

    return inorder


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)


    inorder = getInorder(root)

    print(" Morris Inorder Traversal:", end=" ")
    for val in inorder:
        print(val, end=" ")
    print()
                           
                        

