#https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline
# n = 6
# wines = [6,10,13,9,8,1]
n = int(input())
wines = []
for _ in range(n):
    wines.append(int(input()))

if n == 1:
    print(wines[0])
    quit()
if n == 2:
    print(sum(wines))
    quit()

dp = [None for _ in range(n)]
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
dp[2] = max(wines[0] + wines[2] , wines[1] + wines[2])

if n == 3:
    print(max(dp))
    quit()

curr = wines[3]
prev = wines[3-1]
dp[3] = max(dp[0] + prev + curr, dp[1] + curr)

if n == 4:
    print(max(dp))
    quit()
for i in range(4,n):
    curr = wines[i]
    prev = wines[i-1]
    dp[i] = max(dp[i-4] + prev + curr, dp[i-3] + prev + curr, dp[i-2] + curr)
# print(dp)
print(max(dp))