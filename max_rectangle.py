a = [[0, 1, 1, 0], [1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 0, 0]]
row = [1 for i in range(len(a))]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 0:
            row[i] = 0
print(row)
count = 0
max_count = 0
for i in row:
    if i == 1:
        count += 1
        max_count = max(count, max_count)
        print(max_count)
    else:
        count = 0
print(max_count)
print(max_count * 4)