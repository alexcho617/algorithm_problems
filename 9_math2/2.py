#https://www.acmicpc.net/problem/2581
#소수

m = int(input())
n = int(input())

primeList = []

def checkPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num % i == 0: return False
    return True

for num in range(m,n+1):
    if checkPrime(num):
        primeList.append(num)

if(primeList):
    print(sum(primeList))
    print(min(primeList))
#no prime numbers case
else:print(-1)