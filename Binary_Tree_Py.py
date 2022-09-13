"""""
Binary Tree Represntation in python_branch
Binary Tree
(1) A structure that represents a binary tree node;
(2) A binary tree using the structure in (1). The nodes are not necessarily ordered 
in any fashion (that would be BST);
(3) An additional function that returns the total number of nodes in the tree in (2).
 It should give the correct answer for any binary tree.

""" ""
COUNT = [5]

# Indiviual Node in Python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Function to print binary tree in 2D
# It does reverse inorder traversal
def Display_BST(root, space):

    # Base case
    if root == None:
        return

    # Increase distance between levels
    space += COUNT[0] - 1

    # Process right child first
    Display_BST(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    Display_BST(root.left, space)


# Wrapper over print2DUtil()
def print_BST(root):

    # space=[0]
    # Pass initial space count as 0
    Display_BST(root, 0)


def count_nodes(root):
    if root == None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    # Creation of Root
    root = Node(1)
print(root)
"""""
    tree Created will be as like below :
         1
        / \
      None  None

""" ""

root.left = Node(2)
root.right = Node(3)
""""
Tree will look like as below :

                   1
                /      \
               2         3
              /  \      /  \                
            None None  None None       
""" ""
root.left.left = Node(4)
# root.left.left.right = Node(5)
""""
Tree will look like as below :

                   1
                /      \
               2         3
              /  \      /  \                
            4    None  None None
          /  \
         None None       
""" ""
print_BST(root)
p = count_nodes(root)
print("The Total Number of Nodes in Tree are : ---> ", p)
