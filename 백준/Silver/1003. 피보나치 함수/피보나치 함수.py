#https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline

table = [[] for _ in range(41)]
table[0] = [1,0]
table[1] = [0,1]

def lookUp(n):
    if table[n]:
        return table[n]
    else:
        return False

def solve(n: int):
    global table

    if lookUp(n):
        return lookUp(n)
    else:
        table[n] = [solve(n-1)[0] + solve(n-2)[0],solve(n-1)[1] + solve(n-2)[1]]
    return table[n]


t = int(input())
for _ in range(t):
    print(*solve(int(input())))