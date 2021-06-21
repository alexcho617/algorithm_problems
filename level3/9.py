import sys
n,x = map(int,sys.stdin.readline().split())

inputs = sys.stdin.readline().split()
for item in inputs:
    if int(item) < x:
        print(item, end= ' ')

# import sys
# n,x = map(int,sys.stdin.readline().split())

# inputs = sys.stdin.readline().split()
# result = []
# for item in inputs:
#     if int(item) < x:
#         result.append(item)
# for item in result:
#     i = 0
#     if  i < len(result)-1:
#         print(item,end=' ')
#         i+=1
#     elif i == len(result)-1:
#         print(item, end='')