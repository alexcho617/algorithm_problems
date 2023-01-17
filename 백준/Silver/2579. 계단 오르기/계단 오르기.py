#https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline

n = int(input())

steps = []

dp = [None for _ in range(n)]
for _ in range(n):
    steps.append(int(input()))

if n == 1:
    print(steps[0])
    quit()

if n == 2:
    print(sum(steps))
    quit()


dp[0] = steps[0]
dp[1] = steps[0] + steps[1]
dp[2] = max(steps[0] + steps[2],steps[1]+steps[2])

for i in range(3,n):
    cur = steps[i]
    prev = steps[i-1]

    dp[i] = max(dp[i-2]+ cur,dp[i-3] + prev + cur)
print(dp[-1])