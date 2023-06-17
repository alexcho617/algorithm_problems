def solution(s):
    nums = list(map(int,s.split()))
    nums.sort()
    answer = ''
    answer += str(nums[0])
    answer += ' '
    answer += str(nums[-1])
    return answer