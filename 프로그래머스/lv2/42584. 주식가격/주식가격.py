def solution(prices):
    #상한가로 가정하고 초기화
    answer = [i for i in range(len(prices) - 1,-1,-1)]
    stack = [0]
    for i in range(1,len(prices)):
        while stack and prices[stack[-1]] > prices[i]: #현재 스택의 맨 위의 값과 현재 값을 비교했을때 하한가인 경우
            upperBound = stack.pop()
            answer[upperBound] = i - upperBound #현재 날에서 
        stack.append(i)
            
    return answer