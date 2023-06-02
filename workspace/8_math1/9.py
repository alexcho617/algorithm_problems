#https://www.acmicpc.net/problem/1011
#Fly me to the Alpha Centauri
import sys

n = int(sys.stdin.readline())
for _ in range(n):

    x, y = map(int,input().split())
    distance = y - x
    count = 0
    position = 0
    speed = 0
    interval = [speed - 1, speed, speed + 1]
    while(distance > 0):

        #남은 거리가 절반 이하면 가속
        if (position < (distance / 2)):
            speed += 1
        #남은 거리가 절반 이상이면 감속
        else:
            speed -= 1
        distance -= speed
        count += 1
        print(f'distance = {distance} speed = {speed}, count = {count}')
    print(count)
