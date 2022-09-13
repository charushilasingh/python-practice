# Solution in Python to:
# 1. Declare a Tree structure
# 2. Insert nodes into the tree and not make it BST
# 3. Print and count the inserted nodes

# Tree structure declaration
class treeNode:
    def __init__(node, data):
        node.key = data
        node.left = None
        node.right = None


"""Function to insert a node in binary tree """


def insertNodeInTree(node, key):
    print("insert called with key", key)
    if not node:
        rootNode = treeNode(key)
        return

    q = []
    q.append(node)

    # Do level order traversal until we find
    # an empty place.
    while len(q):
        print("loop begin q size:", len(q))
        currentNode = q[0]
        q.pop(0)
        print("popped q size:", len(q))
        if not currentNode.left:
            currentNode.left = treeNode(key)
            print("create currentNode.left.key and break:", currentNode.left.key)
            break
        else:
            print("append currentNode.left.key:", currentNode.left.key)
            q.append(currentNode.left)
            print("Latest q size:", len(q))

        if not currentNode.right:
            currentNode.right = treeNode(key)
            print("create currentNode.right.key and break:", currentNode.right.key)
            break
        else:
            print("append currentNode.right.key:", currentNode.right.key)
            q.append(currentNode.right)
            print("Latest q size:", len(q))


""" Inorder traversal of a binary tree"""


def inorderTraversal(node):
    if not node:
        return
    inorderTraversal(node.left)
    print(node.key, end=" ")
    inorderTraversal(node.right)


def count_nodes(root):
    if root == None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Driver code
if __name__ == "__main__":
    rootNode = treeNode(3)
    # rootNode.left = treeNode(11)
    # rootNode.left.left = treeNode(7)
    # rootNode.right = treeNode(9)
    # rootNode.right.left = treeNode(15)
    # rootNode.right.right = treeNode(8)

    print("Inorder traversal before insertion:", end=" ")
    inorderTraversal(rootNode)

    # key = 12
    insertNodeInTree(rootNode, 5)
    insertNodeInTree(rootNode, 2)
    insertNodeInTree(rootNode, 1)
    # insertNodeInTree(rootNode, 15)
    # insertNodeInTree(rootNode, 8)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorderTraversal(rootNode)

p = count_nodes(rootNode)
# print()
print("\nThe Total Number of Nodes in Tree are : ---> ", p)
