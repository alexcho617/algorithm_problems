#https://www.acmicpc.net/problem/1978
#소수 찾기
n = input()
numbers = list(map(int,input().split()))
count = 0


def checkPrime(n: int):
    if n == 1 : return False
    if n == 2 : return True
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

for number in numbers:
    
    if checkPrime(number) == True:
        count += 1
print(count)