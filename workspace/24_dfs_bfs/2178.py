#https://www.acmicpc.net/problem/2178
import sys
from collections import deque

input = sys.stdin.readline
n,m = tuple(map(int,input().rsplit()))
graph = [list(map(int,list(input().rstrip())))for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)] # n*m graph init to false


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    que = deque([(x,y,1)])
    visited[x][y] = True
    while que:
        x,y,distance = que.popleft() #map tuple to x,y,distance
        if x == n-1 and y == m-1: #check escape condition
            print(distance)
            break
        else: #check four sides
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #boundary, wall condition check
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    que.append((nx,ny,distance + 1))


bfs(0,0)