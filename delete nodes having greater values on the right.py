#  reverse the linked list
# check the values on the right use nested loop to check the last vlaue on the right
# return the reversed linked list

def prob(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    curr = head
    prev = None
    while curr:
        next = curr.next
        while next and next.data<curr.data:
            next = next.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
