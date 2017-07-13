class Node:
    def __init__(self, value, tail):
        self.value = value
        self.next = tail

class LinkedList:
    def __init__(self, *start):
        self.head = None
        for _ in start:
            self.prepend(_)


    def prepend(self, value):
        self.head = Node(value, self.head)


    def remove(self, value):
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            last = n
            n = n.next
        return Flase

    def pop(self):
        if self.head is None:
            raise Exception ("Empty List.")
        val = self.head.value
        self.head = self.head.next
        return val

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next
            
