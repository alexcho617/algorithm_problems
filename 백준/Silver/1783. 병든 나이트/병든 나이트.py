#https://www.acmicpc.net/problem/1783
n,m = map(int,input().split())
ans = 0
if n == 1:
    ans = 1
elif n == 2 and m in [1,2,3,4,5,6]:
    ans = (m + 1) // 2
elif n == 2 and m > 6:
    ans = 4
elif n > 2 and m > 6:
    ans = m - 2
elif n > 2 and m in [1,2,3,4,5,6]:
    ans = min(4,m)

print(ans)