def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for idx, citation in enumerate(citations):
        print(idx, citation)
        if citation <= idx:
            return idx
    return len(citations)