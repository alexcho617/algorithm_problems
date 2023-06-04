#uses recursive dfs to reach target but use memoization to imporve time complexity
def solution(numbers,target):
    answer = 0
    def dfs(numbers, target, curr, index):
        
        #escape end of tree
        if index == len(numbers):
            if curr == target:
                return 1
            else:
                return 0
        
        #recursive call
        count = dfs(numbers, target, curr + numbers[index], index + 1) + dfs(numbers, target, curr - numbers[index], index + 1)
        return count
    
    answer = dfs(numbers,target,0,0)
    return answer




















# def solution(numbers, target):
#     memo = {}

#     def dfs(nums, target, curr, idx):
#         if idx == len(nums):
#             return 1 if curr == target else 0

#         if (idx, curr) in memo:
#             return memo[(idx, curr)]

#         count = dfs(nums, target, curr + nums[idx], idx + 1) + dfs(nums, target, curr - nums[idx], idx + 1)
#         memo[(idx, curr)] = count

#         return count

#     answer = dfs(numbers, target, 0, 0)
#     return answer