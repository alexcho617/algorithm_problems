#https://www.acmicpc.net/problem/1966
# from collections import deque
import sys
input = sys.stdin.readline

# def maxOfQueue(que:deque):
#     list = []
#     for q in que:
#         list.append(q)

#     return max(list)

def solve(n:int, index:int, priorityList:list):
    counter = 0
    flag = True
    # que = deque(priorityList)
    while flag:
        curr = priorityList[0]
        # m = maxOfQueue(que)
        if curr == max(priorityList):
            counter += 1

            if index == 0:
                flag == False
                return counter
            else:
                index -= 1
                priorityList.pop(0)
            
        else:
            temp = priorityList.pop(0)
            priorityList.append(temp)
            if index == 0:
                index = len(priorityList) - 1
            else:
                index -= 1
        # print("index:",index)
        # print("counter:",counter)
        # print("priority:",priorityList)

    return counter

for _ in range(int(input())):
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    print(solve(n,m,p))