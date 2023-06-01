from itertools import permutations

def solution(k, dungeons):
    answer = -1
    save = k
    #방문 순서가 중요하기 때문에 순열nPr 사용
    perms = list(permutations(dungeons, len(dungeons)))
    #각 순열들을 직접 방문하면서 맥스 값 기록
    for perm in perms:
        k = save
        # print(perm)
        temp = 0
        for dungeon in perm:
            if k >= dungeon[0]:
                temp += 1
                k -= dungeon[1]
        # print(temp)
        answer = max(temp,answer)
    
    return answer