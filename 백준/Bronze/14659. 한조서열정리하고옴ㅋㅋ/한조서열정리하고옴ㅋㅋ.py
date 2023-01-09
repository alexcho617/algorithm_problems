#https://www.acmicpc.net/problem/14659
import sys 
input = sys.stdin.readline

n = int(input())
peaks = list(map(int,input().split()))

localCount, globalCount = 0,0
max = peaks[0]
for i in range(len(peaks)):
    curr = peaks[i]
    if curr < max:
        localCount += 1
    else:
        max = curr
        if globalCount < localCount:
            globalCount = localCount
        localCount = 0

if globalCount < localCount:
    globalCount = localCount    

print(globalCount)
