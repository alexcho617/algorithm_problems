from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i] == False:
            bfs(n,computers,i,visited)
            answer += 1
    return answer


def bfs(nodes,computers,curr,visited):
    que = deque()
    que.append(curr)
    visited[curr] = True
    while que:
        curr = que.popleft()
        visited[curr] = True
        for node in range(nodes):
            if curr != node and computers[curr][node] == 1:
                if visited[node] == False:
                    que.append(node)