#https://www.acmicpc.net/problem/13305
n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
ans = distance[0] * price[0]
currentCost = price[0]

for i in range(1,len(distance)):
    if currentCost > price[i]:
        currentCost = price[i]
    temp = distance[i] * currentCost
    # print(temp)
    ans += temp

print(ans)