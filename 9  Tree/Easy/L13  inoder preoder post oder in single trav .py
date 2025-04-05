class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def pre_in_post_traversal(root):
    
    pre, in_order, post = [], [], []
    if root is None:# Edge case 
        return []
    st =  [(root, 1)]
    while st:
        node, state = st.pop()
        if state == 1:
            pre.append(node.data)
            state = 2
            st.append((node, state))
            if node.left:#kya left exist krraha hai 
                st.append((node.left, 1))
        elif state == 2:
            in_order.append(node.data)
            state = 3
            st.append((node, state))
            if node.right:
                st.append((node.right, 1))
        else:
            post.append(node.data)
    return [pre, in_order, post]

def print_list(lst):
    for num in lst:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    traversals = pre_in_post_traversal(root)
    pre, in_order, post = traversals

    print("Preorder traversal: ", end="")
    print_list(pre)

    print("Inorder traversal: ", end="")
    print_list(in_order)

    print("Postorder traversal: ", end="")
    print_list(post)
print()
print()

# simple rep 
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root):
    
    pre, in_order, post = [], [], []
    if root is None:# Edge case 
        return []
    st =  [(root, 1)]     # also rep     st =  []
                                     #   st.append( (root, 1) )
    while st:
        node, state = st.pop()
        if state == 1:
            pre.append(node.data)
            state = 2 # state += 1 
            st.append((node, state))
            if node.left:
                st.append((node.left, 1))
        elif state == 2:
            in_order.append(node.data)
            state = 3
            st.append((node, state))
            if node.right:
                st.append((node.right, 1))
        else:
            post.append(node.data)
    return pre, in_order, post

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    ans = f(root)
    # print(ans) #  ( [1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [4, 5, 2, 3, 1] ) 
    print()
    for x in ans : 
        print(x)
    print()
print()
# # op  
# [1, 2, 4, 5, 3]
# [4, 2, 5, 1, 3]
# [4, 5, 2, 3, 1]