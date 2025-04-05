
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(root1, root2):
    if root1 is None or root2 is None:
        return root1 == root2
    
    if root1.data != root2.data : return False
    
    return ( check(root1.left, root2.right) and
            check(root1.right, root2.left))

def f(root):
    if not root:
        return True
    return check(root.left, root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)

    print()

    f(root)

    res = f(root)

    print(res)

    print()
    print()
    print()

# ,,,,,,,,,repre ,,,,,,,,,,,,,,,
# 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(root1, root2):
    if root1 is None or root2 is None:
        return root1 == root2
    return (root1.data == root2.data and
            check(root1.left, root2.right) and
            check(root1.right, root2.left))

def f(root):
    if not root:
        return True
    return check(root.left, root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)

    print()

    f(root)

    res = f(root)

    print(res)

    print()
    print()
    print()
