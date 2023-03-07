#https://www.acmicpc.net/problem/2468
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = []
ans = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
MAX = max(map(max, graph))

#count connected componenets
def islandCounter(level: int):
    que = deque()
    counter = 0
    points = []
    visited = set()
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    #filter lower ones
    for i in range(n):
        for j in range(n):
            if graph[i][j] > level:
                points.append((i,j))
    #nodes higher than current level are candidates
    # print("POINTS:",points)
    for point in points:
        if point not in visited:
            visited.add(point)
            que.append(point)
            counter += 1
        while que:
            p = que.popleft()
            x = p[1]
            y = p[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                currentlyVisiting = (ny,nx)
                if 0<= nx < n and 0<= ny < n and graph[ny][nx] > level and currentlyVisiting not in visited:
                    visited.add(currentlyVisiting)
                    que.append(currentlyVisiting)
    return counter



for level in range(MAX + 1):
    ans.append(islandCounter(level))
    # print("CURRENTLY:",level,ans)
print(max(ans))