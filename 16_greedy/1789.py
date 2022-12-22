#https://www.acmicpc.net/problem/1789
#수들의 합                                  
from re import S


s = int(input())

ans = 0
interval = 1
while s > 0:
    #뻈는데
    s -= interval
    #남은 값이 인터벌 보다 크다
    if(s > interval):
        interval += 1
        ans += 1
    #남은 값이 인터벌 보다 작으면 1씩 
    else:
        #이게 굳이 필요 없고 그냥 이 지점에서 카운트 1 증가 시키면 끝임
        #남은값을 인터벌로 나눠서 딱 떨어질떄까지 인터벌을 늘린다
        #이 경우에 엔서 값을 1 줄여야 한다.
        while s % interval != 0:
            interval += 1
            #탈출시 인터벌이 포함 된다
        ans += 1
print(ans)

