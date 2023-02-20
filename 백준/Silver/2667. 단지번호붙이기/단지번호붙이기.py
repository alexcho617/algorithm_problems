#https://www.acmicpc.net/problem/2667
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
graph = [list(map(int,list(input().strip()))) for _ in range(n)]
points = []
visited = []
ans = []

def bfs(point: list):
    que = deque([point])
    count = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while que:
        p = que.popleft()
        x = p[1]
        y = p[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1 and [ny,nx] not in visited:
                visited.append([ny,nx])
                que.append([ny,nx])
                count += 1
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            points.append([i,j])

for point in points:
    if point not in visited:
        visited.append(point)
        ans.append(bfs(point))
ans.sort()
print(len(ans))
for a in ans:
    print(a)