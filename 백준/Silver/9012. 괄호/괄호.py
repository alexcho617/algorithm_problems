#https://www.acmicpc.net/problem/9012
import sys
input = sys.stdin.readline
n = int(input())


def solve(vps: str):
    stack = []
    for v in vps:
        if v == '(':
            stack.append(v)
        elif v == ')':
            if stack:
                stack.pop()
            else:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"


for _ in range(n):
    print(solve(input()))