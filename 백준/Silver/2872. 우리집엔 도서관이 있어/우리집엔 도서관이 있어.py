#https://www.acmicpc.net/problem/2872
from sys import stdin
n = int(stdin.readline())
book_lst = []
for i in range(n):
    book_lst.append(int(stdin.readline()))

counter = n
for book in book_lst[::-1]:
    if book == counter:
        counter -= 1
print(counter)