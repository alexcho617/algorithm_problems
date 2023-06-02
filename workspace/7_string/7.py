#https://www.acmicpc.net/problem/2908

def inverter(number):
    invertedNumber = ''
    for i in range(len(number)-1,-1, -1):
        invertedNumber += number[i]
    return int(invertedNumber)
a,b = input().split(' ')

# a = inverter(a)
# b = inverter(b)
a = int(a[::-1])
b = int(b[::-1])


if(a > b):
    print(a)
else: print(b)