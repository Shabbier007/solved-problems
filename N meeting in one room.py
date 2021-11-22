# this a greedy approach algorithm
# it is generally based on a fact that the smallest finishing time has a chance to enter teh room
# here we are adding both starting and finishing time in one list
# and we are sorting the finishing time accordingly wrt starting time

# time complexity is O(nlogn) + O(n) + O(n)
# O(n)
def maximumMeetings(self,n,start,end):
    meet = []
    for i,j in zip(start, end):
        meet.append([i,j])
    meet = sorted(meet, key = lambda x:x[1])        # here we are sorting the list according to the finishing time
    count = 1
    last = 0
    for i in range(1, len(meet)):
        if meet[last][1] < meet[i][0]:          # here the the finishing time of last meeting should be less than the current start of meeting
            count +=1
            last = i
    return count