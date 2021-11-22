a = [1, 6, 5, 4, 7, 8, 4, 3, 2, 1]
super_star = a[0]
index = 0
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        super_star = a[i+1]
        index = i+1
print(super_star,index)
res = a[index:]
print(res)