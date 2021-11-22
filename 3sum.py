# using 3 loops
# using two loops and a hashmap
# sort the array use two pointer approach
# cannot remove duplicates using set so 10, 16, 18 use to ignore duplicates

def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i==0 or (i>0 and nums[i] != nums[i-1]):
            low = i + 1
            high = len(nums) - 1
            while low<high:
                if nums[low] + nums[high] == -nums[i]:
                    res.append([nums[i], nums[low], nums[high]])
                    while low<high and nums[low] == nums[low + 1]:
                        low += 1
                    while low<high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < nums[i]:
                    low += 1
                else:
                    high -= 1
    return res

# time complexity O(nxn)
# space complexity O(1)
