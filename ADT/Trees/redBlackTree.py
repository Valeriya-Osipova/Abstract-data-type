class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1  # 1 - красный, 0 - черный


class RedBlackTree:
    def __init__(self):
        self.null_node = Node(None)
        self.root = self.null_node
        self.null_node.parent = self.null_node

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.null_node
        new_node.right = self.null_node

        current_node = self.root
        parent_node = None

        while current_node != self.null_node:
            parent_node = current_node
   
            if new_node.key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = parent_node

        if parent_node == None:
            self.root = new_node
            new_node.color = 0
            return

        if parent_node.key < new_node.key:
            parent_node.right = new_node
        else:
            parent_node.left = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node.parent.color == 1:
            if new_node.parent == new_node.parent.parent.right:
                temp_node = new_node.parent.parent.left

                if temp_node.color == 1:
                    temp_node.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)

                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self.left_rotate(new_node.parent.parent)
            else:
                temp_node = new_node.parent.parent.right

                if temp_node.color == 1:
                    temp_node.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)

                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self.right_rotate(new_node.parent.parent)

            if new_node == self.root:
                break

        self.root.color = 0

    def left_rotate(self, node):
        temp_node = node.right
        node.right = temp_node.left

        if temp_node.left != self.null_node:
            temp_node.left.parent = node

        temp_node.parent = node.parent

        if node.parent == None:
            self.root = temp_node
        elif node == node.parent.left:
            node.parent.left = temp_node
        else:
            node.parent.right = temp_node

        temp_node.left = node
        node.parent = temp_node

    def right_rotate(self, node):
        temp_node = node.left
        node.left = temp_node.right

        if temp_node.right != self.null_node:
            temp_node.right.parent = node

        temp_node.parent = node.parent

        if node.parent == None:
            self.root = temp_node
        elif node == node.parent.right:
            node.parent.right = temp_node
        else:
            node.parent.left = temp_node

        temp_node.right = node
        node.parent = temp_node

    def lookup(self, key):
        current_node = self.root
        while current_node != self.null_node:
            if key == current_node.key:
                return current_node
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None
    def min(self, node=None):
        if node is None:
            node = self.root

        while node.left != self.null_node:
            node = node.left

        return node

    def max(self, node=None):
        if node is None:
            node = self.root

        while node.right != self.null_node:
            node = node.right

        return node

    def predecessor(self, key):
        node = self.lookup(key)

        if node is None:
            return None

        if node.left != self.null_node:
            return self.max(node.left)

        parent_node = node.parent

        while parent_node != self.null_node and node == parent_node.left:
            node = parent_node
            parent_node = parent_node.parent

        return parent_node

    def successor(self, key):
        node = self.lookup(key)

        if node is None:
            return None

        if node.right != self.null_node:
            return self.min(node.right)

        parent_node = node.parent

        while parent_node != self.null_node and node == parent_node.right:
            node = parent_node
            parent_node = parent_node.parent

        return parent_node

    def delete_tree(self):
        self.root = self.null_node

    def transplant(self, node1, node2):
        if node1.parent == self.null_node:
            self.root = node2
        elif node1 == node1.parent.left:
            node1.parent.left = node2
        else:
            node1.parent.right = node2

        node2.parent = node1.parent

    def delete_node(self, node):
        y = node
        y_original_color = y.color

        if node.left == self.null_node:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.null_node:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.min(node.right)
            y_original_color = y.color
            x = y.right

            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == 0:
            self.fix_delete(x)

    def fix_delete(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                temp_node = node.parent.right

                if temp_node.color == 1:
                    temp_node.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    temp_node = node.parent.right

                if temp_node.left.color == 0 and temp_node.right.color == 0:
                    temp_node.color = 1
                    node = node.parent
                else:
                    if temp_node.right.color == 0:
                        temp_node.left.color = 0
                        temp_node.color = 1
                        self.right_rotate(temp_node)
                        temp_node = node.parent.right

                    temp_node.color = node.parent.color
                    node.parent.color = 0
                    temp_node.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                temp_node = node.parent.left

                if temp_node.color == 1:
                    temp_node.color = 0
                    node.parent.color = 1
                    self.right_rotate(node.parent)
                    temp_node = node.parent.left

                if temp_node.left.color == 0 and temp_node.right.color == 0:
                    temp_node.color = 1
                    node = node.parent
                else:
                    if temp_node.left.color == 0:
                        temp_node.right.color = 0
                        temp_node.color = 1
                        self.left_rotate(temp_node)
                        temp_node = node.parent.left

                    temp_node.color = node.parent.color
                    node.parent.color = 0
                    temp_node.left.color = 0
                    self.right_rotate(node.parent)
                    node = self.root

        node.color = 0

    def delete(self, key):
        node = self.lookup(key)

        if node is None:
            return

        self.delete_node(node)
    
tree = RedBlackTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.insert(2)
tree.insert(8)
tree.insert(6)
tree.insert(12)

print(tree.lookup(7).key)

print(tree.min().key) 
print(tree.max().key)

print(tree.predecessor(7).key) 
print(tree.successor(7).key) 

tree.delete_tree()
print(tree.lookup(7))