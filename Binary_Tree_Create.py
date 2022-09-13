# Solution in Python to:
# 1. Declare a Tree structure
# 2. Insert nodes into the tree and not make it BST
# 3. Print and count the inserted nodes

# Tree structure declaration
class treeNode:  # Node creation with |key|left|right|
    def __init__(node, data):
        node.key = data
        node.left = None
        node.right = None


"""Function to insert a node in binary tree """


def insertNodeInTree(node, key):
    # print("insert called with key", key)
    if not node:  # check if node is empty  if none then create new node
        rootNode = treeNode(key)
        return

    q = []
    q.append(node)

    # Do level order traversal until we find
    # an empty place.
    while len(q):
        # print("loop begin q size:", len(q))
        currentNode = q[0]
        q.pop(0)
        # print("popped q size:", len(q))
        if not currentNode.left:
            currentNode.left = treeNode(key)
            # print("create currentNode.left.key and break:", currentNode.left.key)
            break
        else:
            # print("append currentNode.left.key:", currentNode.left.key)
            q.append(currentNode.left)
            # print("Latest q size:", len(q))

        if not currentNode.right:
            currentNode.right = treeNode(key)
            # print("create currentNode.right.key and break:", currentNode.right.key)
            break
        else:
            # print("append currentNode.right.key:", currentNode.right.key)
            q.append(currentNode.right)
            # print("Latest q size:", len(q))


""" Inorder traversal of a binary tree"""
# 1. left
# 2. Root
# 3. Right
def inorderTraversal(node):
    if not node:
        return
    inorderTraversal(node.left)
    print(node.key, end=" ")
    inorderTraversal(node.right)


# Counting total Nodes present in Binary tree with left and right side including Root
def count_nodes(root):
    if root == None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Main code
if __name__ == "__main__":
    # creating an empty list
    # list1 = []
    # Taking elements as input and adding them into list.
    # list1 = list()  # Creation of empty list
    input_string = input("Enter elements of a list separated by space ")
    # print("\n")
    list1 = input_string.split()
    # convert each item to int type
    for i in range(len(list1)):
        # convert each item to int type
        list1[i] = int(list1[i])
    # print list
    print("User input as list : ", list1)

    # To remove duplicates in Given user list input
    res = []
    for i in list1:
        if i not in res:
            res.append(i)
    list1 = res  # List without duplicate elements which is ready for insersion
    # print list
    print("User input as list after removal of Duplicates: ", list1)

    # print("List after removing duplicate elements: ", list1)
    rootNode = treeNode(list1[0])
    list1.pop(0)
    for i in list1:
        insertNodeInTree(rootNode, i)
    print("Inorder traversal after insertion:", end=" ")
    inorderTraversal(rootNode)
    p = count_nodes(rootNode)
    print("\nThe Total Number of Nodes in Tree are : ---> ", p)
