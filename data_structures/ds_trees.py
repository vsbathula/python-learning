"""
Tree
A tree is a hierarchical data structure that consists of nodes, where each node points to child nodes.
The most common tree is a binary tree, where each node has at most two children: left and right.

Key Operations:
Insert: Add a new node.
Delete: Remove a node.
Traverse: Visit all the nodes in a specific order (inorder, preorder, postorder).
Search: Find a node.
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)


# Usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)

tree.inorder_traversal(tree.root)  # Output: 2 3 4 5 8
