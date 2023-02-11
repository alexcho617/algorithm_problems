#https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline
n,k = map(int,input().split())

#init
weights = [0] + [0 for _ in range(n)]
values = [0] + [0 for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)] #n*k table, not using index 0

#inputs
for i in range(1,n+1):
    w,v = map(int,input().split())
    weights[i] = w
    values[i] = v

#solve
for i in range(1,n+1):
    for j in range(1,k+1):
        if j < weights[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i]] + values[i])
    # print(dp[i])
    # print("i:",i)
    # print(*dp, sep='\n')


# print(dp)
print(dp[n][k])
