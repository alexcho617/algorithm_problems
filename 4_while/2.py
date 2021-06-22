def digtize(num):
    array = []
    ones = num % 10
    tens = int((num - ones) /10)
    array.append(tens)
    array.append(ones)
    return array

num = int(input())
original = num
count = 1
while True:
    arr = digtize(num)
    sum = arr[0] + arr[1]
    arr2 = digtize(sum)
    newnum = arr[1]*10 + arr2[1]
    
    if newnum != original:
        num = newnum
        count += 1
    else:
        print(count)
        break
