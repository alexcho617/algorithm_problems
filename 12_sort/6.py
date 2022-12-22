# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기
import sys
n = int(sys.stdin.readline())
inputArr = []
for i in range(n):
    inputArr.append(list(map(int,sys.stdin.readline().split()))) #int로 해야 비교가 가능했음

inputArr.sort(key=lambda x: (x[0], x[1])) #
# sortedArr = sorted(inputArr)
# for i in sortedArr:
#     print(*i)
for a in inputArr:
    print(str(a[0]) + ' '+str(a[1]))

