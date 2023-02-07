

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value=2)
bt.root.right = Node(value=3)

bt.root.left.left = Node(value=4)
bt.root.left.right = Node(value=5)
bt.root.right.right = Node(value = 6)

while bt.root is not None:
    print("root value : {0}".format(bt.root.value))
    bt.root = bt.root.left

