def self_number():
    li = []
    for i in range(1,10000):
        li.append(i + sum([int(j) for j in str(i)]))
    return li

li = self_number()
print(li)

#Way too slow. Time outs
# def digitSum(n): #return the sum of all the digits
#     sum = 0
#     while (n != 0):
#         sum = sum + n % 10
#         n = n // 10
#     return sum

# def isSelf(n):#iterate from 1 to n and add the sums. escape on match
#     for i in range(1,n+1):
#         if(i + digitSum(i) == n):
#             return False #meaning it can be generated
#     return True #meaning it cannot be generated

#for i in range(1,10000):
    # if isSelf(i) == True:
    #     print(i)