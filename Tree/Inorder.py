# roles 
# 1 all values of left subtree < root
# 2 all values of right subtree => root

# methods

# inorder --- left subtree then root then right subtree   

# preorder --- root - leftsubtree then right subtree


# postorder --- left subtree then right subtree then root


# BFS Implentation


#Binary search tree using linked list



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

    # Inorder: Left, Root, Right
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # Preorder: Root, Left, Right
    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # Postorder: Left, Right, Root
    def postorder(self, rt):
        if rt is None:
            return

        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")


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

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

  
                
                