a = [10,2,3,4,5,7,8]
n = len(a)
res= []

a.sort()
print(a)
for i in range(n):
    for j in range(i+1, n):
        k , m = j+1, n-1
        while k<m:
            sum_ = a[i] + a[j] + a[k] + a[m]
            if sum_ == 23:
                arr = {a[i], a[j], a[k], a[m]}
                arr = list(arr)
                arr.sort()
                res.append(arr)
                k += 1
                m -= 1
            if sum_ < 23:
                k += 1
            else:
                m -= 1
print(res)
