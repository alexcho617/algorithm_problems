#https://www.acmicpc.net/problem/11726
import sys
input = sys.stdin.readline
n = int(input())
dp = [None for _ in range(n+1)]
dp[0:3] = 1,1,2

def lookUp(n: int):
    global dp
    if dp[n] != None:
        return dp[n]
    else:
        return False


def solve(n: int):
    global dp
    ans = 0
    if lookUp(n):
        return dp[n]
    else:
        #even
        if n % 2 == 0:
            dp[n] = solve((n//2)) ** 2 + solve((n//2 - 1)) ** 2
            return dp[n]
        #odd
        else:
            dp[n] = (solve((n//2)) * solve((n//2 + 1))) + (solve((n//2 -1))* solve(n//2))
            return dp[n]
print(solve(n) % 10007)