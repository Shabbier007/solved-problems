d = {}
curr = l1
while curr is not None:
    d[curr] = 1
    curr = curr.next
curr1 =l2
while curr1 is not None:
    if curr1 in d:
        print(curr1)
        break
    curr1 = curr1.next