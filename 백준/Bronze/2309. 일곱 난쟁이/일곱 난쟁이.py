#https://www.acmicpc.net/problem/2309
from itertools import combinations

dwarf = []
ans = []
for _ in range(9):
    dwarf.append(int(input()))
comb = list(combinations(dwarf, 7))
for c in comb:
    if(sum(c) == 100):
        ans = list(c)
        break
ans.sort()
for a in ans:
    print(a)