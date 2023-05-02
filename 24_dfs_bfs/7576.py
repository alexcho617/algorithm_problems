# https://www.acmicpc.net/problem/7576
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
ripe = []
ans = 0
visited = [[False for _ in range(n)] for _ in range(m)]
for _ in range(m):
    graph.append(list(map(int, input().split())))

# multiple starting points.
for j in range(m):
    for i in range(n):
        if graph[j][i] == 1:
            ripe.append([j, i])

# handle edge case
ripeExist = False
for g in graph:
    if 1 in g:
        ripeExist = True
if ripeExist == False:
    print(-1)
    quit()

# one queue, multiple riped tomatoes to start
que = deque(ripe)
for r in ripe:
    visited[r[0]][r[1]] = True

# iterate using BFS
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
while que:
    y, x = que.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n and visited[ny][nx] == False and graph[ny][nx] == 0:
            que.append([ny, nx])
            visited[ny][nx] = True
            graph[ny][nx] = graph[y][x] + 1


ans = max(map(max, graph)) - 1


# handle impossible edge case here
for g in graph:
    if 0 in g:
        print(-1)
        quit()
else:
    print(ans)
