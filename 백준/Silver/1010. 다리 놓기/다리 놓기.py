#https://www.acmicpc.net/problem/1010
import sys
input = sys.stdin.readline
import math


t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    print(math.comb(m,n))