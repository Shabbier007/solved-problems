def search(self, nums: List[int], target: int) -> int:
    left = 0
    n = len(nums)
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        left_val = nums[left]
        mid_val = nums[mid]
        if left_val < nums[mid] and (left_val <= target < nums[mid]):
            right = mid - 1
        elif (left_val > mid_val) and (target < mid_val or target >= left_val):
            right = mid - 1
        else:
            left = mid + 1
    return -1