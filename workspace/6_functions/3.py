#https://www.acmicpc.net/problem/1065

def hansu(num):
    count = 0
    for n in range(1, num+1):
        if n < 100:
            count += 1
        else:
            numString = list(map(int,str(n)))
            if numString [0] - numString[1] == numString[1] - numString[2]:
                count += 1
    return count
num = int(input())
print(hansu(num))