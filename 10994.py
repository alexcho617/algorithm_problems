# https://www.acmicpc.net/problem/10994

import sys
sys.setrecursionlimit(10**6)


def appendStars(n,factor):
    if n == 1:
        return ['*']
    stars = appendStars(n-1,factor)
    temp = []
    factor = 4*(n-1) + 1

    temp.append("*"*factor)
    temp.append("*"+" "*(factor-2) + "*")


    for s in stars:
        temp.append("* "+s+" *")

    temp.append("*"+" "*(factor-2) + "*")
    temp.append("*"*factor)

    return temp


n = int(sys.stdin.readline().strip())
print('\n'.join(appendStars(n,1)))
