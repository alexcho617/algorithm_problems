#https://www.acmicpc.net/problem/4963
import sys
input = sys.stdin.readline
from collections import deque

#this will find connected componenents
def bfs(graph,visited,x,y,w,h):
    que = deque([(x,y)])
    dx = [-1,1,0,0,-1,-1,1,1] #8 direcitons
    dy = [0,0,-1,1,-1,1,-1,1]
    # debugIter = 0
    while que:
        # print("DEBUG: ITER", debugIter)
        # debugIter += 1
        x,y = que.popleft()

        #escape condition when there are no lands nearby(1 not found)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            #check boundary
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                if graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    que.append((nx,ny))
        
    return 1

#this will iterate through unvisited points
def findIslands(graph,w,h):
    counter = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    #iterate
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == 1:
                # print("Call bfs")
                visited[i][j] = True
                counter += bfs(graph,visited,j,i,w,h)
                # print("Counter:",counter)
    return counter

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        quit()
    else:
        #get graph
        graph = []
        counter = 0
        for _ in range(h):
            graph.append(list(map(int,input().strip().split())))
        #solve
        print(findIslands(graph,w,h))
