# take a priority queue
# put all the element in the priority queue
# get element k times and return the result
def something(matrix):
    from queue import PriorityQueue
            a = PriorityQueue()
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    a.put(matrix[i][j])
            for i in range(k):
                res = a.get()
            return res