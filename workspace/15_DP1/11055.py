# https://www.acmicpc.net/problem/11055
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
dp = [None for _ in range(n)]

# base cases
dp[0] = a[0]
if n == 1:
    print(dp[0])
    quit()
# iterative cases
for i in range(1, n):
    curr = a[i]
    tempMax = 0
    #증가 수열이 조건이기 때문에 curr 보다 작은 수가 포함 된 수열의 합(dp) 중에서 제일 큰  값을 찾는것임. 
    for j in range(i): 
        if a[j] < curr:
            if dp[j] > tempMax:
                tempMax = dp[j]
    dp[i] = tempMax + curr #그 숫자에 자신을 더함

print(max(dp))
