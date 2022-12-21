#https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())
card_deq = deque([i for i in range(1,n+1)]) #1~n initizliae

while len(card_deq) != 1:
    card_deq.popleft()
    card_deq.rotate(-1)
print(card_deq[0])

