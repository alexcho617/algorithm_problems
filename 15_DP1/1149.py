# https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

n = int(input())
ans = 0
dp = [[[],[],[]] for _ in range(n)]
dp[0] = list(map(int, input().split()))

for i in range(1,n):
    r, g, b = map(int, input().split())
    dp[i][0] = min(r + dp[i-1][1],r + dp[i-1][2])
    dp[i][1] = min(g + dp[i-1][0],g + dp[i-1][2])
    dp[i][2] = min(b + dp[i-1][0],b + dp[i-1][1])
print(min(dp[-1]))

    
