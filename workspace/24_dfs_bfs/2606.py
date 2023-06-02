#https://www.acmicpc.net/problem/2606
from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph,root):
    que = deque([root])
    visited = []
    while que:
        n = que.popleft()
        if n not in visited:
            visited.append(n)
            que += graph[n] - set(visited)
    
    return len(visited) - 1


c = int(input())
e = int(input())

graph = [set([]) for _ in range(c+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

print(bfs(graph,1))
