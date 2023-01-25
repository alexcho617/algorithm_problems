#https://www.acmicpc.net/problem/1699
import sys
import math
input = sys.stdin.readline
n = int(input())

#dp will store min number of squares to make n
dp = [i for i in range(n+1)]

for i in range(3,n+1):
    if float(math.sqrt(i)).is_integer():
        dp[i] = 1
        continue
    #iterate until i**2 < n
    j = 1
    while(True):
        if j*j > i:
            break
        #assign dp[i] = min
        else:
            if dp[i] > dp[i-j*j] + 1:
                dp[i] = 1 + dp[i-j*j]
        j += 1
print(dp[n])