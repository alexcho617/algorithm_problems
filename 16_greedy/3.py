#https://www.acmicpc.net/problem/11399
#ATM

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
total = 0

for i in range(n):
    total = total + sum(arr)
    arr.pop()
print(total)