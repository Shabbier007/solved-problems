## here we will take an dict and stores the repeated element
## if we got any element in the given linked list then we will ignore that element

def abc(head):
    if head is None:
        return None
    d = {}
    curr = head
    d[curr.data] = True
    while curr.next is None:
        data = curr.next.data
        if data not in d:
            d[data] = True
            curr = curr.next
        else:
            curr.next = curr.next.next
    return head
