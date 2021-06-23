a = int(input())
b = int(input())
c = int(input())

sum = str(a*b*c)
for i in range(10):
    count = sum.count(str(i)) 
    print(count)

# for i in sum:
#     if i == "0":
#         arr[0] += 1
#     elif i == "1":
#         arr[1] += 1
#     elif i == "2":
#         arr[2] += 1
#     elif i == "3":
#         arr [3] += 1
#     elif i == "4":
#         arr [4] += 1
#     elif i == "5":
#         arr[5] += 1
#     elif i == "6":
#         arr[6] += 1
#     elif i == "7":
#         arr[7] += 1
#     elif i == "8":
#         arr[8] += 1
#     elif i == "9":
#         arr[9] += 1
# for i in arr:
#     print(i)