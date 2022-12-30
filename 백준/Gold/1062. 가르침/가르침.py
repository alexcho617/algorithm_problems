# https://www.acmicpc.net/problem/1062
from itertools import combinations
import sys
n, k = map(int, input().split())
ans = 0
prefix = {'a', 'n', 't', 'i', 'c'}

remain = set(chr(i) for i in range(97, 123)) - prefix
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]


def countReadableWords(words, learned):
    cnt = 0
    for word in words:
        canRead = 1
        for w in word:
            if learned[ord(w)] == 0:
                canRead = 0
                break
        if canRead == 1:
            cnt += 1
    return cnt


if k >= 5:
    learned = [0] * 123
    for x in prefix:
        learned[ord(x)] = 1
    for teach in list(combinations(remain, k-5)):
        for t in teach:
            learned[ord(t)] = 1
        cnt = countReadableWords(words, learned)

        if cnt > ans:
            ans = cnt
        for t in teach:
            learned[ord(t)] = 0
    print(ans)
else:
    print(0)