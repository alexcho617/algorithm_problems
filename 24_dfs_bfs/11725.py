#https://www.acmicpc.net/problem/11725
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

que = deque()
visited = [False for _ in range(n+1)]

#get graph from 1 to n, exclude index 0
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#array to hold parental info
parents = [None for _ in range(n+1)]
# print(graph)
#bfs store parent info
que.append(1)
visited[1] = True

while que:
    # print(que)
    currentParent = que.popleft()
    # print("CP",currentParent)
    visited[currentParent] = True
    if graph[currentParent]:
        children = graph[currentParent]
        # print(children)
        for c in children:
            if visited[c] == False:                
                parents[c] = currentParent
            if graph[c] and visited[c] == False:
                que.append(c)

print(*parents[2:],sep='\n')