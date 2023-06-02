#https://www.acmicpc.net/problem/2675
t = int(input())
for _ in range(t):
    r,string = list(input().split(' '))
    for s in string:
        for _ in range(int(r)):
            print(s, end = '')
    print()
