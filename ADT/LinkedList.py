# Объявляем класс узла

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def delete(self, data):
        if self.head.data == data:
             self.head = self.head.next
             return
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.print_list()

linked_list.delete(2)
print("after delete:")
linked_list.print_list()