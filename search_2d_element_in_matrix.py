# this problem contains two types of variation in gfg and leetcode
# in gfg we need to start our pointed at 1st row last column
# if element is greater move the pointer towards down
# if it is less move the pointer left

a = [[3,30,38],[36,43,60],[40,51,69]]
n , m ,x= 3,3,62
ptr1 = 0
ptr2 = m-1
while True:
    if x<a[ptr1][ptr2]:
        ptr2-=1
        if ptr2<0:
            print('nooooo')
            break
    elif x>a[ptr1][ptr2]:
        ptr1+=1
        if ptr1>n-1:
            print('No')
            break
    elif x==a[ptr1][ptr2]:
        print(ptr1,ptr2,'yes')
        break

## leetcode sol
## This approach is usefull for both
## you need to check the last element of each row if it is less than or equal to x than traverse the only row
## time complexity is O(n+m) and O(1)

last = m-1
for i in range(n):
    	    if x<=matrix[i][last]:
    	        if x in matrix[i]:
    	            return 1
    	return 0