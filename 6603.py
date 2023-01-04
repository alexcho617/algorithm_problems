#https://www.acmicpc.net/problem/6603

from itertools import combinations
def solve(n:int, nums: list):
    comb = list(combinations(nums,6))
    # print(n)
    # print(nums)
    return comb


while(True):
    rawInput = input()
    if(rawInput == '0'):
        break
    lst = list(map(int,rawInput.split()))
    ans = solve(lst[0],lst[1:])
    for a in ans:
        print(*a)
    print()