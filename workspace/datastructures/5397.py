#https://www.acmicpc.net/problem/5397
import sys
input = sys.stdin.readline
n = (int(input()))

for _ in range(n):
    left = []
    right = []
    pw = input().rstrip()
    for p in pw:
        if p == "<":
            if left:
                temp = left.pop()
                right.append(temp)
        elif p == ">":
            if right:
                temp = right.pop()
                left.append(temp)
        elif p == "-":
            if left:
                left.pop()
        else:
            left.append(p)
    ans = left + right[::-1]
    print(*ans, sep = '')