#https://www.acmicpc.net/problem/1158
from collections import deque

n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]
arr = deque(arr)
ans = []
while len(arr) != 0:
    arr.rotate(-k)
    ans.append(arr.pop())
print('<',end='')
print(*ans, sep = ', ', end = '')
print('>')
