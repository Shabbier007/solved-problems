## the time complexity of bubble sort algorithm is O(n2) in average case and O(n) in best case


## this algorithm generaly works on swaping
## in each iteration we will get a maximum element in the end

a = [5,2,3,6,7,1,2,5]

for i in range(len(a)-1,-1,-1):
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)