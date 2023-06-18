from collections import defaultdict
def solution(clothes):
    hash = defaultdict(int)
    #hash
    for name, kind in clothes:
        hash[kind] += 1
        # if kind in hash:
        #     hash[kind] += 1
        # else:
        #     hash[kind] = 1
    print(hash)
    #number of items + hash value multplication
    values = hash.values()
    answer = 1
    
    for value in values:
        answer *= (value+1)
        
    return answer-1