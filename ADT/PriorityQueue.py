class Node:
    def __init__(self, data=None, priority=None):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty() or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def print_queue(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        
Pqueue = PriorityQueue()
Pqueue.enqueue(1, 4)
Pqueue.enqueue(2, 1)
Pqueue.enqueue(3, 2)
Pqueue.enqueue(4, 3)
Pqueue.print_queue()