"""""
Binary Tree Represntation in python_branch
Binary Tree
(1) A structure that represents a binary tree node;
(2) A binary tree using the structure in (1). The nodes are not necessarily ordered 
in any fashion (that would be BST);
(3) An additional function that returns the total number of nodes in the tree in (2).
 It should give the correct answer for any binary tree.

""" ""
COUNT = [6]
# Create Node of Binary search Tree
class BST_Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # Insert node in Binary search Tree


def insert_tree_node(arr, i, n):
    root = None
    # base case recursion
    if i < n:
        root = BST_Node(arr[i])

    # insert left child
    root.left = insert_tree_node(arr, 2 * i + 1, n)

    # insert right child
    root.right = insert_tree_node(arr, 2 * i + 2, n)
    return root


# Function to Print/Display Binary Search Tree
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
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.key)

    # Process left child
    Display_BST(root.left, space)


# Complete Binary Search Tree:
def print_BST(root):
    # space=[0]
    # Pass initial space count as 0
    Display_BST(root, 0)


def count_nodes(root):
    if root == None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

    # ####### Main Function #####


if __name__ == "__main__":

    # creating an empty list
    list1 = []


# Taking elements as input and adding them into list
list1 = list()  # Creation of empty list
while True:
    value = input()
    if value == "":  # If space enterend complete the elements taken by user
        break
    list1.append(value)

root = None
n = len(list1)
root = insert_tree_node(list1, 0, n)

print_BST(root)
p = count_nodes(root)
print("The Total Number of Nodes in Tree are : ---> ", p)

##### If user inut is not required already prestnt data to be used ####
# root = BST_Node(1)
# print(root)

""" ""
#     tree Created will be as like below :
#          1
#         / \
#       None  None

# """ ""

# root.left = BST_Node(2)
# root.right = BST_Node(3)
# """"
# Tree will look like as below :

#                    1
#                 /      \
#                2         3
#               /  \      /  \
#             None None  None None
# """ ""
# root.left.left = BST_Node(4)
# # root.left.left.right = Node(5)
# """"
# Tree will look like as below :

#                    1
#                 /      \
#                2         3
#               /  \      /  \
#             4    None  None None
#           /  \
#          None None
# """ ""
# print_BST(root)
# p = count_nodes(root)
# print("The Total Number of Nodes in Tree are : ---> ", p)
