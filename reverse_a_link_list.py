class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class linked:
    def __init__(self):
        self.head = None
    def insert_at_beg(self,data):
        Node = node(data,None)
        self.head = Node
    def insert_at_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node(data, None)
    def insert_at_index(self, index, data):
        if index == 0:
            return self.insert_at_beg(data)
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                Node = node(data, itr.next)
                itr.next = Node
                break
            count += 1
    def remove_at_index(self, index):
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

