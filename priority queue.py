# The queue follows FIFO (First in first out)
# The queue contains four important terms
# 1) Enqueue    : The process of inputting the data
# 2) Dequeue    : The process of removing the data from queue
# 3) Rear       : Get the last item from the queue
# 4) Front      : Get the first item from the queue
# the time complexity for all the operations are O(1)


# for visualization queue is a great data structure to remove the smallest element from the path

# The priority queue basically works on priority
# the element with the highest priority will come first
# The priority queue contians two priotities
# -------> lowest the element highest the priority
# -------> highest the element highest the priority
# we can set the priority based on the requirement


# we can implement priority queue:import collections

# 1) list O(n)
# 2) collections.deque O(1) for insertion and deletion
# 3) using queue module

## lists

a = []
a.append(5)
a.append(5)
a.append(5)
a.append(5)

a.pop(0)

## from collections.deque

from collections import deque

a = deque()         # initializing a queue

a.append(5)
a.append(4)         # time complexity for inserting and deleting is one
a.append(6)
print(a)
print(a.popleft())


## using queue module

from queue import Queue as Q

a = Q(maxsize=4)
print('The size before putting',a.qsize())
a.put(5)
a.put(4)
a.put(6)

print('The queue after putting',a.queue,a.qsize())