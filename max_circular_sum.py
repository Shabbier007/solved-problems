def kadens(arr,n):
    curr=0
    so_far=0
    for i in range(n):
        curr+=arr[i]
        if curr<0:
            curr=0
        if curr>so_far:
            so_far=curr
    return so_far
def max_circular(arr,n):
    if max(arr)<0:
        return max(arr)
    kade = kadens(arr,n)
    total = 0
    for i in range(n):
        total+=arr[i]
        arr[i]=-arr[i]
    total=total+kadens(arr,n)  ## sum of arr and sum of min conti sub array
    if total>kade:
        return total
    else:
        return kade
arr=[10,-3,-4,7,6,5,-4,-1]
n=len(arr)
res = max_circular(arr,n)
print(res)