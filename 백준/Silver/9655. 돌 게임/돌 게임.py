#https://www.acmicpc.net/problem/9655
n = int(input())
dp = [None for _ in range(n+1)]

dp[:4] = "","SK","CY","SK"

for i in range(4,n+1):
    a = dp[i-1]
    b = dp[i-3]

    val = ""
    if a == 'SK':
        val = "CY"
    else:
        val = "SK"

    dp[i] = val
print(dp[n])