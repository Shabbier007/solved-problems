# in this approach we are taking a dict and storing the sum and upto index
# if anywhere in the array we are getting the sum which is present in the hasharray we are subtracting and update the max_len

a = [15,-2,2,-8,1,7,10,23]
d = {}
sum_ = 0
max_len = 0
for i in range(len(a)):
    sum_ += a[i]
    if sum_==0:
        len_ = i+1
        max_len = max(max_len,len_)
    elif sum_ not in d:                 # if current sum is not in dict add the sum with index as its value
        d[sum_] = i
    elif sum_ in d:                     # if sum in hashmap then subract the current index with hashmaps index
        ind = d[sum_]
        len_ = i-ind
        max_len = max(max_len,len_)
print(max_len)

## find how many subarray with sum equal to k
a = [1,2,3]
k = 3
sum_ = 0
result = 0
d = {0:1}                   # we are storing how many times our sum is coming
for i in range(len(a)):
    sum_ += a[i]
    if sum_-k in d.keys():      # checking the sums
        result += d[sum_-k]

    if sum_ in d.keys():        # updating the count of sums
        d[sum_] += 1
    else:
        d[sum_] = 1             # inserting the sums
print(result)
print(d)