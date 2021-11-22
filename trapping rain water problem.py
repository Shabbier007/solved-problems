# we need to take prefix sum and sufsum of the array and 19 th line
# time complexity is O(n) + O(n) + O(n)
# space complexity is O(n) + O(n)

a = [7,4,0,9]
pre= []
suf = [0 for i in range(len(a))]
pre_max, suf_max = a[0], a[len(a)-1]
for i in a:
    pre_max = max(pre_max, i)
    pre.append(pre_max)
print(pre)
for i in range(len(a)-1, -1, -1):
    suf_max = max(suf_max, a[i])
    suf[i] = suf_max
print(suf)
count = 0
for i in range(len(a)):
    count = count + (min(pre[i], suf[i]) - a[i])
print(count)


# optimal sol
# in the above approach we are calculating the min of left and right to avoid this we can do this in one loop

left_max, right_max = 0, 0              # storing the max left and right value
left, right, res = 0, 0, 0                     # two poiter technique
while left < right:
    if a[left] <= a[right]:
        if a[left] >= left_max:
            left_max = a[left]
        else:
            res = res + (left_max-a[left])          # here the we can surely say that min is left_max not right_max
        left += 1
    else:
        if a[right] >= right_max:
            right_max = a[right]
        else:
            res = res + (right_max - a[right])
        right -= 1
print(res)