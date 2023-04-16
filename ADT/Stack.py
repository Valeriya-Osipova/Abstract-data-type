#Реализация стека с помощью односвязного списка

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

    def is_empty(self):
        return self.top is None

stack = Stack()
stack.push(3)
stack.push(2)
stack.push(1)
a = stack.pop()         #взяли и затем удалили 1
print(a)
a = stack.pop()         #взяли и затем удалили 2
print(a)
b = stack.peek()        #взяли 3
print(b)
c = stack.is_empty()    #так как осталась 3 - false
print(c)
