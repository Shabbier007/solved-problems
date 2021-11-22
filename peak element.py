def peakElement(self, arr, n):
    # Code here
    max = 0
    pos = -1
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            pos = i
    return pos