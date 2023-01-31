#https://www.acmicpc.net/problem/9657
n = int(input())

dp = [0] * 1001
dp[1],dp[3],dp[4] = 1,1,1

for i in range(5,n+1):
    if 0 in [dp[i-1],dp[i-3],dp[i-4]]:
        dp[i] = 1
    else:
        dp[i] = 0
if dp[n]: #meaning if dp[n] == 1
    print("SK")
else:
    print("CY")