class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def lookup(self, key):
        return self._lookup(key, self.root)

    def _lookup(self, key, node):
        if node is None:
            return False
        elif node.val == key:
            return True
        elif key < node.val:
            return self._lookup(key, node.left)
        else:
            return self._lookup(key, node.right)
    
    def search(self, key, node):
        if node is None:
            return None
        elif node.val == key:
            return node
        elif key < node.val:
            return self.search(key, node.left)
        else:
            return self.search(key, node.right)

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return node
        elif key < node.val:
            node.left = self._delete(key, node.left)
        elif key > node.val:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min(node.right)
                node.val = temp.val
                node.right = self._delete(temp.val, node.right)
        return node

    def min(self):
        return self._min(self.root)

    def _min(self, node):
        if node.left is None:
            return node
        else:
            return self._min(node.left)

    def max(self):
        return self._max(self.root)

    def _max(self, node):
        if node.right is None:
            return node
        else:
            return self._max(node.right)

    def predecessor(self, key):
        node = self.search(key, self.root)
        if node is None:
            return None
        elif node.left is not None:
            return self._max(node.left)
        else:
            parent = self._find_parent(key, self.root)
            while parent is not None and node == parent.left:
                node = parent
                parent = self._find_parent(parent.val, self.root)
            return parent

    def successor(self, key):
        node = self.search(key, self.root)
        if node is None:
            return None
        elif node.right is not None:
            return self._min(node.right)
        else:
            parent = self._find_parent(key, self.root)
            while parent is not None and node == parent.right:
                node = parent
                parent = self._find_parent(parent.val, self.root)
            return parent

    def delete_tree(self):
        self.root = None

    def _find_parent(self, key, node):
        if node is None or node.val == key:
            return None
        elif (node.left is not None and node.left.val == key) or (node.right is not None and node.right.val == key):
            return node
        elif key < node.val:
            return self._find_parent(key, node.left)
        else:
            return self._find_parent(key, node.right)
            
tree = BinarySearchTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.insert(2)
tree.insert(8)
tree.insert(6)
tree.insert(12)

print(tree.lookup(7))
print(tree.lookup(4))

print(tree.min().val) 
print(tree.max().val)

print(tree.predecessor(7).val) 
print(tree.successor(7).val) 

tree.delete_tree()
print(tree.lookup(7))