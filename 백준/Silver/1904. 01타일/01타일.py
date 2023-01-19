#https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline

n = int(input())
dp = [None for _ in range(n+1)]

dp[0:2] = [1,1]
for i in range(2,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[-1])