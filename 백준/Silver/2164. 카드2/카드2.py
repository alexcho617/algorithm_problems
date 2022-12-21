#6-1. 카드2	https://www.acmicpc.net/problem/2164
from collections import deque
n = int(input())
queue = deque(maxlen=n)

#assign
for i in range(1,n+1):
    queue.append(i)


while(True):
    #escape condition
    if len(queue)  == 1:
        print(queue[0])
        break
    
    #task
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)