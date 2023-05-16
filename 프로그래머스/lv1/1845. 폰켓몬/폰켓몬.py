def solution(nums):
    #make hash
    hash = {}
    #put array into hash and count
    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    #answer is length of hash keys
    answer = min(len(hash.keys()),len(nums)/2)
    return answer