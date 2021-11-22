# apply kadens algorithm

def rowWithMax1s(self, arr, n, m):
    # code here
    count = 0
    max_count = 0
    row = -1
    for i in range(n):
        count = 0
        for j in range(m):
            if arr[i][j] == 1:
                count += 1
        if count > max_count:
            max_count = count
            row = i

    return row