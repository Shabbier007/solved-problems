# bubble sort contains many swaping operations to overcome this we use selection sort

                        ## SELECTION SORT
# the time complexity of selection sort is O(n2)
# here we will find min value of array until we get a sorted array

a = [5,3,8,6,7,2]
for i in range(len(a)):
    min_ = i
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            min_ = j
    a[i],a[min_] = a[min_],a[i]
print(a)

## we can done this by using max_
## to get sort the array using max we need to iterate from the ending

a = [5,3,8,6,7,2,0]
for i in range(len(a)-1,-1,-1):
    max_ = i
    for j in range(i,-1,-1):
        if a[max_]<a[j]:
            max_ = j

    a[i],a[max_] = a[max_] , a[i]
print(a)