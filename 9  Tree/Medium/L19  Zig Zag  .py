
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def f(root):
    ans = []
    if not root:
        return ans
    q = deque()
    q.append(root)
    Flage = True # 
    while q: 
        n = len(q)
        level = [0] * n
        for i in range(n):
            node = q.popleft()

            index = i if Flage else (n - 1 - i)

            level[index] = node.data
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        Flage = not Flage
        ans.append(level)
    return ans

def printans(ans):
    for row in ans:
        for val in row:
            print(val, end=" ")
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res= f(root)
for x in res : 
    for y in x : 
        print(y, end = " ")
    print()



#  i did, code from avi 


print()

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def f(root):
    ans = []
    if not root:
        return ans
    q = deque()
    q.append(root)
    
    flag = 0     
    # leftToRight = True
    while q:
        n = len(q)
        level = [0] * n
        for i in range(n):
            node = q.popleft()

            if flag == 0 : index = i 
            else : index = n-i-1

            # index = i if leftToRight else (n - 1 - i)

            level[index] = node.data
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if flag == 0 : flag =1 
        else : flag = 0          
        # leftToRight = not leftToRight
        ans.append(level)
    return ans

# def printans(ans):
#     for row in ans:
#         for val in row:
#             print(val, end=" ")
#         print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res= f(root)
for x in res : 
    print(*x)
# print(res)



