#https://www.acmicpc.net/problem/1535

import sys
input = sys.stdin.readline
n = int(input())
cost = [0] + list(map(int,input().split()))
value = [0] + list(map(int,input().split()))

#dp will save largest value earned for each health point upto 100
dp = [[0] * 100 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(100):
        #cannot fit in the bag
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]
        
        #can fit the current item in the bag
        else:
            #choose larger between previous value or add the current
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + value[i])
    # print("DP i :",i,*dp,sep='\n')

print(dp[n][99])