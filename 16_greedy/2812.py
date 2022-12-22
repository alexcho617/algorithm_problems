#https://www.acmicpc.net/problem/2812

from operator import indexOf
import sys
n,k = map(int, input().split())
num = sys.stdin.readline()

for _ in range(k):
    diff = []
    #calculate difference
    for i in range(len(num)-2):
        curr = int(num[i])
        next = int(num[i+1])
        diff.append(next-curr)
    #delimiter
    diff.append(-999)

    #get first occurance of max
    idx = indexOf(diff,max(diff))
    #remove it
    newNum = num[:idx] + num[idx+1:]
    num = newNum

print(newNum)