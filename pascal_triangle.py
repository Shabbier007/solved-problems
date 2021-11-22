
# print first nth rows of pascal traingle
# tells us value at nth row and cth column of pascal traingle
# if we want the value at nth row and cth column then the answer will be combinations ( n-1 C c-1)

n = 6
a = []
for i in range(1,n+1):
    res = []
    for j in range(i):
        res.append(j)
    a.append(res)
print(a)
for i in range(n):
    a[i][0] = 1   # the first element is 0
    a[i][-1] = 1  #the last element is 1
    for j in range(1,i):
        a[i][j] = a[i-1][j-1]+a[i-1][j]         # adding the previous row of the previous element and current element of previous row
print(a)