# we need to see whether the intervals are sorted or not
# otherwise we need to sort the intervals
#

a = [[1,4],[0,2],[3,5]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        for i in intervals:
            if result and (i[0]>=result[-1][0] and i[0]<=result[-1][1]):
                result[-1][1]=max(result[-1][1],i[1])
            else:
                result.append(i)
        return result
