#https://www.acmicpc.net/problem/2490
for _ in range(3):
    arr = list(map(int,input().split()))
    ans = arr.count(0)
    if ans == 0:
        print('E')
    elif ans == 1:
        print('A')
    elif ans == 2:
        print('B')
    elif ans == 3:
        print('C')
    elif ans == 4:
        print('D')
