#https://www.acmicpc.net/problem/14503
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph=[]
dir = 0
#N,E,S,W
dx = [0,-1,0,1]
dy = [-1,0,1,0]
ans = 0
for _ in range(n):
    graph.append(list(map(int,input().split())))



# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
# 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다. quit()
# 3. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
# 1. 반시계 방향으로 $90^\circ$ 회전한다.
# 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 3. 1번으로 돌아간다.
while 1:
    #clean
    if graph[r][c] == 0:
        graph[r][c] == 1
        ans += 1
    quit()
print(ans)