# https://www.acmicpc.net/problem/10678
from collections import deque

# get graphs for elsie and bessie

edge1 = {}
edge2 = {}
n, m = map(int, input().split())
for i in range(1, n):
    edge1[i] = []
    edge2[i] = []

for _ in range(m):
    a, b, c, d = map(int, input().split())
    edge1[a].append([b, c])
    edge2[a].append([b, d])

# perform dfs


def dfs(graph, dist, cur, sums):
    global n
    if cur == n:     # arrive at n, save accumulated sums
        dist.append(sums)
        return
    for adjNodes in graph[cur]: # otherwise continue search
        dfs(graph, dist, adjNodes[0], sums + adjNodes[1])

    return dist
   
# compare and get results
dist1 = []
dist2 = []

dist1 = dfs(edge1, dist1, 1, 0)
dist2 = dfs(edge2, dist2, 1, 0)
dist1.sort()
print(dist1,dist2)
for d in dist1:
    if d in dist2:
        print(d)
        quit()
print("IMPOSSIBLE")

    

