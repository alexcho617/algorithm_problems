#https://www.acmicpc.net/problem/11286
import sys, heapq
input = sys.stdin.readline
minHeap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if minHeap:
            print(heapq.heappop(minHeap)[1])
        else:
            print(0)
    else:
        heapq.heappush(minHeap,(abs(x),x))