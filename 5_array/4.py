arr = []
#a = set() set will automatically filter redundant data

for i in range(10):
    num = int(input())
    rem = num%42
    if rem in arr:
        continue
    else:arr.append(rem)
print(len(arr))