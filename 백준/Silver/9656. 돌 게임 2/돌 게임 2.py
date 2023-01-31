#https://www.acmicpc.net/problem/9656
n = int(input())
dp = [None for _ in range(n+1)]
dp[:4] = "","CY","SK","CY"
for i in range(4,n+1):
    a = dp[i-1]
    b = dp[i-3]

    if a == b:
        if a == "SK":
            dp[i] = "CY"
        else:
            dp[i] = "SK"
print(dp[n])