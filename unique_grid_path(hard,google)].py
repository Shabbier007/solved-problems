# here we need to find how many ways we can move from start to the end
# for finding we can move in only two direction either down or right
# here we are using recursion to check the ways



# this is a brute force sol we are checking each and every possibility to reach end
# the time complexity is exponential
m , n = 3,4
fin_m , fin_n = m-1 , n-1
i,j = 0,0
def sol(i,j,fin_m,fin_n):
    if i==fin_m and j == fin_n:
        return 1
    elif i > fin_m or j > fin_n:
        return 0
    return sol(i+1,j,fin_m,fin_n) + sol(i,j+1,fin_m,fin_n)
print(sol(i,j,fin_m,fin_n))



# dynamic programming solution
# dynamic programming means repeating the past without actually computing it

a=[]
for i in range(m):
    l = []
    for j in range(n):
        l.append(-1)
    a.append(l)
print(a)
def sol1(i,j,fin_m,fin_n,a):
    print(a)

    if i == fin_m and j == fin_n:
        return 1
    if i >= fin_m or j>=fin_n:
        return 0


    if a[i][j] != -1:
        return a[i][j]
    a[i][j] =  sol1(i+1,j,fin_m,fin_n,a) + sol1(i,j+1,fin_m,fin_n,a)

sol1(i,j,fin_m,fin_n,a)


# if we there are a total of m-1+n-1 path in which we have to choose n-1 or m-1 paths
# m+n-2 C n-1

upper = m+n-2
lower = m-1
num , deno = 1 , 1
for i in range(m-1):
    num = num*upper
    deno = deno*lower
    print(deno)
    upper -= 1
    lower -= 1
print(num,deno)
print('combinations answer' , num//deno)
