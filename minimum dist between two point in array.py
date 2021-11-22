def minDist(self, arr, n, x, y):
    first = -1
    second = -1
    dis = 9999999
    for i in range(n):
        if arr[i] == x:
            first = i
        elif arr[i] == y:
            second = i
        if first != -1 and second != -1:
            dis = min(dis, abs(first - second))
    if first == -1 or second == -1:
        return -1
    else:
        return dis