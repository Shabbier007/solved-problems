# in this we need to find all the elements which are greater than the len(a)/3

a = [1,2,3]
d = {}
res = []
count = len(a)//3 + 1
for i in a:
    if i not in d:
        d[i] = 0
    d[i] += 1
for i in d.keys():
    if d[i]>=count:
        res.append(i)
print(res)