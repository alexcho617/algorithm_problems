#https://www.acmicpc.net/problem/1012
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def printGraph(graph: list):
    print(*graph,sep='\n')

def solve(cabbages: list, graph: list):
    counter = 0
    visited = []
    for cabbage in cabbages:
        if cabbage not in visited:
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            # print("cabbage", cabbage)
            que = deque([cabbage])
            # print("que", que)
            visited.append(cabbage)
            #bfs
            while que:
                x,y = que.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and [nx,ny] not in visited and graph[ny][nx] == 1:
                        # print("got a cabbage at:",nx,ny)
                        que.append([nx,ny])
                        visited.append([nx,ny])
            counter += 1
    return counter

for _ in range(t):
    cabbages = []
    visited = []

    #solve
    m,n,k = map(int,input().split())
    #create graph
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        cabbages.append([x,y])
        graph[y][x] = 1
    print(solve(cabbages,graph))

    # printGraph(graph)