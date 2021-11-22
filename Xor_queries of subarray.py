# first we need to find all the prefix sum of the which is from 0 to n in a dict
# after check the ranges if there are starting from 0 the go into the dict and append the value
# if starting from a certain point then
# find xor of last element range
# current xor of the element
# starting xor of the element ( here ranges are given in the queries)

arr = [1, 3, 4, 8]
queries = [[0,1],[1,2],[0,3],[3,3]]
d = {}
xor = 0
for i in range(len(arr)):
    xor = xor ^ arr[i]
    d[i] = xor              # putting all prefix sum xor in dict starting from 0

print(d)
res = []
for i in queries:
    if i[0] == i[1]:
        res.append(arr[i[0]])
    elif i[0] == 0:
        res.append(d[i[1]])
    else:                                   # if ranges are not starting from zero
        x = d[i[1]] ^ arr[d[0]] ^ d[i[0]]
        res.append(x)
print(res)