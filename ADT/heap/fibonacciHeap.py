class FibonacciHeap:
    class Node:
        def __init__(self, k):
            self.k = k
            self.degree = 0
            self.mark = False
            self.parent = None
            self.child = None
            self.left = self.right = self

    def __init__(self):
        self.min = None
        self.n = 0

    def is_empty(self):
        return self.min == None

    def insert(self, x):
        node = self.Node(x)
        self.min = self._merge_lists(self.min, node)
        self.n += 1

    def find_min(self):
        if self.is_empty():
            raise Exception('Heap is empty.')
        return self.min.k

    def remove_min(self):
        z = self.min
        if z is not None:
            for child in z.child:
                child.parent = None
            self.min = self._remove_node_from_list(z)
            self.min = self._merge_lists(self.min, z.child)
            if self.min is not None:
                self._consolidate()
            self.n -= 1
        return z.k

    def _remove_node_from_list(self, node):
        if node.right == node:
            return None
        left = node.left
        right = node.right
        left.right = right
        right.left = left
        return left

    def _merge_lists(self, a, b):
        if a is None and b is None:
            return None
        if a is None:
            return b
        if b is None:
            return a
        a.right.left = b.left
        b.left.right = a.right
        a.right = b
        b.left = a
        return a if a.k < b.k else b

    def _consolidate(self):
        A = [None] * self.n
        nodes = [w for w in self._iterate_nodes(self.min)]
        for w in nodes:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.k > y.k:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min = None
        for i in range(self.n):
            if A[i] is not None:
                self.min = self._merge_lists(self.min, A[i])

    def _link(self, y, x):
        y.parent = x
        y.mark = False
        x.child = self._merge_lists(x.child, y)
        x.degree += 1

    def _iterate_nodes(self, node):
        head = node
        while True:
            yield head
            if head.child is not None:
                for child in self._iterate_nodes(head.child):
                    yield child
            head = head.right
            if head == node:
                break

h = FibonacciHeap()

h.insert(5)
h.insert(3)
h.insert(7)
h.insert(1)

print(h.find_min())  # 1

print(h.remove_min())  # 1
print(h.find_min())  # 3

h.insert(6)
h.insert(2)

print(h.remove_min())  # 2
print(h.remove_min())  # 3
print(h.remove_min())  # 5
print(h.remove_min())  # 6
print(h.remove_min())  # 7
