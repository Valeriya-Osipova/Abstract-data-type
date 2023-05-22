class BinomialHeap:
    
    # Вершина биномиального дерева
    class Node:
        def __init__(self, key):
            self.key = key
            self.parent = None
            self.sibling = None
            self.child = None
            self.degree = 0
    
    # Конструктор кучи
    def __init__(self):
        self.head = None
    
    # Методы создания биномиального дерева
    def create_tree(self, key):
        return BinomialHeap.Node(key)
    
    # Методы слияния биномиальных деревьев
    def merge_trees(self, tree1, tree2):
        if tree1.key > tree2.key:
            tree1, tree2 = tree2, tree1
        tree2.parent = tree1
        tree2.sibling = tree1.child
        tree1.child = tree2
        tree1.degree += 1
        return tree1
    
    def merge_lists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.key < list2.key:
            list1.sibling = self.merge_lists(list1.sibling, list2)
            return list1
        else:
            list2.sibling = self.merge_lists(list2.sibling, list1)
            return list2
    
    # Методы вставки и удаления элементов
    def insert(self, key):
        new_tree = self.create_tree(key)
        self.head = self.merge_lists(self.head, new_tree)
    
    def find_min(self):
        if not self.head:
            return None
        min_node = self.head
        curr_node = self.head.sibling
        while curr_node:
            if curr_node.key < min_node.key:
                min_node = curr_node
            curr_node = curr_node.sibling
        return min_node
    
    def extract_min(self):
        if not self.head:
            return None
        min_node = self.head
        prev_node = None
        curr_node = self.head.sibling
        while curr_node:
            if curr_node.key < min_node.key:
                min_node = curr_node
                prev_node = prev_node
            prev_node = curr_node
            curr_node = curr_node.sibling
        if prev_node:
            prev_node.sibling = min_node.sibling
        else:
            self.head = min_node.sibling
        new_list = None
        child = min_node.child
        while child:
            next_child = child.sibling
            child.parent = None
            child.sibling = new_list
            new_list = child
            child = next_child
        self.head = self.merge_lists(self.head, new_list)
        return min_node.key

heap = BinomialHeap()

heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)

print(heap.find_min().key) # 1
print(heap.extract_min()) # 1
print(heap.extract_min()) # 3
print(heap.extract_min()) # 5
print(heap.extract_min()) # 7