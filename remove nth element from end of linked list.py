slow , fast = head, head
for i in range(n):
    fast = fast.next
if not fast:
    return head.next
while fast.next is not None:
    fast = fast.next
    slow = slow.next
slow.next = slow.next.next
return head
