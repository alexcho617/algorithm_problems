from itertools import combinations

n,m = map(int, input().split())
arr = [i+1 for i in range(n)]

com = list(combinations(arr,m))
for c in com:
    print(*c)