#https://www.acmicpc.net/problem/10250
#ACM 호텔


n = int(input())
for _ in range(n):    
    h,w,n = map(int,input().split())
    
    if n % h == 0:
        room = n//h
        floor = h
    else:
        room = n // h + 1
        floor = n % h
    print(f'{floor * 100 + room}') #formated string literals python 3.6