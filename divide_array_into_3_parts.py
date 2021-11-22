a = [33,4,5,45,2,7,8,9,3,34,6,8,23,56,5,342,68,8,4]
i=0
for j in range(len(a)):
    if j==0:
        continue
    if j%3==0:
        print(a[i:j],end='    ')
        i+=3
print(a[i:])