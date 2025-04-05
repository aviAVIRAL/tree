

                
print()
print()
# simple rep 
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def f(root):
    ans = []
    if root is None:
        return ans
    st1, st2 = [], []
    st1.append(root)
    while st1:
        node = st1.pop()
        st2.append(node)
        if node.left is not None:# if node.left :
            st1.append(node.left)
        if node.right is not None:
            st1.append(node.right)
    while st2:
        ans.append(st2[-1].data)
        st2.pop()
    return ans

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(f(root))

print()                            
print()

# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to return the postOrder
# traversal of a binary tree using
# two stacks
def postOrder(root):
    # Vector to store
    # postorder traversal
    ans = []

    # If the tree is empty,
    # return an empty traversal
    if root is None:
        return ans

    # Two stacks for
    # iterative traversal
    st1, st2 = [], []

    # Push the root node
    # onto the first stack
    st1.append(root)

    # Iterative traversal to populate
    # st2 with nodes in ans
    while st1:
        # Get the top node from st1
        node = st1.pop()

        # Push the node onto st2
        st2.append(node)

        # Push left child onto st1 if exists
        if node.left is not None:
            st1.append(node.left)

        # Push right child onto st1 if exists
        if node.right is not None:
            st1.append(node.right)

    # Populate the ans traversal
    # list by popping st2
    while st2:
        ans.append(st2[-1].data)
        st2.pop()

    # Return the
    # ans traversal
    return ans


# Function to print the
# elements of a list
def printList(lst):
    # Iterate through the list
    # and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting postorder traversal
    result = postOrder(root)

    # Printing the postorder
    # traversal result
    print("Postorder traversal: ", end="")
    printList(result)
                           
        