# https://www.acmicpc.net/problem/1181
import sys
input = sys.stdin.readline
n = int(input())
words = []
for _ in range(n):
    word = input().rstrip()
    if word not in words:
        words.append(word)
words.sort(key=lambda x: (len(x), x))
for w in words:
    print(w)
