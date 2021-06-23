arr = []
for i in range(0,9):
    n = int(input())
    arr.append(n)
print(max(arr))
print(arr.index(max(arr))+1)