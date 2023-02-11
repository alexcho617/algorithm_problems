#https://www.acmicpc.net/problem/11052

n = int(input())
price = [0] + list(map(int,input().split()))

dp = [0 for _ in range(n+1)]

for i in range(n+1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[i-j] + price[j])
print(dp[n])

# price = list(map(int,input().split()))

# dp = price

# for i in range(n):
#     for j in range(1,i):
#         dp[i] = max(dp[i], dp[i-j-1] + price[j])
# print(dp)
