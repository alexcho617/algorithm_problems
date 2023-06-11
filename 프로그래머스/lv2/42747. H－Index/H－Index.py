def solution(citations):
    answer = 0
    #내림차순 정렬을 하여 index 와 citation 값을 비교한다
    citations.sort(reverse = True)
    
    for idx, citation in enumerate(citations):
            #현재 인덱스가 인용된 수보다 같거나 큰 순간에 최대 H-Index가 된다.
            #내림 차순 정렬이기 때문에 그 밑으로의 논문들은 이미 인용된 수보다 낮다.
        if citation <= idx:
            return idx
    #만족하는 수가 없는 경우에 최대치 리턴
    return len(citations)