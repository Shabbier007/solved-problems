# just make the logic works great (derrick sherrill) video
# the time complexity of average case is O(n2) and linear space complexity

a = [5,7,8,2,4,6,3]
n = len(a)
for i in range(n):
    while a[i-1]>a[i] and i>0:              # here we are checking with the previous element
        a[i-1],a[i] = a[i],a[i-1]           # if the previous element is greater than swap the elements
        i-=1
print(a)
