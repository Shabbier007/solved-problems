# the brute force approach count the total no of nodes and return the middle one O(n) + O(n/2)
# the optimal approach is O(n)
# we are doing this by using two tortoise method or two pointer method
# we will take two pointer one is updating at speed 1 and 2 resp.
# when the second reach the end return the current position of the 1 pointer

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

    def middle_of_ll_brute(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        ind = count//2
        count = 0
        current = self.head

        while current is not None:
            if ind <= count:
                print(current.data)

            count += 1
            current = current.next
    def middle_of_ll_optimal(self):
        slow = self.head
        fast = self.head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
li = Linked()
li.insert_at_beg(1)
li.insert_at_beg(2)
li.insert_at_beg(3)
li.insert_at_end(4)
li.insert_at_index(3,'shaik')
li.middle_of_ll_optimal()
li.print()
print(5//2)