#https://www.acmicpc.net/problem/15649
from itertools import permutations
n,m = map(int,input().split())

arr = [int(i+1) for i in range(n)]
perm = list(permutations(arr,m))
for p in perm:
    print(*p)