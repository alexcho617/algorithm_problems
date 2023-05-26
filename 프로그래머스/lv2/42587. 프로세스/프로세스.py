from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    target = priorities[location]
    counter = 0
        #돌리면서 location(인덱스)를 맞춰주는것이 중요하다    
    while que:
        print(location)
        #1.대기 프로세스 꺼냄
        curr = que[0]
        #2.상위 프로세스 존재 -> 큐 뒤로 보냄
        if curr < max(que):
            que.rotate(-1)
            #location 처리: 내 로케이션이 0 이었을 경우 맨뒤로, 
            if location == 0:
                location = len(que) - 1 
            #아닌 경우 -1    
            else:                    
                location -= 1
        #3.상위 프로세스 -> 실행 -> 큐에서 꺼냄
        else:
            que.popleft()
            counter += 1
            if location == 0:
                return counter
            else:
                location -= 1