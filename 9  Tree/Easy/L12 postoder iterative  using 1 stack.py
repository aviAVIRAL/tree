# memory algo type ka hai 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def f(root):
    ans = []
    if not root: # if root == Noene 
        return ans

    curr = root
    st = []
    while st or curr:
        if curr:
            st.append(curr)
            curr = curr.left
        else:
            temp = st[-1].right
            if temp == None:# if not temp:
                temp = st.pop()
                ans.append(temp.data)
                while st and temp == st[-1].right:
                    temp = st.pop()
                    ans.append(temp.data)
            else: # reassign curr 
                curr = temp
    return ans 
