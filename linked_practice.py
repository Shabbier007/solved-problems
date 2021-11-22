class node:
    def __init__(self,data=None,next=None):
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
        itr.next = node(data,None)
    def insert_at_index(self,index,data):
        if index == 0:
            self.insert_at_beg(data)
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = node(data,itr.next)
                break
            count+=1
            itr = itr.next
    def remove_element(self,index):
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count+=1
            itr = itr.next
    def print(self):
        if self.head is None:
            print('empty')
            return
        res = ''
        itr = self.head
        while itr:
            res += str(itr.data)+'--->'
            itr = itr.next
        print(res)
        return res
    def length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        print(count)
        return count
li = Link()
li.insert_at_beg(2)
li.insert_at_beg(3)
li.insert_at_beg(4)
li.insert_at_end(5)
li.insert_at_end(6)
li.insert_at_index(2,8)
li.remove_element(2)
li.length()
li.print()




