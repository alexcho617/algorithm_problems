def solution(numbers, target):
    memo = {}

    def dfs(nums, target, curr, idx):
        if idx == len(nums):
            return 1 if curr == target else 0

        if (idx, curr) in memo:
            return memo[(idx, curr)]

        count = dfs(nums, target, curr + nums[idx], idx + 1) + dfs(nums, target, curr - nums[idx], idx + 1)
        memo[(idx, curr)] = count

        return count

    answer = dfs(numbers, target, 0, 0)
    return answer
