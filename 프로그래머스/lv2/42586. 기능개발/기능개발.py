from collections import deque

def solution(progresses, speeds):
    que = deque(progresses)
    speedQue = deque(speeds)
    answer = []
    temp = 0
    while que:
        #keep progresses and speeds in sync while popping
        for i in range(len(que)):
            que[i] += speedQue[i]
        while que and que[0] >= 100:
            que.popleft()
            speedQue.popleft()
            temp += 1
        if temp != 0: answer.append(temp)
        temp = 0

    #각 배포마다 몇개의 기능이 배포되는지를 리턴 []
    return answer