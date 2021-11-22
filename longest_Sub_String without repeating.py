que = ' '
d = {}
len_ = 0
i = 0
j = 0
max_len = 0

while j < len(que)-1 and i<len(que):
    if que[j] in d:
        del d[que[i]]
        i += 1
    if que[j] not in d:
        len_ = j-i + 1
        max_len = max(len_, max_len)
        d[que[j]] = 1
        j += 1

print(max_len)

