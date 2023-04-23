class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        else:
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return data

    def remove_back(self):
        if self.is_empty():
            return None
        else:
            data = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return data

    # def peek_front(self):
    #     if self.is_empty():
    #         return None
    #     else:
    #         return self.head.data

    # def peek_back(self):
    #     if self.is_empty():
    #         return None
    #     else:
    #         return self.tail.data

    def print_deque(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

deque = Deque()
deque.add_front(1)
deque.add_front(2)
deque.add_back(1)
deque.add_back(2)
deque.print_deque()
print("After remove:")
deque.remove_front()
deque.remove_back()
deque.print_deque()
