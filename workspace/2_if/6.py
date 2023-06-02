#https://www.acmicpc.net/step/4
#오븐 시계

hour,minute = map(int,input().split())
time = int(input())
h = time // 60
m = time % 60

hour += h
minute += m
if minute > 59:
    minute -= 60
    hour += 1
print(hour % 24, minute)

