#https://www.acmicpc.net/problem/11051
import math
n,k = map(int,input().split())
print(math.comb(n,k)%10007)