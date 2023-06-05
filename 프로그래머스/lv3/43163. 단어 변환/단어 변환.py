#단어는 한알파벳 차이가 나는 단어로만 변환 가능
from collections import deque
def solution(begin, target, words):
    wordLen = len(begin)
    que = deque([[begin,0]])
    visited = []
    visited.append(begin)

    if target not in words:
        return 0
    
    while que:
        curr, depth = que.popleft()
        print(curr, depth)
        if curr == target:
            return depth
        for word in words:
            counter = 0
            for i in range(wordLen):
                if curr[i] != word[i]:
                    counter += 1
            if counter == 1 and word not in visited:
                que.append([word,depth + 1])
                visited.append(word)