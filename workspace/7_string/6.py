# #https://www.acmicpc.net/problem/1152
# str = input()

# if(str[0] == ' ' and len(str) == 1):
#     print(0)
#     exit
# elif(str[0] == ' ' and str[-1]== ' '):
#     str = str[1:-1]
#     print(len(list(str.split(' '))))
#     exit
# elif(str[0] == ' '):
#     str = str[1:]
#     print(len(list(str.split(' '))))
#     exit
# elif(str[-1]== ' '):
#     str = str[:-1]
#     print(len(list(str.split(' '))))
#     exit
# else:
#     print(len(list(str.split(' '))))
print(len(input().split()))