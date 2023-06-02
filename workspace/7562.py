# https://www.acmicpc.net/problem/7562
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())


def solve(l: int, src: list, dest: list):
    # init graph, queue
    graph = [[0 for _ in range(l)] for _ in range(l)]
    que = deque()
    count = 0
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    visited = [[False for _ in range(l)] for _ in range(l)]
    ans = 0
    # from the source do bfs
    que.append(src)
    # print('DEBUG', que)
    while que:
        visited[src[0]][src[1]] = True
        # curr = que.popleft()
        # print('DEBUG CURR', curr)
        y,x = que.popleft()

        
        # traverse
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[ny][nx] == False:
                visited[ny][nx] = True
                que.append([ny, nx])
                graph[ny][nx] = graph[y][x] + 1
                # if curr is at dest, return count
                if [ny, nx] == dest:
                    ans = graph[ny][nx]
    # print(graph)
    return ans


for _ in range(t):
    l = int(input())
    src = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    # print('DEBUG',l,src,dest)
    print(solve(l, src, dest))
