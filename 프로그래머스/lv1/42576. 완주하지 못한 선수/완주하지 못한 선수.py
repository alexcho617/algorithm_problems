from collections import defaultdict
def solution(participant, completion):
    #make hash
    hash = defaultdict(int)
    #count names
    for part in participant:
        hash[part] += 1
    #eliminate completion
    for comp in completion:
        hash[comp] -= 1
        if hash[comp] == 0:
            del hash[comp]
    result = list(hash.items())
    return result[0][0]