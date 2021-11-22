## get the max difference between two elements (brute force approach)  (O(n2))

a = [7,1,5,3,6,4]
min_ = 10000
pro = 0
max_pro = 0
for i in range(len(a)):
    min_ = min(min_,a[i])
    pro = a[i]-min_
    if pro>max_pro:
        max_pro = pro
print(max_pro)