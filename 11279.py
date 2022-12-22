#https://www.acmicpc.net/problem/11279
import sys, heapq
heap = []

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline()) * -1 #-1를 곱하여서 min heap을 max heap처럼 사용 할 수 있다. 가장 큰수가 가장 작은 수가 되는것
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, n)