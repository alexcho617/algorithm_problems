#https://www.acmicpc.net/problem/17298
#오큰수
import sys

n = int(input())
numList = list(map(int,input().split()))
stack = []
answer = [-1] * n

stack.append(0)

for i in range(1,n):
    #last index of stack and current number comparison
    while stack and numList[stack[-1]] < numList[i]:#RBN is found
        #put the RBN at the answer index
        answer[stack.pop()] = numList[i]
    #have to add index anyways to find other RBN
    stack.append(i)
print(*answer)