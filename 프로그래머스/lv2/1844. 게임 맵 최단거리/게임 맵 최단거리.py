from collections import deque
def solution(maps):
    answer = 0
    def bfs():
        que = deque([(0,0)])
        # visited = set() #use set (y,x)
        # visited.add((0,0))
        dx = [1,-1,0,0]#동서남북  
        dy = [0,0,1,-1]
        counter = 0
        while que:
            y,x = que.popleft()
            counter +=1
            if y == len(maps)-1 and x == len(maps[0])-1:
                print("reached target:",counter)
                return maps[-1][-1]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                    if maps[ny][nx] == 1:
                        print("hit:", ny,nx)
                        maps[ny][nx] = maps[y][x] + 1
                        que.append((ny,nx))
                        # visited.add((ny,nx))
        return -1
    answer = bfs()
    
    
    return answer