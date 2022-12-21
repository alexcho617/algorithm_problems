from itertools import combinations
#eucl
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
for _ in range(n):
    ans = 0
    num = list(map(int, input().split()))
    # num = num[1:]
    num.pop(0)
    num = list(combinations(num, 2))
    for n in num:
        ans += gcd(n[0],n[1])
    print(ans)