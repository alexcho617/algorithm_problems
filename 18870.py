#https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
numSet = sorted(list(set(nums)))

#dicitonary 사용하여 look up table 만들어 o(n)으로 해결한다.
dic = {numSet[i] : i for i in range(len(numSet))}

for i in nums: #O(n)
    print(dic[i], end = ' ') #O(1)
