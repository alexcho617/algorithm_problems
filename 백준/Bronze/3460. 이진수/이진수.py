# https://www.acmicpc.net/problem/3460
import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ans = []
    biN = bin(n)
    biN = biN[2:]
    biN = biN[::-1]
    for i in range(len(biN)):
        if biN[i] == '1':
            ans.append(i)
    print(*ans)
