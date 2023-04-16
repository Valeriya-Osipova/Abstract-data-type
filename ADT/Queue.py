#Очередь с использованием односвязного списка

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
a = queue.dequeue()
print(a)
a = queue.dequeue()
print(a)