#https://www.acmicpc.net/problem/1965
import sys
input = sys.stdin.readline
n = int(input())
boxes = list(map(int,input().split()))
dp = [ 1 for _ in range(n)]

for i in range(1,n):
    curr = boxes[i]
    #get max dp value within smaller boxes
    temp = 0
    for j in range(i):
        if boxes[j] < curr:
            #iterate and find max
            if dp[j] > temp:
                temp = dp[j]
    dp[i] = temp + 1
print(max(dp))


