# sort the two arrays
# start multiplying from end
def MaxSum(self, A, B, N):
    # code here
    A.sort()
    B.sort()
    res = 0
    for i in range(len(A) - 1, -1, -1):
        res += A[i] * B[i]
    return res