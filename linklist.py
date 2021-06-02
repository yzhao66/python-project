class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self,node=None):
        self.head = node
        if node:
            self.size = 1
        else:
            self.size = 0
    def is_empty(self):
        return self.size == 0
    def length(self):
        return  self.size
    def append(self,val):
        node = Node(val)
        current =self.head
        if current is None:
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node
        self.size += 1