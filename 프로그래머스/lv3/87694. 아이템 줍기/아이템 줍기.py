from collections import deque
def printGraph(graph: list):
    graph = graph[::-1]
    for gra in graph:
        for g in gra:
            print('%2d' %g, end = ' ')
        print()

def bfs(graph,x1,y1,x2,y2):
    que = deque()
    start = (y1 * 2, x1 * 2)
    visited = set()
    gridSize = len(graph)
    visited.add(start)
    que.append(start)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while que:
        y,x = que.popleft()
        # print("Curr:", x,y)
        if x == x2 * 2 and y == y2 * 2:
            # print("target found at:" "x=", x,"y=", y)
            # printGraph(graph)
            return graph[y][x] // 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print("visiting:", nx,ny)
            if 0 <= nx < gridSize and 0 <= ny < gridSize and graph[ny][nx] == 1 and (ny,nx) not in visited:
                graph[ny][nx] = graph[y][x] + 1
                que.append((ny,nx))
                visited.add((ny,nx))
    return 0
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    gridSize = 102
    #n by n graph
    graph = [[0 for _ in range(gridSize)] for _ in range(gridSize)]
    visited = [[False for _ in range(gridSize)] for _ in range(gridSize)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x : x*2, rec)
        #For Each Cell
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                #if cell is not visited
                if visited[j][i] == False:
                    #mark boundaries
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        graph[j][i] = 1
                        visited[j][i] = True
                    #mark insides
                    else:
                        graph[j][i] = 0
                        visited[j][i] = True
                #cell is visited
                else:
                    #ignore boundaries
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        continue
                    #mark insides nontheless
                    else:
                        graph[j][i] = 0
    # printGraph(graph)
        
    answer = bfs(graph, characterX, characterY, itemX, itemY)
    return answer