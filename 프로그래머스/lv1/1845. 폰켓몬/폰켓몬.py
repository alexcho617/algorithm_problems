from collections import defaultdict
def solution(nums):
    #make hash
    hash = defaultdict(int)
    #put array into hash and count
    for num in nums:
        hash[num] += 1
        
    #answer is length of hash keys
    answer = min(len(hash.keys()),len(nums)/2)
    return answer