# read the functioning of split function

s = 'ababaa'
x = 'abaa'
new_lin = s.split(x)
count = 0
print(new_lin)
if len(new_lin) == 1:
    print(-1)
else:
    print(len(new_lin[0]))