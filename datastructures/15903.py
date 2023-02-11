#https://www.acmicpc.net/problem/15903
n,m = map(int,input().split())
cards = list(map(int,input().split()))

for _ in range(m):
    cards.sort()
    minSum = (cards[0] + cards [1])
    cards[0] = minSum
    cards[1] = minSum
print(sum(cards))

