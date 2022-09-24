#https://www.acmicpc.net/problem/1541

#- 로 나눔
#덩어리들 합산
#- 연산
eqs = input().split('-')
nums = []

for eq in eqs:
    sum = 0
    temp = eq.split('+')
    for j in temp:
        sum += int(j)
    nums.append(sum)



ans = nums[0]
for i in range(1,len(nums)):
    ans -= nums[i]
print(ans)


# nums = []
# ops = []

# text = input()
# func = text.split('+')
# #re를 쓰면 한번에 + - 둘 다 파싱 가능하다는데 잘 안되서 일단 따로따로
# #num parse
# for f in func:
#     s = map(int,f.split('-'))
#     nums += s

# #back to string for using eval()
# nums = list(map(str,nums))

# #ops parse
# for t in text:
#     if t == '+' or t == '-':
#         ops.append(t)

# equation = ''
# prevAns = 0
# currAns = 0

# prevOp = ''
# currOp = ''

# for i in range(len(nums)-1):
    
#     #base case: a +/- b
#     if i == 0:
#         currOp = ops[i]

#         equation = nums[0] + currOp + nums[1]
#         currAns = eval(equation)
#         prevAns = currAns
#         prevOp = currOp
#         equation = ''

#     #normal case: a +/- b +/- c
#     else:
#         currOp = ops[i]

#         #이전 연산자가 - 이고 현재 연산자가 +인 경우 현재 연산자를 -로 바꿔서 계산한다.
#         if prevOp == '-' and currOp == '+':
#             equation += str(prevAns) + '-' + nums[i+1]
#         else:
#             equation += str(prevAns) + currOp + nums[i+1]
        
#         currAns = eval(equation)
#         prevAns = currAns
#         prevOp = currOp
#         equation = ''
# print(currAns)