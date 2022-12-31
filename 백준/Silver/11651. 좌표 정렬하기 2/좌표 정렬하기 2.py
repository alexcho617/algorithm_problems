#https://www.acmicpc.net/problem/11651
import sys
input = sys.stdin.readline
n = int(input())
nums =[]
for _ in range(n):
    x,y = map(int,input().split())
    nums.append([y,x])
nums = sorted(nums)

for y,x in nums:
    print(x,y)