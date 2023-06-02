#https://www.acmicpc.net/problem/1260
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph: dict, root: int):
    que = deque([root])
    visited = []
    while que:
        n = que.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                que += sorted(list(graph[n] - set(visited)))
    return visited

def dfs(graph: dict, root: int):
    stack = [root]
    visited = []
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                stack += sorted(list(graph[n] - set(visited)), reverse= True)
    return visited


n,m,v = map(int,input().split())
graph = {}
for _ in range(m):
    a,b = map(int,input().split())
    if a not in graph:
        graph[a] = {b} #set
    else:
        graph[a].add(b) #set add
    
    if b not in graph:
        graph[b] = {a} #set
    else:
        graph[b].add(a) #set add

print(*dfs(graph,v))
print(*bfs(graph,v))