#https://www.acmicpc.net/problem/5430
import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    popRight = False
    errorFlag = False
    ops = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    arr = arr[1:-1].split(',')
    # print('arr',arr, len(arr))

    if arr == ['']: arr = []#0 edge case
    que = deque(arr)
    # print('que',que)
    #R is reverse, D is pop
    for op in ops:
        if op == 'R':
            popRight = not popRight
        elif op == 'D':
            if que:
                if popRight:
                    que.pop()
                else:
                    que.popleft()
            else:
                errorFlag = True
                break
    if errorFlag:
        print('error')
    else:
        arr = list(que)
        # print('arr',arr)
        if popRight:
            #reverse print
            arr = arr[::-1]
        print('[', end='')
        print(*arr,sep=',',end='')
        print(']')