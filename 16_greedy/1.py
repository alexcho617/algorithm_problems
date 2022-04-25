#https://www.acmicpc.net/problem/11047
n,k = map(int,input().split(' '))
count: int = 0
sum = 0
coinList = []
for _ in range(n):
    coinList.append(int(input()))

while(k != 0):
    #get greedy coin
    for _ in range(len(coinList)):
        localMax = max(coinList)
        if(localMax > k):
            coinList.remove(localMax)
    #get coin count
    localCount = (k // max(coinList))
    #multiply get coin value 
    #subtract it from k
    k = k - (localCount * max(coinList))
    #add to count
    count += localCount
    localCount = 0

# print('n = ', n)
# print('k = ', k)
# print('coinList = ',coinList)
# print('localCount = ',localCount)
print(count)