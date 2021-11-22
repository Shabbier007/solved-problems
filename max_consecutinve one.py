nums = [1,1,0,1,1,1]
rt = 0
s = 0
for x in nums:
    if x:
        s+=1
        continue
    rt = max(rt, s)
    s = 0
print(max(rt, s))