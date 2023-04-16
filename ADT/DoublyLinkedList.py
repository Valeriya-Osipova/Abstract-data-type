class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

DLinked_list = DoublyLinkedList()
DLinked_list.append(2)
DLinked_list.append(3)
DLinked_list.prepend(1)
DLinked_list.print_list()
print("after delete:")
DLinked_list.delete(1)
DLinked_list.print_list()