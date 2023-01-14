#https://www.acmicpc.net/problem/16112
n,k = map(int, input().split())
exp = list(map(int, input().split()))
ans = 0
active = 0
exp.sort()
for e in exp:
    ans += (active * e)
    if active < k: active += 1

print(ans)