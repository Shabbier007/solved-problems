# first we need to merge the two list in a
# apply insertion sort algorithm
# make sure there is a base case involved in leetcode
# insert all element in the matrix
# apply sorting algorithm on matrix on
a = [4,0,0,0,0,0]
m = 1
b = [1,2,3,5,6]
j = 0
for i in range(len(a)):
    if a[i]==0 and i>=m:
        a[i] = b[j]
        j+=1
for i in range(len(a)):
    while a[i-1]>a[i] and i>0:
        a[i-1],a[i] = a[i] , a[i-1]
        i-=1
print(a)
