a = [1,9,3,10,4,20,2]
d = {}
for i in a:
    if i not in d:
        d[i] = 0
    d[i] += 1
max_count = 0
count = 0
for i in range(len(a)):
    if i-1 not in d:
        current_elem = a[i]
        count = 0
        while current_elem in d:
            count += 1
            current_elem += 1
    max_count = max(max_count, count)
print(max_count)