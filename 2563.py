#https://www.acmicpc.net/problem/2563
n = int(input())
paper = []
rows, cols = 100,100
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    paper.append(col)

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
answer = 0
for row in paper:
    answer += row.count(1)
print(answer)