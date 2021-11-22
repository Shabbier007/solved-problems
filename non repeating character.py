a = 'hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs'
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
res = ''
for i in a:
    if d[i] == 1:
        res = i
        break
    else:
        res = '$'
print(res)