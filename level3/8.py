import sys
n = sys.stdin.readline()
n = int(n)
star = 1
space = n-1
for i in range(1,n+1):
    for j in range(0,space):
        print(' ',end='')
    for j in range(0,star):
        print('*',end='')
    star += 1
    space -= 1
    print()

#Alternative
# x=int(input())
# for i in range(1,x+1):
#     print(' '*(x-i)+'*'*i)