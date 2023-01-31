#https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))

dp = [None for _ in range(n)]
dp[0] = nums [0]

for i in range(1,n):
    dp[i] = dp[i-1] + nums[i]
    if dp[i] <= 0:
        dp[i] = nums[i]
print(max(dp)) 