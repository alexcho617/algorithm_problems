#https://www.acmicpc.net/problem/11501
import sys
input = sys.stdin.readline
t = int(input())

def solve(price: list, n: int):
    ans = 0
    max = -1
    for i in range(n-1,-1,-1):
        if price[i] > max:
            max = price[i]
        if price[i] < max:
            ans += (max - price[i])
    return ans

for _ in range(t):
    n = int(input())
    price = list(map(int,input().split()))
    print(solve(price,n))






# def solve(price: list, n: int):
#     ans = 0
#     ceiling = max(price)
#     # purchase = []
#     # for p in price:
#     for i in range(n):
#         if price[i] < ceiling:
#             # purchase.append(price[i])
#             ans += (ceiling - price[i])
#         #calculate revenue and reset ceiling
#         elif price[i] == ceiling:
#             # for pur in purchase:
#             #     ans += (ceiling - pur)
#             if i < n-1:
#                 ceiling = max(price[i+1:])

            

#     return ans