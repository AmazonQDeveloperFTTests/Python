'''
A binary search Tree
'''


class Node:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):

        # Create a new Node

        node = Node(label)

        if self.empty():
            self.root = node
        else:
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:

                    dad_node = curr_node

                    if node.getLabel() < curr_node.getLabel():
                        curr_node = curr_node.getLeft()
                    else:
                        curr_node = curr_node.getRight()
                else:
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)
                    break

    def empty(self):
        if self.root is None:
            return True
        return False

    def preorderShow(self, curr_node):
        if curr_node is not None:
            print(curr_node.getLabel(), end=" ")
            self.preorderShow(curr_node.getLeft())
            self.preorderShow(curr_node.getRight())
    
    def postorderShow(self, curr_node):
        if curr_node is not None:
            self.postorderShow(curr_node.getLeft())
            self.postorderShow(curr_node.getRight())
            print(curr_node.getLabel(), end=" ")

    def inorderShow(self, curr_node):
        if curr_node is not None:
            self.inorderShow(curr_node.getLeft())
            print(curr_node.getLabel(), end=" ")
            self.inorderShow(curr_node.getRight())

    def getRoot(self):
        return self.root


'''
Example
            8
           / \
          3   10
         / \    \
        1   6    14
           / \   /
          4   7 13 
'''

if __name__ == '__main__':
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(1)
    t.insert(6)
    t.insert(4)
    t.insert(7)
    t.insert(10)
    t.insert(14)
    t.insert(13)

    t.preorderShow(t.getRoot())
    t.inorderShow(t.getRoot())
    t.postorderShow(t.getRoot())
