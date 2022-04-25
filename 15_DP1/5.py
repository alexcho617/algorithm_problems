#https://www.acmicpc.net/problem/1149
#RGB거리
from operator import indexOf


n = int(input())
arrInput = []
for i in range(n):
    arr = list(map(int,input().split()))
    arrInput.append(arr)

totalCost = 0
previousIndex = -1
for arr in arrInput:
    # print(arr)
    currentIndex = indexOf(arr,min(arr))
    # print(currentIndex)
    if  currentIndex != previousIndex:
        currentCost = min(arr)
        previousIndex = currentIndex
        # print(currentCost)
    else:
        arr[currentIndex] = 9999
        # print(arr)
        currentCost = min(arr)
        currentIndex = indexOf(arr,min(arr))
        previousIndex = currentIndex
        # print(currentCost)

    totalCost += currentCost
    # print('totalCost:',totalCost)
print(totalCost)
    