#https://www.acmicpc.net/problem/1712
#손익분기점
#A = Fixed, B = Per Cost, C = Sales
a,b,c = map(int,(input().split()))
if ( b >= c):
    print(-1)
else:
    print(int(a/(c-b)) + 1)

#문제를 잘 읽자... 쉬운건데 인풋 순서 착각해서 오래 걸림..