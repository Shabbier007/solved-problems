arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
arr.sort()
dep.sort()
print(arr)
print(dep)
i,j = 1,0
plat, max_ = 1,1
while i<len(arr) and j<len(dep):
    if arr[i] > dep[j]:
        j += 1
        plat -= 1
    elif arr[i] <= arr[j]:
        j += 1
        plat += 1
    if plat > max_:
        max_ = plat
print(max_)

