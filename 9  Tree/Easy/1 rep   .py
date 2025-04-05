# simple rep 

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root):
    if not root:
        return
    arr.append(root.data)
    f(root.left)
    f(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    arr = []
    f(root)
    print(arr)    #   print(*arr)


