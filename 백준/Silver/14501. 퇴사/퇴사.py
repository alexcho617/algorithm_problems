# https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline
n = int(input())
counsels = []
for _ in range(n):
    counsels.append(list(map(int,input().split())))
dp = [0 for _ in range(n+1)]

#init first iteration
counsels.append([0,0]) # for last index

#start from behind
for i in range(n-1,-1,-1):
    if counsels[i][0] + i <= n: #include if they are same
        #perform optimization
        #since dp is passed down, compare dp[i+1](previous)dp with counsel[i][1] + dp[i+ offset]
        dp[i] = max(dp[i+1], dp[i + counsels[i][0]] + counsels[i][1])
    else:
        #take previous item
        dp[i] = dp[i+1]
print(max(dp))

