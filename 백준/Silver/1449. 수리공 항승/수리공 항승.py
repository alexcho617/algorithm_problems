#https://www.acmicpc.net/problem/1449
n,l = map(int,input().split())
holes = list(map(int,input().split()))
ans = 0
startTape, endTape = 0,0
holes.sort()
for h in holes:
    if h not in range(startTape,endTape):
        ans += 1
        startTape = h
        endTape = startTape + l
print(ans)