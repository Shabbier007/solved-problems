# use sliding window approach
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 3
start = 0
zero_count = 0
max_count = 0
for i in range(len(nums)):
    if nums[i] == 0:
        zero_count += 1
    while zero_count>k:
        if nums[start] == 0:
            zero_count -= 1
        start += 1
    max_count = max(max_count, i-start+1)
print(max_count)
