# it contains the player scores and top players scores(ranked)


# approach firstly we need to remove the duplicates from the top scores
# check the player scores individually with the ranked

ranked = [100,90,90,80,75,60]
player = [50,65,77,90,102]

a = list(set(ranked))
a.sort(reverse=True)
l = len(a)
res=[]
for i in player:
    while l>0 and i>a[l-1]:
        l-=1
    res.append(l+1)
print(res)