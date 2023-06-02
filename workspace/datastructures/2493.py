#https://www.acmicpc.net/problem/2493
import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int,input().split()))
stack = []
ans = []
#iter towers
for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            ans.append(stack[-1][0] + 1) #index+1 = i th tower
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    
    stack.append([i,towers[i]]) #index : height
print(*ans)