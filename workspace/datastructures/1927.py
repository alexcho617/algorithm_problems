#https://www.acmicpc.net/problem/1927
import sys, heapq
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)