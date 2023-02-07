

class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

# first = Node(1)
# second = Node(2)
# third = Node(3)
# first.next = second
# second.next = third

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        # if self.head is None :
        #     self.head = new_node
        # else :
        #     current = self.head
        #     while(current.next):
        #         current = current.next
        #     current.next = new_node
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = self.tail.next
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    def remove(self, idx):
        pass
    def insert(self, idx):
        pass

