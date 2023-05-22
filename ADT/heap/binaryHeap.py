class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while (i > 0) and (self.heap[i] < self.heap[self.parent(i)]):
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) > 1:
            min_item = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return min_item
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            return None

    def heapify_down(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        self.heapify_up(i)

    def merge(self, other_heap):
        self.heap += other_heap.heap
        self.build_heap()

    def build_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify_down(i)

# создание бинарной кучи
heap = BinaryHeap()

# добавление элементов
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)

# поиск и удаление узла с минимальным приоритетом
print(heap.extract_min())  # 1

# понижение приоритета заданного элемента
heap.decrease_key(1, 2)

# слияние двух очередей в одну
other_heap = BinaryHeap()
other_heap.insert(4)
other_heap.insert(6)
heap.merge(other_heap)

# поиск и удаление узла с максимальным приоритетом
print(heap.extract_min())  # 2