#https://www.acmicpc.net/problem/17212
import sys
n = int(input())
dp = [ None for _ in range(n+1)]
dp[0:8] = 0,1,1,2,2,1,2,1

for i in range(8,n+1):
    #4case
    a = dp[i-1] + dp[1]
    b = dp[i-2] + dp[2]
    c = dp[i-5] + dp[5]
    d = dp[i-7] + dp[7]
    dp[i] = min(a,b,c,d)
print(dp[n])