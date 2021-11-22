## brute force approach

## take a dict and stores all the node
## check whether the node exists in the hashmap or not

def detectLoop(self, head):
    # code here
    d = {}
    curr = head
    if curr is None or curr.next is None:
        return False
    while curr is not None:
        if curr in d:
            return True
        else:
            d[curr] = 1
        curr = curr.next
    return False