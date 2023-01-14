#https://www.acmicpc.net/problem/2847
import sys
input = sys.stdin.readline
n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))
ans = 0
curr = score[-1]
#iterate from behind
for i in range(n-2,-1,-1):
    if score[i] >= curr:
        diff = (score[i] - curr) + 1
        ans += diff
        score[i] -= diff
        curr = score[i]
    else:
        curr = score[i]
print(ans)