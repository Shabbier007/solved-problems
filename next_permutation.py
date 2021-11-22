# traverse from right to left
# get index a[i]<a[i+1]
# get index[2] > index[1]
# swap(a[index1] and a[index2])
# reverse

nums = [1,2,3]
N = len(nums)
pivot = 0

# find pivot
for i in range(N - 1, 0, -1):
    if nums[i - 1] < nums[i]:
        pivot = i
        break

if pivot == 0:
    nums.sort()

swap = N - 1
while nums[pivot - 1] >= nums[swap]:
    swap -= 1
nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
nums[pivot:] = sorted(nums[pivot:])