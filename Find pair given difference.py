a = [5, 20, 3, 2, 5, 80]
x = 78
d = {}
for i in a:
    if i not in d:
        d[i] = 1
print(d)
for i in a:
    y = i+x
    if y in d.keys():
        print('True')
        break