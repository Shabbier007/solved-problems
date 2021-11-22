# merge sort is a recursive method
# it is a divide and conquer algorithm
# very efficient for large dataset
# time complexity O(nlogn)

arr = [5,3,2,1,4,6,3,4,9,7,1,2,3,5,9,0,5,6,8,9]

def mergesort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)                       # dividing step

    i , j , k = 0 , 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
mergesort(arr)
print(arr)
