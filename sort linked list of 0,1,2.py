# take three variable count no of zero,one,two
# create a new linked list with no of zero, one two
def segregate(self, head):
    # code here
    if head is None:
        return None
    zero, one, two = 0, 0, 0
    curr = head
    while curr:
        if curr.data == 0:
            zero += 1
        if curr.data == 1:
            one += 1
        if curr.data == 2:
            two += 1
        curr = curr.next
    temp = Node(0)
    curr = temp
    for i in range(zero):
        node = Node(0)
        curr.next = node
        curr = node
    for i in range(one):
        node = Node(1)
        curr.next = node
        curr = node
    for i in range(two):
        node = Node(2)
        curr.next = node
        curr = node
    return temp.next