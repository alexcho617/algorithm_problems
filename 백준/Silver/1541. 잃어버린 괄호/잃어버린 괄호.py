#https://www.acmicpc.net/problem/1541

#- 기준으로 나눔
eqs = input().split('-')
nums = []

#+덩어리들 합산
for eq in eqs:
    sum = 0
    temp = eq.split('+')
    for j in temp:
        sum += int(j)
    nums.append(sum)


#- 연산
ans = nums[0] # 앞 숫자 초기화
for i in range(1,len(nums)):
    ans -= nums[i]
print(ans)

