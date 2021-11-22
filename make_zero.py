a = [[1,2,3,4],[5,6,0,7],[8,9,4,6],[8,4,5,2]]
res = []
for i in range(len(a)):
    b = []
    for j in range(len(a[i])):
        b.append(a[i][j])
    res.append(b)
print(res)
for i in range(len(res)):
    for j in range(len(res[i])):
        total = 0
        if a[i][j] == 0:
            if i != 0:
                total += a[i-1][j]
                res[i-1][j] = 0
            if i != len(res)-1:
                total += a[i+1][j]
                res[i+1][j] = 0
            if j !=0 :
                total += a[i][j-1]
                res[i][j-1] = 0
            if j != len(a[i])-1:
                total += a[i][j+1]
                res[i][j+1] = 0
            res[i][j] = total
print(res)