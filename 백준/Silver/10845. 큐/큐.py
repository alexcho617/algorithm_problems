#https://www.acmicpc.net/problem/10845
from collections import deque
import sys
input = sys.stdin.readline
que = deque()

n = int(input())

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        que.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else: print(-1)

    elif cmd[0] == 'back':
        if que:
            print(que[-1])
        else: print(-1)