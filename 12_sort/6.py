#https://www.acmicpc.net/problem/11650
#좌표 정렬하기
import sys
n = int(sys.stdin.readline())
inputArr = []
for i in range(n):
    inputArr.append(input().split())

sortedArr = sorted(inputArr)
for i in sortedArr:
    print(*i)