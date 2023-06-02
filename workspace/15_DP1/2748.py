#https://www.acmicpc.net/problem/2748
n = int(input())

dp = [None for _ in range(n+1)]
dp[0:3] = 0,1,1

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

