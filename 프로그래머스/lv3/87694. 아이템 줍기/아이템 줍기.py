from collections import deque

def printGraph(graph: list):
    for gra in graph:
        for g in gra:
            print('%2d' %g, end = ' ')
        print()

def bfs(graph,x1,y1,x2,y2):
    que = deque()
    start = (x1 * 2, y1 * 2)
    visited = set()
    gridSize = len(graph)
    visited.add(start)
    que.append(start)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while que:
        x,y = que.popleft()
        if x == x2 * 2 and y == y2 * 2:
            return graph[x][y] // 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < gridSize and 0 <= ny < gridSize and graph[nx][ny] == 1 and (nx,ny) not in visited:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))
                visited.add((nx,ny))
    return 0

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    gridSize = 102
    #n by n graph
    graph = [[-1 for _ in range(gridSize)] for _ in range(gridSize)]
    visited = [[False for _ in range(gridSize)] for _ in range(gridSize)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x : x*2, rec)
        #For Each Cell
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                #if cell is not visited
                if visited[i][j] == False:
                    #mark boundaries
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        graph[i][j] = 1
                        visited[i][j] = True
                    #mark insides
                    else:
                        graph[i][j] = 0
                        visited[i][j] = True
                #cell is visited
                else:
                    #ignore boundaries
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        continue
                    #mark insides nontheless
                    else:
                        graph[i][j] = 0
    answer = bfs(graph, characterX, characterY, itemX, itemY)
    return answer



