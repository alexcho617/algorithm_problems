#https://www.acmicpc.net/problem/14916

from unittest import case


n = int(input())
f = 0
t = 0
ans = 0

#when n is greater than 5
if n >= 5:
    a = n // 5
    remain = n % 5
    b = remain // 2
    #divisible by 5
    if remain == 0:
        ans = a
    elif remain == 1 or remain == 3:
        a -= 1
        remain += 5
        b = remain // 2
        ans = a + b
    elif remain == 2 or remain == 4:
        b = remain // 2
        ans = a+b
#when n is lesser than 5
else:
    if n == 1 or 3:
        ans = -1
    if n == 0:
        ans = 0
    if n == 4:
        ans = 2
    if n == 2:
        ans = 1
# print(ans, a, b, remain)
print(ans)
