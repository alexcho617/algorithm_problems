#https://www.acmicpc.net/problem/2847
n = int(input())
scores = []
count = 0
for _ in range(n):
    scores.append(int(input()))
max = scores[-1]

for i in range(n-1,0,-1):
    if scores[i-1] >= scores[i]:
        while scores[i-1] >= scores[i]:
            scores[i-1] -= 1
            count += 1
print(count)