class node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
class Linked:
    def __init__(self):
        self.head = None
    def insert_at_begi(self,data):
        Node = node(data,self.head)
        self.head = Node
    def insert_at_end(self,data):
        if self.head is None:
            Node = node(data,None)
            self.head = Node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data,None)
