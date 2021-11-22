def productExceptSelf(self, nums, n):
    # code here
    res = []
    final = 1
    zero_count = 0
    for i in nums:
        if i == 0:
            zero_count += 1
        else:
            final *= i
    for i in nums:
        if zero_count == 0:
            res.append(final // i)
        elif i == 0 and zero_count == 1:
            res.append(final)
        elif i == 0 and zero_count > 1:
            res.append(0)
        elif i != 0 and zero_count >= 1:
            res.append(0)
    return res