class Node:
    def __init__(self, value, tail):
        #added note directly
        self.value = value
        self.next = tail

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        #add new node and point next to the old head.
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
        #if the linkedList is empty raise an exeption.
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
