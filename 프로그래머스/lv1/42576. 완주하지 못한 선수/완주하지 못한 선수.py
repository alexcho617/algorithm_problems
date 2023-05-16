def solution(participant, completion):
    #make hash
    hash = {}
    #count names
    for part in participant:
        if part in hash:
            hash[part] += 1
        else:
            hash[part] = 1
    #eliminate completion
    for comp in completion:
        hash[comp] -= 1
    #return non 0 name
    for h in hash:
        if hash[h] != 0:
            return h