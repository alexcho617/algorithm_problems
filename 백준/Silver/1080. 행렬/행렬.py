#https://www.acmicpc.net/problem/1080
n,m = map(int,input().split())
a,b=[],[]
ans = 0
for _ in range(n):
    a.append([int(c) for c in input()])
for _ in range(n):
    b.append([int(c) for c in input()])

#edge case
if  n < 3 or m < 3:
    if a == b:
        print(0)
    else:
        print(-1)
    quit()

#only check up to (n-3, m-3) for discrete flip
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            #flip 3 x 3
            ans += 1
            for k in range(3):
                for l in range(3):
                    if a[i+k][j+l] == 0:
                        a[i+k][j+l] = 1
                    else:
                        a[i+k][j+l] = 0
if a == b:
    print(ans)
else:
    print(-1)