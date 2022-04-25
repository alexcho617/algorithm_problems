#https://www.acmicpc.net/problem/2480
#주사위 세개
a,b,c = map(int, input().split())

if a != b and b != c:
    print(max(a,b,c) * 100)
    quit
elif a == b ==c:
    print(10000 + a * 1000)
    quit
elif a==b or a == c:
    print(1000 + a * 100)
    quit
elif b==c:
    print(1000 + b * 100)
    quit
