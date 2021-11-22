## find length then length -n

# use two pointer one is starting from n and other from head if first ptr is none return second pointer.data
def getNthFromLast(head, n):
    # code here
    if head is None:
        return None
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    target = count - n
    if target < 0:
        return -1
    if target == 0:
        return head.data
    curr1 = head
    index = 0
    while curr1:

        if index == target:
            return curr1.data
        curr1 = curr1.next
        index += 1