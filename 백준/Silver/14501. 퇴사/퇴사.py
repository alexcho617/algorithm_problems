# https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline
n = int(input())
counsels =[]
for _ in range(n):
    counsels.append(list(map(int,input().split())))
counsels.append([0,0])

dp = [0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    if counsels[i][0] + i <= n:
        dp[i] = max(dp[i+1], dp[i + counsels[i][0]] + counsels[i][1])
    else:
        dp[i] = dp[i+1]
print(max(dp))