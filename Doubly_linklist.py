class node:
    def __init__(self,data=None,next=None,prev=None):
        self.prev = prev
        self.data = data
        self.next = next
class Link:
    def __init__(self):
        self.head = None
    def insert_at_beg(self,data):
        Node = node(data,self.head)
        self.head = Node
    def insert_at_end(self,data):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node(data,None,itr)
        print(itr.prev)
    def print(self):
        itr = self.head
        res = ''
        while itr:
            res+=str(itr.data)+'-->'
            itr = itr.next
        print(res)

li = Link()
li.insert_at_beg(10)
li.insert_at_beg(11)
li.insert_at_beg(12)
li.insert_at_end(13)
li.insert_at_end(14)
li.print()