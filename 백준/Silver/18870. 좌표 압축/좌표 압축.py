#https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
numSet = sorted(list(set(nums)))

dic = {numSet[i] : i for i in range(len(numSet))}
for i in nums:
    print(dic[i], end = ' ')
