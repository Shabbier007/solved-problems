a = [3,1,3,4,2]
d = {}
for i in a:
    if i not in d:
        d[i] = 0
    d[i]+=1
print(d)
for i in d.keys():
    if d[i]>1:
        print(i)
