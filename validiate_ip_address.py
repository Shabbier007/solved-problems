s = '222.111.111.111'
a = s.split('.')
print(a)
count = 0
for i in a:
        if len(i) ==0:
            print('False')
            break
        elif int(i)>=0 and int(i)<256:
            count += 1
print(count)
