# we need to transpose the matrix
# reverse each element of the matrix

a = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        a[i][j],a[j][i] = a[j][i],a[i][j]
print(a)
for i in a:
    i.reverse()
print(a)