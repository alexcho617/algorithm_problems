#https://www.acmicpc.net/problem/11722
import sys
input = sys.stdin.readline

n = int(input())
a = [1001] + list(map(int,input().split()))
dp = [0] + [ 1 for _ in range(n)]

# print(a)
for i in range(1, n+1):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
print(max(dp))