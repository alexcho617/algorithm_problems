#https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

t = int(input())

def solution(row1: list,row2: list, n: int):
    dp1 = [0 for _ in range(n+1)]
    dp2 = [0 for _ in range(n+1)]
    dp1[1] = row1[1]
    dp2[1] = row2[1]

    if n == 1:
        return max(dp1[1], dp2[1])
    
    dp1[2] = row2[1] + row1[2]
    dp2[2] = row1[1] + row2[2]

    for i in range(3, n+1):
        dp1[i] = max(dp1[i-2],dp2[i-2],dp2[i-1]) + row1[i]
        dp2[i] = max(dp2[i-2],dp1[i-2],dp1[i-1]) + row2[i]
    return max(dp1[-1],dp2[-1])


for _ in range(t):
    #init
    n = int(input())    
    firstRow = [0] + list(map(int,input().split()))
    secondRow = [0] + list(map(int,input().split()))
    
    print(solution(firstRow,secondRow,n))