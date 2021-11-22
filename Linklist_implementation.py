# implementation of linked list
class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class Linked:
    def __init__(self):
        self.head = None
    def insert_at_beg(self,data):
        Node = node(data,self.head)
        self.head = Node
    def insert_at_end(self,data):
        if self.head is None:
            Node = node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node(data,None)
    def length(self):
        count=0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    def insert_at_index(self,index,data):
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = node(data,itr.next)
                break
            count+=1
            itr = itr.next
    def remove_index(self,index):
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    def remove_element(self,elem):

        itr = self.head
        while itr:
            if elem==itr.data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print('empty list')
            return
        itr = self.head
        res = ''
        while itr:
            res = res+str(itr.data)+'--->'
            itr = itr.next
        print(res)
        return res
    def reverse(self):
        prev = None
        itr = self.head
        while itr:
            next = itr.next
            itr.next = prev
            prev = itr
            itr = next
        self.head = prev
li = Linked()
li.insert_at_beg(1)
li.insert_at_beg(2)
li.insert_at_beg(3)
li.insert_at_end(4)
li.insert_at_index(3,'shaik')
li.print()
li.remove_index(3)
li.print()
li.remove_element(3)
li.print()
print('length',li.length())