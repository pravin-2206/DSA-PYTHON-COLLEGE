class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # Find Minimum
    def find_min(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.left is not None:
            temp = temp.left

        print("Minimum value:", temp.data)

    # Find Maximum
    def find_max(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.right is not None:
            temp = temp.right

        print("Maximum value:", temp.data)


b1 = BST()

b1.insert(Node(100))
b1.insert(Node(110))
b1.insert(Node(120))
b1.insert(Node(130))
b1.insert(Node(13))
b1.insert(Node(1))
b1.insert(Node(3))

print("Inorder:")
b1.inorder(b1.root)

print("\nMinimum and Maximum:")
b1.find_min()
b1.find_max()

