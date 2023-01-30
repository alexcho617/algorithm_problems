#https://www.acmicpc.net/problem/17175
n = int(input())

#number of fib calls
dp = [None for _ in range(n+1)]
dp[:2] = 1,1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2] + 1
print(dp[n]%1000000007)