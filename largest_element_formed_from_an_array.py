a=[3, 30, 34, 5, 9]
for i in range(len(a)-1):
    j=i+1
    while j<len(a):
        x=str(a[i])+str(a[j])
        y=str(a[j])+str(a[i])
        if int(x)>int(y):
            j+=1
        else:
            a[i],a[j]=a[j],a[i]
            j+=1
total = ''
for i in a:
    total+=str(i)
print(total)
9534330