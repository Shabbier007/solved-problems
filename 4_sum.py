# use two nested loops and use two pointer to get of element

nums = [1,2,3,4]
Set = set()
nums.sort()
for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left = j+1
                right = len(nums)-1
                while left<right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ == target:
                        Set.add((nums[i],nums[j],nums[left],nums[right]))
                        right -= 1
                        left += 1
                    elif sum_ > target:
                        right -= 1
                    elif sum_ < target:
                        left += 1
print([list(i) for i in Set])