#https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dp = [None for _ in range(n+1)]


    dp[0:5] = [1,1,1,2,2]

    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[n-1])