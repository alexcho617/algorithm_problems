#https://www.acmicpc.net/problem/11727
n = int(input())

dp = [None for _ in range(n+1)]


dp[0:2] = 1,1
# print(dp)
for i in range(2,n+1):
    dp[i] = dp[i-1] + 2*(dp[i-2])
print(dp[-1]%10007)
